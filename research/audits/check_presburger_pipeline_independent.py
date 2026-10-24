"""Independent concrete words and finite graph walks against supplied-template code."""
from pathlib import Path
import sys,random,itertools,json,hashlib
R=Path(__file__).resolve().parents[1];D=R/'computability/unit_inductive_certificates';sys.path.insert(0,str(D))
SOURCE_PATHS=[D/'presburger_read_set_solver.py',D/'presburger_template_validator.py']
SOURCE_HASHES={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in SOURCE_PATHS}
import presburger_read_set_solver as candidate
import presburger_template_validator as validator
ctx=candidate.Context(max_operations=20_000_000)
malformed=0
for images,root in [(['R','L']*3,0),(['R','L']*5,0),(['X','L']*4,0),(['','L']*4,0),([1,'L']*4,0),(['R','L']*4,8),(['R','L']*4,False),('RLRLRLRL',0)]:
 try:validator.validate(ctx,images,root,{}, {}, set())
 except (AssertionError,ValueError,TypeError):malformed+=1
 else:raise AssertionError('Malformed input accepted')
def finite_relation(depth,points):
 clauses=[f'(r={depth} and x={x} and y={y})'for x,y in sorted(points)]
 return ctx.set('{ [r,x,y] : '+(' or '.join(clauses)if clauses else '0=1')+' }')
rng=random.Random(113947);graphs=[]
for N in range(1,4):
 for _ in range(12):
  edges=[(u,v,(rng.randrange(-2,3),rng.randrange(-2,3)))for u in range(N)for v in range(N)if rng.randrange(3)==0]
  graphs.append((N,edges))
graphs += [(4,[(0,1,(1,0)),(1,0,(0,1)),(2,3,(-1,0)),(3,2,(0,-1))]),(3,[(0,1,(1,0)),(0,1,(1,0)),(1,1,(-1,2)),(1,2,(0,-1))])]
graph_checks=0
for N,edges in graphs:
 for root in range(N):
  ctx.reset_operations();rel,_=candidate.relation(ctx,range(N),edges,root)
  current={(root,0,0)}
  for depth in range(7):
   got=rel.intersect(ctx.set(f'{{ [r,x,y] : r={depth} }}'))
   want=finite_relation(depth,{(x,y)for s,x,y in current});assert got.is_equal(want),(N,edges,root,depth,str(got),str(want));graph_checks+=1
   current={(v,x+dx,y+dy)for s,x,y in current for u,v,(dx,dy)in edges if s==u}

def orbit(turn,heading,count):
 p=0j;h=(1j,1,-1j,-1)[heading]
 parity=set()
 for _ in range(count):
  if p in parity:parity.remove(p)
  else:parity.add(p)
  h*=(-1j if turn=='R' else 1j);p+=h
 return parity,p

def board(phases):
 clauses=[]
 for phase,points in enumerate(phases):
  for z in points:clauses.append(f'(r%{len(phases)}={phase} and x={int(z.real)} and y={int(z.imag)})')
 return ctx.set('{ [r,x,y] : r>=0 and ('+(' or '.join(clauses)if clauses else '0=1')+') }')
records=[]
for root in range(8):
 images=['R','L']*4;B={0j}if root%2 else set();I={root:board([B])};O={root:board([B^{0j}])}
 good=validator.validate(ctx,images,root,I,O,{(int(z.real),int(z.imag))for z in B});assert good['all_template_checks_pass']and not good['accepted'];records.append([root,'identity',len(good['failures'])])
 forged=validator.validate(ctx,images,root,I,I,{(int(z.real),int(z.imag))for z in B});assert any(x['kind']=='base_output'for x in forged['failures']);records.append([root,'forged-output',len(forged['failures'])])
 # Fresh canonical period-two templates, directly computed in complex coordinates.
 turn='L'if root%2 else 'R';sgn=-1 if root%2 else 1;I={};O={};h0=root//2
 images=['RRRRR','LLLLL']*4
 for j in range(4):
  h=(h0+j*sgn)%4;s=2*h+(root%2);z=orbit(turn,h0,j)[1];ins=[];outs=[]
  for count in(1,5):
   before=orbit(turn,h0,j*count)[0];local={q-z for q in before};parity=orbit(turn,h,count)[0]
   ins.append(local);outs.append(local^parity)
  I[s]=board(ins);O[s]=board(outs)
 bad=validator.validate(ctx,images,root,I,O,set());assert bad['growing_root']and not bad['accepted']
 # Left-first roots are already invalid on the blank seed at depth zero.
 assert any(x['kind']=='frame'for x in bad['failures'])
 assert all(x['kind']in ('frame','base')for x in bad['failures']);records.append([root,'five-turn-canonical',len(bad['failures'])])
out={'status':'PASS independently generated exact-solver controls','graph_families':len(graphs),'exact_depth_fiber_comparisons':graph_checks,'template_controls':records,'malformed_inputs_rejected':malformed,'hashes':SOURCE_HASHES,'scope':'A=I supplied-template pipeline only; no general automatic extraction or accepted growing model.'}
assert SOURCE_HASHES=={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in SOURCE_PATHS}
(R/'audits/presburger_pipeline_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
