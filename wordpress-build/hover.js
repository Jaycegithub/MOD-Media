const {chromium}=require('playwright');
const REF='file:///tmp/claude-0/-home-user-MOD-Media/5d839d89-548b-57da-a519-19ed4001428d/scratchpad/concept/mod-media-website-concept.html';
const LIVE='https://healthy-mediumaquamarine-elk-60.hostingersite.com/?h='+Date.now();
const st=e=>{const c=getComputedStyle(e);return `bg=${c.backgroundColor} col=${c.color} rad=${c.borderTopLeftRadius} pad=${c.padding} tf=${c.transform}`};
(async()=>{const b=await chromium.launch();
for(const [name,u,nav,cta] of [['REF',REF,'.nav-links a','.hero-ctas .btn-primary'],['LIVE',LIVE,'.mm-header .elementor-nav-menu--main a.elementor-item','.mm-hero .mm-btn .elementor-button']]){
 const p=await b.newPage({viewport:{width:1440,height:900}});await p.goto(u,{waitUntil:'networkidle'});await p.waitForTimeout(800);
 const out=[];
 const navActiveTop=await p.evaluate(s=>[...document.querySelectorAll(s)].filter(a=>a.classList.contains('active')||a.classList.contains('mm-active')).map(a=>a.textContent.trim()).join(',')||'none',nav);
 out.push('nav active at top: '+navActiveTop);
 await p.hover(nav+':nth-child(2)'.replace(':nth-child(2)',''));
 const links=await p.$$(nav); await links[1].hover(); await p.waitForTimeout(400);
 out.push('nav hover: '+await links[1].evaluate(e=>{const c=getComputedStyle(e),a=getComputedStyle(e,'::after'),b=getComputedStyle(e,'::before');return 'col='+c.color+' after='+(a.content!=='none'&&a.opacity!=='0'&&a.width!=='0px'?a.backgroundColor+' w='+a.width:'none')+' before='+(b.content!=='none'&&b.opacity!=='0'?b.backgroundColor:'none')}));
 await p.evaluate(()=>document.querySelector('#gallery').scrollIntoView());await p.waitForTimeout(800);
 out.push('nav active at #gallery: '+await p.evaluate(s=>[...document.querySelectorAll(s)].filter(a=>a.classList.contains('active')||a.classList.contains('mm-active')).map(a=>a.textContent.trim()).join(','),nav));
 await p.evaluate(()=>scrollTo(0,0));await p.waitForTimeout(300);
 const c=await p.$(cta); await c.hover(); await p.waitForTimeout(400); out.push('cta hover: '+await c.evaluate(st));
 for(const sel of ['#tHead','#swatches button:nth-child(2)','#effects button:nth-child(2)','#qBiz button']){
   const e=await p.$(sel); await e.scrollIntoViewIfNeeded(); await e.hover(); await p.waitForTimeout(350);
   out.push(sel+' hover: '+await e.evaluate(st));
 }
 const t=await p.$('#tFx button, .tg:not([aria-pressed="true"])');
 console.log('== '+name+'\n'+out.join('\n')); await p.close();}
await b.close()})();
