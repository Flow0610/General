import sys, numpy as np
from PIL import Image
work, dst = sys.argv[1], sys.argv[2]
cut = Image.open(f"{work}/box_cutout.png")
cut.resize((1300, round(cut.height * 1300 / cut.width)), Image.LANCZOS).save(f"{dst}/box-cutout.png", optimize=True)
packs = Image.fromarray(np.load(f"{work}/packs_rot.npy"))
packs.crop((300, 270, 1912, 1420)).save(f"{dst}/packs.jpg", quality=92, subsampling=0)
for k in ["lavender", "moon-dreams", "rain-forest", "white-musk", "coconut", "baby-powder"]:
    Image.open(f"{work}/out/scent-{k}.jpg").save(f"{dst}/scent-{k}.jpg", quality=92, subsampling=0)
box = Image.open(f"{work}/box_retouched.jpg")
box.crop((360, 410, 1210, 1130)).save(f"{dst}/pkg-window.jpg", quality=92, subsampling=0)     # window with 6 packs
box.crop((175, 180, 395, 400)).save(f"{dst}/pkg-logo.jpg", quality=93, subsampling=0)          # brand logo + sprig
box.crop((1206, 318, 1462, 574)).save(f"{dst}/pkg-jasmine.jpg", quality=93, subsampling=0)    # jasmine garland
box.save(f"{dst}/box-retouched.jpg", quality=92, subsampling=0)
print("exported")
