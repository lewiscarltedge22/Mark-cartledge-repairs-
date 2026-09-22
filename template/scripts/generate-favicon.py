"""
Regenerate favicon.ico, favicon-16.png, favicon-32.png and apple-touch-icon.png
for a new brand. Run from the project root after editing the CONFIG below to
match the new business's initials and brand colors (pulled from the :root
CSS variables in index.html).

Requires Pillow: pip install Pillow

Usage: python3 template/scripts/generate-favicon.py
"""
from PIL import Image, ImageDraw, ImageFont
import os

# --- CONFIG: edit these for the new brand ---
INITIALS = "XX"
BACKGROUND = (44, 51, 58, 255)   # --charcoal
ACCENT = (217, 98, 43, 255)      # --brick
OUTPUT_DIR = "images"
# ---------------------------------------------

def make_icon(size, radius_ratio=0.22):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    r = int(size * radius_ratio)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=BACKGROUND)
    font = None
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    fsize = int(size * 0.44)
    for c in candidates:
        if os.path.exists(c):
            font = ImageFont.truetype(c, fsize)
            break
    if font is None:
        font = ImageFont.load_default()
    bbox = d.textbbox((0, 0), INITIALS, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size - tw) / 2 - bbox[0]
    y = (size - th) / 2 - bbox[1]
    d.text((x, y), INITIALS, font=font, fill=ACCENT)
    return img

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    make_icon(16).save(os.path.join(OUTPUT_DIR, "favicon-16.png"))
    make_icon(32).save(os.path.join(OUTPUT_DIR, "favicon-32.png"))
    make_icon(180).save(os.path.join(OUTPUT_DIR, "apple-touch-icon.png"))
    icons = [make_icon(s) for s in (16, 32, 48)]
    icons[0].save(os.path.join(OUTPUT_DIR, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    print("Favicon assets written to", OUTPUT_DIR)
    print("Also update favicon.svg's <text> content and colors to match.")
