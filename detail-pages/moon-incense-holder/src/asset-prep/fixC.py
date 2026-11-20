import sys, numpy as np, cv2
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
im = cv2.imread(src)  # BGR
C = im[4662:5860, 0:1336].copy()
cy0 = 4662
y0, y1, x0, x1 = 5068 - cy0, 5192 - cy0, 960, 1180
sub = C[y0:y1, x0:x1].astype(np.int16)
lum = sub.mean(axis=2)
# local wood baseline: median of region
base = np.median(lum)
m = np.zeros(C.shape[:2], np.uint8)
m[y0:y1, x0:x1] = ((lum - base) > 22).astype(np.uint8) * 255
m = cv2.dilate(m, np.ones((15, 15), np.uint8), 1)
inp = cv2.inpaint(C, m, 15, cv2.INPAINT_NS)
# add matching grain inside the mask so it doesn't look smeared
rng = np.random.default_rng(3)
noise = cv2.GaussianBlur(rng.normal(0, 6, C.shape[:2]).astype(np.float32), (0, 0), 1.2)
soft = cv2.GaussianBlur(m.astype(np.float32) / 255, (0, 0), 4)[..., None]
res = inp.astype(np.float32) + noise[..., None] * soft
C = np.clip(res, 0, 255).astype(np.uint8)
cv2.imwrite(f"{out}/C_open.png", C)
# detail circles (square crops; masked to circles in CSS)
def sq(cx, cy, r, name):
    cv2.imwrite(f"{out}/{name}", im[cy - r:cy + r, cx - r:cx + r])
sq(797, 3252, 92, "B_sun.png")
sq(340, 3230, 72, "B_moon.png")
print("ok", int(m.sum() / 255))
