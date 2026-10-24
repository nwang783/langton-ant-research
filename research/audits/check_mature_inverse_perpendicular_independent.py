from pathlib import Path
from collections import defaultdict,Counter
import hashlib,json
ROOT=Path(__file__).resolve().parents[1];R=ROOT/'nonlinear_global_budget_2026-10-23';D=(1j,1,-1j,-1)
J=json.loads((R/'prepared_travelling_wave_certificate.json').read_text());w=J['word'];assert hashlib.sha256(w.encode()).hexdigest()=='96e6e1dd2935e1e7afeb9dc14759320bb2b82bd2855b1596f9b1a591d1ff2122'
H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];I=''.join('L' if c=='R' else 'R' for c in H[::-1]);assert len(I)==104
p=complex(*J['wave_pose'][0]);h=J['wave_pose'][1];G=defaultdict(list)
for i,c in enumerate(w):
 x,y=int(p.real),int(p.imag);G[x-y,x%14].append((x,i,c));h=(h+(1 if c=='R' else -1))%4;p+=D[h]
assert p==8+8j and h==0 and len(G)==557
bulk={}
for k,v in G.items():
 v.sort(key=lambda row:row[1]-1564*(row[0]//14));assert all(a[2]!=b[2]for a,b in zip(v,v[1:]));bulk[k]=v[0][2]=='L'
assert max(max(x for x,i,c in v)for v in G.values())==12
# Thus every active class at x>=12 has its full list, not merely its first eligible slot.
results=[];offsets={}
for heading in (0,2):
 p=0j;h=heading;us=[]
 for c in I:
  us.append(int(p.real+p.imag));h=(h+(1 if c=='R' else -1))%4;p+=D[h]
 assert h==heading and p==(-2+2j if heading==0 else 2-2j)
 offsets[heading]=[min(us),max(us)]
 for phase in range(14):
  u0=2001+2*phase
  for parity in (0,1):
   x=(u0+(201 if heading==0 else -201))//2
   if x%2!=parity:x+=1
   start=complex(x,u0-x);p=start;h=heading;seen={};flips=set();tick=0;failure=None
   while True:
    normal=int(p.real-p.imag)
    if tick%104==0 and ((heading==0 and normal<=11)or(heading==2 and normal>=-5)):break
    c=I[tick%104];want=c=='L'
    if p in seen:assert seen[p]^(p in flips)==want
    else:
     seen[p]=want;x,y=int(p.real),int(p.imag);key=(x-y,x%14)
     if key in G:
      assert x>=max(row[0]for row in G[key])
      if bulk[key]!=want:
       failure={'step':tick,'normal':x-y,'relative_u':x+y-u0,'required':c,'actual':'L'if bulk[key]else'R'};break
    if p in flips:flips.remove(p)
    else:flips.add(p)
    h=(h+(1 if c=='R'else-1))%4;p+=D[h];tick+=1
   assert failure is not None
   results.append({'heading':heading,'u0_mod28':u0%28,'start_x_parity':parity,'conflict':failure})
assert offsets=={0:[-4,6],2:[-6,4]}
# Fresh large-offset controls cover exactly the full periodic type domain.
author=json.loads((R/'mature_inverse_perpendicular_approach.json').read_text())
A={(x['incoming_I_heading'],x['u0_mod28'],x['start_x_parity'])for x in author['results']}
assert A=={(x['heading'],x['u0_mod28'],x['start_x_parity'])for x in results} and len(A)==56
report={'status':'PASS independent all56 mature perpendicular inverse-standard approach obstruction','wave_sha256':hashlib.sha256(w.encode()).hexdigest(),'complete_eligibility_x_bound':12,'mature_u_bound':78,'inverse_slot_u_offsets':offsets,'phase0_sufficient_u_bounds':{'N':82,'S':84},'case_count':56,'conflict_normal_range':[min(x['conflict']['normal']for x in results),max(x['conflict']['normal']for x in results)],'cases':results,'scope':'Clean phase-zero inverse-H perpendicular approach from exterior into the central [-5,11] strip, with every constrained first color mature and unedited. Does not exclude nonstandard/revisited approaches, near-kernel starts, or a launch.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status']);print(report['conflict_normal_range'])
