# The Occasion Room: Design Guide for the Elementor Build

This guide is the blueprint for rebuilding the marketing site in **WordPress + Elementor**
(Hostinger, built through the Novamira MCP plugin). It is written so a person or an AI agent
can follow it step by step without guessing.

- **Visual reference:** `prototype/index.html` (open in a browser). Screenshots are in `prototype/screenshots/`.
- **Source of truth for values:** `prototype/css/style.css`. If this guide and the CSS ever disagree, the CSS wins.
- **Status:** Homepage designed and ready to build. The other pages are outlined in section 10 and get full
  specs and final text as each one is approved.

---

## 1. Brand feeling (read first)

Premium, warm, personal, like a high-end wedding stationery brand. Lots of ivory space, wine accents,
a small touch of gold, thin elegant lines. Never busy, never "techy". When in doubt: more white space,
fewer effects.

Audience: **wedding planners** first (they buy), couples second. The single main action everywhere is
**contacting us / becoming a partner planner**. The contact page must never be more than one click away.

---

## 2. Colors

Set these up as **Elementor Global Colors** (Site Settings > Global Colors) using these exact names.

| Global name  | Hex       | Role |
|--------------|-----------|------|
| Ivory        | `#FBF7F1` | Page background, card backgrounds on Champagne, text on dark backgrounds |
| Champagne    | `#F2E8DA` | Alternate section background, testimonial cards |
| Line         | `#DCCBB8` | Borders, dividers, card outlines, header bottom border |
| Taupe        | `#7A6358` | Muted text: captions, small labels, testimonial details (contrast 5.2:1 on Ivory) |
| Espresso     | `#3B2A2D` | Body text (12.6:1 on Ivory) |
| Deep Wine    | `#3F0E18` | Headings, dark sections (Memory Mode), footer background |
| Wine         | `#6E1F2F` | **Accent**: primary buttons, links, eyebrows, icons |
| Wine Hover   | `#561623` | Primary button hover |
| Gold         | `#B08D57` | Decoration on light backgrounds only: step numbers, thin rules, diamond bullets, quote marks, nav underline. **Never for body text.** |
| Soft Gold    | `#C9A96E` | Accents and small labels on Deep Wine (7.3:1), light-button border |

Extra fixed colors (no global needed):

| Hex | Where |
|-----|-------|
| `#FFFFFF` | Countdown card background |
| `#EFE4D6` | Body text inside the Deep Wine Memory Mode section |
| `#E6D8C6` | Footer body text and links |
| `#BFAE9C` | Footer copyright line |
| `#2B1B1F` | Device frames in the mockups (already baked into the images) |
| `rgba(251,247,241,0.96)` | Sticky header background (Ivory at 96%) |

Contrast rules: body text is always Espresso on Ivory or Champagne, or `#EFE4D6` / Ivory on Deep Wine.
Gold is only for decoration or text 24px and larger.

---

## 3. Typography

Load from Google Fonts (Elementor lists all three). Set as **Global Fonts** (Site Settings > Global Fonts).

| Font | Use | Weights |
|------|-----|---------|
| **Italiana** | Headings (display serif) | 400 (only weight) |
| **Quicksand** | Body text, countdown numbers | 400, 500, 600 |
| **League Spartan** | Eyebrows, buttons, navigation, labels (always UPPERCASE) | 500, 600 |

Italiana has one weight. Never bold it and never use it below 20px.

### Type scale

Elementor breakpoints: **Desktop > 1024px**, **Tablet ≤ 1024px**, **Mobile ≤ 767px** (the defaults).

| Style | Font / weight | Desktop | Tablet | Mobile | Line height | Letter spacing | Color | Transform |
|-------|---------------|---------|--------|--------|-------------|----------------|-------|-----------|
| H1 | Italiana 400 | 60px | 48px | 40px | 1.08 | 0 | Deep Wine | none |
| H2 | Italiana 400 | 46px | 38px | 32px | 1.15 | 0 | Deep Wine (Ivory on dark) | none |
| H2 in final CTA | Italiana 400 | 52px | 42px | 34px | 1.15 | 0 | Deep Wine | none |
| H3 | Italiana 400 | 26px | 26px | 24px | 1.25 | 0 | Deep Wine | none |
| H3 in benefit list | Italiana 400 | 24px | 24px | 22px | 1.25 | 0 | Deep Wine | none |
| Eyebrow (small label above H2) | League Spartan 500 | 13px | 13px | 13px | 1.4 | 0.2em (2.6px) | Wine (Soft Gold on dark) | UPPERCASE |
| Body | Quicksand 500 | 17px | 17px | 16px | 1.7 | 0 | Espresso | none |
| Lead (hero paragraph) | Quicksand 500 | 19px | 19px | 17px | 1.7 | 0 | Espresso | none |
| Small body (benefit text) | Quicksand 500 | 16px | 16px | 16px | 1.7 | 0 | Espresso | none |
| Button | League Spartan 600 | 14px | 14px | 14px | 1 | 0.12em (1.7px) | see buttons | UPPERCASE |
| Button, small | League Spartan 600 | 13px | 13px | 13px | 1 | 0.12em (1.6px) | see buttons | UPPERCASE |
| Nav link | League Spartan 500 | 14px | 15px (in menu) | 15px (in menu) | 1 | 0.1em (1.4px) | Espresso; Wine when active/hover | UPPERCASE |
| Trust points / small caps labels | League Spartan 500 | 13px | 13px | 13px | 1.4 | 0.08em | Taupe | UPPERCASE |
| Testimonial name | League Spartan 600 | 14px | 14px | 14px | 1.4 | 0.1em | Deep Wine | UPPERCASE |
| Testimonial detail | Quicksand 500 | 14px | 14px | 14px | 1.5 | 0 | Taupe | none |
| Footer column title | League Spartan 600 | 13px | 13px | 13px | 1.4 | 0.18em | Soft Gold | UPPERCASE |
| Footer text | Quicksand 500 | 15px | 15px | 15px | 1.7 | 0 | `#E6D8C6` | none |
| Step number (01, 02, 03) | Italiana 400 | 56px | 56px | 56px | 1 | 0 | Gold | none |
| Countdown digits | Quicksand 500 | 32px | 32px | 28px | 1 | 0 | Deep Wine | none |
| Countdown labels | League Spartan 500 | 10px | 10px | 10px | 1 | 0.16em | Taupe | UPPERCASE |

Paragraph spacing: 20px below each paragraph. Heading margin below: H1 24px, H2 20px, H3 10px (4px in benefit list).

---

## 4. Layout, spacing, shapes

| Token | Value |
|-------|-------|
| Content width (boxed containers) | **1200px** |
| Side padding (gutter) | 24px desktop/tablet, **20px mobile** |
| Section padding top/bottom | **112px** desktop, **88px** tablet, **72px** mobile |
| Hero section top padding | 88px desktop/tablet, 48px mobile (bottom as normal section) |
| Section heading block (eyebrow + H2 + intro) | centered, max width 860px, **64px** gap below (44px mobile) |
| Gap before a section's closing button | 56px (40px mobile) |
| Column gap, 2-column split sections | 80px desktop, 48px tablet, 40px mobile (stacked) |
| Column gap, hero | 56px desktop, 48px stacked |
| Card grid gap | 32px (24px mobile) |
| Border radius: buttons, small elements | **4px** |
| Border radius: cards, photos | **8px** |
| Border radius: floating mobile button | 999px (pill) |
| Card border | 1px solid Line `#DCCBB8` |
| Soft shadow (cards that float, countdown) | `0 18px 40px -24px rgba(63,14,24,0.35)` |
| Section background alternation | Ivory, Champagne, Ivory, Champagne, Deep Wine, Ivory, Champagne (CTA), Deep Wine (footer) |

Elementor setup: Site Settings > Layout > Content Width **1200**, Container padding 24px (mobile 20px).
Use **Flexbox Containers** (not old sections/columns).

---

## 5. Buttons

All buttons: League Spartan 600, 14px, UPPERCASE, letter spacing 0.12em, line height 1,
padding **18px 30px**, border 1px solid, radius **4px**, transition 0.25s on colors.
On mobile, buttons inside a button row are **full width** (stacked, 16px gap).
Button text is always clear action wording ("Contact Us", "Become a Partner Planner").

| Style | Normal | Hover | Used for |
|-------|--------|-------|----------|
| **Primary** | bg Wine `#6E1F2F`, text Ivory, border Wine | bg Wine Hover `#561623`, border Wine Hover, text Ivory | Main action: Contact Us, Become a Partner Planner |
| **Secondary** (outline) | bg transparent, text Wine, border Wine | bg Wine, text Ivory | Second action next to a primary: See How It Works, View Pricing |
| **Light** (on dark) | bg transparent, text Ivory, border Soft Gold `#C9A96E` | bg Soft Gold, text Deep Wine | Buttons on Deep Wine sections and footer |
| **Small** (modifier) | padding 14px 22px, font 13px | same as its style | Header "Contact Us", footer button |

Button rows: horizontal, 16px gap, wrap allowed. Never more than two buttons side by side.

---

## 6. Reusable components

**Eyebrow + heading block.** Every section starts with an eyebrow label (League Spartan, uppercase, Wine),
then an H2. Centered for full-width sections, left-aligned inside split sections.

**Diamond bullet list** (Elementor Icon List). Icon: `prototype/assets/icons/diamond.svg` (Gold) at 10px,
or `diamond-light.svg` (Soft Gold) on Deep Wine. 18px space between icon and text, 12px between items.

**Icon benefit list.** Icon (40×40px, line style, Wine, files in `prototype/assets/icons/`) on the left,
H3 + short paragraph on the right, 20px gap, 24px between items. In Elementor, use an **Icon Box** widget
with the icon positioned left, or a small container with an Image widget + Text.

**Photo placeholders.** Soft gradient boxes with a small label saying which photo goes there. Replace
each with a real **Image** widget (radius 8px, object-fit cover) at the same aspect ratio, and use the
label text as the image's alt text. The gradients are only stand-ins.

**Cards.** Ivory background, 1px Line border, 8px radius, photo on top, body padding 36px 40px 40px
(28px 24px 32px mobile).

**Quote cards.** Champagne background, 8px radius, padding 40px 36px 36px. A big Gold opening quote
mark (Georgia serif, 64px), the quote in Body style, then a 1px Line divider, the name (small caps) and
a detail line (Taupe).

**Device mockups.** Use the exported images instead of rebuilding them:
- `prototype/assets/images/hero-mockup.png`: laptop and phone, transparent background.
- `prototype/assets/images/memory-mockup.png`: phone in Memory Mode, transparent background.

**Icons available** (`prototype/assets/icons/`): `sparkle.svg`, `message-check.svg`, `award.svg`,
`seal.svg`, `check-circle.svg`, `heart.svg`, `diamond.svg`, `diamond-light.svg`. Upload them as SVG
(Elementor: Settings > Features > enable SVG uploads, or use Elementor's "Upload SVG" in the Icon picker).

---

## 7. Header (Theme Builder > Header, applied to the entire site)

- **Sticky** at the top (Motion Effects > Sticky: Top, all devices). Background `rgba(251,247,241,0.96)`,
  1px Line bottom border. Height **88px** desktop, **72px** mobile.
- **Left:** logo `brand/logo-wine/occasion-room-horizontal.svg`, width 250px (180px mobile), links to Home.
- **Right:** Nav Menu widget with exactly six items: **Home, How It Works, Features, Designs, Pricing, About**.
  32px between items. Active/hover: Wine text with a 1px Gold underline.
- **Far right:** **"Contact Us"** Primary button (small) → Contact page. It is always visible on desktop
  because the header is sticky.
- **Tablet & mobile (≤1024px):** hide the inline menu and the header button. Show a hamburger toggle
  labeled "MENU" (Deep Wine). The dropdown is full width, Ivory, and lists the six links (15px, 18px
  vertical padding, 1px Line divider between items), then a full-width Primary **"Contact Us"** button.

### Floating mobile contact button

- **Mobile only** (hide on desktop and tablet). Text: **"Contact"** → Contact page.
- Position **fixed**, bottom 16px, right 16px, z-index above content.
- Wine background, Ivory text, League Spartan 600 13px uppercase, letter spacing 0.14em,
  padding 14px 22px, pill radius 999px, shadow `0 10px 24px -8px rgba(63,14,24,0.55)`.
- Elementor: a Button widget in the footer template with Advanced > Position: Fixed, or a
  "floating button" widget. Give the footer 104px bottom padding on mobile so the button never covers
  the copyright line.

---

## 8. Final call to action (on EVERY page, just above the footer)

Build once as a **Saved Template / Global Widget** and insert it at the bottom of every page.

- Full-width container, Champagne background, 1px Line top border, section padding.
- Centered content, max width 760px:
  1. Ampersand mark `brand/logo-wine/mark-ampersand.svg`, 56px wide, 24px below
  2. Eyebrow: **BECOME A PARTNER PLANNER**
  3. H2 (CTA size): **Let's create something beautiful together**
  4. Text: **Tell me about your business and the weddings you plan. I'll reply within 24 hours with everything you need to get started.** (36px below)
  5. Buttons (centered): **Contact Us** (Primary → Contact) + **View Pricing** (Secondary → Pricing)
- On the Pricing page, swap the secondary button for **See How It Works**. On the Contact page, leave this section out (the form is the call to action).

---

## 9. Footer (Theme Builder > Footer, entire site)

- Deep Wine background, text `#E6D8C6` 15px. Padding 88px top, 32px bottom (64px / 104px on mobile).
- Three columns (2fr / 1fr / 1.3fr), 48px gap. Tablet: logo column full width, then two columns. Mobile: stacked.
  1. Logo `prototype/assets/logo/occasion-room-horizontal-light.svg` (240px) + text: **Premium, custom wedding websites, offered by the planners who make the day happen.**
  2. Title **EXPLORE** + links: Home, How It Works, Features, Designs, Pricing, About
  3. Title **GET IN TOUCH** + hello@theoccasionroom.com, +1 (000) 000-0000, Instagram: @theoccasionroom (placeholders) + **Contact Us** Light button (small)
- Bottom bar: 64px above (44px mobile), 1px `rgba(201,169,110,0.3)` top border, 24px padding,
  13px `#BFAE9C`: **© 2026 The Occasion Room. All rights reserved.**
- Footer links: `#E6D8C6`, no underline, Soft Gold on hover.

---

## 10. Pages

### 10.1 Home (approved design: build exactly as below)

Each numbered block is one full-width Elementor container with a boxed 1200px inner container.

**1. Hero** (Ivory, top padding 88px)
- Two columns, **52% / 48%**, vertically centered, 56px gap. Tablet/mobile: stacked, text first.
- Left column:
  - Eyebrow: **CUSTOM WEDDING WEBSITES FOR PLANNERS**
  - H1: **Bespoke wedding websites your couples will treasure**
  - Lead text: **Premium, custom-made wedding websites you offer as part of your planning packages. Every detail for guests and couples, all in one place, and a keepsake that lasts long after the last dance.**
  - Buttons (32px above, 28px below): **Become a Partner Planner** (Primary → Contact) + **See How It Works** (Secondary → How It Works)
  - Trust points (Icon List, inline, Gold diamond, 28px gap): **Done for you** · **Your branding on every site** · **Made for phones first**
- Right column:
  - Image `hero-mockup.png` (alt: "A sample wedding website for Isabella and Mateo, shown on a laptop and a phone").
  - **Live countdown card** overlapping the bottom-left of the image: white card, 1px Line border,
    8px radius, soft shadow, padding 18px 24px 16px, centered.
    - Label: **ISABELLA & MATEO'S BIG DAY** (League Spartan 500, 11px, 0.18em, Wine)
    - Elementor **Countdown** widget (Pro), due date **12 June 2027, 16:00**, showing Days / Hours / Min / Sec,
      no boxes, 18px gap, digits and labels styled as in the type scale.
    - Desktop: Advanced > Position Absolute, left −32px, bottom 0. Mobile: normal flow, centered,
      −8px top margin so it slightly overlaps the image.

**2. How it works** (Champagne)
- Centered head: eyebrow **HOW IT WORKS**, H2 **Effortless for you. Unforgettable for them.**
- Three equal columns (40px gap; stacked on mobile with 44px gap), each centered:
  step number in Gold Italiana 56px, a 40px × 1px Gold rule (20px above and below), H3, paragraph.
  - **01 · You partner with us**: Add a custom wedding website to your planning packages. Send us your couple's details and we take it from there.
  - **02 · We design and build each site**: Every site is personalized to the couple's style, colors, and story, with your branding included. No templates, no extra work for you.
  - **03 · Guests RSVP, the couple keeps the memory**: Guests find every detail and reply in moments. After the wedding, the site becomes a keepsake the couple can return to for years.
- Centered button: **See the Full Process** (Secondary → How It Works)

**3. For planners** (Ivory)
- Two columns **42% / 58%**, 80px gap, vertically centered. Mobile: photo on top.
- Left: photo, 4:5 ratio (4:3 on mobile), 8px radius. Placeholder: *planner with a client, reviewing the site on a tablet*.
- Right:
  - Eyebrow **FOR WEDDING PLANNERS**, H2 **Make your service look even more polished**
  - Text: **A custom wedding website is a thoughtful touch that makes your clients feel cared for, and quietly shows the level of detail you bring to every wedding.**
  - Icon benefit list (32px above, 40px below):
    - `sparkle.svg` **A premium client experience**: Give your couples something personal and beautifully finished, as part of your package.
    - `message-check.svg` **Fewer guest questions**: Times, addresses, dress codes, and hotels live in one place, so guests stop calling you and your couple.
    - `award.svg` **Stand out from other planners**: Offer something your competitors don't, and give couples one more reason to choose you.
    - `seal.svg` **Your branding on every site**: Each site carries a discreet "Planned by" credit with your logo, seen by every guest.
    - `check-circle.svg` **No extra work**: We handle design, setup, and updates. You simply send us the details.
  - Button: **Become a Partner Planner** (Primary → Contact)

**4. For couples & guests** (Champagne)
- Centered head: eyebrow **FOR COUPLES & GUESTS**, H2 **Everything for the day, all in one place**, text **A customized home for a once-in-a-lifetime day, made to feel completely like them.**
- Two cards side by side (32px gap; stacked on mobile). Each: 16:9 photo on top, then H3 and a diamond list.
  - Card 1 photo: *the couple* (alt: "A couple smiling together outdoors"). H3 **For the couple**:
    - A site that feels completely theirs, in their colors and style
    - Smart RSVPs with meal choices, dietary needs, and song requests
    - Every reply gathered in one tidy list, shared with their planner
    - A keepsake of their day, long after the wedding
  - Card 2 photo: *guests at the celebration* (alt: "Wedding guests checking the schedule on a phone"). H3 **For their guests**:
    - The schedule, addresses, and map links at a glance
    - Dress code inspiration for every event
    - Travel and hotel details, clearly explained
    - An RSVP that takes less than a minute, on any phone

**5. Memory mode** (Deep Wine background, body text `#EFE4D6`, H2 in Ivory)
- Two columns **55% / 45%**, 80px gap. Mobile: image on top, then text.
- Left:
  - Eyebrow **MEMORY MODE** (Soft Gold), H2 **When the day is over, the story stays**
  - Text: **After the wedding, each site gently becomes a keepsake: a heartfelt thank-you to guests, favorite photos, and memories from the day, kept in one lovely place the couple can revisit and share.**
  - Diamond list (Soft Gold diamonds): A thank-you message to every guest · A gallery of photos from the day · Guest photos collected by QR code at the reception (Luxe)
  - Button: **Explore All Features** (Light → Features)
- Right: image `memory-mockup.png`, centered, max 280px wide (alt: "A wedding website in memory mode, showing a thank-you message and photos").

**6. Testimonials** (Ivory). **Placeholders: replace with real quotes before launch.**
- Centered head: eyebrow **KIND WORDS**, H2 **Loved by planners and their couples**
- Three quote cards (32px gap; one column on tablet and mobile, max 640px):
  1. "My couples were overjoyed. It felt like an extension of the whole planning experience, and my phone finally stopped ringing with guest questions." **PLANNER NAME**, Studio Name · City
  2. "It matched our invitations perfectly. Our guests kept telling us how beautiful and easy it was, and we still visit it to relive the day." **COUPLE NAMES**, Married in City, 2026
  3. "Adding The Occasion Room to my packages was the easiest upgrade I've made. It looks premium, and I don't lift a finger." **PLANNER NAME**, Studio Name · City

**7. Final call to action**: the global template from section 8.

**Page SEO:** title "The Occasion Room | Custom Wedding Websites for Planners"; meta description
"Premium, custom wedding websites that wedding planners offer their couples. Every detail in one place, and a keepsake that lasts."

### 10.2 How It Works (planned; full spec after approval)
Hero (title + intro) → full step-by-step timeline (partnering → onboarding → design → review → launch and RSVPs → wedding day → memory site) → "What we need from you" (couple's details, photos, guest list) → typical turnaround (placeholder) → general FAQ (accordion) → Final CTA.

### 10.3 Features (planned)
Hero → feature grid with small icons and benefit-focused text: live countdown; smart RSVP; RSVP results shared with couple and planner; schedule with maps; dress code per event; guest guidelines; travel and hotels; menu, our story, gallery, wedding party, registry, FAQ; password protection; mobile-first; planner branding; memory mode; guest photo gallery (Luxe) → Final CTA.

### 10.4 Designs (planned)
Hero → gallery of sample designs (Classic, Modern, Garden, Romantic, Minimalist) → note "Every design is personalized for each couple" → Final CTA.

### 10.5 Pricing (planned)
Hero → three packages (Essential, **Signature: Most Popular**, Luxe) with placeholder prices → Partner Bundles (single, 3, 5, 10+) and how credits work (Essential 1, Signature 2, Luxe 3; valid 12 months; mix packages; include or resell at your own price) → pricing FAQ → custom quote CTA → Final CTA.

### 10.6 About (planned)
Hero → story (placeholder text) with photo placeholder → values → Final CTA.

### 10.7 Contact (planned)
Welcoming headline → form (built with the WordPress/Elementor Form widget): name, business name, email, phone, city, weddings per year, interested package/bundle (dropdown), message → email, phone, Instagram → "What happens next: I'll get back to you within 24 hours." No final CTA section on this page.

---

## 11. Motion and effects

Keep motion subtle. Only use effects Elementor provides natively:
- **Entrance animation:** "Fade In Up", duration *Normal* (about 600ms), no delay or 100ms steps
  within a row. Apply to section headings, cards, and images, not to every line of text.
- **Hover:** button color transitions (0.25s), nav underline, footer link color. No scaling or bouncing.
- **Sticky header** and **fixed floating mobile button** (see section 7).
- Countdown ticks live (Countdown widget).
- No parallax, particle, typing, or scroll-jacking effects.

---

## 12. Accessibility and quality checklist

- Every image has alt text (suggested alt text is given above). Decorative icons get empty alt text.
- Text contrast follows section 2. Never put Gold text under 24px on a light background.
- Minimum body text 16px on mobile. Buttons at least 44px tall (they are about 52px).
- One H1 per page. Section titles are H2, card and item titles are H3.
- Check each page at 390px (phone), 768px (tablet) and 1440px (desktop). There must be no sideways scrolling.
- Compress images (WebP, under 200 KB each where possible). Use SVG for logos and icons.

---

## 13. Asset list

| File | Use |
|------|-----|
| `brand/logo-wine/occasion-room-horizontal.svg` | Header logo |
| `prototype/assets/logo/occasion-room-horizontal-light.svg` | Footer logo (transparent, light text) |
| `brand/logo-wine/mark-ampersand.svg` | Final CTA mark |
| `brand/logo-wine/favicon.svg`, `brand/logo-wine/png/icon-wine.png` | Site icon (Elementor: Site Settings > Site Identity) |
| `prototype/assets/images/hero-mockup.png` | Home hero image |
| `prototype/assets/images/memory-mockup.png` | Home Memory Mode image |
| `prototype/assets/icons/*.svg` | Benefit icons and diamond bullets |
| `brand/logo-wine/` | Full wine and gold logo set (PNG versions in `png/`) |
| `brand/logo/` | Original lavender logo set (kept for reference) |
