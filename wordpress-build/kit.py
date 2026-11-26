import json,sys
sys.path.insert(0,'.')
from wp import req
px=lambda n:{"unit":"px","size":n,"sizes":[]}
em=lambda n:{"unit":"em","size":n,"sizes":[]}
def typo(fam,w,size=None,lh=None,ls=None,tr=None,ts=None,ms=None,lhu='em'):
    d={"typography_typography":"custom","typography_font_family":fam,"typography_font_weight":str(w)}
    if size: d["typography_font_size"]=px(size)
    if ts: d["typography_font_size_tablet"]=px(ts)
    if ms: d["typography_font_size_mobile"]=px(ms)
    if lh: d["typography_line_height"]={"unit":lhu,"size":lh,"sizes":[]}
    if ls is not None: d["typography_letter_spacing"]=px(ls)
    if tr: d["typography_text_transform"]=tr
    return d
def T(_id,title,**kw):
    d={"_id":_id,"title":title}; d.update(typo(**kw)); return d
S={
 "system_colors":[
   {"_id":"primary","title":"Primary (LED Cyan)","color":"#2EE6F0"},
   {"_id":"secondary","title":"Secondary (Pink)","color":"#FF3D8B"},
   {"_id":"text","title":"Text","color":"#EEF2FB"},
   {"_id":"accent","title":"Accent (Amber)","color":"#FFC24B"}],
 "custom_colors":[
   {"_id":"bg_main","title":"Background (Night)","color":"#06080F"},
   {"_id":"bg_alt","title":"Alt Background","color":"#0B1020"},
   {"_id":"panel","title":"Card / Panel","color":"#111830"},
   {"_id":"muted","title":"Secondary Text","color":"#9AA6C2"},
   {"_id":"border","title":"Border / Divider","color":"#FFFFFF17"},
   {"_id":"btn_text","title":"Button Text (Dark)","color":"#031317"},
   {"_id":"cyan_soft","title":"Cyan Soft","color":"#2EE6F024"},
   {"_id":"cyan_hover","title":"Button Hover","color":"#7DF3F8"},
   {"_id":"ghost","title":"Ghost Button","color":"#FFFFFF0F"}],
 "system_typography":[
   T("primary","Headings",fam="Plus Jakarta Sans",w=800,lh=1.08,ls=-1),
   T("secondary","Subheadings",fam="Plus Jakarta Sans",w=700,lh=1.25),
   T("text","Body",fam="Inter",w=400,size=16,lh=1.65),
   T("accent","Labels",fam="Inter",w=700,size=12,ls=2,tr="uppercase",lh=1)],
 "custom_typography":[
   T("hero_h1","Hero H1",fam="Plus Jakarta Sans",w=800,size=78,ts=56,ms=42,lh=1.02,ls=-2.5),
   T("section_h2","Section H2",fam="Plus Jakarta Sans",w=800,size=54,ts=42,ms=32,lh=1.08,ls=-1.3),
   T("card_h3","Card H3",fam="Plus Jakarta Sans",w=800,size=21,lh=1.25,ls=-0.2),
   T("lede","Lead Paragraph",fam="Inter",w=400,size=18,ms=16,lh=1.65),
   T("small","Small Text",fam="Inter",w=500,size=14,lh=1.5),
   T("button","Button",fam="Inter",w=700,size=15,lh=1),
   T("nav","Navigation",fam="Inter",w=500,size=15,lh=1)],
 # layout
 "container_width":px(1200),
 "container_padding":{"unit":"px","top":"0","right":"20","bottom":"0","left":"20","isLinked":False},
 "space_between_widgets":{"column":"20","row":"20","isLinked":True,"unit":"px","size":20},
 # background & body
 "body_background_background":"classic","body_background_color":"#06080F",
 "body_color":"#EEF2FB","link_normal_color":"#2EE6F0","link_hover_color":"#7DF3F8",
 "__globals__":{
   "body_background_color":"globals/colors?id=bg_main","body_color":"globals/colors?id=text",
   "link_normal_color":"globals/colors?id=primary","link_hover_color":"globals/colors?id=cyan_hover",
   "body_typography_typography":"globals/typography?id=text",
   "h1_typography_typography":"globals/typography?id=hero_h1","h1_color":"globals/colors?id=text",
   "h2_typography_typography":"globals/typography?id=section_h2","h2_color":"globals/colors?id=text",
   "h3_typography_typography":"globals/typography?id=card_h3","h3_color":"globals/colors?id=text",
   "h4_typography_typography":"globals/typography?id=secondary","h4_color":"globals/colors?id=text",
   "button_typography_typography":"globals/typography?id=button",
   "button_text_color":"globals/colors?id=btn_text","button_background_color":"globals/colors?id=primary",
   "button_hover_text_color":"globals/colors?id=btn_text","button_hover_background_color":"globals/colors?id=cyan_hover",
   "form_label_color":"globals/colors?id=muted","form_field_text_color":"globals/colors?id=text",
   "form_field_background_color":"globals/colors?id=bg_main","form_field_border_color":"globals/colors?id=border",
   "form_field_focus_border_color":"globals/colors?id=primary"},
 # buttons
 "button_background_background":"classic","button_hover_background_background":"classic",
 "button_border_radius":{"unit":"px","top":"999","right":"999","bottom":"999","left":"999","isLinked":True},
 "button_hover_border_radius":{"unit":"px","top":"999","right":"999","bottom":"999","left":"999","isLinked":True},
 "button_padding":{"unit":"px","top":"16","right":"26","bottom":"16","left":"26","isLinked":False},
 # form fields
 "form_field_border_border":"solid","form_field_border_width":{"unit":"px","top":"1","right":"1","bottom":"1","left":"1","isLinked":True},
 "form_field_border_radius":{"unit":"px","top":"12","right":"12","bottom":"12","left":"12","isLinked":True},
 "form_field_padding":{"unit":"px","top":"14","right":"16","bottom":"14","left":"16","isLinked":False},
 "form_label_typography_typography":"custom","form_label_typography_font_family":"Inter","form_label_typography_font_weight":"600",
 "form_label_typography_font_size":px(12),"form_label_typography_text_transform":"uppercase","form_label_typography_letter_spacing":px(1),
 # identity
 "site_name":"MOD Media","site_description":"Mobile LED Billboard Truck Advertising",
 "viewport_md":768,"viewport_lg":1025,
}
st,res=req("POST","/wp/v2/elementor_library/6",{"meta":{"_elementor_page_settings":S}})
print(st, str(res)[:300] if st!=200 else 'kit saved')
st,res=req("GET","/wp/v2/elementor_library/6?context=edit")
ps=res['meta']['_elementor_page_settings']; print('colors:',[c['title'] for c in ps['system_colors']+ps['custom_colors']])
