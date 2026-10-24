from pathlib import Path
import json,subprocess,hashlib,time
R=Path(__file__).resolve().parents[1]/'core_periodicity_new';P=R/'chronology_dcuv';H=P/'hypothesis_U_upper3.tsv';out=P/'upper3_DC_batch';out.mkdir(exist_ok=True);rows=[list(map(int,l.split()))for l in H.read_text().splitlines()];rows=[r for r in rows if r[0]==1 and r[1]==7];results=[]
manifest={'status':'Conditional discovery; no closed family claim','profile':str(P/'profile.json'),'profile_sha256':hashlib.sha256((P/'profile.json').read_bytes()).hexdigest(),'H':str(H),'H_sha256':hashlib.sha256(H.read_bytes()).hexdigest(),'rows':rows,'results':results}
for i,row in enumerate(rows,1):
 pref=out/f'case{i:02d}';summary=Path(str(pref)+'_summary.json')
 if summary.exists():raise SystemExit('Refusing overwrite '+str(summary))
 start=time.time();cmd=['python',str(R/'run_resource_producer_refinement.py'),'--profile',str(P/'profile.json'),'--hypotheses',str(H),'--signed',str(P/'empty.tsv'),'--row',*map(str,row),'--prefix',str(pref),'--rounds','8','--cap','1500000','--expand']
 with open(str(pref)+'.log','w')as f:z=subprocess.run(cmd,cwd=R,stdout=f,stderr=subprocess.STDOUT)
 result={'index':i,'row':row,'returncode':z.returncode,'seconds':time.time()-start,'summary':str(summary)}
 if summary.exists():
  j=json.loads(summary.read_text());last=j['results'][-1]if j['results']else{};result['last']=last;result['no_hit']='verification'in last
 results.append(result);(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(i,row,'no_hit',result.get('no_hit'),round(result['seconds'],2),flush=True)
 if z.returncode:print('ERROR inspect',pref,flush=True)
