from pathlib import Path
import json,hashlib,subprocess
import synthesize_heading_defect_pairs as s
P=Path(__file__).resolve().parent;O=P/'heading_defect_pairs';s.old.old.O=O
names,C,g,domains,W,h,rails,con=s.build(1,0,'free')
z=json.loads((O/'cut1_root0_free.result.json').read_text());images=z['images']
chosen=[names[f'x{j}_{next(k for k,a in enumerate(d) if list(a)==images[j])}'] for j,d in enumerate(domains)]
C.append([-v for v in chosen]);tag='cut1_root0_free_except_P108';cnf=O/(tag+'.cnf');cnf.write_text(s.old.old.dimacs(names,C))
out,model=s.old.old.z3solve(names,C,tag,timeout=30000)
out.update(blocked_images=images,variables=len(names),clauses=len(C),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest())
if out['result']=='UNSAT_ARCHITECTURE':
 proof=O/(tag+'.rup');p=subprocess.run([str(s.old.old.core.HERE/'prove_cnf_rup'),str(cnf),str(proof),'100000'],capture_output=True,text=True,timeout=120)
 out.update(producer=p.stdout.strip(),producer_returncode=p.returncode)
 if p.returncode==0:
  c=subprocess.run([str(s.old.old.core.HERE/'check_drat'),str(cnf),str(proof)],capture_output=True,text=True,timeout=120);assert c.returncode==0;out['checker']=json.loads(c.stdout)
 out['rup_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
(O/(tag+'.result.json')).write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ['blocked_images','producer']})
