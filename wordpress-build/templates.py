"""Reusable Elementor templates (campaign page, city page, blog post) built from the homepage's own blocks."""
import copy, json
import build2 as B  # builds HOME/HEADER/FOOTER and exposes the helpers
from build2 import (H, Wd, con, row, grid, section, sec_head, eyebrow, h2, lede, button, custom_type,
                    px, CU, box, gap, img, LINE, C, nid, step, svc)

def fresh(el):
    """Deep copy with new element ids, so a block can be reused on another page."""
    e = copy.deepcopy(el)
    def walk(x):
        x["id"] = nid()
        for c in x.get("elements", []): walk(c)
    walk(e); return e

STRIP, REVIEWS, QUOTE = B.HOME[1], B.HOME[9], B.HOME[13]
PH = "#9AA6C2"  # placeholder text reads as muted

def hero(eb, title, sub, image_key):
    left = con([
        eyebrow(eb, mb=22),
        H(title, 'h1', 'hero_h1', 'text', _element_width='initial', _element_custom_width=px(620)),
        H(sub, 'p', None, '#C8D1E6', mt=24, **custom_type('Inter', 400, 19, 1.65), _element_width='initial', _element_custom_width=CU('60ch')),
        row([button("Get Campaign Pricing →", "#quote"), button("Call or Text (469) 279-2511", "tel:+14692792511", 'ghost')],
            g=14, wrap=True, margin=box(34, 0, 0, 0)),
    ])
    pic = Wd("image", image=img(image_key), image_size="large", css_classes="mm-gfig", height=px(420), height_mobile=px(260),
             _border_border="solid", _border_width=box(1), _border_color=LINE, _border_radius=box(20), _title="Hero photo")
    return con([left, pic], content_width="boxed", _title="Hero", css_classes="mm-hero", container_type="grid",
               grid_columns_grid=CU("1.05fr .95fr"), grid_columns_grid_tablet=CU("1fr"), grid_columns_grid_mobile=CU("1fr"),
               grid_rows_grid={"unit": "fr", "size": 1, "sizes": []}, grid_gaps=gap(56), grid_align_items="center",
               padding=box(90, 20, 70, 20), padding_mobile=box(76, 20, 64, 20), overflow="hidden",
               background_background="classic", background_color="#06080F")

def chips(items):
    return Wd("icon-list", view="inline", css_classes="mm-inds",
              icon_list=[{"_id": nid(), "text": t, "selected_icon": {"value": "fas fa-circle", "library": "fa-solid"}} for t in items],
              icon_size=px(9), text_indent=px(8), icon_color="#2EE6F0", text_color="#EEF2FB", space_between=px(0),
              **custom_type('Inter', 600, 15, 1.65, pre='icon_typography'))

def faq(qs):
    return Wd("accordion", tabs=[{"_id": nid(), "tab_title": q, "tab_content": f"<p>{a}</p>"} for q, a in qs], css_classes="mm-faq",
              selected_icon={"value": "fas fa-plus", "library": "fa-solid"}, selected_active_icon={"value": "fas fa-times", "library": "fa-solid"},
              icon_align="right", title_html_tag="div", faq_schema="yes", border_width=px(0),
              title_color="#EEF2FB", tab_active_color="#EEF2FB", icon_color="#2EE6F0", icon_active_color="#2EE6F0", content_color="#9AA6C2",
              **custom_type('Inter', 700, 17, 1.65, pre='title_typography'), **custom_type('Inter', 400, 16, 1.65, pre='content_typography'),
              _element_width="initial", _element_custom_width=px(880))

def text_block(paras):
    return Wd("text-editor", editor="".join(f"<p>{p}</p>" for p in paras), text_color="#C8D1E6",
              **custom_type('Inter', 400, 17, 1.75), css_classes="mm-prose")

def photo_row(keys):
    return row([Wd("image", image=img(k), image_size="large", css_classes="mm-gfig", link_to="file", open_lightbox="yes",
                   _element_width="initial", _element_custom_width=CU("calc((100% - 28px) / 3)"), _element_width_mobile="initial",
                   _element_custom_width_mobile=CU("100%"), _flex_size="none", height=px(260), height_mobile=px(220),
                   _border_border="solid", _border_width=box(1), _border_color=LINE, _border_radius=box(16)) for k in keys],
               g=14, align='stretch', flex_direction_mobile="column")

def link_card(tag, title, body, url, cta):
    c = svc(tag, title, body, "see page", cta)
    c["elements"].pop(3)                       # no "Best for" line on link cards
    c["elements"][-1]["settings"]["link"] = {"url": url, "is_external": "", "nofollow": ""}
    return c

# ---------------- shared building blocks for long-form pages ----------------
BRANDWALL = B.HOME[3]

def crumbs():
    return Wd("shortcode", shortcode="[rank_math_breadcrumb]", css_classes="mm-crumbs", _title="Breadcrumbs")

def info_card(title, body, tag=None):
    kids = ([H(tag, 'div', 'tag', 'primary')] if tag else []) + [H(title, 'h3', 'card_h3', 'text'), H(body, 'p', 'card_p', 'muted')]
    return con(kids, css_classes="mm-svc", padding=box(28, 26), flex_gap=gap(12), background_background="gradient",
               background_color="#0F1529", background_color_b="#0A0F1E", background_gradient_angle=px(180, 'deg'),
               border_border="solid", border_width=box(1), border_color=LINE, border_radius=box(18))

def glance(title, facts):
    return con([H(title, 'h3', 'card_h3', 'text', mb=10),
                Wd("icon-list", icon_list=[{"_id": nid(), "text": f"<strong>{a}</strong> {b}", "selected_icon": {"value": "fas fa-check-circle", "library": "fa-solid"}} for a, b in facts],
                   icon_color="#2EE6F0", text_color="#C8D1E6", icon_size=px(15), text_indent=px(10), space_between=px(14),
                   **custom_type('Inter', 400, 15, 1.6, pre='icon_typography'))],
               padding=box(30), border_border="solid", border_width=box(1), border_color="#2EE6F059", border_radius=box(22),
               background_background="gradient", background_color="#0F2B3A", background_color_b="#121A33", background_gradient_angle=px(135, 'deg'))

def two_col(left, right, cols="1.15fr .85fr"):
    return con([left, right], container_type="grid", grid_columns_grid=CU(cols), grid_columns_grid_tablet=CU("1fr"),
               grid_columns_grid_mobile=CU("1fr"), grid_rows_grid={"unit": "fr", "size": 1, "sizes": []}, grid_gaps=gap(56),
               grid_align_items="start")

def link_chips(items):
    return Wd("icon-list", view="inline", css_classes="mm-inds",
              icon_list=[{"_id": nid(), "text": t, "link": {"url": u, "is_external": "", "nofollow": ""},
                          "selected_icon": {"value": "fas fa-arrow-right", "library": "fa-solid"}} for t, u in items],
              icon_size=px(11), text_indent=px(8), icon_color="#2EE6F0", text_color="#EEF2FB", space_between=px(0),
              **custom_type('Inter', 600, 15, 1.65, pre='icon_typography'))

COMPARE = ("<table><thead><tr><th></th><th><a href='/campaigns/daily/'>Daily</a></th><th><a href='/campaigns/weekly/'>Weekly</a></th>"
           "<th><a href='/campaigns/monthly/'>Monthly</a></th></tr></thead><tbody>"
           "<tr><td>Best for</td><td>Launches, grand openings, events, game days</td><td>Promotions, sales, openings, recruiting</td><td>Brand awareness, political campaigns, market entry</td></tr>"
           "<tr><td>Length</td><td>One day</td><td>A full week</td><td>A month or longer</td></tr>"
           "<tr><td>What it delivers</td><td>One high-impact day, timed to your event</td><td>Repeat exposure, so the message sticks</td><td>A steady presence that builds recognition</td></tr>"
           "<tr><td>Cost per day</td><td>Highest</td><td>Lower</td><td>Lowest</td></tr>"
           "<tr><td>Dedicated truck, your ads only</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></tbody></table>")

BENEFITS = [
    ("100% share of voice", "Your truck shows only your ads. No rotating slot with other advertisers, unlike most digital billboards."),
    ("It goes to your audience", "Roadside billboards wait for traffic. A truck drives to the districts, events and neighborhoods where your customers are."),
    ("Bright day and night", "High-resolution LED screens stay readable in daylight and stand out after dark."),
    ("Change your ad any time", "Run video, animation or static ads, rotate several, or update the message during the campaign."),
    ("Planned around your timing", "Rush hour, lunch, game time or late night: the truck runs when your audience is out."),
    ("Easy to measure", "Add a QR code, short web address or promo code and you can count every response."),
]
DESIGN_TIPS = [
    ("Keep it under 7 words", "People see a moving truck for a few seconds. One short headline beats a paragraph."),
    ("Use strong contrast", "Light text on a dark background, or the reverse, reads from across the street."),
    ("One clear next step", "A phone number, a short web address or a QR code. Pick one and make it big."),
    ("Show the brand early", "Put your logo where it's seen first, so even a glance builds recognition."),
]
TRACKING = ["Campaign photos and a report showing where and when your ad ran.",
            "A QR code or short web address on the ad, so visits can be counted.",
            "A promo code or dedicated phone number for responses.",
            "Watch branded Google searches and website visits during the campaign."]
CITY_LINKS = [("Dallas", "/mobile-billboards-dallas/"), ("Fort Worth", "/mobile-billboards-fort-worth/"), ("Arlington", "/mobile-billboards-arlington/"),
              ("Frisco & Plano", "/mobile-billboards-frisco-plano/"), ("Rockwall & Rowlett", "/mobile-billboards-rockwall-rowlett/"),
              ("Houston", "/mobile-billboards-houston/"), ("Austin", "/mobile-billboards-austin/"), ("San Antonio", "/mobile-billboards-san-antonio/")]

def bullets(items):
    return Wd("text-editor", editor="<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>", text_color="#C8D1E6",
              **custom_type('Inter', 400, 17, 1.75), css_classes="mm-prose")

# ---------------- CAMPAIGN PAGE TEMPLATE ----------------
camp_hero = hero("[Campaign type] · Mobile LED billboard trucks", "[H1: page's main keyword, e.g. LED Billboard Truck Rental for a Day]",
                 "[Intro, 2–3 sentences (40–60 words): who this campaign is for and what they get. Use the main keyword once.]",
                 'mod-media-led-billboard-truck-fleet')
camp_hero["elements"][0]["elements"].insert(0, crumbs())
CAMPAIGN = [
    camp_hero,
    fresh(STRIP),
    section("overview", [two_col(
        con([eyebrow("Overview"), h2("[H2: What a [campaign type] LED truck campaign is]", 18, 620),
             text_block(["[Paragraph 1, 80–110 words: what this campaign is and the problem it solves. Use the main keyword naturally.]",
                         "[Paragraph 2, 80–110 words: how the day/week/month runs, from planning to the truck on the road.]",
                         "[Paragraph 3, 60–90 words: why businesses pick this length over the others. Link to the other campaign pages.]"])]),
        glance("At a glance", [("Length:", "[one day / a full week / a month or longer]"), ("Hours per day:", "[from Jamie]"),
                               ("Truck and screen:", "[screen size, video and sound, from Jamie]"), ("Where:", "Dallas–Fort Worth, Texas and nationwide"),
                               ("Your ad:", "static, animated or video, changeable during the campaign"), ("Reporting:", "campaign photos and a report of where and when your ad ran")]))],
        title="Overview"),
    section("included", [
        *sec_head("What's included", "[H2: What you get with a [campaign type] campaign]",
                  "Every MOD Media campaign comes with the same essentials, whatever the length."),
        grid([svc("Included", "Dedicated LED truck", "Your truck shows only your ads, so you get 100% share of voice for the whole campaign.", "every campaign", "Get pricing →"),
              svc("Included", "A plan for where it drives", "We plan where and when the truck drives around your audience: districts, events and busy corridors.", "every campaign", "Get pricing →"),
              svc("Included", "Ad set-up for the screen", "Send your artwork or your message. We format it for the LED screen before day one.", "every campaign", "Get pricing →"),
              svc("Included", "Photos and a report", "Campaign photos and a report of where and when your ad ran.", "every campaign", "Get pricing →")], 4, 2, 1, 18),
    ], bg='bg_alt', title="What's included"),
    section("benefits", [*sec_head("Why it works", "[H2: Why [campaign type] LED truck advertising works]",
                                   "[One sentence connecting these benefits to this campaign length.]"),
        grid([info_card(t, b) for t, b in BENEFITS], 3, 2, 1, 18)], title="Benefits"),
    section("use-cases", [*sec_head("Best for", "[H2: Who books [campaign type] campaigns]",
                                    "[One sentence: the businesses and goals this length suits best.]"),
        grid([info_card("[Use case 1, e.g. Grand openings]", "[2–3 sentences, 40–60 words: how this kind of business uses a [campaign type] campaign, and the result they're after.]"),
              info_card("[Use case 2]", "[40–60 words]"), info_card("[Use case 3]", "[40–60 words]"), info_card("[Use case 4]", "[40–60 words]")], 2, 2, 1, 18)],
        pt=0, title="Use cases"),
    section("compare", [*sec_head("Daily, weekly or monthly?", "Which campaign length is right for you?",
                                  "All three use a dedicated truck that shows only your ads. The difference is how long your message stays on the road."),
        Wd("text-editor", editor=COMPARE, css_classes="mm-prose mm-table", text_color="#C8D1E6", **custom_type('Inter', 400, 15, 1.6))],
        bg='bg_alt', title="Compare lengths"),
    section("how", [*sec_head("How it works", "On the road in four simple steps"),
        grid([step("01", "Tell us your goal", "Share your audience, cities and dates. We recommend a daily, weekly or monthly campaign."),
              step("02", "Send your ad", "Send us your artwork, or tell us your message and we'll help format it for the LED screen."),
              step("03", "We plan &amp; drive", "We plan where and when your truck drives, then put your dedicated truck on the road."),
              step("04", "See the results", "Get campaign photos and a report showing where and when your ad ran.")], 4, 2, 1, 18)],
        title="How it works"),
    section("design", [*sec_head("Ad design tips", "Make your ad work on a moving screen",
                                 "We format every ad for the LED screen. These four rules get the most from it."),
        grid([info_card(t, b, f"Tip {i + 1}") for i, (t, b) in enumerate(DESIGN_TIPS)], 4, 2, 1, 18)], pt=0, title="Design tips"),
    section("results", [two_col(
        con([eyebrow("Measuring results"), h2("How you'll know it worked", 18, 560),
             text_block(["[60–90 words: how results are tracked for this campaign length, and what a good outcome looks like.]"]),
             bullets(TRACKING)]),
        Wd("image", image=img('mod-media-led-truck-night-campaign-texas'), image_size="large", css_classes="mm-gfig", height=px(380),
           height_mobile=px(240), _border_border="solid", _border_width=box(1), _border_color=LINE, _border_radius=box(20)), "1fr 1fr")],
        bg='bg_alt', title="Results"),
    section("photos", [*sec_head("Real campaigns", "[H2: [Campaign type] campaigns we've run]",
                                 "[One sentence describing the photos below. Use real campaigns only.]"),
        photo_row(['mod-media-khaite-led-truck-new-york', 'mod-media-led-truck-game-night-arlington', 'mod-media-grimaldis-led-truck-game-day'])],
        title="Photos"),
    fresh(BRANDWALL),
    fresh(REVIEWS),
    section("cities", [*sec_head("Where we run campaigns", "[H2: [Campaign type] campaigns across Texas]",
                                 "Based in Dallas–Fort Worth, with campaigns across Texas and nationwide."),
        link_chips(CITY_LINKS)], pt=0, title="Cities"),
    section("faq", [*sec_head("Questions", "[H2: [Campaign type] campaign questions]"),
        faq([("[Q1 from the Page outlines tab]", "[Answer, 40–80 words]"), ("[Q2]", "[Answer]"), ("[Q3]", "[Answer]"), ("[Q4]", "[Answer]"),
             ("[Q5]", "[Answer]"), ("[Q6]", "[Answer]"), ("[Q7]", "[Answer]"), ("[Q8]", "[Answer]")])], bg='bg_alt', title="FAQ"),
    section("related", [*sec_head("Keep exploring", "Other ways to run your campaign"),
        grid([link_card("Launches &amp; events", "Daily Campaigns", "One high-impact day for a launch, opening or event.", "/campaigns/daily/", "See daily campaigns →"),
              link_card("Most booked", "Weekly Campaigns", "Repeat exposure across the week so your message sticks.", "/campaigns/weekly/", "See weekly campaigns →"),
              link_card("Maximum reach", "Monthly Campaigns", "Own the streets for a month or longer.", "/campaigns/monthly/", "See monthly campaigns →"),
              link_card("Cost guide", "What does it cost?", "Typical prices and what changes them.", "/blog/mobile-billboard-truck-advertising-guide/", "Read the pricing guide →")], 4, 2, 1, 18)],
        title="Related"),
    fresh(QUOTE),
]

# ---------------- CITY PAGE TEMPLATE ----------------
city_hero = con([
    crumbs(),
    eyebrow("Mobile billboards in [City], TX"),
    H("[H1: e.g. Mobile Billboard Truck Advertising in [City]]", 'h1', 'hero_h1', 'text', _element_width='initial', _element_custom_width=px(720)),
    H("[Intro, 2–3 sentences (40–60 words): why [City] works for LED truck campaigns, with one real local detail.]", 'p', None, '#C8D1E6', mt=24,
      **custom_type('Inter', 400, 19, 1.65), _element_width='initial', _element_custom_width=CU('60ch')),
    row([button("Get Campaign Pricing →", "#quote"), button("Call or Text (469) 279-2511", "tel:+14692792511", 'ghost')],
        g=14, wrap=True, margin=box(34, 0, 0, 0)),
], content_width="boxed", _title="City hero", css_classes="mm-feat", min_height=px(560), flex_justify_content="center",
   flex_align_items="flex-start", padding=box(90, 20, 80, 20), overflow="hidden", background_background="classic",
   background_image=img('mod-media-dallas-skyline-reunion-tower-led-truck'), background_position="center center",
   background_size="cover", background_color="#06080F")
CITY = [
    city_hero,
    fresh(STRIP),
    section("why", [two_col(
        con([eyebrow("Why [City]"), h2("[H2: Why mobile billboards work in [City]]", 18, 600),
             text_block(["[Paragraph 1, 90–120 words: the local audience, business districts and traffic. Specific to this city only.]",
                         "[Paragraph 2, 90–120 words: the events and venues that draw crowds, and how a campaign is timed around them.]",
                         "[Paragraph 3, 70–100 words: which campaign lengths work best here, with links to Daily, Weekly and Monthly Campaigns.]"])]),
        con([Wd("image", image=img('mod-media-led-truck-night-campaign-texas'), image_size="large", css_classes="mm-gfig",
                height=px(300), height_mobile=px(240), _border_border="solid", _border_width=box(1), _border_color=LINE, _border_radius=box(20)),
             glance("[City] at a glance", [("Served from:", "MOD Media's base in Rockwall, Dallas–Fort Worth"), ("Campaigns:", "daily, weekly and monthly"),
                                           ("Busiest areas:", "[2–3 real areas]"), ("Big events:", "[2–3 real events]"),
                                           ("Minimum booking:", "[from Jamie, for cities outside DFW]")])], flex_gap=gap(18)))],
        title="Why this city"),
    section("areas", [*sec_head("Where your brand is seen", "[H2: [City] areas and venues we target]",
                                "[One sentence: the truck goes where your customers already are.]"),
        grid([info_card("[Area or venue 1]", "[40–60 words: who is there, when it's busiest, and which businesses benefit.]", "[District / Venue / Corridor]"),
              info_card("[Area or venue 2]", "[40–60 words]", "[Type]"), info_card("[Area or venue 3]", "[40–60 words]", "[Type]"),
              info_card("[Area or venue 4]", "[40–60 words]", "[Type]"), info_card("[Area or venue 5]", "[40–60 words]", "[Type]"),
              info_card("[Area or venue 6]", "[40–60 words]", "[Type]")], 3, 2, 1, 18)], bg='bg_alt', title="Areas and venues"),
    section("events", [*sec_head("Event calendar", "[H2: [City] events worth a campaign]",
                                 "[One sentence on timing: book early for the busiest dates.]"),
        grid([info_card("[Event 1]", "[30–50 words: when it happens and how brands use a truck around it.]", "[Month]"),
              info_card("[Event 2]", "[30–50 words]", "[Month]"), info_card("[Event 3]", "[30–50 words]", "[Month]"),
              info_card("[Event 4]", "[30–50 words]", "[Month]")], 4, 2, 1, 18)], pt=0, title="Events"),
    section("industries", [two_col(
        con([eyebrow("Who advertises here"), h2("[H2: Businesses that advertise with LED trucks in [City]]", 18, 600),
             text_block(["[70–100 words: the local industries that get the most from a truck here, with one example of how each would use it.]"])]),
        chips(["[Industry 1]", "[Industry 2]", "[Industry 3]", "[Industry 4]", "[Industry 5]", "[Industry 6]"]), "1fr 1fr")],
        bg='bg_alt', title="Industries"),
    section("campaigns", [*sec_head("Campaigns in [City]", "Book by the day, week or month",
                                    "Every campaign uses a dedicated truck that shows only your ads."),
        grid([link_card("Launches &amp; events", "Daily Campaigns", "One high-impact day for a launch, opening or event.", "/campaigns/daily/", "See daily campaigns →"),
              link_card("Most booked", "Weekly Campaigns", "Repeat exposure across the week so your message sticks.", "/campaigns/weekly/", "See weekly campaigns →"),
              link_card("Maximum reach", "Monthly Campaigns", "Own the streets for a month or longer.", "/campaigns/monthly/", "See monthly campaigns →"),
              link_card("Texas &amp; nationwide", "Multi-City &amp; Agency", "Coordinated campaigns in more than one city.", "/campaigns/multi-city-agency/", "See multi-city →")], 4, 2, 1, 18)],
        title="Campaign types"),
    section("how", [*sec_head("How it works", "[H2: How a [City] campaign works]"),
        grid([step("01", "Tell us your goal", "Share your audience, dates and the [City] areas you want to reach."),
              step("02", "Send your ad", "Send your artwork, or tell us your message and we'll format it for the LED screen."),
              step("03", "We plan &amp; drive", "We plan where and when the truck drives in [City], then put it on the road."),
              step("04", "See the results", "Get campaign photos and a report showing where and when your ad ran.")], 4, 2, 1, 18)],
        pt=0, title="How it works"),
    section("photos", [*sec_head("Real campaigns", "[H2: LED truck campaigns in [City]]", "[One sentence. Real photos from this city where we have them.]"),
        photo_row(['mod-media-led-truck-dallas-skyline-sunset', 'mod-media-buckley-apartments-led-truck', 'mod-media-atlas-led-truck-night'])],
        bg='bg_alt', title="Photos"),
    fresh(BRANDWALL),
    fresh(REVIEWS),
    section("nearby", [*sec_head("Nearby", "Other cities we serve", "Running a campaign in more than one city? We coordinate them for you."),
        link_chips(CITY_LINKS)], pt=0, title="Nearby cities"),
    section("faq", [*sec_head("Questions", "[H2: Mobile billboard questions in [City]]"),
        faq([("[Q1 from the Page outlines tab, e.g. How much does a mobile billboard cost in [City]?]", "[Answer, 40–80 words]"),
             ("[Q2, e.g. Do I need a permit for a mobile billboard truck in [City]?]", "[Answer, verified facts only]"),
             ("[Q3]", "[Answer]"), ("[Q4]", "[Answer]"), ("[Q5]", "[Answer]"), ("[Q6]", "[Answer]"), ("[Q7]", "[Answer]"), ("[Q8]", "[Answer]")])],
        bg='bg_alt', title="FAQ"),
    fresh(QUOTE),
]

# ---------------- BLOG POST TEMPLATE (Theme Builder: single post) ----------------
POST = [
    con([
        eyebrow("MOD Media blog"),
        Wd("theme-post-title", header_size="h1", title_color="#EEF2FB", align="left",
           __dynamic__={"title": '[elementor-tag id="mmpt001" name="post-title" settings="%7B%7D"]'},
           typography_typography="globals", __globals__={"typography_typography": "globals/typography?id=section_h2"},
           _element_width="initial", _element_custom_width=px(820)),
        Wd("post-info", view="inline", icon_list=[{"_id": nid(), "type": "date", "selected_icon": {"value": "far fa-calendar", "library": "fa-regular"}},
                                                  {"_id": nid(), "type": "custom", "custom_text": "MOD Media", "selected_icon": {"value": "far fa-user", "library": "fa-regular"}}],
           icon_color="#2EE6F0", text_color="#9AA6C2", space_between=px(22), _margin=box(18, 0, 0, 0),
           **custom_type('Inter', 500, 14, 1.65, pre='icon_typography')),
    ], content_width="boxed", _title="Post header", css_classes="mm-hero", padding=box(80, 20, 40, 20), padding_mobile=box(64, 20, 32, 20),
       background_background="classic", background_color="#06080F", overflow="hidden"),
    con([
        Wd("theme-post-featured-image", image_size="large", css_classes="mm-gfig", height=px(460), height_mobile=px(240),
           __dynamic__={"image": '[elementor-tag id="mmfi001" name="post-featured-image" settings="%7B%7D"]'},
           width=px(100, '%'), _element_width="initial", _element_custom_width=px(960),
           _border_border="solid", _border_width=box(1), _border_color=LINE, _border_radius=box(20)),
        Wd("theme-post-content", text_color="#C8D1E6", css_classes="mm-prose", **custom_type('Inter', 400, 17, 1.75),
           _margin=box(40, 0, 0, 0), _element_width="initial", _element_custom_width=px(760)),
    ], content_width="boxed", _title="Post body", flex_align_items="center", padding=box(0, 20, 90, 20), padding_mobile=box(0, 20, 64, 20),
       background_background="classic", background_color="#06080F"),
    con([
        eyebrow("Ready to plan your campaign?"),
        h2("Put your brand on a MOD Media truck.", 18, 620),
        H("Daily, weekly and monthly LED billboard truck campaigns across Dallas–Fort Worth, Texas and nationwide.", 'p', 'lede', 'muted',
          _element_width='initial', _element_custom_width=px(620)),
        row([button("Get Campaign Pricing →", "/get-pricing/"), button("Call or Text (469) 279-2511", "tel:+14692792511", 'ghost')],
            g=14, wrap=True, margin=box(28, 0, 0, 0)),
    ], content_width="boxed", _title="Post call to action", css_classes="mm-quote", padding=box(90, 20, 90, 20), padding_mobile=box(64, 20, 64, 20),
       border_border="solid", border_width=box(1, 0, 0, 0), border_color=LINE),
]

B.mark(CAMPAIGN); B.mark(CITY); B.mark(POST)
json.dump({"campaign": CAMPAIGN, "city": CITY, "post": POST}, open('templates.json', 'w'))
print({k: len(json.dumps(v)) // 1024 for k, v in {"campaign": CAMPAIGN, "city": CITY, "post": POST}.items()}, 'KB')
