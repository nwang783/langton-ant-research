from pathlib import Path
import json,subprocess,time
R=Path(__file__).resolve().parents[1];D=R/'chronology_dcuv/global_record_residual';summary=[]
for name in ['t7h1','t6h0','t9h0']:
 base=D/name;p=base.with_name(name+'_I64');start=time.time();subprocess.run(['python',str(R/'raise_global_record_activation_weight.py'),str(base.with_suffix('.json')),str(p),'64'],check=True)
 with p.with_suffix('.log').open('w')as f:subprocess.run([str(R/'protected_patch_bdd_labels'),str(p.with_suffix('.dat')),'1000000',str(p.with_suffix('.bdd'))],stdout=f,stderr=f)
 status=[l for l in p.with_suffix('.log').read_text().splitlines()if l.startswith('status ')][-1]
 if 'EXHAUSTED_NO_HIT'in status:
  r=subprocess.run(['python',str(R/'verify_protected_patch_bdd_labels.py'),str(p.with_suffix('.dat')),str(p.with_suffix('.bdd'))],capture_output=True,text=True);assert r.returncode==0;p.with_suffix('.verify').write_text(r.stdout+r.stderr)
 summary.append({'prefix':str(p),'status':status,'seconds':time.time()-start});(D/'I64_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary[-1]),flush=True)
