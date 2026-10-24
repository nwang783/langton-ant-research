from pathlib import Path
import subprocess,json,time,sys
R=Path(__file__).resolve().parents[1]/'core_periodicity_new';D=R/'chronology_dcuv';O=D/'global_record_v_vc_0329/v1_refinement';O.mkdir(exist_ok=True)
base=json.loads((D/'global_record_v_vc_0329/goal_origins/target4_phase1_base.json').read_text());pts=set(map(tuple,base['points']));pts|={(-1,-2),(-1,1)}
for z in sys.argv[1:]:pts.add(tuple(map(int,z.split(','))))
patch=O/'patch_plus2.json';patch.write_text(json.dumps(sorted(pts)))
p=O/'v1_plus2';t=time.time()
cmds=[['python',str(R/'generate_resource_global_record_snapshot0329.py'),str(D/'profile_recurrent8.json'),str(D/'record_head_offset_search/head_1_1.json'),'4','1',str(p)+'_base','file:'+str(patch),'inputs'],['python',str(R/'normalize_global_record_initial_white.py'),str(p)+'_base.json',str(p)]]
for cmd in cmds:subprocess.run(cmd,check=True)
with open(str(p)+'.txt','w')as f,open(str(p)+'.log','w')as e:r=subprocess.run([str(R/'protected_patch_bdd_labels'),str(p)+'.dat','750000',str(p)+'.bdd'],stdout=f,stderr=e)
txt=Path(str(p)+'.txt').read_text();print(txt,flush=True)
if 'EXHAUSTED_NO_HIT'in txt:
 with open(str(p)+'.verified.json','w')as f:subprocess.run(['python',str(R/'verify_protected_patch_bdd_labels.py'),str(p)+'.dat',str(p)+'.bdd'],stdout=f,check=True)
elif 'ABSTRACT_WITNESS'in txt:
 with open(str(p)+'.witness.txt','w')as f,open(str(p)+'.witness.log','w')as e:subprocess.run([str(R/'protected_patch_bdd_labels_witness_v2'),str(p)+'.dat','1000000'],stdout=f,stderr=e)
 subprocess.run(['python',str(Path(__file__).parent/'analyze_global_record_witness.py'),str(p)+'.json',str(p)+'.witness.txt',str(p)+'.analysis.json'],check=True)
print('seconds',time.time()-t)
