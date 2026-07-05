from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1200, 630
CREAM = (231, 235, 245)
INK = (22, 24, 15)
INK_DEEP = (22, 24, 15)
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

# ---------- fonts: the site's real display system, not Arial ----------
FONT_DIR = "/Users/divyaabhilash/AI_Projects/thegrowthpmm/scratchpad/fonts"

def bricolage(size, weight="ExtraBold"):
    f = ImageFont.truetype(f"{FONT_DIR}/BricolageGrotesque.ttf", size)
    f.set_variation_by_name(weight)
    return f

def inter(size, weight="Regular"):
    f = ImageFont.truetype(f"{FONT_DIR}/Inter.ttf", size)
    f.set_variation_by_name(weight)
    return f

def caveat(size, weight="Bold"):
    f = ImageFont.truetype(f"{FONT_DIR}/Caveat.ttf", size)
    f.set_variation_by_name(weight)
    return f

def rotated_paste(base, w, h, angle, cx, cy, draw_fn):
    """Draw on a transparent w x h layer (exact content bounds) via
    draw_fn(layer_draw, layer), rotate about its own center by angle
    degrees (expand handles the larger bounding box automatically), then
    paste so the *original* unrotated center lands at (cx, cy)."""
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer, "RGBA")
    draw_fn(ld, layer)
    rotated = layer.rotate(angle, resample=Image.BICUBIC, expand=True)
    rw, rh = rotated.size
    base.paste(rotated, (int(cx - rw / 2), int(cy - rh / 2)), rotated)

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
word_f = bricolage(31, "Bold")
wy = badge_y + (BADGE - 31) // 2 - 3
d.text((PAD + BADGE + 16, wy), "The Growth PMM", font=word_f, fill=INK)

# ---------- corner stamp: the real credential, worn like a rubber stamp ----------
# Reuses the site's rotated sticky-tag / ba-stamp vocabulary (near-black fill,
# lime text, tilted) instead of inventing a new shape for "fun."
stamp_f = bricolage(17, "Bold")
stamp_text = "TOP 100 GLOBAL PMM, 2025"
stw = stamp_f.getlength(stamp_text)
stamp_w, stamp_h = int(stw + 46), 50

def draw_stamp(ld, layer):
    ld.rounded_rectangle([0, 0, stamp_w, stamp_h], radius=25, fill=(22, 24, 15, 255))
    ld.text((23, (stamp_h - 17) // 2 - 2), stamp_text, font=stamp_f, fill=LIME)

rotated_paste(img, stamp_w, stamp_h, 5, W - PAD - stamp_w / 2 + 6, 96, draw_stamp)

# ---------- headline (matches the live hero H1) ----------
head_f = bricolage(46, "ExtraBold")
line1 = "Product Marketing that turns early traction"
line2 = "into scalable growth."
hx = PAD
hy = 214
lh = 60
d.text((hx, hy), line1, font=head_f, fill=INK)

# marker highlight: a hand-swiped shape, not a perfect rectangle, so it reads
# as drawn rather than a CSS box. Slight rotation + a soft alpha fade at both
# ends, mirroring the site's `.marker` gradient + irregular border-radius.
mark_phrase = "scalable growth."
pre = "into "
pre_w = d.textlength(pre, font=head_f)
mark_w = d.textlength(mark_phrase, font=head_f)
mx0 = hx + pre_w
my0 = hy + lh

# covers roughly the same visible band as the site's `.marker` (padding
# 0.04em/0.18em around the glyphs): cap-height to just past the baseline.
mk_w, mk_h = int(mark_w + 24), 50
def draw_marker(ld, layer):
    top_y, bot_y = 4, mk_h - 6
    pts = [
        (2, top_y + 3), (mk_w * 0.3, top_y - 1), (mk_w * 0.7, top_y + 2), (mk_w - 2, top_y - 2),
        (mk_w - 1, bot_y + 3), (mk_w * 0.65, bot_y + 6), (mk_w * 0.25, bot_y + 1), (1, bot_y + 5),
    ]
    ld.polygon(pts, fill=(219, 255, 0, 232))
    # feathered ends so the stroke reads hand-swiped, not ruled
    fade = Image.new("RGBA", (mk_w, mk_h), (0, 0, 0, 0))
    fd = ImageDraw.Draw(fade)
    fade_w = 26
    for i in range(fade_w):
        a = int(232 * (i / fade_w))
        fd.line([(i, 0), (i, mk_h)], fill=(231, 235, 245, 232 - a))
        fd.line([(mk_w - 1 - i, 0), (mk_w - 1 - i, mk_h)], fill=(231, 235, 245, 232 - a))
    layer.alpha_composite(fade)
rotated_paste(img, mk_w, mk_h, -1.4, mx0 + mark_w / 2, my0 + 33, draw_marker)

d.text((hx, my0), line2, font=head_f, fill=INK)

# a small coral dot closes the highlighted thought, echoing the logo's coral
# drop and the funnel drop-off color (the site's one deliberate accent color)
dot_x, dot_y = mx0 + mark_w + 16, my0 + 30
d.ellipse([dot_x - 5, dot_y - 5, dot_x + 5, dot_y + 5], fill=CORAL)

# ---------- subtext ----------
sub_f = inter(25, "Regular")
sub_lines = [
    "I help post-PMF startups build the positioning, messaging, and",
    "GTM that turn early traction into scalable growth.",
]
sy = hy + lh * 2 + 34
for i, ln in enumerate(sub_lines):
    d.text((PAD, sy + i * 36), ln, font=sub_f, fill=INK_MUTE)

# ---------- footer row: role tag, worn at a tilt like a stuck-on note ----------
fy = H - 88
tag = "Fractional Head of PMM"
tag_f = inter(20, "Bold")
tw = tag_f.getlength(tag)
tag_w, tag_h = int(tw + 40), 44
def draw_role_tag(ld, layer):
    ld.rounded_rectangle([0, 0, tag_w, tag_h], radius=22, fill=(22, 24, 15, 255))
    ld.text((20, (tag_h - 20) // 2 - 2), tag, font=tag_f, fill=LIME)
rotated_paste(img, tag_w, tag_h, -3, PAD + tag_w / 2, fy + tag_h / 2, draw_role_tag)

# a curly hand-drawn arrow + Caveat caption pointing at the tag, reusing the
# hero diagram's exact "the missing piece" annotation vocabulary
note_f = caveat(30, "Bold")
note_text = "12+ years of experience"
nx, ny = PAD + tag_w + 46, fy - 46
d.text((nx, ny), note_text, font=note_f, fill=INK)

def bezier(p0, p1, p2, steps=28):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts

arrow_start = (nx - 6, ny + 38)
arrow_ctrl = (nx - 46, ny + 60)
arrow_end = (PAD + tag_w * 0.35, fy - 14)
curl = bezier(arrow_start, arrow_ctrl, arrow_end)
d.line(curl, fill=(*INK_MUTE, 235), width=2, joint="curve")
# small arrowhead
ex, ey = curl[-1]
px, py = curl[-4]
ang = math.atan2(ey - py, ex - px)
for da in (-2.5, 2.5):
    a = ang + math.pi - da * 0.35
    d.line([(ex, ey), (ex + 9 * math.cos(a + da), ey + 9 * math.sin(a + da))],
           fill=(*INK_MUTE, 235), width=2)

# bottom lime accent bar
d.rectangle([0, H - 12, W, H], fill=LIME)

img.save("/Users/divyaabhilash/AI_Projects/thegrowthpmm/public/og-image.png")
print("saved", img.size)
