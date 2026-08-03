# LinkedIn profile cover (1584x396) for The Growth PMM.
# Near-black brand background, lime accents only as fills (site rule: lime is
# never text). Badge+wordmark top right, headline center-aligned on the left
# (kept clear of LinkedIn's avatar overlap zone, bottom-left), past-experience
# logo strip bottom right, lime signature bar along the bottom edge.
#
# The two SVG logos (fi-money, makemytrip) are rasterized with macOS QuickLook
# before this runs:
#   qlmanage -t -s 600 -o <LOGO_TMP> public/logos/fi-money.svg public/logos/makemytrip.svg
import os
from PIL import Image, ImageDraw, ImageFont, ImageChops

W, H = 1584, 396
INK_DEEP = (22, 24, 15)
LIME = (219, 255, 0)
CORAL = (204, 65, 23)

ROOT = "/Users/divyaabhilash/AI_Projects/thegrowthpmm"
LOGO_TMP = os.environ.get("LOGO_TMP", "/tmp/logos")

img = Image.new("RGB", (W, H), INK_DEEP)
d = ImageDraw.Draw(img, "RGBA")

# --- faint grid, echoing the site's grid-canvas (lime at whisper opacity) ---
for x in range(0, W, 48):
    d.line([(x, 0), (x, H)], fill=(219, 255, 0, 10), width=1)
for y in range(0, H, 48):
    d.line([(0, y), (W, y)], fill=(219, 255, 0, 10), width=1)

BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

# ---------- brand badge (same geometry as make_og.py / favicon.svg) ----------
def draw_badge(im, bx, by, B):
    dd = ImageDraw.Draw(im, "RGBA")
    rad = int(B * 9 / 40)
    dd.rounded_rectangle([bx, by, bx + B, by + B], radius=rad, fill=LIME)
    scale = B / 40.0
    f = 0.65 * scale
    off = 7 * scale
    def P(pts):
        return [(bx + off + x * f, by + off + y * f) for x, y in pts]
    dd.polygon(P([(5, 6), (35, 6), (30.5, 12.6), (9.5, 12.6)]), fill=(22, 24, 15, 255))
    dd.polygon(P([(11, 15.4), (29, 15.4), (25, 21.5), (15, 21.5)]), fill=(22, 24, 15, 179))
    dd.polygon(P([(16.5, 24.3), (23.5, 24.3), (21.9, 29.6), (18.1, 29.6)]), fill=(22, 24, 15, 112))
    ccx, ccy = bx + off + 20 * f, by + off + 35 * f
    cr = 2.7 * f
    dd.ellipse([ccx - cr, ccy - cr, ccx + cr, ccy + cr], fill=CORAL)

# ---------- top right: badge + wordmark ----------
PAD = 64
BADGE = 56
word_f = font(BOLD, 30)
word = "The Growth PMM"
ww = d.textlength(word, font=word_f)
total = BADGE + 16 + ww
bx = W - PAD - total
by = 44
draw_badge(img, bx, by, BADGE)
d.text((bx + BADGE + 16, by + (BADGE - 30) // 2 - 3), word, font=word_f, fill=(255, 255, 255))

# ---------- left: headline, center-aligned stack ----------
# Mirrors the site's current hero: H1 (outcome, lime marker on "scalable
# growth.") stacked above the bold sub-head (positioning line, plain white,
# smaller), one line each. Two visual tiers, same as the live page's
# H1 -> sub-head hierarchy, compressed to fit above the avatar safe line.
line1_pre = "Turning early traction into"
line1_mark = "scalable growth."
line1 = line1_pre + " " + line1_mark
sub = "The first Product Marketing leader you need today, before you're ready to hire one full-time."
COL_CX = 600          # center of the left column (nudged right of the avatar)
COL_MAX = 900         # max line width

size = 40
while size > 28:
    f1 = font(BLACK, size)
    if d.textlength(line1, font=f1) + 36 <= COL_MAX:
        break
    size -= 2
head_f = font(BLACK, size)

sub_size = 18
while sub_size > 12:
    sub_f = font(BOLD, sub_size)
    if d.textlength(sub, font=sub_f) <= COL_MAX:
        break
    sub_size -= 1
sub_f = font(BOLD, sub_size)

lh = int(size * 1.3)
sub_lh = int(sub_size * 1.4)
gap = 16
pad_top, pad_bot = 6, 12
pad_right = size * 0.18  # small, matches the site's .marker padding — box hugs the period
# LinkedIn overlays a circular profile photo over the bottom-left of the cover
# (confirmed on the live profile — it clipped text that ran past y=198). Anchor
# the whole stack to a safe bottom that sits ABOVE that avatar zone.
AVATAR_SAFE_BOTTOM = 198
y_sub = AVATAR_SAFE_BOTTOM - sub_size
y1 = y_sub - gap - lh

# line 1: white prefix, then the lime-marked closing phrase; whole line centered.
# Pre and mark are measured (and gapped) separately so the marker's own left
# padding never eats into the space after "into" — pad_left is capped below
# the natural space width instead of assumed to include it.
space_w = d.textlength(" ", font=head_f)
w_pre = d.textlength(line1_pre, font=head_f)
w_mark = d.textlength(line1_mark, font=head_f)
l1x = COL_CX - (w_pre + space_w + w_mark) / 2
d.text((l1x, y1), line1_pre, font=head_f, fill=(255, 255, 255))
mx0 = l1x + w_pre + space_w
pad_left = space_w * 0.35  # only nibbles part of the natural word-space, never the word
d.rounded_rectangle(
    [mx0 - pad_left, y1 - pad_top, mx0 + w_mark + pad_right, y1 + size + pad_bot],
    radius=10, fill=(219, 255, 0, 235))
d.text((mx0, y1), line1_mark, font=head_f, fill=INK_DEEP)

# sub-head: one centered line, plain, lighter than the H1.
w_sub = d.textlength(sub, font=sub_f)
d.text((COL_CX - w_sub / 2, y_sub), sub, font=sub_f, fill=(219, 224, 204))

# ---------- bottom right: past-experience logo strip ----------
# Uniform light stencil treatment: composite each logo on white, mask by
# difference-from-white (so white internals knock out, like MakeMyTrip's "my"),
# tint a single light neutral. Mirrors the site's grayscale-at-75% strip.
TINT = (222, 226, 210)
STRIP_ALPHA = 0.82

def light_logo(path, target_h):
    src = Image.open(path).convert("RGBA")
    flat = Image.new("RGB", src.size, (255, 255, 255))
    flat.paste(src, (0, 0), src)
    diff = ImageChops.difference(flat, Image.new("RGB", src.size, (255, 255, 255))).convert("L")
    mask = diff.point(lambda v: min(255, v * 3))
    bbox = mask.getbbox()
    mask = mask.crop(bbox)
    ratio = target_h / mask.height
    mask = mask.resize((max(1, int(mask.width * ratio)), target_h), Image.LANCZOS)
    mask = mask.point(lambda v: int(v * STRIP_ALPHA))
    out = Image.new("RGBA", mask.size, TINT + (0,))
    tint_img = Image.new("RGBA", mask.size, TINT + (255,))
    out.paste(tint_img, (0, 0), mask)
    return out

# (path, height) — heights mirror the site strip's ratios, scaled up.
logos = [
    (f"{LOGO_TMP}/fi-money.svg.png", 30),
    (f"{ROOT}/public/logos/practo.png", 30),
    (f"{LOGO_TMP}/mmt-square.svg.png", 36),
    (f"{ROOT}/public/logos/raymond.png", 30),
    (f"{ROOT}/public/logos/tcs.png", 30),
]
imgs = [light_logo(p, h) for p, h in logos]
GAP = 36
strip_w = sum(i.width for i in imgs) + GAP * (len(imgs) - 1)
sx = W - PAD - strip_w
strip_cy = H - 56
for li in imgs:
    img.paste(li, (int(sx), int(strip_cy - li.height / 2)), li)
    sx += li.width + GAP

# ---------- lime signature bar ----------
d.rectangle([0, H - 8, W, H], fill=LIME)

out_path = f"{ROOT}/scratchpad/linkedin-cover.png"
img.save(out_path)
print("saved", out_path, img.size)
