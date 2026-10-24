from pathlib import Path
import json,subprocess,time,hashlib
R=Path(__file__).resolve().parents[1]/'core_periodicity_new';D=R/'chronology_dcuv';out=D/'global_record_v_vc_0329';out.mkdir(exist_ok=True);profile=D/'profile_recurrent8.json';potential=D/'record_head_offset_search/head_1_1.json';gen=R/'generate_resource_global_record_snapshot0329.py';results=[];manifest={'status':'Provisional entire-prefix record event closures; independent generator/model audit required','profile':str(profile),'profile_sha256':hashlib.sha256(profile.read_bytes()).hexdigest(),'potential':str(potential),'potential_sha256':hashlib.sha256(potential.read_bytes()).hexdigest(),'generator':str(gen),'generator_sha256':hashlib.sha256(gen.read_bytes()).hexdigest(),'events':[[4,0],[4,1],[5,0],[5,3]],'results':results}
for a,phase in manifest['events']:
 pref=out/f'target{a}_phase{phase}';start=time.time()
 with open(str(pref)+'.generate.log','w')as f:subprocess.run(['python',str(gen),str(profile),str(potential),str(a),str(phase),str(pref),'context','all'],stdout=f,stderr=f,check=True,cwd=R)
 with open(str(pref)+'.txt','w')as so,open(str(pref)+'.log','w')as se:z=subprocess.run([str(R/'protected_patch_bdd_labels'),str(pref)+'.dat','750000',str(pref)+'.bdd'],stdout=so,stderr=se,cwd=R)
 txt=Path(str(pref)+'.txt').read_text();r={'target':a,'phase':phase,'prefix':str(pref),'returncode':z.returncode,'result':txt,'seconds':time.time()-start}
 if 'EXHAUSTED_NO_HIT'in txt:
  with open(str(pref)+'.verified.json','w')as f:q=subprocess.run(['python',str(R/'verify_protected_patch_bdd_labels.py'),str(pref)+'.dat',str(pref)+'.bdd'],stdout=f,stderr=subprocess.STDOUT,cwd=R)
  r['verified']=q.returncode==0;assert r['verified']
 results.append(r);(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(r,flush=True)
