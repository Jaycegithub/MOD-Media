import json, random, string

random.seed(42)
M = json.load(open('media.json'))
W = json.load(open('html_widgets.json'))
MAPS = 'https://www.google.com/maps/place/MOD+Media/@32.9483767,-98.2124309,8z/data=!4m6!3m5!1s0x6e4f45aa517042a1:0x71b3eeff57eca41!8m2!3d32.9553105!4d-96.8930934!16s%2Fg%2F11wfppzqnz'

_used = set()
def nid():
    while True:
        s = ''.join(random.choice('0123456789abcdef') for _ in range(7))
        if s not in _used:
            _used.add(s); return s

def px(n, u='px'): return {"unit": u, "size": n, "sizes": []}
def box(t, r=None, b=None, l=None, u='px'):
    r = t if r is None else r; b = t if b is None else b; l = r if l is None else l
    return {"unit": u, "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": len({t, r, b, l}) == 1}
def gap(n): return {"column": str(n), "row": str(n), "isLinked": True, "unit": "px", "size": n}
def C(c): return f"globals/colors?id={c}"
def TY(t): return f"globals/typography?id={t}"
def img(key): return {"id": M[key]['id'], "url": M[key]['url'], "alt": "", "source": "library"}

def con(children, **s):
    s.setdefault('content_width', 'full')
    s.setdefault('flex_direction', 'column')
    return {"id": nid(), "elType": "container", "settings": s, "elements": children, "isInner": False}

def W_(wt, **s): return {"id": nid(), "elType": "widget", "widgetType": wt, "settings": s, "elements": []}

# ---------- widget helpers ----------
def heading(text, tag='h2', typo=None, color='text', align=None, link=None, **extra):
    s = {"title": text, "header_size": tag, "__globals__": {"title_color": C(color)}}
    if typo: s["__globals__"]["typography_typography"] = TY(typo)
    if align: s["align"] = align
    if link: s["link"] = {"url": link, "is_external": "", "nofollow": ""}
    s.update(extra); return W_("heading", **s)

def text(html, typo='text', color='muted', align=None, **extra):
    s = {"editor": html, "__globals__": {"text_color": C(color), "typography_typography": TY(typo)}}
    if align: s["align"] = align
    s.update(extra); return W_("text-editor", **s)

def eyebrow(label, align=None):
    s = {"view": "inline",
         "icon_list": [{"_id": nid(), "text": label, "selected_icon": {"value": "fas fa-circle", "library": "fa-solid"}}],
         "icon_size": px(8), "text_indent": px(10),
         "__globals__": {"icon_color": C('primary'), "text_color": C('primary'), "icon_typography_typography": TY('accent')}}
    if align: s["icon_align"] = align
    return W_("icon-list", **s)

def button(label, link, style='primary', size='md', external=False, **extra):
    s = {"text": label, "link": {"url": link, "is_external": "on" if external else "", "nofollow": ""}, "size": size,
         "__globals__": {"typography_typography": TY('button'), "background_color": C('primary'), "button_text_color": C('btn_text'),
                         "hover_color": C('btn_text'), "button_background_hover_color": C('cyan_hover')},
         "background_background": "classic", "button_background_hover_background": "classic", "border_radius": box(999), "text_padding": box(16, 26)}
    if style == 'ghost':
        s.update({"background_background": "classic", "button_background_hover_background": "classic",
                  "border_border": "solid", "border_width": box(1), "border_radius": box(999),
                  "text_padding": box(16, 26)})
        s["__globals__"].update({"background_color": C('ghost'), "button_text_color": C('text'), "hover_color": C('text'),
                                 "border_color": C('border'), "button_background_hover_color": C('border')})
    s.update(extra); return W_("button", **s)

def section(anchor, children, bg='bg_main', pad=(110, 110), tpad=(80, 80), mpad=(64, 64), **extra):
    s = {"content_width": "boxed", "flex_direction": "column", "flex_align_items": "flex-start", "flex_gap": gap(20),
         "padding": box(pad[0], 20, pad[1], 20), "padding_tablet": box(tpad[0], 20, tpad[1], 20), "padding_mobile": box(mpad[0], 16, mpad[1], 16),
         "background_background": "classic", "__globals__": {"background_color": C(bg)}}
    if anchor: s["_element_id"] = anchor
    s.update(extra); return con(children, **s)

def sec_head(eb, title, lede=None, mb=36):
    out = [eyebrow(eb), heading(title, 'h2', typo='section_h2', _element_width="initial", _element_custom_width=px(760),
                                 _element_width_mobile="inherit")]
    if lede:
        out.append(text(f"<p>{lede}</p>", typo='lede', _element_width="initial", _element_custom_width=px(680),
                        _element_width_mobile="inherit", _margin=box(0, 0, mb, 0)))
    else:
        out[-1]["settings"]["_margin"] = box(0, 0, mb, 0)
    return out

def grid(children, cols=4, tcols=2, mcols=1, g=18):
    return con(children, container_type="grid", width=px(100, '%'),
               grid_columns_grid={"unit": "fr", "size": cols, "sizes": []},
               grid_columns_grid_tablet={"unit": "fr", "size": tcols, "sizes": []},
               grid_columns_grid_mobile={"unit": "fr", "size": mcols, "sizes": []},
               grid_rows_grid={"unit": "fr", "size": 1, "sizes": []},
               grid_gaps={"column": str(g), "row": str(g), "isLinked": True, "unit": "px", "size": g},
               grid_auto_flow="row", padding=box(0))

def row(children, g=18, wrap=False, align='stretch', justify='flex-start', mobile_col=True, **extra):
    s = dict(flex_direction="row", flex_gap=gap(g), flex_align_items=align, flex_justify_content=justify,
             width=px(100, '%'), padding=box(0))
    if wrap: s["flex_wrap"] = "wrap"
    if mobile_col: s["flex_direction_mobile"] = "column"
    s.update(extra); return con(children, **s)

def card_style(**extra):
    s = dict(padding=box(30, 26, 28, 26), flex_gap=gap(14), background_background="gradient",
             background_color="#0F1529", background_color_b="#0A0F1E", background_gradient_angle=px(180, 'deg'),
             border_border="solid", border_width=box(1), border_radius=box(18),
             border_hover_border="solid", border_hover_width=box(1),
             box_shadow_hover_box_shadow_type="yes",
             box_shadow_hover_box_shadow={"horizontal": 0, "vertical": 18, "blur": 50, "spread": -20, "color": "rgba(46,230,240,0.45)"},
             __globals__={"border_color": C('border'), "border_hover_color": C('primary')})
    s.update(extra); return s

# ================= HOME =================
H = []

# HERO
hero_left = con([
    eyebrow("Based in Dallas–Fort Worth · Campaigns nationwide"),
    heading('Mobile LED billboard truck advertising.<br><span style="color:var(--e-global-color-primary);text-shadow:0 0 30px rgba(46,230,240,.55),0 0 80px rgba(46,230,240,.35)">Light up your brand.</span>',
            'h1', typo='hero_h1'),
    text("<p>High-impact out-of-home (OOH) campaigns on dedicated digital billboard trucks. We run daily, weekly and monthly campaigns for national brands, agencies and growing businesses, in Dallas–Fort Worth and wherever your audience is.</p>",
         typo='lede', color='text', _element_width="initial", _element_custom_width=px(560), _element_width_tablet="inherit"),
    row([button("Request Campaign Pricing →", "#quote"),
         button("Call or Text (469) 279-2511", "tel:+14692792511", style='ghost')],
        g=14, wrap=True, align='center', mobile_col=False, _margin=box(14, 0, 0, 0)),
    W_("icon-list", view="inline",
       icon_list=[{"_id": nid(), "text": t, "selected_icon": {"value": "fas fa-check-circle", "library": "fa-solid"}} for t in
                  ["Trusted by HP, Intuit, the NFL &amp; more", "Daily, weekly &amp; monthly campaigns", "Family-owned in Texas"]],
       icon_size=px(16), text_indent=px(8), space_between=px(22),
       __globals__={"icon_color": C('primary'), "text_color": C('muted'), "icon_typography_typography": TY('small')},
       _margin=box(10, 0, 0, 0)),
], width=px(52, '%'), width_tablet=px(100, '%'), flex_gap=gap(18), padding=box(0), flex_align_items="flex-start")
hero_right = con([W_("html", html=W['truck'], _title="LED truck animation (custom)")],
                 width=px(48, '%'), width_tablet=px(100, '%'), padding=box(0))
H.append(con([row([hero_left, hero_right], g=56, align='center', flex_direction_tablet="column")],
             content_width="boxed", _title="Hero", overflow="hidden", padding=box(90, 20, 70, 20), padding_mobile=box(56, 16, 48, 16),
             background_background="classic", background_image=img('mod-media-dallas-skyline-reunion-tower-led-truck'),
             background_position="center center", background_size="cover",
             background_overlay_background="gradient", background_overlay_color="rgba(6,8,15,0.62)",
             background_overlay_color_stop=px(0, '%'), background_overlay_color_b="#06080F",
             background_overlay_color_b_stop=px(100, '%'), background_overlay_gradient_angle=px(180, 'deg'),
             background_overlay_opacity=px(1, ''), __globals__={}))

# BRAND STRIP
logos = ['hp', 'choctaw', 'jh', 'academy', 'nfl', 'khaite', 'intuit', 'fiesta', 'cricket', 'big12', 'jd', 'wildplanet']
H.append(con([
    heading("Trusted by leading brands", 'p', typo='accent', color='muted', align='center'),
    W_("image-carousel", carousel=[img(f'logo-{k}-white') for k in logos], thumbnail_size="medium",
       slides_to_show="6", slides_to_show_tablet="4", slides_to_show_mobile="3", slides_to_scroll="1",
       navigation="none", autoplay="yes", autoplay_speed=1800, speed=700, infinite="yes",
       pause_on_hover="no", pause_on_interaction="no", image_spacing="custom", image_spacing_custom=px(44),
       gallery_vertical_align="center", caption_type="", link_to="none",
       custom_css="selector .swiper-slide img{max-height:40px;width:auto;margin:0 auto;opacity:.72}"),
], content_width="boxed", _title="Brand strip", _element_id="trusted", padding=box(22, 20, 24, 20), flex_gap=gap(14),
   background_background="classic", border_border="solid", border_width=box(1, 0, 1, 0),
   __globals__={"background_color": C('bg_alt'), "border_color": C('border')}))

# SERVICES
def svc(tag, title, body, best, cta):
    return con([
        heading(tag, 'p', typo='accent', color='primary'),
        heading(title, 'h3', typo='card_h3'),
        text(f"<p>{body}</p>", typo='small', color='muted', _flex_grow=1, _flex_size="grow"),
        text(f"<p><strong>Best for:</strong> {best}</p>", typo='small', color='text',
             _padding=box(14, 0, 0, 0), _border_border="dashed", _border_width=box(1, 0, 0, 0),
             __globals__={"text_color": C('text'), "typography_typography": TY('small'), "_border_color": C('border')}),
        heading(cta, 'p', typo='button', color='primary', link="#quote"),
    ], **card_style())
stats = [("12+", "national brands served, including HP, Intuit and the NFL"), ("Day · Week · Month", "flexible campaign lengths"),
         ("100%", "share of voice: your truck shows only your ads"), ("Since 2023", "running LED truck campaigns")]
H.append(section("services", [
    *sec_head("Our campaigns", "Dedicated LED billboard trucks, booked by the day, week or month",
              "Every campaign gets its own digital billboard truck showing only your brand, with a custom route planned around your audience: business districts, events, neighborhoods and high-traffic corridors."),
    grid([
        svc("Launches &amp; events", "Daily Campaigns", "One high-impact day for a product launch, grand opening, conference or game day. Your brand on the move from morning to night.", "launches, activations, events", "Book a day →"),
        svc("Most booked", "Weekly Campaigns", "Repeat exposure across the week so your message sticks: ideal for promotions, openings, recruiting drives and seasonal pushes.", "promotions, seasonal campaigns", "Plan a week →"),
        svc("Maximum reach", "Monthly Campaigns", "Own the streets for a month or longer. Sustained brand awareness for national brands, political campaigns and market launches.", "brand awareness, market entry", "Talk long-term →"),
        svc("Texas &amp; nationwide", "Multi-City &amp; Agency", "Coordinated campaigns in more than one city, and white-glove support for media agencies adding mobile billboards to a client's plan.", "national brands, media agencies", "Request a proposal →"),
    ]),
    grid([W_("icon-box", selected_icon={"value": "", "library": ""}, title_text=a, description_text=b, title_size="div",
             text_align="left", title_bottom_space=px(8),
             _padding=box(22), _background_background="classic", _background_color="#FFFFFF05",
             _border_border="solid", _border_width=box(1), _border_radius=box(16),
             __globals__={"title_color": C('text'), "description_color": C('muted'), "_border_color": C('border'),
                          "title_typography_typography": TY('card_h3'), "description_typography_typography": TY('small')},
             title_typography_font_size=px(28)) for a, b in stats], g=14),
], _title="Campaigns"))
# make stats title bigger via local override (global typography plus local size)
for w in H[-1]["elements"][-1]["elements"]:
    w["settings"]["title_typography_typography"] = "custom"; w["settings"]["title_typography_font_family"] = "Plus Jakarta Sans"
    w["settings"]["title_typography_font_weight"] = "800"; w["settings"]["title_typography_font_size"] = px(28)
    w["settings"]["title_typography_line_height"] = px(1.1, 'em')
    del w["settings"]["__globals__"]["title_typography_typography"]

# BRANDS
def logo_tile(k):
    wide = k in ('intuit', 'jh', 'academy', 'choctaw', 'cricket', 'fiesta', 'khaite')
    return W_("image", image=img(f'logo-{k}-white'), image_size="full", align="center",
              width=px(66, '%'), height=px(38 if wide else 64), object_fit="contain", **{"object-fit": "contain"},
              opacity=px(0.78, ''), opacity_hover=px(1, ''),
              _padding=box(33 if wide else 20, 20), _background_background="gradient",
              _background_color="#FFFFFF0F", _background_color_b="#FFFFFF04", _background_gradient_angle=px(180, 'deg'),
              _border_border="solid", _border_width=box(1), _border_radius=box(18), _border_color="#FFFFFF17",
              _border_hover_border="solid", _border_hover_width=box(1), _border_hover_color="#2EE6F08C",
              _box_shadow_hover_box_shadow_type="yes",
              _box_shadow_hover_box_shadow={"horizontal": 0, "vertical": 18, "blur": 50, "spread": -20, "color": "rgba(46,230,240,0.6)"},
              _css_classes="mm-logo-tile")
H.append(section("brands", [
    *sec_head("Proudly trusted by leading brands", "Brands that have lit up the streets with MOD Media",
              "From national retailers and tech companies to professional sports and luxury fashion, these are some of the brands whose campaigns we've put on the road."),
    grid([logo_tile(k) for k in logos], cols=4, tcols=3, mcols=2, g=14),
    text("<p>All logos and names are trademarks of their respective owners and are shown to reflect campaigns executed by MOD Media. No endorsement is implied.</p>",
         typo='small', color='muted', typography_typography="custom", typography_font_size=px(12)),
], pad=(20, 110), tpad=(10, 80), mpad=(10, 64), _title="Brands"))
H[-1]["elements"][-1]["settings"]["__globals__"].pop("typography_typography", None)

# TRY YOUR AD
H.append(section("try", [
    *sec_head("Try it yourself", "See your ad on a MOD Media truck",
              "Type your message, pick a style and watch it light up the screen. When it looks right, send it to us with your quote request."),
    W_("html", html=W['builder'], _title="Ad builder (custom)", _element_width="inherit"),
], bg='bg_alt', _title="Try your ad"))

# CAMPAIGN PLANNER
H.append(section("finder", [
    *sec_head("Plan your campaign", "Which campaign fits your goal?",
              "Answer two quick questions and we'll recommend a campaign length and approach."),
    W_("html", html=W['finder'], _title="Campaign planner (custom)", _element_width="inherit"),
], _title="Plan a campaign"))

# HOW IT WORKS
def step(n, t, b):
    return con([
        heading(n, 'p', color='text', typography_typography="custom", typography_font_family="Plus Jakarta Sans",
                typography_font_weight="800", typography_font_size=px(52), typography_line_height=px(1, 'em'),
                text_stroke_text_stroke_type="yes", text_stroke_text_stroke=px(1.5), text_stroke_stroke_color="rgba(46,230,240,0.6)",
                title_color="#00000000", __globals__={}),
        heading(t, 'h3', typo='card_h3', _margin=box(6, 0, 0, 0)),
        text(f"<p>{b}</p>", typo='small', color='muted'),
    ], padding=box(28), flex_gap=gap(10), background_background="classic", border_border="solid", border_width=box(1),
       border_radius=box(18), __globals__={"background_color": C('bg_alt'), "border_color": C('border')})
H.append(section("how", [
    eyebrow("How it works"),
    heading("On the road in four simple steps", 'h2', typo='section_h2', _margin=box(0, 0, 36, 0)),
    grid([step("01", "Tell us your goal", "Share your audience, cities and dates. We recommend a daily, weekly or monthly campaign."),
          step("02", "Send your ad", "Send us your artwork, or tell us your message and we'll help format it for the LED screen."),
          step("03", "We plan &amp; drive", "We build a custom route around your audience and put your dedicated truck on the road."),
          step("04", "See the results", "Get campaign photos and a report showing where and when your ad ran.")]),
], pad=(20, 110), tpad=(10, 80), mpad=(10, 64), _title="How it works"))

# GALLERY
def gimg(key, h, hm=240, wpct=None):
    s = dict(image=img(key), image_size="large", width=px(100, '%'), height=px(h), height_mobile=px(hm),
             object_fit="cover", **{"object-fit": "cover"}, image_border_radius=box(16), link_to="file", open_lightbox="yes",
             _border_border="solid", _border_width=box(1), _border_radius=box(16), _border_color="#FFFFFF17", _flex_size="none",
             custom_css="selector a{display:block;width:100%}\nselector img{display:block}")
    if wpct:
        s.update(_element_width="initial", _element_custom_width=px(wpct, '%'), _element_width_mobile="inherit")
    return W_("image", **s)
H.append(section("gallery", [
    *sec_head("See what we've been up to", "Real campaigns. Real streets.", "Click any photo to see it full size."),
    row([gimg('mod-media-khaite-led-billboard-truck-campaign', 420, wpct=65.5),
         con([gimg('mod-media-jackson-hewitt-led-truck-sunset', 203), gimg('mod-media-atlas-led-truck-night', 203)],
             flex_gap=gap(14), padding=box(0), width=px(32.6, '%'), width_mobile=px(100, '%'), _flex_size="none")], g=14),
    row([gimg('mod-media-led-truck-game-night-arlington', 320, wpct=32.4), gimg('mod-media-buckley-apartments-led-truck', 320, wpct=32.4),
         gimg('mod-media-grimaldis-led-truck-game-day', 320, wpct=32.4)], g=14),
    row([gimg('mod-media-led-truck-dallas-skyline-sunset', 340, wpct=49.3), gimg('mod-media-led-billboard-truck-fleet', 340, wpct=49.3)], g=14),
], pad=(20, 110), tpad=(10, 80), mpad=(10, 64), flex_gap=gap(14), _title="Our work"))

# WHO WE HELP
inds = ["National brands", "Media &amp; ad agencies", "Retail &amp; consumer goods", "Tech &amp; finance", "Sports &amp; entertainment",
        "Fashion &amp; luxury", "Real estate &amp; apartments", "Restaurants &amp; hospitality", "Political campaigns",
        "Recruiting &amp; hiring", "Product launches &amp; activations"]
H.append(section("industries", [
    eyebrow("Who we help"),
    heading("Built for brands that want to be seen", 'h2', typo='section_h2', _element_width="initial", _element_custom_width=px(760),
            _element_width_mobile="inherit", _margin=box(0, 0, 28, 0)),
    W_("icon-list", view="inline", icon_list=[{"_id": nid(), "text": t, "selected_icon": {"value": "fas fa-circle", "library": "fa-solid"}} for t in inds],
       icon_size=px(8), text_indent=px(10), space_between=px(12),
       __globals__={"icon_color": C('primary'), "text_color": C('text'), "icon_typography_typography": TY('small')},
       custom_css="selector .elementor-icon-list-items{row-gap:12px}\nselector .elementor-icon-list-item{padding:14px 20px!important;border:1px solid rgba(255,255,255,.09);border-radius:999px;background:rgba(255,255,255,.03);font-weight:600}"),
], pad=(20, 110), tpad=(10, 80), mpad=(10, 64), _title="Who we help"))

# REVIEWS
REV = [("Caleb Miller", "Christmas light installation", "I had one of my ads ran for my Christmas light install company and my phone was ringing off the hook with new clients."),
       ("Matthew Hodgson", "Game day campaign", "We recently had our business advertised with MOD Media at the last Cowboys game! Our ad grabbed a lot of attention and we’ve already had some calls from it!"),
       ("Michelle Robledo", "Atlas Bail Bonds", "We have been working with MOD Media for over a year and love their friendly and reliable team!"),
       ("Luke Hutcheson", "MOD Media client", "You will not find a more professional team to work with. They will treat your business like it’s their own and do everything they can to make it successful."),
       ("Corey Schex", "MOD Media client", "Their LED billboard trucks are vibrant, eye-catching, and perfect for making a statement. The quality of the display exceeded my expectations."),
       ("Scott Mueller", "MOD Media client", "Cool, unique way to advertise your business! They put the eyes on your advertising and supercharge it."),
       ("Brian Drums", "MOD Media client", "Fantastic company. Great quality customer service. Highly recommend.")]
summary = con([
    W_("star-rating", rating_scale="5", rating=5, star_style="star_unicode", unmarked_star_style="solid", icon_size=px(26), icon_space=px(4),
       __globals__={"stars_color": C('accent')}, align="left"),
    heading("5.0", 'p', color='text', typography_typography="custom", typography_font_family="Plus Jakarta Sans",
            typography_font_weight="800", typography_font_size=px(88), typography_line_height=px(0.9, 'em'), typography_letter_spacing=px(-3)),
    heading("average rating from client reviews", 'p', typo='small', color='muted'),
    text("<p>Restaurants, service companies and national brands trust MOD Media to put their message where people can’t miss it.</p>", typo='small', color='text'),
    button("See our reviews on Google →", MAPS, style='ghost', external=True, _margin=box(10, 0, 0, 0)),
], width=px(30, '%'), width_tablet=px(100, '%'), padding=box(34, 30), flex_gap=gap(14), border_border="solid", border_width=box(1),
   border_color="rgba(46,230,240,0.35)", border_radius=box(24), background_background="gradient", background_color="#0F2B3A",
   background_color_b="#121A33", background_gradient_angle=px(135, 'deg'), flex_align_items="flex-start", __globals__={})
reviews = W_("reviews", slides=[{"_id": nid(), "content": q, "name": n, "title": r, "rating": 5,
                                 "image": {"url": "", "id": ""}, "selected_social_icon": {"value": "", "library": ""}} for n, r, q in REV],
             slides_per_view="2", slides_per_view_tablet="1", slides_per_view_mobile="1", slides_to_scroll="1",
             autoplay="yes", autoplay_speed=6000, loop="yes", pause_on_hover="yes", show_arrows="yes", pagination="bullets",
             space_between=px(18), speed=500, star_style="star_unicode",
             slide_background_color="#151D38", slide_border_size=box(1), slide_border_color="#FFFFFF17",
             slide_border_radius=px(22), slide_padding=box(30), header_margin=px(14),
             name_color="#EEF2FB", title_color="#9AA6C2", content_color="#E7ECF8", stars_color="#FFC24B",
             arrows_color="#EEF2FB", pagination_color="#2EE6F0",
             name_typography_typography="custom", name_typography_font_family="Inter", name_typography_font_weight="700",
             content_typography_typography="custom", content_typography_font_family="Inter", content_typography_font_size=px(17),
             content_typography_line_height=px(1.6, 'em'),
             _element_width="initial", _element_custom_width=px(68, '%'), _element_width_tablet="inherit", _title="Client reviews carousel",
             custom_css="selector .elementor-testimonial__header{border-bottom:1px solid rgba(255,255,255,.09)!important;padding-bottom:14px}\nselector .elementor-testimonial__header::after{display:none}\n@media(max-width:767px){selector .elementor-swiper-button{display:none}}\nselector .swiper-pagination-bullet{width:10px;height:10px;margin:0 8px!important}")
H.append(section("results", [
    eyebrow("Client reviews"),
    heading("Businesses love what our trucks do for them", 'h2', typo='section_h2', _element_width="initial", _element_custom_width=px(760),
            _element_width_mobile="inherit", _margin=box(0, 0, 36, 0)),
    row([summary, reviews], g=24, align='stretch', flex_direction_tablet="column"),
], bg='bg_alt', _title="Reviews"))

# MARKETS
def mk(key, t, b):
    return con([heading(t, 'h3', typo='card_h3'), text(f"<p>{b}</p>", typo='small', color='text', text_color="#C8D1E6", __globals__={"typography_typography": TY('small')})],
               min_height=px(360), min_height_mobile=px(300), flex_justify_content="flex-end", padding=box(26), flex_gap=gap(8), overflow="hidden",
               border_border="solid", border_width=box(1), border_radius=box(20),
               background_background="classic", background_image=img(key), background_position="center center", background_size="cover",
               background_overlay_background="gradient", background_overlay_color="rgba(6,8,15,0)", background_overlay_color_stop=px(30, '%'),
               background_overlay_color_b="rgba(6,8,15,0.92)", background_overlay_color_b_stop=px(90, '%'),
               background_overlay_gradient_angle=px(180, 'deg'), background_overlay_opacity=px(1, ''),
               __globals__={"border_color": C('border')})
H.append(section("markets", [
    *sec_head("Cities we serve", "Based in Dallas. Campaigns wherever your audience is.",
              "Our home market is Dallas–Fort Worth, and our trucks travel for campaigns across Texas and around the country."),
    grid([mk('mod-media-dallas-skyline-reunion-tower-led-truck', "Dallas–Fort Worth", "Our home base. Mobile LED advertising throughout Dallas, Fort Worth, Arlington, Frisco, Plano and surrounding cities."),
          mk('mod-media-led-truck-night-campaign-texas', "Across Texas", "Campaigns in Houston, Austin and San Antonio for conventions, sporting events, concerts and statewide launches."),
          mk('mod-media-khaite-led-truck-new-york', "Nationwide", "Multi-city and out-of-state campaigns for national brands and agencies, including New York and San Francisco.")],
         cols=3, tcols=1, mcols=1),
], _title="Cities we serve"))

# KHAITE FEATURE
H.append(con([
    eyebrow("Featured campaign · KHAITE"),
    heading("From DFW to the streets of New York.", 'h2', typo='section_h2', _element_width="initial", _element_custom_width=px(620), _element_width_mobile="inherit"),
    text("<p>When luxury fashion house KHAITE wanted to stop people in their tracks, MOD Media put their campaign on high-resolution LED trucks in New York City. Big brands trust us to deliver, wherever the audience is.</p>",
         typo='lede', _element_width="initial", _element_custom_width=px(620), _element_width_mobile="inherit"),
    button("Plan your campaign →", "#quote", _margin=box(10, 0, 0, 0)),
], content_width="boxed", _title="Featured campaign", min_height=px(520), flex_justify_content="center", flex_align_items="flex-start",
   flex_gap=gap(18), padding=box(80, 20), padding_mobile=box(64, 16),
   background_background="classic", background_image=img('mod-media-khaite-led-screen-closeup'), background_position="center center", background_size="cover",
   background_overlay_background="gradient", background_overlay_color="rgba(6,8,15,0.96)", background_overlay_color_stop=px(0, '%'),
   background_overlay_color_b="rgba(6,8,15,0.15)", background_overlay_color_b_stop=px(100, '%'), background_overlay_gradient_angle=px(90, 'deg'),
   background_overlay_gradient_angle_mobile=px(180, 'deg'), background_overlay_opacity=px(1, '')))

# FAQ
FAQ = [("What is a mobile LED billboard truck?", "It's a truck fitted with large, high-resolution digital LED screens that drives your ad through the areas where your audience lives, works and gathers, or parks it at an event or store. It's out-of-home (OOH) advertising that goes to the people instead of waiting for them to drive past."),
       ("How much does it cost to rent an LED billboard truck in Dallas?", "Pricing depends on the campaign length (daily, weekly or monthly), the hours per day and the city. Longer campaigns cost less per day. Tell us your goals and dates and we'll send a custom quote."),
       ("How long can a campaign run?", "From a single day for a launch or event, to a week for a promotion, to a month or longer for sustained brand awareness."),
       ("Can I choose where the truck goes?", "Yes. Every campaign gets a custom route planned around your audience: business districts, neighborhoods, events, competitor locations or high-traffic corridors. The truck can also park at a set location."),
       ("Can I change my ad during the campaign?", "Yes. Our digital screens can show static images, video or animated content, and you can rotate several ads or update your creative during the campaign."),
       ("Do you run campaigns outside Dallas?", "Yes. We're based in Dallas–Fort Worth and run campaigns across Texas, including Houston, Austin and San Antonio, as well as in other states."),
       ("How do I track the results?", "You'll receive campaign photos and a report showing where and when your ad ran. Adding a QR code, short URL or promo code to your ad makes responses easy to measure."),
       ("Do you work with advertising agencies?", "Yes. We regularly support media and advertising agencies adding mobile billboards to their clients' campaigns.")]
H.append(section("faq", [
    eyebrow("Questions"),
    heading("Good questions, straight answers", 'h2', typo='section_h2', _margin=box(0, 0, 28, 0)),
    W_("accordion", tabs=[{"_id": nid(), "tab_title": q, "tab_content": f"<p>{a}</p>"} for q, a in FAQ],
       selected_icon={"value": "fas fa-plus", "library": "fa-solid"}, selected_active_icon={"value": "fas fa-minus", "library": "fa-solid"},
       icon_align="right", title_html_tag="div", faq_schema="yes",
       border_width=px(1), border_color="#FFFFFF17", title_background="#0B1020", content_background_color="#0B1020",
       title_padding=box(18, 22), content_padding=box(0, 22, 20, 22),
       __globals__={"title_color": C('text'), "tab_active_color": C('primary'), "icon_color": C('primary'), "icon_active_color": C('primary'),
                    "content_color": C('muted'), "content_typography_typography": TY('text')},
       title_typography_typography="custom", title_typography_font_family="Inter", title_typography_font_weight="700", title_typography_font_size=px(17),
       _element_width="initial", _element_custom_width=px(880), _element_width_tablet="inherit",
       custom_css="selector .elementor-accordion-item{border-radius:14px;overflow:hidden;margin-bottom:12px}"),
], _title="FAQ"))

# QUOTE
fields = [
    ("campaign", "select", "What kind of campaign?", "", "true", "100", "Daily campaign\nWeekly campaign\nMonthly campaign\nMulti-city / agency campaign"),
    ("area", "select", "Area", "", "", "50", "Dallas–Fort Worth\nHouston\nAustin\nSan Antonio\nSeveral cities\nOutside Texas"),
    ("start_date", "date", "Start date", "", "", "50", ""),
    ("name", "text", "Your name", "Jane Smith", "true", "50", ""),
    ("business", "text", "Business", "Your business name", "", "50", ""),
    ("phone", "text", "Phone", "(214) 555-0123", "true", "50", ""),
    ("email", "email", "Email", "you@business.com", "true", "50", ""),
    ("budget", "select", "Budget (optional)", "", "", "100", "Not sure yet\nUnder $500\n$500 – $1,500\n$1,500 – $5,000\n$5,000+"),
    ("message", "textarea", "Your ad message (optional)", "What should your ad say?", "", "100", ""),
]
form = W_("form", form_name="Campaign Pricing Request",
          form_fields=[{"_id": nid(), "custom_id": cid, "field_type": ft, "field_label": lab, "placeholder": ph, "required": req,
                        "width": w, "field_options": opts, "rows": 3, "use_native_date": "yes"} for cid, ft, lab, ph, req, w, opts in fields],
          show_labels="true", input_size="md", mark_required="", button_text="Request pricing", button_size="md", button_width="100",
          button_align="stretch", submit_actions=["save-to-database", "email"],
          email_subject="New campaign pricing request from the MOD Media website", email_content="[all-fields]",
          custom_messages="yes", success_message="Thanks! We received your request and will send your campaign plan and pricing soon.",
          error_message="Something went wrong. Please call or text (469) 279-2511.",
          required_field_message="This field is required.", invalid_message="Please check this field.",
          column_gap=px(14), row_gap=px(16), label_spacing=px(8),
          field_text_color="#EEF2FB", field_background_color="#0A0F1E", field_border_color="#26304A", field_border_width=box(1),
          field_border_radius=box(12), label_color="#9AA6C2",
          label_typography_typography="custom", label_typography_font_family="Inter", label_typography_font_weight="600",
          label_typography_font_size=px(12), label_typography_text_transform="uppercase", label_typography_letter_spacing=px(1),
          field_typography_typography="custom", field_typography_font_family="Inter", field_typography_font_size=px(16),
          button_background_color="#2EE6F0", button_text_color="#031317", button_background_hover_color="#7DF3F8", button_hover_color="#031317",
          button_border_radius=box(999), button_text_padding=box(16, 26),
          button_typography_typography="custom", button_typography_font_family="Inter", button_typography_font_weight="700", button_typography_font_size=px(15),
          button_typography_text_transform="none", button_typography_letter_spacing=px(0),
          _title="Quote form")
H.append(section("quote", [
    row([
        con([eyebrow("Request campaign pricing"),
             heading("Let’s put your name in lights.", 'h2', typo='section_h2'),
             text("<p>Tell us what you’re promoting, where and when. We’ll send a custom campaign plan and price.</p>", typo='lede'),
             W_("icon-list", icon_list=[
                 {"_id": nid(), "text": "Call / Text: (469) 279-2511", "selected_icon": {"value": "fas fa-phone", "library": "fa-solid"}, "link": {"url": "tel:+14692792511"}},
                 {"_id": nid(), "text": "info@modmediaads.com", "selected_icon": {"value": "fas fa-envelope", "library": "fa-solid"}, "link": {"url": "mailto:info@modmediaads.com"}},
                 {"_id": nid(), "text": "Based in Dallas–Fort Worth, Texas", "selected_icon": {"value": "fas fa-map-marker-alt", "library": "fa-solid"}}],
                icon_size=px(16), text_indent=px(12), space_between=px(14), _margin=box(18, 0, 0, 0),
                __globals__={"icon_color": C('primary'), "text_color": C('text'), "icon_typography_typography": TY('text')})],
            width=px(42, '%'), width_tablet=px(100, '%'), padding=box(0), flex_gap=gap(18), flex_align_items="flex-start"),
        con([heading("What kind of campaign?", 'h3', typo='card_h3', _margin=box(0, 0, 6, 0)), form],
            width=px(58, '%'), width_tablet=px(100, '%'), padding=box(34), padding_mobile=box(24, 18), flex_gap=gap(10),
            background_background="classic", background_color="#111830E6", border_border="solid", border_width=box(1),
            border_color="rgba(46,230,240,0.25)", border_radius=box(22),
            box_shadow_box_shadow_type="yes", box_shadow_box_shadow={"horizontal": 0, "vertical": 30, "blur": 80, "spread": -30, "color": "rgba(0,0,0,0.8)"}),
    ], g=56, align='flex-start', flex_direction_tablet="column"),
], bg='bg_alt', _title="Quote", background_background="gradient", background_color="#0F2633", background_color_stop=px(0, '%'),
   background_color_b="#0B1020", background_color_b_stop=px(60, '%'), background_gradient_type="radial",
   background_gradient_position="top right", border_border="solid", border_width=box(1, 0, 0, 0), border_color="#FFFFFF17"))
# the quote heading duplicates the form question; remove the h3 (form fields carry the label)
H[-1]["elements"][0]["elements"][1]["elements"].pop(0)

# ================= HEADER =================
HEADER = [con([
    W_("image", image=img('mod-media-logo'), image_size="full", width=px(214), width_mobile=px(170), link_to="custom",
       link={"url": "/", "is_external": "", "nofollow": ""}, _title="Logo"),
    W_("nav-menu", menu="main-menu", layout="horizontal", align_items="center", pointer="underline", animation_line="fade",
       dropdown="tablet", toggle="burger", full_width="stretch", text_align="aside",
       color_menu_item="#9AA6C2", color_menu_item_hover="#EEF2FB", pointer_color_menu_item_hover="#2EE6F0",
       color_menu_item_active="#EEF2FB", pointer_color_menu_item_active="#2EE6F0",
       menu_typography_typography="custom", menu_typography_font_family="Inter", menu_typography_font_weight="500", menu_typography_font_size=px(15),
       padding_horizontal_menu_item=px(13), padding_vertical_menu_item=px(10),
       color_dropdown_item="#EEF2FB", background_color_dropdown_item="#0B1020", color_dropdown_item_hover="#031317",
       background_color_dropdown_item_hover="#2EE6F0", toggle_color="#EEF2FB", toggle_background_color="#FFFFFF0F",
       toggle_size=px(22), toggle_border_radius=px(10), dropdown_top_distance=px(16),
       dropdown_typography_typography="custom", dropdown_typography_font_family="Inter", dropdown_typography_font_weight="600", dropdown_typography_font_size=px(16), dropdown_typography_text_transform="none", dropdown_typography_letter_spacing=px(0), padding_vertical_dropdown_item=px(14),
       _flex_size="grow", _title="Main menu"),
    row([heading("(469) 279-2511", 'p', typo='nav', color='text', link="tel:+14692792511", hide_tablet="hidden-tablet", hide_mobile="hidden-mobile"),
         button("Get Pricing", "#quote", size="sm", text_padding=box(12, 20), hide_mobile="hidden-mobile")],
        g=14, align='center', mobile_col=False, width=px(100, '%'), _element_width="initial", width_tablet={"unit": "%", "size": "", "sizes": []},
        flex_justify_content="flex-end"),
], content_width="boxed", flex_direction="row", flex_direction_mobile="row", flex_justify_content="space-between", flex_align_items="center",
   flex_gap=gap(20), min_height=px(74), padding=box(0, 20), padding_mobile=box(0, 16), _title="Header",
   background_background="classic", background_color="#06080FEB", border_border="solid", border_width=box(0, 0, 1, 0), border_color="#FFFFFF17",
   sticky="top", sticky_on=["desktop", "tablet", "mobile"], sticky_offset=0, sticky_effects_offset=0, z_index=99)]
# header right group should not stretch full width
HEADER[0]["elements"][2]["settings"].update({"width": px(250), "width_tablet": px(130), "_flex_size": "none", "hide_mobile": "hidden-mobile"})

# ================= FOOTER =================
def flink(items):
    return W_("icon-list", icon_list=[{"_id": nid(), "text": t, "selected_icon": {"value": "", "library": ""}, "link": {"url": u}} for t, u in items],
              space_between=px(10), __globals__={"text_color": C('muted'), "text_color_hover": C('text'), "icon_typography_typography": TY('small')})
def fcol(title, items, w=19):
    return con([heading(title, 'p', typo='accent', color='text'), flink(items)], width=px(w, '%'), width_tablet=px(46, '%'), width_mobile=px(100, '%'),
               padding=box(0), flex_gap=gap(14))
FOOTER = [con([
    row([
        con([W_("image", image=img('mod-media-logo'), image_size="full", width=px(214), align="left", link_to="custom", link={"url": "/"}),
             text("<p>Family-owned mobile LED billboard truck advertising company based in Dallas–Fort Worth, running campaigns across Texas and nationwide.</p>",
                  typo='small', color='muted', _element_width="initial", _element_custom_width=px(320), _element_width_mobile="inherit")],
            width=px(31, '%'), width_tablet=px(100, '%'), padding=box(0), flex_gap=gap(16)),
        fcol("Campaigns", [("Daily Campaigns", "/#services"), ("Weekly Campaigns", "/#services"), ("Monthly Campaigns", "/#services"), ("Multi-City &amp; Agency", "/#services")]),
        fcol("Cities", [("Dallas–Fort Worth", "/#markets"), ("Houston", "/#markets"), ("Austin", "/#markets"), ("San Antonio", "/#markets"), ("Nationwide", "/#markets")]),
        fcol("Contact", [("(469) 279-2511", "tel:+14692792511"), ("info@modmediaads.com", "mailto:info@modmediaads.com"), ("181 County Line Road, Rockwall, TX 75032", "")]),
    ], g=30, wrap=True, flex_wrap_tablet="wrap"),
    row([text("<p>© 2026 MOD Media</p>", typo='small', color='muted'), text("<p>Website by Jayce Cabangcala</p>", typo='small', color='muted')],
        g=12, align='center', justify='space-between', padding=box(24, 0, 0, 0), border_border="solid", border_width=box(1, 0, 0, 0),
        border_color="#FFFFFF17", _margin=box(40, 0, 0, 0)),
], content_width="boxed", _title="Footer", padding=box(60, 20, 40, 20), padding_mobile=box(48, 16, 110, 16),
   background_background="classic", border_border="solid", border_width=box(1, 0, 0, 0), border_color="#FFFFFF17",
   __globals__={"background_color": C('bg_main')}),
    con([button("Call", "tel:+14692792511", style='ghost', size="sm", _element_width="initial", _element_custom_width=px(25, '%'), align="justify"),
         button("Text", "sms:+14692792511", style='ghost', size="sm", _element_width="initial", _element_custom_width=px(25, '%'), align="justify"),
         button("Get Pricing", "#quote", size="sm", _flex_grow=1, _flex_size="grow", align="justify")],
        _title="Mobile action bar", flex_direction="row", flex_direction_mobile="row", flex_gap=gap(8), padding=box(10, 12),
        background_background="classic", background_color="#06080FEB", border_border="solid", border_width=box(1, 0, 0, 0), border_color="#FFFFFF17",
        hide_desktop="hidden-desktop", hide_tablet="hidden-tablet", sticky="bottom", sticky_on=["mobile"], z_index=99)]

def mark(els):
    for e in els:
        for ch in e["elements"]:
            if ch["elType"] == "container": ch["isInner"] = True
        mark(e["elements"])
mark(H); mark(HEADER); mark(FOOTER)
json.dump({"home": H, "header": HEADER, "footer": FOOTER}, open('built.json', 'w'))
print('home sections', len(H), 'size', len(json.dumps(H)) // 1024, 'KB')
