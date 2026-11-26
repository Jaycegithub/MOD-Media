const {chromium}=require('playwright');
const U='https://healthy-mediumaquamarine-elk-60.hostingersite.com/';
const res={};const errs=[];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});
p.on('pageerror',e=>errs.push('PAGEERR '+e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
p.on('requestfailed',r=>errs.push('REQFAIL '+r.url()));
await p.goto(U+'?qa='+Date.now(),{waitUntil:'networkidle'});
const links=await p.$$eval('a[href]',as=>as.map(a=>a.getAttribute('href')));
const anchors=[...new Set(links.filter(h=>/^\/?#/.test(h)).map(h=>h.replace(/^\/?#/,'')))];
res.anchorsOk=anchors.every(a=>true);res.anchors={};for(const a of anchors)res.anchors[a]=await p.$('#'+a)!==null;
await p.click('.elementor-nav-menu--main a[href="/#faq"]');await p.waitForTimeout(1500);
res.navFaqTop=await p.$eval('#faq',e=>Math.round(e.getBoundingClientRect().top));
const t=await p.$$('#faq .elementor-tab-title');await t[2].click();await p.waitForTimeout(800);
res.accordionOpen=await p.$$eval('#faq .elementor-tab-content',cs=>cs.map(c=>getComputedStyle(c).display).join(','));
// reviews carousel
const first=await p.$eval('.mm-rv .swiper-slide-active',e=>e.textContent.trim().slice(0,30));
await p.click('.mm-rv .elementor-swiper-button-next');await p.waitForTimeout(900);
res.carousel=first+' -> '+await p.$eval('.mm-rv .swiper-slide-active',e=>e.textContent.trim().slice(0,30));
// builder
await p.fill('#adHead','TEST HEADLINE');await p.waitForTimeout(300);
res.builderScreen=await p.$eval('#adBig',e=>e.textContent);
res.builderHiddenOk=await p.$eval('#adImgRm',e=>getComputedStyle(e).display==='none');
await p.click('#useAd');await p.waitForTimeout(800);
res.builderMsg=await p.$eval('#form-field-message',e=>e.value);
// planner -> radio + area
await p.click('#qBiz button[data-v="promo"]');await p.click('#qGoal button[data-v="texas"]');await p.waitForTimeout(400);
res.planner=await p.$eval('#result h3',e=>e.textContent);
await p.click('#result a');await p.waitForTimeout(800);
res.plannerForm=[await p.$eval('input[name="form_fields[campaign]"]:checked',e=>e.value),await p.$eval('#form-field-area',e=>e.value)];
// multi-step form
await p.click('.e-form__buttons__wrapper__button-next');await p.waitForTimeout(600);
res.step2Visible=await p.$eval('#form-field-name',e=>e.offsetParent!==null);
await p.click('.e-form__buttons__wrapper__button-previous');await p.waitForTimeout(400);
res.backWorks=await p.$eval('input[name="form_fields[campaign]"]',e=>e.offsetParent!==null);
await p.click('.e-form__buttons__wrapper__button-next');await p.waitForTimeout(400);
await p.click('#quote button[type=submit]');await p.waitForTimeout(500);
res.requiredBlocked=await p.$eval('#form-field-name',e=>e.validationMessage);
await p.fill('#form-field-name','QA TEST - please ignore');
await p.fill('#form-field-business','QA test submission');
await p.fill('#form-field-phone','(214) 555-0123');
await p.fill('#form-field-email','qa-test@example.com');
await p.click('#quote button[type=submit]');
await p.waitForSelector('.elementor-message',{timeout:30000}).catch(()=>{});
res.formResult=await p.$eval('.elementor-message',e=>e.className.split(' ').pop()+' :: '+e.textContent).catch(()=>'no message');
// mobile
const m=await b.newPage({viewport:{width:390,height:844},isMobile:true,hasTouch:true});
await m.goto(U+'?qa='+Date.now(),{waitUntil:'networkidle'});
res.mobileOverflow=await m.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
await m.tap('.elementor-menu-toggle');await m.waitForTimeout(600);
res.mobileMenu=await m.$eval('.elementor-nav-menu--dropdown',e=>getComputedStyle(e).display+' h='+Math.round(e.getBoundingClientRect().height));
await m.tap('.elementor-menu-toggle');
await m.evaluate(()=>scrollTo(0,3000));await m.waitForTimeout(800);
res.mobileBar=await m.evaluate(()=>{const e=[...document.querySelectorAll('.elementor-location-footer .elementor-button')].find(b=>b.textContent.includes('Get Pricing'));const r=e.getBoundingClientRect();return Math.round(r.bottom)+'/'+innerHeight});
res.toTop=await m.$eval('.mm-totop',e=>e.classList.contains('show'));
const tab=await b.newPage({viewport:{width:820,height:1180}});await tab.goto(U,{waitUntil:'networkidle'});
res.tabletOverflow=await tab.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
res.desktopOverflow=await p.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
console.log(JSON.stringify(res,null,1));console.log('ERRORS:\n'+errs.join('\n'));await b.close()})();
