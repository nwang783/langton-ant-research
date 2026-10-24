from pathlib import Path
import json,subprocess,time
R=Path(__file__).resolve().parents[1];D=R/'chronology_dcuv';summary=[]
for name in ['t1h3','t6h0','t6h3','t7h1','t9h0','t1h3_plus5']:
 base=D/'global_record_rest'/name;p=base.with_name(name+'_white');start=time.time();subprocess.run(['python',str(R/'normalize_global_record_initial_white.py'),str(base.with_suffix('.json')),str(p)],check=True)
 with p.with_suffix('.log').open('w')as f:subprocess.run([str(R/'protected_patch_bdd_labels'),str(p.with_suffix('.dat')),'1000000',str(p.with_suffix('.bdd'))],stdout=f,stderr=f)
 status=[l for l in p.with_suffix('.log').read_text().splitlines()if l.startswith('status ')][-1]
 if 'EXHAUSTED_NO_HIT'in status:
  r=subprocess.run(['python',str(R/'verify_protected_patch_bdd_labels.py'),str(p.with_suffix('.dat')),str(p.with_suffix('.bdd'))],capture_output=True,text=True);assert r.returncode==0;p.with_suffix('.verify').write_text(r.stdout+r.stderr)
 summary.append({'prefix':str(p),'status':status,'seconds':time.time()-start});(D/'global_record_rest/white_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary[-1]),flush=True)
