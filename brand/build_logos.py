"""Build The Occasion Room logo files.

All text is converted to vector outlines, so the SVGs look identical everywhere
without needing the fonts installed.

    pip install fonttools
    python brand/build_logos.py

To use Eyesome instead of the stand-in display font (Italiana), put the font
file at brand/fonts/Eyesome.otf (or .ttf) and run the script again.
"""

from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).parent
FONTS = ROOT / "fonts"
OUT = ROOT / "logo"

COLORS = {
    "plum": "#4A3A50",      # Plum Ink: added for text, 9.6:1 on Linen
    "lavender": "#8D6B94",  # Vintage Lavender
    "amethyst": "#B185A7",  # Amethyst Smoke
    "taupe": "#C3A29E",     # Rosy Taupe
    "sand": "#E8DBC5",      # Sand Dune
    "linen": "#FFF4E9",     # Linen
}


def display_font_path():
    for name in ("Eyesome.otf", "Eyesome.ttf"):
        if (FONTS / name).exists():
            return FONTS / name
    return FONTS / "Italiana-400.ttf"


class Face:
    def __init__(self, path):
        self.font = TTFont(path)
        self.glyphs = self.font.getGlyphSet()
        self.cmap = self.font.getBestCmap()
        self.upm = self.font["head"].unitsPerEm
        self.cap = self.font["OS/2"].sCapHeight or 0.7 * self.upm

    def text(self, s, cap, x, baseline, tracking=0.0):
        """Outline `s` with its caps `cap` px tall, starting at x on `baseline`.

        `tracking` is extra letter spacing in em. Returns (svg path d, width).
        """
        scale = cap / self.cap
        pen = SVGPathPen(self.glyphs)
        cursor = x
        for i, ch in enumerate(s):
            name = self.cmap[ord(ch)]
            glyph = self.glyphs[name]
            glyph.draw(TransformPen(pen, (scale, 0, 0, -scale, cursor, baseline)))
            cursor += glyph.width * scale
            if i < len(s) - 1:
                cursor += tracking * self.upm * scale
        return pen.getCommands(), cursor - x

    def width(self, s, cap, tracking=0.0):
        return self.text(s, cap, 0, 0, tracking)[1]

    def centered(self, s, cap, cx, baseline, tracking=0.0):
        return self.text(s, cap, cx - self.width(s, cap, tracking) / 2, baseline, tracking)[0]


DISPLAY = Face(display_font_path())
SANS = Face(FONTS / "LeagueSpartan-500.ttf")
AMP = Face(FONTS / "BodoniModa-400.ttf")

WORDMARK = "THE OCCASION ROOM"
TAGLINE = "WEDDING WEBSITES · ALL IN ONE PLACE"


def arch(cx, top, w, h, stroke, ink):
    """An open doorway arch: the "room". A heavy outer line and a hairline inside it."""
    def path(inset):
        r = w / 2 - inset
        left, right, bottom = cx - r, cx + r, top + h
        return (f"M{left:.2f} {bottom:.2f}V{top + w / 2:.2f}"
                f"A{r:.2f} {r:.2f} 0 0 1 {right:.2f} {top + w / 2:.2f}V{bottom:.2f}")
    gap = stroke * 2.6
    return (f'<path d="{path(0)}" fill="none" stroke="{ink}" stroke-width="{stroke}"/>'
            f'<path d="{path(gap)}" fill="none" stroke="{ink}" stroke-width="{stroke / 3:.2f}"/>'
            f'<path d="M{cx - w / 2 - w * 0.18:.2f} {top + h:.2f}H{cx + w / 2 + w * 0.18:.2f}" '
            f'stroke="{ink}" stroke-width="{stroke / 3:.2f}"/>')


def mark(cx, top, w, ink, inner="&"):
    """Arch with an ampersand (or monogram) standing in the doorway."""
    h = w * 1.34
    stroke = w * 0.028
    parts = [arch(cx, top, w, h, stroke, ink)]
    if inner == "&":
        cap = w * 0.5
        parts.append(f'<path d="{AMP.centered("&", cap, cx, top + h * 0.8)}" fill="{ink}"/>')
    else:
        cap = w * 0.3
        parts.append(f'<path d="{DISPLAY.centered(inner, cap, cx, top + h * 0.74, 0.04)}" fill="{ink}"/>')
    return "".join(parts), h


def svg(width, height, body, bg=None, title="The Occasion Room"):
    rect = f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height:.0f}" '
            f'width="{width:.0f}" height="{height:.0f}" role="img"><title>{title}</title>'
            f'{rect}{body}</svg>\n')


def stacked(ink, accent, bg=None):
    """Primary logo: arch mark, wordmark, tagline."""
    W, pad = 1000, 70
    mark_w = 120
    body, mh = mark(W / 2, pad, mark_w, accent)
    cap = 50
    base = pad + mh + 44 + cap
    body += f'<path d="{DISPLAY.centered(WORDMARK, cap, W / 2, base, 0.06)}" fill="{ink}"/>'
    tcap = 12.5
    tbase = base + 34 + tcap
    body += f'<path d="{SANS.centered(TAGLINE, tcap, W / 2, tbase, 0.32)}" fill="{accent}"/>'
    return svg(W, tbase + pad, body, bg)


def wordmark(ink, accent, bg=None, tagline=True):
    """Two-line wordmark: a small tracked THE between hairlines, OCCASION ROOM below."""
    main = "OCCASION ROOM"
    cap = 64
    tr = 0.06
    main_w = DISPLAY.width(main, cap, tr)
    pad = 48
    W = main_w + pad * 2
    cx = W / 2
    the_cap = 15
    the_base = pad + the_cap
    the_w = SANS.width("THE", the_cap, 0.5)
    body = f'<path d="{SANS.centered("THE", the_cap, cx, the_base, 0.5)}" fill="{accent}"/>'
    rule_y = the_base - the_cap / 2
    rule = main_w * 0.3
    for x1, x2 in ((cx - the_w / 2 - 22 - rule, cx - the_w / 2 - 22),
                   (cx + the_w / 2 + 22, cx + the_w / 2 + 22 + rule)):
        body += f'<path d="M{x1:.2f} {rule_y:.2f}H{x2:.2f}" stroke="{accent}" stroke-width="1.2"/>'
    base = the_base + 30 + cap
    body += f'<path d="{DISPLAY.centered(main, cap, cx, base, tr)}" fill="{ink}"/>'
    end = base
    if tagline:
        tcap = 12
        end = base + 30 + tcap
        body += f'<path d="{SANS.centered(TAGLINE, tcap, cx, end, 0.34)}" fill="{accent}"/>'
    return svg(W, end + pad, body, bg)


def horizontal(ink, accent, bg=None):
    """Mark on the left, a hairline divider, name and tagline on the right: for headers."""
    pad = 36
    mark_w = 78
    body, mh = mark(pad + mark_w / 2 + 12, pad, mark_w, accent)
    div_x = pad + mark_w + 24 + 36
    body += f'<path d="M{div_x:.2f} {pad + 6:.2f}V{pad + mh - 6:.2f}" stroke="{accent}" stroke-width="1"/>'
    x = div_x + 36
    cap = 40
    mid = pad + mh / 2
    base = mid + 4
    d, w = DISPLAY.text(WORDMARK, cap, x, base, 0.06)
    body += f'<path d="{d}" fill="{ink}"/>'
    tcap = 10
    d2, w2 = SANS.text(TAGLINE, tcap, x + 2, base + 22 + tcap, 0.3)
    body += f'<path d="{d2}" fill="{accent}"/>'
    return svg(x + max(w, w2) + pad, mh + pad * 2, body, bg)


def icon(fg, bg, inner="&", size=512, radius=0.22):
    """Square app icon / favicon / social avatar."""
    mark_w = size * 0.42
    h = mark_w * 1.34
    body, _ = mark(size / 2, (size - h) / 2 - size * 0.01, mark_w, fg, inner)
    r = size * radius
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" '
            f'height="{size}" role="img"><title>The Occasion Room</title>'
            f'<rect width="{size}" height="{size}" rx="{r:.1f}" fill="{bg}"/>{body}</svg>\n')


def mark_only(ink, inner="&"):
    w = 200
    body, h = mark(w / 2 + 40, 30, w, ink, inner)
    return svg(w + 80, h + 60, body)


def main():
    OUT.mkdir(exist_ok=True)
    c = COLORS
    files = {
        # Primary stacked logo
        "occasion-room-stacked.svg": stacked(c["plum"], c["lavender"]),
        "occasion-room-stacked-lavender.svg": stacked(c["lavender"], c["lavender"]),
        "occasion-room-stacked-reverse.svg": stacked(c["linen"], c["sand"], bg=c["lavender"]),
        # Wordmark only
        "occasion-room-wordmark.svg": wordmark(c["plum"], c["lavender"]),
        "occasion-room-wordmark-notag.svg": wordmark(c["plum"], c["lavender"], tagline=False),
        "occasion-room-wordmark-reverse.svg": wordmark(c["linen"], c["sand"], bg=c["plum"]),
        # Website header
        "occasion-room-horizontal.svg": horizontal(c["plum"], c["lavender"]),
        "occasion-room-horizontal-reverse.svg": horizontal(c["linen"], c["sand"], bg=c["lavender"]),
        # Marks
        "mark-ampersand.svg": mark_only(c["lavender"]),
        "mark-monogram.svg": mark_only(c["lavender"], "OR"),
        # Icons
        "icon-lavender.svg": icon(c["linen"], c["lavender"]),
        "icon-linen.svg": icon(c["lavender"], c["linen"]),
        "icon-plum.svg": icon(c["sand"], c["plum"]),
        "icon-monogram.svg": icon(c["linen"], c["lavender"], "OR"),
        "favicon.svg": icon(c["linen"], c["lavender"], size=64, radius=0.2),
    }
    for name, content in files.items():
        (OUT / name).write_text(content)
    print(f"Wrote {len(files)} files to {OUT} using {display_font_path().name}")


if __name__ == "__main__":
    main()
