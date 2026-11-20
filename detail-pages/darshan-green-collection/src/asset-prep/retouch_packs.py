import sys, numpy as np, cv2
from PIL import Image
sys.path.insert(0, sys.argv[3])
from retouch_common import fit_illumination, flat_field, tone, sharpen
src, out = sys.argv[1], sys.argv[2]
img = np.asarray(Image.open(src).convert("RGB")).astype(np.float32)
h, w, _ = img.shape

# 1) lighting: fit on the outer frame first, then refine on everything that is not product/shadow
frame = np.zeros((h, w), np.uint8); frame[:, :260] = 255; frame[:, w - 110:] = 255; frame[:230] = 255; frame[h - 70:] = 255
f0 = fit_illumination(img, frame, deg=2)
ratio = img / np.maximum(f0, 1)
obj = (np.abs(ratio - 1).max(2) > 0.07).astype(np.uint8) * 255
obj = cv2.morphologyEx(obj, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
n, lab, st, _ = cv2.connectedComponentsWithStats(obj, 8)
keep = [i for i in range(1, n) if st[i, cv2.CC_STAT_AREA] > 4000]
obj = np.isin(lab, keep).astype(np.uint8) * 255
bgm = cv2.bitwise_not(cv2.dilate(obj, np.ones((61, 61), np.uint8)))
field = fit_illumination(img, bgm, deg=3)
corr = flat_field(img, field, target=247.0)
print("bg corners after:", [corr[y0:y0+60, x0:x0+60].reshape(-1, 3).mean(0).round(1).tolist()
      for y0, x0 in [(10, 10), (10, w - 70), (h - 70, 10), (h - 70, w - 70)]])

# 2) level: angle from long near-horizontal edges inside the packs
gray = cv2.cvtColor(np.clip(corr, 0, 255).astype(np.uint8), cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(gray, 60, 160)
edges[obj == 0] = 0
lines = cv2.HoughLinesP(edges, 1, np.pi / 1800, threshold=200, minLineLength=500, maxLineGap=15)
angs = []
for l in np.asarray(lines).reshape(-1, 4):
    x1, y1, x2, y2 = l
    a = np.degrees(np.arctan2(y2 - y1, x2 - x1))
    if abs(a) < 5: angs.append(a)
ang = float(np.median(angs)); print("lines", len(angs), "median angle %.3f deg" % ang)
M = cv2.getRotationMatrix2D((w / 2, h / 2), ang, 1.0)
rot = np.clip(cv2.warpAffine(corr, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE), 0, 255)
robj = cv2.warpAffine(obj, M, (w, h), flags=cv2.INTER_NEAREST)

# 3) tone, sharpen, crop
rot = sharpen(tone(rot, contrast=0.10, sat=1.06), sigma=1.0, amount=0.5)
ys, xs = np.where(robj > 0)
print("objects bbox", xs.min(), ys.min(), xs.max(), ys.max())
np.save(f"{out}/packs_rot.npy", rot.astype(np.uint8))
Image.fromarray(rot.astype(np.uint8)).save(f"{out}/packs_rot_full.jpg", quality=95, subsampling=0)
cv2.imwrite(f"{out}/packs_obj.png", robj)
