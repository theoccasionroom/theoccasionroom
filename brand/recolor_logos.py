"""Make the burgundy (wine & gold) logo set from the original lavender logos.

The lavender originals in brand/logo/ are left untouched. This script copies
every SVG into brand/logo-wine/ and swaps the colors:

    python3 brand/recolor_logos.py

Run it again after rebuilding the lavender logos (build_logos.py) to refresh
the wine versions.
"""

from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "logo"
OUT = ROOT / "logo-wine"

# Lavender palette -> wine palette
SWAP = {
    "#4A3A50": "#3F0E18",  # Plum Ink      -> Deep Wine (text)
    "#8D6B94": "#6E1F2F",  # Lavender      -> Wine (arch, monogram, backgrounds)
    "#E8DBC5": "#C9A96E",  # Sand Dune     -> Soft Gold (accents on dark backgrounds)
    "#FFF4E9": "#FBF7F1",  # Linen         -> Ivory
}

# Extra light-background versions with a gold arch and monogram
GOLD_SWAP = {
    "#4A3A50": "#3F0E18",  # text stays Deep Wine
    "#8D6B94": "#B08D57",  # arch, monogram and tagline in Gold
}
GOLD_FILES = ["occasion-room-stacked.svg", "occasion-room-horizontal.svg"]


def recolor(svg, swap):
    for old, new in swap.items():
        svg = svg.replace(old, new).replace(old.lower(), new)
    return svg


def rename(name):
    return name.replace("lavender", "wine").replace("plum", "deep-wine")


def main():
    OUT.mkdir(exist_ok=True)
    for path in sorted(SRC.glob("*.svg")):
        (OUT / rename(path.name)).write_text(recolor(path.read_text(), SWAP))
        print("wrote", OUT / rename(path.name))
    for name in GOLD_FILES:
        gold = name.replace(".svg", "-gold.svg")
        (OUT / gold).write_text(recolor((SRC / name).read_text(), GOLD_SWAP))
        print("wrote", OUT / gold)


if __name__ == "__main__":
    main()
