"""All compatible finite standard-rail INPUT bundles for one reverse scaffold.
Same complete exact-pose1/5/9 palette as the signed single-wake result.
No palette, period, geometric-radius, or cap escalation. SAT is BULK ONLY.
"""
from pathlib import Path
import collections,itertools,json,hashlib,subprocess,time,sys
import certify_short_refinement_rup as core
P=Path(__file__).resolve().parent
O=P/'multirail_short_refinement';O.mkdir(exist_ok=True)
H=core.H
REV=''.join('L' if c=='R' else 'R' for c in H[::-1])

def key(q):return q[0]-q[1],q[0]%2

def standard_profile(h):
 rows,e,g=core.trace(H,(0,0),h);assert g==h and e in [(2,2),(-2,-2)]
 by=collections.defaultdict(list)
 for i,(q,hh,c) in enumerate(rows):
  by[key(q)].append((i-(1 if e[0]>0 else -1)*104*(q[0]//2),c))
 for vv in by.values():
  vv.sort();assert vv[0][1]=='R'
  assert all(a[1]!=b[1] for a,b in zip(vv,vv[1:]))
 read=set(by);black={q for q,v in by.items() if v[-1][1]=='R'}
 lo=min(q[0] for q in read);hi=max(q[0] for q in read)
 assert hi-lo==10 and read=={(t,p) for t in range(lo,hi+1) for p in (0,1)}
 assert all((t,p) in black for t in (lo,hi) for p in (0,1))
 return read,black

def build(word=REV, mode='rails'):
 names={};clauses=[]
 def var(s):
  if s not in names:names[s]=len(names)+1
  return names[s]
 true=var('TRUE');clauses.append([true])
 groups=collections.defaultdict(lambda:collections.defaultdict(list))
 coarse,e,g=core.trace(word,(0,0),3);assert (e,g)==((-2,-2),3)
 for j,(p,h,c) in enumerate(coarse):
  xx=[var(f'x{j}_{k}') for k in range(len(core.dom[c]))]
  clauses.append(xx)
  clauses.extend([-a,-b] for a,b in itertools.combinations(xx,2))
  for k,w in enumerate(core.dom[c]):
   rr,ee,gg=core.trace(w,p,h);assert (ee,gg)==core.trace(c,p,h)[1:]
   for i,(q,hh,t) in enumerate(rr):groups[key(q)][q[0]//2,j,i,t].append(xx[k])
 # Every relevant rail must have a black class meeting the possible read set.
 # Same-sector E/W launches differ by even coordinate sum, i.e. even normal.
 rails=[]
 for name,h in [('NE',1),('SW',3)]:
  R,B=standard_profile(h)
  shifts={(a[0]-b[0],(a[1]-b[1])%2) for a in groups for b in B if (a[0]-b[0])%2==0}
  for normal,parity in sorted(shifts):
   tr=lambda q:(q[0]+normal,(q[1]+parity)%2)
   rails.append(dict(orientation=name,normal_shift=normal,x_parity_shift=parity,
                     read=set(map(tr,R)),black=set(map(tr,B))))
 for i,r in enumerate(rails):r['selector']=var(f'rail{i}')
 conflicts=[]
 for i,j in itertools.combinations(range(len(rails)),2):
  if rails[i]['read']&rails[j]['read']:
   conflicts.append((i,j));clauses.append([-rails[i]['selector'],-rails[j]['selector']])
 input_constraints=[]
 for a,(orbit,ev) in enumerate(sorted(groups.items())):
  prev=var(f'input{a}')
  if mode=='rails':
   rs=[r['selector'] for r in rails if orbit in r['black']]
   cc=[[-x,prev] for x in rs]+[rs+[-prev]]
   clauses.extend(cc);input_constraints.extend(cc)
  elif mode!='free':raise ValueError(mode)
  for b,(event,xs) in enumerate(sorted(ev.items())):
   active=var(f'a{a}_{b}');nxt=var(f'b{a}_{b}')
   clauses.extend([-x,active] for x in xs);clauses.append(xs+[-active])
   clauses.append([-active,prev if event[3]=='L' else -prev])
   clauses.extend([[prev,active,-nxt],[-prev,-active,-nxt],[prev,-active,nxt],[-prev,active,nxt]])
   prev=nxt
 return names,clauses,groups,rails,conflicts,input_constraints

def dimacs(names,clauses):
 return f'p cnf {len(names)} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in clauses)

def z3solve(names,clauses,tag,timeout=30000):
 sys.path.insert(0,str(P.parents[1]/'periodic_classification_new'))
 from probe_one_a_local_constraints import mkcontext,mkconfig,mksolver,inc,parse,solve,getmodel,modelstr,reason
 from synthesize_axis_compact_clock import values
 neg=lambda x:f'v{x}' if x>0 else f'(not v{-x})'
 txt='\n'.join(['(set-logic QF_UF)',f'(set-option :timeout {timeout})','(set-option :produce-models true)']+
               [f'(declare-fun v{i} () Bool)' for i in range(1,len(names)+1)]+
               ['(assert '+('false' if not c else neg(c[0]) if len(c)==1 else '(or '+' '.join(map(neg,c))+')')+')' for c in clauses])+'\n'
 (O/(tag+'.smt2')).write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());t=time.monotonic();ans=solve(ctx,sol)
 out=dict(result={1:'SAT_BULK_ONLY',-1:'UNSAT_ARCHITECTURE',0:'UNKNOWN'}[ans],seconds=time.monotonic()-t)
 if ans==1:
  model=modelstr(ctx,getmodel(ctx,sol)).decode();(O/(tag+'.model')).write_text(model)
  vv=values(model);assignment={i:bool(vv[f'v{i}']) for i in range(1,len(names)+1)}
  assert all(any(assignment[abs(x)]==(x>0) for x in c) for c in clauses)
  return out,assignment
 if ans==0:out['reason']=reason(ctx,sol).decode()
 return out,None

def main():
 names,C,groups,rails,conflicts,inp=build()
 manifest=dict(scope=__doc__,scaffold=REV,start=[0,0,'W'],local_images=core.dom,
               possible_read_orbits=sorted(groups),rail_candidates=len(rails),incompatible_pairs=len(conflicts),
               rails=[{**{k:v for k,v in r.items() if k not in ('read','black')},'read':sorted(r['read']),'black':sorted(r['black'])} for r in rails],
               variables=len(names),clauses=len(C),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               core_source_sha256=hashlib.sha256(Path(core.__file__).read_bytes()).hexdigest())
 (O/'architecture.json').write_text(json.dumps(manifest,indent=2)+'\n')
 cnf=O/'all_bundles.cnf';cnf.write_text(dimacs(names,C))
 # Direct truth-table controls on the new OR/profile layer, including every
 # single rail and every pairwise-compatible two-rail assignment.
 assignments=[()]+[(i,) for i in range(len(rails))]+[(i,j) for i,j in itertools.combinations(range(len(rails)),2) if not(rails[i]['read']&rails[j]['read'])]
 for chosen in assignments:
  bits={r['selector']:i in chosen for i,r in enumerate(rails)}
  B=set().union(*(rails[i]['black'] for i in chosen)) if chosen else set()
  bits.update({names[f'input{a}']:q in B for a,q in enumerate(sorted(groups))})
  assert all(any(bits[abs(x)]==(x>0) for x in cc) for cc in inp)
 out=dict(scope=__doc__,variables=len(names),clauses=len(C),rail_candidates=len(rails),
          profile_layer_controls=len(assignments),cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest())
 result,model=z3solve(names,C,'all_bundles');out.update(result)
 if model is not None:
  chosen_rails=[i for i,r in enumerate(rails) if model[r['selector']]]
  inputB=set().union(*(rails[i]['black'] for i in chosen_rails)) if chosen_rails else set()
  images=[]
  for j,c in enumerate(REV):
   vv=[w for k,w in enumerate(core.dom[c]) if model[names[f'x{j}_{k}']]];assert len(vv)==1;images+=vv
  word=''.join(images);rr,e,g=core.trace(word,(0,0),3);assert (e,g)==((-2,-2),3)
  hh=collections.defaultdict(list)
  for t,(q,h,c) in enumerate(rr):hh[key(q)].append((t+len(word)*(q[0]//2),c))
  for q,v in hh.items():
   v.sort();assert (v[0][1]=='L')==(q in inputB)
   assert all(a[1]!=b[1] for a,b in zip(v,v[1:]))
  out.update(selected_rails=chosen_rails,images=images,word=word,length=len(word),
             input_black_classes=sorted(inputB),output_black_classes=sorted(inputB^{q for q,v in hh.items() if len(v)%2}),literal_orbit_replay=True)
 if out['result']=='UNSAT_ARCHITECTURE':
  proof=O/'all_bundles.rup';t=time.monotonic()
  rr=subprocess.run([str(core.HERE/'prove_cnf_rup'),str(cnf),str(proof),'100000'],capture_output=True,text=True,timeout=120)
  out.update(producer=rr.stdout.strip(),producer_returncode=rr.returncode,proof_seconds=time.monotonic()-t)
  if rr.returncode==0:
   kk=subprocess.run([str(core.HERE/'check_drat'),str(cnf),str(proof)],capture_output=True,text=True,timeout=120)
   assert kk.returncode==0,(kk.stdout,kk.stderr)
   vv=json.loads(kk.stdout);assert vv['valid'] and vv['RAT']==0 and vv['deletions']==0;out['checker']=vv
  out['rup_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
 out['source_sha256']=manifest['source_sha256']
 (O/'result.json').write_text(json.dumps(out,indent=2)+'\n');print(out,flush=True)
if __name__=='__main__':main()
