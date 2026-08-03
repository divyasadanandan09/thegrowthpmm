# LinkedIn Company Page cover (1128x191) for The Growth PMM.
# Same brand system as the personal profile cover (make_linkedin_cover.py):
# near-black bg, faint lime grid, lime accents as fills only, lime signature
# bar. Laid out differently because the company banner is a much shorter,
# wider strip and the safe zone is different: LinkedIn overlays the square
# company logo on the BOTTOM-LEFT corner only (not a big circular avatar like
# a personal profile), so everything here is pushed clear of that corner
# instead of clear of a wide avatar band.
from PIL import Image, ImageDraw, ImageFont

W, H = 1128, 191
INK_DEEP = (22, 24, 15)
LIME = (219, 255, 0)
CORAL = (204, 65, 23)

ROOT = "/Users/divyaabhilash/AI_Projects/thegrowthpmm"

img = Image.new("RGB", (W, H), INK_DEEP)
d = ImageDraw.Draw(img, "RGBA")

# --- faint grid, echoing the site's grid-canvas ---
for x in range(0, W, 36):
    d.line([(x, 0), (x, H)], fill=(219, 255, 0, 10), width=1)
for y in range(0, H, 36):
    d.line([(0, y), (W, y)], fill=(219, 255, 0, 10), width=1)

BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

# ---------- brand badge (same geometry as make_linkedin_cover.py) ----------
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
PAD = 28
BADGE = 30
word_f = font(BOLD, 17)
word = "The Growth PMM"
ww = d.textlength(word, font=word_f)
total = BADGE + 10 + ww
bx = W - PAD - total
by = 16
draw_badge(img, bx, by, BADGE)
d.text((bx + BADGE + 10, by + (BADGE - 17) // 2 - 1), word, font=word_f, fill=(255, 255, 255))

# ---------- headline + subline, kept clear of the bottom-left logo zone ----------
# LinkedIn overlays the square company logo on the bottom-left corner of the
# banner, roughly the bottom half of a ~120px-wide block. Starting the text
# well right of that (x >= 260) keeps it safe. Two tiers mirror the site's
# H1 -> sub-head hierarchy, just compressed for this much shorter strip.
line_pre = "Turning early traction into"
line_mark = "scalable growth."
sub = "The first Product Marketing leader you need today, before you're ready to hire one full-time."
SAFE_X = 260
right_edge = W - PAD
avail_w = right_edge - SAFE_X

size = 26
while size > 14:
    f1 = font(BLACK, size)
    if d.textlength(line_pre, font=f1) + d.textlength(" ", font=f1) + d.textlength(line_mark, font=f1) + 28 <= avail_w:
        break
    size -= 1
head_f = font(BLACK, size)

sub_size = 14
sub_f = font(BOLD, sub_size)
while sub_size > 9:
    sub_f = font(BOLD, sub_size)
    if d.textlength(sub, font=sub_f) <= avail_w:
        break
    sub_size -= 1

gap = 8
BAR_RESERVE = 12   # keep clear of the lime signature bar at the bottom edge
block_h = size + gap + sub_size
top = by + BADGE
ly = top + (H - BAR_RESERVE - top - block_h) / 2
sy = ly + size + gap

space_w = d.textlength(" ", font=head_f)
w_pre = d.textlength(line_pre, font=head_f)
w_mark = d.textlength(line_mark, font=head_f)
total_w = w_pre + space_w + w_mark
lx = SAFE_X + (avail_w - total_w) / 2

d.text((lx, ly), line_pre, font=head_f, fill=(255, 255, 255))
mx0 = lx + w_pre + space_w
pad_top, pad_bot = 4, 8
pad_left = space_w * 0.35  # only nibbles part of the natural word-space, never the word
pad_right = size * 0.18    # small, matches the site's .marker padding — box hugs the period
d.rounded_rectangle(
    [mx0 - pad_left, ly - pad_top, mx0 + w_mark + pad_right, ly + size + pad_bot],
    radius=8, fill=(219, 255, 0, 235))
d.text((mx0, ly), line_mark, font=head_f, fill=INK_DEEP)

w_sub = d.textlength(sub, font=sub_f)
d.text((SAFE_X + (avail_w - w_sub) / 2, sy), sub, font=sub_f, fill=(219, 224, 204))

# ---------- lime signature bar ----------
BAR = 4
d.rectangle([0, H - BAR, W, H], fill=LIME)

out_path = f"{ROOT}/scratchpad/linkedin-company-cover.png"
img.save(out_path)
print("saved", out_path, img.size)
