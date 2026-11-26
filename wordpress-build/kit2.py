"""Exact design-system values from the reference CSS (ref.css)."""
import json
from wp import req

def px(n, u='px'): return {"unit": u, "size": n, "sizes": []}
def T(_id, title, fam, w, size, lh, ls=None, tt='none', extra=None):
    t = {"_id": _id, "title": title, "typography_typography": "custom", "typography_font_family": fam,
         "typography_font_weight": str(w), "typography_font_size": size,
         "typography_line_height": px(lh, 'em'), "typography_text_transform": tt,
         "typography_letter_spacing": ls if ls is not None else px(0)}
    if extra: t.update(extra)
    return t
CUST = lambda v: {"unit": "custom", "size": v, "sizes": []}

s, r = req('GET', '/wp/v2/elementor_library/6?context=edit'); ps = r['meta']['_elementor_page_settings']

ps['system_typography'] = [
    T('primary', 'Headings', 'Plus Jakarta Sans', 800, px(54), 1.08, px(-0.025, 'em')),
    T('secondary', 'Subheadings', 'Plus Jakarta Sans', 800, px(21), 1.25, px(-0.01, 'em')),
    T('text', 'Body', 'Inter', 400, px(16), 1.65),
    T('accent', 'Eyebrow', 'Inter', 700, px(12), 1, px(0.16, 'em'), 'uppercase'),
]
ps['custom_typography'] = [
    T('hero_h1', 'Hero H1', 'Plus Jakarta Sans', 800, CUST('clamp(42px,6vw,78px)'), 1.02, px(-0.035, 'em')),
    T('section_h2', 'Section H2', 'Plus Jakarta Sans', 800, CUST('clamp(32px,4.4vw,54px)'), 1.08, px(-0.025, 'em')),
    T('card_h3', 'Card H3', 'Plus Jakarta Sans', 800, px(21), 1.25, px(-0.01, 'em')),
    T('lede', 'Lead Paragraph', 'Inter', 400, px(18), 1.65),
    T('small', 'Small Text', 'Inter', 400, px(14), 1.65),
    T('card_p', 'Card Text', 'Inter', 400, px(15), 1.65),
    T('tag', 'Card Tag', 'Inter', 700, px(11), 1, px(0.16, 'em'), 'uppercase'),
    T('button', 'Button', 'Inter', 700, px(15), 1),
    T('nav', 'Navigation', 'Inter', 500, px(15), 1.65),
]
ps['default_generic_fonts'] = 'system-ui, -apple-system, Segoe UI, Roboto, sans-serif'
ps.setdefault('__globals__', {})['button_hover_background_color'] = 'globals/colors?id=primary'
ps['container_width'] = px(1160)
ps['container_padding'] = {"unit": "px", "top": "0", "right": "20", "bottom": "0", "left": "20", "isLinked": False}
ps['space_between_widgets'] = {"column": "0", "row": "0", "isLinked": True, "unit": "px", "size": 0}
# Reference breakpoints: <=1000px and <=640px
ps['viewport_tablet'] = 1000; ps['viewport_mobile'] = 640
ps['viewport_md'] = 641; ps['viewport_lg'] = 1001
ps['active_breakpoints'] = ['viewport_mobile', 'viewport_tablet']

# Global utility classes for effects Elementor has no control for (pseudo-elements, glows, hover lifts).
ps['custom_css'] = r"""/* ---- MOD Media utility classes (mirror the reference design) ---- */
:root{color-scheme:dark}
h1.elementor-heading-title,h2.elementor-heading-title,h3.elementor-heading-title{text-wrap:balance}
.elementor-widget-heading p.elementor-heading-title{margin:0}
.elementor-kit-6 .elementor-element .elementor-button:focus-visible{outline:3px solid #2EE6F0;outline-offset:3px}
/* eyebrow with glowing dot */
.mm-eyebrow .elementor-heading-title{display:flex;align-items:center;gap:10px}
.mm-eyebrow .elementor-heading-title::before{content:"";flex:none;width:8px;height:8px;border-radius:50%;background:#2EE6F0;box-shadow:0 0 12px #2EE6F0}
/* primary button glow + lift */
.mm-btn .elementor-button{transition:transform .2s ease,box-shadow .2s ease,background .2s ease;box-shadow:0 10px 40px -10px rgba(46,230,240,.7)}
.mm-btn .elementor-button:hover{transform:translateY(-2px);box-shadow:0 14px 50px -10px rgba(46,230,240,.9)}
.mm-ghost .elementor-button{transition:background .2s ease}
/* hero */
.mm-hero::before{content:"";position:absolute;inset:0;z-index:0;pointer-events:none;background:radial-gradient(1200px 500px at 70% 30%,rgba(46,230,240,.16),transparent 60%),radial-gradient(800px 400px at 10% 90%,rgba(255,61,139,.14),transparent 60%),linear-gradient(180deg,rgba(6,8,15,.2) 0%,rgba(6,8,15,.75) 60%,#06080F 100%)}
.mm-hero>.e-con-inner{position:relative;z-index:1}
.mm-hero .mm-glow{color:#2EE6F0;text-shadow:0 0 30px rgba(46,230,240,.55),0 0 80px rgba(46,230,240,.35)}
.mm-ticks .elementor-icon-list-items{row-gap:10px}
.mm-ticks .elementor-icon-list-icon{display:none!important}
.mm-ticks .elementor-icon-list-item{gap:8px}
.mm-ticks .elementor-icon-list-item::before{content:"";flex:none;width:16px;height:16px;border-radius:50%;box-sizing:border-box;background:rgba(46,230,240,.14);border:1px solid rgba(46,230,240,.5);box-shadow:inset 0 0 0 3px #06080F,inset 0 0 0 10px #2EE6F0}
/* header */
.mm-header{backdrop-filter:saturate(160%) blur(14px);-webkit-backdrop-filter:saturate(160%) blur(14px)}
.mm-header .elementor-nav-menu--main .elementor-item{position:relative;transition:color .2s}
.mm-header .elementor-nav-menu--main .elementor-item.mm-active{color:#EEF2FB!important}
.mm-header .elementor-nav-menu--main .elementor-item.mm-active::after{content:""!important;display:block!important;position:absolute!important;left:14px!important;right:14px!important;top:auto!important;bottom:0!important;width:auto!important;height:2px!important;border-radius:2px;background:#2EE6F0!important;box-shadow:0 0 8px #2EE6F0;opacity:1!important;transform:none!important;z-index:2}
/* brand strip marquee */
.mm-strip .swiper-wrapper{transition-timing-function:linear!important}
.mm-strip .swiper-slide{display:grid;place-items:center;height:56px}
.mm-strip .swiper-slide img{max-height:38px!important;width:auto!important;max-width:100%;object-fit:contain;opacity:.7;margin:0 auto}
/* service cards */
.mm-svc{overflow:hidden;transition:transform .3s ease,border-color .3s ease}
.mm-svc:hover{transform:translateY(-6px)}
.mm-svc::after{content:"";position:absolute;right:-40%;bottom:-60%;width:260px;height:260px;border-radius:50%;background:radial-gradient(circle,rgba(46,230,240,.16),transparent 70%);opacity:.4;transition:opacity .3s;pointer-events:none}
.mm-svc:hover::after{opacity:1}
/* brand wall glass tiles */
.mm-lt{position:relative;display:grid!important;place-items:center;min-height:130px;border-radius:18px;background:linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,.015));border:1px solid rgba(255,255,255,.09);box-shadow:inset 0 1px 0 rgba(255,255,255,.06);transition:transform .35s,box-shadow .35s,border-color .35s}
.mm-lt::before{content:"";position:absolute;inset:0;border-radius:inherit;background:radial-gradient(60% 70% at 50% 50%,rgba(46,230,240,.18),transparent 70%);opacity:0;transition:opacity .35s}
.mm-lt:hover{transform:translateY(-4px);border-color:rgba(46,230,240,.55);box-shadow:0 18px 50px -20px rgba(46,230,240,.6)}
.mm-lt:hover::before{opacity:1}
.mm-lt img{position:relative;z-index:1;width:auto!important;height:auto!important;max-width:66%!important;max-height:60px!important;object-fit:contain;opacity:.78;transition:opacity .35s,filter .35s}
.mm-lt.wide img{max-width:74%!important;max-height:38px!important}
.mm-lt.tall img{max-height:74px!important}
.mm-lt:hover img{opacity:1;filter:drop-shadow(0 0 10px rgba(46,230,240,.55))}
/* gallery figures with caption pills */
.mm-gfig{overflow:hidden}
.mm-gfig .elementor-widget-container,.mm-gfig figure,.mm-gfig a{display:block;height:100%;margin:0;position:relative}
.mm-gfig img{width:100%!important;object-fit:cover;display:block;transition:transform .6s ease;cursor:zoom-in}
.mm-gfig:hover img{transform:scale(1.05)}
.mm-gfig .widget-image-caption{position:absolute!important;left:12px;bottom:12px;margin:0!important;font:600 11px/1 Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif!important;letter-spacing:.1em!important;text-transform:uppercase!important;padding:8px 10px!important;border-radius:999px;background:rgba(6,8,15,.75)!important;backdrop-filter:blur(6px);color:#EEF2FB!important;text-align:left!important}
/* industry chips */
.mm-inds .elementor-icon-list-items{gap:12px}
.mm-inds .elementor-icon-list-item{margin:0!important;padding:14px 20px!important;border:1px solid rgba(255,255,255,.09);border-radius:999px;background:rgba(255,255,255,.03)}
.mm-inds .elementor-icon-list-item::after{display:none!important}
/* reviews */
.mm-rvsum{background:radial-gradient(420px 260px at 0% 0%,rgba(46,230,240,.28),transparent 60%),radial-gradient(420px 300px at 100% 100%,rgba(255,61,139,.25),transparent 60%),#0F1529!important}
.mm-av{flex:none}
.mm-av .elementor-heading-title{display:grid;place-items:center;width:100%;height:100%}
.mm-avs>.mm-av+.mm-av{margin-left:-10px!important}
.mm-rcard{overflow:hidden;transition:border-color .4s,box-shadow .4s}
.mm-rcard::before{content:"\201C"!important;display:block!important;position:absolute!important;left:auto!important;right:18px!important;top:-24px!important;width:auto!important;height:auto!important;opacity:1!important;mix-blend-mode:normal!important;background:none!important;border:0!important;box-shadow:none!important;border-radius:0!important;font:800 170px/1 "Plus Jakarta Sans",Inter,system-ui,-apple-system,"Segoe UI",sans-serif;color:rgba(46,230,240,.12);pointer-events:none;z-index:0}
.mm-rv .swiper-button-disabled{opacity:1!important}
.mm-rv .swiper-slide-active .mm-rcard,.mm-rv .swiper-slide-active>.mm-rcard{border-color:rgba(46,230,240,.55)!important;box-shadow:0 20px 60px -24px rgba(46,230,240,.55)}
.mm-who p{margin:0}
.mm-who strong{display:block;font-weight:700;color:#9AA6C2;font-size:14px}
.mm-who span{display:block;font-size:14px;color:#9AA6C2}
.mm-rv .e-n-carousel{padding:4px 2px 74px!important}
.mm-rv .swiper-pagination{position:absolute!important;text-align:left;top:386px!important;bottom:auto!important;left:0!important;right:auto!important;width:auto!important;transform:none!important;display:flex;gap:8px;line-height:0}
.mm-rv .swiper-pagination-bullet{width:8px!important;height:8px!important;border-radius:999px!important;background:#2A3246!important;opacity:1!important;margin:0!important;transition:width .3s,background .3s}
.mm-rv .swiper-pagination-bullet-active{width:26px!important;background:#2EE6F0!important;box-shadow:0 0 10px #2EE6F0}
.mm-rv .elementor-swiper-button{position:absolute!important;top:366px!important;bottom:auto!important;transform:none!important;width:48px!important;height:48px!important;box-sizing:border-box;border-radius:50%!important;display:grid!important;place-items:center;border:1px solid rgba(255,255,255,.09)!important;background:rgba(255,255,255,.04)!important;color:#EEF2FB!important;font-size:18px!important}
.mm-rv .elementor-swiper-button svg{width:18px;height:18px;fill:#EEF2FB}
.mm-rv .elementor-swiper-button:hover{border-color:#2EE6F0!important}
.mm-rv .elementor-swiper-button-prev{left:auto!important;right:58px!important}
.mm-rv .elementor-swiper-button-next{right:0!important;left:auto!important}
/* feature band */
.mm-feat::before{content:"";position:absolute;inset:0;z-index:0;pointer-events:none;background:linear-gradient(90deg,rgba(6,8,15,.96) 0%,rgba(6,8,15,.8) 40%,rgba(6,8,15,.1) 100%)}
.mm-feat>.e-con-inner{position:relative;z-index:1}
/* faq */
.mm-faq .elementor-accordion-item{border:1px solid rgba(255,255,255,.09)!important;border-radius:14px;background:#0B1020;padding:4px 22px;margin-bottom:12px;overflow:hidden}
.mm-faq .elementor-accordion-item:last-of-type{margin-bottom:0}
.mm-faq .elementor-tab-title{padding:18px 0!important;border:0!important;background:none!important}
.mm-faq .elementor-tab-content{padding:0 0 20px!important;border:0!important;background:none!important}
.mm-faq .elementor-tab-content p{max-width:70ch;margin:0}
.mm-faq .elementor-accordion-icon{font-size:13px;line-height:28px}
.mm-faq .elementor-accordion-icon svg{width:13px;height:13px}
/* quote */
.mm-quote{background:radial-gradient(900px 400px at 85% 0%,rgba(46,230,240,.18),transparent 60%),radial-gradient(700px 400px at 0% 100%,rgba(255,61,139,.16),transparent 60%),#0B1020!important}
.mm-qform{margin-bottom:16px!important}
.mm-qform .elementor-form-fields-wrapper{margin-bottom:0!important}
.mm-qform .mm-fh{margin:0;font:800 24px/1.25 "Plus Jakarta Sans",Inter,system-ui,-apple-system,"Segoe UI",sans-serif;letter-spacing:-.01em;color:#EEF2FB}
.mm-qform .elementor-field-group-campaign>.elementor-field-label{display:none}
.mm-qform .elementor-field-group-campaign .elementor-field-subgroup{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;width:100%}
@media(max-width:640px){.mm-qform .elementor-field-group-campaign .elementor-field-subgroup{grid-template-columns:1fr}}
.mm-qform .elementor-field-group-campaign .elementor-field-option{position:relative;margin:0!important;padding:0!important;width:auto!important}
.mm-qform .elementor-field-group-campaign input{position:absolute;opacity:0}
.mm-qform .elementor-field-group-campaign .elementor-field-option label{display:block!important;cursor:pointer;padding:16px!important;border-radius:12px;border:1px solid rgba(255,255,255,.09);background:rgba(255,255,255,.03);font:600 15px/1.65 Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif!important;color:#EEF2FB!important;letter-spacing:0!important;text-transform:none!important;transition:border-color .2s,background .2s}
.mm-qform .elementor-field-group-campaign .elementor-field-option label::after{display:block;font-weight:500;color:#9AA6C2;font-size:13px;margin-top:4px;line-height:1.65}
.mm-qform .elementor-field-group-campaign .elementor-field-option:nth-child(1) label::after{content:"Launches, events, activations"}
.mm-qform .elementor-field-group-campaign .elementor-field-option:nth-child(2) label::after{content:"Promotions & seasonal pushes"}
.mm-qform .elementor-field-group-campaign .elementor-field-option:nth-child(3) label::after{content:"Sustained brand awareness"}
.mm-qform .elementor-field-group-campaign .elementor-field-option:nth-child(4) label::after{content:"Texas & nationwide"}
.mm-qform .elementor-field-group-campaign input:checked+label{border-color:#2EE6F0;background:rgba(46,230,240,.14)}
.mm-qform .elementor-field-group-campaign input:focus-visible+label{outline:2px solid #2EE6F0;outline-offset:2px}
.mm-qform .elementor-field-textual,.mm-qform select{padding:14px 16px!important;min-height:0!important;font-weight:500}
.mm-qform .elementor-field-textual{line-height:normal!important}
.mm-qform select.elementor-field-textual{appearance:auto!important;-webkit-appearance:menulist!important}
.mm-qform .select-caret-down-wrapper{display:none!important}
.mm-qform .elementor-field-group>.elementor-field-label{line-height:normal!important}
.mm-qform .elementor-field:focus{border-color:#2EE6F0!important;box-shadow:0 0 0 3px rgba(46,230,240,.14)!important;outline:none}
.mm-qform .e-form__indicators{margin:0 0 22px!important;padding:0!important}
.mm-qform .e-form__indicators__indicator__progress{height:4px;border-radius:4px;background:linear-gradient(90deg,#26304A calc(50% - 4px),transparent calc(50% - 4px),transparent calc(50% + 4px),#26304A calc(50% + 4px))}
.mm-qform .e-form__indicators__indicator__progress__meter{height:4px!important;border-radius:4px;background:#2EE6F0!important;box-shadow:0 0 10px #2EE6F0;font-size:0!important;line-height:0!important;color:transparent!important;padding:0!important;text-indent:-9999px;overflow:hidden}
.mm-qform .e-form__buttons{display:flex!important;justify-content:flex-end!important;flex-wrap:wrap;gap:12px;width:100%!important;flex:0 0 100%!important;max-width:100%!important}
.mm-qform .e-form__buttons__wrapper{flex:none!important;width:auto!important;padding:0!important;margin:0!important}
.mm-qform .e-form__buttons__wrapper:has(.e-form__buttons__wrapper__button-previous){margin-right:auto!important}
.mm-qform .elementor-button{border-radius:999px!important;padding:16px 26px!important;font:700 15px/1 Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif!important;text-transform:none!important;letter-spacing:0!important;min-height:0!important;box-shadow:0 10px 40px -10px rgba(46,230,240,.7)}
.mm-qform .e-form__buttons__wrapper__button-previous{background:rgba(255,255,255,.06)!important;color:#EEF2FB!important;border:1px solid rgba(255,255,255,.09)!important;box-shadow:none!important}
.mm-qform .elementor-message{font-size:16px;color:#C8D1E6}
/* contact lines */
.mm-cl a{text-decoration:underline}
/* footer */
.mm-foot a:hover,.mm-foot .elementor-icon-list-item a:hover .elementor-icon-list-text{color:#EEF2FB!important}
"""
st, res = req('POST', '/wp/v2/elementor_library/6', {"meta": {"_elementor_page_settings": ps}})
print(st, 'kit saved' if st == 200 else str(res)[:300])
