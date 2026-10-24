"""Same seven-period free-color problem, exact central controller classification.
No new horizon/palette: test whether the middle period differs from every
known legal controller (identity, and P108 only in the odd pair alignment).
"""
from pathlib import Path
import json,hashlib,subprocess,time
import check_heading_defect_backward_window as s
P=Path(__file__).resolve().parent;O=P/'heading_defect_local_classification';O.mkdir(exist_ok=True)
s.s.old.old.O=O

def run(cut):
 names,C,g,domains,W,h,bc=s.build(cut);assert C[16380]==bc;del C[16380]
 allowed=[[0]*52]
 if cut==1:
  z=json.loads((P/'heading_defect_pairs/cut1_root0_free.result.json').read_text())
  allowed.append([next(k for k,a in enumerate(d) if list(a)==z['images'][j]) for j,d in enumerate(domains[3])])
 for assignment in allowed:C.append([-names[f'x3_{j}_{k}'] for j,k in enumerate(assignment)])
 tag=f'cut{cut}';cnf=O/(tag+'.cnf');cnf.write_text(s.s.old.old.dimacs(names,C))
 (O/(tag+'.architecture.json')).write_text(json.dumps(dict(scope=__doc__,cut=cut,periods=7,central_period=3,allowed_central_assignments=allowed,variables=len(names),clauses=len(C)),indent=2)+'\n')
 out,model=s.s.old.old.z3solve(names,C,tag,timeout=30000);out.update(cut=cut,variables=len(names),clauses=len(C),allowed_central_assignments=allowed)
 if model:
  images=[[next(a for k,a in enumerate(d) if model[names[f'x{r}_{j}_{k}']]) for j,d in enumerate(row)] for r,row in enumerate(domains)]
  w=''.join(a[2] for row in images for a in row);hh=(h+2*int(model[names['h0']]))%4;rr,e,gg=s.s.old.old.core.trace(w,(0,0),hh)
  last={};I=set();B=set()
  for q,gh,c in rr:
   if q not in last and c=='L':I.add(q);B.add(q)
   assert(q in B)==(c=='L')
   if q in B:B.remove(q)
   else:B.add(q)
   last[q]=c
  out.update(images=images,word=w,start_heading=hh,final_heading=gg,input_black=sorted(I),output_black=sorted(B))
 elif out['result']=='UNSAT_ARCHITECTURE':
  proof=O/(tag+'.rup');t=time.monotonic();p=subprocess.run([str(s.s.old.old.core.HERE/'prove_cnf_rup'),str(cnf),str(proof),'100000'],capture_output=True,text=True,timeout=120)
  out.update(producer=p.stdout.strip(),producer_returncode=p.returncode,proof_seconds=time.monotonic()-t)
  if p.returncode==0:
   c=subprocess.run([str(s.s.old.old.core.HERE/'check_drat'),str(cnf),str(proof)],capture_output=True,text=True,timeout=120);assert c.returncode==0,(c.stdout,c.stderr);out['checker']=json.loads(c.stdout)
  out['rup_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
 out.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest())
 (O/(tag+'.result.json')).write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ['images','word','input_black','output_black','producer','allowed_central_assignments']},flush=True)
if __name__=='__main__':
 for cut in [0,1]:run(cut)
