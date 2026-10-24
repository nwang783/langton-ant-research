import json,subprocess,time
from pathlib import Path
P=Path('/workspace/shared/langton/core_periodicity_new');g=P/'generate_protected_transfer_patch.py';b=P/'probe_protected_patch_bfs';orig=json.loads((P/'protected_patch_source.json').read_text());pts=orig['points'];mask=(1<<len(pts))-1;records=[]
# Drop distant cells first, keep q as a transparent protection anchor.
order=sorted(range(len(pts)),key=lambda i:-sum(abs(pts[i][j]-[2,3][j])for j in[0,1]))
for i in order:
 if pts[i]==[2,3]:continue
 mm=mask&~(1<<i);name=f'protected_patch_min_drop{i}';subprocess.run(['python',str(g),'1','0','2','2','0','2','3',name,f'mask{mm:x}'],check=True,capture_output=True)
 st=time.time()
 with(P/f'{name}.txt').open('w')as o,(P/f'{name}.log').open('w')as e:r=subprocess.run([str(b),str(P/f'{name}.dat'),'50000000'],stdout=o,stderr=e)
 status=(P/f'{name}.txt').read_text().splitlines()[0] if(P/f'{name}.txt').stat().st_size else f'rc{r.returncode}'
 accepted='EXHAUSTED_NO_HIT'in status
 if accepted:mask=mm
 rec={'drop':pts[i],'drop_index':i,'mask':f'{mm:x}','accepted':accepted,'status':status,'seconds':round(time.time()-st,3),'file':name};records.append(rec);print(rec,flush=True)
(P/'protected_patch_minimization.json').write_text(json.dumps({'remaining_mask':f'{mask:x}','remaining_points':[p for i,p in enumerate(pts)if mask>>i&1],'trials':records},indent=2))
