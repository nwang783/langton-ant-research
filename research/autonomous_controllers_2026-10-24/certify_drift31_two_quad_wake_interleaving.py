#!/usr/bin/env python3
"""Symbolic all-parameter quadratic screen for the two-quadruple g8 wake family.
Affine step-two run overlaps, explicit integer-domain branch certificates.
"""
import json,sys,hashlib
from pathlib import Path
from itertools import combinations
ROOT=Path(__file__).resolve().parent
SOURCE=ROOT.parent/'sources/kehao95-core/wake_synthesis/verification/general_wake_parity'
sys.path.insert(0,str(SOURCE));import screen
Z=(0,0,0,0)
def C(c):return(c,0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def mul(a,n):return tuple(x*n for x in a)
def div(a,n):assert all(x%n==0 for x in a);return tuple(x//n for x in a)
def floor_aff(a,n):assert all(x%n==0 for x in a[1:]);return(a[0]//n,*(x//n for x in a[1:]))
def ceil_aff(a,n):return neg(floor_aff(neg(a),n))
def ev(a,v):return a[0]+sum(x*y for x,y in zip(a[1:],v))
def plus(a,n):return add(a,C(n))
U=(0,1,0,0);V=(0,0,1,0);W=(0,0,0,1)

def parameters(region):
 if region=='a_le_b':a=plus(U,2);b=add(a,V);c=plus(add(b,W),1)
 elif region=='b_lt_a_le_c':b=plus(U,1);a=plus(add(b,V),1);c=add(a,W)
 else:b=plus(U,1);c=plus(add(b,V),1);a=plus(add(c,W),1)
 return a,b,c

def runs(region,delta):
 a,b,c=parameters(region);A=plus(mul(a,6),1);B=plus(mul(b,6),2 if delta==1 else 5);D=plus(mul(c,6),2 if delta==1 else 5)
 order=[A,B,D]if region=='a_le_b'else[B,A,D]if region=='b_lt_a_le_c'else[B,D,A]
 ts=[C(0),C(1),C(2),C(5),C(6),*order];out=[]
 for lowT,highT in zip(ts[::2],ts[1::2]):
  L,R=neg(highT),neg(lowT)
  for r in range(3):
   low=ceil_aff(plus(L,-r),3);high=floor_aff(plus(R,-1-r),3)
   for parity in(0,1):
    first=plus(low,(parity-low[0])%2);last=plus(high,-((high[0]-parity)%2));n=plus(div(sub(last,first),2),1)
    assert all(x%2==0 for x in low[1:]+high[1:]);positive=(r+parity)%2==0;ly=neg(last);rx=(r+1)%3;ry=plus(ly,-int(r==2))
    sx,sy,tx,ty=(r,ly,rx,ry)if positive else(rx,ry,r,ly)
    out.append({'n':n,'sx':sx,'sy':sy,'tx':tx,'ty':ty,'positive':int(positive)})
 intervals=[(0,C(0),C(2)),(1,C(1),C(2)),(1,plus(mul(b,2),delta),plus(mul(c,2),delta)),(2,C(1),plus(mul(a,2),1))]
 for x,L,R in intervals:
  for parity in(0,1):
   y=plus(L,(parity-L[0])%2);n=plus(floor_aff(sub(plus(R,-1),y),2),1);positive=(x+parity)%2==1;sy=y if positive else plus(y,1);ty=plus(y,1)if positive else y
   out.append({'n':n,'sx':x,'sy':sy,'tx':x,'ty':ty,'positive':int(positive)})
 for q in out:
  assert all(x>=0 for x in q['n']) # Every retained symbolic run has n>=0.
  assert all(x%2==0 for x in q['sy'][1:]+q['ty'][1:])
 return out

class NeedSplit(Exception):
 def __init__(self,a):self.a=a

def reduced(a,domain):
 const=a[0]+sum(x*y for x,y in zip(a[1:],domain['offset']));coeff=[x if f else 0 for x,f in zip(a[1:],domain['free'])];return const,coeff

def sign(a,domain,trace):
 c,co=reduced(a,domain)
 if c>=0 and all(x>=0 for x in co):trace.append({'affine':a,'sign':'nonnegative','minimum':c});return 1
 if c<=0 and all(x<=0 for x in co):trace.append({'affine':a,'sign':'nonpositive','maximum':c});return-1
 if any(x>0 for x in co)and any(x<0 for x in co):raise RuntimeError(('mixed incomparable affine',a,domain,c,co))
 raise NeedSplit(a)

def maximum(a,b,domain,tr):return a if sign(sub(a,b),domain,tr)>=0 else b
def minimum(a,b,domain,tr):return b if sign(sub(a,b),domain,tr)>=0 else a

def signature(rr,domain):
 tr=[];E=Z
 for A,B in combinations(rr,2):
  sa=0 if(A['sx'],A['positive'])<(B['sx'],B['positive'])else -1
  da=sub(A['ty'],A['sy']);db=sub(B['ty'],B['sy']);delta=sub(da,db);assert not any(delta[1:]);tb=-delta[0]+(0 if(A['tx'],A['positive'])<(B['tx'],B['positive'])else -1)
  lo,hi=sorted((sa,tb))
  for v in range(lo+1,hi+1):
   if(sub(A['sy'],B['sy'])[0]-v)%2:continue
   start=maximum(A['sy'],plus(B['sy'],v),domain,tr)
   enda=add(A['sy'],mul(plus(A['n'],-1),2));endb=plus(add(B['sy'],mul(plus(B['n'],-1),2)),v)
   end=minimum(enda,endb,domain,tr);count=plus(div(sub(end,start),2),1)
   count=maximum(count,Z,domain,tr);E=add(E,count)
 Np=Z
 for r in rr:
  if r['positive']:Np=add(Np,r['n'])
 # Fixed C-parity: baseline T1,T5 plus A, plus either zero or two odd B/C.
 Cparity=1;q=plus(add(E,Np),Cparity);constant,co=reduced(q,domain);assert all(x%2==0 for x in co),(q,domain)
 return{'E_affine':E,'positive_edges_affine':Np,'C_parity':Cparity,'signature':constant%2,'all_comparison_proofs':tr}

def cover(rr):
 nodes=[]
 def visit(domain):
  ident=len(nodes);n={'id':ident,'integer_domain':domain};nodes.append(n)
  try:n.update(leaf='symbolic_affine',result=signature(rr,domain))
  except NeedSplit as e:
   const,coef=reduced(e.a,domain);var=next(i for i,x in enumerate(coef)if x!=0);n.update(split_variable=var,undecided_affine=e.a,children=[])
   zero={'offset':list(domain['offset']),'free':list(domain['free'])};zero['free'][var]=False
   rest={'offset':list(domain['offset']),'free':list(domain['free'])};rest['offset'][var]+=1
   n['children']=[visit(zero),visit(rest)]
  return ident
 visit({'offset':[0,0,0],'free':[True,True,True]});return nodes

def main():
 results=[]
 for delta in(1,2):
  for region in('a_le_b','b_lt_a_le_c','a_gt_c'):
   rr=runs(region,delta);nodes=cover(rr);expected=int(region!='b_lt_a_le_c');assert all(n['result']['signature']==expected for n in nodes if 'result'in n)
   # Literal compressed-run comparisons are controls, not interpolation proof.
   controls=[]
   for v in((0,0,0),(1,2,3),(5,0,2),(10**30,10**20,10**10)):
    a,b,c=[ev(x,v)for x in parameters(region)];ss=2 if delta==1 else 5;T=[0,1,2,5,6,6*a+1,6*b+ss,6*c+ss];O=[(-t,0)for t in T]
    literal=screen.runs_for(O,(3,1));mine=[]
    for r in rr:
     n=ev(r['n'],v)
     if n:mine.append(screen.Run(n,2,ev(r['sy'],v),r['sx'],ev(r['ty'],v),r['tx'],r['positive']))
    key=lambda r:(r.sy,r.sx,r.positive,r.ty,r.tx,r.step,r.n);assert sorted(mine,key=key)==literal
    z=screen.screen(O,(3,1));assert z['winding']==1 and z['signature']==expected;controls.append({'parameters':[a,b,c],'raw_nonnegative_parameters':v,'screen':z})
   results.append({'delta':delta,'region':region,'a_b_c_affine':parameters(region),'symbolic_runs':rr,'complete_integer_domain_tree':nodes,'literal_controls':controls,'required_signature':0,'proved_signature':expected});print(delta,region,'nodes',len(nodes),'leaves',sum('result'in n for n in nodes),'q',expected,flush=True)
 result={'scope':__doc__,'definition':'O_T={0,1,2,5,6,6a+1,6b+s,6c+s}, s in{2,5}, a>=2,1<=b<c. Physical representatives(-T,0), full drift(3,1).','screen_source_sha256':hashlib.sha256((SOURCE/'screen.py').read_bytes()).hexdigest(),'all_cases':results,'theorem':'All signed residues and winding pass; quadratic q=0 exactly when b<a<=c. NOT_EXCLUDED is not realizability.'}
 (ROOT/'drift31_two_quad_wake_interleaving_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
if __name__=='__main__':main()
