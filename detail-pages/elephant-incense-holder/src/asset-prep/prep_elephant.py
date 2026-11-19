import sys, numpy as np, cv2
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
im = np.asarray(Image.open(src).convert("RGB"))
g = im.astype(np.int16)

# ---- hero cutout (largest non-white component) ----
notwhite = ((g.min(axis=2) < 236) | ((g.max(axis=2) - g.min(axis=2)) > 16)).astype(np.uint8)
n, lab, st, _ = cv2.connectedComponentsWithStats(notwhite, 8)
big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
mask = (lab == big).astype(np.uint8) * 255
ff = mask.copy(); h, w = ff.shape
cv2.floodFill(ff, np.zeros((h + 2, w + 2), np.uint8), (0, 0), 255)
mask = mask | cv2.bitwise_not(ff)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
mask = cv2.erode(mask, np.ones((3, 3), np.uint8), 1)
mask = cv2.GaussianBlur(mask, (5, 5), 0)
ys, xs = np.where(mask > 10)
y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
print("product bbox", x0, y0, x1, y1)
Image.fromarray(np.dstack([im[y0:y1, x0:x1], mask[y0:y1, x0:x1]]), "RGBA").save(f"{out}/hero-cutout.png", optimize=True)

# ---- gold inlay mask -> elephant silhouette (for icons) ----
R, G, B = g[..., 0], g[..., 1], g[..., 2]
gold = ((R > 170) & (G > 135) & (R - B > 55) & (mask > 128)).astype(np.uint8) * 255
gold = cv2.morphologyEx(gold, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
n, lab, st, cen = cv2.connectedComponentsWithStats(gold, 8)
order = np.argsort(-st[1:, cv2.CC_STAT_AREA])[:5] + 1
for i in order:
    print("gold comp", st[i].tolist())
el = order[0]
x, y, ww, hh = st[el, :4]
sil = (lab[y:y + hh, x:x + ww] == el).astype(np.uint8) * 255
ff = np.pad(sil, 2).copy(); cv2.floodFill(ff, None, (0, 0), 255)
sil = sil | cv2.bitwise_not(ff)[2:-2, 2:-2]
sil = cv2.resize(sil, (ww * 4, hh * 4), interpolation=cv2.INTER_CUBIC)
sil = cv2.GaussianBlur(sil, (0, 0), 2.2)
sil = np.where(sil > 127, 255, 0).astype(np.uint8)
sil = cv2.GaussianBlur(sil, (3, 3), 0)
pad = 12
sil = np.pad(sil, pad)
gold_rgb = np.zeros(sil.shape + (3,), np.uint8); gold_rgb[:] = (201, 162, 91)
Image.fromarray(np.dstack([gold_rgb, sil]), "RGBA").save(f"{out}/elephant-gold.png")
Image.fromarray(np.dstack([np.full(sil.shape + (3,), 255, np.uint8), sil]), "RGBA").save(f"{out}/elephant-mask.png")
np.save(f"{out}/_gold_stats.npy", st)
