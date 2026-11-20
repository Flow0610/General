import sys
from PIL import Image, ImageDraw, ImageFont
work, src_dir, dst = sys.argv[1], sys.argv[2], sys.argv[3]
box = Image.open(f"{work}/box_retouched.jpg"); box.save(f"{dst}/box_retouched.jpg", quality=95, subsampling=0)
cut = Image.open(f"{work}/box_cutout.png"); cut.save(f"{dst}/box_cutout.png", optimize=True)
packs = Image.open(f"{work}/packs_rot_full.jpg").crop((230, 220, 1980, 1470)); packs.save(f"{dst}/packs_retouched.jpg", quality=95, subsampling=0)
# square white-background image (e.g. for a main thumbnail), product ~86% of the frame
sq = Image.new("RGB", (1000, 1000), "white")
s = 860 / max(cut.size); c2 = cut.resize((round(cut.width * s), round(cut.height * s)), Image.LANCZOS)
sq.paste(c2, ((1000 - c2.width) // 2, (1000 - c2.height) // 2), c2); sq.save(f"{dst}/box_square_1000.jpg", quality=95, subsampling=0)
# before / after sheet
def fit(im, w):
    return im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
b0 = fit(Image.open(f"{src_dir}/5.jpg").convert("RGB"), 760); b1 = fit(box.convert("RGB"), 760)
p0 = fit(Image.open(f"{src_dir}/6.jpg").convert("RGB"), 760); p1 = fit(packs.convert("RGB"), 760)
H = 70 + max(b0.height, b1.height) + 40 + max(p0.height, p1.height) + 30
sheet = Image.new("RGB", (760 * 2 + 60, H), (244, 247, 246)); d = ImageDraw.Draw(sheet)
try:
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
except OSError:
    f = ImageFont.load_default()
d.text((20, 22), "BEFORE", fill=(90, 90, 90), font=f); d.text((800, 22), "AFTER", fill=(31, 138, 124), font=f)
sheet.paste(b0, (20, 70)); sheet.paste(b1, (800, 70))
y = 70 + max(b0.height, b1.height) + 40
sheet.paste(p0, (20, y)); sheet.paste(p1, (800, y))
sheet.save(f"{dst}/before_after.jpg", quality=90)
print("saved", box.size, cut.size, packs.size, sheet.size)
