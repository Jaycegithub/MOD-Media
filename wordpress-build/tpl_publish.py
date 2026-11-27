import json, os
from wp import req
T = json.load(open('templates.json'))
st = json.load(open('tpl_state.json')) if os.path.exists('tpl_state.json') else {}
def save(): json.dump(st, open('tpl_state.json', 'w'), indent=1)
def upsert(key, path, body):
    if key in st: s, r = req('POST', f"{path}/{st[key]}", body)
    else:
        s, r = req('POST', path, body); st[key] = r.get('id') if isinstance(r, dict) else None
    print(key, s, st.get(key), '' if s < 300 else str(r)[:300]); save()
for key, title, typ in (('campaign', 'MOD Media – Campaign page template', 'page'), ('city', 'MOD Media – City page template', 'page'),
                        ('post', 'MOD Media – Blog post template', 'single-post')):
    upsert('lib_' + key, '/wp/v2/elementor_library', {"title": title, "status": "publish", "meta": {
        "_elementor_edit_mode": "builder", "_elementor_template_type": typ, "_elementor_data": json.dumps(T[key])}})
s, r = req('POST', f"/elementor/v1/site-editor/templates-conditions/{st['lib_post']}",
           {"conditions": [{"type": "include", "name": "singular", "sub_name": "post", "sub_id": ""}]})
print('post conditions', s, r)
# temporary previews (deleted after checking)
for key in ('campaign', 'city'):
    upsert('prev_' + key, '/wp/v2/pages', {"title": f"Template preview {key}", "slug": f"tpl-preview-{key}", "status": "publish",
        "template": "elementor_header_footer", "meta": {"_elementor_edit_mode": "builder", "_elementor_template_type": "wp-page",
        "_elementor_data": json.dumps(T[key]), "_elementor_page_settings": {"hide_title": "yes"}}})
sample = ("<p>This is sample text to preview the blog post layout. Real posts replace it.</p>"
          "<h2>A section heading</h2><p>Body text runs at 17px with relaxed spacing so long articles are easy to read on a phone.</p>"
          "<ul><li>A list item</li><li>Another list item</li></ul><h3>A smaller heading</h3><p>A paragraph with a <a href='/get-pricing/'>link</a>.</p>"
          "<blockquote>A pull quote for emphasis.</blockquote>")
upsert('prev_post', '/wp/v2/posts', {"title": "Template preview: how to plan an LED truck campaign", "slug": "tpl-preview-post",
       "status": "publish", "content": sample, "featured_media": 37})
