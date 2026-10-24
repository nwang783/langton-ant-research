from pathlib import Path
import subprocess,json,time
R=Path(__file__).resolve().parents[1]/'core_periodicity_new';D=R/'chronology_dcuv/global_record_v_vc_0329';O=D/'whitened';O.mkdir(exist_ok=True);results=[]
for a,ph in [(4,1),(5,3)]:
 src=D/f'target{a}_phase{ph}.json';pref=O/f'target{a}_phase{ph}';t=time.time()
 with open(str(pref)+'.generate.log','w')as f:subprocess.run(['python',str(R/'restrict_record_initial_high_white.py'),str(src),str(pref)],stdout=f,stderr=f,check=True)
 with open(str(pref)+'.txt','w')as so,open(str(pref)+'.log','w')as se:z=subprocess.run([str(R/'protected_patch_bdd_labels'),str(pref)+'.dat','750000',str(pref)+'.bdd'],stdout=so,stderr=se)
 txt=Path(str(pref)+'.txt').read_text();r={'target':a,'phase':ph,'prefix':str(pref),'returncode':z.returncode,'result':txt,'seconds':time.time()-t}
 if 'EXHAUSTED_NO_HIT'in txt:
  with open(str(pref)+'.verified.json','w')as f:q=subprocess.run(['python',str(R/'verify_protected_patch_bdd_labels.py'),str(pref)+'.dat',str(pref)+'.bdd'],stdout=f,stderr=subprocess.STDOUT)
  r['verified']=q.returncode==0;assert r['verified']
 results.append(r);(O/'summary.json').write_text(json.dumps(results,indent=2)+'\n');print(r,flush=True)
