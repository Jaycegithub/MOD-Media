import re,json
T=open('../concept/template.html').read()
M=json.load(open('media.json'))
css=T[T.index('<style>')+7:T.index('</style>')]
css=re.sub(r'/\*.*?\*/','',css,flags=re.S)
# split top-level statements
def split(s):
    out=[];i=0;depth=0;start=0
    while i<len(s):
        c=s[i]
        if c=='{': depth+=1
        elif c=='}':
            depth-=1
            if depth==0: out.append(s[start:i+1].strip()); start=i+1
        i+=1
    return [x for x in out if x]
stmts=split(css)
KF={}
for st in stmts:
    if st.startswith('@keyframes'): KF[st.split()[1].split('{')[0]]=st
def pre_sel(sel):
    parts=[]
    for p in sel.split(','):
        p=p.strip()
        if p in (':root','html','body','*,*::before,*::after','*'): parts.append('.mmx' if p!='*' else '.mmx *'); continue
        parts.append('.mmx '+p)
    return ','.join(parts)
def keep(sel,keys):
    return any(re.search(k,sel) for k in keys)
def prefix_rule(rule,keys):
    sel,body=rule.split('{',1)
    sel=sel.strip()
    if not keep(sel,keys): return None
    return pre_sel(sel)+'{'+body
def build(keys,kfs):
    out=[]
    for st in stmts:
        if st.startswith('@keyframes'): continue
        if st.startswith('@media'):
            head,inner=st.split('{',1); inner=inner[:-1]
            rs=[prefix_rule(r,keys) for r in split(inner)]
            rs=[r for r in rs if r]
            if rs: out.append(head+'{'+''.join(rs)+'}')
        elif not st.startswith('@'):
            r=prefix_rule(st,keys)
            if r: out.append(r)
    for k in kfs: out.append(KF[k].replace('@keyframes '+k,'@keyframes mmx-'+k))
    s='\n'.join(out)
    for k in kfs: s=re.sub(r'(animation:[^;}]*?)\b'+k+r'\b',r'\1mmx-'+k,s)
    return s
root=re.search(r':root\{(.*?)\}',css,re.S).group(1)
BASE='.mmx{'+root+';color:var(--text);font-family:var(--body)}\n.mmx *{box-sizing:border-box}\n.mmx button{font-family:inherit}\n@media (prefers-reduced-motion:reduce){.mmx *,.mmx *::before,.mmx *::after{animation:none!important;transition:none!important}}'
TRUCK_K=[r'\.truck',r'\.screen',r'\.slide',r'\.hx',r'\.cab',r'\.chassis',r'\.wheel',r'\.road',r'\.dots',r'\.beam',r'\.rig']
BUILD_K=[r'\.builder',r'\.bpanel',r'\.swatches',r'\.sw\b',r'\.toggles',r'\.tg\b',r'\.counter',r'\.stage',r'\.ad\b',r'\.upl',r'\.field',r'\.screen(?!-caption)',r'\.truck-body',r'\.btn']
FIND_K=[r'\.finder',r'\.qblock',r'\.chips',r'\.pick',r'\.result',r'\.pop\b',r'\.btn']
truck_css=build(TRUCK_K,['hxIn','float','spin','pulse','flicker','kb','stripes','fall'])
build_css=build(BUILD_K,['flash','crawl'])
find_css=build(FIND_K,['pop'])
# HTML
def between(a,b,start=0):
    i=T.index(a,start); j=T.index(b,i); return T[i:j]
truck_html=between('<div class="truck hx"','\n  </div>\n</section>')
truck_html=truck_html.replace("{{frisco}}",M['mod-media-frisco-legacy-aerial']['url']).replace("{{fleet}}",M['mod-media-led-billboard-truck-fleet']['url'])
bs=T.index('<section id="try"'); builder_html=between('<div class="builder">','\n  </div>\n</section>',bs)
fs=T.index('<section id="finder"'); finder_html=between('<div class="finder">','\n  </div>\n</section>',fs)
assert '{{' not in truck_html+builder_html+finder_html, re.findall(r'\{\{\w+\}\}',truck_html+builder_html+finder_html)
js=T[T.index('<script>\n')+9:T.index('</script>')]
def jsblock(start_marker):
    i=js.index(start_marker); j=js.index('\n// ',i+5); return js[i:j]
RM="var RM=window.matchMedia('(prefers-reduced-motion: reduce)').matches;"
truck_js=jsblock('// LED screen slideshow')
builder_js=js[js.index('// Ad builder'):js.index('// Campaign planner')]
planner_js=js[js.index('// Campaign planner'):js.index('// Gallery lightbox')]
useAd="document.getElementById('useAd').addEventListener('click',function(){var parts=[];if(adState.showHead&&document.getElementById('adHead').value)parts.push(document.getElementById('adHead').value);if(adState.showSub&&document.getElementById('adSub').value)parts.push(document.getElementById('adSub').value);var m='Ad message: '+parts.join(' — ');if(adState.img)m+=' (I have my own background image to send)';var f=document.getElementById('form-field-message');if(f){f.value=m;}});"
planner_js=planner_js.replace("var o=(ans.goal==='multi'||ans.goal==='national')?'o4':g.opt;document.getElementById(o).checked=true;var c=document.getElementById('city');c.value={dfw:'Dallas–Fort Worth',texas:'Houston',multi:'Several cities',national:'Outside Texas'}[ans.goal];",
 "var camp={o1:'Daily campaign',o2:'Weekly campaign',o3:'Monthly campaign',o4:'Multi-city / agency campaign'}[(ans.goal==='multi'||ans.goal==='national')?'o4':g.opt];var s=document.getElementById('form-field-campaign');if(s)s.value=camp;var c=document.getElementById('form-field-area');if(c)c.value={dfw:'Dallas–Fort Worth',texas:'Houston',multi:'Several cities',national:'Outside Texas'}[ans.goal];")
assert 'form-field-campaign' in planner_js
def wrap(cid,css_,html,jsx):
    return f'<style>{BASE}\n{css_}</style>\n<div class="mmx" id="{cid}">\n{html}\n</div>\n<script>(function(){{{RM}\n{jsx}\n}})();</script>'
W={'truck':wrap('mmx-truck',truck_css,truck_html,truck_js),
   'builder':wrap('mmx-builder',build_css,builder_html,builder_js+'\n'+useAd),
   'finder':wrap('mmx-finder',find_css,finder_html,planner_js)}
json.dump(W,open('html_widgets.json','w'))
for k,v in W.items(): print(k,len(v)//1024,'KB')
