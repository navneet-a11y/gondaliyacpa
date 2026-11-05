import json
D=json.load(open('/tmp/claude-0/-home-user-gondaliyacpa/5e30d53f-dc31-54b6-8491-e5c35631246a/scratchpad/pkg/WealthScale-201-Pages/site-wide/ws-data.json'))
T=D['tax']; DV=T['dividends']
NEW={'AB':[0.0812,0.0218],'SK':[0.11,0.02519],'MB':[0.08,0.007835],'YT':[0.1202,0.0067],'NT':[0.115,0.06],'NU':[0.0551,0.0261]}
PDTC=dict(DV['provincial_dtc']); PDTC.update(NEW)
def brk(x,br):
    t=0;lo=0
    for up,r in br:
        hi=up if up is not None else 1e18
        if x>lo: t+=(min(x,hi)-lo)*r
        lo=hi
    return t
def bpa(x,j):
    b=j['bpa']; ph=j.get('bpa_phase')
    if not ph: return b
    lo,hi=ph[0],ph[1]; mn=ph[2] if len(ph)>2 else j.get('bpa_min',0)
    if x<=lo: return b
    if x>=hi: return mn
    return b-(b-mn)*(x-lo)/(hi-lo)
def ftax(x,dtc=0):
    f=T['federal']; f2=dict(f); f2['bpa_phase']=f['bpa_phase']+[f['bpa_min']]
    return max(0,brk(x,f['brackets'])-f['brackets'][0][1]*bpa(x,f2)-dtc)
def ptax(x,p,dtc=0):
    j=T['provinces'][p]; return max(0,brk(x,j['brackets'])-j['brackets'][0][1]*bpa(x,j)-dtc)
def total(x,p,el=0,ne=0):
    g=x+1.38*el+1.15*ne
    fd=1.38*el*DV['federal_dtc_eligible']+1.15*ne*DV['federal_dtc_noneligible']
    pd=1.38*el*PDTC[p][0]+1.15*ne*PDTC[p][1]
    return ftax(g,fd)+ptax(g,p,pd)
def rates(x,p,h=1.0):
    o=(total(x+h,p)-total(x,p))/h
    e=(total(x,p,el=h)-total(x,p))/h
    n=(total(x,p,ne=h)-total(x,p))/h
    return o,e,n
