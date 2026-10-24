from pathlib import Path
from collections import Counter,deque
import hashlib,json,time
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'reframe_finite_seed_2026-10-24';G=R/'kernel_cycle_lift_2026-10-24'
p=SELF.parent/'check_cycle_birth_finite_fuel_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('cells=')[0],ns)
ends,component,step,wvertex=[ns[k]for k in('ends','component','step','wvertex')]
def xy(z):return(int(z.real),int(z.imag))
def key(C):return tuple(sorted(map(xy,C)))
def edgevertices(C):return {v for q in C for v in ends(q,0)}
root=1-1j;lev=[{frozenset()}]
for mass in range(1,7):
 nxt=set()
 for C in lev[-1]:
  for v in {root}|edgevertices(C):
   for dd in(1+1j,1-1j,-1+1j,-1-1j):
    q=(v+dd)/2;assert q.real.is_integer()and q.imag.is_integer()and v in ends(q,0)
    if q not in C:nxt.add(C|{q})
 lev.append(nxt)
print('shapes',list(map(len,lev)),flush=True)
M=6;states=sorted(set().union(*lev),key=lambda C:(len(C),key(C)));ind={C:i for i,C in enumerate(states)};fresh=[]
for C in states:
 V={root}|edgevertices(C);ds=[frozenset()]
 if 0 not in C:
  a,b=ends(0,0);other=b if a==root else a
  if other not in V:
   delta=(other-root)/2
   for n in range(1,M-len(C)):
    for E in lev[n]:
     d=frozenset(q+delta for q in E)
     if not V&edgevertices(d):ds.append(d)
 for d in ds:
  B=set(C|d);assert component(B,0,root)[1]==C
  pn,hn,ch=step(B,0j,0);N=component(B,0,wvertex(pn,hn))[1]
  if len(N)>M:continue
  lost=B-N;normal=frozenset((q-pn)*1j**hn for q in N)
  fresh.append((ind[C],ind[normal],ch,key(C),key(d),key(N),key(lost),(xy(pn),hn)))
def expected(z):return(z['source'],z['target'],z['turn'],tuple(map(tuple,z['input_component'])),tuple(map(tuple,z['imported_component'])),tuple(map(tuple,z['output_active'])),tuple(map(tuple,z['emitted_component'])),(tuple(z['output_pose'][0]),z['output_pose'][1]))
K=json.loads((D/'component_kernel_M6.json').read_text());T=[expected(z)for z in K['transitions']];assert Counter(fresh)==Counter(T);assert len(states)==14116 and len(T)==12060
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
def reach(back=False):
 seen={0};todo=[0]
 for a in todo:
  for b in (rev[a]if back else[T[i][1]for i in adj[a]]):
   if b not in seen:seen.add(b);todo.append(b)
 return seen
scc=reach()&reach(True);paths=[]
def dfs(a,P):
 for i in adj[a]:
  b=T[i][1]
  if b==0:paths.append(P+[i])
  else:dfs(b,P+[i])
dfs(0,[]);paths.sort(key=lambda a:(len(a),a))
J=json.loads((D/'kernel_M6_compact_returns.json').read_text());assert paths==[r['indices']for r in J['returns']];assert set(J['recurrent_scc'])==scc;assert len(scc)==1093
assert set(J['recurrent_edge_indices'])=={i for i,z in enumerate(T)if z[0]in scc and z[1]in scc}
words=[''.join(T[z][2]for z in P)for P in paths];assert all(a==b['word']for a,b in zip(words,J['returns']));assert len(paths)==43527
print('kernel and returns PASS',Counter(words),flush=True)
# Full complete-component constraints, independently assembled from physical coordinates.
def lift(P,replay=True):
 p=0j;h=0;parity=set();req={};trace=[]
 for t,idx in enumerate(P+[None]):
  C=set()if idx is None else {p+complex(*q)*(-1j)**h for q in T[idx][3]}
  V=edgevertices(C)|{wvertex(p,h)};ports={(v+dd)/2 for v in V for dd in(1+1j,1-1j,-1+1j,-1-1j)}
  for q in ports:
   value=(q in C)^(q in parity)
   if q in req and req[q][0]!=value:return None,{'q':xy(q),'first':req[q][1],'second':t,'initial_bits':[int(req[q][0]),int(value)]}
   req.setdefault(q,(value,t))
  trace.append((p,h,C))
  if idx is not None:
   assert(p in C)==(T[idx][2]=='L')
   parity.symmetric_difference_update({p});h=(h+(1 if T[idx][2]=='R'else-1))%4;p+=1j*(-1j)**h
 seed={q for q,(v,_)in req.items()if v};B=set(seed);pp=0j;hh=0
 if replay:
  for t,(p,h,C)in enumerate(trace):
   assert(pp,hh)==(p,h)and component(B,0,wvertex(p,h))[1]==C
   if t<len(P):
    pp,hh,ch=step(B,pp,hh);assert ch==T[P[t]][2]
 else:B=seed^parity
 return (seed,B,p,h,trace),None

def trap(B,p,h):
 w=wvertex(p,h);tips=[w+(-2+2j)*(-1j)**(h+i)for i in range(4)];U=set()
 for tip in tips:U|=component(B,0,tip)[1]
 return len(U)>2 or(len(U)==2 and tips[0]not in edgevertices(U)),{'mass':len(U),'first_tip_incident':tips[0]in edgevertices(U),'edges':key(U)}
def weight(C):
 if len(C)==1:return 1
 if len(C)!=2:return 0
 a,b=[set(ends(q,0))for q in C];v,=a&b;u,=a-{v};w,=b-{v};return 2 if u+w==2*v else 1
def field_weight(B):
 todo=set(B);n=0
 while todo:
  q=next(iter(todo));C=component(B,0,ends(q,0)[0])[1];n+=weight(C);todo-=C
 return n
# Rebuild word-only mandatory last-R sets, rather than importing a selected OPEN list.
word_traps={}
for word in sorted(set(words)):
 p=0j;h=0;last={}
 for c in word:last[p]=c;h=(h+(1 if c=='R'else-1))%4;p+=1j*(-1j)**h
 bad,detail=trap({q for q,c in last.items()if c=='R'},p,h);word_traps[word]={'trapped':bad,**detail}
assert sum(v['trapped']for v in word_traps.values())==7
physical=[];survive=[];zero=[];drops=[];trapped=Counter();seeds={};outfields={}
for i,P in enumerate(paths):
 if word_traps[words[i]]['trapped']:continue
 lifted,conflict=lift(P)
 if lifted is None:continue
 physical.append(i);seed,B,p,h,trace=lifted
 bad,det=trap(B,p,h)
 if bad:trapped[(det['mass'],det['first_tip_incident'])]+=1;continue
 survive.append(i);drop=sum(weight({complex(*q)for q in T[z][4]})-weight({complex(*q)for q in T[z][6]})for z in P)
 assert drop==field_weight(seed)-field_weight(B)and drop>=0
 drops.append({'index':i,'drop':drop});seeds[i]=key(seed);outfields[i]=key(B)
 if drop==0:zero.append(i)
assert physical==json.loads((D/'cap6_physical_return_filter.json').read_text())['feasible_indices']
assert survive==json.loads((D/'cap6_profile_budget_filter.json').read_text())['surviving_indices']
assert len(physical)==4657 and len(survive)==93 and zero==[78,4554,4555,4866,4895,5169,33389]
print('physical/fuel PASS',len(physical),len(survive),zero,flush=True)
# Consecutive complete profiles: concatenate normalized transitions, preserving complete ports at the seam.
pair_controls=[]
for a in zero:
 for b in zero:
  result,conflict=lift(paths[a]+paths[b]);assert result is None
  pair_controls.append({'a':a,'b':b,**conflict})
seven=json.loads((D/'cap6_seven_zero_fuel_profiles.json').read_text())
assert sorted(r['index']for r in seven['profiles'])==zero
for r in seven['profiles']:
 assert tuple(map(tuple,r['minimal_seed']))==seeds[r['index']]
 assert r['indices']==paths[r['index']] and [expected(t)for t in r['transitions']]==[T[z]for z in paths[r['index']]]
 assert r['word']==words[r['index']]
print('all49 arbitrary-exterior pair conflicts PASS',flush=True)
manifest=json.loads((D/'cap6_exit_manifest.json').read_text())
for f,h in manifest.items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
extra={str(f.relative_to(R)):hashlib.sha256(f.read_bytes()).hexdigest()for f in [G/'EMPTY_CURSOR_IMPORT_BUDGET_TRAPS.md',G/'SEVEN_ZERO_FUEL_PROFILES_PAIR_OBSTRUCTION.md',G/'seven_cap6_profiles_certificate.json',SELF.parent/'check_empty_cursor_budget_corner_writer_independent.json']}
pair_author=json.loads((G/'seven_cap6_profiles_certificate.json').read_text());assert not pair_author['compatible_edges'] and len(pair_author['all_49_ordered_pairs'])==49
assert pair_author['source_sha256']['reframe_finite_seed_2026-10-24/cap6_seven_zero_fuel_profiles.json']==manifest['cap6_seven_zero_fuel_profiles.json']
out={'additional_dependencies':extra,'status':'PASS complete cap-six kernel, mandatory-field filters, finite component fuel and all49 zero-fuel pair obstructions','author_dependencies':manifest,'fresh_rooted_shape_counts':list(map(len,lev)),'kernel':{'states':len(states),'transitions':len(T),'nonempty_DAG':len(top),'scc_states':len(scc),'scc_edges':sum(z[0]in scc and z[1]in scc for z in T),'returns':len(paths),'word_counts':dict(Counter(words))},'word_traps':word_traps,'physical_count':len(physical),'surviving_count':len(survive),'surviving_word_counts':dict(Counter(words[i]for i in survive)),'drops':drops,'zero_indices':zero,'zero_seed_fields':seeds,'zero_final_fields':outfields,'all49_pair_conflicts':pair_controls,'analytic':['Every finite rooted connected edge set appears by incident-edge growth; every actual cap-six R either stays in the active component or imports exactly one complete disjoint component of mass<=5-|C| at the other endpoint. The unique L split is exact. No passive geometry is discarded from actual accounting.','Deleting empty state0 is an acyclic graph on all14115 other states. Thus any indefinitely cap-six actual path visits empty infinitely often; all43527 first-return paths are exhausted, independently of physical realizability of the relaxed graph.','At each cut, prescribe every edge of C black and every other edge incident to C vertices white, including the isolated cursor when C is empty. Earlier read parity translates these into exact initial bits. Consistency is sufficient by literal full-board induction, and inconsistency excludes every additional unread exterior. Every actual realizing board contains the minimal seed; all extra initial edges are unread throughout the word, hence the whole minimal final field remains a mandatory subset.','The signed import-budget theorem can therefore use both last-R mandatory word cells and additional old surviving forced profile cells. Its stronger subset union only grows under arbitrary exterior; at equality/non-first-tip any extra imports either fail earlier or leave the same exact forced reset. These are necessary exclusions for a sustained cap-six tail, not exclusions of individual finite words.','At each empty cut all complete black components are passive. Imports and detached components account for all changes in the geometric weight: singleton1, straight dimer2, corner dimer1, others0. There are no passive merges without an R import. The total is a finite nonnegative integer for finite support. Across the93 necessary surviving profiles86 decrease it and seven preserve it. The per-profile component ledger agrees with independently replayed complete-field weight, but the ledger cancellation argument covers arbitrary unread components too.','All49 pairs of the seven exact zero-drop profiles have contradictory physical initial-bit requirements. Consequently no two consecutive zero-drop returns can occur. Finite nonnegative fuel cannot decrease infinitely often, while a sustained cap-six tail would make infinitely many empty returns, contradiction. Every finite-support ant orbit therefore has infinitely many cuts with active-w component mass at least7. No assertion of unbounded component sizes, eventual standard104 capture, or a physically composable abstract return grammar.'],'scope':'Finite COMPLETE black support is essential to the finite fuel argument. Local kernel and arbitrary-exterior negative pair constraints themselves do not require a finite total board.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
