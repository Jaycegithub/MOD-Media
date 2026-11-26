// node measure.js <width>  -> writes meas_<w>.json with ref/new text metrics per section
const {chromium}=require('playwright');const fs=require('fs');
const W=+process.argv[2]||1440;
const REF='file:///tmp/claude-0/-home-user-MOD-Media/5d839d89-548b-57da-a519-19ed4001428d/scratchpad/concept/mod-media-website-concept.html';
const LIVE='https://healthy-mediumaquamarine-elk-60.hostingersite.com/?v='+Date.now();
async function run(b,url,secSel){
  const p=await b.newPage({viewport:{width:W,height:900},reducedMotion:'reduce'});
  await p.goto(url,{waitUntil:'networkidle',timeout:120000});
  await p.addStyleTag({content:'.ribbon{display:none!important}'});
  await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=500){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,80))}window.scrollTo(0,0)});
  await p.waitForTimeout(1500);
  return await p.evaluate((secSel)=>{
    const secs=[...document.querySelectorAll(secSel)].filter(s=>s.getBoundingClientRect().height>=20);
    return secs.map(s=>{const sr=s.getBoundingClientRect();const cs0=getComputedStyle(s);
      const items=[];
      s.querySelectorAll('*').forEach(e=>{
        if(e.closest('.mmx,.truck,.builder,.finder,.mm-strip,.swiper-slide-duplicate'))return;
        if(['SCRIPT','STYLE','SVG','PATH','svg','path'].includes(e.tagName))return;
        const own=[...e.childNodes].filter(n=>n.nodeType===3).map(n=>n.textContent).join('').replace(/\s+/g,' ').trim();
        if(own.length<2)return;
        const r=e.getBoundingClientRect();if(r.width===0||r.height===0)return;
        const c=getComputedStyle(e);
        // text block: climb to block-level parent for width
        let blk=e;while(blk.parentElement&&getComputedStyle(blk).display==='inline')blk=blk.parentElement;
        const br=blk.getBoundingClientRect();
        items.push({t:own.slice(0,40),x:Math.round(r.left-sr.left),y:Math.round(r.top-sr.top),w:Math.round(br.width),h:Math.round(r.height),
          fs:c.fontSize,fw:c.fontWeight,lh:c.lineHeight,ls:c.letterSpacing,ff:c.fontFamily.split(',')[0].replace(/"/g,''),col:c.color,tt:c.textTransform});
      });
      return {h:Math.round(sr.height),pad:cs0.paddingTop+' '+cs0.paddingBottom,bg:cs0.backgroundColor,items};
    });
  },secSel);
}
(async()=>{const b=await chromium.launch();
const ref=await run(b,REF,'body > header.nav, main#top > *, body > footer');
const neu=await run(b,LIVE,'.elementor-location-header > .e-con:not(.elementor-sticky__spacer), [data-elementor-type="wp-page"] > .e-con, .elementor-location-footer > .e-con:first-child');
fs.writeFileSync(`meas_${W}.json`,JSON.stringify({ref,neu}));await b.close();
// diff
const norm=t=>t.toLowerCase().replace(/[^a-z0-9]/g,'').slice(0,24);
const out=[];
ref.forEach((rs,i)=>{const ns=neu[i];if(!ns)return;out.push(`\n=== SECTION ${i}  h ref=${rs.h} new=${ns.h}  pad ref=${rs.pad} new=${ns.pad}`);
  const used=new Set();
  rs.items.forEach(ri=>{const k=norm(ri.t);if(!k)return;const j=ns.items.findIndex((ni,ix)=>!used.has(ix)&&norm(ni.t)===k);
    if(j<0){out.push(`  MISSING in new: "${ri.t}"`);return;}used.add(j);const ni=ns.items[j];
    const d=[];for(const f of ['x','y','w','h']) if(Math.abs(ri[f]-ni[f])>3)d.push(`${f} ${ri[f]}→${ni[f]}`);
    for(const f of ['fs','fw','lh','ls','ff','col','tt']) if(ri[f]!==ni[f])d.push(`${f} ${ri[f]}→${ni[f]}`);
    if(d.length)out.push(`  "${ri.t.slice(0,30)}": ${d.join(' | ')}`);});
  ns.items.forEach((ni,ix)=>{if(!used.has(ix))out.push(`  EXTRA in new: "${ni.t}"`)});
});
fs.writeFileSync(`diff_${W}.txt`,out.join('\n'));console.log('lines',out.length);
})();
