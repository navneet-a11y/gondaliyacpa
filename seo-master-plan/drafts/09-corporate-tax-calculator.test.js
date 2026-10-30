const fs=require('fs');
const html=fs.readFileSync(process.argv[2],'utf8');
const js=html.match(/<script>([\s\S]*?)<\/script>/)[1];
// DOM stub
const els={};const vals={};let radio='ccpc';
global.document={getElementById:id=>els[id]||(els[id]={value:vals[id],textContent:'',innerHTML:'',classList:{add(){}},scrollIntoView(){}}),querySelector:()=>({value:radio})};
global.alert=m=>console.log('ALERT',m);
eval(js+';global.ctcCompute=ctcCompute;global.calcCorpTax=calcCorpTax;');
const f=n=>n.toFixed(2);
const cases=[['2026-12-31',5e6],['2026-12-31',3e7],['2026-12-31',5e7],['2026-06-30',5e6],['2026-06-30',3e7],['2026-06-30',5e7],['2025-12-31',5e6],['2025-12-31',3e7],['2025-12-31',5e7],['2027-06-30',5e6],['2028-02-29',5e6]];
console.log('net income 600,000 (revenue 1,000,000 - expenses 400,000), CCPC');
console.log('yearEnd | capital | start | days(before/after) | ONT SBD rate | limit | fed | ont | combined | eff%');
for(const [ye,cap] of cases){const r=ctcCompute({revenue:1e6,expenses:4e5,capital:cap,yearEnd:ye,type:'ccpc'});const t=r.taxYear;
console.log([ye,cap,new Date(t.start).toISOString().slice(0,10),t.total+'('+t.before+'/'+t.after+')',(r.ontSbdRate*100).toFixed(4)+'%',f(r.limit),f(r.fedTotal),f(r.ontTotal),f(r.combined),r.effRate.toFixed(2)].join(' | '));}
const p=ctcCompute({revenue:1e6,expenses:4e5,capital:3e7,yearEnd:'2026-12-31',type:'public'});
console.log('Non-CCPC, 2026-12-31, 30M: limit',p.limit,'fed',f(p.fedTotal),'ont',f(p.ontTotal),'combined',f(p.combined));
// full DOM run
Object.assign(vals,{'ctc-revenue':'1000000','ctc-expenses':'400000','ctc-capital':'30000000','ctc-yearend':'2026-12-31'});
for(const k in vals) document.getElementById(k).value=vals[k];
calcCorpTax();
for(const k of ['r-title','r-period','r-limit','r-sbd-limit','r-ont-sbd-label','r-ont-sbd','r-ont-gen','r-combined','r-eff-rate','r-after-tax']) console.log(k,'=',els[k].textContent);
