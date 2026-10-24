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

import itertools,collections
for line in(P/'DRIFT31_MIDDLE_SHORT_FULL_ODD_SHA256SUMS').read_text().splitlines():
 h,f=line.split(None,1);assert sha(P/f)==h
J=json.loads((P/'drift31_middle_short_wake_families_certificate.json').read_text());cfg={'r2':{'P':(2,1),'Q':(2,2),'N':(5,1)},'r0':{'P':(2,1),'Q':(0,2),'N':(3,1)},'r1':{'P':(2,1),'Q':(4,1),'N':(1,2)}}
def newpars(f,order):
 ns={};axes=[u,v,w];prev=None
 for i,label in enumerate(order):
  rem,lo=cfg[f][label]
  ns[label]=inc(axes[0],lo)if i==0 else add(inc(prev,int(cfg[f][order[i-1]][0]>=rem)),axes[i]);prev=ns[label]
 ts={k:inc(scale(a,6),cfg[f][k][0])for k,a in ns.items()};bounds=[inc(ns[k],-cfg[f][k][1])for k in order];return ns,ts,bounds

def newruns(ts):
 rr=[]
 for loT,hiT in zip(ts[::2],ts[1::2]):
  for x in range(3):
   lo=ce(inc(scale(hiT,-1),-x),3);hi=fl(inc(scale(loT,-1),-1-x),3)
   for par in[0,1]:
    fst=inc(lo,(par-lo[0])%2);last=inc(hi,-((hi[0]-par)%2));n=inc(half(sub(last,fst)),1);ly=scale(last,-1);rx=(x+1)%3;ry=inc(ly,-int(x==2));positive=(x+par)%2==0
    sx,sy,tx,ty=(x,ly,rx,ry)if positive else(rx,ry,x,ly);rr.append(dict(n=n,sx=sx,sy=sy,tx=tx,ty=ty,positive=int(positive)))
 for x in range(3):
  ys=[fl(inc(t,x),3)for t in ts if(-t[0])%3==x];assert len(ys)%2==0
  for low,hi in zip(ys[::2],ys[1::2]):
   for par in[0,1]:
    fst=inc(low,(par-low[0])%2);last=inc(inc(hi,-1),-((hi[0]-1-par)%2));n=inc(half(sub(last,fst)),1);positive=(x+par)%2==1
    rr.append(dict(n=n,sx=x,sy=fst if positive else inc(fst,1),tx=x,ty=inc(fst,1)if positive else fst,positive=int(positive)))
 return rr
nodes=leaves=compares=0;cases=set();qvalues={}
for case in J['all_cases']:
 f,order=case['family'],case['actual_position_order'];assert(f,order)not in cases;cases.add((f,order));ns,tt,bb=newpars(f,order);ts=[C(i)for i in[0,1,2,6,7]]+[tt[k]for k in order];rr=newruns(ts)
 assert json.dumps(ns)==json.dumps(case['integer_parameters_affine'])and json.dumps(tt)==json.dumps(case['variable_levels_affine'])and json.dumps(bb)==json.dumps(case['parameter_bounds_nonnegative'])and json.dumps(rr)==json.dumps(case['symbolic_runs'])
 # Exact checker endpoint and winding parities, all coefficients even.
 cterm=sum(t[0]%2 for t in ts)%2;Y=z
 for t in ts:Y=add(Y,fl(inc(t,(-t[0])%3),3))
 assert cterm==1 and Y[0]%2==1 and all(x%2==0 for x in Y[1:])
 expected=1 if f=='r2'else int(order not in['NPQ','QPN']);assert expected==case['proved_signature'];tree=case['domain_tree'];seen=set()
 def visit(i,D):
  global nodes,leaves,compares
  assert i not in seen;seen.add(i);node=tree[i];nodes+=1;assert node['id']==i and node['integer_domain']==D
  if'children'in node:
   k=node['split_variable'];assert D['free'][k];a={'offset':D['offset'][:],'free':D['free'][:]};a['free'][k]=False;b={'offset':D['offset'][:],'free':D['free'][:]};b['offset'][k]+=1;visit(node['children'][0],a);visit(node['children'][1],b);return
  leaves+=1
  if node['leaf']=='invalid_parameter_domain':
   bv=tuple(node['violated_bound']);assert bv in bb;red=reduce(bv,D);assert red[0]<0 and red[1:]==(0,0,0)and node['maximum']==red[0];return
  assert node['leaf']=='symbolic_affine'
  assert len(node['parameter_bound_proofs'])==len(bb)
  for bd,pr in zip(bb,node['parameter_bound_proofs']):assert list(bd)==pr['affine']and ge(bd,D)and reduce(bd,D)[0]==pr['minimum']
  assert all(ge(r['n'],D)for r in rr)
  E,NP,Q=qproof(rr,D);res=node['result'];assert reduce(sub(E,tuple(res['E_affine'])),D)==z and reduce(sub(NP,tuple(res['positive_edges_affine'])),D)==z
  qr=reduce(Q,D);assert all(c%2==0 for c in qr[1:])and qr[0]%2==res['signature']==expected and res['C_parity']==1
  for pr in res['all_comparison_proofs']:
   red=reduce(tuple(pr['affine']),D);compares+=1
   if pr['sign']=='nonnegative':assert all(a>=0 for a in red)and red[0]==pr['minimum']
   else:assert all(a<=0 for a in red)and red[0]==pr['maximum']
 visit(0,{'offset':[0,0,0],'free':[True,True,True]});assert len(seen)==len(tree);qvalues[f,order]=expected
assert len(cases)==15 and cases=={(f,''.join(o))for f in cfg for o in itertools.permutations('PQN')if f!='r2'or o.index('P')<o.index('Q')}
assert(nodes,leaves)==(41,28)
# Exhaust all signed residue allocations for the three remaining actual odd classes.
known=[0,1,2,6,7];charges=[sum((-1)**t for t in known if t%3==r)for r in range(3)];assert charges==[2,-2,1];alloc=[]
for a in itertools.combinations_with_replacement([(r,s)for r in range(3)for s in[-1,1]],3):
 if all((charges[r]+sum(s for rr,s in a if rr==r))%4==2 for r in range(3)):alloc.append(a)
expected_alloc=[((2,-1),(2,-1),(2,-1)),((2,-1),(2,1),(2,1)),((0,-1),(0,1),(2,1)),((1,-1),(1,1),(2,1))];assert set(alloc)==set(expected_alloc)
report={'status':'PASS conditional middle-short FULL odd inventory reduces to {0,1,2,6,7,6c+1,6a+2,6a+4},2<=c<=a','proof_sha256':sha(P/'DRIFT31_MIDDLE_SHORT_FULL_ODD_REDUCTION.md'),'certificate_sha256':sha(P/'drift31_middle_short_wake_families_certificate.json'),'script_sha256':sha(Path(__file__)),'residual_signed_allocations':alloc,'order_cases':len(cases),'integer_tree_nodes':nodes,'integer_tree_leaves':leaves,'verified_affine_comparisons':compares,'analytic_checks':['Actual complete middle-shortprefix fixes5oddclasses0,1,2,6,7; g8 leavesEXACT3actualfullclassesT>=8. All signedresidue allocations exhaustively checked; allnegative hasodd fullreadmaxandfails. No partialwake subtraction.','15 strictpositionorders parametrizedbijectively bynonnegativegaps withtrue lowerbounds andr2P<Q;41node domain trees exhaustallintegerparameters. Affinehorizontal/verticalruns independentlyrebuilt; everyvalidleaf hasnonnegativelengths, exact overlapcount parity andchecker/windingterms.','r2q1always; r0/r1q0onlyNPQorQPN. QPNnegativeoddmaxfailsactualREADextreme.','r0NPQ givesa<=b-1,c<=a-1; a<=b-2 violates6gap, a=b-1 leavesonlyM-4oddnearmaxandviolatesrefined5positiongap. r1NPQ givesc<=a<=b; a<b violates6gap, hencea=b and2<=c<=a.','Both c=a andc<a remainOPEN; supplieda=c=2separateexclusion doesnotextendtoallparameters. Conditionalonspecificmiddleallquadmode, fullgrowth8anddrift3,1.'],'not_claimed':['middlemodeclosed','other2shortmodesclassified','passinginventoryrealization','singleusedcircleexistence','globalattraction']}
p=R/'audits/drift31_middle_short_full_odd_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
