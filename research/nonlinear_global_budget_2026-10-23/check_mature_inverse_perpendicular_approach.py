#!/usr/bin/env python3
"""All56 same-sector mature perpendicular inverse-H approach phases."""
from pathlib import Path
from collections import defaultdict,Counter
import json,runpy
ROOT=Path(__file__).parent;E=runpy.run_path(str(ROOT/'endpoint_catalog.py'));N=json.loads((ROOT/'prepared_wave_five_band_normal_form.json').read_text());J=json.loads((ROOT/'prepared_travelling_wave_certificate.json').read_text());B={tuple(j)for j in N['full_black_orbit_profiles']};G=defaultdict(list);p=tuple(J['wave_pose'][0]);h=J['wave_pose'][1];V=E['V']
for i,ch in enumerate(J['word']):
 x,y=p;G[x-y,x%14].append((x-x%14)//14);h=(h+(-1 if ch=='L'else 1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
G={j:min(v)for j,v in G.items()};I=''.join('L'if c=='R'else'R'for c in E['H'][::-1]);out=[]
for heading in[0,2]:
 for phase in range(14):
  u0=401+2*phase
  for parity in[0,1]:
   x=(u0+(101 if heading==0 else -101))//2
   if x%2!=parity:x+=1
   p=(x,u0-x);h=heading;start=p;seen={};flips=set();fail=None;k=0
   while k<104*100:
    t=p[0]-p[1]
    if k%104==0 and((heading==0 and t<=11)or(heading==2 and t>=-5)):break
    ch=I[k%104];want=ch=='L'
    if p in seen:
     assert (seen[p]^(p in flips))==want
    else:
     seen[p]=want;x,y=p;j=(x-y,x%14);n=(x-x%14)//14
     if j in G:
      assert n>=G[j] # the supplied placement is in the mature-wave regime
      actual=(x-y,x%2)in B
      if actual!=want:fail={'step':k,'cell':list(p),'normal':x-y,'u':x+y,'required':ch,'actual_wave':'L'if actual else'R'};break
    flips.symmetric_difference_update({p});h=(h+(-1 if want else 1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1]);k+=1
   out.append({'incoming_I_heading':heading,'u0_mod28':u0%28,'start_x_parity':parity,'start':list(start),'status':'REJECTED'if fail else'REACHED_CENTRAL_PHASE0','conflict':fail,'steps':k,'last_pose':[list(p),h]})
report={'scope':'Allsame-sector phase0 inverse-H perpendicular approaches fromexterior tocentral[-5,11] in mature1564futurecolorregime; not near-kernel or nonstandardapproach impossibility.','case_count':len(out),'outcomes':dict(Counter(r['status']for r in out)),'results':out};(ROOT/'mature_inverse_perpendicular_approach.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if k!='results'},indent=2));print('conflictnormalrange',min(r['conflict']['normal']for r in out if r['conflict']),max(r['conflict']['normal']for r in out if r['conflict']))
