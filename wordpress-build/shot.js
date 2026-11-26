const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
const errs=[];
for (const [n,w,h] of [['desk',1440,900],['tab',820,1180],['mob',390,844]]){
 const p=await b.newPage({viewport:{width:w,height:h}});
 p.on('console',m=>{if(m.type()==='error')errs.push(n+': '+m.text())}); p.on('pageerror',e=>errs.push(n+' PAGEERR: '+e.message));
 await p.goto('https://healthy-mediumaquamarine-elk-60.hostingersite.com/?nocache='+Date.now(),{waitUntil:'networkidle',timeout:90000});
 await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,120))}window.scrollTo(0,0)});
 await p.waitForTimeout(1500);
 await p.screenshot({path:`shots/${n}.png`,fullPage:true});
 const info=await p.evaluate(()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth,h:document.body.scrollHeight,
   hdr:!!document.querySelector('.elementor-location-header'),ftr:!!document.querySelector('.elementor-location-footer'),
   form:!!document.querySelector('form.elementor-form'),reviews:document.querySelectorAll('.elementor-testimonial').length,nav:document.querySelectorAll('.elementor-nav-menu a').length}));
 console.log(n,JSON.stringify(info)); await p.close();}
console.log(errs.join('\n')); await b.close();})();
