import json, sys
from wp import req
B = json.load(open('built.json'))
st = json.load(open('state.json')) if __import__('os').path.exists('state.json') else {}
def save(): json.dump(st, open('state.json','w'), indent=1)

def guard(path, key):
    """Refuse to overwrite a document someone edited in Elementor since our last publish."""
    if key not in st: return
    s, r = req('GET', f"{path}/{st[key]}?context=edit&_fields=modified_gmt")
    last = st.get(key + '_modified')
    if last and r.get('modified_gmt') != last:
        raise SystemExit(f"STOP: {path}/{st[key]} was edited since our last publish ({last} -> {r.get('modified_gmt')}). Merge the edit first.")
def remember(path, key):
    s, r = req('GET', f"{path}/{st[key]}?context=edit&_fields=modified_gmt"); st[key + '_modified'] = r.get('modified_gmt'); save()
# Home page
body = {"title":"Home","status":"publish","template":"elementor_header_footer",
        "meta":{"_elementor_edit_mode":"builder","_elementor_template_type":"wp-page",
                "_elementor_data":json.dumps(B['home']),"_elementor_page_settings":{"hide_title":"yes"}}}
guard('/wp/v2/pages', 'home')
if 'home' in st: s,r = req('POST', f"/wp/v2/pages/{st['home']}", body)
else:
    s,r = req('POST', "/wp/v2/pages", body); st['home']=r.get('id') if isinstance(r,dict) else None
print('home', s, st.get('home')); save(); remember('/wp/v2/pages', 'home')
for key,typ in (('header','header'),('footer','footer')):
    body = {"title":f"MOD Media {typ.title()}","status":"publish",
            "meta":{"_elementor_edit_mode":"builder","_elementor_template_type":typ,"_elementor_data":json.dumps(B[key])}}
    guard('/wp/v2/elementor_library', key)
    if key in st: s,r = req('POST', f"/wp/v2/elementor_library/{st[key]}", body)
    else:
        s,r = req('POST', "/wp/v2/elementor_library", body); st[key]=r.get('id') if isinstance(r,dict) else None
    print(key, s, st.get(key), '' if s<300 else str(r)[:300]); save(); remember('/wp/v2/elementor_library', key)
