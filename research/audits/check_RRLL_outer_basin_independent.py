from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
P=D/'pure_RRLL_one_use_reader_graph_has_a_closed_first_R_basin.md';Jf=D/'check_RRLL_outer_reader_basin.json'
assert sha(P)=='b4a5265e598157577cc9f34e1ccfef206012b9496fa0fca91d6d88049963e430' and sha(Jf).startswith('72c15c7d') and sha(D/'check_RRLL_outer_reader_basin.py').startswith('91177984')
J=json.loads(Jf.read_text());lib=S.parent/'check_global_max_flow2_staircase_independent.py';N={'__file__':str(lib)};exec(lib.read_text().split('rows=[];stats=Counter()')[0],N);cv,out,test,V=[N[k]for k in('cv','out','test','V')];xy=lambda p:[int(p.real),int(p.imag)]
def enc(w):
 if isinstance(w,complex):return xy(w)
 if isinstance(w,(list,tuple)):return[enc(x)for x in w]
 return w
words=lambda a:[''.join(w)for n in range(5)for w in product(a,repeat=n)]
Gs=[w for w in words('NS')if w.count('S')==1];Fs=[w for w in words('EW')if sum(out(cv(w),r)==0 for r in range(len(w)))==1];assert Gs==J['G_domain']and Fs==J['F_domain']and len(Gs)==len(Fs)==10
families={'T':(0+1j,'E'),'R':(1+1j,'N'),'C':(0j,'NNSN'),'A':(1+0j,'WWEW'),'D':(-1j,'WWWE'),'E':(1-1j,'SSSN')}
def fixed(j):return{p+2*j:cv(w)for p,w in families.values()}
def patch(z,j=0):return fixed(j)|{2*j-2j:cv(z[0]),2*j+1-2j:cv(z[1])}
# Python 2j is complex while 2*j is the integer unit translation.
def check(hs):
 k,w=test(hs);assert k in['port','clock','open']
 if k=='port':
  for p,s in hs.items():
   for h,v in enumerate(V):
    q=p+v
    if q not in hs:continue
    a=[r for r in range(len(s))if out(s,r)==h];b=[r for r,c in enumerate(hs[q])if c==h]
    if len(a)!=len(b):return k,[xy(p),xy(q),h,a,b]
  assert False
 if k=='clock':
  edges=set()
  for p,s in hs.items():
   for r in range(len(s)-1):edges.add(((p,r),(p,r+1),4))
   for h,v in enumerate(V):
    q=p+v
    if q not in hs:continue
    a=[r for r in range(len(s))if out(s,r)==h];b=[r for r,c in enumerate(hs[q])if c==h];assert len(a)==len(b)
    for r,t in zip(a,b):edges.add(((p,r),(q,t),1));edges.add(((q,t),(p,r),-1))
  assert all(tuple(e)in edges for e in w)and sum(e[2]for e in w)>0
  assert all(w[i][0]==w[(i+1)%len(w)][1]for i in range(len(w)))
 return k,enc(w)
states=[];nodes=[];nc=Counter()
for z in product(Gs,Fs):
 k,w=check(patch(z));nodes.append(dict(state=z,result=k,witness=w));nc[k]+=1
 if k=='open':states.append(z)
assert list(map(list,states))==J['states']and nc=={'port':70,'clock':6,'open':24}
pairs=[];edges=[];ec=Counter()
for i,z in enumerate(states):
 for j,w in enumerate(states):
  k,wi=check(patch(z)|patch(w,1));ec[k]+=1;pairs.append(dict(source=i,target=j,result=k,witness=wi));assert ('clock_cycle'if k=='clock'else k)==J['edge_rows'][24*i+j]['result']
  if k=='open':edges.append((i,j))
assert ec=={'port':422,'clock':100,'open':54}and list(map(list,edges))==J['open_edges']
alive=set(range(24));rounds=[]
while True:
 rm=sorted(i for i in alive if not any(a==i and b in alive for a,b in edges)or not any(b==i and a in alive for a,b in edges))
 if not rm:break
 rounds.append(rm);alive-=set(rm)
assert rounds==J['pruning_rounds']and sorted(alive)==[0,2,7,8,9,14,17,18,19]
ce=[(a,b)for a,b in edges if a in alive and b in alive];assert len(ce)==36 and {b for a,b in ce if a==0}=={17,18,19};assert states[0]==('S','W')and all(a==0 or(states[a][0][0]=='N'and states[a][1][0]=='E')for a in alive)
ports=[];preds=[]
for a,b in ce:
 hs=fixed(-1)|patch(states[a])|patch(states[b],1)|fixed(2)
 targets={f:p for f,(p,w)in families.items()}
 if a==0:targets['F']=1-2j
 for f,q in targets.items():
  pp=[]
  for h,v in enumerate(V):
   p=q-v;rs=[r for r,c in enumerate(hs[q])if c==h]
   if rs:assert p in hs and len(hs[p])>0
   dest=p+V[out(hs[p],0)]if p in hs and hs[p]else None;hit=bool(rs)and dest==q
   ports.append(dict(pair=[a,b],target=f,input_heading=h,arrival_ranks=rs,source=xy(p),source_word=''.join('NESW'[c]for c in hs[p])if p in hs else None,first_destination=xy(dest)if dest is not None else None,first_R_predecessor=hit))
   if hit:pp.append(p)
  expected={'T':{-1+1j},'R':{1+0j},'C':{1j,-1j},'A':{0j},'D':{1-1j},'E':{1-2j}if a==0 else set(),'F':set()}[f]
  assert set(pp)==expected;preds.append(dict(pair=[a,b],target=f,predecessors=sorted(map(xy,pp))))
  # Every included vertex maps directly to the band or to its immediate lower ancestor.
  dest=q+V[out(hs[q],0)];assert dest in set(fixed(-1))|set(fixed(0))|set(fixed(1))
assert len(ports)==876
# Every full-drift class keeps its y layer and x parity, so no hidden K/G alias.
assert len({(int(p.imag),int(p.real)%2)for p,w in families.values()}|{(-2,1),(-2,0)})==8
DEPS={'audits/check_one_use_RRLL_transfer_independent.json':'feebdb692b9fe2ea5bc88191fa6e67547fd26f4e3bcc29dbca089bcb4f095242','audits/check_even_staircase_basin_independent.json':'6770ffdfc647c032ebff7148b08c06b461be26bfb395d040b45592d7a9343d2d','audits/check_mixed_first_track_pipeline_independent.json':'8ff4e2b77138f10372b4074fe93d9e0a7d28b4af32d29137f16cf4df8add9bab'}
for f,h in DEPS.items():assert sha(R/f)==h
BL=R/'audits/boundary_local_first_track_independent.json';bj=json.loads(BL.read_text());assert bj['proof_sha256']=='3eee26b9785a7af4b759bca2e0c3c96c5018d65a4d0b1c1aff8b60613194b789'
for f,h in bj['dependencies'].items():assert sha(R/f)==h
DEPS[str(BL.relative_to(R))]=sha(BL)
O=dict(status='PASS exact pure RRLL outer-reader transfer, full first-R basin closure and critical cap4 RIGHT-extremal consequence',proof=sha(P),author_certificate=sha(Jf),script=sha(S),signed_dependencies=DEPS,G_domain=Gs,F_domain=Fs,nodes=nodes,node_counts=dict(nc),pairs=pairs,pair_counts=dict(ec),states=states,edges=edges,pruning_rounds=rounds,cyclic_types=sorted(alive),cyclic_edges=ce,all876_direction_domains=ports,physical_predecessor_sets=preds,analytic_review=[
'The signed whole pure RRLL one-use circle forces the supplied NNSN/WWEW band and WWWE/SSSN first reader row. Complete WHITE cap4 plus the exact unique S arrival or N departure gives all ten G and ten F histories, not an imposed first/last-port convention.',
'All100 unit and576 ordered-pair patches are rebuilt independently. Every port rejection has an explicit unequal list; every one of106 clock rejections has a replayed positive cycle from physical successor equalities and true rank gaps>=4. No new height, age or bounded-period filter occurs. Short full quotients still satisfy these physical lifted patches; additional alias constraints cannot resurrect a rejected patch.',
'Any actual finite cyclic state word lies in the iteratively nonzero in/out core. Two rounds leave the stated nine types and36 edges, without an all-length cycle scan. These are necessary only, not attained exterior fields. State0 has only17/18/19 successors; all their G first-R departures point away from F0.',
'All876 physical input-direction cases, including zero ports, give precisely pred(C)={T,D},pred(A)={C},pred(T)={previousR},pred(R)={A},pred(D)={E},pred(E)={F} only at0,and pred(F0)=empty. Every allowed input has a supplied physical neighbor. All included K vertices feed Gamma in at most3 steps, while no vertex outside K can first-R enter K. Thus K is exactly the full basin, with no guessed deeper-row source.',
'Full d=(-2n,0) preserves y and x parity, separating all eight cell families for every n>=1. Any G has a genuine firstR because its complete history startsWHITE. It lies outside K, and its forward b-orbit in the finite full quotient therefore reaches a different b-cycle. This is functional-graph closure, not spatial descent or a new original BLACK root.',
'Geometric Gamma is the essential eastward RRLL staircase; every G lies strictly below on RIGHT. Unit grid edges cannot cross it except at a Gamma vertex. Backward closure forbids that vertex, so the entire new b-cycle is on RIGHT. No distinct C-plateau, source-basin or fuel claim is inferred.',
'The final extremal contradiction requires critical GLOBAL M=c_right+1 and COMPLETEcap4. The signed first-R monotone-height theorem makes every b-cycle constant-height; the separately signed EVERY-cycle positive first-track winding gives c>=c_right+1. Hence every such cycle has heightM. Selecting a RIGHT-extremal M cycle rules out this pure RRLL whole-one-use shape, but does not exclude mixed RRLL/alternating shapes or multiply-used segments.',
'The earlier pure alternating basin exclusion has the same restricted critical cap4 consequence. Neither local result proves global capture, WHITE-only lifetime winding, a fuel budget or arbitrary all-cap first-R maximality.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(nc,ec,len(ports));print(sha(S.with_suffix('.json')))
