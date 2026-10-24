from pathlib import Path
import json,subprocess,hashlib,time
R=Path(__file__).resolve().parents[1]/'core_periodicity_new';P=R/'chronology_dcuv';H=P/'hypothesis_U_upper3_post_dccc.tsv';out=P/'joint_DC_recurrent8_batch';out.mkdir(exist_ok=True);rows=[list(map(int,l.split()))for l in H.read_text().splitlines()];rows=[r for r in rows if r[0]==1 and r[1]==7];results=[]
manifest={'status':'Conditional JOINT all-three-produced events only; no individual freshness or closed family claim','profile':str(P/'profile_recurrent8.json'),'profile_sha256':hashlib.sha256((P/'profile_recurrent8.json').read_bytes()).hexdigest(),'H':str(H),'H_sha256':hashlib.sha256(H.read_bytes()).hexdigest(),'rows':rows,'results':results}
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
for i,row in enumerate(rows,1):
 if (out/'STOP').exists():break
 pref=out/f'case{i:02d}';jpref=Path(str(pref)+'_joint');base=Path(str(pref)+'_base');points=Path(str(pref)+'_goalpoints.json');x,y,h=row[2:5];pts=[[x+a,y+b]for a,b in [rot(z,h)for z in [(-1,4),(0,2),(0,3)]]];points.write_text(json.dumps(pts)+'\n');start=time.time()
 result={'index':i,'row':row,'goal_upper_cells':pts}
 with open(str(pref)+'.generate.log','w')as log:
  for cmd in [['python',str(R/'generate_resource_transfer_patch.py'),str(P/'profile_recurrent8.json'),*map(str,row),str(base),'sourceplus:'+str(points)],['python',str(R/'add_resource_joint_upper_fuel_fused.py'),str(base)+'.json',str(jpref),str(H),'all']]:
   z=subprocess.run(cmd,cwd=R,stdout=log,stderr=subprocess.STDOUT)
   if z.returncode:raise RuntimeError(str(cmd))
 result['n']=json.loads(Path(str(jpref)+'.json').read_text())['n']
 with open(str(jpref)+'.txt','w')as so,open(str(jpref)+'.log','w')as se:z=subprocess.run([str(R/'protected_patch_bdd_labels_witness_v2'),str(jpref)+'.dat','750000',str(jpref)+'.bdd'],stdout=so,stderr=se,cwd=R)
 txt=Path(str(jpref)+'.txt').read_text();result.update(returncode=z.returncode,result=txt[:2000],seconds=time.time()-start)
 if Path(str(jpref)+'.bdd').exists():
  with open(str(jpref)+'.verified.json','w')as f:q=subprocess.run(['python',str(R/'verify_protected_patch_bdd_labels.py'),str(jpref)+'.dat',str(jpref)+'.bdd'],stdout=f,stderr=subprocess.STDOUT,cwd=R)
  result['verified_no_hit']=q.returncode==0
 results.append(result);(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(i,row,'n',result['n'],'no_hit',result.get('verified_no_hit'),txt.splitlines()[:1],round(result['seconds'],2),flush=True)
