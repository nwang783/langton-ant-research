"""Fresh image inventories and direct-orbit sixteen-state filter control."""
from pathlib import Path
from itertools import combinations,product
import json,hashlib
P=Path(__file__).resolve().parents[1];D=P/'causal_reduction/matrix_candidates';v=[1j,1,-1j,-1];last=[1j,-1,-1j,-1]
def legal(w,h):
 p=0j;state={}
 for d in w:
  b=d/h==1j
  if p in state and state[p]!=b:return False
  state[p]=not b;p+=d;h=d
 return True
dom=[]
for d in v:
 target=complex(3*d.real+2*d.imag,2*d.real+7*d.imag);H=[i for i in range(13)if(i%2)==int(d.real==0)];V=[i for i in range(13)if i not in H];own=[]
 for a in combinations(H,(len(H)+int(target.real))//2):
  for b in combinations(V,(len(V)+int(target.imag))//2):
   positive=set(a)|set(b);w=tuple((1 if i in H else 1j)*(1 if i in positive else-1)for i in range(13));assert sum(w)==target
   if legal(w,d*1j)or legal(w,-d*1j):own.append(w)
 dom.append(own)
assert list(map(len,dom))==[15,91,15,91]
features=[]
for h in range(4):
 for delta in[1,3]:
  d=(h+delta)%4;out=set()
  for w in dom[d]:
   if w[-1]!=last[d]:continue
   end=sum(w);p=0j;arrivals=[];endpoint_reads=0
   for i,z in enumerate(w):
    endpoint_reads+=p==end;p+=z
    if p==end:arrivals.append(i+1)
   j=arrivals[0];assert j>=2;H=w[j-1];eps=w[-1]/H;assert eps in(1,-1)
   out.add((v.index(w[0]),v.index(w[j-2]),v.index(H),int((-1)**endpoint_reads*eps.real)))
  features.append(sorted(out))
assert list(map(len,features))==[10,9,2,2,9,10,2,2]
triples=[(w,u,z)for w,u,z in product(range(4),repeat=3)if(w-u)%2 and(z-u)%2];index={t:i for i,t in enumerate(triples)}
state=lambda h,z:2*h+int((z-h)%4==3)
count=survive=0;hist={}
for ff in product(*features):
 if ff[0][0]!=1:continue
 count+=1;T=[]
 for w,u,z in triples:
  _,M,H,sgn=ff[state(w,u)];F=ff[state(u,z)][0];new=(M,H,(F+(2 if sgn==-1 else 0))%4);T.append(index[new])
 safe=set()
 for start in range(16):
  seen=set();s=start
  while s not in seen and(triples[s][2]-triples[s][1])%4==1:seen.add(s);s=T[s]
  if s in seen:safe.add(start)
  else:assert len(seen)<=8
 directions=[]
 for u in range(4):
  z=(u+1)%4;zz=(u+2)%4
  if index[u,z,zz]in safe and any(index[w,u,z]in safe for w in range(4)if(w-u)%2):directions.append(u)
 hist[str(tuple(directions))]=hist.get(str(tuple(directions)),0)+1
 survive+=bool(set(directions)&{0,2})and bool(set(directions)&{1,3})
saved=json.loads((D/'pair_first_visit_features.json').read_text());assert count==saved['feature_assignments']==77760 and survive==saved['record_filter_survivors']==26624 and hist==saved['record_direction_histogram']
out={'status':'PASS independently regenerated first-visit feature diagnostic; not a family exclusion','image_domains':list(map(len,dom)),'feature_domains':list(map(len,features)),'assignments':count,'survivors':survive,'unsafe_first_L_iteration_bound':8,'unsafe_cell_bound':'9*initial_black_mass','note_sha256':hashlib.sha256((D/'pair_context_first_visit_filter.md').read_bytes()).hexdigest(),'diagnostic_sha256':hashlib.sha256((D/'pair_first_visit_features.json').read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
