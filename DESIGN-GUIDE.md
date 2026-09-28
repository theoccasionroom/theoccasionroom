# The Occasion Room: Design Guide for the Elementor Build

This guide is the blueprint for rebuilding the marketing site in **WordPress + Elementor**
(Hostinger, built through the Novamira MCP plugin). It is written so a person or an AI agent
can follow it step by step without guessing.

- **Visual reference:** `prototype/index.html` (open in a browser). Screenshots are in `prototype/screenshots/`.
- **Source of truth for values:** `prototype/css/style.css`. If this guide and the CSS ever disagree, the CSS wins.
- **Status:** Homepage designed (version 2, "premium stationery" direction). The other pages are outlined in
  section 11 and get full specs and final text as each one is approved.

---

## 1. Brand feeling (read first)

Premium, romantic, and editorial, like a luxury wedding stationery suite: deep wine, ivory paper,
gold foil details, a wax seal, a script signature line. Inspired by the mood board in the repo root
(`IMG_8126`–`IMG_8140`: wine wax seals, embossed wine paper, gold monograms, Didone logotypes with script).

Signature elements, used consistently:
1. **Didone headline + script line:** a Bodoni Moda heading followed by a Pinyon Script line in Wine (or Soft Gold on dark).
2. **Invitation frame:** a thin gold border with a second hairline 8px inside.
3. **Arch photos** that echo a chapel window.
4. **Gold wax seal** with the rings mark.
5. **Deep Wine sections** with a faint tone-on-tone rings pattern.
6. **Paper texture** on light sections.

Audience: **wedding planners** first (they buy), couples second. The single main action everywhere is
**contacting us / becoming a partner planner**. The contact page must never be more than one click away.

---

## 2. Logo

The logo is the **rings mark**: two interlocking wedding rings with a location pin above them. It comes
with the wordmark **THE OCCASION ROOM** and the tagline **Every detail. One room**. It was designed in Canva.
Vector recreations are in `brand/logo-rings/` (PNG versions in `brand/logo-rings/png/`).

| File | Use |
|------|-----|
| `rings-horizontal.svg` | **Header** (on Ivory) |
| `rings-horizontal-light.svg` | **Footer** and any Deep Wine background |
| `rings-stacked.svg` / `rings-stacked-gold.svg` | Large use on light backgrounds (About page, proposals) |
| `rings-stacked-wine-bg.svg` | The original Canva layout (cream on wine) for social posts |
| `rings-mark-wine.svg` / `-gold.svg` / `-cream.svg` | Mark only |
| `favicon.svg`, `png/rings-icon-wine.png` | Site icon (Elementor: Site Settings > Site Identity) |

If the original Canva export is available, it can replace these, as long as it keeps the same colors.
The older arch-and-ampersand logos (`brand/logo/` lavender, `brand/logo-wine/` wine) are archived and not used on the site.

---

## 3. Colors

Set these up as **Elementor Global Colors** (Site Settings > Global Colors) using these exact names.

| Global name  | Hex       | Role |
|--------------|-----------|------|
| Ivory        | `#FBF7F1` | Page background, cards, text on dark backgrounds |
| Champagne    | `#F2E8DA` | Alternate section background |
| Cream        | `#EFE5D6` | Body text on Deep Wine (13.3:1); the logo's line color |
| Line         | `#DCCBB8` | Neutral dividers (header border, form fields) |
| Taupe        | `#7A6358` | Muted text: captions, small labels, countdown labels (5.2:1 on Ivory) |
| Espresso     | `#3B2A2D` | Body text on light backgrounds (12.6:1 on Ivory) |
| Deep Wine    | `#3D0B21` | Headings, dark sections (hero, Memory Mode, top bar, footer) |
| Wine         | `#721840` | **Accent (matches the logo)**: primary buttons, links, eyebrows, icons, script lines on light |
| Wine Hover   | `#5A1232` | Primary button hover |
| Gold         | `#B08D57` | Frames, ornaments, step numerals, quote marks, diamond bullets on light. **Never body text.** |
| Soft Gold    | `#C9A96E` | On Deep Wine: script lines, eyebrows, gold button, outline buttons (7.4:1) |

Extra fixed colors (no global needed):

| Value | Where |
|-------|-------|
| `rgba(176,141,87,0.45)` | Inner hairline of the invitation frame |
| `rgba(201,169,110,0.10)` | Oversized "Forever" script word in Memory Mode |
| `rgba(201,169,110,0.30)` | Footer bottom divider |
| `#BFA99A` | Footer copyright line |
| `rgba(251,247,241,0.97)` | Sticky header background |

Contrast rules: body text is Espresso on Ivory or Champagne, or Cream on Deep Wine. Gold only for
decoration or text 24px and larger.

---

## 4. Typography

All free Google Fonts, available in Elementor. Set as **Global Fonts** (Site Settings > Global Fonts).

| Font | Use | Weights |
|------|-----|---------|
| **Bodoni Moda** | Headings, statement text, quotes, numerals (high-contrast Didone serif) | 400, 500 (+ italic 400) |
| **Pinyon Script** | The script line inside headings, signatures, names | 400 |
| **League Spartan** | Eyebrows, buttons, navigation, small labels (always UPPERCASE, widely spaced) | 500, 600 |
| **Quicksand** | Body text | 500 |

### Headline + script pattern (used on every H1/H2)

Each main heading is one **Heading** widget whose title contains a span for the script part:

```html
Effortless for you, <span class="script">unforgettable for them</span>
```

Add this once in **Site Settings > Custom CSS** (Elementor Pro) so every heading can use it:

```css
.script {
  display: block;
  font-family: "Pinyon Script", cursive;
  font-weight: 400;
  font-size: 1.2em;          /* 1.22em in the hero H1 */
  line-height: 1.15;
  text-transform: none;
  letter-spacing: 0;
  color: #721840;            /* Wine */
}
.on-dark .script { color: #C9A96E; }  /* Soft Gold: add CSS class "on-dark" to every Deep Wine container */
```

### Type scale

Elementor breakpoints: **Desktop > 1024px**, **Tablet ≤ 1024px**, **Mobile ≤ 767px** (the defaults).

| Style | Font / weight | Desktop | Tablet | Mobile | Line height | Letter spacing | Color | Transform |
|-------|---------------|---------|--------|--------|-------------|----------------|-------|-----------|
| H1 (hero) | Bodoni Moda 500 | 64px | 50px | 36px | 1.05 | 0.01em | Ivory (on Deep Wine) | UPPERCASE |
| H2 | Bodoni Moda 400 | 46px | 38px | 32px | 1.12 | 0 | Deep Wine (Ivory on dark) | none |
| H2 in final CTA | Bodoni Moda 400 | 50px | 42px | 32px | 1.12 | 0 | Deep Wine | none |
| Script line (in H1/H2) | Pinyon Script 400 | 1.2× heading | same | same | 1.15 | 0 | Wine / Soft Gold on dark | none |
| H3 | Bodoni Moda 400 | 24px | 24px | 22px | 1.3 | 0 | Deep Wine | none |
| H3 in benefit list | Bodoni Moda 400 | 22px | 22px | 21px | 1.3 | 0 | Deep Wine | none |
| Statement | Bodoni Moda italic 400 | 36px | 36px | 26px | 1.35 | 0 | Deep Wine | none |
| Testimonial quote | Bodoni Moda italic 400 | 19px | 19px | 19px | 1.6 | 0 | Deep Wine | none |
| Step numeral (I, II, III) | Bodoni Moda 500 | 40px | 40px | 40px | 1 | 0.08em | Gold | none |
| Eyebrow | League Spartan 500 | 12px | 12px | 12px | 1.4 | 0.3em | Wine (Soft Gold on dark) | UPPERCASE |
| Body | Quicksand 500 | 17px | 17px | 16px | 1.75 | 0 | Espresso (Cream on dark) | none |
| Lead (hero paragraph) | Quicksand 500 | 19px | 19px | 17px | 1.75 | 0 | Cream | none |
| Small body (benefit text) | Quicksand 500 | 16px | 16px | 16px | 1.75 | 0 | Espresso | none |
| Button | League Spartan 600 | 13px | 13px | 13px | 1 | 0.2em | see buttons | UPPERCASE |
| Button, small | League Spartan 600 | 12px | 12px | 12px | 1 | 0.2em | see buttons | UPPERCASE |
| Nav link | League Spartan 500 | 13px | 14px (menu) | 14px (menu) | 1 | 0.16em | Espresso; Wine when active/hover | UPPERCASE |
| Top bar | League Spartan 500 | 11px | 11px | 10px | 1.4 | 0.3em (0.12em mobile) | Soft Gold | UPPERCASE |
| Trust points | League Spartan 500 | 12px | 12px | 12px | 1.4 | 0.16em | Cream | UPPERCASE |
| Signature names (testimonials, countdown) | Pinyon Script 400 | 30px | 30px | 30px | 1.15 | 0 | Wine | none |
| Countdown digits | Bodoni Moda 500 | 34px | 34px | 30px | 1 | 0 | Deep Wine | none |
| Countdown labels | League Spartan 500 | 10px | 10px | 10px | 1 | 0.2em | Taupe | UPPERCASE |
| Footer column title | League Spartan 600 | 12px | 12px | 12px | 1.4 | 0.26em | Soft Gold | UPPERCASE |
| Footer text | Quicksand 500 | 15px | 15px | 15px | 1.75 | 0 | Cream | none |

Paragraph spacing: 20px. Heading margin below: 20px (H1 28px, H3 10px).

---

## 5. Layout, spacing, shapes

| Token | Value |
|-------|-------|
| Content width (boxed containers) | **1200px** |
| Side padding (gutter) | 24px desktop/tablet, **20px mobile** |
| Section padding top/bottom | **120px** desktop, **96px** tablet, **76px** mobile |
| Section heading block (eyebrow + H2 + intro) | centered, max width 860px, **64px** below (44px mobile) |
| Gap before a section's closing button | 56px (40px mobile) |
| Column gap, 2-column split sections | 88px desktop, 48px tablet, 48px mobile (stacked) |
| Card grid gap | 32px (24px mobile) |
| Button radius | **2px** (crisp, stationery-like) |
| Cards and frames | **square corners** |
| Arch shape | top-left and top-right radius **400px**, bottom corners 0 |
| Floating mobile button | pill, radius 999px |
| Soft shadow (countdown card, phone) | `0 24px 50px -28px rgba(61,11,33,0.45)` |

Elementor setup: Site Settings > Layout > Content Width **1200**. Use **Flexbox Containers**.

### Backgrounds

| Name | Elementor background settings |
|------|------------------------------|
| **Ivory paper** | Color Ivory + image `prototype/assets/images/paper-texture.png`, repeat, size auto |
| **Champagne paper** | Color Champagne + the same texture image |
| **Deep Wine pattern** | Color Deep Wine + image `prototype/assets/images/pattern-rings.svg`, repeat, size auto (180px tile) |

---

## 6. Buttons

All buttons: League Spartan 600, 13px, UPPERCASE, letter spacing 0.2em, line height 1,
padding **19px 34px**, border 1px solid, radius **2px**, transition 0.3s on colors.
On mobile, buttons in a button row are **full width** (stacked, 16px gap).

| Style | Normal | Hover | Used for |
|-------|--------|-------|----------|
| **Primary** | bg Wine `#721840`, text Ivory, border Wine | bg Wine Hover `#5A1232` | Main action on light backgrounds |
| **Secondary** (outline) | transparent, text Wine, border Wine | bg Wine, text Ivory | Second action on light backgrounds |
| **Gold** | bg Soft Gold `#C9A96E`, text Deep Wine, border Soft Gold | bg Cream `#EFE5D6`, border Cream | Main action on Deep Wine (hero) |
| **Light** (outline on dark) | transparent, text Ivory, border Soft Gold | bg Soft Gold, text Deep Wine | Second action on Deep Wine, footer |
| **Small** (modifier) | padding 15px 24px, font 12px | same as its style | Header "Contact Us", footer button |

Never more than two buttons side by side.

---

## 7. Reusable components

**Invitation frame.** Elementor: an outer container with a 1px Gold border and 8px padding (6px mobile),
containing an inner container with a 1px `rgba(176,141,87,0.45)` border that holds the content.
Background Ivory. Square corners. Used for step cards, couple/guest cards, testimonials, the countdown card and the final CTA card.

**Ornament.** A 64px Gold line, a 9px Gold diamond (`prototype/assets/icons/diamond.svg`), then another 64px line, centered, 14px gaps.
Elementor: Divider widget with a "diamond" element, or three items in a row container.

**Arch photo.** An outer container with a 1px Gold border, 12px padding, and radius 400px 400px 0 0.
Inside, an Image widget with the same arch radius (object-fit cover, 4:5 ratio).

**Diamond bullet list** (Icon List). Icon `diamond.svg` (Gold) or `diamond-light.svg` (Soft Gold on dark) at 9px, 18px text indent, 12px between items.

**Icon benefit list.** A 40×40 Wine line icon (`prototype/assets/icons/`), then H3 and a short paragraph. 22px gap, 26px between items. Use the Icon Box widget, icon position left.

**Wax seal.** `prototype/assets/images/wax-seal.svg` (gold seal pressed with the rings mark). Drop shadow `0 8px 14px rgba(0,0,0,0.35)` (Elementor: Image > CSS Filters or Box Shadow).

**Photo placeholders.** The soft gradient boxes in the prototype stand in for real photos. Each one is labeled with the photo that goes there. Replace them with Image widgets, and use the label as the alt text.

**Device mockups.** Use the exported images instead of rebuilding them:
- `prototype/assets/images/hero-mockup.png`: laptop and phone, transparent background.
- `prototype/assets/images/memory-mockup.png`: phone in Memory Mode, transparent background.

**Icons** (`prototype/assets/icons/`): `sparkle.svg`, `message-check.svg`, `award.svg`, `seal.svg`,
`check-circle.svg`, `heart.svg`, `diamond.svg`, `diamond-light.svg`. Upload them as SVG (enable SVG uploads in Elementor settings).

---

## 8. Header (Theme Builder > Header, entire site)

**Top bar** (above the header): full width, Deep Wine, padding 12px (10px mobile), centered text
**NOW WELCOMING PARTNER PLANNERS FOR 2027 WEDDINGS** in the "Top bar" type style. It scrolls away; only the header below is sticky.

**Header row:**
- **Sticky** (Motion Effects > Sticky: Top, all devices). Background `rgba(251,247,241,0.97)`, 1px Line bottom border.
  Height **92px** desktop, **76px** mobile.
- **Left:** logo `brand/logo-rings/rings-horizontal.svg`, width 240px (190px mobile), links to Home.
- **Right:** Nav Menu with exactly six items: **Home, How It Works, Features, Designs, Pricing, About**.
  30px between items. Active/hover: Wine text with a 1px Gold underline.
- **Far right:** **"Contact Us"** Primary button (small) → Contact page. Always visible on desktop.
- **Tablet & mobile (≤1024px):** hide the inline menu and header button. Show a hamburger labeled "MENU" (Deep Wine).
  The dropdown is full width and Ivory, with the six links (14px, 18px vertical padding, 1px Line dividers),
  then a full-width Primary **"Contact Us"** button.

### Floating mobile contact button
- **Mobile only.** Text **"Contact"** → Contact page. Position **fixed**, bottom 16px, right 16px.
- Wine background, Ivory text, 1px Soft Gold border, League Spartan 600 12px uppercase, 0.2em letter spacing,
  padding 15px 24px, pill radius, shadow `0 10px 24px -8px rgba(61,11,33,0.6)`.
- Give the footer 104px bottom padding on mobile so the button never covers the copyright line.

---

## 9. Final call to action (on EVERY page, just above the footer)

Build once as a **Saved Template** and insert it at the bottom of every page (not on Contact).

- Full-width container, **Champagne paper** background, top padding 140px (116px mobile), bottom 120px.
- Centered **invitation frame** card, Ivory, max width 880px, padding 88px 64px 72px (72px 24px 48px mobile):
  1. Wax seal image, 104px (88px mobile), **negative top margin −140px** (−118px mobile) so it sits on the card's top edge
  2. Eyebrow: **BECOME A PARTNER PLANNER**
  3. H2 (CTA size): **Let's create something** `<span class="script">beautiful together</span>`
  4. Text (max 600px, centered): **Tell me about your business and the weddings you plan. I'll reply within 24 hours with everything you need to get started.**
  5. Buttons: **Contact Us** (Primary → Contact) + **View Pricing** (Secondary → Pricing). On the Pricing page use **See How It Works** instead.

---

## 10. Footer (Theme Builder > Footer, entire site)

- **Deep Wine pattern** background, Cream text 15px. Padding 96px top, 32px bottom (72px / 104px mobile).
- Three columns (2fr / 1fr / 1.3fr), 48px gap. Tablet: logo full width, then two columns. Mobile: stacked.
  1. Logo `brand/logo-rings/rings-horizontal-light.svg` (280px; 240px mobile) + **Premium, custom wedding websites, offered by the planners who make the day happen.**
  2. **EXPLORE**: Home, How It Works, Features, Designs, Pricing, About
  3. **GET IN TOUCH**: hello@theoccasionroom.com · +1 (000) 000-0000 · Instagram: @theoccasionroom (placeholders) + **Contact Us** Light button (small)
- Bottom bar: 64px above (44px mobile), 1px `rgba(201,169,110,0.3)` top border, 24px padding, 13px `#BFA99A`:
  **© 2026 The Occasion Room. All rights reserved.**
- Links Cream, no underline, Soft Gold on hover.

---

## 11. Pages

### 11.1 Home (build exactly as below)

Each numbered block is one full-width container with a boxed 1200px inner container.

**1. Hero** (Deep Wine pattern; top padding 88px desktop/tablet, 56px mobile; bottom padding 0; centered text)
- Wax seal image, 96px (76px mobile), centered, 28px below
- Eyebrow (Soft Gold): **CUSTOM WEDDING WEBSITES FOR PLANNERS**
- H1 (max width 900px): **Bespoke wedding websites** `<span class="script">your couples will treasure</span>` (script at 1.22em, 6px above)
- Lead (Cream, max width 700px): **Premium, custom-made wedding websites you offer as part of your planning packages. Every detail for guests and couples, all in one place, and a keepsake that lasts long after the last dance.**
- Buttons (40px above, 28px below, centered): **Become a Partner Planner** (Gold → Contact) + **See How It Works** (Light → How It Works)
- Trust points (inline, centered, 36px gaps, Soft Gold diamonds): **Done for you** · **Your branding on every site** · **Made for phones first**
- **Mockup** (72px below the trust points; 48px on mobile), centered, max width 900px:
  image `hero-mockup.png` (alt: "A sample wedding website for Isabella and Mateo, shown on a laptop and a phone").
  It **hangs into the next section**: negative bottom margin **−150px** desktop, −110px tablet, −60px mobile, z-index 2.
- **Live countdown card** (invitation frame, Ivory, soft shadow, padding 24px 32px 22px, centered text):
  - Script name: **Isabella & Mateo** (Pinyon Script 30px, Wine)
  - Label: **COUNTING DOWN TO THE BIG DAY** (League Spartan 500, 10px, 0.24em, Taupe)
  - Elementor **Countdown** widget (Pro): due date **12 June 2027, 16:00**, Days / Hours / Min / Sec, no boxes, 20px gap.
  - Desktop: Position Absolute over the bottom-left of the mockup (left −48px, bottom −24px); tablet left 0.
    Mobile: normal flow, centered, 16px below the mockup.

**2. Statement** (Ivory paper; top padding = section padding + the mockup overhang: 270px desktop, 206px tablet, 136px mobile)
- Centered, max width 900px: ornament (28px below)
- Statement text (Bodoni italic): **A wedding website should feel like the invitation: considered, personal, and unmistakably theirs.**
- Signature line (Pinyon Script 38px, 32px mobile, Wine): **Every detail. One room.**

**3. How it works** (Champagne paper)
- Head: eyebrow **HOW IT WORKS**, H2 **Effortless for you,** `<span class="script">unforgettable for them</span>`
- Three invitation-frame cards (Ivory), 32px gap, centered text, padding 56px 36px 48px.
  Tablet and mobile: one column, max 560px, 24px gap.
  Each card: Roman numeral (Gold), a 9px Gold diamond 18px below it, H3, paragraph.
  - **I · You partner with us**: Add a custom wedding website to your planning packages. Send us your couple's details and we take it from there.
  - **II · We design and build each site**: Every site is personalized to the couple's style, colors, and story, with your branding included. No templates, no extra work for you.
  - **III · Guests RSVP, the couple keeps the memory**: Guests find every detail and reply in moments. After the wedding, the site becomes a keepsake the couple can return to for years.
- Button: **See the Full Process** (Secondary → How It Works)

**4. For planners** (Ivory)
- Two columns **42% / 58%**, 88px gap, vertically centered. Mobile: arch photo on top (max 360px, centered).
- Left: **arch photo** (4:5). Placeholder: *planner with a client, reviewing the site on a tablet*.
- Right:
  - Eyebrow **FOR WEDDING PLANNERS**, H2 **Make your service look** `<span class="script">even more polished</span>`
  - Text: **A custom wedding website is a thoughtful touch that makes your clients feel cared for, and quietly shows the level of detail you bring to every wedding.**
  - Icon benefit list (32px above, 44px below):
    - `sparkle.svg` **A premium client experience**: Give your couples something personal and beautifully finished, as part of your package.
    - `message-check.svg` **Fewer guest questions**: Times, addresses, dress codes, and hotels live in one place, so guests stop calling you and your couple.
    - `award.svg` **Stand out from other planners**: Offer something your competitors don't, and give couples one more reason to choose you.
    - `seal.svg` **Your branding on every site**: Each site carries a discreet "Planned by" credit with your logo, seen by every guest.
    - `check-circle.svg` **No extra work**: We handle design, setup, and updates. You simply send us the details.
  - Button: **Become a Partner Planner** (Primary → Contact)

**5. For couples & guests** (Champagne paper)
- Head: eyebrow **FOR COUPLES & GUESTS**, H2 **Everything for the day,** `<span class="script">all in one place</span>`, text **A customized home for a once-in-a-lifetime day, made to feel completely like them.**
- Two invitation-frame cards (Ivory, padding 20px; 14px mobile), 32px gap, stacked on mobile.
  Each: a 16:9 photo with an arch top (radius 300px 300px 0 0), then a centered H3 and a diamond list (max 440px, left-aligned).
  - Photo *the couple* (alt "A couple smiling together outdoors"). H3 **For the couple**:
    A site that feels completely theirs, in their colors and style · Smart RSVPs with meal choices, dietary needs, and song requests · Every reply gathered in one tidy list, shared with their planner · A keepsake of their day, long after the wedding
  - Photo *guests at the celebration* (alt "Wedding guests checking the schedule on a phone"). H3 **For their guests**:
    The schedule, addresses, and map links at a glance · Dress code inspiration for every event · Travel and hotel details, clearly explained · An RSVP that takes less than a minute, on any phone

**6. Memory mode** (Deep Wine pattern, overflow hidden)
- A decorative Heading widget **Forever** (Pinyon Script 260px, 150px mobile, color `rgba(201,169,110,0.10)`),
  Position Absolute, top-left (left −20px, top 20px), behind the content, hidden from screen readers.
- Two columns **55% / 45%**, 88px gap. Mobile: phone image on top.
- Left:
  - Eyebrow **MEMORY MODE** (Soft Gold), H2 **When the day is over,** `<span class="script">the story stays</span>`
  - Text: **After the wedding, each site gently becomes a keepsake: a heartfelt thank-you to guests, favorite photos, and memories from the day, kept in one lovely place the couple can revisit and share.**
  - Diamond list (Soft Gold): A thank-you message to every guest · A gallery of photos from the day · Guest photos collected by QR code at the reception (Luxe)
  - Button: **Explore All Features** (Light → Features)
- Right: image `memory-mockup.png`, centered, max 280px (alt "A wedding website in memory mode, showing a thank-you message and photos").

**7. Testimonials** (Ivory paper). **Placeholders: replace with real quotes before launch.**
- Head: eyebrow **KIND WORDS**, H2 **Loved by planners** `<span class="script">and their couples</span>`
- Three invitation-frame cards (Ivory, padding 48px 40px 40px, centered), 32px gap; one column on tablet and mobile (max 640px).
  Each: a Gold Bodoni quotation mark (72px), the quote (Bodoni italic), the name in script (Wine), and a detail line (Taupe 14px).
  1. "My couples were overjoyed. It felt like an extension of the whole planning experience, and my phone finally stopped ringing with guest questions." *Planner Name*, Studio Name · City
  2. "It matched our invitations perfectly. Our guests kept telling us how beautiful and easy it was, and we still visit it to relive the day." *Couple Names*, Married in City, 2026
  3. "Adding The Occasion Room to my packages was the easiest upgrade I've made. It looks premium, and I don't lift a finger." *Planner Name*, Studio Name · City

**8. Final call to action**: the saved template from section 9.

**Page SEO:** title "The Occasion Room | Custom Wedding Websites for Planners"; meta description
"Premium, custom wedding websites that wedding planners offer their couples. Every detail in one place, and a keepsake that lasts."

### 11.2 How It Works (planned; full spec after approval)
Hero (title + intro) → full step-by-step timeline (partnering → onboarding → design → review → launch and RSVPs → wedding day → memory site) → "What we need from you" (couple's details, photos, guest list) → typical turnaround (placeholder) → general FAQ (accordion) → Final CTA.

### 11.3 Features (planned)
Hero → feature grid with small icons and benefit-focused text: live countdown; smart RSVP; RSVP results shared with couple and planner; schedule with maps; dress code per event; guest guidelines; travel and hotels; menu, our story, gallery, wedding party, registry, FAQ; password protection; mobile-first; planner branding; memory mode; guest photo gallery (Luxe) → Final CTA.

### 11.4 Designs (planned)
Hero → gallery of sample designs (Classic, Modern, Garden, Romantic, Minimalist) → note "Every design is personalized for each couple" → Final CTA.

### 11.5 Pricing (planned)
Hero → three packages (Essential, **Signature: Most Popular**, Luxe) with placeholder prices → Partner Bundles (single, 3, 5, 10+) and how credits work (Essential 1, Signature 2, Luxe 3; valid 12 months; mix packages; include or resell at your own price) → pricing FAQ → custom quote CTA → Final CTA.

### 11.6 About (planned)
Hero → story (placeholder text) with photo placeholder → values → Final CTA.

### 11.7 Contact (planned)
Welcoming headline → form (Elementor Form widget): name, business name, email, phone, city, weddings per year, interested package/bundle (dropdown), message → email, phone, Instagram → "What happens next: I'll get back to you within 24 hours." No final CTA section on this page.

---

## 12. Motion and effects

Keep motion slow and graceful. Only use effects Elementor provides natively:
- **Entrance animation:** "Fade In Up", duration *Slow* (about 1s), on section heads, cards and images. Within a row, stagger by 150ms.
- **Hover:** button color transitions (0.3s), nav underline, footer link color. No scaling or bouncing.
- **Sticky header**, **fixed floating mobile button**, live **Countdown**.
- No parallax, particles, typing effects or scroll-jacking.

---

## 13. Accessibility and quality checklist

- Every image has alt text (given above). Decorative images (seal, pattern, "Forever", icons) get empty alt text.
- Text contrast follows section 3. Never put Gold text under 24px on a light background.
- Body text at least 16px on mobile. Buttons at least 44px tall (about 52px here).
- One H1 per page. Section titles are H2, card and item titles are H3.
- Check each page at 390px, 768px and 1440px. There must be no sideways scrolling.
- Compress photos (WebP, under 200 KB where possible). Use SVG for logos, icons, the seal and the pattern.

---

## 14. Asset list

| File | Use |
|------|-----|
| `brand/logo-rings/rings-horizontal.svg` | Header logo |
| `brand/logo-rings/rings-horizontal-light.svg` | Footer logo |
| `brand/logo-rings/favicon.svg`, `png/rings-icon-wine.png` | Site icon |
| `prototype/assets/images/wax-seal.svg` | Hero seal, CTA seal |
| `prototype/assets/images/pattern-rings.svg` | Deep Wine background pattern (repeat) |
| `prototype/assets/images/paper-texture.png` | Ivory/Champagne paper texture (repeat) |
| `prototype/assets/images/hero-mockup.png` | Hero devices |
| `prototype/assets/images/memory-mockup.png` | Memory Mode phone |
| `prototype/assets/icons/*.svg` | Benefit icons and diamond bullets |
| `brand/build_rings_logo.py` | Rebuilds every rings logo file |
