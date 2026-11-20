import sys
from PIL import Image
src_x4, work, dst = sys.argv[1], sys.argv[2], sys.argv[3]
im = Image.open(src_x4).convert("RGB")
im.crop((0, 6600, 1336, 7440)).save(f"{dst}/photo-drawer.jpg", quality=92, subsampling=0)
for name, out in [("B_closeup.png", "photo-closeup.jpg"), ("C_open.png", "photo-open.jpg"),
                  ("B_sun.png", "detail-sun.jpg"), ("B_moon.png", "detail-moon.jpg")]:
    Image.open(f"{work}/{name}").convert("RGB").save(f"{dst}/{out}", quality=92, subsampling=0)
Image.open(f"{work}/A_cut.png").save(f"{dst}/hero-cutout.png", optimize=True)
print("exported")
