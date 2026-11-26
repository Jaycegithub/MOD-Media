// Usage: node cmp.js <width> <outdir>
const {chromium}=require('playwright');const fs=require('fs');
const W=+process.argv[2]||1440, OUT=process.argv[3]||'cmp';
fs.mkdirSync(OUT,{recursive:true});
const REF='file:///tmp/claude-0/-home-user-MOD-Media/5d839d89-548b-57da-a519-19ed4001428d/scratchpad/concept/mod-media-website-concept.html';
const LIVE='https://healthy-mediumaquamarine-elk-60.hostingersite.com/?v='+Date.now();
async function grab(b,url,sel,tag){
  const p=await b.newPage({viewport:{width:W,height:900},reducedMotion:'reduce'});
  await p.goto(url,{waitUntil:'networkidle',timeout:120000});
  await p.addStyleTag({content:'.ribbon{display:none!important} header.nav,.elementor-location-header .e-con{position:static!important} .mobilebar,[data-id] .elementor-sticky--active{position:static!important}'});
  await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=400){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,120))}window.scrollTo(0,0)});
  await p.evaluate(()=>document.querySelectorAll('.reveal,[class*=reveal]').forEach(e=>e.classList.add('in','visible','shown')));
  await p.waitForTimeout(2500);
  const els=await p.$$(sel);const n=[];
  for(let i=0;i<els.length;i++){const bb=await els[i].boundingBox();if(!bb||bb.height<20)continue;
    const f=`${OUT}/${tag}_${String(n.length).padStart(2,'0')}.png`;await els[i].screenshot({path:f});n.push(Math.round(bb.height));}
  console.log(tag,n.length,JSON.stringify(n));await p.close();
}
(async()=>{const b=await chromium.launch();
await grab(b,REF,'body > header.nav, main#top > *, body > footer','ref');
await grab(b,LIVE,'.elementor-location-header > .e-con, [data-elementor-type="wp-page"] > .e-con, .elementor-location-footer > .e-con:first-child','new');
await b.close()})();
