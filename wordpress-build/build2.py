"""Home page + header + footer as standard Elementor JSON, matched to the reference CSS (ref.css)."""
import json, random
random.seed(7)
M = json.load(open('media.json'))
W = json.load(open('html_widgets.json'))
MAPS = 'https://www.google.com/maps/place/MOD+Media/@32.9483767,-98.2124309,8z/data=!4m6!3m5!1s0x6e4f45aa517042a1:0x71b3eeff57eca41!8m2!3d32.9553105!4d-96.8930934!16s%2Fg%2F11wfppzqnz'
_used = set()
def nid():
    while True:
        s = ''.join(random.choice('0123456789abcdef') for _ in range(7))
        if s not in _used: _used.add(s); return s
def px(n, u='px'): return {"unit": u, "size": n, "sizes": []}
def CU(v): return {"unit": "custom", "size": v, "sizes": []}
def box(t, r=None, b=None, l=None, u='px'):
    r = t if r is None else r; b = t if b is None else b; l = r if l is None else l
    return {"unit": u, "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": len({t, r, b, l}) == 1}
def gap(c, r=None):
    r = c if r is None else r
    return {"column": str(c), "row": str(r), "isLinked": c == r, "unit": "px", "size": c}
def C(c): return f"globals/colors?id={c}"
def TY(t): return f"globals/typography?id={t}"
def img(k): return {"id": M[k]['id'], "url": M[k]['url'], "alt": "", "source": "library"}
LINE = "#FFFFFF17"

def con(children, **s):
    s.setdefault('content_width', 'full'); s.setdefault('flex_direction', 'column')
    s.setdefault('flex_gap', gap(0)); s.setdefault('padding', box(0))
    return {"id": nid(), "elType": "container", "settings": s, "elements": children, "isInner": False}
def Wd(wt, **s):
    if 'css_classes' in s: s['_css_classes'] = s.pop('css_classes')   # widgets use the Advanced-tab key
    return {"id": nid(), "elType": "widget", "widgetType": wt, "settings": s, "elements": []}
def merge_globals(s, g):
    s.setdefault("__globals__", {}).update(g); return s

def H(text, tag='p', typo=None, color='text', link=None, mt=0, mb=0, **x):
    """Heading widget (also used for single paragraphs: no theme <p> margins)."""
    s = {"title": text, "header_size": tag}
    g = {}
    if color and not color.startswith('#'): g["title_color"] = C(color)
    elif color: s["title_color"] = color
    if typo: g["typography_typography"] = TY(typo)
    if g: s["__globals__"] = g
    if link: s["link"] = {"url": link, "is_external": "", "nofollow": ""}
    if mt or mb: s["_margin"] = box(mt, 0, mb, 0)
    for k, v in x.items():
        if k == '__globals__': s.setdefault('__globals__', {}).update(v)
        else: s[k] = v
    return Wd("heading", **s)

def custom_type(fam, w, size, lh, ls=None, tt=None, pre='typography'):
    d = {f"{pre}_typography": "custom", f"{pre}_font_family": fam, f"{pre}_font_weight": str(w),
         f"{pre}_font_size": px(size) if not isinstance(size, dict) else size, f"{pre}_line_height": px(lh, 'em')}
    d[f"{pre}_letter_spacing"] = ls if ls is not None else px(0)
    if tt: d[f"{pre}_text_transform"] = tt
    return d

def eyebrow(t, mb=18): return H(t, 'div', 'accent', 'primary', mb=mb, css_classes='mm-eyebrow')
def h2(t, mb, w=760): return H(t, 'h2', 'section_h2', 'text', mb=mb, _element_width='initial', _element_custom_width=px(w))
def lede(t, mb=56, w=681, color='muted', typo='lede', mt=0):
    return H(t, 'p', typo, color, mt=mt, mb=mb, _element_width='initial', _element_custom_width=px(w))
def sec_head(eb, title, ld=None):
    if ld: return [eyebrow(eb), h2(title, 18), lede(ld)]
    return [eyebrow(eb), h2(title, 56)]

def button(label, link, style='primary', small=False, mt=0, external=False, **x):
    s = {"text": label, "link": {"url": link, "is_external": "on" if external else "", "nofollow": ""},
         "text_padding": box(12, 20) if small else box(16, 26), "border_radius": box(999),
         "typography_typography": "custom", "typography_font_family": "Inter", "typography_font_weight": "700",
         "typography_font_size": px(14 if small else 15), "typography_line_height": px(1, 'em'),
         "typography_text_transform": "none", "typography_letter_spacing": px(0),
         "background_background": "classic", "button_background_hover_background": "classic"}
    if style == 'primary':
        s.update(css_classes='mm-btn', background_color="#2EE6F0", button_text_color="#031317",
                 button_background_hover_color="#2EE6F0", hover_color="#031317")
    else:
        s.update(css_classes='mm-ghost', background_color="#FFFFFF0F", button_text_color="#EEF2FB", hover_color="#EEF2FB",
                 button_background_hover_color="#FFFFFF1F", border_border="solid", border_width=box(1), border_color=LINE,
                 button_hover_border_color=LINE)
    if mt: s["_margin"] = box(mt, 0, 0, 0)
    s.update(x); return Wd("button", **s)

def section(anchor, children, bg='bg_main', pt=110, pb=110, title=None, **x):
    s = dict(content_width="boxed", flex_direction="column", flex_align_items="stretch",
             padding=box(pt, 20, pb, 20), padding_mobile=box(76 if pt else 0, 20, 76 if pb else 0, 20),
             background_background="classic", __globals__={"background_color": C(bg)})
    if anchor: s["_element_id"] = anchor
    if title: s["_title"] = title
    s.update(x); return con(children, **s)

def grid(children, cols, tcols, mcols, g=18, **x):
    def gc(v): return {"unit": "fr", "size": v, "sizes": []} if isinstance(v, int) else CU(v)
    s = dict(container_type="grid", grid_columns_grid=gc(cols), grid_columns_grid_tablet=gc(tcols),
             grid_columns_grid_mobile=gc(mcols), grid_rows_grid={"unit": "fr", "size": 1, "sizes": []},
             grid_rows_grid_tablet={"unit": "fr", "size": 1, "sizes": []}, grid_rows_grid_mobile={"unit": "fr", "size": 1, "sizes": []},
             grid_gaps=gap(g), grid_auto_flow="row", grid_justify_items="stretch", grid_align_items="stretch")
    s.update(x); return con(children, **s)

def row(children, g=14, align='center', justify='flex-start', wrap=False, **x):
    s = dict(flex_direction="row", flex_gap=gap(g), flex_align_items=align, flex_justify_content=justify)
    if wrap: s["flex_wrap"] = "wrap"
    s.update(x); return con(children, **s)

# =====================================================================
HOME = []

# ---- HERO ----------------------------------------------------------
hero_left = con([
    eyebrow("Based in Dallas–Fort Worth · Campaigns nationwide", mb=22),
    H('Mobile LED billboard truck advertising.<br><span class="mm-glow">Light up your brand.</span>', 'h1', 'hero_h1', 'text'),
    H("High-impact out-of-home (OOH) campaigns on dedicated digital billboard trucks. We run daily, weekly and monthly campaigns for national brands, agencies and growing businesses, in Dallas–Fort Worth and wherever your audience is.",
      'p', None, '#C8D1E6', mt=24, **custom_type('Inter', 400, 19, 1.65), _element_width='initial', _element_custom_width=CU('60ch')),
    row([button("Request Campaign Pricing →", "#quote"), button("Call or Text (469) 279-2511", "tel:+14692792511", 'ghost')],
        g=14, wrap=True, margin=box(34, 0, 0, 0)),
    Wd("icon-list", view="inline", css_classes="mm-ticks", _margin=box(30, 0, 0, 0),
       icon_list=[{"_id": nid(), "text": t, "selected_icon": {"value": "fas fa-circle", "library": "fa-solid"}} for t in
                  ["Trusted by HP, Intuit, the NFL &amp; more", "Daily, weekly &amp; monthly campaigns", "Family-owned in Texas"]],
       space_between=px(22), text_color="#9AA6C2", **custom_type('Inter', 400, 14, 1.65, pre='icon_typography')),
])
HOME.append(con([hero_left, Wd("html", html=W['truck'], _title="LED truck animation (custom)")],
    content_width="boxed", _title="Hero", css_classes="mm-hero", container_type="grid",
    grid_columns_grid=CU("1.05fr .95fr"), grid_columns_grid_tablet=CU("1fr"), grid_columns_grid_mobile=CU("1fr"),
    grid_rows_grid={"unit": "fr", "size": 1, "sizes": []}, grid_gaps=gap(56), grid_align_items="center",
    padding=box(90, 20, 70, 20), padding_mobile=box(90, 20, 70, 20), overflow="hidden",
    background_background="classic", background_color="#06080F",
    custom_css=("selector{isolation:isolate}\n"
                "selector::after{content:'';position:absolute;inset:0;z-index:-1;pointer-events:none;"
                "background:#06080F url('" + M['mod-media-dallas-skyline-reunion-tower-led-truck']['url'] + "') center/cover no-repeat;"
                "opacity:.55;transform:scale(1.05)}")))

# ---- BRAND STRIP (marquee) -----------------------------------------
logos = ['hp', 'choctaw', 'jh', 'academy', 'nfl', 'khaite', 'intuit', 'fiesta', 'cricket', 'big12', 'jd', 'wildplanet']
HOME.append(con([
    H("Trusted by leading brands", 'div', None, 'muted', mb=16, align="center",
      **custom_type('Inter', 700, 11, 1, px(0.2, 'em'), 'uppercase')),
    Wd("image-carousel", carousel=[img(f'logo-{k}-white') for k in logos], thumbnail_size="medium", css_classes="mm-strip",
       slides_to_show="9", slides_to_show_tablet="6", slides_to_show_mobile="3", slides_to_scroll="1",
       navigation="none", autoplay="yes", autoplay_speed=0, speed=3750, infinite="yes",
       pause_on_hover="no", pause_on_interaction="no", image_spacing="custom", image_spacing_custom=px(18),
       gallery_vertical_align="center", caption_type="", link_to="none"),
], _title="Brand strip", _element_id="trusted", padding=box(22, 0, 22, 0), background_background="classic",
   border_border="solid", border_width=box(1, 0, 1, 0), border_color=LINE, overflow="hidden",
   __globals__={"background_color": C('bg_alt')}))

# ---- SERVICES ------------------------------------------------------
def svc(tag, title, body, best, cta):
    return con([
        H(tag, 'div', 'tag', 'primary'),
        H(title, 'h3', 'card_h3', 'text'),
        H(body, 'p', 'card_p', 'muted', _flex_grow=1, _flex_size="grow"),
        H(f"Best for: {best}", 'div', None, 'text', _padding=box(14, 0, 0, 0), _border_border="dashed",
          _border_width=box(1, 0, 0, 0), _border_color=LINE, **custom_type('Inter', 600, 13, 1.4)),
        H(cta, 'div', None, 'primary', link="#quote", **custom_type('Inter', 700, 14, 1.65)),
    ], css_classes="mm-svc", padding=box(30, 26, 28, 26), flex_gap=gap(14), background_background="gradient",
       background_color="#0F1529", background_color_b="#0A0F1E", background_gradient_angle=px(180, 'deg'),
       border_border="solid", border_width=box(1), border_color=LINE, border_radius=box(18),
       border_hover_border="solid", border_hover_width=box(1), border_hover_color="#2EE6F073")
stats = [("12+", "national brands served, including HP, Intuit and the NFL"), ("Day · Week · Month", "flexible campaign lengths"),
         ("100%", "share of voice: your truck shows only your ads"), ("Since 2023", "running LED truck campaigns")]
HOME.append(section("services", [
    *sec_head("Our campaigns", "Dedicated LED billboard trucks, booked by the day, week or month",
              "Every campaign gets its own digital billboard truck showing only your brand, with a custom plan for where and when it drives: business districts, events, neighborhoods and high-traffic corridors."),
    grid([svc("Launches &amp; events", "Daily Campaigns", "One high-impact day for a product launch, grand opening, conference or game day. Your brand on the move from morning to night.", "launches, activations, events", "Book a day →"),
          svc("Most booked", "Weekly Campaigns", "Repeat exposure across the week so your message sticks: ideal for promotions, openings, recruiting drives and seasonal pushes.", "promotions, seasonal campaigns", "Plan a week →"),
          svc("Maximum reach", "Monthly Campaigns", "Own the streets for a month or longer. Sustained brand awareness for national brands, political campaigns and market launches.", "brand awareness, market entry", "Talk long-term →"),
          svc("Texas &amp; nationwide", "Multi-City &amp; Agency", "Coordinated campaigns in more than one city, and white-glove support for media agencies adding mobile billboards to a client's plan.", "national brands, media agencies", "Request a proposal →")],
         4, 2, 1, 18),
    grid([Wd("icon-box", selected_icon={"value": "", "library": ""}, title_text=a, description_text=b, title_size="div",
             position="top", text_align="left", title_bottom_space=px(8), title_color="#EEF2FB", description_color="#9AA6C2",
             **custom_type('Plus Jakarta Sans', 800, 30, 1, px(0), pre='title_typography'),
             **custom_type('Inter', 400, 14, 1.65, pre='description_typography'),
             _padding=box(22), _background_background="classic", _background_color="#FFFFFF05",
             _border_border="solid", _border_width=box(1), _border_color=LINE, _border_radius=box(16)) for a, b in stats],
         4, 2, 2, 14, margin=box(40, 0, 0, 0)),
], title="Campaigns"))

# ---- BRANDS --------------------------------------------------------
kind = {'hp': 'tall', 'jh': 'wide', 'academy': 'wide', 'nfl': 'tall', 'intuit': 'wide', 'big12': 'tall', 'jd': 'tall', 'wildplanet': 'tall'}
alts = {'hp': 'HP', 'choctaw': 'Choctaw Casinos & Resorts', 'jh': 'Jackson Hewitt Tax Service', 'academy': 'Academy Sports + Outdoors',
        'nfl': 'NFL', 'khaite': 'KHAITE', 'intuit': 'Intuit', 'fiesta': 'Fiesta Food Marts', 'cricket': 'Cricket Wireless',
        'big12': 'Big 12 Conference', 'jd': 'JD Sports', 'wildplanet': 'Wild Planet'}
HOME.append(section("brands", [
    *sec_head("Proudly trusted by leading brands", "Brands that have lit up the streets with MOD Media",
              "From national retailers and tech companies to professional sports and luxury fashion, these are some of the brands whose campaigns we've put on the road."),
    grid([Wd("image", image=img(f'logo-{k}-white'), image_size="full", align="center",
             css_classes=("mm-lt " + kind.get(k, '')).strip(), _padding=box(22, 26)) for k in logos], 4, 3, 2, 14),
    H("All logos and names are trademarks of their respective owners and are shown to reflect campaigns executed by MOD Media. No endorsement is implied.",
      'p', None, 'muted', mt=18, **custom_type('Inter', 400, 12, 1.65)),
], pt=0, title="Brands"))

# ---- TRY YOUR AD ---------------------------------------------------
HOME.append(section("try", [*sec_head("Try it yourself", "See your ad on a MOD Media truck",
    "Type your message, pick a style and watch it light up the screen. When it looks right, send it to us with your quote request."),
    Wd("html", html=W['builder'], _title="Ad builder (custom)")], bg='bg_alt', title="Try your ad"))

# ---- PLANNER -------------------------------------------------------
HOME.append(section("finder", [*sec_head("Plan your campaign", "Which campaign fits your goal?",
    "Answer two quick questions and we'll recommend a campaign length and approach."),
    Wd("html", html=W['finder'], _title="Campaign planner (custom)")], title="Plan a campaign"))

# ---- HOW IT WORKS --------------------------------------------------
def step(n, t, b):
    return con([
        H(n, 'div', None, '#00000000', **custom_type('Plus Jakarta Sans', 800, 52, 1),
          text_stroke_text_stroke_type="yes", text_stroke_text_stroke=px(1.5), text_stroke_stroke_color="#2EE6F099"),
        H(t, 'h3', None, 'text', mt=14, **custom_type('Plus Jakarta Sans', 800, 26, 1.25, px(-0.01, 'em'))),
        H(b, 'p', 'card_p', 'muted', mt=10),
    ], padding=box(28), border_border="solid", border_width=box(1), border_color=LINE, border_radius=box(18),
       background_background="classic", __globals__={"background_color": C('bg_alt')})
HOME.append(section("how", [*sec_head("How it works", "On the road in four simple steps"),
    grid([step("01", "Tell us your goal", "Share your audience, cities and dates. We recommend a daily, weekly or monthly campaign."),
          step("02", "Send your ad", "Send us your artwork, or tell us your message and we'll help format it for the LED screen."),
          step("03", "We plan &amp; drive", "We plan where and when your truck drives, then put your dedicated truck on the road."),
          step("04", "See the results", "Get campaign photos of your ad on the road, and a full impressions report on request.")], 4, 2, 1, 18)],
    title="How it works"))

# ---- GALLERY (6-col grid, 170px rows, 14px gaps) -------------------
def gfig(key, cap, w, h, wm='100%', hm=312):
    return Wd("image", image=img(key), image_size="large", link_to="file", open_lightbox="yes",
              caption_source="custom", caption=cap, css_classes="mm-gfig",
              _element_width="initial", _element_custom_width=CU(w), _element_width_mobile="initial", _element_custom_width_mobile=CU(wm),
              _flex_size="none", height=px(h), height_mobile=px(hm), _border_border="solid", _border_width=box(1),
              _border_color=LINE, _border_radius=box(16), image_border_radius=box(0))
COLW = "((100% - 70px) / 6)"
span = lambda n: f"calc({COLW} * {n} + {14 * (n - 1)}px)"
HOME.append(section("gallery", [
    *sec_head("See what we've been up to", "Real campaigns. Real streets.", "Click any photo to see it full size."),
    row([gfig('mod-media-khaite-led-billboard-truck-campaign', "Khaite", span(4), 352),
         con([gfig('mod-media-jackson-hewitt-led-truck-sunset', "Jackson Hewitt", '100%', 168, "calc(50% - 7px)", 148),
              gfig('mod-media-atlas-led-truck-night', "Night campaign", '100%', 168, "calc(50% - 7px)", 148)],
             flex_gap=gap(14), width=CU(span(2)), width_mobile=CU('100%'), flex_direction_mobile="row", _flex_size="none")],
        g=14, align='stretch', flex_direction_mobile="column"),
    row([gfig('mod-media-led-truck-game-night-arlington', "Game night", span(2), 352),
         gfig('mod-media-buckley-apartments-led-truck', "The Buckley", span(2), 352),
         gfig('mod-media-grimaldis-led-truck-game-day', "Grimaldi's", span(2), 352)], g=14, align='stretch',
        flex_direction_mobile="column", margin=box(14, 0, 0, 0)),
    row([gfig('mod-media-led-truck-dallas-skyline-sunset', "Dallas at sunset", span(3), 352),
         gfig('mod-media-led-billboard-truck-fleet', "Our fleet", span(3), 352)], g=14, align='stretch',
        flex_direction_mobile="column", margin=box(14, 0, 0, 0)),
], pt=0, title="Our work"))

# ---- WHO WE HELP ---------------------------------------------------
inds = ["National brands", "Media &amp; ad agencies", "Retail &amp; consumer goods", "Tech &amp; finance", "Sports &amp; entertainment",
        "Fashion &amp; luxury", "Real estate &amp; apartments", "Restaurants &amp; hospitality", "Political campaigns",
        "Recruiting &amp; hiring", "Product launches &amp; activations"]
HOME.append(section("industries", [*sec_head("Who we help", "Built for brands that want to be seen"),
    Wd("icon-list", view="inline", css_classes="mm-inds",
       icon_list=[{"_id": nid(), "text": t, "selected_icon": {"value": "fas fa-circle", "library": "fa-solid"}} for t in inds],
       icon_size=px(9), text_indent=px(8), icon_color="#2EE6F0", text_color="#EEF2FB", space_between=px(0),
       **custom_type('Inter', 600, 15, 1.65, pre='icon_typography'))], pt=0, title="Who we help"))

# ---- REVIEWS -------------------------------------------------------
G = {'g1c': ("#2EE6F0", "#7C5CFF"), 'g2c': ("#FF3D8B", "#FFC24B"), 'g3c': ("#FFC24B", "#2EE6F0"), 'g4c': ("#7C5CFF", "#FF3D8B")}
def avatar(ini, g, size, fs, border=None):
    a, b = G[g]
    s = dict(css_classes="mm-av", align="center", _element_width="initial", _element_custom_width=px(size),
             _background_background="gradient", _background_color=a, _background_color_b=b, _background_gradient_angle=px(135, 'deg'),
             _border_radius=box(50, u='%'), **custom_type('Plus Jakarta Sans', 800, fs, 1))
    if border: s.update(_border_border="solid", _border_width=box(3), _border_color=border)
    s["_attributes"] = "aria-hidden|true"   # decorative, as in the reference
    w = H(ini, 'div', None, '#06121A', **s)
    w["settings"]["custom_css"] = f"selector{{height:{size}px;background-color:{a}}}\nselector .elementor-widget-container{{height:100%}}"
    return w
REV = [("Results", "I had one of my ads ran for my Christmas light install company and my phone was ringing off the hook with new clients.", "CM", "g1c", "Caleb Miller", "Christmas light installation"),
       ("Game day", "We recently had our business advertised with MOD Media at the last Cowboys game! Our ad grabbed a lot of attention and we’ve already had some calls from it!", "MH", "g2c", "Matthew Hodgson", "Game day campaign"),
       ("Repeat client", "We have been working with MOD Media for over a year and love their friendly and reliable team!", "MR", "g3c", "Michelle Robledo", "Atlas Bail Bonds"),
       ("Service", "You will not find a more professional team to work with. They will treat your business like it’s their own and do everything they can to make it successful.", "LH", "g4c", "Luke Hutcheson", "MOD Media client"),
       ("Quality", "Their LED billboard trucks are vibrant, eye-catching, and perfect for making a statement. The quality of the display exceeded my expectations.", "CS", "g1c", "Corey Schex", "MOD Media client"),
       ("Unique reach", "Cool, unique way to advertise your business! They put the eyes on your advertising and supercharge it.", "SM", "g2c", "Scott Mueller", "MOD Media client"),
       ("Service", "Fantastic company. Great quality customer service. Highly recommend.", "BD", "g3c", "Brian Drums", "MOD Media client")]
def rcard(tag, q, ini, g, name, role):
    return con([
        row([H("★★★★★", 'div', None, '#FFC24B', **custom_type('Inter', 400, 15, 1.65, px(3))),
             H(tag, 'div', None, 'primary', _element_width="auto", _padding=box(7, 10), _background_background="classic",
               _background_color="#2EE6F024", _border_border="solid", _border_width=box(1), _border_color="#2EE6F059",
               _border_radius=box(999), **custom_type('Inter', 700, 11, 1, px(0.12, 'em'), 'uppercase'))],
            g=10, justify='space-between', border_radius=box(0)),
        H(f"“{q}”", 'p', None, '#E7ECF8', _flex_grow=1, _flex_size="grow", **custom_type('Inter', 400, 18, 1.6)),
        row([avatar(ini, g, 48, 16),
             Wd("text-editor", editor=f"<p><strong>{name}</strong><span>{role}</span></p>", css_classes="mm-who",
                text_color="#9AA6C2", **custom_type('Inter', 400, 14, 1.65))],
            g=14, padding=box(16, 0, 0, 0), border_border="solid", border_width=box(1, 0, 0, 0), border_color=LINE, border_radius=box(0)),
    ], css_classes="mm-rcard", padding=box(30), flex_gap=gap(18), height=CU("100%"), border_border="solid",
       border_width=box(1), border_color=LINE, border_radius=box(22), background_background="gradient",
       background_color="#151D38", background_color_b="#0C1224", background_gradient_angle=px(180, 'deg'))
summary = con([
    H("★★★★★", 'div', None, '#FFC24B', text_shadow_text_shadow_type="yes",
      text_shadow_text_shadow={"horizontal": 0, "vertical": 0, "blur": 18, "color": "rgba(255,194,75,0.5)"},
      **custom_type('Inter', 400, 26, 1.65, px(4))),
    row([H("5.0", 'div', None, '#FFFFFF', **custom_type('Plus Jakarta Sans', 800, 88, 0.85, px(-0.04, 'em'))),
         H("average rating<br>from client reviews", 'div', None, 'muted', _padding=box(0, 0, 6, 0), **custom_type('Inter', 400, 14, 1.65))],
        g=12, align='flex-end'),
    row([avatar(i, g, 40, 13, "#0F1529") for i, g in [("CM", 'g1c'), ("MH", 'g2c'), ("MR", 'g3c'), ("LH", 'g4c'), ("CS", 'g1c')]],
        g=0, css_classes="mm-avs", margin=box(4, 0, 0, 0)),
    H("Restaurants, service companies and national brands trust MOD Media to put their message where people can’t miss it.",
      'p', None, '#C8D1E6', _flex_grow=1, _flex_size="grow", **custom_type('Inter', 400, 15, 1.65)),
    button("See our reviews on Google →", MAPS, 'ghost', external=True),
], css_classes="mm-rvsum", padding=box(34, 30), flex_gap=gap(16), border_border="solid", border_width=box(1),
   border_color="#2EE6F059", border_radius=box(24), overflow="hidden")
carousel = {"id": nid(), "elType": "widget", "widgetType": "nested-carousel", "elements": [], "settings": dict(
    carousel_items=[{"_id": nid(), "slide_title": f"Review {i + 1}"} for i in range(len(REV))],
    slides_to_show="2", slides_to_show_tablet="1.1718", slides_to_show_mobile="1.1288", slides_to_scroll="1",
    image_spacing_custom=px(18), autoplay="", infinite="", speed=500, pagination="bullets", arrows="yes",
    navigation_previous_icon={"value": "fas fa-arrow-left", "library": "fa-solid"},
    navigation_next_icon={"value": "fas fa-arrow-right", "library": "fa-solid"},
    _css_classes="mm-rv", _title="Client reviews carousel")}
for r in REV:
    c = rcard(*r); c["isInner"] = True
    carousel["elements"].append(c)
HOME.append(section("results", [*sec_head("Client reviews", "Businesses love what our trucks do for them"),
    con([summary, carousel], container_type="grid", grid_columns_grid=CU("minmax(0,340px) minmax(0,1fr)"),
        grid_columns_grid_tablet=CU("1fr"), grid_columns_grid_mobile=CU("1fr"), grid_rows_grid={"unit": "fr", "size": 1, "sizes": []},
        grid_gaps=gap(24), grid_align_items="stretch")], bg='bg_alt', title="Reviews"))

# ---- MARKETS -------------------------------------------------------
def mk(key, t, b):
    return con([H(t, 'h3', 'card_h3', 'text'), H(b, 'p', None, '#C8D1E6', **custom_type('Inter', 400, 15, 1.65))],
        min_height=px(300), flex_justify_content="flex-end", padding=box(26), flex_gap=gap(8), overflow="hidden",
        border_border="solid", border_width=box(1), border_color=LINE, border_radius=box(20),
        background_background="classic", background_image=img(key), background_position="center center", background_size="cover",
        background_color="#0A0F1E", background_overlay_background="gradient", background_overlay_color="#06080F00",
        background_overlay_color_stop=px(30, '%'), background_overlay_color_b="#06080FEB", background_overlay_color_b_stop=px(90, '%'),
        background_overlay_gradient_angle=px(180, 'deg'), background_overlay_opacity=px(1, ''))
HOME.append(section("markets", [*sec_head("Cities we serve", "Based in Dallas. Campaigns wherever your audience is.",
    "Our home market is Dallas–Fort Worth, and our trucks travel for campaigns across Texas and around the country."),
    grid([mk('mod-media-dallas-skyline-reunion-tower-led-truck', "Dallas–Fort Worth", "Our home base. Mobile LED advertising throughout Dallas, Fort Worth, Arlington, Frisco, Plano and surrounding cities."),
          mk('mod-media-led-truck-night-campaign-texas', "Across Texas", "Campaigns in Houston, Austin and San Antonio for conventions, sporting events, concerts and statewide launches."),
          mk('mod-media-khaite-led-truck-new-york', "Nationwide", "Multi-city and out-of-state campaigns for national brands and agencies, including New York and San Francisco.")],
         3, 1, 1, 18)], title="Cities we serve"))

# ---- FEATURE BAND --------------------------------------------------
HOME.append(con([
    eyebrow("Featured campaign · KHAITE"),
    h2("From DFW to the streets of New York.", 18, 620),
    lede("When luxury fashion house KHAITE wanted to stop people in their tracks, MOD Media put their campaign on high-resolution LED trucks in New York City. Big brands trust us to deliver, wherever the audience is.", 0, 620),
    button("Plan your campaign →", "#quote", mt=28),
], content_width="boxed", boxed_width=px(620), _title="Featured campaign", css_classes="mm-feat", min_height=px(520), flex_justify_content="center",
   flex_align_items="flex-start", padding=box(80, 20), padding_mobile=box(80, 20), overflow="hidden",
   background_background="classic", background_image=img('mod-media-khaite-led-screen-closeup'),
   background_position="center center", background_size="cover", background_color="#000000"))

# ---- FAQ -----------------------------------------------------------
FAQ = [("What is a mobile LED billboard truck?", "It's a truck fitted with large, high-resolution digital LED screens that drives your ad through the areas where your audience lives, works and gathers, or parks it at an event or store. It's out-of-home (OOH) advertising that goes to the people instead of waiting for them to drive past."),
       ("How much does it cost to rent an LED billboard truck in Dallas?", "Pricing depends on the campaign length (daily, weekly or monthly), the hours per day and the city. Longer campaigns cost less per day. Tell us your goals and dates and we'll send a custom quote."),
       ("How long can a campaign run?", "From a single day for a launch or event, to a week for a promotion, to a month or longer for sustained brand awareness."),
       ("Can I choose where the truck goes?", "Yes. Every campaign gets a custom plan for where and when the truck drives: business districts, neighborhoods, events, competitor locations or high-traffic corridors. The truck can also park at a set location."),
       ("Can I change my ad during the campaign?", "Yes. Our digital screens can show static images, video or animated content, and you can rotate several ads or update your creative during the campaign."),
       ("Do you run campaigns outside Dallas?", "Yes. We're based in Dallas–Fort Worth and run campaigns across Texas, including Houston, Austin and San Antonio, as well as in other states."),
       ("How do I track the results?", "You'll receive campaign photos, and on request a report with impressions and a GPS map of where your truck drove. Adding a QR code, short URL or promo code to your ad makes responses easy to measure."),
       ("Do you work with advertising agencies?", "Yes. We regularly support media and advertising agencies adding mobile billboards to their clients' campaigns.")]
HOME.append(section("faq", [*sec_head("Questions", "Good questions, straight answers"),
    Wd("accordion", tabs=[{"_id": nid(), "tab_title": q, "tab_content": f"<p>{a}</p>"} for q, a in FAQ], css_classes="mm-faq",
       selected_icon={"value": "fas fa-plus", "library": "fa-solid"}, selected_active_icon={"value": "fas fa-times", "library": "fa-solid"},
       icon_align="right", title_html_tag="div", faq_schema="yes", border_width=px(0),
       title_color="#EEF2FB", tab_active_color="#EEF2FB", icon_color="#2EE6F0", icon_active_color="#2EE6F0", content_color="#9AA6C2",
       **custom_type('Inter', 700, 17, 1.65, pre='title_typography'), **custom_type('Inter', 400, 16, 1.65, pre='content_typography'),
       _element_width="initial", _element_custom_width=px(880))], title="FAQ"))

# ---- QUOTE ---------------------------------------------------------
def cline(label, value, link=None):
    return row([H(label, 'div', None, 'muted', _element_width="initial", _element_custom_width=px(70), _flex_size="none",
                  **custom_type('Inter', 600, 11, 1, px(0.16, 'em'), 'uppercase')),
                H(value, 'div', None, 'text', link=link, css_classes="mm-cl", **custom_type('Inter', 400, 17, 1.65))], g=14)
F = lambda cid, ft, lab, ph="", req="", w="100", opts="", **x: dict({"_id": nid(), "custom_id": cid, "field_type": ft, "field_label": lab,
                                                                       "placeholder": ph, "required": req, "width": w, "field_options": opts}, **x)
fields = [
    F("step1", "step", "Campaign", previous_button="", next_button="Next step →"),
    F("h1", "html", "", field_html='<h3 class="mm-fh">What kind of campaign?</h3>'),
    F("campaign", "radio", "Campaign type", req="true", opts="Daily campaign\nWeekly campaign\nMonthly campaign\nMulti-city / agency",
      inline_list="elementor-subgroup-inline", field_value="Daily campaign"),
    F("area", "select", "Area", w="50", opts="Dallas–Fort Worth\nHouston\nAustin\nSan Antonio\nSeveral cities\nOutside Texas"),
    F("start_date", "date", "Start date", w="50", use_native_date="yes"),
    F("step2", "step", "Contact", previous_button="← Back", next_button=""),
    F("h2", "html", "", field_html='<h3 class="mm-fh">Where should we send your plan?</h3>'),
    F("name", "text", "Your name", "Jane Smith", "true", "50"),
    F("business", "text", "Business", "Your business name", "", "50"),
    F("phone", "text", "Phone", "(214) 555-0123", "true", "50"),
    F("email", "email", "Email", "you@business.com", "true", "50"),
    F("message", "text", "Your ad message (optional)", "What should your ad say?"),
    F("budget", "select", "Budget (optional)", opts="Not sure yet\nUnder $500\n$500 – $1,500\n$1,500 – $5,000\n$5,000+"),
]
form = Wd("form", form_name="Campaign Pricing Request", form_fields=fields, css_classes="mm-qform",
          show_labels="true", input_size="md", mark_required="", button_text="Request pricing", button_size="md",
          button_width="", button_align="end", submit_actions=["save-to-database", "email"], step_type="progress_bar",
          email_subject="New campaign pricing request from the MOD Media website", email_content="[all-fields]",
          custom_messages="yes", success_message="Request received. We'll send your campaign plan and pricing soon.",
          error_message="Something went wrong. Please call or text (469) 279-2511.",
          required_field_message="This field is required.", invalid_message="Please check this field.",
          column_gap=px(14), row_gap=px(18), label_spacing=px(8),
          field_text_color="#EEF2FB", field_background_color="#0A0F1E", field_border_color="#26304A", field_border_width=box(1),
          field_border_radius=box(12), label_color="#9AA6C2",
          **custom_type('Inter', 600, 12, 1.2, px(0.1, 'em'), 'uppercase', pre='label_typography'),
          **custom_type('Inter', 500, 16, 1.4, pre='field_typography'),
          button_background_color="#2EE6F0", button_text_color="#031317", button_background_hover_color="#2EE6F0",
          button_hover_color="#031317", previous_button_background_color="#FFFFFF0F", previous_button_text_color="#EEF2FB",
          _padding=box(34), _background_background="classic", _background_color="#111830D9", _border_border="solid",
          _border_width=box(1), _border_color="#2EE6F040", _border_radius=box(22),
          _box_shadow_box_shadow_type="yes", _box_shadow_box_shadow={"horizontal": 0, "vertical": 30, "blur": 80, "spread": -30, "color": "rgba(0,0,0,0.8)"},
          _title="Quote form")
HOME.append(section("quote", [con([
    con([eyebrow("Request campaign pricing", 0),
         h2("Let’s put your name in lights.", 0),
         lede("Tell us what you’re promoting, where and when. We’ll send a custom campaign plan and price.", 0, 9999, mt=18),
         con([cline("Call/Text", "(469) 279-2511", "tel:+14692792511"), cline("Email", "info@modmediaads.com", "mailto:info@modmediaads.com"),
              cline("Based in", "Dallas–Fort Worth, Texas")], flex_gap=gap(14), margin=box(30, 0, 0, 0))]),
    form], container_type="grid", grid_columns_grid=CU(".9fr 1.1fr"), grid_columns_grid_tablet=CU("1fr"), grid_columns_grid_mobile=CU("1fr"),
    grid_rows_grid={"unit": "fr", "size": 1, "sizes": []}, grid_gaps=gap(56), grid_align_items="start")],
    bg='bg_alt', title="Quote", css_classes="mm-quote", border_border="solid", border_width=box(1, 0, 0, 0), border_color=LINE))
# h2 in the quote column has an 18px top margin in the reference
HOME[-1]["elements"][0]["elements"][0]["elements"][1]["settings"]["_margin"] = box(18, 0, 0, 0)
HOME[-1]["elements"][0]["elements"][0]["elements"][2]["settings"].pop("_element_custom_width", None)

# =====================================================================
LOGO = lambda w=200: Wd("image", image=img('mod-media-logo-newest'), image_size="full", width=px(w), link_to="custom",
                        link={"url": "/", "is_external": "", "nofollow": ""}, align="left", _title="Logo", _flex_size="none")
HEADER = [con([
    LOGO(),
    Wd("nav-menu", menu="main-menu", layout="horizontal", align_items="center", pointer="none",
       dropdown="tablet", toggle="burger", full_width="stretch", text_align="aside",
       color_menu_item="#9AA6C2", color_menu_item_hover="#EEF2FB", pointer_color_menu_item_hover="#2EE6F0",
       color_menu_item_active="#9AA6C2",
       **custom_type('Inter', 500, 15, 1.65, px(0), 'none', pre='menu_typography'),
       padding_horizontal_menu_item=px(14), padding_vertical_menu_item=px(8), menu_space_between=px(0),
       color_dropdown_item="#EEF2FB", background_color_dropdown_item="#0B1020", color_dropdown_item_hover="#031317",
       background_color_dropdown_item_hover="#2EE6F0", toggle_color="#EEF2FB", toggle_background_color="#FFFFFF0F",
       toggle_size=px(22), toggle_border_radius=px(10), dropdown_top_distance=px(18),
       **custom_type('Inter', 600, 16, 1.4, px(0), 'none', pre='dropdown_typography'), padding_vertical_dropdown_item=px(14),
       _margin=box(0, -14, 0, -14), _margin_tablet=box(0), _flex_size="none", _title="Main menu"),
    row([H("(469) 279-2511", 'div', None, 'text', link="tel:+14692792511", hide_tablet="", hide_mobile="hidden-mobile",
           **custom_type('Inter', 600, 14, 1.2)),
         button("Get Pricing", "#quote", small=True, hide_mobile="hidden-mobile")], g=14, _flex_size="none", hide_mobile="hidden-mobile",
        width=CU("auto"), width_tablet=CU("auto")),
], content_width="boxed", css_classes="mm-header", flex_direction="row", flex_direction_tablet="row", flex_direction_mobile="row",
   flex_justify_content="space-between", flex_align_items="center", flex_gap=gap(20), min_height=px(75), padding=box(0, 20),
   background_background="classic", background_color="#06080FB8", border_border="solid", border_width=box(0, 0, 1, 0), border_color=LINE,
   sticky="top", sticky_on=["desktop", "tablet", "mobile"], sticky_offset=0, sticky_effects_offset=0, z_index=99, _title="Header")]
# tablet/mobile: burger sits at the right, next to the CTA group
HEADER[0]["elements"][1]["settings"]["_flex_order_tablet"] = "end"

def fcol(title, items):
    return con([H(title, 'div', None, 'text', mb=14, **custom_type('Inter', 700, 12, 1.25, px(0.16, 'em'), 'uppercase')),
                Wd("icon-list", icon_list=[{"_id": nid(), "text": t, "selected_icon": {"value": "", "library": ""}, "link": {"url": u} if u else {"url": ""}} for t, u in items],
                   space_between=px(8), text_color="#9AA6C2", text_color_hover="#EEF2FB", **custom_type('Inter', 400, 14, 1.65, pre='icon_typography'))])
TOTOP = """<style>.mm-pbar{position:fixed;top:0;left:0;height:3px;width:0;z-index:100;background:linear-gradient(90deg,#2EE6F0,#FF3D8B);box-shadow:0 0 12px #2EE6F0}
.mm-totop{position:fixed;right:20px;bottom:24px;z-index:55;width:48px;height:48px;border-radius:50%!important;border:1px solid rgba(255,255,255,.09)!important;background:rgba(17,24,48,.9)!important;color:#EEF2FB!important;font:400 20px/1 Inter,sans-serif!important;cursor:pointer;opacity:0;pointer-events:none;transform:translateY(10px);transition:opacity .3s,transform .3s;padding:0!important;box-shadow:none!important}
.mm-totop.show{opacity:1;pointer-events:auto;transform:none}.mm-totop:focus-visible{outline:3px solid #2EE6F0;outline-offset:3px}
@media(max-width:640px){.mm-totop{bottom:84px}}</style>
<div class="mm-pbar" aria-hidden="true"></div><button class="mm-totop" type="button" aria-label="Back to top">↑</button>
<script>(function(){var b=document.querySelector('.mm-pbar'),t=document.querySelector('.mm-totop');function u(){var h=document.documentElement,m=h.scrollHeight-h.clientHeight,y=h.scrollTop||document.body.scrollTop;b.style.width=(m>0?y/m*100:0)+'%';t.classList.toggle('show',y>800)}addEventListener('scroll',u,{passive:true});u();t.addEventListener('click',function(){scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'})});
var ids=['services','brands','try','finder','gallery','faq'],secs=ids.map(function(i){return document.getElementById(i)});
function spy(){var cur=-1;secs.forEach(function(x,k){if(x&&x.getBoundingClientRect().top<160)cur=k});
document.querySelectorAll('.mm-header .elementor-nav-menu--main a.elementor-item').forEach(function(a){var h=(a.getAttribute('href')||'').split('#')[1];a.classList.toggle('mm-active',cur>-1&&h===ids[cur]);a.classList.remove('elementor-item-active')})}
addEventListener('scroll',spy,{passive:true});addEventListener('load',spy);spy();})();</script>"""
FOOTER = [con([
    con([
        con([LOGO(), H("Family-owned mobile LED billboard truck advertising company based in Dallas–Fort Worth, running campaigns across Texas and nationwide.",
                       'p', 'small', 'muted', mt=18, _element_width="initial", _element_custom_width=px(300))]),
        fcol("Campaigns", [("Daily Campaigns", "/#services"), ("Weekly Campaigns", "/#services"), ("Monthly Campaigns", "/#services"), ("Multi-City &amp; Agency", "/#services")]),
        fcol("Cities", [("Dallas–Fort Worth", "/#markets"), ("Houston", "/#markets"), ("Austin", "/#markets"), ("San Antonio", "/#markets"), ("Nationwide", "/#markets")]),
        fcol("Contact", [("(469) 279-2511", "tel:+14692792511"), ("info@modmediaads.com", "mailto:info@modmediaads.com"), ("181 County Line Road<br>Rockwall, TX 75032", "")]),
    ], container_type="grid", grid_columns_grid=CU("1.4fr 1fr 1fr 1fr"), grid_columns_grid_tablet=CU("1fr 1fr"), grid_columns_grid_mobile=CU("1fr"),
       grid_rows_grid={"unit": "fr", "size": 1, "sizes": []}, grid_gaps=gap(30)),
    row([H("© 2026 MOD Media", 'div', None, 'muted', **custom_type('Inter', 400, 13, 1.65)),
         H("Website by Jayce Cabangcala · hirejayce.com", 'div', None, 'muted', **custom_type('Inter', 400, 13, 1.65))],
        g=12, justify='space-between', wrap=True, margin=box(40, 0, 0, 0), padding=box(24, 0, 0, 0),
        border_border="solid", border_width=box(1, 0, 0, 0), border_color=LINE),
    Wd("html", html=TOTOP, _title="Back to top + scroll progress (custom)"),
], content_width="boxed", _title="Footer", css_classes="mm-foot", padding=box(60, 20, 120, 20), padding_mobile=box(60, 20, 120, 20),
   background_background="classic", border_border="solid", border_width=box(1, 0, 0, 0), border_color=LINE,
   __globals__={"background_color": C('bg_main')}),
    con([button(t, u, 'ghost', small=True, text_padding=box(13, 10), border_radius=box(12), border_border="none",
                background_color="#FFFFFF12", typography_font_size=px(14), align="justify") for t, u in (("Call", "tel:+14692792511"), ("Text", "sms:+14692792511"))]
        + [button("Get Pricing", "#quote", small=True, text_padding=box(13, 10), border_radius=box(12), align="justify", css_classes="")],
        container_type="grid", grid_columns_grid=CU("1fr 1fr 1.4fr"), grid_columns_grid_tablet=CU("1fr 1fr 1.4fr"),
        grid_columns_grid_mobile=CU("1fr 1fr 1.4fr"), grid_rows_grid={"unit": "fr", "size": 1, "sizes": []}, grid_gaps=gap(8),
        _title="Mobile action bar", padding=box(10, 12), background_background="classic", background_color="#06080FEB",
        border_border="solid", border_width=box(1, 0, 0, 0), border_color=LINE, hide_desktop="hidden-desktop",
        hide_tablet="hidden-tablet", sticky="bottom", sticky_on=["mobile"], z_index=60)]

def mark(els):
    for e in els:
        for ch in e["elements"]:
            if ch["elType"] == "container":
                ch["isInner"] = True
                ch["settings"].setdefault("border_radius", box(0))
                if "border_border" not in ch["settings"]:
                    ch["settings"]["border_border"] = "none"
        mark(e["elements"])
mark(HOME); mark(HEADER); mark(FOOTER)
json.dump({"home": HOME, "header": HEADER, "footer": FOOTER}, open('built.json', 'w'))
print('sections', len(HOME), 'KB', len(json.dumps(HOME)) // 1024)
