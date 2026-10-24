from pathlib import Path
from itertools import combinations
import hashlib,json
R=Path('/workspace/shared/langton');P=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for line in(P/'DRIFT31_WAKE_INTERLEAVING_SHA256SUMS').read_text().splitlines():h,f=line.split(None,1);assert sha(P/f)==h
J=json.loads((P/'drift31_two_quad_wake_interleaving_certificate.json').read_text())
z=(0,0,0,0);u=(0,1,0,0);v=(0,0,1,0);w=(0,0,0,1);C=lambda n:(n,0,0,0);add=lambda a,b:tuple(x+y for x,y in zip(a,b));scale=lambda a,n:tuple(x*n for x in a);sub=lambda a,b:add(a,scale(b,-1));inc=lambda a,n:add(a,C(n))
def fl(a,n):assert all(c%n==0 for c in a[1:]);return(a[0]//n,*(c//n for c in a[1:]))
def ce(a,n):return scale(fl(scale(a,-1),n),-1)
def half(a):assert all(c%2==0 for c in a);return tuple(c//2 for c in a)
def pars(reg):
 if reg=='a_le_b':a=inc(u,2);b=add(a,v);c=inc(add(b,w),1)
 elif reg=='b_lt_a_le_c':b=inc(u,1);a=inc(add(b,v),1);c=add(a,w)
 else:b=inc(u,1);c=inc(add(b,v),1);a=inc(add(c,w),1)
 return a,b,c

def build(reg,s):
 a,b,c=pars(reg);A=inc(scale(a,6),1);B=inc(scale(b,6),s);D=inc(scale(c,6),s)
 tail={'a_le_b':[A,B,D],'b_lt_a_le_c':[B,A,D],'a_gt_c':[B,D,A]}[reg];ts=[C(i)for i in[0,1,2,5,6]]+tail;rr=[]
 for tlo,thi in zip(ts[::2],ts[1::2]):
  # Horizontal physical left endpoints X in [-thi,-tlo), split X=r+3k.
  for r in range(3):
   lo=ce(inc(scale(thi,-1),-r),3);hi=fl(inc(scale(tlo,-1),-1-r),3)
   for p in(0,1):
    first=inc(lo,(p-lo[0])%2);last=inc(hi,-((hi[0]-p)%2));n=inc(half(sub(last,first)),1);ly=scale(last,-1);rx=(r+1)%3;ry=inc(ly,-(r==2));pos=(r+p)%2==0
    sx,sy,tx,ty=(r,ly,rx,ry)if pos else(rx,ry,r,ly);rr.append(dict(n=n,sx=sx,sy=sy,tx=tx,ty=ty,positive=int(pos)))
 delta=1 if s==2 else 2
 # Canonical O coordinates from (-T,0), r=-T mod3, y=(T+r)/3.
 intervals=[(0,C(0),C(2)),(1,C(1),C(2)),(1,inc(scale(b,2),delta),inc(scale(c,2),delta)),(2,C(1),inc(scale(a,2),1))]
 for x,lo,hi in intervals:
  for p in(0,1):
   first=inc(lo,(p-lo[0])%2);last=inc(inc(hi,-1),-((hi[0]-1-p)%2));n=inc(half(sub(last,first)),1);pos=(x+p)%2==1
   rr.append(dict(n=n,sx=x,sy=first if pos else inc(first,1),tx=x,ty=inc(first,1)if pos else first,positive=int(pos)))
 assert len(rr)==32 and all(all(c>=0 for c in r['n'])for r in rr)
 return rr

def reduce(a,D):return (a[0]+sum(c*x for c,x in zip(a[1:],D['offset'])),*(c if f else 0 for c,f in zip(a[1:],D['free'])))
def ge(a,D):return all(x>=0 for x in reduce(a,D))
def maxx(a,b,D):
 t=sub(a,b)
 if ge(t,D):return a
 assert ge(scale(t,-1),D);return b

def minn(a,b,D):return scale(maxx(scale(a,-1),scale(b,-1),D),-1)
def qproof(rr,D):
 E=z;NP=z
 for a in rr:
  if a['positive']:NP=add(NP,a['n'])
 for a,b in combinations(rr,2):
  source_threshold=0 if(a['sx'],a['positive'])<(b['sx'],b['positive'])else-1
  da=sub(a['ty'],a['sy']);db=sub(b['ty'],b['sy']);delta=sub(da,db);assert delta[1:]==(0,0,0)
  target_threshold=-delta[0]+(0 if(a['tx'],a['positive'])<(b['tx'],b['positive'])else-1)
  low,high=sorted((source_threshold,target_threshold))
  for dif in range(low+1,high+1):
   if(sub(a['sy'],b['sy'])[0]-dif)%2:continue
   begin=maxx(a['sy'],inc(b['sy'],dif),D)
   enda=add(a['sy'],scale(inc(a['n'],-1),2));endb=inc(add(b['sy'],scale(inc(b['n'],-1),2)),dif)
   end=minn(enda,endb,D);num=maxx(inc(half(sub(end,begin)),1),z,D);E=add(E,num)
 return E,NP,inc(add(E,NP),1)
nodes=leaves=comparisons=0
for case in J['all_cases']:
 reg=case['region'];s=2 if case['delta']==1 else 5;rr=build(reg,s)
 assert json.dumps(rr)==json.dumps(case['symbolic_runs'])and json.dumps(pars(reg))==json.dumps(case['a_b_c_affine'])
 tree=case['complete_integer_domain_tree'];seen=set()
 def visit(i,D):
  global nodes,leaves,comparisons
  assert i not in seen;seen.add(i);node=tree[i];nodes+=1;assert node['id']==i and node['integer_domain']==D
  if 'children'in node:
   k=node['split_variable'];assert D['free'][k];zero={'offset':D['offset'][:],'free':D['free'][:]};zero['free'][k]=False
   rest={'offset':D['offset'][:],'free':D['free'][:]};rest['offset'][k]+=1
   visit(node['children'][0],zero);visit(node['children'][1],rest);return
  leaves+=1;E,NP,Q=qproof(rr,D);res=node['result'];assert reduce(sub(E,tuple(res['E_affine'])),D)==z and reduce(sub(NP,tuple(res['positive_edges_affine'])),D)==z
  qr=reduce(Q,D);assert all(c%2==0 for c in qr[1:])and qr[0]%2==res['signature']==int(reg!='b_lt_a_le_c')and res['C_parity']==1
  for tr in res['all_comparison_proofs']:
   a=tuple(tr['affine']);red=reduce(a,D);comparisons+=1
   if tr['sign']=='nonnegative':assert all(x>=0 for x in red)and red[0]==tr['minimum']
   else:assert all(x<=0 for x in red)and red[0]==tr['maximum']
 visit(0,{'offset':[0,0,0],'free':[True,True,True]});assert len(seen)==len(tree)
assert(nodes,leaves)==(10,8)
# Tight signed-fibre residual demand is derived from the COMPLETE named prefix.
known=[0,1,2,5,6];sums=[sum((-1)**t for t in known if(-t)%3==r)for r in range(3)];assert sums==[2,0,-1]
assert [min((2-a)%4,(a-2)%4)for a in sums]==[0,2,1]
report={'status':'PASS exact full-inventory quadratic interleaving, conditional on live two-quadruple F-circle branch','proof_sha256':sha(P/'DRIFT31_TWO_QUAD_FULL_WAKE_INTERLEAVING.md'),'certificate_sha256':sha(P/'drift31_two_quad_wake_interleaving_certificate.json'),'script_sha256':sha(Path(__file__)),'integer_cover_nodes':nodes,'integer_cover_leaves':leaves,'verified_affine_comparisons':comparisons,'result':'q=0 iff b<a<=c for a>=2,1<=b<c,s=2 or5','analytic_scope':['Complete named histories atT0..7 plus single-used right-support confine all remaining odd classes above7. Exact three remaining full odd classes saturate fibre deficits: one negative at6a+1 and a same-checker pair6b+s,6c+s, not subtraction of a physical wake.','All three relative integer order regions parametrized bijectively with u,v,w>=0; boundary equalities a=b and a=c retained.','Independent exact affine endpoint pairing reconstructs all32 horizontal/vertical runs. Every zero-length run remains empty. Source/target inversion thresholds and step2 overlap cardinalities give exact parity, not interpolation.','All six sign/order cases checked through complete finite domain trees and coefficientwise inequalities; every free coefficient of resulting parity is even.','Uses attributed retained nonaxis full-wake q=1+a obstruction with actual entire O and full d(3,1), plus finite-support realization of complete WHITE front. No passing-set realization or growth8 branch exclusion follows.'],'not_claimed':['controller realization','chronological incompatibility with interleaving','cyclic-E application','general g8 exclusion']}
p=R/'audits/drift31_wake_interleaving_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
