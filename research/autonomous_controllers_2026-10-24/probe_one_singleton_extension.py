#!/usr/bin/env python3
"""Discovery continuation of the six signed-cover candidates; no claims."""
import json
from itertools import product
from collections import Counter
import probe_boundary_extension as p
from probe_consecutive_port_generator import generate
TARGETS=[v for v in product(range(9),repeat=4)if sum(v)==8 and all(x%4==2 for x in[v[0]-v[1],v[3]-v[2],v[0]-v[2],v[3]-v[1]])]
def fits(H):
 v=[0]*4
 for i,h in enumerate(H):
  if len(h)%2:
   t=i//2-1;r=i%2;v[2*r+(t-r)%2]+=1
 return [a for a in TARGETS if all(x<=y for x,y in zip(v,a))]
def extend(H):
 k,g=p.graph(H);assert k=='open';rel=p.relations(H,g);a,b=H[-2:];isC=(len(H)//2-1)%2==1
 oc=lambda hs,d:sum((x+(1 if k%2==0 else-1))%4==d for k,x in enumerate(hs))
 if isC:I0,J0,I1,J1=oc(b,1),a.count(2),oc(a,1),b.count(2)
 else:I0,J0,I1,J1=oc(a,0),b.count(3),oc(b,0),a.count(3)
 q=generate(I0,J0,isC,rel[0]);r=generate(I1,J1,isC,rel[1]);out=[];cc=Counter({'candidates':len(q)*len(r)})
 if len(q)*len(r)>100000:return None,cc
 for aa,bb in product(q,r):
  HH=H+[aa,bb]
  if not fits(HH):cc['residue_budget']+=1;continue
  k,g=p.graph(HH)
  if k=='open'and p.positive_clock_cycle(HH,g):k='clock'
  cc[k]+=1
  if k=='open':out.append(HH)
 return out,cc
if __name__=='__main__':
 cert=json.load(open('certify_diagonal_read_minimum.json'));F=[]
 for c in cert['cases'][:4]:
  for s in c.get('survivors',[]):F.append([tuple(h)for h in c['lower_headings']+s['A_headings']])
 for step in range(1,4):
  S=Counter();new=[]
  for i,H in enumerate(F):
   out,cc=extend(H);S.update(cc)
   if out is None:S['large_unprocessed']+=1
   else:new.extend(out)
  print(step,len(new),dict(S),flush=True)
  json.dump(new,open('/tmp/one_singleton_step%d.json'%step,'w'))
  if S['large_unprocessed']or len(new)>1000:break
  F=new
