import math, random

def _bezier(pts):
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i > 0 else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f"C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}"
    return d

def wisp(sx, sy, ey, rnd, amp, waves, drift, calm=0.22):
    """Laminar near the ember (first `calm` of the rise), then growing curls."""
    pts, ph = [], rnd.uniform(0, 6.283)
    for i in range(25):
        t = i / 24
        u = max(0.0, (t - calm) / (1 - calm))
        a = amp * u ** 1.25
        x = sx + drift * u ** 1.7 + a * math.sin(ph + waves * 6.283 * u ** 1.15)
        pts.append((x, sy + (ey - sy) * t))
    return _bezier(pts)

LAYERS = (  # name, count, width range, opacity, amplitude mult, turbulence freq, octaves, displacement, blur
    ("halo", 3, (34, 64), .055, 1.6, "0.003 0.007", 2, 80, 13),
    ("body", 4, (3.5, 7.5), .17, 1.0, "0.004 0.009", 2, 34, 2.2),
    ("core", 2, (1.5, 2.1), .55, .45, "0.006 0.012", 1, 12, .8),
)

def smoke_svg(uid, w, h, sx, sy, ey=0, seed=1, amp=70, color="#f4ede2", strength=1.0, drift=40, cls="smoke"):
    rnd = random.Random(seed)
    defs, groups = [], []
    for name, n, (w0, w1), op, am, freq, octv, disp, blur in LAYERS:
        defs.append(f'<filter id="{uid}-{name}" x="-60%" y="-5%" width="220%" height="110%" color-interpolation-filters="sRGB">'
                    f'<feTurbulence type="fractalNoise" baseFrequency="{freq}" numOctaves="{octv}" seed="{seed + len(defs) * 5}"/>'
                    f'<feDisplacementMap in="SourceGraphic" scale="{disp}" xChannelSelector="R" yChannelSelector="G"/>'
                    f'<feGaussianBlur stdDeviation="{blur}"/></filter>')
        paths = "".join(
            f'<path d="{wisp(sx + rnd.uniform(-2, 2), sy, ey + rnd.uniform(0, 80), rnd, amp * am * rnd.uniform(.75, 1.25), rnd.uniform(1.0, 1.8), drift * rnd.uniform(-.7, 1.2))}" '
            f'stroke-width="{rnd.uniform(w0, w1):.1f}" opacity="{op * strength:.3f}"/>' for _ in range(n))
        top = ey + (sy - ey) * (0.42 if name == "core" else 0)       # core fades out halfway up
        defs.append(f'<linearGradient id="{uid}-{name}-g" x1="0" y1="{sy}" x2="0" y2="{top:.0f}" gradientUnits="userSpaceOnUse">'
                    '<stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".05" stop-color="#fff"/>'
                    '<stop offset=".5" stop-color="#fff" stop-opacity=".85"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
                    f'<mask id="{uid}-{name}-m" maskUnits="userSpaceOnUse" x="0" y="0" width="{w}" height="{h}"><rect width="{w}" height="{h}" fill="url(#{uid}-{name}-g)"/></mask>')
        groups.append(f'<g mask="url(#{uid}-{name}-m)"><g filter="url(#{uid}-{name})">{paths}</g></g>')
    return (f'<svg class="{cls}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true"><defs>{"".join(defs)}</defs>'
            f'<g fill="none" stroke="{color}" stroke-linecap="round">{"".join(groups)}</g></svg>')
