#!/usr/bin/env python3
"""Remove the 'AI render finish' from a generated image so it reads as a real photo.

Usage:
  python degrade.py input.png output.jpg [--width 1200 --height 675]
                    [--preset event|phone|portrait|daylight|film] [--strength 1.0] [--seed 7]
"""
import argparse, io
import numpy as np
from PIL import Image, ImageFilter

PRESETS = {
    #            soften  anti_clarity  desat  noise  chroma  vignette  jpeg  black_lift  sharpen
    "event":    (0.75,   0.18,         0.14,  0.056, 0.008,  0.12,     80,   0.025,      0.0),
    "phone":    (0.45,   0.10,         0.06,  0.030, 0.006,  0.05,     84,   0.035,      0.6),
    "portrait": (0.55,   0.12,         0.10,  0.035, 0.005,  0.08,     86,   0.018,      0.0),
    "daylight": (0.50,   0.12,         0.10,  0.022, 0.004,  0.06,     84,   0.015,      0.0),
    "film":     (0.65,   0.14,         0.08,  0.050, 0.002,  0.10,     88,   0.040,      0.0),
}

def cover_resize(im, w, h):
    """Scale and center-crop to exactly w x h."""
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    l, t = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((l, t, l + w, t + h))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("input"); p.add_argument("output")
    p.add_argument("--width", type=int); p.add_argument("--height", type=int)
    p.add_argument("--preset", default="event", choices=PRESETS)
    p.add_argument("--strength", type=float, default=1.0)
    p.add_argument("--seed", type=int, default=7)
    a = p.parse_args()
    soften, clar, desat, noise, chroma, vig, q, lift, sharpen = PRESETS[a.preset]
    k = a.strength

    im = Image.open(a.input).convert("RGB")
    W = a.width or im.width; H = a.height or im.height
    # Work at ~1.33x final size: enough room to soften, then downsample.
    work = cover_resize(im, round(W * 4 / 3), round(H * 4 / 3))
    work = work.filter(ImageFilter.GaussianBlur(soften * k))

    x = np.asarray(work).astype(np.float32) / 255
    big = np.asarray(work.filter(ImageFilter.GaussianBlur(18))).astype(np.float32) / 255
    x += (big - x) * clar * k                                # anti-clarity
    g = x.mean(axis=2, keepdims=True); x = g + (x - g) * (1 - desat * k)
    x[..., 0] *= 1 + 0.02 * k; x[..., 2] *= 1 - 0.02 * k      # slight WB error
    x = lift * k + x * (1 - lift * k * 2)                   # lift blacks
    x = np.where(x > 0.75, 0.75 + (x - 0.75) * (1 - 0.2 * k), x)  # highlight roll-off

    rng = np.random.default_rng(a.seed)
    shadow_w = (0.6 - x.mean(axis=2)).clip(0.15, 0.6) / 0.6
    n = rng.normal(0, 1, x.shape[:2]).astype(np.float32)
    n = np.asarray(Image.fromarray(((n * 0.15 + 0.5).clip(0, 1) * 255).astype(np.uint8))
                   .filter(ImageFilter.GaussianBlur(0.5))).astype(np.float32) / 255 - 0.5
    x += (n / 0.15 * noise * k * shadow_w)[..., None]
    x += rng.normal(0, chroma * k, x.shape)

    h, w = x.shape[:2]; yy, xx = np.ogrid[:h, :w]
    r = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    x *= (1 - vig * k * np.clip(r - 0.5, 0, 1) ** 1.5)[..., None]

    out = Image.fromarray((x.clip(0, 1) * 255).astype(np.uint8)).resize((W, H), Image.LANCZOS)
    if sharpen:  # phones over-sharpen in their own, cruder way
        out = out.filter(ImageFilter.UnsharpMask(radius=1.2, percent=int(60 * sharpen), threshold=2))
    buf = io.BytesIO(); out.save(buf, "JPEG", quality=q)    # camera JPEG round trip
    Image.open(buf).save(a.output, "JPEG", quality=90)
    print(f"saved {a.output} ({W}x{H}, preset={a.preset}, strength={k})")

if __name__ == "__main__":
    main()
