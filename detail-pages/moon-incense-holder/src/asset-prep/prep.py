import sys, numpy as np, cv2
from PIL import Image, ImageFilter
src, out = sys.argv[1], sys.argv[2]
im = cv2.cvtColor(cv2.imread(src), cv2.COLOR_BGR2RGB)

def save(arr, name, alpha=None):
    if alpha is None:
        Image.fromarray(arr).save(f"{out}/{name}")
    else:
        rgba = np.dstack([arr, alpha])
        Image.fromarray(rgba, "RGBA").save(f"{out}/{name}")

# ---- A: full box, cut out for dark hero ----
A = im[1235:1800, 0:1336].copy()
g = A.astype(np.int16)
notwhite = ((g.min(axis=2) < 232) | ((g.max(axis=2) - g.min(axis=2)) > 18)).astype(np.uint8)
n, lab, stats, _ = cv2.connectedComponentsWithStats(notwhite, 8)
big = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
mask = (lab == big).astype(np.uint8) * 255
# fill holes
ff = mask.copy(); h, w = ff.shape
cv2.floodFill(ff, np.zeros((h + 2, w + 2), np.uint8), (0, 0), 255)
mask = mask | cv2.bitwise_not(ff)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
mask = cv2.erode(mask, np.ones((3, 3), np.uint8), 1)
mask = cv2.GaussianBlur(mask, (5, 5), 0)
ys, xs = np.where(mask > 10)
y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
save(A[y0:y1, x0:x1], "A_cut.png", mask[y0:y1, x0:x1])
save(A, "A_full.png")

# ---- B: close-up front (white bg) ----
B = im[2900:3420, 0:1336].copy()
save(B, "B_closeup.png")
# detail circles: sun + crescent moon
def circle(cx, cy, r, name):
    crop = im[cy - r:cy + r, cx - r:cx + r].copy()
    save(crop, name)
circle(797, 3257, 150, "B_sun.png")
circle(345, 3240, 130, "B_moon.png")

# ---- C: open lid; remove the white overlay label on the end piece ----
C = im[4700:5860, 0:1336].copy()
cy0 = 4700
reg = (slice(5075 - cy0, 5185 - cy0), slice(965, 1175))
sub = C[reg].astype(np.int16)
lum = sub.mean(axis=2)
m = np.zeros(C.shape[:2], np.uint8)
m[reg] = (lum > 150).astype(np.uint8) * 255
m = cv2.dilate(m, np.ones((9, 9), np.uint8), 1)
Cbgr = cv2.cvtColor(C, cv2.COLOR_RGB2BGR)
Cin = cv2.inpaint(Cbgr, m, 9, cv2.INPAINT_TELEA)
C = cv2.cvtColor(Cin, cv2.COLOR_BGR2RGB)
save(C, "C_open.png")

# ---- D: drawer ----
D = im[6600:7340, 0:1336].copy()
save(D, "D_drawer.png")
print("ok", A.shape, (y1 - y0, x1 - x0), B.shape, C.shape, D.shape)
