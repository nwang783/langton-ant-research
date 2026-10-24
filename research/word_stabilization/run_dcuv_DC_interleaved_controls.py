from pathlib import Path
import json,subprocess,time
R=Path(__file__).resolve().parents[1]/'core_periodicity_new';P=R/'chronology_dcuv/upper3_DC_recurrent8_batch';M=json.loads((P/'manifest.json').read_text());O=P/'interleaved';O.mkdir(exist_ok=True);results=[]
for e in M['results']:
 if e.get('no_hit')or e['last'].get('stop')!='no reconstructed witness':continue
 q=Path(e['last']['prefix']);pref=O/f"case{e['index']:02d}";t=time.time();z=subprocess.run(['python',str(R/'permute_guarded_reset_model.py'),str(q)+'.json',str(pref),'interleave'],cwd=R,capture_output=True,text=True);assert z.returncode==0,z.stderr
 z=subprocess.run([str(R/'protected_patch_bdd_labels'),str(pref)+'.dat','750000',str(pref)+'.bdd'],cwd=R,capture_output=True,text=True);Path(str(pref)+'.txt').write_text(z.stdout);Path(str(pref)+'.log').write_text(z.stderr);res={'index':e['index'],'row':e['row'],'source':str(q),'permuted':str(pref),'result':z.stdout.strip(),'seconds':time.time()-t}
 if 'EXHAUSTED_NO_HIT'in z.stdout:
  v=subprocess.run(['python',str(R/'verify_protected_patch_bdd_labels.py'),str(pref)+'.dat',str(pref)+'.bdd'],cwd=R,capture_output=True,text=True);res['verification']=v.stdout.strip();res['verify_returncode']=v.returncode
 results.append(res);(O/'summary.json').write_text(json.dumps({'status':'Conditional fixed-H model results; permutation wrapper needs independent review','results':results},indent=2)+'\n');print(e['index'],res['result'],round(res['seconds'],2),flush=True)
