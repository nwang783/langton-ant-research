"""Combine signed common-output endpoints with the two-role atomic clock guard.
Scope: actual atomic cuts inside complete retained-eight factors, not arbitrary
words over a larger independently licensed atomic language.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';AP=R/'chronology_dcuv/counted_input_age_rules_complete.json';CP=R/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';J=json.loads(GP.read_text());G=J['geometry'];K=set(map(tuple,J['core']));IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};mins={(a,x,y):v for a,x,y,v in json.loads(AP.read_text())};D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
C=G[1]['word'][len(G[0]['word']):];marker=G[0]['marker'];assert C.startswith(marker);p=(0,0);h=0;par=set();need={};end=None
for t,ch in enumerate(C+marker):
 b=(ch=='L')^(p in par);assert p not in need or need[p]==b;need[p]=b
 if p in par:par.remove(p)
 else:par.add(p)
 h=(h+(-1 if ch=='L'else 1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 if t+1==len(C):end=(p,h,set(par))
assert {p for p,b in need.items()if b}==K and need[2,0]==False
p,h,odd=end;B=K^odd;newcore={(p[0]+rot(z,h)[0],p[1]+rot(z,h)[1])for z in K};assert newcore<=B;CO=B-newcore
assert(p,h)==((0,1),3)and CO=={(1,2),(2,0),(2,1)}
roles=[]
for a in IDS:
 base=0 if a in(0,1)else 4 if a in(4,5,6)else 7;c=G[a]['name'].count('C');assert G[a]['word']==G[base]['word']+C*c
 assert[2,0]in G[a]['outputs']
 roles.append(dict(full_source=a,atomic_source=G[base]['name'],atomic_start=[0,0,0],atomic_birth_clock_shift=0,full_source_output=[2,0],age_guard='ORDINARY_JO_PLUS_AGE2_SECTOR'))
 p=tuple(G[base]['endpoint'][:2]);h=0
 for j in range(c):
  r=rot((2,0),h);o=(p[0]+r[0],p[1]+r[1]);assert list(o)in G[a]['outputs']
  assert j in(0,1)
  if j==1:assert(a,o)in[(6,(1,6)),(9,(0,7))]
  roles.append(dict(full_source=a,atomic_source='C',atomic_start=[*p,h],atomic_birth_clock_shift=j,full_source_output=o,age_guard='SIGNED_TWO_ROLE_SECOND_C_CLOCK_GUARD'if j else'ORDINARY_JO_PLUS_AGE2_SECTOR'))
  u,v=rot((0,1),h);p=(p[0]+u,p[1]+v);h=(h-1)%4
assert len(roles)==15 and sum(r['atomic_birth_clock_shift']==1 for r in roles)==2
queries=[]
for a,o in[(6,(1,6)),(9,(0,7))]:
 for n in range(4):
  h=(-n)%4
  for b in IDS:
   for inp in G[b]['inputs']:
    u,v=rot(inp,h);p=(o[0]-u,o[1]-v);key=(mp[a],mp[b],*p,h,*o,n);wrong=(sum(p)+h)%2
    if not wrong:assert key in COUNT
    queries.append(dict(full_source=a,output=o,full_source_age=n,atomic_source_age=n-1,consumer=b,input=inp,consumer_pose=[*p,h],reason='SECTOR_IMPOSSIBLE'if wrong else'SIGNED_COUNT5_EXCLUDED',query=key))
assert len(queries)==184
assert all(v>=2 for v in mins.values());sector=[]
for a in IDS:
 for inp in G[a]['inputs']:
  if mins[a,*inp]>2:continue
  u,v=rot(inp,2);p=(2-u,-v);assert(sum(p)+2)%2;sector.append(dict(consumer=a,input=inp,pose=[*p,2]))
assert len(sector)==2
ends=[]
for h in(0,1):
 for b in(0,4,7):
  step=rot(G[b]['endpoint'][:2],h)
  for inp in G[b]['inputs']:
   u,v=rot(inp,h);p=(2-u,-v);e=(p[0]+step[0],p[1]+step[1]);assert e[0]>=2;ends.append(dict(retiring_base=b,input=inp,heading=h,start=p,end=e))
assert all(rot(G[b]['endpoint'][:2],h)[0]>=0 for b in(0,4,7)for h in(0,1))and rot((0,1),1)==(1,0)
for a in IDS:assert [2,0,False,8]in G[a]['requirements']
O=dict(status='AUTHOR_ATOMIC_COMMON_OUTPUT_UNCONDITIONAL_FOUR_C_NONRETURN_PASS',scope='All actual D/V/U/C atomic marked cuts arising INSIDE a valid complete recurrent-eight factor. Source atomic output(2,0) is fresh and has atomic age at least3 before any residual input. Thus signed E/N endpoint proof gives exact4C marked-pose nonreturn without factor-first exception. Not arbitrary atomic words, not higherC cycles.',literal_C=dict(word=C,residual_inputs=[],residual_outputs=sorted(CO),endpoint=[0,1,3],before_white_2_0=True),all15_atomic_source_roles=roles,all184_second_C_clock_queries=queries,ordinary_age2_sector_failures=sector,all16_retiring_base_endpoints=ends,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,AP,CP,Path(__file__).resolve()]})
(R/'chronology_dcuv/atomic_common_output_four_C.json').write_text(json.dumps(O,indent=2)+'\n');print(dict(atomic_source_roles=len(roles),second_C_clock_queries=len(queries),ordinary_sector_cases=len(sector),retiring_endpoints=len(ends)))
