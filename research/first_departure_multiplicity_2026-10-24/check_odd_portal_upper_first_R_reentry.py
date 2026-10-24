"""Odd-root fixed upper interface: exact same-circle reentry or outward tree.
Necessary local histories/calendars only; no completed front is certified.
"""
from pathlib import Path
from itertools import product
from collections import Counter,defaultdict,deque
import json
b=Path(__file__).parent;S={'__file__':str(b/'check_terminal_LL_upper_side_collision.py')};exec((b/'check_terminal_LL_upper_side_collision.py').read_text().split('# Shift the physical Q')[0],S)
analyze,words,out,V,fp=[S[k] for k in ['analyze','words','out','V','fp']]
# The calendar packs event-disjoint complete successor components, not windows.
C=(b/'check_even_portal_uncapped_outer_shields.py').read_text();exec(C[C.index('def calendar('):C.index('ct=Counter();pr=Counter();ans=[]')],globals())
ct1=Counter();tops=[]
for r,a,z in product(['SNN','SNNS'],words('NS'),words('EW')):
 hs={(0,-1):'WWE',(1,-1):r,(0,0):a,(1,0):z};res,cert=analyze(hs);ct1[res]+=1
 if res=='open':tops.append((r,a,z))
assert ct1=={'port':1871,'rank':34,'higher_C':9,'open':5,'clock':3}
ct2=Counter();rows=[]
for (r,a,z),ll,k in product(tops,words('EW'),words('NS')):
 hs={(-2,-1):'EEWW',(-1,-1):'SNN',(0,-1):'WWE',(1,-1):r,(0,0):a,(1,0):z,(-1,0):ll,(-2,0):k}
 res,cert=analyze(hs);ct2[res]+=1
 if res!='open':continue
 assert (ll,k) in [('EEW','NNSS'),('WEE','SSNN'),('WEEE','NSN')]
 su={(tuple(e[0]),e[1]):(tuple(f[0]),f[1]) for e,f in cert['successor_edges']}
 vals={tuple(p):h for p,h in cert['face_values']}
 bm={p:(p[0]+V[out(h,0)][0],p[1]+V[out(h,0)][1]) for p,h in hs.items()}
 assert bm[(0,-1)]==(0,0) and bm[(0,0)]==(-1,0)
 assert all(vals[fp(p,out(hs[p],0))[0]]==0 for p in [(0,-1),(0,0),(-1,0)])
 assert su[(0,-1),0]==((0,0),2)
 if ll=='EEW':
  assert su[(0,0),0]==((-1,0),2) and su[(-1,0),0]==((-1,-1),0)
  path=[((-2,-1),1),((-2,0),0),((-1,0),0),((-1,-1),0),((-2,-1),2)]
  assert all(su[e]==f for e,f in zip(path,path[1:]))
 else:
  assert su[(0,0),0]==((-1,0),0) and su[(-1,0),2]==((-1,-1),0)
  assert bm[(-1,0)]==(-1,1)
  if ll=='WEE':assert bm[(-2,0)]==(-3,0)
  else:
   assert bm[(-2,0)]==(-1,0) and bm[(-2,-1)]==(-2,-2)
   assert vals[(-3,0)]==-2 and vals[(-2,-1)]==0
 rows.append(dict(R=r,U=a,W=z,L=ll,K=k,histories={str(p):h for p,h in sorted(hs.items())},certificate=cert,first_R_edges=[[p,q] for p,q in sorted(bm.items())],finite_event_calendar=calendar(hs,cert)))
assert ct2=={'port':4755,'open':15,'rank':35} and len(rows)==15
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,translation_from_physical=[-1,-3],Q_square_counts=dict(ct1),Q_square_modes=tops,eight_cell_counts=dict(ct2),controls=rows,warning='Same-Gamma placement/return conclusions are conditional on the stated actual GLOBAL-M essential b-circle. Calendars leave exterior connectors open; branches may merge; no paid roots, fuel, front or controller.'),indent=2)+'\n')
print('PASS odd upper1922->5;4805->15 modes; exact first-R target ranks, immediate LRRR return, all maximum levels and calendars')
