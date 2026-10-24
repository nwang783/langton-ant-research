"""Geometry-derived five-period nonstationary inverse104 slab.
Every image occurrence is independent. Inherited front colors are arbitrary;
only cells unreachable by ANY earlier allowed period have rail-supplied input.
A SAT slab is finite feasibility only, never an infinite construction.
"""
from pathlib import Path
import collections,itertools,json,time,subprocess,hashlib
import synthesize_multirail_short_refinement as M
P=Path(__file__).resolve().parent
O=P/'nonstationary_short_slab';O.mkdir(exist_ok=True)
PERIODS=5

def build(all_input_free=False):
 _,_,base,rawrails,_,_=M.build()
 lo={a:min(e[0] for e in es) for a,es in base.items()}
 hi={a:max(e[0] for e in es) for a,es in base.items()}
 global_min=min(lo.values());global_max=max(hi.values())
 assert global_max-global_min==4 and PERIODS==global_max-global_min+1
 names={};C=[]
 def var(s):
  if s not in names:names[s]=len(names)+1
  return names[s]
 true=var('TRUE');C.append([true]);groups=collections.defaultdict(lambda:collections.defaultdict(list))
 for r in range(PERIODS):
  coarse,e,g=M.core.trace(M.REV,(-2*r,-2*r),3)
  assert (e,g)==((-2*r-2,-2*r-2),3)
  for j,(p,h,c) in enumerate(coarse):
   xs=[var(f'x{r}_{j}_{k}') for k in range(len(M.core.dom[c]))]
   C.append(xs);C.extend([-x,-y] for x,y in itertools.combinations(xs,2))
   for k,w in enumerate(M.core.dom[c]):
    rr,ee,gg=M.core.trace(w,p,h);assert (ee,gg)==M.core.trace(c,p,h)[1:]
    for i,(q,hh,t) in enumerate(rr):groups[q][r,j,i,t].append(xs[k])
 rails=[]
 for i,a in enumerate(rawrails):
  v=var(f'rail{i}');rails.append({**a,'selector':v})
 for a,b in itertools.combinations(rails,2):
  if a['read']&b['read']:C.append([-a['selector'],-b['selector']])
 cells=[]
 for a,(q,es) in enumerate(sorted(groups.items())):
  orbit=M.key(q);level=q[0]//2
  # For an earlier period r=-j, j>=1, a potential phase offset l reads
  # level l+j. Their union starts exactly at min_l+1. Free treatment of
  # every such cell overapproximates ALL possible inherited entry fields.
  inherited=level>=lo[orbit]+1
  prev=var(f'input{a}')
  if not all_input_free and not inherited:
   xs=[z['selector'] for z in rails if orbit in z['black']]
   C.extend([-x,prev] for x in xs);C.append(xs+[-prev])
  for b,(event,xs) in enumerate(sorted(es.items())):
   active=var(f'a{a}_{b}');nxt=var(f'b{a}_{b}')
   C.extend([-x,active] for x in xs);C.append(xs+[-active])
   C.append([-active,prev if event[3]=='L' else -prev])
   C.extend([[prev,active,-nxt],[-prev,-active,-nxt],[prev,-active,nxt],[-prev,active,nxt]])
   prev=nxt
  cells.append(dict(position=q,orbit=orbit,level=level,earliest_possible_previous_level=lo[orbit]+1,
                    inherited_arbitrary=inherited,input_variable=names[f'input{a}']))
 return names,C,groups,rails,cells,lo,hi

def replay(names,assignment,rails,cells):
 images=[];byperiod=[]
 for r in range(PERIODS):
  one=[]
  for j,c in enumerate(M.REV):
   got=[w for k,w in enumerate(M.core.dom[c]) if assignment[names[f'x{r}_{j}_{k}']]]
   assert len(got)==1;one+=got
  images+=one;byperiod.append(one)
 word=''.join(images);inputB={tuple(c['position']) for c in cells if assignment[c['input_variable']]}
 board=set(inputB);q=0j;h=-1+0j
 for turn in word:
  p=(int(q.real),int(q.imag));assert (p in board)==(turn=='L')
  if p in board:board.remove(p)
  else:board.add(p)
  h*=(-1j if turn=='R' else 1j);q+=h
 assert q==complex(-2*PERIODS,-2*PERIODS) and h==-1
 selected=[i for i,r in enumerate(rails) if assignment[r['selector']]]
 return dict(images_by_period=byperiod,word=word,length=len(word),input_black=sorted(inputB),output_black=sorted(board),
             selected_rails=selected,nonstationary=len({tuple(x) for x in byperiod})>1,literal_complete_field_replay=True)

def main():
 M.O=O
 # Positive: the actual prepared108 pattern is fixed for every period and
 # all entry colors may be inferred. This checks finite chronology independently.
 pn,pc,pg,pr,ps,plo,phi=build(all_input_free=True)
 for r in range(PERIODS):
  for j,c in enumerate(M.REV):
   w='LRRRR' if j==31 else c
   pc.append([pn[f'x{r}_{j}_{M.core.dom[c].index(w)}']])
 for rail in pr:pc.append([-rail['selector']])
 positive,pa=M.z3solve(pn,pc,'prepared108_finite_positive');assert pa is not None
 positive.update(replay(pn,pa,pr,ps));(O/'prepared108_finite_positive.json').write_text(json.dumps(positive,indent=2)+'\n')
 # Independent-occurrence positive: enforce two distinct local choices, with
 # otherwise unrestricted entry board. A successful result is only a control.
 nn,nc,ng,nr,ns,nlo,nhi=build(all_input_free=True)
 nc += [[nn['x0_31_0']],[nn[f'x4_31_{M.core.dom["L"].index("LRRRR")}']]]
 for rail in nr:nc.append([-rail['selector']])
 nonstationary,na=M.z3solve(nn,nc,'nonstationary_finite_positive')
 if na is not None:nonstationary.update(replay(nn,na,nr,ns));assert nonstationary['nonstationary']
 (O/'nonstationary_finite_positive.json').write_text(json.dumps(nonstationary,indent=2)+'\n')
 names,C,groups,rails,cells,lo,hi=build()
 manifest=dict(scope=__doc__,periods=PERIODS,variables=len(names),clauses=len(C),physical_cells=len(cells),
               arbitrary_inherited_cells=sum(c['inherited_arbitrary'] for c in cells),
               prescribed_new_cells=sum(not c['inherited_arbitrary'] for c in cells),
               global_phase_level_range=[min(lo.values()),max(hi.values())],
               orbit_offset_ranges=[dict(orbit=a,min=lo[a],max=hi[a]) for a in sorted(lo)],cells=cells,
               source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               multirail_source_sha256=hashlib.sha256(Path(M.__file__).read_bytes()).hexdigest())
 (O/'architecture.json').write_text(json.dumps(manifest,indent=2)+'\n')
 cnf=O/'five_period.cnf';cnf.write_text(M.dimacs(names,C))
 out,assignment=M.z3solve(names,C,'five_period')
 if assignment is not None:out.update(replay(names,assignment,rails,cells))
 if out['result']=='UNSAT_ARCHITECTURE':
  proof=O/'five_period.rup';t=time.monotonic()
  pp=subprocess.run([str(M.core.HERE/'prove_cnf_rup'),str(cnf),str(proof),'100000'],capture_output=True,text=True,timeout=120)
  out.update(producer=pp.stdout.strip(),producer_returncode=pp.returncode,proof_seconds=time.monotonic()-t)
  if pp.returncode==0:
   kk=subprocess.run([str(M.core.HERE/'check_drat'),str(cnf),str(proof)],capture_output=True,text=True,timeout=120)
   assert kk.returncode==0,(kk.stdout,kk.stderr)
   vv=json.loads(kk.stdout);assert vv['valid'] and vv['RAT']==0 and vv['deletions']==0;out['checker']=vv
  out['rup_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
 out.update(scope=__doc__,periods=PERIODS,variables=len(names),clauses=len(C),
            source_sha256=manifest['source_sha256'],cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest(),
            inherited_arbitrary=manifest['arbitrary_inherited_cells'],prescribed_new_cells=manifest['prescribed_new_cells'])
 (O/'result.json').write_text(json.dumps(out,indent=2)+'\n')
 print({k:v for k,v in out.items() if k not in ('images_by_period','word','input_black','output_black')},flush=True)
if __name__=='__main__':main()
