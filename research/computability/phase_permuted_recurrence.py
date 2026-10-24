#!/usr/bin/env python3
"""Exact visit equality for finite-phase, permutation-coupled expanding paths.
P_c(kn+j)=a*P_perm[s][j][c](n)+off[s][j][c], S(kn+j)=nxt[s][j].
The phase permutation may depend on the finite control and input digit.
"""
from dataclasses import dataclass
from math import isqrt
from automatic_radix import Rel
from selfsimilar_visit_relations import add,sub,mul
import json

@dataclass
class PhaseRecurrence:
 base:int
 scale:tuple
 nxt:list
 perm:list
 off:list
 start:int=0
 def validate(self):
  assert self.base>=2 and sum(v*v for v in self.scale)>1
  assert len(self.nxt)==len(self.perm)==len(self.off)>0
  self.phases=len(self.perm[0][0]);assert self.phases>0
  assert self.nxt[self.start][0]==self.start
  for s in range(len(self.nxt)):
   assert len(self.nxt[s])==len(self.perm[s])==len(self.off[s])==self.base
   for j in range(self.base):
    assert 0<=self.nxt[s][j]<len(self.nxt)
    assert sorted(self.perm[s][j])==list(range(self.phases))
    assert len(self.off[s][j])==self.phases
  assert all(v==(0,0)for v in self.off[self.start][0])
 def state(self,n):
  ds=[]
  while n:ds.append(n%self.base);n//=self.base
  s=self.start
  for j in reversed(ds):s=self.nxt[s][j]
  return s
 def point(self,n,phase=0):
  self.validate();assert n>=0 and 0<=phase<self.phases
  if not n:return (0,0)
  q,j=divmod(n,self.base);s=self.state(q)
  return add(mul(self.scale,self.point(q,self.perm[s][j][phase])),self.off[s][j][phase])
 def difference_machine(self,max_target_norm=1):
  self.validate();b=self.base;l=self.phases;norm=sum(v*v for v in self.scale)
  n=max(x*x+y*y for row in self.off for cell in row for x,y in cell)
  m=isqrt(n)+(isqrt(n)**2<n);delta=2*m;r=max_target_norm
  while norm*r*r<(r+delta)**2:r+=1
  inverse=[]
  for row in self.perm:
   inverse.append([[p.index(c)for c in range(l)]for p in row])
  states=[(self.start,self.start,c,d,(0,0))for c in range(l)for d in range(l)]
  starts=set(range(len(states)));ix={v:i for i,v in enumerate(states)};tr=[]
  for st in states:
   row=[]
   for code in range(b*b):
    j=code%b;k=code//b;ns=None
    if st is not None:
     s,t,c,d,D=st;nc=inverse[s][j][c];nd=inverse[t][k][d]
     DD=add(mul(self.scale,D),sub(self.off[s][j][nc],self.off[t][k][nd]))
     if DD[0]**2+DD[1]**2<=r*r:ns=(self.nxt[s][j],self.nxt[t][k],nc,nd,DD)
    if ns not in ix:ix[ns]=len(states);states.append(ns)
    row.append(ix[ns])
   tr.append(row)
  alpha=b*b;back=[[set()for _ in tr]for _ in range(alpha)]
  for q,row in enumerate(tr):
   for j,t in enumerate(row):back[j][t].add(q)
  def relation(target=(0,0),phases=(0,0)):
   assert sum(v*v for v in target)<=max_target_norm**2
   finals={i for i,v in enumerate(states)if v is not None and v[2:4]==phases and v[4]==target}
   # Reverse the multiple-start MSB machine and determinize. Acceptance is
   # intersection with ANY original start, not one arbitrarily chosen phase.
   subsets=[frozenset(finals)];ids={subsets[0]:0};out=[];accept=set()
   for i,qs in enumerate(subsets):
    if qs&starts:accept.add(i)
    row=[]
    for j in range(alpha):
     ns=frozenset(q for t in qs for q in back[j][t])
     if ns not in ids:ids[ns]=len(subsets);subsets.append(ns)
     row.append(ids[ns])
    out.append(row)
   return Rel(('s','t'),out,accept,b).minimal()
  return relation,dict(raw_difference_states=len(states),carry_radius=r,phases=l)

def controls():
 models=[PhaseRecurrence(2,(-2,0),[[0,0]],[[[1,0],[1,0]]],[[[(0,0),(0,0)],[(1,0),(-1,0)]]]),
         PhaseRecurrence(3,(2,0),[[0,0,0]],[[[0,1],[1,0],[0,1]]],[[[(0,0),(0,0)],[(1,0),(0,1)],[(0,1),(1,0)]]])]
 out=[]
 for k,m in enumerate(models):
  rs,meta=m.difference_machine(1);ps=[[m.point(n,c)for n in range(70)]for c in range(2)];checks=0
  if k==0:
   assert ps[0]==[(n,0)for n in range(70)] and ps[1]==[(-n,0)for n in range(70)]
  for c in range(2):
   for d in range(2):
    for target in [(0,0),(1,0),(0,1)]:
     rel=rs(target,(c,d))
     for s in range(70):
      for t in range(70):
       assert rel.eval(s=s,t=t)==(sub(ps[c][s],ps[d][t])==target);checks+=1
  out.append(dict(model=k,**meta,comparison_controls=checks))
 return dict(status='PASS finite phase/carry implementation controls; no ant model claimed',cases=out)
if __name__=='__main__':
 from pathlib import Path
 out=controls();Path(__file__).with_name('phase_permuted_recurrence_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
