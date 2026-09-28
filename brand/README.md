# The Occasion Room: brand kit

Open `brand-guide.html` in a browser to see every logo, color and type rule.
`brand-guide-preview.png` is a screenshot of it.

## Logo files (`logo/`)

| File | Use it for |
| --- | --- |
| `occasion-room-stacked.svg` | Primary logo: hero section, proposals, pitch decks |
| `occasion-room-horizontal.svg` | Website header, email signature, invoices |
| `occasion-room-wordmark.svg` | Where the arch already appears nearby |
| `icon-lavender.svg` / `icon-plum.svg` | Instagram and LinkedIn avatars, app icon |
| `favicon.svg` | Browser tab: `<link rel="icon" href="/favicon.svg">` |
| `mark-ampersand.svg` | Stickers, wax-seal style stamp, watermark |
| `*-reverse.svg` | Versions for Lavender or Plum backgrounds |
| `png/` | High-resolution PNGs for tools that don't accept SVG (Canva, Instagram) |

All text in the SVGs is converted to vector outlines, so the files look the same everywhere.

## Fonts

- **Display:** Eyesome. The files here use **Italiana** (a free Google Font) as a
  stand-in. Check that your Eyesome license covers commercial and logo use. Then put
  `Eyesome.otf` in `fonts/` and run `pip install fonttools && python brand/build_logos.py`
  to rebuild every logo with it.
- **Labels and buttons:** League Spartan 500–600
- **Body:** Quicksand 400–500

`tokens.css` has the colors and font stacks as CSS variables for the website.
