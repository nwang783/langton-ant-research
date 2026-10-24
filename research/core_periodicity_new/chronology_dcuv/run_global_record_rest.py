from pathlib import Path
import json,subprocess,time
R=Path(__file__).resolve().parents[1];D=R/'chronology_dcuv';out=D/'global_record_rest';out.mkdir(exist_ok=True);G=json.load(open(D/'literal_residual_geometry.json'))['geometry'];rows=[(1,3),(6,0),(6,3),(7,1),(8,0),(9,0)];summary=[]
for a,h in rows:
 p=out/f't{a}h{h}';watch='all'if len(G[a]['requirements'])<=25 else'inputs';start=time.time();subprocess.run(['python',str(R/'generate_resource_global_record.py'),str(D/'profile_recurrent8.json'),str(D/'record_head_offset_search/head_1_1.json'),str(a),str(h),str(p),'context',watch],check=True)
 with p.with_suffix('.log').open('w')as f:subprocess.run([str(R/'protected_patch_bdd_labels'),str(p.with_suffix('.dat')),'1000000',str(p.with_suffix('.bdd'))],stdout=f,stderr=f)
 status=[l for l in p.with_suffix('.log').read_text().splitlines()if l.startswith('status ')][-1]
 if 'EXHAUSTED_NO_HIT'in status:
  r=subprocess.run(['python',str(R/'verify_protected_patch_bdd_labels.py'),str(p.with_suffix('.dat')),str(p.with_suffix('.bdd'))],capture_output=True,text=True);assert r.returncode==0;p.with_suffix('.verify').write_text(r.stdout+r.stderr)
 summary.append({'target':a,'phase':h,'watch':watch,'prefix':str(p),'status':status,'seconds':time.time()-start});(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary[-1]),flush=True)
