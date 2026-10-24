from pathlib import Path
from collections import Counter,deque
import hashlib,json
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'reframe_finite_seed_2026-10-24';p=SELF.parent/'check_cycle_birth_finite_fuel_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('cells=')[0],ns)
ends,component,step,wvertex=[ns[k]for k in('ends','component','step','wvertex')]
def xy(z):return(int(z.real),int(z.imag))
def key(C):return tuple(sorted(map(xy,C)))
root=1-1j;lattice=0
lev=[{frozenset()}]
for mass in range(1,6):
 nxt=set()
 for C in lev[-1]:
  vertices={root}|{v for q in C for v in ends(q,lattice)}
  for v in vertices:
   for dd in(1+1j,1-1j,-1+1j,-1-1j):
    q=(v+dd)/2;assert q.real.is_integer()and q.imag.is_integer()and v in ends(q,lattice)
    if q not in C:nxt.add(C|{q})
 lev.append(nxt)
assert list(map(len,lev))==[1,4,18,88,439,2224]

allout={}
for M in(4,5):
 states=sorted(set().union(*lev[:M+1]),key=lambda C:(len(C),key(C)));ind={C:i for i,C in enumerate(states)};T=[]
 for C in states:
  V={root}|{v for q in C for v in ends(q,lattice)};ds=[frozenset()]
  if 0 not in C:
   a,b=ends(0,lattice);other=b if a==root else a
   if other not in V:
    delta=(other-root)/2
    for n in range(1,M-len(C)):
     for E in lev[n]:
      d=frozenset(q+delta for q in E)
      if not V&{v for q in d for v in ends(q,lattice)}:ds.append(d)
  for d in ds:
   B=set(C|d);assert component(B,lattice,root)[1]==C
   pn,hn,ch=step(B,0j,0);N=component(B,lattice,wvertex(pn,hn))[1]
   if len(N)>M:continue
   lost=B-N;normal=frozenset((q-pn)*1j**hn for q in N)
   T.append((ind[C],ind[normal],ch,key(C),key(d),key(N),key(lost),(xy(pn),hn)))
 saved=json.loads((D/f'component_kernel_M{M}.json').read_text())
 def expected(z):return(z['source'],z['target'],z['turn'],tuple(map(tuple,z['input_component'])),tuple(map(tuple,z['imported_component'])),tuple(map(tuple,z['output_active'])),tuple(map(tuple,z['emitted_component'])),(tuple(z['output_pose'][0]),z['output_pose'][1]))
 E=[expected(z)for z in saved['transitions']];assert Counter(T)==Counter(E)
 adj=[[]for _ in states];rev=[[]for _ in states];indeg=[0]*len(states)
 for i,z in enumerate(T):
  a,b=z[:2];adj[a].append(i);rev[b].append(a)
  if a and b:indeg[b]+=1
 todo=deque(i for i in range(1,len(states))if not indeg[i]);top=[]
 while todo:
  a=todo.popleft();top.append(a)
  for i in adj[a]:
   b=T[i][1]
   if b:
    indeg[b]-=1
    if not indeg[b]:todo.append(b)
 assert len(top)==len(states)-1
 def reach(reverse=False):
  seen={0};todo=[0]
  for a in todo:
   for b in (rev[a]if reverse else[T[i][1]for i in adj[a]]):
    if b not in seen:seen.add(b);todo.append(b)
  return seen
 scc=reach()&reach(True);paths=[]
 def dfs(a,P):
  for i in adj[a]:
   b=T[i][1]
   if b==0:paths.append(P+[i])
   else:dfs(b,P+[i])
 dfs(0,[])
 def pk(path):return tuple(T[i]for i in path)
 cert=json.loads((D/f'kernel_M{M}_scc.json').read_text())
 assert set(cert['recurrent_scc'])==scc
 assert Counter(map(pk,paths))==Counter(tuple(expected(z)for z in r['transitions'])for r in cert['first_return_cycles'])
 words=Counter(''.join(T[i][2]for i in P)for P in paths)
 for r in cert['first_return_cycles']:
  p=0j;h=0
  for ch in r['word']:
   h=(h+(1 if ch=='R'else-1))%4;p+=(1j)*(-1j)**h
  assert xy(p)==tuple(r['displacement'])and h==r['heading']
 allout[M]={'states':len(states),'transitions':len(T),'scc_size':len(scc),'scc_edges':sum(z[0]in scc and z[1]in scc for z in T),'first_returns':len(paths),'words':dict(words),'nonempty_DAG_vertices':len(top),'max_first_return_length':max(map(len,paths))}
 if M==4:
  assert len(scc)==5 and allout[M]['scc_edges']==5 and words=={'RRRRL':1}
 else:
  assert words=={'RRRRLRRL':37,'RRRRLRL':62,'RRRRLL':1,'RRRRL':10}
  r=cert['first_return_cycles'][11];assert r['word']=='RRRRLRL'
  imp=[z['imported_component']for z in r['transitions']if z['imported_component']];out=[z['emitted_component']for z in r['transitions']if z['emitted_component']]
  assert list(map(len,imp))==[1]and sorted(map(len,out))==[1,3]
  star=next(c for c in out if len(c)==3);deg=Counter(v for q in star for v in ends(complex(*q),lattice));assert sorted(deg.values())==[1,1,1,3]
  allout[M]['path11_resource_identity']={'imports':imp,'emissions':out}
# Empty start physical chronology, all earlier required-white cells exclude any hidden archive which might change the forced collision.
B=set();p=0j;h=0;reads=[];imported=[]
for t in range(9):
 V,C=component(B,lattice,wvertex(p,h));before=set(B)
 if p not in B:
  a,b=ends(p,lattice);v=b if a==wvertex(p,h)else a;Z=component(B,lattice,v)[1]
  if Z and Z!=C:imported.append((t,len(C),len(Z),len(C|Z|{p})))
 q=p;p,h,ch=step(B,p,h);reads.append({'tick':t,'q':xy(q),'turn':ch,'active_mass_after':len(component(B,lattice,wvertex(p,h))[1])})
assert imported==[(8,3,3,7)]
assert ''.join(z['turn']for z in reads)=='RRRRLRRRR'
mf=json.loads((D/'grammar_manifest.json').read_text())
for f,h in mf.items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out={'status':'PASS cap4 universal exit within558 updates and exact cap5 first-return grammar','dependencies':mf,'kernels':allout,'empty_start_physical_prefix':reads,'cap4_cut_bound':545+13,'analytic':['The cap5 extension independently constructs all2224 mass5 rooted connected shapes by incident-edge growth, then every allowed import and unique L split. Complete states2774 and transitions2292 exactly match. The same coverage proof as signed cap3/4 applies, without assuming physical composability across edges.','Deleting empty active0 gives a DAG at both caps. Thus all recurrent SCCs contain0; independent reachability yields the unique5-state/5-edge cap4 and153-state/262-edge cap5 components. DFS of the full nonempty DAG exhausts all110 cap5 first returns, with the four recorded word multiplicities.','A cap4 physical state path has at most545 cuts outside the unique SCC. The cyclic interval is contiguous and all its internal edges are the forced no-import RRRRL loop. Within4 updates it reaches empty. Nine subsequent forced updates are impossible because the first emitted star is imported at update8, making mass7. Any extra archive causes an earlier departure from that SCC, not cancellation of this collision. Thus at most13 cuts in the cyclic interval and at most558 cap4 cuts total, so an exit occurs within558 updates from any cap4 start. This uses no finite support or eventual behavior premise.','Cap5 path11 consumes exactly one singleton and emits singleton plus3-star. A sum of any active-shape potential changes telescopes to zero on this return, and passive nonnegative type weights cannot strictly decrease. This is a local resource obstruction, not a physically composable infinite gadget.'],'scope':'Cap4 exits universally on any background. Cap5 graph and resource identities are necessary local options only; no sustained cap5 trajectory or standard capture theorem.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(allout)
