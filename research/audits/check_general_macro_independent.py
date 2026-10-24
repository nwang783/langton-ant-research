"""Independent full-base traces, terminal offsets, parity and canonical frames.
Subject imported to produce the candidate automata, never as the physical oracle.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from functools import lru_cache
import sys,json,hashlib,time
B=Path('/workspace/shared/langton');H=B/'computability/flat_exact_validator';sys.path.insert(0,str(H))
import general_macro_decider as A
start=time.monotonic();dirs=(1j,1,-1j,-1)
rb=[(h,'R' if t==1 else 'L') for h in range(4) for t in (1,-1)]+[(1,'LLLRRRRL'),(0,'R'),(1,'LLLRRRRLRRRR')]
ri=[[s] for s in range(10)]+[[8]+A.word_states('RRR',1)+[9]]
models=[('identity',A.GeneralMacroModel([(1,'LLLRRRRL')],[[0]]),True),('two_cycle',A.GeneralMacroModel([(1,'LLLRRRRL')]*2,[[1],[0]]),True),('branching_zero',A.GeneralMacroModel([(0,'RRRR')],[[0,0]]),False),('illegal_zero_parity',A.GeneralMacroModel([(0,'RRRRRRRR')],[[0]]),False),('transient',A.GeneralMacroModel([(1,'LLLR'),(3,'RRRL'),(1,'LLLRRRRL')],[[0],[1],[0,1]],2),True),('revisited_prefix',A.GeneralMacroModel(rb,ri,10),True),('nested_branch',A.GeneralMacroModel([(0,'RRRR')]*3,[[0],[1,1],[1,2]],2),False)]
seed={(-1,1),(0,0),(0,1)};rows=[]
for name,m,expect in models:
 board=seed if expect else set();V=A.MacroGivenSeedValidator(m,board);verdict=V.solve();assert verdict['possible']==expect
 @lru_cache(None)
 def expand(s,r):return (s,) if not r else tuple(v for t in m.images[s] for v in expand(t,r-1))
 def literal(word,heading):
  z=0j;h=dirs[heading];out=[]
  for s in word:
   assert h==dirs[m.bases[s][0]]
   for c in m.bases[s][1]:out.append((z,c));h*=(-1j if c=='R' else 1j);z+=h
  return out,z,h
 coords=0;refs=0
 for s in m.reach:
  pref=V.refs[s]
  assert s==m.root or any(len(expand(m.root,d))>len(pref) and expand(m.root,d)[:len(pref)]==pref and expand(m.root,d)[len(pref)]==s for d in range(len(m.reach)+1))
  _,origin,heading=literal(pref,m.bases[m.root][0]);assert origin==complex(*V.positions[s]);assert heading==dirs[m.bases[s][0]];refs+=1
  tables={}
  for sg in product((-1,1),repeat=2):
   x=({'x':sg[0]},0);y=({'y':sg[1]},0);r=({'r':1},0);tables[sg]=(V.I(s,r,x,y,('r','x','y')),V.Q(s,r,x,y,('r','x','y')))
  for r in range(4):
   trace,_,_=literal(expand(s,r),m.bases[s][0]);count=Counter(z for z,c in trace)
   prefix=tuple(v for t in pref for v in expand(t,r));before,_,_=literal(prefix,m.bases[m.root][0]);prior=Counter(z for z,c in before)
   for x,y in product(range(-5,6),repeat=2):
    sg=(1 if x>=0 else -1,1 if y>=0 else -1);val=dict(r=r,x=abs(x),y=abs(y));I,Q=tables[sg];z=complex(x,y);p=z+origin
    assert V.read[s][sg].eval(**val)==(z in count),(name,s,r,z,'read')
    assert Q.eval(**val)==bool(count[z]%2),(name,s,r,z,'Q')
    want=((int(p.real),int(p.imag))in board)^(prior[p]%2)
    assert I.eval(**val)==want,(name,s,r,z,'I')
    coords+=3
 shifts,machines,rat=m.parity_machines();prefixchecks=0;schemes=0
 for dep,scheme,bound in A.bounded_schemes(m,max_length=2,max_schemes=40):
  chunks,terminal=scheme;cycles=sum(c for c,es in chunks)
  if cycles>3:continue
  schemes+=1
  for j in range(len(m.bases[terminal][1])):
   comp=A.compile_terminal(m,scheme,j,shifts,machines)
   for ns in product(range(3),repeat=cycles):
    path=[];n=0
    for cyc,es in chunks:
     repeat=ns[n] if cyc else 1;n+=int(cyc);path.extend([e.index for e in es]*repeat)
    if len(path)>7:continue
    s=m.root;offset=0
    for i,ix in enumerate(path):
     offset+=sum(sum(len(m.bases[v][1]) for v in expand(t,len(path)-i-1)) for t in m.images[s][:ix]);s=m.images[s][ix]
    assert s==terminal
    trace,_,_=literal(expand(m.root,len(path)),m.bases[m.root][0]);z,c=trace[offset+j];odd=sum(q==z for q,t in trace[:offset+j])%2;vals=dict(zip(comp['variables'],ns))
    assert comp['prior'].eval(**vals)==bool(odd),(name,path,j,'prior')
    assert comp['black'].eval(**vals)==bool(odd^(c=='L'))
    for key,want in [('x',z.real),('y',z.imag),('length',len(path))]:
     co,cn=comp[key];assert sum(a*b for a,b in zip(co,ns))+cn==want
    prefixchecks+=1
 for r in range(5):
  trace,_,_=literal(expand(m.root,r),m.bases[m.root][0]);actual={complex(*p) for p in board};legal=True
  for z,c in trace:
   if (z in actual)!=(c=='L'):legal=False;break
   actual.symmetric_difference_update({z})
  if expect:assert legal
 result=dict(name=name,full_frame_verdict=verdict,canonical_references=refs,literal_coordinate_checks=coords,genuine_schemes=schemes,terminal_prefix_parities=prefixchecks)
 if name in ('identity','two_cycle','transient','revisited_prefix','branching_zero'):
  generated=A.solve_macro_generated(m);assert generated['status']=='decided' and generated['possible']==expect
  if expect:assert set(map(tuple,generated['candidate_seed']))==seed
  result['generated_decision']=generated
 rows.append(result);print(name,coords,prefixchecks,flush=True)
# A resource cap is never a mathematical NO.
assert A.solve_macro_generated(models[4][1],max_length=0)['possible'] is None
out=dict(status='PASS independent finite-base physical traces, every tested terminal read and exact all-depth decisions',models=rows,seconds=time.monotonic()-start,subject_sha256=hashlib.sha256((H/'general_macro_decider.py').read_bytes()).hexdigest(),scope='General branching additive-I finite-base macro realization. Positive controls nongrowing; no ant capture theorem.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
