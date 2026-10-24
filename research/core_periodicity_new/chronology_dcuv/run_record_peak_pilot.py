from pathlib import Path
import json,subprocess,time,sys
R=Path(__file__).resolve().parents[1];D=R/'chronology_dcuv';J=json.loads((D/'record_peak_inventory01.json').read_text());out=D/'record_peak_pilot';profile=D/'profile_recurrent8.json';potential=D/'potential_extend_dcv_policy01_saturated.json'
rows=[r for r in J['rows']if r[0]==0 and r[1]in (0,7)];summary=[]
for i,row in enumerate(rows):
 a,b,x,y,h,qx,qy,phase,threshold=row;p=out/f'case{i+1:02d}';q=p.with_name(p.name+'_fused');coords=[]
 for u,v in json.load(open(D/'literal_residual_geometry.json'))['geometry'][b]['inputs']:
  u,v=[(u,v),(v,-u),(-u,-v),(-v,u)][h];coords.append([x+u,y+v])
 p.with_suffix('.extra.json').write_text(json.dumps(coords));start=time.time()
 commands=[['python',str(R/'generate_resource_transfer_patch.py'),str(profile),*map(str,row[:7]),str(p),'sourceplus:'+str(p.with_suffix('.extra.json'))],['python',str(R/'add_resource_record_peak_fused.py'),str(p.with_suffix('.json')),str(q),str(potential),str(phase)]]
 for cmd in commands:subprocess.run(cmd,check=True,stdout=subprocess.DEVNULL)
 with q.with_suffix('.log').open('w')as f:subprocess.run([str(R/'protected_patch_bdd_labels'),str(q.with_suffix('.dat')),'750000',str(q.with_suffix('.bdd'))],stdout=f,stderr=f)
 log=q.with_suffix('.log').read_text();status=[l for l in log.splitlines()if l.startswith('status ')][-1]
 if status.startswith('status EXHAUSTED_NO_HIT'):
  res=subprocess.run(['python',str(R/'verify_protected_patch_bdd_labels.py'),str(q.with_suffix('.dat')),str(q.with_suffix('.bdd'))],capture_output=True,text=True);assert res.returncode==0,res.stdout+res.stderr;q.with_suffix('.verify').write_text(res.stdout+res.stderr)
 summary.append({'case':i+1,'row':row,'prefix':str(q),'status':status,'seconds':time.time()-start});(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary[-1]),flush=True)
