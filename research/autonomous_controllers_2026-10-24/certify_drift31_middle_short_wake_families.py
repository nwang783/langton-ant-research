#!/usr/bin/env python3
"""All-parameter quadratic screens for three residual families of the middle
short mode. Necessary wake obstruction only, not chronology or realization.
"""
import itertools,json,hashlib
from pathlib import Path
import certify_drift31_two_quad_wake_interleaving as a
ROOT=Path(__file__).resolve().parent
BASE=[0,1,2,6,7]
FAMILIES={'r2':{'P':(2,1),'Q':(2,2),'N':(5,1)},'r0':{'P':(2,1),'Q':(0,2),'N':(3,1)},'r1':{'P':(2,1),'Q':(4,1),'N':(1,2)}}

def params(family,order):
 cfg=FAMILIES[family];nums={};previous=None
 for i,label in enumerate(order):
  r,L=cfg[label]
  if i==0:n=a.plus(a.U,L)
  else:n=a.add(a.plus(previous,int(cfg[order[i-1]][0]>=r)),[a.U,a.V,a.W][i])
  nums[label]=n;previous=n
 Ts={z:a.plus(a.mul(n,6),cfg[z][0])for z,n in nums.items()}
 bounds=[a.plus(nums[z],-cfg[z][1])for z in order]
 return nums,Ts,bounds

def runs(Ts):
 out=[]
 for lowT,highT in zip(Ts[::2],Ts[1::2]):
  L,R=a.neg(highT),a.neg(lowT)
  for r in range(3):
   low=a.ceil_aff(a.plus(L,-r),3);high=a.floor_aff(a.plus(R,-1-r),3)
   for parity in(0,1):
    first=a.plus(low,(parity-low[0])%2);last=a.plus(high,-((high[0]-parity)%2));n=a.plus(a.div(a.sub(last,first),2),1)
    positive=(r+parity)%2==0;ly=a.neg(last);rx=(r+1)%3;ry=a.plus(ly,-int(r==2));sx,sy,tx,ty=(r,ly,rx,ry)if positive else(rx,ry,r,ly)
    out.append({'n':n,'sx':sx,'sy':sy,'tx':tx,'ty':ty,'positive':int(positive)})
 groups={r:[]for r in range(3)}
 for T in Ts:
  x=(-T[0])%3;y=a.div(a.plus(T,x),3);groups[x].append(y)
 for x,ys in groups.items():
  assert len(ys)%2==0
  for L,R in zip(ys[::2],ys[1::2]):
   for parity in(0,1):
    y=a.plus(L,(parity-L[0])%2);n=a.plus(a.floor_aff(a.sub(a.plus(R,-1),y),2),1);positive=(x+parity)%2==1;sy=y if positive else a.plus(y,1);ty=a.plus(y,1)if positive else y
    out.append({'n':n,'sx':x,'sy':sy,'tx':x,'ty':ty,'positive':int(positive)})
 return out

def cover(rr,bounds):
 nodes=[]
 def visit(domain):
  i=len(nodes);node={'id':i,'integer_domain':domain};nodes.append(node)
  for b in bounds:
   c,co=a.reduced(b,domain)
   if c<0 and all(x==0 for x in co):node.update(leaf='invalid_parameter_domain',violated_bound=b,maximum=c);return i
  try:
   bt=[]
   for b in bounds:
    c,co=a.reduced(b,domain)
    assert all(x>=0 for x in co)
    if c<0:raise a.NeedSplit(b)
    bt.append({'affine':b,'minimum':c})
   node.update(leaf='symbolic_affine',parameter_bound_proofs=bt,result=a.signature(rr,domain))
  except a.NeedSplit as e:
   c,co=a.reduced(e.a,domain);v=next(i for i,x in enumerate(co)if x!=0);node.update(split_variable=v,undecided_affine=e.a)
   z={'offset':list(domain['offset']),'free':list(domain['free'])};z['free'][v]=False
   r={'offset':list(domain['offset']),'free':list(domain['free'])};r['offset'][v]+=1
   node['children']=[visit(z),visit(r)]
  return i
 visit({'offset':[0,0,0],'free':[True,True,True]});return nodes

def main():
 cases=[]
 for family,cfg in FAMILIES.items():
  for oo in itertools.permutations('PQN'):
   order=''.join(oo)
   if family=='r2'and order.index('P')>order.index('Q'):continue
   ns,tt,bb=params(family,order);Ts=[a.C(t)for t in BASE]+[tt[z]for z in order];rr=runs(Ts);nodes=cover(rr,bb)
   signatures={x['result']['signature']for x in nodes if x.get('leaf')=='symbolic_affine'}
   expect=1 if family=='r2'else int(order not in ('NPQ','QPN'))
   assert signatures=={expect},(family,order,signatures)
   controls=[]
   for v in itertools.product(range(3),repeat=3):
    if any(a.ev(b,v)<0 for b in bb):continue
    T=[a.ev(t,v)for t in Ts];O=[(-t,0)for t in T];literal=a.screen.runs_for(O,(3,1));mine=[]
    for r in rr:
     n=a.ev(r['n'],v);assert n>=0
     if n:mine.append(a.screen.Run(n,2,a.ev(r['sy'],v),r['sx'],a.ev(r['ty'],v),r['tx'],r['positive']))
    key=lambda r:(r.sy,r.sx,r.positive,r.ty,r.tx,r.step,r.n);assert sorted(mine,key=key)==literal
    s=a.screen.screen(O,(3,1));assert s['signature']==expect and s['winding']==1;controls.append({'raw_parameters':v,'normal_odd_levels':T,'signature':s['signature']})
   cases.append({'family':family,'actual_position_order':order,'integer_parameters_affine':ns,'variable_levels_affine':tt,'parameter_bounds_nonnegative':bb,'symbolic_runs':rr,'domain_tree':nodes,'proved_signature':expect,'literal_controls':controls});print(family,order,'nodes',len(nodes),'q',expect,flush=True)
 result={'scope':__doc__,'base_odd_levels':BASE,'family_definitions':'r2: P=6a+2,Q=6b+2,N=6c+5 with1<=a<b,c>=1; r0:P=6a+2,Q=6b,N=6c+3 witha,c>=1,b>=2; r1:P=6a+2,Q=6b+4,N=6c+1 witha,b>=1,c>=2.','all_cases':cases,'theorem':'r2 always fails q. In r0/r1, q0 exactly for N<P<Q or Q<P<N. The latter has odd maximum and is separately impossible by the signed read-maximum lemma.','source_hashes':{f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest()for f in ['certify_drift31_two_quad_wake_interleaving.py','DRIFT31_TWO_QUAD_EXTREME_READ_EXCLUSIONS.md']},'warning':'Only the middle short T6=NNNSS,T7=EEEWW has this full residual inventory. Other two short modes remain unclassified.'}
 (ROOT/'drift31_middle_short_wake_families_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
if __name__=='__main__':main()
