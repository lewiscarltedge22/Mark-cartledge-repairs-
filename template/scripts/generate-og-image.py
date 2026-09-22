"""
Regenerate images/og-image.png (1200x630) — the image shown when a link to
this site is shared on Facebook, WhatsApp, LinkedIn, X, iMessage, etc.

Edit the CONFIG below to match the real business name, owner, town and
services, then run: python3 template/scripts/generate-og-image.py

Requires Pillow: pip install Pillow
"""
from PIL import Image, ImageDraw, ImageFont
import os

# --- CONFIG: edit these for the new brand ---
INITIALS = "XX"
BUSINESS_NAME = "[Business Name]"
SUBTITLE = "[Owner Name]  ·  Self-Employed Builder  ·  [Your Town]"
SERVICES_LINE = "Bathrooms  ·  Kitchens  ·  Patios  ·  Fencing  ·  En Suites  ·  Plastering"
BACKGROUND = (44, 51, 58, 255)   # --charcoal
ACCENT = (217, 98, 43, 255)      # --brick
OUTPUT_PATH = "images/og-image.png"
# ---------------------------------------------

W, H = 1200, 630

def font(path_list, size):
    for p in path_list:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

BOLD = ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"]
REG = ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"]

img = Image.new("RGB", (W, H), BACKGROUND).convert("RGBA")
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
od.ellipse([W - 420, -260, W + 180, 340], fill=ACCENT[:3] + (28,))
img = Image.alpha_composite(img, overlay).convert("RGB")
d = ImageDraw.Draw(img)

lm_size, lm_x, lm_y = 88, 80, 80
d.rounded_rectangle([lm_x, lm_y, lm_x + lm_size, lm_y + lm_size], radius=18, fill=(255, 255, 255, 255))
f_logo = font(BOLD, 34)
bbox = d.textbbox((0, 0), INITIALS, font=f_logo)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
d.text((lm_x + (lm_size - tw) / 2 - bbox[0], lm_y + (lm_size - th) / 2 - bbox[1]), INITIALS, font=f_logo, fill=ACCENT)

d.text((lm_x, lm_y + lm_size + 34), BUSINESS_NAME, font=font(BOLD, 52), fill=(255, 255, 255, 255))
d.text((lm_x, lm_y + lm_size + 34 + 66), SUBTITLE, font=font(REG, 28), fill=(199, 205, 211, 255))
d.text((lm_x, H - 90), SERVICES_LINE, font=font(REG, 24), fill=(240, 165, 122, 255))

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
img.save(OUTPUT_PATH)
print("saved", OUTPUT_PATH, img.size)
