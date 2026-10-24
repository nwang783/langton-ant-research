from pathlib import Path
import json,subprocess,time
R=Path(__file__).resolve().parents[1];D=R/'chronology_dcuv';old=json.loads((D/'record_peak_pilot/summary.json').read_text());out=D/'record_peak_both';out.mkdir(exist_ok=True);summary=[]
for s in old:
 if 'ABSTRACT_WITNESS'not in s['status']:continue
 row=s['row'];p=out/f"case{s['case']:02d}";q=p.with_name(p.name+'_fused');start=time.time()
 for cmd in [['python',str(R/'generate_resource_transfer_patch.py'),str(D/'profile_recurrent8.json'),*map(str,row[:7]),str(p),'both'],['python',str(R/'add_resource_record_peak_fused.py'),str(p.with_suffix('.json')),str(q),str(D/'potential_extend_dcv_policy01_saturated.json'),str(row[7])]]:subprocess.run(cmd,check=True,stdout=subprocess.DEVNULL)
 with q.with_suffix('.log').open('w')as f:subprocess.run([str(R/'protected_patch_bdd_labels'),str(q.with_suffix('.dat')),'750000',str(q.with_suffix('.bdd'))],stdout=f,stderr=f)
 status=[l for l in q.with_suffix('.log').read_text().splitlines()if l.startswith('status ')][-1]
 if 'EXHAUSTED_NO_HIT'in status:
  res=subprocess.run(['python',str(R/'verify_protected_patch_bdd_labels.py'),str(q.with_suffix('.dat')),str(q.with_suffix('.bdd'))],capture_output=True,text=True);assert res.returncode==0;q.with_suffix('.verify').write_text(res.stdout+res.stderr)
 summary.append({'case':s['case'],'row':row,'prefix':str(q),'status':status,'seconds':time.time()-start});(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary[-1]),flush=True)
