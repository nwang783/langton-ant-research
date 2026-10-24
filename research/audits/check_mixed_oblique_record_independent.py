"""Independent integer-coordinate reconstruction of the 80 local oblique tests."""
from itertools import combinations,product
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parents[1];base=P/'causal_reduction/matrix_candidates/check_mixed_matrix_oblique_record'
saved=json.loads(base.with_suffix('.json').read_text());records=json.loads(base.with_suffix('.records.json').read_text())
D=[(0,1),(1,0),(0,-1),(-1,0)];N=[];E=[]
for west in range(4):
 w=[0]*9
 for i in range(4):w[2*i+1]=3 if i==west else 1
 N.append(tuple(w))
for west,south in product(range(5),range(4)):
 w=[]
 for i in range(9):w.append((3 if i//2==west else 1)if i%2==0 else(2 if i//2==south else 0))
 E.append(tuple(w))
domains=[N,E,[tuple((d+2)%4 for d in w)for w in N],[tuple((d+2)%4 for d in w)for w in E]]
extrema=[]
for i,words in enumerate(domains):
 assert set(words)=={tuple(w)for w in saved['domains'][i]}
 values=[]
 for w in words:
  x=y=0
  for d in w:values.append(-2*x+3*y);dx,dy=D[d];x+=dx;y+=dy
 extrema.append([min(values),max(values)])
assert extrema==[[0,10],[-7,7],[-10,0],[-7,7]]==saved['proper_prefix_extrema']
def replay(word):
 x=y=0;h=0;odd=set();first={};previous={};turns=''
 for t,d in enumerate(word):
  delta=(d-h)%4;assert delta in(1,3);wanted=delta==3;p=(x,y);height=-2*x+3*y
  if p not in first:first[p]=False if height>=0 else wanted
  current=first[p]^(p in odd)
  if current!=wanted:return {'read':t,'cell':[x,y],'linear_height':height,'required':'L'if wanted else'R','available':'L'if current else'R','previous_local_read':previous.get(p),'turn_prefix':turns}
  odd.symmetric_difference_update({p});previous[p]=t;turns+='L'if wanted else'R';dx,dy=D[d];x+=dx;y+=dy;h=d
 return None
indexed={(tuple(saved['domains'][1][r['east']]),tuple(saved['domains'][2][r['south']])):{k:v for k,v in r.items()if k not in['east','south']}for r in records}
assert len(indexed)==80;hist={};east_survive=[]
for u in E:
 if replay(u)is None:east_survive.append(u)
 for v in domains[2]:
  r=replay(u+v);assert r is not None and r==indexed[u,v]
  hist[r['read']]=hist.get(r['read'],0)+1
assert len(east_survive)==4 and max(hist)==15
result={'status':'PASS independent complete raw geometry and local first-conflict replay','domain_counts':list(map(len,domains)),'proper_prefix_extrema':extrema,'east_survivors':len(east_survive),'pairs':80,'latest_zero_based_conflict':max(hist),'histogram':hist,'sha256':{str(base.with_suffix(s).relative_to(P)):hashlib.sha256(base.with_suffix(s).read_bytes()).hexdigest()for s in ['.json','.records.json']}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
