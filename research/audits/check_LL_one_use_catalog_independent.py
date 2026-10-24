from pathlib import Path
from collections import Counter,defaultdict
from itertools import product
import json,hashlib,ast
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'critical_LL_catalog_with_one_use_even_portals.md':'a93b53b9','check_critical_LL_one_use_endpoint_catalog.py':'96bda527','check_critical_LL_one_use_endpoint_catalog.json':'6bf048a3','check_even_one_use_LL_portal_calendar.py':'90379e00','check_even_one_use_LL_portal_calendar.json':'193d98cb'}
for f,h in files.items():assert sha(D/f).startswith(h)
J=json.loads((D/'check_critical_LL_one_use_endpoint_catalog.json').read_text());C=json.loads((D/'check_even_one_use_LL_portal_calendar.json').read_text())
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def out(w,r):return H[(H.index(w[r])+(1 if r%2==0 else-1))%4]
def allwords(ax):return[''.join(w)for n in range(1,5)for w in product(ax,repeat=n)]
Bs=[w for w in allwords('NS')if w[0]=='S'and sum(out(w,r)=='W'for r in range(len(w)))==2]
As=[w for w in allwords('EW')if w[0]=='E'and w.count('E')==2]
assert set(Bs)=={'SN','SNN','SSNN','SNNS','SSS','SSSS'}and set(As)=={'EE','EEW','EEWW','EWWE','EWE','EWEW'}
def graph(hs):
 succ={}
 for p,w in hs.items():
  for d,v in V.items():
   q=(p[0]+v[0],p[1]+v[1])
   if q not in hs:continue
   sr=[r for r in range(len(w))if out(w,r)==d];rr=[r for r,c in enumerate(hs[q])if c==d]
   if len(sr)!=len(rr):return None
   for r,s in zip(sr,rr):succ[p,r]=q,s
 return succ
def contradiction(succ):
 for start in succ:
  walk=[start];seen={start};cur=start
  while cur in succ:
   cur=succ[cur];walk.append(cur)
   if cur[0]==start[0]:
    if cur[1]!=start[1]+1:return walk
    break
   if cur in seen:return walk
   seen.add(cur)
 return None
cnt=Counter();opens=[];witness=[]
for b,a,y in product(Bs,As,['EWW','EWWE','EEWW']):
 hs={(1,1):b,(1,0):a,(0,1):y,(0,0):'NNSS'};g=graph(hs)
 if g is None:cnt['port']+=1;continue
 bad=contradiction(g)
 if bad:cnt['skipped_rank']+=1;witness.append(dict(B=b,A=a,Y=y,path=bad));continue
 cnt['open']+=1;opens.append(dict(B=b,A=a,Y=y,Z='NNSS'))
assert cnt==J['summary'];key=lambda r:(r['B'],r['A'],r['Y']);assert {key(z)for z in opens}=={key(z)for z in J['local_open']}
rejected=[z for z in opens if z['B']in ['SSS','SSSS']and z['Y']!='EEWW'];left=[z for z in opens if z not in rejected]
assert len(rejected)==8 and len(left)==16 and{key(z)for z in left}=={key(z)for z in J['critical_necessary_rows']}
# Explicit old high-sink nesting strands remain valid with any upstream flow.
for y in ['EWW','EWWE']:
 hs={(1,2):'EWWW',(1,1):'SSS',(0,1):y};g=graph(hs);assert g
 assert g[(1,2),0]==((1,1),0)and g[(1,1),0]==((0,1),1)
 assert g[(1,2),3]==((1,1),2)and g[(1,1),2]==((0,1),2)
# Unique cap4 source of FOUR S arrivals: all four departures pointS.
four=[w for w in allwords('EW')if sum(out(w,r)=='S'for r in range(len(w)))==4];assert four==['EWEW']
hs={ast.literal_eval(p):w for p,w in C['histories'].items()};g=graph(hs);assert g and not contradiction(g)
E={(p,r)for p,w in hs.items()for r in range(len(w))};components=[];used=set();prev={v:u for u,v in g.items()}
assert len(prev)==len(g)
for e in sorted(E-prev.keys()):
 chain=[e]
 while chain[-1]in g:chain.append(g[chain[-1]])
 assert not used.intersection(chain);used.update(chain);components.append(chain)
assert used==E and len(E)==12 and len(components)==5
canonical=lambda rows:{tuple((tuple(p),r)for p,r in z)for z in rows};assert canonical(components)==canonical(C['components'])
times={ast.literal_eval(e):t for e,t in C['injective_mod4_calendar'].items()};assert set(times)==E and len(set(times.values()))==12
for e,f in g.items():assert times[f]-times[e]==1
phase=lambda p:2*(p[0]%2)if sum(p)%2==0 else 3-2*(p[0]%2)
for p,w in hs.items():
 for r in range(len(w)):
  assert times[p,r]%4==phase(p)
  if r:assert times[p,r]-times[p,r-1]>=4
path=[(tuple(p),r)for p,r in C['actual_four_L_cleanup']];assert all(g[e]==f for e,f in zip(path,path[1:]))and all(r%2 for p,r in path[:-1])
assert hs[(1,1)].count('S')==1 and sum(out(hs[(1,0)],r)=='S'for r in range(2))==1
O=dict(status='PASS critical LL endpoint catalog with one-use allowed, and necessary even portal calendar',files={f:sha(D/f)for f in files},script=sha(S),complete_B_domain=Bs,complete_A_domain=As,counts=cnt,all_rank_witnesses=witness,critical_remaining=left,portal_components=components,portal_calendar=C['injective_mod4_calendar'],analytic_review=['Critical last-LEFT passiveV theorem has no no-one-use premise; it fixesZ only. All cap4RIGHT endpoints are independently count-derived, including two-read one-use sources/sinks, not assumed singletons.','For high4 predecessorSSSS, the only physical four-output supplier is RIGHT EWEW, so general mixedRR forces the adjoining LEFT passive orflow1, not O/U. For odd sinkSSS, a RIGHT predecessor yields the same RR gate, including1to3 sources; a LEFT predecessor mustEWWW. Exact w0→q0→Y1 andw3→q2→Y2 give T1w>=T1Y+2,T2w<=T2Y-6, impossible for critical same-physical disjoint return intervals. No upstream one-use edge changes those actual strands.','Only high-sink rejection transfers; the old conclusion predecessorFLAT doesNOT. Remaining sourcesSN/SNN are retained. All16 rows are necessary local interfaces, with unfilled exterior and full-quotient alias constraints not silently solved.','The12-event all-even control preserves both earlierR0s, allL3s, zero ports and five event-disjoint whole successor components with injective mod4 clocks. It is not an actual factor by itself and supplies no odd/fuel charge.'],scope='Complete WHITE cap4 actual critical constant-selected-C b-circle; one-use edges allowed. No global attraction, wholly single-used boundary, attained front or new controller claim.')
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(sha(S.with_suffix('.json')))
