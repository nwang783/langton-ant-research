from pathlib import Path
from itertools import product
from collections import deque
import importlib.util,json,hashlib,random
ROOT=Path(__file__).resolve().parents[1];SRC=ROOT/'global_architecture_2026-10-23/directed_palette_front.py';assert hashlib.sha256(SRC.read_bytes()).hexdigest()=='595a5af07ee56e82181e86c8ba99fc6042f6589507223152b2a53817b49e9d71'
spec=importlib.util.spec_from_file_location('candidate_front',SRC);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def trace(w,h,p=0j):
 out=[]
 for c in w:
  out.append((p,c=='L'));h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 return out,p,h
xy=lambda p:(int(p.real),int(p.imag))
def geometry(a):
 D=complex(*a.drift);den=int(D.real**2+D.imag**2)
 def locate(p):
  for o,rr in enumerate(a.representatives):
   diff=p-complex(*rr);num=int(diff.real*D.real+diff.imag*D.imag)
   if num%den==0 and diff==(num//den)*D:return o,num//den
  return None,None
 levels=[set()for _ in a.representatives]
 for w in a.words:
  rows,e,h=trace(w,a.heading);assert e==D and h==a.heading
  for p,b in rows:
   o,k=locate(p);assert o is not None;levels[o].add(k)
 assert levels==a.levels and [min(v)for v in levels]==a.lower and [max(v)for v in levels]==a.upper
 assert a.front==tuple((o,k)for o,v in enumerate(levels)for k in range(min(v),max(v)))
 return D,locate
def physical_edge(p,state,label,flips=()):
 a=p.architecture;D,locate=geometry(a);phase,bits=state
 B={complex(*a.representatives[o])+(phase+k)*D:(bits>>i)&1 for i,(o,k)in enumerate(a.front)}
 for o,k in enumerate(a.upper):B[complex(*a.representatives[o])+(phase+k)*D]=p.profiles[o][(phase+k)%p.period]^(o in flips)
 rr,end,h=trace(a.words[label],a.heading,phase*D)
 for cell,required in rr:
  assert cell in B
  if B[cell]!=required:return None
  B[cell]^=1
 assert end==(phase+1)*D and h==a.heading
 out=sum(B[complex(*a.representatives[o])+(phase+1+k)*D]<<i for i,(o,k)in enumerate(a.front))
 return((phase+1)%p.period,out)
def finite_states(p):return[(n,b)for n in range(p.period)for b in range(1<<p.architecture.front_bits)]
def reference_cycle(p,starts):
 edges={s:{t for l in range(len(p.architecture.words))if(t:=physical_edge(p,s,l))is not None}for s in finite_states(p)}
 reachable=set(starts);todo=list(starts)
 while todo:
  for t in edges[todo.pop()]:
   if t not in reachable:reachable.add(t);todo.append(t)
 # Repeated sink removal, independent of the candidate DFS/back-edge method.
 active=set(reachable)
 while True:
  remove={s for s in active if not(edges[s]&active)}
  if not remove:break
  active-=remove
 return bool(active)
def replay_from_board(p,labels,cap=()):
 a=p.architecture;D,locate=geometry(a);changed={complex(*z)for z in cap};at=0j;h=a.heading
 for label in labels:
  rows,end,hh=trace(a.words[label],h,at)
  for cell,required in rows:
   o,k=locate(cell);assert o is not None
   actual=p.profiles[o][k%p.period]^(cell in changed)
   assert actual==required
   changed.symmetric_difference_update({cell})
  at=end;h=hh
 return changed
rng=random.Random(20261023);transitions=cycles=witnesses=prefixes=0
palettes=[('RL',),('RL','RLRRRR'),('LR','LRLLLL'),('RLLR','RLLRRRRR'),('RLRL',)]
for words in palettes:
 for h in range(4):
  a=mod.FrontArchitecture(words,h);D,locate=geometry(a)
  for period in(1,2,3):
   size=len(a.levels)*period
   patterns=list(product((0,1),repeat=size))if size<=6 else[tuple(rng.randrange(2)for _ in range(size))for _ in range(24)]
   for pattern in patterns:
    p=mod.PeriodicFront(a,[pattern[i*period:(i+1)*period]for i in range(len(a.levels))])
    for state in finite_states(p):
     for flips in((),tuple(range(len(a.levels)))):
      actual={l:t for t,l in p.edges(state,flips)}
      for label in range(len(words)):
       assert actual.get(label)==physical_edge(p,state,label,flips);transitions+=1
    r=p.decide(max_states=128);expect=reference_cycle(p,[(0,b)for b in range(1<<a.front_bits)]);assert(r['status']=='INFINITE_SCHEDULE')==expect;cycles+=1
    if expect:
     labels=[e['label']for e in r['cycle']];replay_from_board(p,labels*8,r['witness_cap']);witnesses+=1
    # Independent finite-board prefixes: flip cells in stored front, fresh,
    # behind-front, and off-strip; retain every altered cell physically.
    if cycles%13:continue
    cap=[]
    for o in range(len(a.levels)):
     for k in(a.lower[o]-1,a.upper[o]+rng.randrange(5)):
      if rng.randrange(2):cap.append(xy(complex(*a.representatives[o])+k*D))
    cap.append((731,918));stop=max([k-a.upper[o]+1 for cell in cap for o,k in[locate(complex(*cell))]if o is not None and k>=a.upper[o]]or[0])
    states={frozenset(map(lambda x:complex(*x),cap))};dead=None
    for n in range(stop):
     nxt=set()
     for board in states:
      for w in words:
       bb=set(board);valid=True
       for cell,required in trace(w,h,n*D)[0]:
        o,k=locate(cell);assert o is not None
        if p.profiles[o][k%period]^(cell in bb)!=required:valid=False;break
        bb.symmetric_difference_update({cell})
       if valid:nxt.add(frozenset(bb))
     states=nxt
     if not states:dead=n+1;break
    got=p.cap_prefix(cap,max_prefix=10000)
    if dead:assert got['status']=='FINITE_PREFIX_IMPOSSIBLE'and got['prefix_blocks']==dead
    else:
     expectstates={(stop%period,sum((p.profiles[o][(stop+k)%period]^(complex(*a.representatives[o])+(stop+k)*D in board))<<i for i,(o,k)in enumerate(a.front)))for board in states}
     assert got['status']=='EXACT_PREFIX'and set(got['states'])==expectstates
     r=p.decide(cap,max_states=128);assert(r['status']=='INFINITE_SCHEDULE')==reference_cycle(p,expectstates)
    prefixes+=1
# Retained full standard is a nontrivial18-bit positive with complete finite seed.
std=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());a=mod.FrontArchitecture([std['word']],std['heading']);p=mod.PeriodicFront(a,[[0]for _ in a.levels]);r=p.decide(std['seed'],max_states=1<<19);assert r['status']=='INFINITE_SCHEDULE'and a.front_bits==18
replay_from_board(p,[0]*20,std['seed'])
assert p.decide(max_states=1)['status']=='UNKNOWN_STATE_BUDGET'
a=mod.FrontArchitecture(['RL']);p=mod.PeriodicFront(a,[[0],[1]]);assert p.decide(cap=[a.physical(0,100)],max_prefix=20)['status']=='UNKNOWN_PREFIX_BUDGET'
for words in[[],[''],['RRRR'],['R'],['RL','LR']]:
 try:mod.FrontArchitecture(words)
 except ValueError:pass
 else:raise AssertionError(words)
out={'status':'PASS independent physical edges, sink-pruning cycles, exact specified-cap physical prefixes and witnesses','source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'physical_edge_comparisons':transitions,'independent_cycle_decisions':cycles,'unknown_cap_full_board_witnesses':witnesses,'specified_cap_prefix_controls':prefixes,'standard_front_bits':18,'scope':'Supplied finite common-drift architecture only. Unknown arbitrary-XOR cap and specified finite-XOR cap implemented; black-additions-only remains analytic. Budget exhaustion UNKNOWN; no generic full64-bit graph or universal capture claim.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
