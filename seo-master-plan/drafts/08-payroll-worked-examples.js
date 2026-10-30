function calc(annual,f,fedBPAv,onBr,onBPAv){
var cppRate=0.0595,cppMax=74600,cppExempt=3500,cppMaxContrib=4230.45;
var p=Math.max(0,Math.min(annual,cppMax)-cppExempt);var cpp=Math.min(p*cppRate,cppMaxContrib);
var cpp2=0;if(annual>cppMax)cpp2=Math.min((Math.min(annual,85000)-cppMax)*0.04,416);
var ei=Math.min(annual*0.0163,1123.07);
var ti=Math.max(0,annual-cpp-cpp2-ei-fedBPAv);var fed;
if(ti<=58523)fed=ti*0.14;else if(ti<=117045)fed=58523*0.14+(ti-58523)*0.205;else if(ti<=181440)fed=58523*0.14+58522*0.205+(ti-117045)*0.26;else if(ti<=258482)fed=58523*0.14+58522*0.205+64395*0.26+(ti-181440)*0.29;else fed=58523*0.14+58522*0.205+64395*0.26+77042*0.29+(ti-258482)*0.33;
var pt=Math.max(0,annual-cpp-cpp2-ei-onBPAv),prov=0,prev=0;for(const b of onBr){var a=Math.min(pt,b.l)-prev;if(a>0)prov+=a*b.r;prev=b.l;if(pt<=b.l)break;}
var g=annual/f,r=x=>Math.round(x/f*100)/100;
var o={gross:Math.round(g*100)/100,cpp:r(cpp+cpp2),ei:r(ei),fed:r(fed),prov:r(prov)};
o.total=+(o.cpp+o.ei+o.fed+o.prov).toFixed(2);o.net=+(o.gross-o.total).toFixed(2);o.empEI=+(o.ei*1.4).toFixed(2);o.empCost=+(o.gross+o.cpp+o.empEI).toFixed(2);
o.annual={cpp,cpp2,ei,fedTaxable:ti,fed,provTaxable:pt,prov};return o;}
var ONold=[{l:52886,r:0.0505},{l:105775,r:0.0915},{l:150000,r:0.1116},{l:220000,r:0.1216},{l:Infinity,r:0.1316}];
var ONnew=[{l:53891,r:0.0505},{l:107785,r:0.0915},{l:150000,r:0.1116},{l:220000,r:0.1216},{l:Infinity,r:0.1316}];
for(const s of [60000,100000]){console.log(s,'NEW',JSON.stringify(calc(s,26,16452,ONnew,12989)));}
for(const s of [60000,100000]){console.log(s,'currentJS',JSON.stringify(calc(s,26,16129,ONold,11865)));}
