from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
CREAM = (231, 235, 245)
INK = (22, 24, 15)
INK_MUTE = (95, 100, 112)
LIME = (219, 255, 0)
CORAL = (204, 65, 23)

img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img, "RGBA")

# --- subtle aurora wash (top-left cool, top-right violet) ---
aur = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ad = ImageDraw.Draw(aur)
for cx, cy, r, col in [(150, 60, 520, (231, 236, 255, 90)),
                       (1050, 120, 520, (236, 228, 255, 80)),
                       (860, 680, 560, (227, 239, 240, 90))]:
    for i in range(r, 0, -6):
        a = int(col[3] * (1 - i / r))
        ad.ellipse([cx - i, cy - i, cx + i, cy + i], fill=(col[0], col[1], col[2], a))
img = Image.alpha_composite(img.convert("RGBA"), aur).convert("RGB")
d = ImageDraw.Draw(img, "RGBA")

# --- grid canvas (echoes the site hero) ---
for x in range(0, W, 48):
    d.line([(x, 0), (x, H)], fill=(22, 24, 15, 12), width=1)
for y in range(0, H, 48):
    d.line([(0, y), (W, y)], fill=(22, 24, 15, 12), width=1)

def font(path, size):
    return ImageFont.truetype(path, size)

BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

PAD = 80

# ---------- brand badge (lime rounded square + funnel mark) ----------
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

BADGE = 58
badge_y = 70
draw_badge(img, PAD, badge_y, BADGE)
word_f = font(BOLD, 34)
wy = badge_y + (BADGE - 34) // 2 - 4
d.text((PAD + BADGE + 16, wy), "The Growth PMM", font=word_f, fill=INK)

# ---------- headline ----------
head_f = font(BLACK, 52)
line1 = "The first Product Marketing leader you"
line2 = "bring in before you hire a full-time one."
hx = PAD
hy = 210
lh = 66
d.text((hx, hy), line1, font=head_f, fill=INK)

# marker highlight behind part of line 2
mark_phrase = "before you hire a full-time one."
pre = "bring in "
pre_w = d.textlength(pre, font=head_f)
mark_w = d.textlength(mark_phrase, font=head_f)
mx0 = hx + pre_w
my0 = hy + lh
d.rounded_rectangle([mx0 - 6, my0 + 8, mx0 + mark_w + 6, my0 + 54], radius=8,
                    fill=(219, 255, 0, 235))
d.text((hx, my0), line2, font=head_f, fill=INK)

# ---------- subtext ----------
sub_f = font(REG, 25)
sub_lines = [
    "I help post-PMF startups build the positioning, messaging, and",
    "GTM that turn early traction into scalable growth.",
]
sy = hy + lh * 2 + 34
for i, ln in enumerate(sub_lines):
    d.text((PAD, sy + i * 36), ln, font=sub_f, fill=INK_MUTE)

# ---------- footer row: role tag only ----------
# URL dropped 2026-07-03: the platform (LinkedIn/Slack/iMessage) already shows
# the link's own domain next to the card, so it was redundant weight. Pill
# stays left, under the badge/headline column, so the page reads as one clean
# left rail (badge -> headline -> subtext -> tag) rather than two competing
# bottom anchors.
fy = H - 88
tag = "Fractional Head of PMM"
tag_f = font(BOLD, 20)
tw = d.textlength(tag, font=tag_f)
px0 = PAD
px1 = px0 + tw + 40
d.rounded_rectangle([px0, fy - 8, px1, fy + 36], radius=22, fill=INK)
d.text((px0 + 20, fy + 2), tag, font=tag_f, fill=LIME)

# bottom lime accent bar
d.rectangle([0, H - 12, W, H], fill=LIME)

img.save("/Users/divyaabhilash/AI_Projects/thegrowthpmm/public/og-image.png")
print("saved", img.size)
