from pathlib import Path
from itertools import product
import importlib.util,sys,json,hashlib,random
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'reframe_finite_seed_2026-10-24';sys.path.insert(0,str(D));sp=importlib.util.spec_from_file_location('candidate_symbolic',D/'symbolic_capped_word.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
p=SELF.with_name('check_cycle_birth_finite_fuel_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('cells=')[0],ns);component,wvertex,step=[ns[k]for k in('component','wvertex','step')];xy=lambda z:(int(z.real),int(z.imag))
def minimum(word):
 p=0j;h=0;last={};B=set();visited=set()
 for t,c in enumerate(word):
  if p in last and last[p]==c:return None,visited
  if p not in last and c=='L':B.add(p)
  last[p]=c;visited.add(p);h=(h+(1 if c=='R'else-1))%4;p+=1j*(-1j)**h
 return B,visited

def physical(B0,word,cap):
 B=set(B0);p=0j;h=0;rows=[]
 for t in range(len(word)+1):
  C=component(B,0,wvertex(p,h))[1];rows.append((t,xy(p),h,len(C),sorted(map(xy,B))))
  if len(C)>cap or bool(C)!=(0<t<len(word)):return False,rows
  if t==len(word):break
  p,h,c=step(B,p,h)
  if c!=word[t]:return False,rows
 return True,rows
rng=random.Random(620247);tests=0;fixtures=[('RRRRL',4,set()),('RRRRLRL',5,{-1+1j}),('RRRRLRLRL',6,{-1+1j,-2+2j}),('RRRRLRLRRL',6,{-1+1j,-1+2j}),('RRRRLRLRLRL',7,{-i+i*1j for i in range(1,4)})];counts=[]
for word,cap,seed in fixtures:
 C=m.build(word,cap);boards=[]
 if cap==4:
  cells=[complex(x,y)for x in range(-1,2)for y in range(-1,2)];boards=[{q for i,q in enumerate(cells)if mask>>i&1}for mask in range(512)]
 else:
  cells=[complex(x,y)for x in range(-4,5)for y in range(-4,5)];boards=[set(rng.sample(cells,rng.randrange(15)))for _ in range(100)]
 boards +=[seed|{100+j+(100-j)*1j for j in range(8)},{-i+i*1j for i in range(1,cap+9)}]
 for B in boards:
  val=C.assignment(set(map(xy,B)));cnf=all(any(val[abs(x)]==(x>0)for x in clause)for clause in C.clauses);literal,_=physical(B,word,cap);assert cnf==literal;tests+=1
 assert physical(seed,word,cap)[0];counts.append((word,cap,C.n,len(C.clauses),len(boards)))
assert tests==922
# Decode every saved assignment and independently verify all clauses and full physical fields.
models=json.loads((D/'cap7_word_cnf_models.json').read_text());modelrows=[]
for ref in models['models']:
 word=ref['word'];C=m.build(word,7);packed=bytes.fromhex(ref['packed_assignment_hex']);val={i:bool(packed[(i-1)//8]>>(i-1)%8&1)for i in range(1,C.n+1)}
 assert C.n==ref['variables']and len(C.clauses)==ref['clauses']
 assert all(any(val[abs(x)]==(x>0)for x in clause)for clause in C.clauses)
 seed={complex(*q)for q,z in C.inputs.items()if val[z]};assert seed=={complex(*q)for q in ref['finite_seed']};assert minimum(word)[0]==seed
 ok,trace=physical(seed,word,7);assert ok
 for z,r in zip(trace,ref['complete_board_replay']):assert z==(r['time'],tuple(r['pose'][0]),r['pose'][1],r['active_mass'],list(map(tuple,r['field'])))
 modelrows.append((word,len(seed),C.n,len(C.clauses)))
assert len(modelrows)==23
C=m.build('RRRR',4);units={c[0]for c in C.clauses if len(c)==1};assert any(-x in units for x in units)
# Independent minimum-field monotonicity and interior-empty four-R controls.
rng=random.Random(11124);consistent=0;extra_tests=0
for n in range(1,9):
 for cs in product('RL',repeat=n):
  word=''.join(cs);seed,vs=minimum(word)
  if seed is None:continue
  consistent+=1;unread=[complex(x,y)for x in range(-4,5)for y in range(-4,5)if complex(x,y)not in vs]
  for _ in range(8):
   extra=set(rng.sample(unread,rng.randrange(10)));B=seed|extra;smallB=set(seed);p=0j;h=0
   for t,c in enumerate(word):
    assert B==smallB|extra and not smallB&extra
    Cm=component(smallB,0,wvertex(p,h))[1];CB=component(B,0,wvertex(p,h))[1];assert Cm<=CB
    if t+4<=len(word)and word[t:t+4]=='RRRR':assert not CB
    pm,hm,cm=step(smallB,p,h);p,h,cc=step(B,p,h);assert(pm,hm,cm)==(p,h,cc)and cc==c
   for cap in(4,7):assert not physical(seed|extra,word,cap)[0]or physical(seed,word,cap)[0]
   extra_tests+=1
assert(consistent,extra_tests)==(350,2800)
mp=D/'symbolic_guard_with_minimum_manifest.json';manifest=json.loads(mp.read_text())
for f,h in manifest.items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out={'status':'PASS exact finite-word Boolean compiler WITH mandatory minimum-board simplification; no solver/global claim','manifest_sha256':hashlib.sha256(mp.read_bytes()).hexdigest(),'all_source_hashes':manifest,'fresh922_CNF_versus_full_graph_controls':counts,'fresh23_decoded_clause_and_complete_field_models':modelrows,'minimum_consistent_words':consistent,'unread_extra_background_tests':extra_tests,'analytic_review':[
'For any fixed literal word, parity fixes each visited cell initial bit; all other realizing boards add only globally unread cells to the first-L minimum board. They stay unread and unchanged at every cut. Cap and empty-endpoint failures of the minimum cannot be repaired by adding black edges.',
'The interior nonempty requirement is also exact at the minimum: if it is empty at an interior cut on a realization ending empty, there must be at least four updates left. Four R ports then occur consecutively at that same stationary w root, so all four incident cells were white in EVERY realization. Added unread exterior cannot make this cut nonempty. Thus the minimum-board algorithm is the primary bare-word existence decision, with no SAT required.',
'The alternate CNF uses a common initial bit per queried physical cell and exact read-parity XOR across all phases. At an interior cut the radius-M root ball is closed by every incident edge, including edges leaving to distanceM+1. M rounds of black reachability exactly identify paths of length<=M; marking edges with a reached endpoint and requiring at mostM is equivalent to the COMPLETE component cap. Any larger component has a connected witness ofM+1 edges, each with an endpoint at distance<=M. This covers cycles, arbitrary external attachments, andM0.',
'AND/OR Tseitin clauses are equivalences, and the sequential threshold circuit enforces the cardinality exactly, including constant literals and negative residual limits. Total gates/clauses are O((wordlength+1)(M+1)^3). Every satisfying initial-bit assignment extends by white elsewhere to a finite physical witness; any matching arbitrary outside field cannot violate the enforced cap through an unqueried bypass.',
'Fresh independent graph replay matches922 circuit evaluations, and all23 packed assignments are decoded and every clause checked without a SAT solver; all full fields and active masses match. The saved RRRR/cap4 contradiction has opposite unit clauses. The longest saved circuit remains NOT_RUN, with no inferred solver outcome.',
'The mandatory simplification prevents claiming CNF novelty or necessity for bare literal existence. It is only an exact alternate representation potentially useful for additional nonmonotone profile/resource constraints; no general infinite-orbit decision, indefinite composition, or capture follows.'
]}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(tests,consistent,extra_tests,len(modelrows))
