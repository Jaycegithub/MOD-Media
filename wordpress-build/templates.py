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

# ---------------- CAMPAIGN PAGE TEMPLATE ----------------
CAMPAIGN = [
    hero("[Campaign type] · Mobile LED billboard trucks", "[H1: page's main keyword, e.g. LED Billboard Truck Rental for a Day]",
         "[Intro, 2–3 sentences: who this campaign is for and what they get. Mention Dallas–Fort Worth and the main keyword once.]",
         'mod-media-led-billboard-truck-fleet'),
    fresh(STRIP),
    section("included", [
        *sec_head("What's included", "[H2: What you get with a [campaign type] campaign]",
                  "[One sentence on what every campaign includes.]"),
        grid([svc("Included", "Dedicated LED truck", "Your truck shows only your ads, so you get 100% share of voice for the whole campaign.", "every campaign", "Get pricing →"),
              svc("Included", "A plan for where it drives", "We plan where and when the truck drives around your audience: districts, events and busy corridors.", "every campaign", "Get pricing →"),
              svc("Included", "Ad set-up for the screen", "Send your artwork or your message. We format it for the LED screen before day one.", "every campaign", "Get pricing →"),
              svc("Included", "Photos and a report", "Campaign photos and a report of where and when your ad ran.", "every campaign", "Get pricing →")], 4, 2, 1, 18),
    ], title="What's included"),
    section("best-for", [
        *sec_head("Best for", "[H2: Who books [campaign type] campaigns]"),
        chips(["[Use case 1]", "[Use case 2]", "[Use case 3]", "[Use case 4]", "[Use case 5]", "[Use case 6]"]),
        H("[1–2 sentences linking to the other campaign lengths, e.g. need longer exposure? See Weekly Campaigns.]", 'p', 'lede', 'muted', mt=28,
          _element_width='initial', _element_custom_width=px(681)),
    ], pt=0, title="Best for"),
    section("how", [*sec_head("How it works", "On the road in four simple steps"),
        grid([step("01", "Tell us your goal", "Share your audience, cities and dates. We recommend a daily, weekly or monthly campaign."),
              step("02", "Send your ad", "Send us your artwork, or tell us your message and we'll help format it for the LED screen."),
              step("03", "We plan &amp; drive", "We plan where and when your truck drives, then put your dedicated truck on the road."),
              step("04", "See the results", "Get campaign photos and a report showing where and when your ad ran.")], 4, 2, 1, 18)],
        bg='bg_alt', title="How it works"),
    section("photos", [*sec_head("Real campaigns", "[H2: [Campaign type] campaigns we've run]"),
        photo_row(['mod-media-khaite-led-truck-new-york', 'mod-media-led-truck-game-night-arlington', 'mod-media-grimaldis-led-truck-game-day'])],
        title="Photos"),
    fresh(REVIEWS),
    section("faq", [*sec_head("Questions", "[H2: [Campaign type] campaign questions]"),
        faq([("[Question from the Keywords tab, e.g. How much does a one-day LED truck campaign cost?]", "[Answer in 2–4 sentences.]"),
             ("[Question 2]", "[Answer]"), ("[Question 3]", "[Answer]"), ("[Question 4]", "[Answer]")])], title="FAQ"),
    fresh(QUOTE),
]

# ---------------- CITY PAGE TEMPLATE ----------------
city_hero = con([
    eyebrow("Mobile billboards in [City], TX"),
    H("[H1: e.g. Mobile Billboard Truck Advertising in [City]]", 'h1', 'hero_h1', 'text', _element_width='initial', _element_custom_width=px(720)),
    H("[Intro, 2–3 sentences: why [City] works for LED truck campaigns, with one local detail.]", 'p', None, '#C8D1E6', mt=24,
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
    section("why", [con([
        con([eyebrow("Why [City]"), h2("[H2: Why mobile billboards work in [City]]", 18, 560),
             text_block(["[Paragraph 1: the local audience, neighborhoods and traffic. Specific to this city.]",
                         "[Paragraph 2: events and venues, and how a campaign is planned around them.]",
                         "[Paragraph 3: campaign lengths available here, linking to Daily, Weekly and Monthly Campaigns.]"])]),
        Wd("image", image=img('mod-media-led-truck-night-campaign-texas'), image_size="large", css_classes="mm-gfig",
           height=px(440), height_mobile=px(260), _border_border="solid", _border_width=box(1), _border_color=LINE, _border_radius=box(20))],
        container_type="grid", grid_columns_grid=CU("1fr 1fr"), grid_columns_grid_tablet=CU("1fr"), grid_columns_grid_mobile=CU("1fr"),
        grid_rows_grid={"unit": "fr", "size": 1, "sizes": []}, grid_gaps=gap(56), grid_align_items="center")], title="Why this city"),
    section("areas", [*sec_head("Where your brand is seen", "[H2: [City] areas and venues we target]",
                                "[One sentence: the truck goes where your customers are.]"),
        chips(["[District 1]", "[District 2]", "[Venue 1]", "[Venue 2]", "[Corridor 1]", "[Event 1]", "[Event 2]"])],
        bg='bg_alt', title="Areas and venues"),
    section("campaigns", [*sec_head("Campaigns in [City]", "Book by the day, week or month"),
        grid([link_card("Launches &amp; events", "Daily Campaigns", "One high-impact day for a launch, opening or event.", "/campaigns/daily/", "See daily campaigns →"),
              link_card("Most booked", "Weekly Campaigns", "Repeat exposure across the week so your message sticks.", "/campaigns/weekly/", "See weekly campaigns →"),
              link_card("Maximum reach", "Monthly Campaigns", "Own the streets for a month or longer.", "/campaigns/monthly/", "See monthly campaigns →"),
              link_card("Texas &amp; nationwide", "Multi-City &amp; Agency", "Coordinated campaigns in more than one city.", "/campaigns/multi-city-agency/", "See multi-city →")], 4, 2, 1, 18)],
        title="Campaign types"),
    fresh(REVIEWS),
    section("faq", [*sec_head("Questions", "[H2: Mobile billboard questions in [City]]"),
        faq([("[Local question, e.g. Do I need a permit for a mobile billboard truck in [City]?]", "[Answer, only with verified facts.]"),
             ("[How much does a mobile billboard cost in [City]?]", "[Answer]"), ("[Question 3]", "[Answer]"), ("[Question 4]", "[Answer]")])], title="FAQ"),
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
