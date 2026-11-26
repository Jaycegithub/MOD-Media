# MOD Media: WordPress / Elementor Build Report

**Target:** https://healthy-mediumaquamarine-elk-60.hostingersite.com/ (staging)
**Reference:** MOD Media website concept (https://claude.ai/artifact/H9PQrsQ3kBqrSNBdRVWPbh)
**Date:** 26 November 2026 · Prepared by Jayce Cabangcala

Every result below was checked on the **published front end** (not the editor preview) with a real browser (Chromium/Playwright) at 1440px, 820px and 390px.

---

## 0. Fidelity check against the reference (v2 rebuild)

After the first build, the page was rebuilt from the reference's exact CSS values and then measured against the reference. A script compared the position, size and font of every text element section by section; this was repeated until the numbers matched.

**Section heights (px), reference → live:**

| Section | 1440 desktop | 820 tablet | 390 phone |
|---|---|---|---|
| Header | 75 → 75 | 75 → 75 | 75 → 75 |
| Hero | 910 → 910 | 1164 → 1164 | 1255 → 1256 |
| Brand strip | 129 → 129 | 129 → 129 | 129 → 129 |
| Campaigns | 1117 → 1117 | 1417 → 1417 | 2265 → 2265 |
| Brands | 846 → 846 | 971 → 971 | 1359 → 1360 |
| Try your ad | 1350 → 1350 | 1832 → 1833 | 1814 → 1814 |
| Plan a campaign | 881 → 881 | 990 → 990 | 1164 → 1164 |
| How it works | 688 → 688 | 844 → 844 | 1299 → 1299 |
| Gallery | 1392 → 1392 | 1373 → 1373 | 2397 → 2397 |
| Who we help | 501 → 501 | 490 → 490 | 953 → 953 |
| Reviews | 867 → 867 | 1120 → 1118 | 1246 → 1244 |
| Cities | 800 → 800 | 1397 → 1397 | 1385 → 1385 |
| Feature band | 520 → 520 | 520 → 520 | 530 → 530 |
| FAQ | 1225 → 1225 | 1147 → 1147 | 1383 → 1383 |
| Quote | 717 → 717 | 1062 → 1062 | 1331 → 1335 |
| Footer | 444 → 444 | 622 → 623 | 1020 → 1000 * |

\* The phone footer is 20px shorter only because the credit line now reads "Website by Jayce Cabangcala · hirejayce.com" instead of the concept's longer "Website design concept by…", which wrapped to two lines.

**Pixel comparison at 1440px** (share of identical pixels, same viewport):
- 97–99.7% for the header, campaigns, brands, try your ad, planner, how it works, gallery, who we help, reviews, FAQ, quote and footer.
- Hero: 99.4% with the animated truck hidden.
- Feature band: 93.4%. The remaining difference is a sub-pixel shift in the dot-matrix LED photo, which isn't visible.
- Brand strip: varies, because it's a moving marquee.

The remaining pixels are text anti-aliasing and 1px rounding. See `screenshots/compare-reference-vs-live-1440.jpg`.

**Intentional differences from the reference:**
- The concept-only pink "design concept" ribbon is removed.
- The footer credit wording is changed for production.
- Phones and tablets get a **menu button**. The reference simply hides the navigation below 1000px, which would leave mobile visitors without a menu. The menu button can be removed in one click if you want strict parity.
- The review carousel shows 6 position dots instead of 7, because Swiper counts positions rather than cards when 2 are visible.

---

## 1. Sections completed

The Home page (page ID **48**) is set as the static front page at the root URL, with a Theme Builder header (template **49**) and footer (template **50**) applied site-wide.

| # | Section | Anchor | Status |
|---|---|---|---|
| 1 | Sticky header: logo, menu, phone, Get Pricing | — | Done |
| 2 | Hero: skyline background, H1, intro, 2 CTAs, proof ticks, animated LED truck | — | Done |
| 3 | Trusted-by logo carousel (12 brands) | `#trusted` | Done |
| 4 | Campaigns: 4 service cards + 4 stat boxes | `#services` | Done |
| 5 | Brand wall: 12 glass logo tiles + trademark note | `#brands` | Done |
| 6 | Try your ad: ad builder | `#try` | Done |
| 7 | Plan your campaign: campaign planner | `#finder` | Done |
| 8 | How it works: 4 steps | `#how` | Done |
| 9 | Gallery: 8 real campaign photos, lightbox | `#gallery` | Done |
| 10 | Who we help: 11 industry chips | `#industries` | Done |
| 11 | Client reviews: 5.0 summary + carousel of 7 real Google reviews | `#results` | Done |
| 12 | Cities we serve: DFW / Texas / Nationwide | `#markets` | Done |
| 13 | KHAITE featured campaign band | — | Done |
| 14 | FAQ: 8 questions | `#faq` | Done |
| 15 | Quote form + contact details | `#quote` | Done |
| 16 | Footer: about, campaigns, cities, contact, credit | — | Done |
| 17 | Mobile sticky Call / Text / Get Pricing bar | — | Done |

Content comes from the approved concept, which is based on MOD Media's existing site and Google reviews. No content, ratings or claims were invented.

## 2. Global styling configured (Site Settings → Default Kit)

- **Colors:**
  - System colors: Primary `#2EE6F0`, Secondary `#FF3D8B`, Text `#EEF2FB`, Accent `#FFC24B`.
  - Nine named custom colors: page background, alt background, panel, muted text, border, button text, soft cyan, cyan hover, ghost.
- **Typography:**
  - Plus Jakarta Sans for headings and Inter for body text.
  - Named global styles: Hero H1, Section H2, Card H3, Lead paragraph, Small text, Button, Navigation.
  - The hero and section headings have responsive sizes (78/56/42px and 54/42/32px).
- **Buttons:** cyan background with dark text, pill shape, 16×26 padding, hover `#7DF3F8`, visible keyboard focus ring.
- **Form fields:** dark field style.
- **Layout:** 1160px content width plus 20px gutters (the reference's 1200px wrap), page background `#06080F`.
- **Breakpoints:** set to the reference's own, **tablet ≤1000px and mobile ≤640px**, in Site Settings → Layout → Breakpoints.
- **Fluid type:** the Hero and Section heading globals use the reference's exact `clamp()` sizes. Letter-spacing is in em, as in the reference.
- **Fallback fonts:** set to `system-ui, -apple-system, Segoe UI, Roboto, sans-serif`, so glyphs Inter lacks (such as →) render the same as the reference.
- **Global utility classes** in Site Settings → Custom CSS (`mm-*`). These cover effects Elementor has no controls for: the glowing eyebrow dot, button glow, hero and feature-band gradient layers, glass logo tiles, gallery caption pills, chips, review cards and controls, FAQ cards, form option cards, and the header blur.
- Widgets reference these globals, so a color or font change in Site Settings updates the whole page.

## 3. Widgets and containers used

Everything uses **standard Elementor (V3) containers and widgets**. The Atomic Editor was not enabled.

- **Native widgets:**
  - Core: Heading, Text Editor, Button, Icon List, Icon Box, Image (with captions), Image Carousel, Accordion.
  - Pro: **Carousel (nested)** for the reviews, where each slide is an editable container with stars, tag, quote and author. Also the **multi-step Form** (2 steps, progress bar, option cards) and Nav Menu.
- **Containers:** flexbox and CSS grid containers. Hero, reviews, quote and footer use grid containers with the reference's exact column ratios (e.g. `1.05fr .95fr`, `minmax(0,340px) 1fr`, `.9fr 1.1fr`, `1.4fr 1fr 1fr 1fr`).
- **Theme Builder:** Header and Footer templates, display condition "Entire Site". Elementor Sticky is used for the header and the mobile action bar.

## 4. Custom code added, and why

| Item | Where | Why |
|---|---|---|
| **3 HTML widgets:** animated LED truck, ad builder, campaign planner | Home page | These are the concept's interactive features. No native widget can do them. Each is a self-contained, scoped widget (CSS under `.mmx`, no global JS). The ad builder and planner pre-fill the native Elementor form. |
| `mm-*` utility classes | Site Settings → Custom CSS | Reproduce reference effects Elementor has no controls for: pseudo-element glows and gradients, hover lifts, caption pills, the form option-card subtitles, and the carousel control positions. They're applied by adding the class name in each element's Advanced tab. |
| Hero background layer | Hero container Custom CSS | The reference draws the skyline on its own layer at 55% opacity, scaled to 105%. This is reproduced exactly. |
| Avatar sizing | Review avatars Custom CSS | Fixed 40/48px circles. |
| Back-to-top button + scroll progress bar | Footer HTML widget | Small scoped script, matching the reference. |
| Inline `<span>` in the H1 | Hero heading | Colors and glows the "Light up your brand." line. |

No iframes, no full-page custom code, and no extra plugins.

## 5. Responsive adjustments completed

- Hero and the quote and review rows stack on tablet and mobile.
- Card grids go 4 → 2 → 1 columns; the brand wall goes 4 → 3 → 2.
- Headline sizes step down by breakpoint.
- The menu becomes a hamburger at tablet width. The phone link is hidden on tablet, and the whole action group is hidden on mobile.
- Gallery images become full width with a 240px height on mobile.
- The review carousel shows 2 slides on desktop and 1 on tablet and mobile, with arrows hidden on mobile.
- A mobile-only sticky Call / Text / Get Pricing bar was added.
- **No horizontal scroll at 1440, 820 or 390px.** An overflow from the truck headlight beam on tablet was found and fixed.

## 6. Functionality tested (published page)

| Test | Result |
|---|---|
| All 9 in-page anchor links resolve to a section; nav click scrolls to FAQ | ✅ Pass |
| Phone (`tel:`), SMS (`sms:`), email (`mailto:`), Google reviews link, 8 gallery lightbox links | ✅ Present and correct |
| FAQ accordion opens and closes | ✅ Pass |
| Ad builder: typing updates the truck screen; "Use this ad in my quote" fills the form message | ✅ Pass |
| Campaign planner: answers produce a recommendation; "Get pricing" pre-selects campaign and area in the form | ✅ Pass (e.g. Promotion + Texas → Weekly campaign / Houston) |
| Review carousel (7 reviews, nested carousel), logo marquee | ✅ Rendering; next arrow advances to the next review |
| Multi-step form: Next → step 2, Back → step 1, planner pre-selects the campaign card | ✅ Pass |
| Mobile menu opens and closes | ✅ Pass |
| Form: empty required field blocked | ✅ Pass |
| Form: real submission | ✅ Custom success message shown; entry saved in Elementor → Submissions; email action reported success. **All clearly labelled QA test entries were deleted afterwards** (Submissions count is 0). |
| Browser console errors / failed requests | ✅ None, apart from the missing favicon (see §8) |
| Keyboard navigation and focus | ✅ Every tested link and button shows a focus outline |
| Color contrast (Lighthouse) | ✅ Pass |

**Fix found during testing:** Elementor Pro's *Tel* field rejected normal phone formats with spaces, such as "(214) 555-0123". Its pattern also caused a console error in current Chrome. The phone field now uses a required *Text* field, so every format is accepted.

## 7. Technical SEO, schema and performance

### Technical SEO
- **Rank Math title:** "Mobile LED Billboard Truck Advertising in Dallas | MOD Media" (60 characters).
- **Rank Math description:** 153 characters, matching the visible content.
- **Rank Math identity:** set to Company / "MOD Media" with an organization description.
- One H1, 12 H2s, a logical heading order, and alt text on every image.
- Canonical and Open Graph tags are output by Rank Math. The XML sitemap returns 200.
- **Staging is intentionally not indexable.** WordPress "Discourage search engines" is on, and Hostinger's staging robots.txt blocks Googlebot. Both were left unchanged and must be switched at launch (§9).

### Schema (audited before adding)
- **Before:** Rank Math output a generic Person + WebSite + WebPage + Article graph named after the staging domain.
- **After:**
  - Rank Math outputs **Organization (MOD Media) + WebSite + WebPage**.
  - The default Article/Person schema was turned off **for the homepage only**.
  - Elementor's native accordion option outputs one **FAQPage** (8 Q&As that match the visible FAQ exactly).
  - No duplicate schema.

**WPCode note:** the brief asked for WPCode snippets with `is_page(ID)` conditions. I didn't add a WPCode snippet because:
1. The API access available here can only *read* WPCode snippets.
2. Rank Math and Elementor already output the correct schema types for this page, so a WPCode Organization snippet would duplicate them.

If richer business details are wanted (logo, phone, address, `sameAs` profiles), add them in Rank Math → Titles & Meta → Local SEO. That keeps one Organization entity. Alternatively, use a WPCode snippet wrapped in `if ( is_page( 48 ) )` once the address to publish is confirmed.

Google's Rich Results Test and the Schema.org validator could not be run from this environment. Run both on the live URL after launch.

### Performance (Lighthouse 12.2.1, lab data)

| | Old live site (baseline) | New build |
|---|---|---|
| Mobile performance | 63 | **67–74** |
| Mobile LCP | 19.8 s | **5.1–6.5 s** |
| Mobile TBT / CLS | 190 ms / 0 | **100–150 ms / 0** |
| Desktop performance | 74 | **86–88** |
| Desktop LCP | 4.0 s | **1.7–2.1 s** |
| Accessibility (mobile) | 96 | 88 (see note) |
| Best practices | 100 | 96 (favicon 404 only) |
| SEO | 85 | 58 *(staging noindex; expected ~92+ once indexable)* |

- All images were uploaded locally as WebP (largest 351 KB). Total page weight is about 1 MB.
- Below-the-fold backgrounds use Elementor lazy loading.
- **Remaining bottleneck:** mobile LCP is the hero headline waiting for Google Fonts. Recommendation: Elementor → Settings → Performance → *Load Google Fonts locally*, plus Hostinger's LiteSpeed cache at launch. I didn't change these global performance settings without your approval.
- **Accessibility note:** the v2 rebuild copies the reference's design exactly, including two things Lighthouse flags:
  - the truck's 9px ad-selector dots (target size);
  - one purple review avatar at 4.35:1 contrast against a 4.5:1 target.

  The other flag comes from Elementor's own accordion markup (ARIA), which can't be changed from the editor. If you prefer, the avatar colour and dot size can be adjusted slightly to clear these flags.
- Field data (CrUX/INP) isn't available because staging has no real traffic.

### Analytics and tracking
- No GA4, GTM, Meta Pixel or Clarity is installed on **either** the current live site or staging, so there were no existing IDs to preserve.
- Recommended at launch: GA4 via Site Kit or GTM, with conversion events for form submission, `tel:` clicks and `sms:` clicks. Also verify Search Console and submit the sitemap.

## 8. Remaining visual differences / unavailable assets

- See §0 for the measured comparison and the intentional differences: concept ribbon removed, production footer credit, mobile menu button, 6 vs 7 carousel dots.
- The scroll progress bar and back-to-top button are now included, as in the reference.
- **Favicon:** missing (404). The only icon available is 114×117px, below the 512px WordPress needs. **A 512×512 logo mark is needed from MOD Media.**

## 9. Unresolved items / launch checklist

1. Turn **off** "Discourage search engines" and make sure the production robots.txt doesn't block Googlebot.
2. When moving to modmediadfw.com, run Elementor → Tools → **Replace URL**. The custom HTML widgets and image URLs contain the staging domain.
3. Install GA4/GTM and set up conversion events; verify Search Console.
4. Confirm that form notification emails arrive in MOD Media's inbox. WordPress reported the send as successful, but inbox delivery can't be verified from here. Use SMTP (e.g. Hostinger SMTP / WP Mail SMTP) for reliable delivery.
5. Add the favicon once a 512px logo mark is supplied.
6. Optional: load Google Fonts locally; add Local SEO business details in Rank Math.
7. Run the Rich Results Test and Schema validator on the live URL.
8. Rotate the WordPress application password used for this build.

## 10. Unrelated settings

I didn't touch other pages, posts, plugins or the theme. The only site-level changes were:
- The front-page setting (Home as the static front page).
- The menu "Main Menu".
- Default Kit styling: global colors and typography, layout width, breakpoints (1000/640, matching the reference), fallback font stack, and the `mm-*` utility CSS.
- Rank Math website identity and homepage meta.

## Files in this folder

- `build2.py`: generates the Elementor JSON for the Home page, header and footer, using the reference's exact values.
- `publish.py`: pushes it through the WordPress REST API.
- `kit2.py`: sets the global design system (typography, breakpoints, layout, utility classes).
- `comps.py` and `html_widgets.json`: the three custom HTML widgets.
- `media.json`: uploaded media IDs.
- `measure.js` and `cmp.js`: the reference-vs-live measurement and screenshot tools.
- `qa2.js` and `shot.js`: the browser QA and screenshot scripts.
- `screenshots/`: the live page at 1440/820/390px, plus `compare-reference-vs-live-1440.jpg` (every section side by side).
- The credential helper (`wp.py`) is deliberately **not** committed.
