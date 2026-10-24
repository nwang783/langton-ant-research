from pathlib import Path
import subprocess,json,time
R=Path(__file__).resolve().parents[1]/'core_periodicity_new';D=R/'chronology_dcuv';O=D/'global_record_v_vc_0329/goal_origins';O.mkdir(exist_ok=True);res=[]
for a,ph in [(4,1),(5,3)]:
 base=O/f'target{a}_phase{ph}_base';p=O/f'target{a}_phase{ph}';t=time.time()
 for cmd in [['python',str(R/'generate_resource_global_record_snapshot0329.py'),str(D/'profile_recurrent8.json'),str(D/'record_head_offset_search/head_1_1.json'),str(a),str(ph),str(base),'context','inputs'],['python',str(R/'normalize_global_record_initial_white.py'),str(base)+'.json',str(p)]]:
  with open(str(p)+'.generate.log','a')as f:subprocess.run(cmd,stdout=f,stderr=f,check=True)
 with open(str(p)+'.txt','w')as so,open(str(p)+'.log','w')as se:z=subprocess.run([str(R/'protected_patch_bdd_labels'),str(p)+'.dat','750000',str(p)+'.bdd'],stdout=so,stderr=se)
 txt=Path(str(p)+'.txt').read_text();r={'target':a,'phase':ph,'prefix':str(p),'returncode':z.returncode,'result':txt,'seconds':time.time()-t}
 if 'EXHAUSTED_NO_HIT'in txt:
  with open(str(p)+'.verified.json','w')as f:q=subprocess.run(['python',str(R/'verify_protected_patch_bdd_labels.py'),str(p)+'.dat',str(p)+'.bdd'],stdout=f,stderr=subprocess.STDOUT)
  r['verified']=q.returncode==0;assert r['verified']
 res.append(r);(O/'summary.json').write_text(json.dumps(res,indent=2)+'\n');print(r,flush=True)
