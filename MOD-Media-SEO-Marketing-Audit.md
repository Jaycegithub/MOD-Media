# MOD Media DFW — SEO, Local SEO, Conversion & Digital Marketing Audit

**Website audited:** https://modmediadfw.com/
**Audit date:** 13 November 2026
**Scope:** An independent external review of the website, local search presence and competitive landscape, with a strategy and 90-day roadmap.

---

## How to read this report

Every finding is labelled so the client can see what it rests on:

| Label | Meaning |
|---|---|
| **[Verified]** | Observed directly on the live site: page HTML, XML sitemap, HTTP headers, or a Google Lighthouse test. Supporting evidence is in `/evidence`. |
| **[Estimate]** | Professional judgement based on the search results, competitor sites and industry experience. |
| **[To confirm]** | A business fact the owner can confirm in a few minutes (for example, the operating address or which logos are clients). |

### Audit approach

- **Website review.** Every URL in the site's XML sitemap was reviewed (18 pages, plus 1 post, 1 category archive and 1 author archive), along with common unlinked URLs (`/contact/`, `/contact-us/`, `/blog/`, `/pricing/`) and all redirects. Each page was checked for titles, meta tags, headings, structured data, links, images, forms and copy.
- **Performance.** The homepage and a representative city page were tested with Google Lighthouse 12.2.1 under mobile and desktop conditions.
- **Search landscape.** Live Google-style searches for the core buyer phrases in Dallas–Fort Worth and Texas were reviewed, and the leading competitor pages were analysed directly.
- **Keyword strategy.** Keywords are prioritised by buyer intent and business value. Exact monthly volumes and cost-per-click figures are finalised in the first week of the engagement (see the proposal).
- **Local presence.** MOD Media's Google Maps listing ("MOD Media") and the business details published on the website were reviewed for consistency.

---

# PART A — EXECUTIVE REPORT

## 1. Executive summary

MOD Media has a real, differentiated product. It runs scheduled shared routes (Dallas days and nights, Frisco, North Dallas, Rockwall/Rowlett), event routes (Cowboys and other major events), and exclusive truck rentals across DFW, Austin, Houston and San Antonio. Genuine customer testimonials name real businesses, such as Atlas Bail Bonds and a Christmas-light installer. That gives MOD Media a strong base to build on.

**The website isn't yet built to win Google searches or to turn visitors into leads.** The problems are specific and fixable:

1. **Unfinished pages are live.** Four core service pages (Daily Route, Dallas Nightlife, Exclusive Rental, Event Routes) show *"Lorem Ipsum is simply dummy text…"* and a placeholder phone link (`tel:123 444 678`). A prospect who taps "Call Now" on those pages can't reach the business.
2. **Google can't tell what each page is about.** **None of the 18 real pages has an H1 heading.** Titles are generic, such as "Services - modmediadfw.com" and "Testimonials - modmediadfw.com", and the same blocks of copy are repeated across city pages. Some of that copy refers to the wrong city: the Houston page says "Dallas Businesses: Own the Streets…".
3. **The pages aren't set up to target what buyers type.** People search for "mobile billboard advertising Dallas", "LED billboard truck rental" and "how much does a mobile billboard cost". No page is clearly optimised for those phrases, and nothing on the site answers the price question.
4. **The quote path is weak.** The quote form asks only for name, email and message. It doesn't ask for a phone number, city, dates, campaign type or budget. The "Pricing" section lists no prices. Most CTAs say "Call Now", and nothing tracks those calls.
5. **The site is heavy on mobile.** The homepage downloads about **15 MB**, including a ~21 MB autoplay video file and ~1 MB PNG backgrounds. Lighthouse measured mobile **Largest Contentful Paint at 17.6 s** (the target is under 2.5 s).
6. **Nothing is measured.** We found no Google Analytics 4, Google Tag Manager or Meta Pixel in the page code, so the business can't tell which channel produces leads.
7. **Brand and location signals conflict.** The brand appears as "MOD Media", "Mod Media Ads" and "Mod Media DFW". The email domain (modmediaads.com) serves a hosting placeholder page. The footer address is in Rockwall, but the linked Google Maps pin appears to sit in the Carrollton/Farmers Branch area, which needs checking. These conflicts weaken the local signals that drive Google Maps rankings.

**The opportunity is real because the competition is thin.** The DFW search results for this niche are dominated by multi-city template sites (Bulldog Billboards, LED Truck Media, Mobile Billboard Global, American Mobile Ads) and an older Dallas operator (Texas Mobile Advertising). Few of them show real DFW routes, real local campaign photos and transparent pricing. A locally run operator with genuine route schedules, event coverage and proof is exactly what Google's local and "helpful content" systems are designed to reward. It's also what a business owner wants to see before calling.

**Recommended approach, in order:**
1. Fix the trust breakers first (Lorem Ipsum, the dead phone link, the spam blog post, the exposed author archive).
2. Install measurement.
3. Rebuild the website in a new, modern layout, structured around buyer searches.
4. Fully optimise Google Business Profile and start a steady review program.
5. Build an active Facebook presence with truck photos, route updates and client spotlights, and add Google or Meta ads later if faster results are wanted.

We can't guarantee rankings or lead volume. What we can say is that the issues blocking performance today are concrete and verifiable, and they can be fixed quickly.

## 2. Main problems

### 2a. Verified issues (seen directly on the site)

| # | Issue | Where | Why it hurts leads or rankings |
|---|---|---|---|
| 1 | Lorem Ipsum placeholder copy in the "Secure Your Appointment or Get Instant Assistance" block | `/daily-route-advertising/`, `/dallas-nightlife-route/`, `/exclusive-rental/`, `/event-routes/` | Destroys credibility with prospects and is a quality red flag for Google on the most important commercial pages |
| 2 | Broken placeholder phone link `tel:123 444 678` behind "Call Now" | Same four pages | Lost calls from people who are ready to buy |
| 3 | No H1 on any of the 18 pages | Site-wide | Weakest possible on-page relevance signal |
| 4 | Generic, duplicated or mismatched titles, e.g. "Services - modmediadfw.com"; the Free Quote page is titled "Mobile Digital LED Billboard Advertising Truck Benefits" | Site-wide | Low click-through and poor keyword targeting |
| 5 | Missing meta descriptions | `/services/`, `/testimonials/`, `/dallas-nightlife-route/` | Google writes its own snippet, often badly |
| 6 | Boilerplate copied between city pages, including the wrong city (Houston and San Antonio pages carry "Dallas Businesses: Own the Streets…"; North Dallas, Rockwall, Houston and San Antonio all carry "Strategy Behind frisco & nightlife route"; the Frisco page says "We turn the roads of Houston, San Antonio, and Austin…") | City pages | Thin and duplicate content signals, and it confuses prospects |
| 7 | Two competing nightlife pages: `/dallas-night-routes/` and `/dallas-nightlife-route/` | Services and City Routes | Keyword cannibalisation: Google has to pick one of two weak pages |
| 8 | Quote form has only Name, Email (required) and Message. No phone, city, date or budget fields | `/free-quote/` | Leads are slow to follow up and hard to qualify |
| 9 | "Mobile Billboard Advertising Truck Pricing" section lists no prices or starting points | `/services/` | Price is the #1 question buyers have. Competitors show "From $1,400/Day" (Mobile Billboard Global) |
| 10 | Default WordPress "Hello world!" post is indexed, with spam comments linking to a trading site (traderzo.com) | `/2025/02/24/hello-world/` | Spam outbound links and a low-quality page in the index |
| 11 | Author archive is indexed and exposes the WordPress admin username/email in the page title | `/author/texasnvbullies/` | Security and privacy risk, plus a thin page |
| 12 | "Uncategorized" category archive is indexed | `/category/uncategorized/` | Thin page |
| 13 | "Analytics Reporting" button links to a PDF hosted on a third-party developer domain (`judy.onlinedigitalprojects.com`) | Homepage and `/services/` | Leaks authority to another domain and looks unprofessional. The asset is outside the client's control |
| 14 | Footer social icons (Facebook, Twitter, Instagram, LinkedIn, YouTube) have no link (`href` missing) | Site-wide | Dead clicks. Lighthouse flags "Links are not crawlable" |
| 15 | Homepage downloads about 15 MB. Mobile LCP is 17.6 s (lab) | `/` | Slow pages lose mobile visitors and weaken page-experience signals |
| 16 | No GA4, GTM or Meta Pixel found in the HTML | Site-wide | Lead sources can't be measured |
| 17 | Inconsistent brand name: "MOD Media", "Mod Media Ads", "Mod Media DFW", Instagram `@modmediaadsllc`, and the WebSite schema name is literally "https://www.modmediadfw.com/" | Site-wide and schema | Weak entity signals for Google and for AI search |
| 18 | The email domain modmediaads.com serves a hosting default page and doesn't redirect to the website | modmediaads.com | Prospects who type the email domain hit a dead end |
| 19 | 35 of 44 images on the homepage have no alt text. Files are named `image-23.png`, `WhatsApp-Image-2025-03-14…jpeg` | Site-wide | Lost image-search visibility and accessibility problems |
| 20 | The Houston page still says "Minute Maid Park", which was renamed Daikin Park in 2025 | `/houston-led-advertising-truck/` | Outdated details undermine "local expert" credibility |

### 2b. Business details to confirm

| Item | How to confirm |
|---|---|
| Whether the Maps pin (about 32.955, ‑96.893, which appears to be Carrollton/Farmers Branch) matches the Rockwall footer address | Owner confirmation of the real operating base |
| Whether the claim "City of Frisco prohibits roadside billboards" can be cited to the ordinance | Cite Frisco Sign Ordinance Section 70-18 on the page |
| Whether featured partner logos (NFL, Big 12, Academy, Choctaw, Fiesta and others) are actual clients or campaign placements | Client confirmation. Logo use without a client relationship is a legal and trust risk |

## 3. Top 10 growth opportunities

1. **Turn the four core service pages into real sales pages.** Remove the placeholders and add real photos, the route schedule, who the service is for, a "starting from" price, FAQs and a quote form.
2. **Build a true "Mobile Billboard Advertising in Dallas–Fort Worth" pillar.** Use the homepage, or a dedicated page linked from it, with a clear H1 and strong local proof.
3. **Publish a "Mobile Billboard Truck Pricing" page.** Cost questions are high-intent, and almost no local competitor answers them honestly.
4. **Make the scheduled routes the selling point.** Fixed weekly routes (Frisco on Monday and Wednesday, Dallas nightlife on Friday and Saturday 6–11 pm) make a low-cost entry product that template-site competitors don't have.
5. **Optimise Google Business Profile fully and run a review program.** For local "near me" and Maps visibility, this is the highest-leverage channel.
6. **Build event-specific landing pages for recurring DFW events,** such as AT&T Stadium game days, the State Fair of Texas and American Airlines Center concerts. Promote them ahead of each season.
7. **Build industry landing pages where MOD Media already has proof,** such as bail bonds and legal, home services, restaurants and bars, and real estate.
8. **Optional: run Facebook lead ads to DFW business owners** with a "Free Route Plan & Quote" offer. Facebook's local targeting produces enquiries in weeks while SEO takes months.
9. **Turn every route into Facebook posts.** LED trucks are inherently visual, so photos of trucks in Deep Ellum, Uptown and outside AT&T Stadium make strong organic posts and ad creative.
10. **Optional: retarget on Facebook** everyone who visits the pricing or quote pages. Advertising buyers rarely convert on the first visit.

## 4. SEO scorecard

The scores are rubric-based. Each category starts at 100 and loses points for verified issues, weighted by business impact. Scores reflect what is publicly visible today.

| Area | Score | How we determined it |
|---|---|---|
| Technical SEO | **58 / 100** | **Good:** HTTPS enforced, non-www canonical, Yoast sitemap present, robots.txt open, self-referencing canonicals, 404 pages noindexed, fast server response (TTFB about 50 ms with LiteSpeed cache). **Lost points:** indexed junk pages (hello-world post, author and category archives), a two-hop redirect chain (http://www → https://www → https://), internal links through a redirect (`/dallas-day-routes/` → 301), a 15 MB homepage, mobile LCP of 17.6 s, no long-term cache headers on 106 resources, and non-crawlable social links. |
| On-Page SEO | **30 / 100** | No H1 on any page. Generic or mismatched titles, missing descriptions, misused heading levels (H4 "About us" labels as decoration, repeated H2s), "Learn More" or "Read More" link text, and missing alt text. |
| Local SEO | **35 / 100** | **Good:** consistent phone (469) 279-2511 on the site, address in the footer, a GBP listing exists, and there are city pages. **Lost points:** no LocalBusiness schema, a possible pin/address mismatch, brand-name variants, city pages that share wrong-city boilerplate, and no embedded map or service-area detail. Listing consistency issues weaken Maps visibility. |
| Content Quality | **28 / 100** | Real and useful details exist (route days and times, venues, Houston and San Antonio district coverage). These are outweighed by Lorem Ipsum, copy-pasted blocks, no pricing information, no case studies, no FAQs and no blog content (only "Hello world!"). |
| Keyword Targeting | **25 / 100** | Titles target loose variations ("Digital Advertising Truck: Effective Advertising Solution") instead of the phrases buyers use. Two nightlife pages compete with each other. There's no pricing, industry or event page, and no clear page for "Fort Worth" or "Plano" (Plano only appears inside the North Dallas copy). |
| Website Conversion | **32 / 100** | Click-to-call is present in the header and many sections, which is good. But there's a broken placeholder tel link on four pages, a minimal quote form, a homepage form that only collects newsletter emails, no prices, no visible "how it works", no truck specs and no case studies. |
| Authority & Brand Footprint | **20 / 100** | A search for the domain and brand name returned no third-party mentions, press coverage or directory listings, while competitors appear on directories, trade publications and marketplaces. Few external signals currently vouch for the business. |
| Facebook Readiness | **30 / 100** | The footer Facebook icon is a dead link, the Page isn't connected to the website through tracking (no Meta Pixel), and nothing on the site invites visitors to follow or message the Page. The product itself is ideal for video. |
| Analytics & Tracking | **10 / 100** | No GA4, GTM or Meta Pixel in the site code, and no call tracking, so lead sources can't currently be attributed. |

## 5. Competitor comparison (summary)

The full analysis is in Section 10.

| Competitor | Type | DFW signal | Notable strength | Notable weakness vs MOD Media |
|---|---|---|---|---|
| [Texas Mobile Advertising](https://www.texasmobileadvertising.com/) | Texas multi-city operator | Dallas-based, 214 number; city pages for Dallas, Fort Worth, Plano, Arlington, Garland and others | Clear H1s, LocalBusiness schema, a 15-city structure, an active blog (posts dated Nov 2026), and a detailed quote form (city, vehicle, number of vehicles, date) | Generic copy. Static, glass-walled and LED mixed together. No published route schedule |
| [Bulldog Billboards](https://bulldogbillboards.com/) | National operator (Dallas and NYC) | Dallas location page. **Uses the same 214-724-2729 number as Texas Mobile Advertising**, so it appears to be the same operator running two brands | 25+ city pages, FAQ, blog, long-form copy | Homepage targets New York City. Template city pages with no DFW-specific proof |
| [Mobile Billboard Global](https://www.mobilebillboardglobal.com/mobile-billboard-texas) | National broker/operator (Atlanta number) | Texas page covering DFW, Houston, Austin and San Antonio | **Shows "From $1,400/Day"**, "$0 creative production", LocalBusiness, Service and FAQ schema, and event pages (NFL, Super Bowl, political) | Not local. Out-of-state phone number |
| [LED Truck Media](https://ledtruckmedia.com/us-markets/region/southeast/city/dallas/) | National network | Dallas city page | FAQ and LocalBusiness schema, budget-range qualifier in the form ($5K–$100K+) | National template. Lists Dallas under "southeast" |
| [Lime Media](https://lime-media.com/locations/led-billboard-truck-dallas/) | National operator | Dallas page mentions Uptown nights, Plano and Frisco | H1 that matches the keyword, FAQ schema, 1,400+ words | Template. No local proof |
| [Big Wave Display](https://bigwavedisplay.com/) | DFW local | DFW-only, 214 number | Clear H1, FAQ section, simple form that includes business name and phone | One-page site with no service or city pages and no schema, so a weak SEO footprint |
| [Rolling Adz](https://rollingadz.com/) | National (Oregon number) | Lists Dallas among its markets | Cost guide, industry pages, case study, FAQ, guarantees page | Not local |
| [American Mobile Ads](https://americanmobileads.com/us/texas) | National broker | Texas market page | Huge market index | Thin page, no schema |
| [AdQuick](https://www.adquick.com/mobile-billboard-advertising) | OOH marketplace | Lists DFW as a popular market | Domain strength. Publishes day-rate benchmarks ($1,250–$3,600+/day) | A marketplace, not an operator. MOD Media could even list inventory there |
| Cowtown Command ([listing](https://www.outdoorbillboard.com/billboards/6971518-cowtown-command-for-rent-in-fort-worth-tx)) | Fort Worth LED trucks | Listing names I-35W, Stockyards, Dickies Arena and TCU | Fort Worth-specific positioning | Found only as a marketplace listing |

**Where MOD Media wins:** it's genuinely local, publishes fixed recurring routes with days and times, has real named testimonials and real truck video, and offers both shared-route (lower cost) and exclusive options.
**Where MOD Media loses:** page structure, H1s and titles, FAQs, schema, pricing transparency, form quality, content depth and site cleanliness.

## 6. Keyword strategy (highest priority)

Relative demand below is an **[Estimate]** based on the live search results and industry knowledge. Exact volumes and CPCs are locked in during week 1 keyword validation.

| Priority | Keyword cluster | Intent | Rel. demand [Estimate] | Target page |
|---|---|---|---|---|
| 1 | mobile billboard advertising Dallas / DFW / Dallas Fort Worth; mobile billboard Dallas | Commercial, local | Medium (highest in the niche locally) | Homepage (re-optimised) |
| 1 | LED billboard truck Dallas; digital billboard truck rental Dallas; LED truck rental Dallas | Commercial, local | Low–medium | `/exclusive-rental/` → re-titled "LED Billboard Truck Rental" |
| 1 | mobile billboard cost / pricing / how much does a mobile billboard cost | Commercial investigation | Medium (national) | NEW `/mobile-billboard-pricing/` |
| 2 | mobile billboard advertising Frisco TX | Commercial, local | Low | `/frisco-routes/` |
| 2 | mobile billboard Fort Worth | Commercial, local | Low–medium | NEW `/fort-worth-mobile-billboards/` (**only if trucks genuinely run there**) |
| 2 | mobile billboard Plano / McKinney / Allen | Commercial, local | Low | `/north-dallas/` (consolidated "North Dallas & Collin County" page) |
| 2 | mobile billboard Rockwall / Rowlett | Commercial, local | Very low, but uncontested | `/rockwall-rowlett/` |
| 2 | event mobile billboard Dallas; billboard truck AT&T Stadium / Cowboys game | Commercial, event | Low, seasonal | `/event-routes/` and event sub-pages |
| 2 | Dallas nightlife advertising; Deep Ellum / Uptown advertising | Commercial, local | Low | Merged `/dallas-nightlife-route/` |
| 3 | mobile billboard Houston / Austin / San Antonio | Commercial, local | Medium in each city, but competitive | Existing city pages, upgraded |
| 3 | mobile billboard for grand opening / restaurants / real estate / political campaigns | Commercial, use case | Low each, high conversion | NEW industry pages (Phase 6) |
| 3 | mobile billboard vs traditional billboard; are mobile billboards effective | Informational, consideration | Low–medium | Blog |

## 7. Website improvement recommendations

The detailed, copy-ready page-by-page plan is in Section 13. The ten most important page actions:

1. **All four service pages:** delete the Lorem Ipsum block, fix the `tel:` link, add an H1 and a real quote form.
2. **Homepage:** add an H1 ("Mobile Billboard Advertising in Dallas–Fort Worth"), a single hero (it's currently duplicated in the DOM), compress the video and backgrounds, add "How it works", "Starting at" pricing, truck specs and a quote form.
3. **Merge `/dallas-night-routes/` into `/dallas-nightlife-route/`** with a 301 redirect.
4. **Rewrite the city pages** to remove the cross-city boilerplate. Every city page needs that city's real routes, venues, schedule and photos.
5. **Build `/mobile-billboard-pricing/`.**
6. **Rebuild `/free-quote/`**: title it "Get a Free Mobile Billboard Quote", add phone, company, city, dates, service and budget-range fields, and add a "What happens next" step list.
7. **Noindex or delete** the hello-world post, the author archive and the category archive. Delete the spam comments and turn comments off.
8. **Host the analytics PDF on modmediadfw.com,** or better, turn it into an HTML "Campaign Reporting" page.
9. **Link the footer Facebook icon to the Page**, remove unused social icons, and fix the Organization `sameAs` list.
10. **Add LocalBusiness and Service schema** (Section 11).

## 8. Facebook strategy (summary)

- **Why Facebook:** DFW small-business owners, restaurant and bar owners, real estate agents and event promoters are active on Facebook, and Facebook ads can target them by location, interests and job role. It's also where local business owners check a company's reviews and recent activity before calling.
- **Posting rhythm:** 3–4 posts per week, up to 15 per month (truck photos, carousels and designed graphics), with photo Stories on route nights.
- **Community:** share route updates and client spotlights in relevant local Facebook groups where the group rules allow it, and reply to every comment and message within business hours.
- **Photos:** every route night and event is a photo opportunity. Photograph the truck in front of recognisable DFW landmarks with the client's ad on screen (with the client's permission). The client or drivers take the photos on a phone, and posts are designed from them in Canva.
- **Paid (optional add-on):** Facebook Lead Ads (instant form) for a "Free Route Plan + Quote" offer, plus retargeting of website visitors and Page engagers. Details are in Section 15.

## 9. Lead generation strategy (how the pieces work together)

```
SEARCH INTENT (Google organic + Google Business Profile/Maps)
   "mobile billboard Dallas", "LED truck rental", "billboard truck cost"
        │
        ▼
FOCUSED LANDING PAGE (service / city / pricing / event)
   real truck photos & video → route schedule → "starting at" price
   → proof (testimonials, client photos) → 2-step quote form + click-to-call
        │                                   │
        │  (didn't convert)                 ▼
        ▼                           LEAD (tracked: form, call, text, email)
RETARGETING (Facebook ads)                  │
   truck photos, case studies,              ▼
   "Fill the Friday-night route" offers   FAST FOLLOW-UP (<15 min, route map + quote)
        │                                   │
        ▼                                   ▼
FACEBOOK (organic posts) builds         CUSTOMER → photo of their ad
   familiarity & brand search  ◄──────── → Google review → case study → new content
```

Every booked campaign should feed the system back: a photo for Facebook, a Google review request, and a case study once results are known.

## 10. 90-day action plan (summary)

Full task tables are in Section 20.
- **Days 1–7:** Fix the placeholders, phone link, spam and junk pages. Install GA4, GTM, Search Console and call tracking. Claim and audit GBP.
- **Days 8–30:** New titles, H1s and descriptions, consolidate pages, rebuild the homepage and quote form, build the pricing page, add schema, compress media, optimise GBP, set up the Facebook Page and Meta Pixel.
- **Days 31–60:** Industry and event pages, the first 4–6 priority articles, first case studies, review program, a steady weekly Facebook posting cadence, Facebook lead and retargeting campaigns, local link building.
- **Days 61–90:** Expand the pages that are winning, fix the ones that aren't, add a Fort Worth page if operations support it, PR and partnerships, ad optimisation, and the first quarterly report.

## 11. Recommended monthly marketing rhythm

| Every month | Activity |
|---|---|
| Week 1 | Report on leads by channel, Search Console queries and GBP insights. Agree next month's priority pages and events |
| Weekly | GBP post (route schedule, event, client spotlight); 3–4 Facebook posts; review requests to every completed campaign |
| Monthly | 2 high-intent articles or landing pages; 1 case study; refresh the event calendar page; 2–4 earned link or PR outreach pushes |
| Monthly (paid) | Facebook ad creative and audience tests; landing-page A/B test |
| Quarterly | Content refresh of the top 10 pages; competitor SERP review; budget re-allocation by cost per qualified lead |

## 12. Investment

Simple monthly pricing: one core service plus two optional add-ons. There are no setup fees, and the new modern website design is included in the Website & SEO service.

| Service | What's included | Monthly fee |
|---|---|---|
| **Website & SEO** (core) | New modern website design (included), on-page SEO (titles, headings, content, schema), off-page SEO (local citations, links, directories), site speed optimisation, up to 5 new articles or landing pages per month, technical fixes, tracking and a monthly SEO report | **$699** |
| **Facebook** (add-on) | Facebook Page set-up and optimisation, up to 15 posts per month (truck photos, route updates, client spotlights), designed graphics in MOD Media branding, monthly content calendar | **$199** |
| **Google Business Profile** (add-on) | Profile clean-up (pin, categories, services, photos), weekly Google posts, review request program and review replies, Q&A and photo updates | **$149** |
| **All three together** | Recommended: the website, Google Maps and Facebook reinforce each other | **$1,047** |
| **Optional: Google Ads / Meta Ads management** | Campaign set-up, targeting, creative and monthly optimisation | Quoted separately. Ad budget is paid directly to Google or Meta |

**Billing:** monthly, at the start of each month, with a 3-month minimum so the SEO work has time to show results, then month to month. We can't guarantee rankings, leads or ad performance.

---

# PART B — DETAILED AUDIT

## 12a. Phase 1 — Page inventory

Data is from raw HTML. "Words" counts the visible body text, including the shared header, footer and navigation (about 220 words are template on every page).

| URL | Title (chars) | Meta description | H1 | Words | Schema (Yoast) | Key issues |
|---|---|---|---|---|---|---|
| `/` | Mobile Digital Billboard Ads: Capture Attention Now - modmediadfw.com (69) | Generic ("Discover how Mobile Digital Billboard Ads…") | **None** | 1,326 | WebPage, ImageObject, BreadcrumbList, WebSite, Organization | Hero and service cards duplicated in DOM; "Cusotmer success" typo; 35/44 images without alt; 15 MB |
| `/services/` | Services - modmediadfw.com (26) | **Missing** | **None** | 424 | same | Empty "pricing" section; analytics PDF on third-party domain |
| `/daily-route-advertising/` | Digital Billboard Truck Maximizes Ad Visibility (65) | Generic | **None** | 541 | same | **Lorem Ipsum; `tel:123 444 678`**; repeated "About us" H4s |
| `/dallas-nightlife-route/` | Dallas Nightlife Route - modmediadfw.com (40) | **Missing** | **None** | 552 | same | **Lorem Ipsum; placeholder tel**; duplicate of `/dallas-night-routes/` |
| `/exclusive-rental/` | Digital Advertising Truck: Effective Advertising Solution (75) | Generic | **None** | 568 | same | **Lorem Ipsum; placeholder tel**; title over 60 chars |
| `/event-routes/` | Led Truck Advertising: Capture Audience Attention (67) | Mentions NFL/NBA/MLB/NHL/UFC | **None** | 555 | same | **Lorem Ipsum; placeholder tel**; "lED" casing in H2 |
| `/city-routes/` | Mobile Billboard Advertising: Reach Dallas - Ft. Worth Consumers (82) | OK | **None** | 343 | same | Thin hub; title too long; H2 "City Routes" duplicated |
| `/dallas-day-routes-mobile-led-billboard-truck/` | Mobile LED Billboard Truck for High Impact Ads (64) | Mentions DFW | **None** | 638 | WebPage, Breadcrumb… | Keyword-stuffed slug; "Strategy Behind frisco & nightlife route" H2; nav links to `/dallas-day-routes/` (301) |
| `/dallas-night-routes/` | Mobile Digital Billboards That Capture Attention (66) | Mentions Deep Ellum & Uptown (good) | **None** | 661 | same | Cannibalises `/dallas-nightlife-route/` |
| `/frisco-routes/` | Frisco Mobile Billboard Advertising to Increase Sales (71) | OK | **None** | 678 | same | Mentions Houston/SA/Austin; the "Frisco prohibits billboards" claim needs a citation |
| `/north-dallas/` | Led Billboard Truck for Effective Brand Marketing (67) | OK | **None** | 626 | same | No city in title; the Frisco block is copied in |
| `/rockwall-rowlett/` | Mobile LED Billboard Boosting Your Brand Visibility (69) | OK; spells "Royce City" (correct: **Royse City**) | **None** | 736 | same | No city in title; Frisco block copied |
| `/austin-texas-best-led-digital-billboard-truck/` | Austin TX Mobile Billboard Advertising for Maximum Impact (57) | OK | **None** | 987 | same | Slug stuffed with "best"; no OG image |
| `/houston-led-advertising-truck/` | Mobile LED Billboard Truck for Effective Marketing in Houston, TX (65) | OK | **None** | 830 | same | "Dallas Businesses" H2; Minute Maid Park → Daikin Park; H2 and H3 duplicated |
| `/san-antonio-texas-led-truck/` | Led Billboard Truck: Capture Attention Locally in San Antonio, TX (65) | OK | **None** | 852 | same | "Dallas Businesses" H2; Frisco block |
| `/about-us/` | Mobile Billboard Truck: Revolutionize Your Ads (64) | Doesn't describe the page | **None** | 591 | same | Vision and Mission repeated 3×; no owner names, photos or fleet info |
| `/testimonials/` | Testimonials - modmediadfw.com (30) | **Missing** | **None** | 594 | same | 21/22 images without alt; two entries are just "Gave MOD Media Ads 5.0 Stars"; no client logos or photos |
| `/free-quote/` | Mobile Digital LED Billboard Advertising Truck Benefits (73) | Mismatched to the page | **None** | 223 | same | Minimal form; slug says "free quote" but the H2 says "Contact Us" |
| `/2025/02/24/hello-world/` | Hello world! (30) | Missing | Hello world! | 391 | Article… | **Spam comments with outbound links**; should be deleted |
| `/author/texasnvbullies/` | (admin email) Author at modmediadfw.com | — | Author name | 228 | ProfilePage | **Exposes the admin login identity**; should be noindexed or disabled |
| `/category/uncategorized/` | Uncategorized Archives | — | Uncategorized | 226 | CollectionPage | Noindex |

**Site-wide template observations [Verified]:**
- **Header/nav:** has click-to-call (469) 279-2511 and a "FREE QUOTE" button (good). The menu lists 9 city items under "City Routes", which is cluttered on mobile.
- **Footer:** the only "form" is a newsletter email field ("Get the latest Updates"). The address is 181 County Line Road, Rockwall, TX 75032. The email is info@modmediaads.com, and the `mailto:` has a leading encoded space (`mailto:%20info@…`) that some mail clients mishandle.
- **Phone links** use three different formats (`tel:+14692792511`, `tel:(469)279-2511`, `tel:%20(469)279-2511`). Standardise on `tel:+14692792511`.
- **Recurring CTA:** "Call Now for Demo and get 1 FREE Ad". The offer is good, but the terms aren't explained.
- **Copy errors:** "Cusotmer success", "bussiness" (in a testimonial, so leave it), "insure" → "ensure" (in a testimonial, so leave it), "Royce City" → "Royse City", and inconsistent casing ("lED", "frisco", "event Routes").

### Issue register (Phase 1 format)

| URL | What's wrong | Why it matters | Fix | Priority | Business impact |
|---|---|---|---|---|---|
| 4 service pages | Lorem Ipsum block "Secure Your Appointment…" | Prospects lose trust; Google sees an unfinished page | Replace with a real "Book your route" block: 3 steps, phone, a form shortcode | **Critical** | High |
| Same 4 pages | `tel:123%20444%20678` | Calls go nowhere | Change to `tel:+14692792511` in the Elementor button link | **Critical** | High |
| All pages | No H1 | Main relevance signal missing | Change the first heading widget ("DAILY ROUTE ADVERTISING" and so on) from H2 to H1 with keyword-led wording (Section 13) | **High** | Medium–High |
| `/dallas-night-routes/` vs `/dallas-nightlife-route/` | Duplicate intent | Splits relevance and links | Merge the best content into `/dallas-nightlife-route/`; 301 the other; update the menu | High | Medium |
| City pages | Copied blocks naming the wrong city | Thin or duplicate content; looks careless | Unique sections per city: schedule, named corridors and venues, local photos, local FAQ | High | Medium |
| `/services/` | Pricing section empty | Unanswered #1 buyer question | Add "Starting at" ranges or link to the new pricing page | High | High |
| `/free-quote/` | 3-field form; mismatched title | Poor lead qualification and SEO | Rebuild (Section 15) | **High** | High |
| Hello-world post | Spam comments with outbound links | Spam signal | Delete the post and comments; Settings → Discussion → disable comments | **High** | Low–Medium (risk reduction) |
| Author and category archives | Indexed; author archive exposes login | Security and thin pages | Yoast → Search Appearance → Archives: disable the author archive and set categories to noindex; change the admin display name | **High** | Security |
| Homepage + `/services/` | PDF on `judy.onlinedigitalprojects.com` | Off-domain dependency | Upload to the Media Library or build an HTML reporting page | Medium | Low–Medium |
| Footer | Social icons without `href` | Dead clicks | Link the Facebook icon to the Page; remove the icons for platforms not in use | Medium | Low |
| All images | Missing alt text; generic file names | Image SEO and accessibility | Rename on upload (`mod-media-led-billboard-truck-deep-ellum.webp`) and write descriptive alt text | Medium | Low–Medium |

## 12b. Phase 2 — Technical SEO audit

### A. Indexing and crawling [Verified unless noted]

| Check | Finding | Status |
|---|---|---|
| robots.txt | `User-agent: * / Disallow:` (nothing blocked), sitemap declared | ✅ OK |
| XML sitemap | `/sitemap_index.xml` (Yoast) → page, post, category and author sitemaps | ⚠️ Remove the author and category sitemaps; remove the hello-world post |
| Noindex | Only 404 pages are `noindex` (correct). All real pages are `index, follow` | ✅ |
| Canonicals | Self-referencing on all pages | ✅ |
| HTTPS / WWW | `http://` → `https://`; `https://www` → `https://` (non-www canonical) | ✅ consistent |
| Redirect chains | `http://www.modmediadfw.com/` → `https://www.modmediadfw.com/` → `https://modmediadfw.com/` (2 hops) | ⚠️ Make it a single 301 in `.htaccess` or the Hostinger panel |
| Internal links via redirect | Menu/hub links to `/dallas-day-routes/` → 301 → `/dallas-day-routes-mobile-led-billboard-truck/` | ⚠️ Update the links (or rename the page slug to `/dallas-day-routes/` and redirect the long one) |
| 404s | `/contact/`, `/contact-us/`, `/blog/`, `/pricing/` return 404. No internal links point to them | ℹ️ Not errors, but `/contact/` is a URL people guess. Create or redirect it to `/free-quote/` |
| Crawl depth | All pages are linked from the header menu (depth 1) | ✅ |
| Orphan pages | None found among sitemap URLs (all in the menu). A full spider is needed to confirm | ℹ️ |
| Duplicate content | Hero and service blocks are duplicated within the homepage DOM (desktop and mobile versions); city-page boilerplate is duplicated | ⚠️ |
| Indexation status in Google | modmediadfw.com pages appear in live search results, so the site is indexed. A full index-coverage review runs in week 1 | ✅ |

### B. Performance [Verified, lab: Lighthouse 12.2.1, local headless Chromium]

| Metric | Home, mobile | Home, desktop | Frisco, mobile | Target |
|---|---|---|---|---|
| Performance score | **70** | 79 | 72 | 90+ |
| First Contentful Paint | 2.2 s | 0.9 s | 1.9 s | < 1.8 s |
| **Largest Contentful Paint** | **17.6 s** | 3.5 s | **13.8 s** | < 2.5 s |
| Total Blocking Time (lab proxy for INP) | 50 ms | 0 ms | 30 ms | < 200 ms ✅ |
| Cumulative Layout Shift | 0 | 0.001 | 0 | < 0.1 ✅ |
| Speed Index | 4.6 s | 1.4 s | 3.7 s | < 3.4 s |
| Total page weight | **14,955 KiB** | 14,705 KiB | 2,759 KiB | < 2,000 KiB |
| Server response (TTFB) | 50 ms (LiteSpeed cache hit) | 50 ms | 50 ms | ✅ |
| Lighthouse SEO score | 85 | 85 | 92 | — |
| Lighthouse Accessibility | 96 | 93 | — | — |

**Interaction to Next Paint (INP):** the low Total Blocking Time indicates interactions should be responsive. The main problem is loading speed (LCP), not interactivity.

**Heaviest resources (homepage):**

| Resource | Transferred | Fix |
|---|---|---|
| `/wp-content/uploads/2025/04/MOD_2.mp4` (file is **20.9 MB**) | 6.4 MB+ during test | Re-encode to 720p H.264 at about 1.5 Mbps (target < 3 MB) plus WebM. Add `preload="none"` and a poster image. Don't autoplay on mobile, or serve a short 6–8 s loop |
| `/wp-content/uploads/2025/06/mod-dallas.mp4` | 3.2 MB | Same treatment |
| `image-54.png` (background) | 1.1 MB | Convert to WebP or AVIF at display size (savings of about 1.05 MB) |
| `image-24.png` (background) | 1.0 MB | WebP (savings of about 1.0 MB) |
| `image-23.png` (background, also the OG image on many pages) | 0.93 MB | WebP (savings of about 0.86 MB) |
| `image-61-1.png`, `image-63.png` | ~240 KB each | WebP |
| Font Awesome 6 solid and brands (from the Unlimited Elements plugin) + a self-hosted `Signika-Medium.ttf` (136 KB) | ~400 KB | Use SVG icons or Elementor's inline icons. Serve the font as WOFF2 |

**Other findings:**
- Lighthouse estimates **3,441 KiB** of savings from modern image formats.
- **106 resources have no browser cache lifetime.** Set `Cache-Control` for `/wp-content/uploads/` with the LiteSpeed Cache plugin → Browser Cache = ON, TTL 31536000.
- Unused CSS is about 86 KiB and unused JS about 43 KiB.
- The DOM has 1,235 elements on the homepage, partly because of the duplicated hero and service sections.

**Plugin stack [Verified from source]:** WordPress 6.8.12, Astra theme, Elementor 4.3.6 + Elementor Pro, Essential Addons for Elementor (Lite), Unlimited Elements for Elementor (Premium), Mousewheel Smooth Scroll, and Yoast SEO, on Hostinger LiteSpeed. **Recommendation for the developer:**
1. Remove Mousewheel Smooth Scroll (it adds JavaScript and hurts scroll UX).
2. Check whether Essential Addons and Unlimited Elements are both needed (they duplicate each other), and remove whichever is unused.
3. In LiteSpeed Cache: enable image WebP replacement, lazy-load below-the-fold images, CSS and JS minification, and "Load JS Deferred". Test the Elementor animations after changes.
4. In Elementor → Settings → Performance: enable "Optimized DOM output", "Improved asset loading" and "Lazy load background images".
5. Preload the hero image (the LCP element), and don't apply the `fadeInUp` entrance animation to above-the-fold content. Elements marked `elementor-invisible` delay LCP.

### C. Schema markup [Verified]

**Current state:** only Yoast defaults are present. Every page has WebPage + BreadcrumbList + WebSite + Organization.
- `Organization.name` = "Mod Media DFW". `WebSite.name` = "https://www.modmediadfw.com/", which is wrong and should be "MOD Media".
- `sameAs` lists Facebook (profile.php?id=100088542497714) and Instagram (modmediaadsllc) only.
- There's **no LocalBusiness, Service, FAQPage or VideoObject**, and no address, phone, areaServed or geo.
- The Breadcrumb on inner pages works, but the WebSite name feeds the site name Google shows in results.
- No duplicate or conflicting schema blocks were found. No fake review markup was found (good).

The recommended implementation is in Section 11 (Phase 11).

## 12c. Phase 3 — Keyword research and search intent

### 3.1 Primary commercial keywords

Demand tiers are directional **[Estimate]** values. Exact volume, difficulty and CPC for each keyword are confirmed in week 1 of the engagement. The final column says whether a new page is needed.

| Keyword | Intent | Rel. demand [Est.] | Geo | Opportunity | Target page | New page? |
|---|---|---|---|---|---|---|
| mobile billboard advertising | Commercial (national SERP, mixed) | High nationally | National | Low (national brands); win it via local variants | Homepage (secondary) | No |
| mobile billboard advertising company | Commercial | Medium | National + local | Medium | Homepage | No |
| mobile digital billboard advertising | Commercial | Low–medium | National | Medium | Homepage | No |
| mobile LED billboard advertising | Commercial | Low–medium | National | Medium | Homepage / Exclusive Rental | No |
| LED billboard truck advertising | Commercial | Low–medium | National | Medium | Exclusive Rental | No |
| digital billboard truck rental | Transactional | Low–medium | National + local | **High** (strong buyer intent) | Exclusive Rental (retitled) | No |
| mobile advertising truck rental | Transactional | Low | National | High | Exclusive Rental | No |
| LED advertising truck | Commercial/mixed (some buyers want to *purchase* a truck) | Medium | National | Medium. Add negatives in Ads for "for sale" | Exclusive Rental | No |
| outdoor mobile advertising | Informational/commercial | Low | National | Low | Blog / Homepage | No |
| mobile billboard rental | Transactional | Medium | National + local | **High** | Exclusive Rental | No |

### 3.2 Local keywords

| Keyword | Intent | Rel. demand [Est.] | Opportunity | Target page | New page? |
|---|---|---|---|---|---|
| mobile billboard advertising Dallas TX | Commercial local | Medium (top local term) | **High** | Homepage | No |
| mobile billboard advertising Dallas Fort Worth / DFW | Commercial local | Low–medium | **High** | Homepage | No |
| LED billboard truck Dallas | Commercial local | Low | **High** | Exclusive Rental / Homepage | No |
| mobile advertising Dallas TX | Mixed (includes mobile phone ads) | Low–medium | Medium | Homepage (secondary) | No |
| mobile billboard advertising Rockwall TX | Commercial local | Very low | **High** (uncontested, and it's the business address) | `/rockwall-rowlett/` | No |
| mobile billboard advertising Frisco TX | Commercial local | Low | **High** | `/frisco-routes/` | No |
| mobile billboard advertising Plano TX | Commercial local | Low | High | `/north-dallas/` → "Plano, Frisco & Collin County" | No (consolidate) |
| mobile billboard advertising Fort Worth TX | Commercial local | Low–medium | Medium–High | `/fort-worth-mobile-billboards/` | **Yes, only if trucks run Fort Worth routes or bookings** |
| mobile billboard advertising Austin TX | Commercial local | Medium | Medium (competitive) | Austin page | No (rebuild) |
| mobile billboard advertising Houston TX | Commercial local | Medium | Medium (competitive) | Houston page | No (rebuild) |
| mobile billboard advertising San Antonio TX | Commercial local | Low–medium | Medium | San Antonio page | No (rebuild) |

### 3.3 Long-tail commercial keywords

| Keyword | Intent | Target page | New page? |
|---|---|---|---|
| rent a mobile digital billboard truck | Transactional | Exclusive Rental | No |
| digital billboard truck for events | Commercial | Event Routes | No |
| mobile billboard advertising for small businesses | Commercial | Daily Route Advertising (shared routes are the SMB product) | No |
| LED truck advertising for grand openings | Commercial | `/grand-opening-advertising/` | **Yes** |
| mobile advertising for concerts and festivals | Commercial | Event Routes + event sub-page | Optional |
| mobile billboard advertising for restaurants | Commercial | `/restaurant-bar-advertising/` (pairs with the Nightlife route) | **Yes** |
| mobile billboard advertising for real estate | Commercial | `/real-estate-mobile-billboards/` | **Yes** |
| mobile billboard advertising for political campaigns | Commercial (seasonal, high value) | `/political-campaign-mobile-billboards/` | **Yes** (by 2027/2028 election cycles; must follow political ad disclosure rules) |
| mobile billboard advertising for product launches | Commercial | Exclusive Rental section + blog | No |
| cost of mobile billboard advertising / pricing | Commercial investigation | `/mobile-billboard-pricing/` | **Yes (top priority)** |

### 3.4 Keyword map and cannibalisation

| Page | Primary | Secondary |
|---|---|---|
| Homepage `/` | mobile billboard advertising Dallas–Fort Worth | mobile LED billboard trucks DFW, mobile billboard company Dallas, digital billboard truck Dallas |
| `/daily-route-advertising/` | shared mobile billboard routes Dallas | affordable mobile billboard advertising, mobile billboard for small business |
| `/dallas-nightlife-route/` (merged) | Dallas nightlife advertising | Deep Ellum / Uptown advertising, mobile billboard Friday Saturday night |
| `/dallas-day-routes/` | mobile billboard Dallas daytime routes | downtown Dallas billboard truck, Victory Park advertising |
| `/exclusive-rental/` | LED billboard truck rental Dallas | digital billboard truck rental, rent a mobile billboard truck |
| `/event-routes/` | event mobile billboard advertising Dallas | AT&T Stadium / Cowboys game advertising, concert billboard truck |
| `/frisco-routes/` | mobile billboard advertising Frisco TX | Legacy West advertising, The Star Frisco |
| `/north-dallas/` | mobile billboard Plano TX | McKinney, Allen, Richardson mobile billboard |
| `/rockwall-rowlett/` | mobile billboard Rockwall TX | Rowlett, Royse City, Rockwall County advertising |
| Austin, Houston and San Antonio pages | mobile billboard advertising [city] TX | LED billboard truck [city] |
| NEW `/mobile-billboard-pricing/` | mobile billboard cost Dallas | LED truck rental price, mobile billboard price per day |
| NEW industry and event pages | [industry] mobile billboard advertising | — |

**Cannibalisation risks [Verified]:**
1. `/dallas-night-routes/` vs `/dallas-nightlife-route/`: merge them.
2. `/daily-route-advertising/` vs `/dallas-day-routes-…/`: differentiate. One is the *product* (how shared routes work, all areas), the other is the *Dallas daytime route* (schedule and corridors).
3. The Exclusive Rental concept repeats on the Austin, Houston and San Antonio pages: keep each city focused on its own city, and link to the main Exclusive Rental page for "how it works".
4. Many titles use near-identical "Mobile LED Billboard Truck…" phrasing, so Google can't tell them apart. The new titles below each lead with a unique modifier.

### 3.5 Week-1 keyword validation (included in the engagement)

1. **Google Keyword Planner** (free with a Google Ads account): Dallas-Fort Worth DMA + Texas, last 12 months. Pull every keyword in 3.1–3.3 plus suggestions.
2. **Search Console → Performance:** last 16 months, filtered by queries containing "billboard", "truck", "led", "mobile".
3. Optional **Semrush or Ahrefs** (one month, about $130–$140): KD, competitor keyword gaps for texasmobileadvertising.com, bulldogbillboards.com, mobilebillboardglobal.com, ledtruckmedia.com.

## 12d. Phase 4 — Local SEO and Google Business Profile

**What we verified:**
- A GBP listing named **"MOD Media"** exists (linked from the site's "Leave a Review" button).
- The Maps link's place coordinates are about **32.9553, ‑96.8931**. That appears to be the Carrollton/Farmers Branch area, **not Rockwall**, while the website footer says **181 County Line Road, Rockwall, TX 75032**. **This should be confirmed and corrected.** If the pin, address and website disagree, local ranking signals weaken.
- The phone number is consistent across the site.

**GBP set-up rules (policy-safe):**
- MOD Media drives to customers, so it should normally be set up as a **service-area business**. *Hide the street address* if customers don't visit it, and list service areas (Dallas, Frisco, Plano, McKinney, Rockwall, Rowlett, Garland, Fort Worth if served…).
- Google allows up to 20 service areas. Keep them to areas where trucks actually run.
- Austin, Houston and San Antonio **must not get separate GBP listings** unless a real, staffed location exists there. A virtual office would violate Google's guidelines. Win those cities through landing pages and Ads.
- **Business name:** use the real-world name exactly as it appears on signage and legal documents ("MOD Media"). Don't add keywords such as "MOD Media – Mobile Billboard Trucks Dallas"; that's a suspension risk.

**Recommended categories.** Verify the exact names in the GBP category picker, because Google's list changes.
- **Primary:** *Advertising service*, or *Advertising agency* if "Advertising service" isn't offered. Pick whichever the top-ranking local competitors use. Check them with a free GBP category inspector extension (e.g. GMBspy or Pleper) on the Maps results for "mobile billboard Dallas".
- **Secondary candidates:** *Marketing agency*, *Outdoor advertising* (if it exists in the picker), *Digital signage* or *Sign shop* (only if relevant), *Event planner* (no, they don't plan events). **Avoid "Truck rental agency"**: customers don't rent the truck to drive themselves, so the category would be misleading.

**GBP optimisation checklist:**

| # | Item | Done? |
|---|---|---|
| 1 | Verify ownership; add a second manager (agency) | ☐ |
| 2 | Confirm the business name = real brand ("MOD Media") with no keywords | ☐ |
| 3 | Fix the pin location; set up as a service-area business; hide the address if no customer visits | ☐ |
| 4 | Service areas: list the DFW cities actually served (max 20) | ☐ |
| 5 | Primary and secondary categories (above) | ☐ |
| 6 | Phone: (469) 279-2511 (or a tracked number as primary, with the main number as additional, to keep NAP consistent) | ☐ |
| 7 | Website: `https://modmediadfw.com/?utm_source=google&utm_medium=organic&utm_campaign=gbp` | ☐ |
| 8 | Hours (office/booking hours); note route schedules in the description and posts | ☐ |
| 9 | Description (750 chars), see the draft below | ☐ |
| 10 | Services: Daily Route Advertising, Dallas Nightlife Route, Dallas Day Route, Frisco Route, North Dallas Route, Rockwall/Rowlett Route, Exclusive LED Truck Rental, Event Route Advertising, Ad Design (if offered), each with a description and "starting at" price where possible | ☐ |
| 11 | Products: one per route/package, with a photo and a "Learn more" link to the matching page | ☐ |
| 12 | Photos: 20+ real photos (trucks at landmarks by day and night, screens showing client ads with permission, team, interior/driver), then 2–4 new each week | ☐ |
| 13 | Videos (optional): upload any existing truck clips the client already has | ☐ |
| 14 | Logo and cover photo | ☐ |
| 15 | Attributes: e.g. "Family-owned" or ownership attributes if they apply and are offered | ☐ |
| 16 | Weekly Google Posts: route schedule, event coverage, client spotlight, offer | ☐ |
| 17 | Seed the Q&A with real frequent questions (asked and answered honestly) | ☐ |
| 18 | Messaging/chat on, with a response target of under 1 hour in business hours | ☐ |
| 19 | Review link: short "write a review" link (GBP → Ask for reviews), replacing the current long Maps URL on the site | ☐ |
| 20 | Respond to every review within 48 h | ☐ |

**Draft GBP description (no keyword stuffing):**
> MOD Media is a family-owned mobile billboard company based in Rockwall, Texas, running full-color LED billboard trucks across Dallas–Fort Worth since 2023. Businesses can join our scheduled shared routes (Dallas days, Dallas nightlife Friday and Saturday 6–11 pm, Frisco Mondays and Wednesdays, North Dallas, and Rockwall/Rowlett) or book an exclusive truck for grand openings, product launches, recruiting, political campaigns and major events at AT&T Stadium, American Airlines Center and beyond. Exclusive rentals are also available in Austin, Houston and San Antonio. Call or text for a free route plan and quote.

*(Confirm every claim, such as "since 2023", the route days and the cities, before publishing.)*

**Review acquisition program (genuine customers only):**
1. **Trigger:** the day a campaign ends, send the client their photo recap. That's the moment they're happiest.
2. **Message (SMS + email):** "Thanks for running with MOD Media! Here are the photos of your ad on the road. If we earned it, would you share a quick Google review? It really helps a small family business: [short link]."
3. **Follow up once** after 5 days, and never more.
4. **Never offer discounts or gifts for reviews**, never gate (only asking happy clients via a filter), and never write reviews for clients. All of these break Google's policy and the FTC rules on fake reviews (FTC final rule, 2024).
5. **Prompt for useful detail:** ask them to mention the route or event, e.g. "Feel free to mention which route or event you ran". This produces naturally relevant reviews without scripting.
6. **Target:** 2–4 new reviews per month. Respond to every one by name, and mention the service naturally ("Glad the Cowboys game-day route brought calls in!").

**Citations and NAP:** after the name, address and pin are finalised, make NAP consistent on Bing Places, Apple Business Connect, Yelp, BBB, Facebook, the Nextdoor Business page, the Rockwall Area Chamber, the Frisco Chamber, the Dallas Regional Chamber (if joined), Manta, Yellow Pages, Thumbtack (optional), and OOH directories (AdQuick, Billboard Insider, OAAA membership). Use **one** name format everywhere.

## 12e. Phase 5 — Competitor analysis (detail)

All competitor pages were reviewed on 13 Nov 2026. The comparison focuses on what buyers and Google see on each site: structure, content, schema, pricing transparency and lead capture.

| | Texas Mobile Advertising | Bulldog Billboards | Mobile Billboard Global | LED Truck Media | Lime Media | Big Wave Display | Rolling Adz | MOD Media |
|---|---|---|---|---|---|---|---|---|
| URL | texasmobileadvertising.com | bulldogbillboards.com | mobilebillboardglobal.com | ledtruckmedia.com | lime-media.com | bigwavedisplay.com | rollingadz.com | modmediadfw.com |
| Services | LED, static and glass-walled trucks | LED, static, glass-walled | LED trucks, event, political, grand openings | LED trucks + "interactive" | LED trucks | LED truck (DFW) | LED trucks, rideshare wraps, fleets | LED truck: shared routes, exclusive, events |
| Locations | 15 Texas cities | 25+ US cities | 9+ states | National | National | DFW | National | DFW + Austin/Houston/SA |
| Homepage H1 | "Texas Mobile Advertising" | NYC-focused H1 | "Mobile Billboard Advertising in Texas" (Texas page) | Dallas-specific H1 | "LED billboard truck dallas services" | "DFW's most unique way to be seen." | "Nationwide Mobile Billboard Advertising Solutions" | **None** |
| Schema | LocalBusiness, Org | Org only | LocalBusiness, Service, FAQPage | LocalBusiness, FAQPage | FAQPage | None | Org, Article | Org only |
| Pricing shown | No | No | **"From $1,400/Day"** | Budget ranges in form | No | No | Cost guide article | **No** |
| FAQ | Yes (/faq/) | Yes | Yes | Yes | Yes | Yes | Yes | **No** |
| Blog | Active (Nov 2026 posts) | Yes | Yes | — | — | No | "Academy" | Only "Hello world!" |
| Quote form fields | Name, email, phone, city, vehicle, # vehicles, promotion, date | ~8 fields | — (cart/contact) | Name, company, phone, services, budget, dates | — | Name, business, phone, email, message | Book-a-demo | Name, email, message |
| Distinct USP | Texas-wide, multiple vehicle types | National reach, GPS guarantee claims | Transparent pricing, $0 creative | Scale, retargeting | — | Local DFW | Guarantees, measurement | **Fixed weekly DFW routes; family-owned; local events** |

**Why competitors may be outperforming MOD Media:**
- Their pages have clear H1s and titles that match the searched phrase ("Dallas Mobile Advertising and Mobile Billboards", "Mobile Billboard Truck Advertising in Dallas, Texas").
- They answer buyer questions on the page: FAQs, specs, cost guides and price starting points.
- They use LocalBusiness, Service and FAQ schema.
- They have more indexable pages that target cities, industries and events.
- They have no visible placeholder content.
- They collect richer lead data (phone, date, city, budget).

**What MOD Media can do differently:** be the **only genuinely local, transparent DFW operator.** That means publishing real route schedules and maps, a "Starting at" price, real DFW campaign photos, client stories, and event calendars. The national template sites can't fake that.

**Which competitors to prioritise:**
1. **Texas Mobile Advertising / Bulldog** (one operator across two domains; the strongest Dallas organic footprint).
2. **Big Wave Display** (the direct local LED competitor with a weak site, so the easiest to outrank).
3. **Mobile Billboard Global and LED Truck Media** on Dallas and Texas city terms.

**Easiest realistic ranking opportunities [Estimate]:**
- Rockwall, Rowlett and Royse City terms (no competitor targets them).
- Frisco, plus "Legacy West" and "The Star" advertising.
- "Dallas nightlife / Deep Ellum / Uptown advertising".
- "Billboard truck AT&T Stadium / Cowboys game".
- "Mobile billboard cost Dallas".
- Industry + Dallas combinations (bail bonds, restaurants, real estate, home services).

## 12f. Phase 6 — Content strategy

### A. Service and location pages: keep, merge or create

| Topic | Action | Reason |
|---|---|---|
| Mobile billboard advertising in Dallas | **Improve the homepage** to be this page | Avoids a homepage vs. Dallas-page duplicate |
| Mobile LED billboard truck advertising | Fold into the homepage + Exclusive Rental | Same intent |
| Daily Route Advertising | Improve (product page for shared routes) | Core SMB product |
| Dallas Nightlife | **Merge** the two pages into one | Cannibalisation |
| Exclusive LED Truck Rentals | Improve; retitle to "LED Billboard Truck Rental" | Buyer phrase |
| Event Advertising | Improve + add 2–3 event sub-pages (AT&T Stadium game days, State Fair of Texas, AAC concerts) | Seasonal, high-value |
| Frisco | Improve (unique) | Real recurring route |
| North Dallas | Improve; retitle "Plano, McKinney & Collin County" | Captures the Plano searches |
| Rockwall & Rowlett | Improve; fix "Royse City" | Home market |
| Fort Worth | **Create only if trucks run Fort Worth** campaigns (Stockyards, Dickies Arena, Sundance Square) | Medium demand; a competitor already targets it |
| Austin, Houston, San Antonio | Keep as **exclusive-rental city pages**; remove the Dallas boilerplate; add logistics (how the truck gets there, minimum days, travel fee) | Genuinely served, but only through exclusive bookings |
| City Routes hub | Make it a real hub: a map plus a table of routes × days × times × areas | Thin today |
| Pricing | **Create** | Top-converting intent |
| Industry pages (Restaurants & Bars, Real Estate, Grand Openings, Political, Home Services/Legal) | **Create**, one at a time, each with real examples | Conversion-focused long tail |
| Case studies | **Create** `/case-studies/` with 3–5 stories | Trust and AI-search citations |

**Rule for every city page:** at least 60% unique content. That means the specific schedule, corridors and venues, local regulations notes, a local photo and a local FAQ. Don't duplicate pages for cities without real operations.

### B. Blog and resource topics (25, prioritised for commercial intent)

Columns: Title | Primary KW | Secondary | Intent | Audience | Slug | H2 outline (short) | Internal links | Conversion goal | Priority

| # | Title | Primary keyword | Secondary keywords | Intent | Audience | Slug | Suggested H2s | Internal links | Conversion | Pri. |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | How Much Does Mobile Billboard Advertising Cost in Dallas? (2026 Guide) | mobile billboard cost Dallas | LED truck rental price, price per day | Commercial | All SMBs | `/blog/mobile-billboard-cost-dallas/` | What affects price · Shared route vs exclusive · Typical ranges · Hidden costs (design, permits, travel) · How to get a quote | Pricing, Daily Route, Exclusive | Quote | **P1** |
| 2 | Mobile Billboards vs. Traditional Billboards in DFW | mobile billboard vs billboard | static billboard cost Dallas | Comparison | Marketing managers | `/blog/mobile-vs-traditional-billboards-dallas/` | Cost · Targeting · Flexibility · Frisco's billboard rules (cite ordinance) · When to use each | Homepage, Frisco | Quote | **P1** |
| 3 | How to Advertise at a Cowboys Game (Without Being an Official Sponsor) | advertise at AT&T Stadium | Cowboys game advertising, Arlington | Commercial | Local businesses, bars | `/blog/advertise-at-cowboys-games/` | Where crowds walk · Timing · Rules & legal (no trademark misuse) · Example route | Event Routes | Quote | **P1** |
| 4 | Grand Opening Marketing in Dallas: A 30-Day Plan | grand opening marketing Dallas | grand opening advertising ideas | Commercial | New businesses | `/blog/grand-opening-marketing-dallas/` | 30/14/7/day-of timeline · Mobile billboard role · Social + GBP · Measuring footfall | Grand Opening page | Quote | **P1** |
| 5 | Are Mobile Billboards Effective? What the Data Says | are mobile billboards effective | mobile billboard ROI, impressions | Consideration | Skeptical buyers | `/blog/are-mobile-billboards-effective/` | How impressions are estimated · Recall research (cite OAAA/Geopath) · How to track (QR, codes, call tracking) · Real MOD client example | Case studies | Quote | **P1** |
| 6 | Restaurant & Bar Advertising Ideas for Deep Ellum and Uptown | restaurant advertising Dallas | bar marketing, nightlife promotion | Commercial | Restaurants/bars | `/blog/restaurant-bar-advertising-dallas/` | Weekend timing · Promo ideas · QR offers · Nightlife route | Nightlife route, Restaurant page | Quote | P2 |
| 7 | Real Estate Marketing with LED Billboard Trucks | real estate mobile billboard | open house advertising, builder marketing | Commercial | Agents, builders | `/blog/real-estate-mobile-billboards/` | New-community launches · Open houses · Recruiting agents · Compliance (TREC advertising rules) | Real Estate page | Quote | P2 |
| 8 | Political Mobile Billboards in Texas: Rules & Best Practices | political mobile billboard Texas | campaign truck advertising | Commercial | Campaigns, consultants | `/blog/political-mobile-billboards-texas/` | Disclosure requirements (Texas Ethics Commission) · Route planning by precinct · Timing · Costs | Political page | Quote | P2 |
| 9 | How to Design a Mobile Billboard Ad That People Remember | mobile billboard design tips | LED billboard ad design | Informational → commercial | All | `/blog/mobile-billboard-design-tips/` | 7-word rule · Contrast at night · Motion · QR sizing · Examples | Free quote (design help) | Quote | P2 |
| 10 | Shared Route vs. Exclusive LED Truck: Which Is Right for You? | exclusive LED truck rental | shared mobile billboard | Commercial | SMBs | `/blog/shared-vs-exclusive-mobile-billboard/` | Cost · Share of voice · Use cases · Decision table | Daily Route, Exclusive | Quote | **P1** |
| 11 | Best Places to Advertise in Frisco, TX | advertising in Frisco TX | Legacy West, The Star, PGA Frisco | Commercial local | Frisco businesses | `/blog/advertise-in-frisco-tx/` | Hotspots · Billboard restrictions · Route schedule | Frisco route | Quote | P2 |
| 12 | Hiring Is Hard: Using Mobile Billboards for Recruitment in DFW | recruitment advertising Dallas | hiring billboard truck | Commercial | Employers, staffing | `/blog/recruitment-mobile-billboards-dallas/` | Target industrial corridors · Messaging · QR to apply | Exclusive | Quote | P2 |
| 13 | How to Promote a Concert or Festival in Texas | promote concert Texas | festival marketing | Commercial | Promoters | `/blog/promote-concert-festival-texas/` | Pre-sale buzz · Day-of routes · Cross-city tours (Austin, Houston, SA) | Event Routes, city pages | Quote | P2 |
| 14 | State Fair of Texas Advertising Guide | State Fair of Texas advertising | Fair Park marketing | Commercial, seasonal | Local businesses | `/blog/state-fair-of-texas-advertising/` | Crowds & dates · Routes around Fair Park · Rules | Event Routes | Quote | P2 (publish by Aug) |
| 15 | Mobile Billboards for Home Service Companies (Holiday Lights, HVAC, Roofing) | home services advertising Dallas | contractor marketing | Commercial | Home services | `/blog/home-services-mobile-billboards/` | Seasonal timing · Neighbourhood routes · Case: Christmas-light client (with permission) | Daily Route | Quote | P2 |
| 16 | Mobile Billboard Advertising vs. Facebook Ads for Local Businesses | mobile billboard vs digital ads | offline vs online advertising | Comparison | SMBs | `/blog/mobile-billboard-vs-facebook-ads/` | Reach vs targeting · Combine both · Retargeting with geofencing | Homepage | Quote | P3 |
| 17 | How Many People See a Mobile Billboard? Understanding Impressions | mobile billboard impressions | how impressions are measured | Informational | Marketing managers | `/blog/mobile-billboard-impressions/` | Methodologies · Caveats · What MOD reports | Reporting page | Quote | P2 |
| 18 | Mobile Billboard Advertising in Houston: Where to Route Your Truck | mobile billboard Houston | Galleria, Energy Corridor | Commercial | Houston brands | `/blog/houston-mobile-billboard-routes/` | Districts · Event venues (Daikin Park, Toyota Center, NRG) · Logistics | Houston page | Quote | P3 |
| 19 | Austin Event Marketing: SXSW, ACL and F1 Weekend | Austin event marketing | SXSW advertising | Commercial, seasonal | Brands | `/blog/austin-event-marketing/` | Event calendar · City permit considerations · Exclusive rental | Austin page | Quote | P3 |
| 20 | 10 Creative Mobile Billboard Campaign Ideas | mobile billboard ideas | creative truck advertising | Inspiration | All | `/blog/mobile-billboard-campaign-ideas/` | Ideas with MOD photos | Services | Quote | P3 |
| 21 | How to Track Results from a Mobile Billboard Campaign | mobile billboard tracking | QR code tracking, call tracking | Informational | Marketing managers | `/blog/track-mobile-billboard-results/` | QR + UTM · Unique numbers · Promo codes · Lift in branded search | Reporting | Quote | P2 |
| 22 | Product Launch Marketing with LED Trucks | product launch advertising | launch event marketing | Commercial | Brands | `/blog/product-launch-led-truck/` | Teaser → launch → follow-up · Multi-city | Exclusive | Quote | P3 |
| 23 | Car Dealership Advertising Ideas That Drive Showroom Traffic | car dealership advertising Dallas | dealership promotion | Commercial | Dealers | `/blog/car-dealership-advertising-dallas/` | Sales-event routes · Competitor-adjacent routes (legal) | Exclusive | Quote | P3 |
| 24 | Rockwall & Rowlett Small Business Marketing Guide | Rockwall marketing | Rowlett advertising | Commercial local | Local SMBs | `/blog/rockwall-small-business-marketing/` | Local media options · Route schedule · Chamber events | Rockwall page | Quote | P2 |
| 25 | Is Mobile Billboard Advertising Legal in Dallas? Rules & Permits | mobile billboard laws Texas | truck advertising regulations | Informational | All | `/blog/mobile-billboard-laws-texas/` | State & city rules (cite sources only) · Parking/idling · What MOD handles | FAQ | Quote | P2 (only with verified legal sources) |

Each article must include real MOD photos, a "Get a quote" block and links to two or more service pages. Publish up to 5 per month. Quality and proof matter more than volume.

## 13. Phase 7 — On-page SEO implementation (copy-ready)

> Titles are ≤ 60 characters where possible, and descriptions are ≤ 155. Set Yoast → Settings → Site basics → **Site name = "MOD Media"**, and change the title separator so titles end in "| MOD Media" instead of "- modmediadfw.com".

### Homepage — `https://modmediadfw.com/`
- **SEO title:** Mobile Billboard Advertising in Dallas–Fort Worth | MOD Media
- **Meta description:** LED billboard trucks on scheduled DFW routes, at events, or exclusive to your brand. Family-owned in Rockwall, TX. Get a free route plan and quote.
- **H1:** Mobile Billboard Advertising Across Dallas–Fort Worth
- **H2s:**
  - LED Billboard Trucks That Go Where Your Customers Are
  - Choose Your Campaign: Shared Routes, Nightlife, Events or Exclusive
  - Our Weekly DFW Routes
  - How It Works (Pick a Route → Send Your Ad → We Drive → You Get a Report)
  - What Does a Mobile Billboard Cost?
  - Real Campaigns, Real Clients
  - Why Businesses Choose MOD Media
  - Frequently Asked Questions
  - Get Your Free Route Plan
- **Primary KW:** mobile billboard advertising Dallas–Fort Worth. **Secondary:** LED billboard truck Dallas, digital billboard truck DFW, mobile billboard company.
- **Content changes:**
  - Remove the duplicated hero and services sections (keep one responsive version).
  - Replace "proudly serving ALL of Texas and the US" with "Serving Dallas–Fort Worth daily, with exclusive rentals in Austin, Houston and San Antonio". That's accurate and focused.
  - Add truck specs (screen size, resolution, sides, audio if any, video vs. static ad support, ad length and rotation).
  - Add a "Starting at" line.
  - Add a 6-question FAQ.
  - Fix the "Cusotmer success" typo.
  - Turn "Featured Partner Brands" into "Brands We've Run" only if those clients are confirmed. Otherwise remove the NFL, Big 12 and other logos.
- **Images:**
  - WebP hero image with the alt text "MOD Media LED billboard truck driving through downtown Dallas at night".
  - Compress the video and add a poster image.
  - Name files descriptively.
- **Schema:** LocalBusiness (Organization upgrade), WebSite (name fix), VideoObject for the truck video.
- **CTA:** primary "Get a Free Route Plan & Quote" (opens the form); secondary "Call or Text (469) 279-2511". Use a sticky mobile bar with Call, Text and Quote.

**Suggested hero copy:**
> **Mobile Billboard Advertising Across Dallas–Fort Worth**
> Put your ad on a full-color LED billboard truck and take it straight to Deep Ellum on Saturday night, Legacy West on Monday, or AT&T Stadium on game day. Join a scheduled route or book a truck exclusively for your brand.
> **[Get a Free Route Plan & Quote]** **[Call or Text (469) 279-2511]**
> ✓ Family-owned in Rockwall, TX ✓ Running DFW routes since 2023 ✓ Free ad set-up on your first campaign *(only if true)*

### `/services/`
- **Title:** Mobile Billboard Services & Pricing in DFW | MOD Media
- **Description:** Compare shared daily routes, Dallas nightlife, event routes and exclusive LED truck rentals. See starting prices and book a free quote.
- **H1:** Mobile Billboard Truck Services & Pricing
- **H2s:** Compare Our Services (table) · Shared Routes · Exclusive Truck Rental · Event Routes · What's Included · Starting Prices · FAQs · Get a Quote
- **Content:** a comparison table (Service | Best for | Schedule | Share of voice | Starting at | Link). Replace the empty pricing section.
- **Schema:** Service (×4) with `provider` = the LocalBusiness `@id`.
- **CTA:** "Compare Options & Get a Quote".

### `/daily-route-advertising/`
- **Title:** Shared Mobile Billboard Routes in Dallas | MOD Media
- **Description:** Get your ad on our LED billboard trucks along scheduled routes in Dallas, Frisco, North Dallas and Rockwall. An affordable way to reach locals daily.
- **H1:** Daily Route Mobile Billboard Advertising in DFW
- **H2s:** How Shared Routes Work · Weekly Route Schedule (table) · Who It's For · What's Included (rotation, ad length, number of advertisers per truck) · Pricing · Results from Clients like Atlas Bail Bonds (with permission) · FAQs · Reserve Your Spot
- **Replace the Lorem block** with:
  > **Reserve Your Spot on This Week's Route**
  > Routes fill on a first-come basis. Tell us your business, your target area and your start date. We'll send a route map and price within one business day.
  > [Get My Route Plan] [Call (469) 279-2511]
- **Remove** the repeated "About us" H4 labels and the duplicate "DAILY ROUTE ADVERTISING" closing block.
- **Schema:** Service (`serviceType`: "Shared mobile billboard route advertising", `areaServed`: the DFW cities).

### `/dallas-nightlife-route/` (merge `/dallas-night-routes/` into this one, with a 301)
- **Title:** Dallas Nightlife Advertising: Deep Ellum & Uptown | MOD Media
- **Description:** Put your brand on an LED billboard truck through Deep Ellum, Uptown and Lower Greenville every Friday and Saturday, 6–11 pm. Book your spot.
- **H1:** Dallas Nightlife Mobile Billboard Route
- **H2s:** Friday & Saturday, 6–11 pm · Where We Drive (Deep Ellum, Uptown/McKinney Ave, Lower Greenville, Victory Park; confirm actual) · Best For (bars, restaurants, events, rideshare/legal/bail services, apps) · Ideas That Work at Night (QR, specials) · Pricing · FAQs · Book the Nightlife Route
- **Content:** keep the Deep Ellum and Uptown mentions from the night-routes meta description (they're good).

### `/dallas-day-routes/` (rename the slug from `/dallas-day-routes-mobile-led-billboard-truck/` and 301 the old one)
- **Title:** Dallas Daytime Mobile Billboard Routes | MOD Media
- **H1:** Dallas Day Routes for Mobile Billboard Advertising
- **H2s:** Weekday Route Schedule · Areas Covered (Downtown, Victory Park, Design District…) · Best For · Pricing · FAQs
- **Remove** the "Strategy Behind frisco & nightlife route" section.

### `/exclusive-rental/`
- **Title:** LED Billboard Truck Rental in Dallas & Texas | MOD Media
- **Description:** Rent a digital billboard truck exclusively for your brand: your route, your hours, 100% share of voice. DFW, Austin, Houston and San Antonio.
- **H1:** Exclusive LED Billboard Truck Rental
- **H2s:** Your Truck, Your Route, Your Message · Popular Uses (grand openings, launches, recruiting, political, events) · Truck Specs · How Booking Works · Pricing (hourly/half-day/full-day starting points) · Available in DFW, Austin, Houston & San Antonio · Reporting & GPS · FAQs · Request a Custom Route
- **Schema:** Service + an `offers` priceSpecification only if real starting prices are published.

### `/event-routes/`
- **Title:** Event Mobile Billboard Advertising in DFW | MOD Media
- **Description:** Reach fans before and after Cowboys, Mavericks, Stars and Rangers games, concerts and festivals with LED billboard trucks. See upcoming events.
- **H1:** Event Route Mobile Billboard Advertising in Dallas–Fort Worth
- **H2s:** Venues We Cover (AT&T Stadium, Globe Life Field, American Airlines Center, Fair Park, Dickies Arena, Toyota Stadium; confirm) · Upcoming Event Calendar (refresh monthly) · Timing Strategy · Rules We Follow · Pricing · Client Example (the Cowboys-game testimonial) · FAQs
- **Legal note:** don't use team logos or imply official sponsorship.

### `/frisco-routes/`
- **Title:** Mobile Billboard Advertising in Frisco, TX | MOD Media
- **Description:** Frisco limits roadside billboards, but our LED trucks drive Legacy West, The Star and Frisco Square every Monday and Wednesday. Book your spot.
- **H1:** Frisco Mobile Billboard Advertising Routes
- **H2s:** Why Mobile Works in Frisco (cite the actual sign ordinance) · Monday & Wednesday Route · Stops: Legacy West, The Star, PGA Frisco, Frisco Convention Center · Who Advertises in Frisco · Pricing · FAQs
- **Remove** the Houston, San Antonio and Austin sentence.

### `/north-dallas/`
- **Title:** Mobile Billboards in Plano, McKinney & Allen | MOD Media
- **H1:** North Dallas & Collin County Mobile Billboard Advertising
- **H2s:** Cities We Cover (Richardson, Plano, Frisco, McKinney, Allen, Anna, Melissa) · Route Schedule · Hotspots per City · FAQs
- **Remove** the copied Frisco block.

### `/rockwall-rowlett/`
- **Title:** Mobile Billboard Advertising in Rockwall & Rowlett | MOD Media
- **Description:** Our home market. LED billboard trucks covering Rockwall, Rowlett, Royse City and Heath: shopping centres, I-30 and community events.
- **H1:** Rockwall, Rowlett & Royse City Mobile Billboards
- **Fix** "Royce" → "Royse". Add local events (e.g. Rockwall Founders Day, if they're covered) and Harbor District stops.

### Austin, Houston and San Antonio pages
- **Austin title:** Austin Mobile Billboard Truck Rental | MOD Media (slug ideally `/austin-mobile-billboards/` with a 301 from the current slug)
- **Houston title:** Houston Mobile Billboard Truck Rental | MOD Media (keep the slug)
- **San Antonio title:** San Antonio Mobile Billboard Truck Rental | MOD Media
- **H1 pattern:** "[City] Mobile Billboard Advertising: Exclusive LED Truck Rental"
- **Each page:** remove the "Dallas Businesses…" and "Strategy Behind frisco…" blocks. Add an "Availability & logistics" section (minimum booking, travel or positioning fee, lead time). Update venue names (Houston: **Daikin Park**). Add a city-specific FAQ.

### `/about-us/`
- **Title:** About MOD Media | Family-Owned Mobile Billboards, Texas
- **H1:** About MOD Media
- **Content:**
  - Remove the Vision and Mission repeated three times.
  - Add the owners' names and photo, the founding story (est. 2022, campaigns since May 2023), fleet details (number of trucks, screen specs), service area, and any insurance or DOT compliance details.
  - Add memberships (chambers, OAAA if joined).
  - These are E-E-A-T and entity signals.
- **Schema:** AboutPage + Organization with `founder` and `foundingDate`.

### `/testimonials/`
- **Title:** MOD Media Reviews & Client Results | Mobile Billboards DFW
- **Description:** Read what Dallas–Fort Worth businesses say about advertising with MOD Media's LED billboard trucks, and see real campaigns on the road.
- **H1:** Client Reviews & Campaign Results
- **Content:**
  - Pair each testimonial with the client's business name, industry, route used, and a photo of their ad on the truck (with permission).
  - Remove the empty "Gave MOD Media Ads 5.0 Stars" entries.
  - Add a "Leave a review" short link.
- **Schema:** don't add self-serving `AggregateRating` for LocalBusiness on your own site, because Google doesn't show review stars for self-served LocalBusiness reviews. Plain testimonials are fine.

### `/free-quote/` → (consider renaming the slug to `/get-a-quote/` with a 301; optional)
- **Title:** Get a Free Mobile Billboard Quote | MOD Media
- **Description:** Tell us your goals, area and dates. We'll send a custom route plan and price within one business day. Call or text (469) 279-2511.
- **H1:** Get a Free Route Plan & Quote
- **Form:** see Section 15. Add "What happens next" (1. We review · 2. You get a route map + price · 3. Approve & send artwork, or we design it).
- Also create `/contact/` → 301 to this page.

### NEW `/mobile-billboard-pricing/`
- **Title:** Mobile Billboard Truck Pricing in Dallas (2026) | MOD Media
- **H1:** How Much Does Mobile Billboard Advertising Cost?
- **H2s:** Price Factors · Shared Route Pricing · Exclusive Rental (hourly/day) · Event Pricing · Design & Extras · Example Budgets ($X/week for a restaurant; $Y for a grand opening day) · Compare: Static Billboard Costs in Dallas (cite sources) · FAQs · Get Your Exact Quote
- **Note:** publish ranges the client is comfortable with ("from $___"). Third-party market benchmarks that can be cited include AdQuick ($1,250–$3,600+/day for digital trucks, depending on market) and Mobile Billboard Global ("From $1,400/Day"). MOD's shared routes are likely a cheaper entry point, and that's a selling point if true.

## 14. Phase 8 — Conversion rate optimisation

### First-visit test (business owner persona) [Verified observations]

| Question a prospect has | Can they answer it quickly? | Notes |
|---|---|---|
| What does the company offer? | Partly | The hero says "DFW's #1 Mobile LED Billboards" (an unsupported "#1" claim; remove it unless it can be substantiated). The services are clear further down |
| Who is it for? | No | No industries or use cases named above the fold |
| Which locations? | Confusing | "ALL of Texas and the US" vs DFW routes vs a 9-item city menu |
| Why MOD Media? | Weak | "Family-owned" and the testimonials are good but buried; no specs or proof of reach |
| How does it work? | No | No step-by-step |
| What's different? | Partly | Fixed routes and nightlife timing are unique, but not framed as the advantage |
| How much? | **No** | The pricing section is empty |
| Expected exposure? | No | The "Analytics Reporting" PDF is hidden behind a button on an external domain |
| How to request a quote? | Partly | Header button and phone; the form is weak; four pages have a broken phone link |

### Lead capture fixes

| Item | Current | Recommendation |
|---|---|---|
| Click-to-call | Present in header and sections; inconsistent `tel:` formats; 4 broken | Standardise on `tel:+14692792511`; add a sticky mobile bottom bar: **Call · Text · Get Quote** |
| SMS | "Call or Text Us" copy, but no `sms:` link | Add `sms:+14692792511?&body=Hi%20MOD%20Media%2C%20I%27d%20like%20a%20quote` |
| Email | `mailto:%20info@modmediaads.com` (leading space) | Fix the encoding; consider moving email to the website domain (info@modmediadfw.com) or redirect modmediaads.com to the site |
| Quote form | Name, email, message | **2-step form.** Step 1: Service (Shared route / Nightlife / Event / Exclusive / Not sure) + City + Start date. Step 2: Name, Business, Phone, Email, Budget range (optional: <$500, $500–$1,500, $1,500–$5,000, $5,000+), "Do you have artwork?" (Y/N), message. Starting with easy multiple-choice questions raises completion rates. Show the phone number next to the form |
| Homepage form | Newsletter only | Replace with an inline quote form (step 1) |
| Offer | "Call Now for Demo and get 1 FREE Ad" (unclear) | Clarify: e.g. "Free ad design on your first campaign" or "Free route plan". State the terms |
| Response promise | None | "We reply within 1 business hour" (only if the team can deliver) |
| Exit or scroll CTA | None | A light scroll-triggered banner on pricing and service pages: "Get this week's route availability" |
| Live proof | Testimonials only | Photo gallery of real client ads; a 30-second "ride-along" video; GPS route map screenshot; sample report (HTML) |

### Recommended homepage wireframe

1. **Sticky header:** logo · Services · Routes · Pricing · Results · About · **[Get a Quote]** · ☎ (469) 279-2511
2. **Hero:** H1 + one-line value + 2 CTAs + 3 trust ticks. Background is a compressed 6–8 s loop of the truck at night (with a poster image for mobile)
3. **"Choose your campaign":** 4 cards (Shared Routes · Nightlife · Events · Exclusive), each with "Best for…", "From $…" and "See details →" using descriptive link text
4. **Weekly route schedule:** table + small map (Mon/Wed Frisco; Fri/Sat nightlife; and so on)
5. **How it works:** 4 steps with icons
6. **See it in action:** video + 6-photo grid of real client ads on the truck
7. **Results and reviews:** 3 strongest testimonials with business names + Google rating badge (live widget, only from real GBP data) + link to case studies
8. **Truck specs and reporting:** screen size, resolution, visibility, GPS tracking, sample report
9. **Pricing teaser:** "Shared routes from $__/week · Exclusive from $__/hour" → Pricing page
10. **Who we help:** industry chips (Restaurants & Bars, Real Estate, Home Services, Legal & Bail Bonds, Events, Political, Retail) → industry pages
11. **Service area:** DFW city list + "Exclusive rentals in Austin, Houston, San Antonio"
12. **FAQ:** 6 questions
13. **Final CTA band:** "Get your free route plan in one business day" + inline form step 1
14. **Footer:** NAP (consistent), a working Facebook link, short links to all routes

### CTA library (use consistently)
- **Get a Free Route Plan & Quote** (primary)
- **Book Your Mobile Billboard Campaign**
- **Request a Custom Route**
- **Check This Week's Route Availability**
- **See Our LED Trucks in Action** (video)
- **Call or Text (469) 279-2511**

**Claims to avoid unless substantiated:** "DFW's #1", specific impression counts without a stated method, partner logos without permission, and guaranteed results.

## 15. Phase 9 — Facebook marketing strategy

### Why Facebook is the social channel
| Strength | Why it matters for MOD Media |
|---|---|
| Local business owners use it daily | The buyers (restaurant and bar owners, contractors, agents, retailers) check Facebook for local businesses and recommendations |
| Precise local ad targeting | Ads can reach a radius around Dallas, Frisco, Plano and Rockwall, by interests such as small business ownership, restaurants or real estate |
| Lead Ads | Prospects can request a quote without leaving Facebook, with name, phone and business pre-filled |
| Retargeting | The Meta Pixel lets MOD Media show ads to people who visited the pricing or quote pages |
| Reviews and Messenger | Recommendations and quick replies build trust before the first call |

### Facebook Page set-up checklist
- Use the same business name ("MOD Media"), phone, address/service area and website as the website and Google Business Profile.
- Category: Advertising/Marketing (or the closest available), with a description that mirrors the GBP description.
- Cover photo: a truck at night in Deep Ellum or Uptown with the screen lit.
- "Get Quote" or "Send Message" as the main button, with Messenger auto-replies for common questions (price, routes, availability).
- Turn on Recommendations (reviews).
- Pin a post with this week's route schedule.
- Connect the Page to Meta Business Suite and install the Meta Pixel on the website.

### Audiences
SMB owners within ~25 mi of Dallas; restaurant and bar owners (Deep Ellum, Uptown, Lower Greenville, Frisco); event and concert promoters; real estate agents, builders and brokerages; car dealerships; retail and franchise owners; home service companies; legal and bail bond firms (already proven); marketing managers and agencies; corporate event planners; brands launching products; political campaigns (seasonal).

### Content pillars
1. LED truck demos · 2. Behind the scenes · 3. Route of the week · 4. Client spotlights and success stories · 5. Before/after (design concept → on the truck) · 6. Event coverage · 7. Local advertising tips · 8. Education (cost, effectiveness, design) · 9. Testimonials · 10. Offers and availability ("2 spots left on Saturday's nightlife route")

### 30 Facebook content ideas

| # | Topic | Format | Hook / caption | CTA | Audience |
|---|---|---|---|---|---|
| 1 | Truck lights up in Deep Ellum | Photo post | "This is what 9 pm Saturday in Deep Ellum looks like for our clients 👀" | Message "ROUTE" for availability | Bars, restaurants |
| 2 | How a shared route works | Carousel | "How 5 local businesses share one LED truck (and the cost)" | Link → pricing page | SMBs |
| 3 | Day in the life of a MOD driver | Photo post | "6 hours, 3 cities, 1 truck" | Follow for routes | General |
| 4 | Client spotlight: Atlas Bail Bonds (with permission) | Testimonial graphic (quote + photo) | "A year on the road with Atlas Bail Bonds" | Get a quote | Legal/services |
| 5 | Cowboys game-day route | Photo post | "Game day. One LED truck. Here's where we drove." | Book event route | Bars, local brands |
| 6 | Design before/after | Carousel | "Your flyer vs. your flyer on a 12-ft LED screen" (verify the size) | Free design consult | SMBs |
| 7 | Price myth-buster | Text + photo post | "No, a billboard truck doesn't cost $10K a day. Here's real pricing." | Link → pricing page | SMBs |
| 8 | Frisco billboard rules | Photo post | "Frisco limits roadside billboards. Here's how Frisco brands still get seen." | Message "FRISCO" | Frisco businesses |
| 9 | Route of the week map | Photo post + Story | "This week's route: Legacy West → The Star → Frisco Square" | Message to book | Local SMBs |
| 10 | Spots-left alert | Story | "2 spots left on Saturday's nightlife route" | Tap to message | Bars |
| 11 | 3 mistakes in billboard ads | Photo post | "Stop putting your whole menu on a billboard" | Save + follow | All |
| 12 | Grand opening plan | Carousel | "30-day grand opening plan for Dallas businesses" | Get a quote | New businesses |
| 13 | Night vs day visibility | Side-by-side photo | "Same ad. Noon vs midnight." | Comment "NIGHT" | All |
| 14 | Client reaction | Photo post | "We drove a client's ad past their store. Here's their reaction." | Book yours | SMBs |
| 15 | QR code in action | Photo post | "Someone scanned this from a red light. Here's what happened." (real data only) | Get a quote | Marketers |
| 16 | Real estate open house | Photo post | "Open house this Sunday? Make the whole neighborhood know." | Real estate page | Agents |
| 17 | Holiday campaign (home services) | Testimonial graphic | "Christmas-light company: 'my phone was ringing off the hook'" (client's own words) | Book Q4 now | Home services |
| 18 | Behind the screen tech | Carousel | "What's inside a mobile LED billboard?" | Follow | General |
| 19 | State Fair route preview | Photo post | "Fair Park crowds start in 30 days. Your ad could be there." | Book event | Local brands |
| 20 | Recruiting campaign | Photo post | "Hiring drivers? Put the job on wheels." | Exclusive rental page | Employers |
| 21 | Ask MOD Anything | Q&A text post | "Ask us anything about mobile billboards" | Comment or message | All |
| 22 | Owner story | Text + photo post | "Why our family started a billboard truck company in 2022" | Follow | All (trust) |
| 23 | Shared vs exclusive | Carousel | "Shared route or your own truck? Here's how to choose." | Get a quote | SMBs, marketers |
| 24 | Rockwall local love | Photo + community post | "Proud to drive Rockwall County every week. Shout-out to our local clients." | Tag a local business | Rockwall SMBs |
| 25 | Concert night | Photo post | "Outside American Airlines Center before the show" | Event route | Promoters |
| 26 | Impressions explained | Text + graphic post | "How mobile billboard impressions are actually measured" | Read the article | Marketing managers |
| 27 | Client ad countdown | Story sequence | "Your ad goes live in 3…2…1" | Book | SMBs |
| 28 | Political season | Photo post (compliant) | "Campaign season: reach every precinct you need" | Political page | Campaigns |
| 29 | Monthly highlights | Photo album | "Every ad we ran in [Month]" | Get on next month's highlights | All |
| 30 | Offer post | Designed graphic | "New clients: free ad design on your first route" (if offered) | Claim offer (Lead Ad) | SMBs |

### Facebook post guidelines
- **Cadence:** 3–4 posts per week (up to 15 per month), plus photo Stories on route nights.
- **Mix:** about 40% truck and route photos, 20% client spotlights and testimonials, 20% tips and education (carousels or designed graphics), 20% offers and availability.
- **Photo rules:** shoot the truck with the screen lit and a recognisable DFW landmark in frame, get the client's ad on screen (with permission), and avoid team logos or anything that implies an official sponsorship.
- **Design:** use one consistent Canva template (MOD Media colours, logo and font) so posts are recognisable in the feed. Keep text on images short.
- **Captions:** open with the hook in the first line, keep it to 2–4 short lines, and end with one call to action (message us, tap Get Quote, or visit the pricing page).
- **Opening lines that stop the scroll:**
  - "This is what 9 pm Saturday in Deep Ellum looks like for our clients 👀"
  - "This truck is a billboard."
  - "Frisco limits billboards. So we built one on wheels."
  - "What $___ in advertising looks like in Dallas" (real price)
  - "Your competitor's customers are at this game tonight."
  - "2 spots left on Saturday's nightlife route."

### 10 sample Facebook posts

1. **Route night photo:** truck lit up on Elm St. Caption: "Your ad, where the weekend crowd actually is. Fri & Sat, 6–11 pm, Deep Ellum + Uptown. 🚚✨ Message us 'ROUTE' for this week's openings."
2. **Price myth carousel:** slide 1 "Does a billboard truck cost $10K a day?", slides 2–4 how shared routes work, slide 5 "Shared routes from $__/week". Caption: "Real pricing, no games. Tap Get Quote."
3. **Frisco post:** truck at Legacy West. Caption: "Frisco limits roadside billboards, so we bring the billboard to you. Every Monday and Wednesday. Book the Frisco route."
4. **Game day photo:** truck on a public road near the stadium with a sports-bar special on screen. Caption: "Your bar's specials in front of every fan heading home. Book the next home game."
5. **Before/after graphic:** a flyer next to the same design on the LED screen. Caption: "Glow-up. 💡 Send us your flyer in Messenger and we'll show you how it looks on the truck."
6. **Client spotlight:** photo of the client's ad on the truck + quote from their review. Caption: "A year on the road with Atlas Bail Bonds (with permission). Want to be next? Tap Get Quote."
7. **Route of the Week graphic:** map of this week's stops. Caption: "This week's route: Legacy West → The Star → Frisco Square. 2 spots left."
8. **Design tips carousel:** "3 billboard ad mistakes": too many words, low contrast, tiny QR code. Caption: "Save this before your next campaign. Free design review in Messenger."
9. **Grand opening post:** truck parked outside a real client's opening (only if real). Caption: "Opening a business in Dallas? Make day one loud. Request a custom route."
10. **Owner Q&A post:** photo of Jamie with the truck. Caption: "Do billboard trucks actually work? Ask us anything in the comments and we'll give you an honest answer."

### Facebook advertising (optional add-on)

| Order | Campaign | Objective | Audience | Creative | Indicative budget |
|---|---|---|---|---|---|
| 1 | **Retargeting** | Leads (website conversions) | Website visitors 30 days (Pixel), Page engagers 60 days | Testimonial graphics, "spots left this week", pricing carousel | $10–$20/day |
| 2 | **Lead generation, DFW businesses** | Leads (Instant Form with 3 qualifying questions; or website leads once the Conversions API is live) | 25-mi radius around Dallas + Frisco/Plano + Rockwall; interests such as small business owners, Facebook Page admins, restaurants, real estate | Truck photos + an offer ("Free route plan") | $20–$40/day |
| 3 | **Event and seasonal pushes** | Leads | Location + interests (event promotion, nightlife businesses) 30 days before key events (State Fair, holiday season, election season) | Event-route photos | Burst budgets of $300–$800 per push |

**Notes:**
- **Placements:** run the ads on Facebook placements (Feed, Stories, Marketplace) to keep the focus on Facebook.
- **Special ad category:** political advertisers must complete Meta's "Social issues, elections or politics" authorisation. Promoting MOD's political billboard service may also trigger it, so review Meta policy first.
- **Creative testing:** 3 hooks × 2 offers each month. Keep the winners by **cost per qualified lead**, not cost per lead.
- **Assumptions:** local B2B lead costs on Facebook vary widely. Plan for a 4–6 week learning period before judging results. These are budget ranges, not performance promises.

## 16. Phase 10 — Paid search (optional later add-on)

The current plan focuses on the website, Google Business Profile and Facebook. Once the website pages and tracking are fixed, Google Search Ads can be added later as an optional channel to capture people already searching for "mobile billboard Dallas" or "LED billboard truck rental". The new pricing, service and city pages built in this plan would serve as their landing pages.

## 17. Phase 11 — Schema and AI search visibility

### Recommended schema (WordPress implementation)
Use **Yoast Local SEO** (paid add-on) or a custom JSON-LD snippet via WPCode, injected per page. Don't stack multiple schema plugins.

**Site-wide (on the homepage, referenced elsewhere by `@id`):**
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "ProfessionalService",
      "@id": "https://modmediadfw.com/#organization",
      "name": "MOD Media",
      "alternateName": ["MOD Media DFW", "MOD Media Ads"],
      "url": "https://modmediadfw.com/",
      "logo": "https://modmediadfw.com/wp-content/uploads/2025/02/image-32.png",
      "image": "https://modmediadfw.com/wp-content/uploads/2025/03/truck1-2880w.webp",
      "description": "Family-owned mobile billboard company operating LED billboard trucks on scheduled routes and exclusive rentals across Dallas–Fort Worth, with exclusive rentals in Austin, Houston and San Antonio.",
      "telephone": "+1-469-279-2511",
      "email": "info@modmediaads.com",
      "foundingDate": "2022",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "181 County Line Road",
        "addressLocality": "Rockwall",
        "addressRegion": "TX",
        "postalCode": "75032",
        "addressCountry": "US"
      },
      "areaServed": [
        {"@type": "City", "name": "Dallas"},
        {"@type": "City", "name": "Frisco"},
        {"@type": "City", "name": "Plano"},
        {"@type": "City", "name": "Rockwall"},
        {"@type": "City", "name": "Rowlett"},
        {"@type": "City", "name": "Austin"},
        {"@type": "City", "name": "Houston"},
        {"@type": "City", "name": "San Antonio"}
      ],
      "sameAs": [
        "https://www.facebook.com/profile.php?id=100088542497714",
        "<<Google Maps CID URL>>"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://modmediadfw.com/#website",
      "url": "https://modmediadfw.com/",
      "name": "MOD Media",
      "publisher": {"@id": "https://modmediadfw.com/#organization"}
    }
  ]
}
```
*Notes:*
- `ProfessionalService` is a LocalBusiness subtype. There's no "AdvertisingAgency" type in schema.org.
- Omit `address` (keep `areaServed`) if the GBP hides the address as a service-area business.
- **Confirm the NAP first.**
- Don't add `aggregateRating` from on-site testimonials.

**Each service page: Service schema:**
```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Dallas Nightlife Mobile Billboard Route",
  "serviceType": "Mobile billboard advertising",
  "provider": {"@id": "https://modmediadfw.com/#organization"},
  "areaServed": {"@type": "City", "name": "Dallas"},
  "description": "LED billboard truck route through Deep Ellum and Uptown every Friday and Saturday, 6–11 pm.",
  "url": "https://modmediadfw.com/dallas-nightlife-route/"
}
```

**Other schema:**
- **BreadcrumbList:** keep Yoast's, and enable visible breadcrumbs (Yoast + Astra) on inner pages.
- **VideoObject:** on pages with the truck video. Include `name`, `description`, `thumbnailUrl`, `uploadDate`, `contentUrl` and `duration`.
- **Article/BlogPosting:** automatic via Yoast on blog posts. Add the author as a real person with an author page.
- **FAQPage:** fine to include where real FAQs are visible on the page. Since 2023, Google shows FAQ rich results only for authoritative government and health sites, so **expect no rich-result stars or dropdowns.** The markup still helps machines (including AI systems) understand the Q&A.
- **Review/AggregateRating:** not eligible for self-serving LocalBusiness or Organization review snippets. Show real Google reviews through an embedded widget instead (no markup).

### AI search visibility (Google AI Overviews, ChatGPT search, Copilot, Perplexity)

What realistically helps. We can't promise inclusion.
1. **Entity consistency:** one name ("MOD Media"), one NAP, and the same description everywhere (site, GBP, Facebook, Bing Places, Apple, chambers, directories). AI systems cross-check sources.
2. **Bing Places + Bing Webmaster Tools:** ChatGPT search and Copilot rely heavily on Bing's index. Submit the sitemap to Bing and enable IndexNow (Yoast or the LiteSpeed plugin supports it).
3. **Answer-ready content:** clear, factual statements that AI can quote. For example: "MOD Media's Dallas nightlife route runs Friday and Saturday from 6 to 11 pm through Deep Ellum and Uptown." Add pricing ranges, specs and schedules in plain HTML text (not inside images or sliders).
4. **FAQ sections** on every service and city page, written as natural questions.
5. **Third-party mentions:** local press, chamber directories, OOH industry directories, event partner pages and client "thank you" posts. AI answers lean on sources other than the business's own site.
6. **Reviews on GBP and other platforms** with descriptive text (route, event, results).
7. **Original data:** e.g. publish anonymised "average QR scans per nightlife route" once real data exists. Unique data earns citations.
8. **Crawlability:** don't block AI crawlers (GPTBot, PerplexityBot, Google-Extended) in robots.txt unless the client chooses to. Currently nothing is blocked.

## 18. Phase 12 — Backlinks and authority

**Current footprint:** no third-party mentions, press or directory citations surfaced in brand searches. A full backlink audit (including removal of any spam links) is part of month 1.

**20+ relevant prospects:**

| # | Prospect / category | Example targets | Relevance | Approach |
|---|---|---|---|---|
| 1 | Rockwall Area Chamber of Commerce | rockwallchamber.org | Home-market business association | Membership listing + sponsor events |
| 2 | Rowlett Chamber | rowlettchamber.com | Service area | Membership |
| 3 | Frisco Chamber | friscochamber.com | Frisco route | Membership + event truck presence |
| 4 | Plano Chamber | planochamber.org | North Dallas | Membership |
| 5 | Dallas Regional Chamber / Greater Dallas Hispanic Chamber | dallaschamber.org, gdhcc.com | Dallas | Membership if budget allows |
| 6 | Deep Ellum Foundation / Uptown Dallas Inc. | deepellumtexas.com, uptowndallas.net | Nightlife route districts | Sponsorship of district events → partner page link |
| 7 | Local event organisers | Rockwall Founders Day, Frisco festivals, Dallas food and music festivals | Event routes | In-kind truck sponsorship in exchange for a sponsor listing |
| 8 | Charity and nonprofit partnerships | Local food banks, animal shelters, youth sports | Community | Donate screen time (PSA) → press + partner link |
| 9 | Local news | Rockwall Herald-Banner, Community Impact (Frisco/Plano/Rockwall editions), Dallas Innovates, Dallas Business Journal | Local press | Pitch: "Family business brings billboards to Frisco, where roadside billboards are limited" |
| 10 | Texas business publications | D CEO, Texas Monthly business section | Regional | Founder story, data stories |
| 11 | OOH industry | OAAA member directory, Billboard Insider, OOH Today ("Company of the Day" features) | Industry authority | Membership / feature submission |
| 12 | OOH marketplaces | AdQuick, outdoorbillboard.com, Blip (if applicable) | Industry + leads | List inventory (also a lead source) |
| 13 | Client case-study links | Atlas Bail Bonds, the holiday-lights company, other clients | Customer | Ask clients to post "As seen on MOD Media's truck" with a link |
| 14 | Agencies and marketing partners | DFW marketing agencies, event planners | B2B referral | Partner program with a "preferred vendor" listing |
| 15 | Venue-adjacent businesses | Sports bars, hotels near AT&T Stadium and AAC | Event | Co-marketing |
| 16 | Real estate associations | MetroTex Association of Realtors, Collin County AOR | Real estate vertical | Affiliate/sponsor listings |
| 17 | University and college | SMU, UTD, UNT career fairs and event sponsorship | Recruiting campaigns | Sponsor listing |
| 18 | Podcasts and local business shows | DFW small business podcasts | Founder authority | Guest appearances |
| 19 | HARO-style journalist requests | Qwoted, Featured, Source of Sources | Expert quotes on advertising | Weekly responses |
| 20 | Local directories (quality only) | BBB, Yelp, Nextdoor, Apple Business Connect, Bing Places, Manta | Citations | Consistent NAP |
| 21 | Supplier/manufacturer | The LED truck manufacturer's "customer showcase" page | Industry | Ask for a feature |
| 22 | City and visitor bureaus | Visit Frisco, Visit Rockwall vendor/partner lists | Local tourism | Partner listing where offered |

**Avoid:** paid link packages, PBNs, mass directory submissions, irrelevant guest posts, link exchanges, and "Featured in" badges from pay-to-play sites.

## 19. Phase 13 — Analytics and lead tracking

**Current state [Verified from source]:** no GA4 (`gtag`/`G-`), no GTM (`GTM-`), no Meta Pixel (`fbq`), and no call-tracking scripts were found. Leads today arrive by phone and email without attribution, so nobody can say which channel produces them.

**Setup (WordPress):**
1. **Google Tag Manager:** install via the GTM4WP plugin or Site Kit. One container.
2. **GA4:** through GTM. Enable Enhanced Measurement. Link to Search Console.
3. **Search Console:** a domain property (DNS TXT). Submit `sitemap_index.xml`. Verify **Bing Webmaster Tools** too (import from GSC).
4. **Conversion events (GA4 key events):**

| # | Event | Trigger (GTM) | Key event? |
|---|---|---|---|
| 1 | `generate_lead` (quote form submit) | Elementor form success (a `submit_success` jQuery listener or the Elementor Pro dataLayer push), or a thank-you page `/thank-you/` | ✅ |
| 2 | `click_to_call` | Link click URL starts with `tel:` | ✅ |
| 3 | `phone_call` (actual call) | Call tracking (CallRail, WhatConverts or the Google forwarding number) | ✅ |
| 4 | `email_click` | Link URL starts with `mailto:` | Secondary |
| 5 | `sms_click` | Link URL starts with `sms:` | ✅ |
| 6 | `booking_inquiry` | Form field "Service" = Exclusive or Event, or a budget of $1,500+ | ✅ (qualified) |
| 7 | `scroll_pricing` / `view_pricing` | Pricing page view | Micro |
| 8 | `video_play` | Truck video play | Micro |

5. **Call tracking:** dynamic number insertion (e.g. CallRail, from about $50/month) shows a different number per source (organic search, GBP, Facebook), while the GBP primary number stays consistent or the main number is listed as additional. Record calls only with the disclosures Texas law and the provider's terms require (Texas is a one-party consent state; confirm with counsel for interstate calls).
6. **Meta Pixel + Conversions API:** via the official Meta plugin or GTM server-side. Events: PageView, ViewContent (service pages), Lead (form success), Contact (call/SMS click).
7. **UTMs:** on GBP website and appointment links, the Facebook Page button and every Facebook post link, email signatures, and **QR codes on the trucks' own house ads** (e.g. `?utm_source=truck&utm_medium=qr`).
8. **CRM / lead sheet:** at minimum a Google Sheet or HubSpot Free with Date · Source (form/call/SMS) · Channel (GA4 or call tracking) · Service · City · Budget · Qualified (Y/N) · Booked (Y/N) · Revenue. Capture GCLID/fbclid in hidden form fields for offline conversion uploads.

**Identifying qualified leads by channel:** Qualified = in the service area + a budget above the minimum + a date within 90 days. Report **cost per qualified lead** and **booked revenue per channel** monthly.

**Dashboard (Looker Studio, free):**
- **Page 1, Overview:** leads by channel (form, call, SMS), qualified %, booked campaigns, revenue (from the CRM sheet).
- **Page 2, SEO:** GSC clicks, impressions and avg. position for priority keywords; top landing pages; new pages indexed.
- **Page 3, Local:** GBP calls, website clicks, direction requests, searches (via the GBP Performance export), reviews count and rating trend.
- **Page 4, Facebook ads:** spend, reach, cost per lead, cost per qualified lead.
- **Page 5, Facebook Page:** reach, followers, engagement, link clicks, messages.

## 20. Phase 14 — Prioritised 90-day action plan

### First 7 days: critical fixes

| Task | Priority | Est. time | Difficulty | Expected impact | Dependencies |
|---|---|---|---|---|---|
| Replace the Lorem Ipsum blocks on 4 service pages | Critical | 1–2 h | Easy | High (trust) | Copy (provided above) |
| Fix `tel:123 444 678` → `tel:+14692792511`; standardise all tel links; fix the `mailto:` | Critical | 1 h | Easy | High (calls) | — |
| Delete the hello-world post and spam comments; disable comments | High | 30 min | Easy | Medium (risk) | — |
| Disable the author archive; noindex the category archive; change the admin display name; enforce a strong password + 2FA | High | 30 min | Easy | Security | — |
| Install GTM, GA4, Search Console (+ Bing), Meta Pixel; set up the key events | Critical | 4–6 h | Medium | High (measurement) | — |
| Set up call tracking | High | 2 h | Easy | High | Budget approval |
| Claim/verify GBP; check the pin, address, name and categories | Critical | 2 h | Easy | High (local) | Confirmation of the real base |
| Add H1s to all 18 pages (change the first heading widget) | High | 2 h | Easy | Medium | — |
| Link the footer Facebook icon; remove unused social icons; fix the Yoast site name | Medium | 30 min | Easy | Low | Facebook Page URL |
| Move the analytics PDF onto the site | Medium | 30 min | Easy | Low | PDF file |

### Days 8–30: foundation

| Task | Priority | Est. time | Difficulty | Expected impact | Dependencies |
|---|---|---|---|---|---|
| Rewrite titles and meta descriptions (Section 13) | High | 3 h | Easy | Medium | Keyword map |
| Merge the nightlife pages + 301; rename the Dallas Day Routes slug + 301; update the menu | High | 2 h | Easy | Medium | — |
| Rebuild the quote form (2-step, more fields) + thank-you page + tracking | Critical | 4–6 h | Medium | High | GTM |
| Homepage rebuild to the wireframe | High | 12–20 h | Medium | High | Photos, video, prices |
| Build the pricing page | Critical | 6–8 h | Medium | High | Client pricing approval |
| Rewrite the 4 service pages (unique content, FAQ, CTA) | High | 12–16 h | Medium | High | Route details |
| Rewrite the city pages (remove boilerplate; unique sections) | High | 10–14 h | Medium | Medium–High | Route and venue facts |
| Compress the videos and images; WebP; caching; remove unused plugins | High | 4–8 h | Medium | Medium–High (mobile UX) | Developer, staging |
| Add LocalBusiness, Service and VideoObject schema | Medium | 3 h | Medium | Medium | Final NAP |
| Optimise GBP fully (checklist) + first 20 photos | Critical | 4 h | Easy | High | Photos |
| Start the review program | High | 2 h set-up | Easy | High | Client list |
| NAP citations (top 10) | Medium | 4 h | Easy | Medium | Final NAP |
| Facebook Page optimisation (name, description, Get Quote button, auto-replies) + Meta Pixel | High | 3 h | Easy | Medium | Page access |
| Collect the first 30 truck and campaign photos; build the Canva post template | High | 4 h | Easy | Medium | Client photos |

### Days 31–60: growth

| Task | Priority | Est. time | Difficulty | Expected impact | Dependencies |
|---|---|---|---|---|---|
| Publish priority articles #1, #2, #3, #10 | High | 4–6 h each | Medium | Medium | Keyword data |
| Build industry pages (Restaurants & Bars, Grand Openings) | High | 6 h each | Medium | Medium–High | Examples/photos |
| Build event pages (AT&T Stadium game days; State Fair, for 2027 season) | Medium | 6 h each | Medium | Medium | Event calendar |
| 3 case studies with client permission | High | 4 h each | Medium | High (trust, AI) | Client approval, data |
| Chamber memberships + local PR pitch | Medium | 6 h | Medium | Medium | Budget |
| Facebook retargeting + lead campaigns | High | 4 h | Medium | Medium–High | Pixel, creative |
| Weekly Facebook posting (3–4/wk, up to 15/month) | High | Ongoing | Easy | Medium | Photos |
| Competitor gap pages (Rockwall terms, Frisco hotspot terms) | Medium | 4 h | Easy | Medium | — |
| Facebook ads: audience and creative tests | High | 2 h/wk | Medium | High | Data |

### Days 61–90: expansion

| Task | Priority | Est. time | Difficulty | Expected impact | Dependencies |
|---|---|---|---|---|---|
| Expand pages gaining impressions (from GSC data) | High | 6–10 h | Medium | Medium–High | 60 days of GSC data |
| Improve underperforming pages (titles/CTR, content) | Medium | 4–6 h | Medium | Medium | GSC |
| Fort Worth page (only if operationally true) | Medium | 6 h | Medium | Medium | Confirmed routes |
| Backlink outreach (sponsorships, partners, client links) | Medium | 8 h/mo | Medium | Medium | Case studies |
| Expand Facebook retargeting (lookalike audiences of past leads) | Medium | 3 h | Medium | Medium | Audiences built |
| Facebook ads optimisation: scale winning ads, import booked customers as an audience | High | 4 h | Medium | High | 30+ leads, CRM |
| 90-day performance report + next-quarter plan | High | 6 h | Easy | High (decisions) | Dashboard |

---

## 21. The three critical questions

**1. Why is MOD Media struggling to generate leads and rank on Google?**
- The key commercial pages look unfinished (Lorem Ipsum, a dead phone link).
- No page has an H1, the titles don't match buyer searches, and the city pages repeat copy for the wrong cities.
- There's no pricing information, no FAQ and a weak quote form, so visitors who do arrive have little reason or opportunity to enquire.
- Brand and location signals are inconsistent, which holds back Maps visibility.
- The site is heavy on mobile.
- There's no tracking, so nobody can see or improve what's happening.

**2. What specific changes give the best chance of improving visibility and attracting qualified customers?**
Fix the trust breakers and tracking in week one. Rebuild the homepage and four service pages around buyer keywords with real proof. Publish a pricing page. Merge or rewrite the duplicate and city pages. Fully optimise GBP and collect steady genuine reviews. Add LocalBusiness and Service schema. Compress the media.

**3. How do the website, GBP and Facebook work together?**
- **Google Business Profile** captures people already searching on Google Maps, starting now.
- **Website SEO** builds visibility for buyer searches over months, and gives every visitor a clear way to request a quote.
- **Facebook posts** make MOD Media familiar to local business owners and supply proof for the website and ads.
- **Optional Google or Meta ads** can generate enquiries faster while SEO builds, and retargeting brings back website visitors who didn't enquire the first time.
- **Every finished campaign** produces a review, a case study and new content, which feeds the loop again.

## 22. The 10 highest-priority actions (ranked by impact and urgency)

1. **Remove the Lorem Ipsum and fix the broken `tel:123 444 678` phone link** on the Daily Route, Nightlife, Exclusive Rental and Event Routes pages. *(Day 1)*
2. **Install tracking:** GTM + GA4 + Search Console + call tracking + key events for forms, calls and SMS. *(Week 1)*
3. **Claim and fully optimise Google Business Profile:** confirm the pin and address, service-area setup, correct categories, services, photos, weekly posts. *(Week 1–3)*
4. **Rebuild the quote form** (2-step: service, city, date, phone, budget) and add a sticky mobile Call · Text · Quote bar. *(Week 2)*
5. **Add keyword-led H1s, titles and meta descriptions** to every page, and set the site name to "MOD Media". *(Week 1–2)*
6. **Publish a Mobile Billboard Pricing page** with honest "starting at" ranges, and fill the empty pricing section. *(Week 2–4)*
7. **Rebuild the homepage and the four core service pages** with real truck photos and video, route schedules, how-it-works, FAQs and proof. Merge the duplicate nightlife pages. *(Week 2–5)*
8. **Optional: launch Facebook lead and retargeting ads** (DFW business owners, "Free Route Plan" offer) once the Meta Pixel and landing pages are fixed. *(Week 3–4)*
9. **Clean up the site:** delete the spam hello-world post, disable the author and category archives, compress the 21 MB video and 1 MB PNGs, and rewrite the city pages to remove wrong-city boilerplate. *(Week 1–6)*
10. **Start the review and content engine:** review requests after every campaign, 3–4 Facebook posts a week (up to 15 a month), and one case study a month, amplified with Facebook retargeting. *(Week 3 onward)*

---

### Sources (external research)

- AdQuick, mobile billboard pricing benchmarks: https://www.adquick.com/mobile-billboard-advertising · https://www.adquick.com/media/dooh/advertising-truck
- Texas Mobile Advertising: https://www.texasmobileadvertising.com/ · https://www.texasmobileadvertising.com/service-areas/dallas/
- Bulldog Billboards: https://bulldogbillboards.com/ · https://bulldogbillboards.com/locations/truck-advertising-in-dallas/ · DesignRush profile: https://www.designrush.com/agency/profile/bulldog-mobile-billboards
- Mobile Billboard Global (Texas): https://www.mobilebillboardglobal.com/mobile-billboard-texas
- LED Truck Media (Dallas): https://ledtruckmedia.com/us-markets/region/southeast/city/dallas/
- Lime Media (Dallas): https://lime-media.com/locations/led-billboard-truck-dallas/
- Big Wave Display: https://bigwavedisplay.com/
- Rolling Adz: https://rollingadz.com/
- American Mobile Ads (Texas): https://americanmobileads.com/us/texas
- Cowtown Command listing: https://www.outdoorbillboard.com/billboards/6971518-cowtown-command-for-rent-in-fort-worth-tx
- Premier Mobile Billboards (Dallas): https://premiermobilebillboards.com/dallas/
- Dash Two, Dallas static billboard cost context: https://dashtwo.com/outdoor-advertising/billboards-advertising/dallas/
- Frisco political sign page (references Sign Ordinance Section 70-18): https://www.friscotexas.gov/1871/Political-Campaign-Signs
- Google guidelines to verify against when implementing: Google Business Profile guidelines (https://support.google.com/business/answer/3038177), structured data review-snippet rules (https://developers.google.com/search/docs/appearance/structured-data/review-snippet), FAQ rich result changes (https://developers.google.com/search/blog/2023/08/howto-faq-changes)

*Evidence files (crawl extract and Lighthouse summaries) are in `/evidence` in this repository.*
