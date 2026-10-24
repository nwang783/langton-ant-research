"""Arbitrary per-occurrence unit square insertion, all entry colors free.
Classify the central inverse104 period without a fixed even/odd pairing.
"""
from pathlib import Path
import collections,json,hashlib,subprocess,time
import check_pair_bypass_flexible_tiling as geom
P=Path(__file__).parent;O=P/'unit_square_flexible_classification';O.mkdir(exist_ok=True);geom.s.old.O=O;N=728

def build(require_other=True):
 names={};C=[]
 def var(t):
  if t not in names:names[t]=len(names)+1
  return names[t]
 groups=collections.defaultdict(lambda:collections.defaultdict(list));blocks={};bad=[]
 for i in range(N):
  p,h,c=geom.pose(i);words=[c,c+('L'if c=='R'else'R')*4];xs=[var(f'x{i}_{k}')for k in(0,1)];C += [xs,[-xs[0],-xs[1]]]
  if 312<=i<416 and i%104!=31:bad.append(xs[1])
  for k,w in enumerate(words):
   rr,end,head=geom.s.old.core.trace(w,p,h);assert(end,head)==geom.pose(i+1)[:2];blocks[i,k]=rr
   for j,(q,hh,t)in enumerate(rr):groups[q][i,j,t].append(xs[k])
 if require_other:C.append(bad)
 for a,(q,ev)in enumerate(sorted(groups.items())):
  prev=var(f'input{a}')
  for b,(event,xs)in enumerate(sorted(ev.items())):
   active=var(f'a{a}_{b}');nxt=var(f'b{a}_{b}');C.extend([-x,active]for x in xs);C.append(xs+[-active]);C.append([-active,prev if event[2]=='L'else-prev])
   C.extend([[prev,active,-nxt],[-prev,-active,-nxt],[prev,-active,nxt],[-prev,active,nxt]]);prev=nxt
 return names,C,groups,blocks

def run():
 names,C,g,blocks=build();tag='square';cnf=O/(tag+'.cnf');cnf.write_text(geom.s.old.dimacs(names,C));(O/(tag+'.architecture.json')).write_text(json.dumps(dict(scope=__doc__,periods=7,central_period=3,allowed_square_phase=31,coarse_word=geom.s.V,variables=len(names),clauses=len(C),physical_cells=sorted(g)),indent=2)+'\n')
 out,model=geom.s.old.z3solve(names,C,tag,timeout=30000);out.update(variables=len(names),clauses=len(C),cells=len(g))
 if model:
  chosen=[i for i in range(N)if model[names[f'x{i}_1']]];rr=[row for i in range(N)for row in blocks[i,int(i in chosen)]];I=set();B=set();last={}
  for q,h,c in rr:
   if q not in last and c=='L':I.add(q);B.add(q)
   assert(q in B)==(c=='L')
   if q in B:B.remove(q)
   else:B.add(q)
   last[q]=c
  out.update(square_indices=chosen,input_black=sorted(I),output_black=sorted(B),length=len(rr))
 elif out['result']=='UNSAT_ARCHITECTURE':
  proof=O/(tag+'.rup');t=time.monotonic();p=subprocess.run([str(geom.s.old.core.HERE/'prove_cnf_rup'),str(cnf),str(proof),'100000'],capture_output=True,text=True,timeout=120);out.update(producer=p.stdout.strip(),producer_returncode=p.returncode,proof_seconds=time.monotonic()-t)
  if p.returncode==0:
   c=subprocess.run([str(geom.s.old.core.HERE/'check_drat'),str(cnf),str(proof)],capture_output=True,text=True,timeout=120);assert c.returncode==0;out.update(checker=json.loads(c.stdout))
  out['rup_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
 out.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest());(O/(tag+'.result.json')).write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in['producer','input_black','output_black']},flush=True)
if __name__=='__main__':run()
