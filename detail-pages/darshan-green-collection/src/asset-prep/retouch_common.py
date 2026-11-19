"""Shared photo-retouch helpers: flat-field (illumination) correction, tone, sharpening."""
import numpy as np, cv2


def poly_design(xs, ys, deg):
    cols = []
    for i in range(deg + 1):
        for j in range(deg + 1 - i):
            cols.append((xs ** i) * (ys ** j))
    return np.stack(cols, axis=1)


def fit_illumination(img, bg_mask, deg=3, step=6, iters=3):
    """Fit a smooth per-channel polynomial surface to background pixels."""
    h, w, _ = img.shape
    yy, xx = np.mgrid[0:h:step, 0:w:step]
    m = bg_mask[0:h:step, 0:w:step] > 0
    xs = (xx[m] / w * 2 - 1).astype(np.float64)
    ys = (yy[m] / h * 2 - 1).astype(np.float64)
    vals = img[0:h:step, 0:w:step][m].astype(np.float64)
    A = poly_design(xs, ys, deg)
    keep = np.ones(len(xs), bool)
    for _ in range(iters):
        coefs = [np.linalg.lstsq(A[keep], vals[keep, c], rcond=None)[0] for c in range(3)]
        pred = np.stack([A @ cf for cf in coefs], 1)
        resid = np.abs(vals - pred).max(1)
        keep = resid < max(3 * np.median(resid), 2.0)
    gy, gx = np.mgrid[0:h, 0:w]
    Af = poly_design((gx / w * 2 - 1).ravel(), (gy / h * 2 - 1).ravel(), deg)
    field = np.stack([(Af @ cf).reshape(h, w) for cf in coefs], 2)
    return field.astype(np.float32)


def flat_field(img, field, target=246.0):
    out = img.astype(np.float32) / np.maximum(field, 1.0) * target
    return np.clip(out, 0, 255)


def tone(img, contrast=0.12, sat=1.08, gamma=1.0):
    x = np.clip(img / 255.0, 0, 1)
    if gamma != 1.0:
        x = x ** gamma
    s = x + contrast * (x - 0.5) * (1 - np.abs(2 * x - 1))   # gentle S-curve, protects ends
    s = np.clip(s, 0, 1)
    lab = cv2.cvtColor((s * 255).astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
    lab[..., 1:] = (lab[..., 1:] - 128) * sat + 128
    return cv2.cvtColor(np.clip(lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2RGB).astype(np.float32)


def sharpen(img, sigma=1.1, amount=0.45):
    blur = cv2.GaussianBlur(img, (0, 0), sigma)
    return np.clip(img + amount * (img - blur), 0, 255)
