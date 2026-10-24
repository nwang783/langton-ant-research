"""Simultaneous minimal two-turn bypasses in inverse104.
This finite architecture removes intermediate unit-pose alignment. Each
coarse pair has only its identity and the two ANALYTICALLY MINIMAL bypasses.
First test arbitrary prepared input; rail input is a separate layer.
"""
from pathlib import Path
import collections,itertools,json,hashlib,subprocess,time
import synthesize_multirail_short_refinement as old
from check_pair_bypass_scaffold import histories
P=Path(__file__).resolve().parent;O=P/'pair_bypass_simultaneous';O.mkdir(exist_ok=True)
old.O=O
S=json.loads((P/'short_refinement_scaffold_inputs.json').read_text());V=S['reverse104']
PAL=json.loads((P/'minimal_pair_bypass_geometry.json').read_text())['inventories']

def build(cut,mode,nonidentity=True):
 names={};clauses=[]
 def var(s):
  if s not in names:names[s]=len(names)+1
  return names[s]
 coarse,_,_=old.core.trace(V,(0,0),3);heading=coarse[cut][1];word=V[cut:]+V[:cut]
 rows,e,g=old.core.trace(word,(0,0),heading);assert(e,g)==((-2,-2),heading)
 groups=collections.defaultdict(lambda:collections.defaultdict(list));nonid=[]
 for j in range(52):
  phase=2*j;p,h=rows[phase][:2];pair=word[phase:phase+2]
  xx=[var(f'x{j}_{k}') for k in range(3)];nonid+=xx[1:]
  clauses.append(xx);clauses.extend([-a,-b] for a,b in itertools.combinations(xx,2))
  for k,w in enumerate(PAL[pair]):
   rr,ee,gg=old.core.trace(w,p,h);assert(ee,gg)==old.core.trace(pair,p,h)[1:]
   for i,(q,hh,t) in enumerate(rr):groups[old.key(q)][q[0]//2,j,i,t].append(xx[k])
 if nonidentity:clauses.append(nonid)
 rails=[];conflicts=[]
 if mode=='rails':
  for name,h in [('NE',1),('SW',3)]:
   R,B=old.standard_profile(h)
   shifts={(a[0]-b[0],(a[1]-b[1])%2) for a in groups for b in B if (a[0]-b[0]+h-heading)%2==0}
   for normal,parity in sorted(shifts):
    tr=lambda q:(q[0]+normal,(q[1]+parity)%2)
    rails.append(dict(orientation=name,normal_shift=normal,x_parity_shift=parity,read=set(map(tr,R)),black=set(map(tr,B))))
  for i,r in enumerate(rails):r['selector']=var(f'rail{i}')
  for i,j in itertools.combinations(range(len(rails)),2):
   if rails[i]['read']&rails[j]['read']:
    conflicts.append((i,j));clauses.append([-rails[i]['selector'],-rails[j]['selector']])
 for a,(orbit,ev) in enumerate(sorted(groups.items())):
  prev=var(f'input{a}')
  if mode=='rails':
   rs=[r['selector'] for r in rails if orbit in r['black']]
   clauses.extend([[-x,prev] for x in rs]+[rs+[-prev]])
  elif mode!='free':raise ValueError(mode)
  for b,(event,xs) in enumerate(sorted(ev.items())):
   active=var(f'a{a}_{b}');nxt=var(f'b{a}_{b}')
   clauses.extend([-x,active] for x in xs);clauses.append(xs+[-active])
   clauses.append([-active,prev if event[3]=='L' else -prev])
   clauses.extend([[prev,active,-nxt],[-prev,-active,-nxt],[prev,-active,nxt],[-prev,active,nxt]])
   prev=nxt
 return names,clauses,groups,rails,conflicts,word,heading

def run(cut,mode,nonidentity=True):
 names,C,groups,rails,conflicts,word,heading=build(cut,mode,nonidentity)
 tag=f'cut{cut}_{mode}'+('' if nonidentity else '_identity_allowed')
 cnf=O/(tag+'.cnf');cnf.write_text(old.dimacs(names,C))
 manifest=dict(cut=cut,mode=mode,nonidentity=nonidentity,heading=heading,coarse_word=word,palettes=PAL,
               variables=len(names),clauses=len(C),orbits=sorted(groups),rails=[{**{k:v for k,v in r.items() if k not in ('read','black')},'read':sorted(r['read']),'black':sorted(r['black'])} for r in rails],
               rail_conflicts=conflicts,cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest())
 (O/(tag+'.architecture.json')).write_text(json.dumps(manifest,indent=2)+'\n')
 out,model=old.z3solve(names,C,tag,timeout=30000);out.update(cut=cut,mode=mode,variables=len(names),clauses=len(C))
 if model:
  images=[]
  for j in range(52):
   pair=word[2*j:2*j+2];ws=[w for k,w in enumerate(PAL[pair]) if model[names[f'x{j}_{k}']]];assert len(ws)==1;images+=ws
  literal=histories(''.join(images),heading);assert literal['status']=='LEGAL_PREPARED_PERIODIC'
  out.update(images=images,nonidentity_pairs=sum(len(w)>2 for w in images),literal=literal)
  if mode=='rails':
   sel=[i for i,r in enumerate(rails) if model[r['selector']]]
   black=set().union(*(rails[i]['black'] for i in sel)) if sel else set()
   read=set(tuple(a['orbit']) for a in literal['complete_histories'])
   assert black&read==set(map(tuple,literal['input_black_classes']))
   out.update(selected_rails=sel,input_black_classes=sorted(black))
 else:
  if out['result']=='UNSAT_ARCHITECTURE':
   proof=O/(tag+'.rup');t=time.monotonic()
   p=subprocess.run([str(old.core.HERE/'prove_cnf_rup'),str(cnf),str(proof),'100000'],capture_output=True,text=True,timeout=120)
   out.update(producer=p.stdout.strip(),producer_returncode=p.returncode,proof_seconds=time.monotonic()-t)
   if p.returncode==0:
    c=subprocess.run([str(old.core.HERE/'check_drat'),str(cnf),str(proof)],capture_output=True,text=True,timeout=120)
    assert c.returncode==0,(c.stdout,c.stderr);out['checker']=json.loads(c.stdout)
   out['rup_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
 out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
 (O/(tag+'.result.json')).write_text(json.dumps(out,indent=2)+'\n')
 print(tag,{k:v for k,v in out.items() if k not in ['images','literal','producer']},flush=True)
 return out
if __name__=='__main__':
 for cut in [0,1]:
  out=run(cut,'free')
  if out['result']=='SAT_BULK_ONLY':run(cut,'rails')
