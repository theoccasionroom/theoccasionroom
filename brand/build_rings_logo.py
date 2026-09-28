"""Build the rings logo (two wedding rings + location pin) as vector files.

This is a vector recreation of the logo designed in Canva. The wordmark uses
Italiana (narrowed) and the tagline League Spartan Bold, both as outlines, so
the SVGs look the same everywhere.

    pip install fonttools
    python3 brand/build_rings_logo.py
"""

import math
from pathlib import Path

from build_logos import DISPLAY, FONTS, Face

ROOT = Path(__file__).parent
OUT = ROOT / "logo-rings"
BOLD = Face(FONTS / "LeagueSpartan-700.ttf")

COLORS = {
    "wine": "#721840",       # matches the Canva logo background
    "deep_wine": "#3D0B21",
    "ivory": "#FBF7F1",
    "cream": "#EFE5D6",      # the Canva logo's line color
    "gold": "#B08D57",
    "soft_gold": "#C9A96E",
}

WORDMARK = "THE OCCASION ROOM"
TAGLINE = "Every detail. One room"

# Mark geometry (pin circle centre at 0,0)
RING_R = 100
RING_DX = 54.5
RING_Y = 147
PIN_R = 34
PIN_TIP = 62
PIN_HOLE = 13
STROKE = 8


def mark(color, x=0.0, y=0.0, scale=1.0):
    """The rings + pin mark as an SVG group, pin circle centred at (x, y)."""
    cos_t = PIN_R / PIN_TIP
    sin_t = math.sqrt(1 - cos_t**2)
    tx, ty = PIN_R * sin_t, PIN_R * cos_t
    pin = f"M0 {PIN_TIP}L{tx:.2f} {ty:.2f}A{PIN_R} {PIN_R} 0 1 0 {-tx:.2f} {ty:.2f}Z"
    return (
        f'<g transform="translate({x:.2f} {y:.2f}) scale({scale:.4f})" fill="none" '
        f'stroke="{color}" stroke-width="{STROKE}" stroke-linejoin="round">'
        f'<circle cx="{-RING_DX}" cy="{RING_Y}" r="{RING_R}"/>'
        f'<circle cx="{RING_DX}" cy="{RING_Y}" r="{RING_R}"/>'
        f'<path d="{pin}"/>'
        f'<circle cx="0" cy="0" r="{PIN_HOLE}"/>'
        "</g>"
    )


# Mark bounds in its own units
M_LEFT = -RING_DX - RING_R - STROKE / 2
M_RIGHT = -M_LEFT
M_TOP = -PIN_R - STROKE / 2
M_BOTTOM = RING_Y + RING_R + STROKE / 2
M_W = M_RIGHT - M_LEFT
M_H = M_BOTTOM - M_TOP


def narrow_text(face, s, cap, cx, baseline, squeeze, tracking=0.0):
    """Centered outlined text, horizontally squeezed (Canva wordmark is condensed)."""
    w = face.width(s, cap, tracking) * squeeze
    d, _ = face.text(s, cap, 0, 0, tracking)
    return f'<path transform="translate({cx - w / 2:.2f} {baseline:.2f}) scale({squeeze} 1)" d="{d}"/>'


def svg(w, h, body, bg=None, title="The Occasion Room"):
    rect = f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" '
        f'width="{w:.0f}" height="{h:.0f}" role="img"><title>{title}</title>{rect}{body}</svg>'
    )


def mark_only(color, bg=None, pad=0):
    w, h = M_W + pad * 2, M_H + pad * 2
    return svg(w, h, mark(color, pad - M_LEFT, pad - M_TOP), bg)


def stacked(line, text, tag, bg=None, tagline=True):
    """Mark on top, wordmark, tagline: the Canva layout."""
    W = 700
    s = 0.95
    mark_h = M_H * s
    y0 = 40
    body = mark(line, W / 2, y0 - M_TOP * s, s)
    base = y0 + mark_h + 110
    body += f'<g fill="{text}">{narrow_text(DISPLAY, WORDMARK, 58, W / 2, base, 0.78, 0.02)}</g>'
    h = base + 50
    if tagline:
        tb = base + 72
        body += f'<g fill="{tag}">{narrow_text(BOLD, TAGLINE, 34, W / 2, tb, 1.0)}</g>'
        h = tb + 44
    return svg(W, h, body, bg)


def horizontal(line, text, tag, bg=None):
    """Mark on the left, wordmark + tagline on the right: website header."""
    H = 120
    s = (H - 20) / M_H
    mx = 10 - M_LEFT * s
    body = mark(line, mx, 10 - M_TOP * s, s)
    x = 10 + M_W * s + 28
    d, w = DISPLAY.text(WORDMARK, 34, 0, 0, 0.03)
    squeeze = 0.8
    body += f'<path fill="{text}" transform="translate({x:.2f} 62) scale({squeeze} 1)" d="{d}"/>'
    d2, w2 = BOLD.text(TAGLINE.upper(), 12.5, 0, 0, 0.16)
    body += f'<path fill="{tag}" transform="translate({x + 1:.2f} 92)" d="{d2}"/>'
    W = x + max(w * squeeze, w2) + 12
    return svg(W, H, body, bg)


def main():
    OUT.mkdir(exist_ok=True)
    c = COLORS
    files = {
        # Canva layout: stacked
        "rings-stacked-wine-bg.svg": stacked(c["cream"], c["cream"], c["cream"], bg=c["wine"]),
        "rings-stacked.svg": stacked(c["wine"], c["deep_wine"], c["wine"]),
        "rings-stacked-gold.svg": stacked(c["gold"], c["deep_wine"], c["wine"]),
        "rings-stacked-light.svg": stacked(c["cream"], c["ivory"], c["soft_gold"]),
        "rings-stacked-notag.svg": stacked(c["wine"], c["deep_wine"], c["wine"], tagline=False),
        # Website header / footer
        "rings-horizontal.svg": horizontal(c["wine"], c["deep_wine"], c["wine"]),
        "rings-horizontal-light.svg": horizontal(c["soft_gold"], c["ivory"], c["soft_gold"]),
        # Mark only
        "rings-mark-wine.svg": mark_only(c["wine"]),
        "rings-mark-gold.svg": mark_only(c["gold"]),
        "rings-mark-cream.svg": mark_only(c["cream"]),
        "rings-icon-wine.svg": mark_only(c["cream"], bg=c["wine"], pad=70),
        "favicon.svg": mark_only(c["cream"], bg=c["wine"], pad=40),
    }
    for name, content in files.items():
        (OUT / name).write_text(content)
    print(f"Wrote {len(files)} files to {OUT}")


if __name__ == "__main__":
    main()
