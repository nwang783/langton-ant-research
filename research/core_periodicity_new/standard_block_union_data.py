"""Exact coboundary/first-read data for all standard104 cyclic phases."""
import json
from pathlib import Path
from collections import defaultdict,Counter
D=((0,1),(1,0),(0,-1),(-1,0))
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'recovered_bundle/ant_global/root/standard.json').read_text());W=data['word'];h=data['heading']
rows=[]
for phase in range(104):
 w=W[phase:]+W[:phase];p=(0,0);hh=h;reads=[]
 for a in w:
  reads.append(p);hh=(hh+(1 if a=='R' else -1))%4;dd=D[hh];p=(p[0]+dd[0],p[1]+dd[1])
 d=p;assert d==(-2,-2) and hh==h
 C=Counter(reads);O={p for p,n in C.items() if n%2}
 groups=defaultdict(set)
 for x,y in O:
  a=x%2;t=x-y;k=(a-x)//2;groups[(t,a)].add(k)
 Q=set();P=set()
 for (t,a),ks in groups.items():
  if len(ks)%2:Q.add((a,a-t));ks=ks^{0}
  if not ks:continue
  bit=0
  for k in range(min(ks),max(ks)):
   bit^=k in ks
   if bit:P.add((a-2*k,a-t-2*k))
 shift=lambda S,v:{(x+v[0],y+v[1]) for x,y in S}
 assert O==Q^P^shift(P,d)
 assert len(Q)==12
 # For the actual cyclic phase, read 4 periods and record first-L requirements.
 # The maximum coordinate spread per orbit is <=3, so this is complete;
 # additionally every later newly encountered cell has R as its full-orbit first phase.
 first={};pp=(0,0);hhh=h
 for j,a in enumerate(w*4):
  first.setdefault(pp,a);hhh=(hhh+(1 if a=='R' else -1))%4;dd=D[hhh];pp=(pp[0]+dd[0],pp[1]+dd[1])
 firstL={p for p,a in first.items() if a=='L'}
 g=defaultdict(list)
 for i,(x,y) in enumerate(reads):g[(x-y,x%2)].append((i,(x%2-x)//2))
 maxspan=max(max(k for i,k in seq)-min(k for i,k in seq) for seq in g.values())
 assert maxspan<=3
 for seq in g.values():
  i,k=max(seq,key=lambda z:z[1]*104-z[0]);assert w[i]=='R'
 rows.append({'phase':phase,'heading':h,'odd_write_count':len(O),'coboundary_count':len(P),
              'first_L_count':len(firstL),'max_orbit_span':maxspan,'read_x_range':[min(x for x,y in reads),max(x for x,y in reads)],
              'read_y_range':[min(y for x,y in reads),max(y for x,y in reads)],
              'tile':sorted(Q),'coboundary':sorted(P)})
 h=(h+(1 if W[phase]=='R' else -1))%4
out={'status':'exact phase data; analytic union-error argument separate',
     'max_coboundary_count':max(r['coboundary_count'] for r in rows),
     'max_first_L_count':max(r['first_L_count'] for r in rows),
     'max_orbit_span':max(r['max_orbit_span'] for r in rows),'rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
