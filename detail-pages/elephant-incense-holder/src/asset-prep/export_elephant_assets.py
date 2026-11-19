import sys
from PIL import Image
src, work, dst = sys.argv[1], sys.argv[2], sys.argv[3]
im = Image.open(src).convert("RGB")
im.crop((180, 690, 1620, 1470)).save(f"{dst}/photo-closeup.jpg", quality=92, subsampling=0)
im.crop((872 - 92, 1182 - 92, 872 + 92, 1182 + 92)).save(f"{dst}/detail-elephant.jpg", quality=93, subsampling=0)
im.crop((850 - 105, 930 - 105, 850 + 105, 930 + 105)).save(f"{dst}/detail-pattern.jpg", quality=93, subsampling=0)
cut = Image.open(f"{work}/hero-cutout.png")
w = 1360
cut.resize((w, round(cut.height * w / cut.width)), Image.LANCZOS).save(f"{dst}/hero-cutout.png", optimize=True)
print("exported", cut.size)
