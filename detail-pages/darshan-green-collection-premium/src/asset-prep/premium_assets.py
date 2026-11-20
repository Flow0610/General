"""Premium-page assets, built only from the retouched photos of the v1 page.

- scent cards : pack artwork tiles upscaled 4x with Real-ESRGAN (ncnn, CPU), saved at 2x display size
- color fields: each pack's own artwork, cover-resized, heavily blurred, softly graded + film grain
- box details : jasmine pattern / logo crops of the retouched box, upscaled 4x
Usage: python -I premium_assets.py <v1_assets_dir> <out_assets_dir> <realesrgan_model_dir>
"""
import sys, numpy as np, cv2, ncnn
from PIL import Image

V1, OUT, MODEL = sys.argv[1], sys.argv[2], sys.argv[3]
PAPER = np.array([245, 241, 234], np.float32)

net = ncnn.Net(); net.opt.use_vulkan_compute = False; net.opt.num_threads = 4
net.load_param(f"{MODEL}/realesrgan-x4plus.param"); net.load_model(f"{MODEL}/realesrgan-x4plus.bin")


def esrgan_x4(rgb, T=128, P=10):
    img = rgb.astype(np.float32) / 255.0
    H, W, _ = img.shape
    out = np.zeros((H * 4, W * 4, 3), np.float32)
    for y in range(0, H, T):
        for x in range(0, W, T):
            y0, x0, y1, x1 = max(y - P, 0), max(x - P, 0), min(y + T + P, H), min(x + T + P, W)
            tile = np.ascontiguousarray(img[y0:y1, x0:x1].transpose(2, 0, 1))   # keep alive: ncnn.Mat wraps this buffer
            mat = ncnn.Mat(tile)
            ex = net.create_extractor()
            ex.input("data", mat)
            _, o = ex.extract("output")
            o = np.array(o).transpose(1, 2, 0)
            th, tw = (min(y + T, H) - y) * 4, (min(x + T, W) - x) * 4
            out[y * 4:y * 4 + th, x * 4:x * 4 + tw] = o[(y - y0) * 4:(y - y0) * 4 + th, (x - x0) * 4:(x - x0) * 4 + tw]
    return (np.clip(out, 0, 1) * 255 + .5).astype(np.uint8)


def save_resized(rgb, w, path, q=92):
    im = Image.fromarray(rgb)
    im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(path, quality=q, subsampling=0)


def grain(shape, sigma, seed):
    rng = np.random.default_rng(seed)
    n = rng.normal(0, sigma, shape[:2]).astype(np.float32)
    return cv2.GaussianBlur(n, (0, 0), 0.6)[..., None]


def color_field(rgb, w, h, seed, blur=30, desat=0.22, lift=0.10):
    src = rgb.astype(np.float32)
    s = max(w / src.shape[1], h / src.shape[0]) * 1.15
    big = cv2.resize(src, (round(src.shape[1] * s), round(src.shape[0] * s)), interpolation=cv2.INTER_CUBIC)
    y0, x0 = (big.shape[0] - h) // 2, (big.shape[1] - w) // 2
    f = cv2.GaussianBlur(big[y0:y0 + h, x0:x0 + w], (0, 0), blur)
    f = cv2.GaussianBlur(f, (0, 0), blur / 2)                       # smoother, painterly falloff
    gray = f.mean(2, keepdims=True)
    f = f * (1 - desat) + gray * desat                              # quieter, more "editorial" colour
    f = f * (1 - lift) + PAPER * lift                               # lift blacks toward warm paper
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    vig = 1 - 0.10 * (((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    f = f * vig[..., None] + grain(f.shape, 5.0, seed)
    return np.clip(f, 0, 255).astype(np.uint8)


packs = np.asarray(Image.open(f"{V1}/packs.jpg").convert("RGB"))
FIELD_CROPS = {   # wide artwork regions inside v1 packs.jpg (1612x1150), used only for colour
    "lavender": (820, 30, 1600, 205), "moon-dreams": (150, 222, 820, 382),
    "rain-forest": (880, 400, 1600, 560), "white-musk": (820, 580, 1590, 748),
    "coconut": (960, 760, 1600, 930), "baby-powder": (930, 945, 1600, 1118),
}
for i, (k, (x0, y0, x1, y1)) in enumerate(FIELD_CROPS.items()):
    fld = color_field(packs[y0:y1, x0:x1], 780 * 2, 400 * 2, seed=i + 1)
    Image.fromarray(fld).save(f"{OUT}/field-{k}.jpg", quality=90, subsampling=0)
    lum = float((fld.astype(np.float32) @ np.array([.2126, .7152, .0722])).mean())
    card = esrgan_x4(np.asarray(Image.open(f"{V1}/scent-{k}.jpg").convert("RGB")))
    save_resized(card, 1040, f"{OUT}/card-{k}.jpg")
    print(f"{k:12s} field luminance {lum:5.1f}  card {card.shape[1]}x{card.shape[0]}", flush=True)

box = np.asarray(Image.open(f"{V1}/box-retouched.jpg").convert("RGB"))
for name, (x0, y0, x1, y1) in {"detail-jasmine": (1150, 300, 1480, 630), "detail-logo": (150, 165, 480, 495)}.items():
    save_resized(esrgan_x4(box[y0:y1, x0:x1]), 680, f"{OUT}/{name}.jpg")
    print(name, "ok", flush=True)
