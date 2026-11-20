import sys, json, numpy as np, cv2
from PIL import Image
sys.path.insert(0, sys.argv[3])
from retouch_common import fit_illumination, flat_field, tone, sharpen
src, out = sys.argv[1], sys.argv[2]
img = np.asarray(Image.open(src).convert("RGB")).astype(np.float32)
h, w, _ = img.shape
hsv = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_RGB2HSV)
H, S, V = hsv[..., 0].astype(int), hsv[..., 1].astype(int), hsv[..., 2].astype(int)
teal = ((H >= 68) & (H <= 108) & (S > 38) & (V > 60)).astype(np.uint8) * 255
teal = cv2.morphologyEx(teal, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
n, lab, st, _ = cv2.connectedComponentsWithStats(teal, 8)
big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
box = (lab == big).astype(np.uint8) * 255
ff = box.copy(); cv2.floodFill(ff, np.zeros((h + 2, w + 2), np.uint8), (0, 0), 255)
box = box | cv2.bitwise_not(ff)
box = cv2.morphologyEx(box, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

# --- geometry: left/right/bottom edges of the body, shoulders for the top edge
rows = np.where(box.any(1))[0]; cols = np.where(box.any(0))[0]
print("mask bbox", cols.min(), rows.min(), cols.max(), rows.max())
widths = np.array([(box[y] > 0).sum() for y in range(h)])
left = np.array([np.argmax(box[y] > 0) if widths[y] else -1 for y in range(h)])
right = np.array([w - 1 - np.argmax(box[y, ::-1] > 0) if widths[y] else -1 for y in range(h)])
body_rows = np.where(widths > 0.97 * widths.max())[0]
yb0, yb1 = body_rows.min(), body_rows.max()
print("body rows", yb0, yb1)
ys = np.arange(yb0 + 20, yb1 - 20)
la = np.polyfit(ys, left[ys], 1); ra = np.polyfit(ys, right[ys], 1)
xs = np.arange(left[yb1 - 30] + 40, right[yb1 - 30] - 40)
bottom = np.array([h - 1 - np.argmax(box[::-1, x] > 0) for x in xs])
ba = np.polyfit(xs, bottom, 1)
# top edge of the body at the two shoulders
xl = np.arange(int(np.polyval(la, yb0)) + 6, int(np.polyval(la, yb0)) + 22)
xr = np.arange(int(np.polyval(ra, yb0)) - 22, int(np.polyval(ra, yb0)) - 6)
tl = np.median([np.argmax(box[:, x] > 0) for x in xl]); tr = np.median([np.argmax(box[:, x] > 0) for x in xr])
ta = np.polyfit([xl.mean(), xr.mean()], [tl, tr], 1)
print("left x=a*y+b", la, "right", ra, "bottom y=a*x+b", ba, "top", ta)
print("tilt deg  left %.3f right %.3f bottom %.3f top %.3f" % tuple(np.degrees(np.arctan(v)) for v in (la[0], ra[0], ba[0], ta[0])))
json.dump({"left": la.tolist(), "right": ra.tolist(), "bottom": ba.tolist(), "top": ta.tolist()}, open(f"{out}/box_edges.json", "w"))
cv2.imwrite(f"{out}/box_mask_raw.png", box)

# ---- 1) flat-field: fit the lighting on the background, divide it out (fixes warm cast + left/right falloff)
bg = cv2.bitwise_not(cv2.dilate(box, np.ones((151, 151), np.uint8)))
field = fit_illumination(img, bg, deg=3)
corr = flat_field(img, field, target=247.0)
print("bg after flat-field (TL,TR,BL,BR):", [corr[y0:y0+80, x0:x0+80].reshape(-1, 3).mean(0).round(1).tolist()
      for y0, x0 in [(10, 10), (10, w - 90), (h - 90, 10), (h - 90, w - 90)]])

# ---- 2) tone + color
corr = tone(corr, contrast=0.10, sat=1.07)
corr = sharpen(corr, sigma=1.0, amount=0.5)

# ---- 3) perspective: map the 4 body corners to an exact rectangle
def inter(xline, yline):  # x = a*y+b  and  y = c*x+d
    a, b = xline; c, d = yline
    y = (c * b + d) / (1 - c * a); return [a * y + b, y]
TL, TR = inter(la, ta), inter(ra, ta); BL, BR = inter(la, ba), inter(ra, ba)
W = (np.hypot(*np.subtract(TR, TL)) + np.hypot(*np.subtract(BR, BL))) / 2
Hh = (np.hypot(*np.subtract(BL, TL)) + np.hypot(*np.subtract(BR, TR))) / 2
src_pts = np.float32([TL, TR, BR, BL]); dst_pts = np.float32([[0, 0], [W, 0], [W, Hh], [0, Hh]]) + np.float32([TL])
Mh = cv2.getPerspectiveTransform(src_pts, dst_pts)
warped = np.clip(cv2.warpPerspective(corr, Mh, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE), 0, 255)
flatlab = cv2.cvtColor(np.clip(flat_field(img, field, 247.0), 0, 255).astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
A_, B_ = flatlab[..., 1] - 128, flatlab[..., 2] - 128
chroma = np.hypot(A_, B_)
m2 = ((A_ < -5) & (flatlab[..., 0] < 246)).astype(np.uint8) * 255   # teal a*~-10; bg/shadow a*~0..+2 (neutral-warm)
m2 = cv2.morphologyEx(m2, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
n, lab2, st2, _ = cv2.connectedComponentsWithStats(m2, 8)
m2 = (lab2 == 1 + np.argmax(st2[1:, cv2.CC_STAT_AREA])).astype(np.uint8) * 255
body = np.zeros_like(m2); cv2.fillPoly(body, [np.int32(np.round([TL, TR, BR, BL]))], 255)
m2 = m2 | body
ff = m2.copy(); cv2.floodFill(ff, np.zeros((h + 2, w + 2), np.uint8), (0, 0), 255)
holes = cv2.bitwise_not(ff)
n, hl, hst, hcen = cv2.connectedComponentsWithStats(holes, 8)
filled = m2 | holes
for i in range(1, n):
    x_, y_, ww_, hh_, area = hst[i]
    if 2500 < area < 15000 and ww_ > 2.5 * hh_ and hcen[i][1] < TL[1]:   # the die-cut hang slot
        filled[hl == i] = 0
        print("hang slot kept open", hst[i].tolist())
filled = cv2.morphologyEx(filled, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
# smooth the die-cut hanger outline (pale print made the threshold edge wavy); keep the body rectangle crisp
smooth = (cv2.GaussianBlur(filled.astype(np.float32), (0, 0), 2.0) > 127).astype(np.uint8) * 255
filled = np.where(body > 0, 255, smooth).astype(np.uint8)
cv2.imwrite(f"{out}/box_mask.png", filled)
wmask = cv2.warpPerspective(filled, Mh, (w, h), flags=cv2.INTER_LINEAR)
print("corners", np.round([TL, TR, BR, BL], 1).tolist(), "-> rect", round(W, 1), round(Hh, 1))

# ---- 4) outputs: full retouched photo (natural shadow kept) + cutout
ys_, xs_ = np.where(wmask > 128)
x0, x1, y0, y1 = xs_.min(), xs_.max() + 1, ys_.min(), ys_.max() + 1
pad = 70
full = warped[max(y0 - pad, 0):min(y1 + pad, h), max(x0 - pad, 0):min(x1 + pad, w)]
Image.fromarray(full.astype(np.uint8)).save(f"{out}/box_retouched.jpg", quality=95, subsampling=0)
alpha = cv2.erode(wmask, np.ones((3, 3), np.uint8), 1)
alpha = cv2.GaussianBlur(alpha, (0, 0), 0.9)
rgba = np.dstack([warped.astype(np.uint8), alpha])[y0:y1, x0:x1]
Image.fromarray(rgba, "RGBA").save(f"{out}/box_cutout.png", optimize=True)
print("cutout size", rgba.shape[1], rgba.shape[0])
