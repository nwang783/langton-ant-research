import json,subprocess,time
from pathlib import Path
P=Path('dcv_anchored_transfer_min');J=json.load(open('dcv_anchored_transfer_v2/summary.json'));B=json.load(open('dcv_conditional_confinement_optimized.json'))['unproved_bad_transfers'];result=[]
M=json.load(open('seven_sub_dcv_port_quotient.json'))['macro_words'];D=[1j,1,-1j,-1];allpoints=[]
for m in M:
 p=0j;h=0;points=set()
 for c in m['word']+m['end_marker']:
  points.add((int(p.real),int(p.imag)));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 allpoints.append(sorted(points))
for idx in J['excluded']:
 b=B[idx-1];a=b['source_packet'];q=tuple(b['source_output']);points=allpoints[a];oldmode='source'if a!=5 else'nearest18';orig=json.load(open(f'dcv_anchored_transfer_v2/protected_patch_{idx:02d}_{oldmode}.json'));mask=sum(1<<points.index(tuple(p)) for p in orig['points']);startmask=mask;last=None;tests=[]
 # Retain q so the target pose necessarily belongs to the near-patch head set.
 for j in sorted(range(len(points)),key=lambda j:(-abs(points[j][0]-q[0])-abs(points[j][1]-q[1]),points[j])):
  if points[j]==q or not(mask>>j)&1:continue
  cand=mask^(1<<j);mode=f'mask{cand:x}';base=P/f'protected_patch_{idx:02d}_{mode}';t=time.time();subprocess.run(['python','generate_dcv_anchored_transfer_min.py',str(idx),mode],stdout=subprocess.DEVNULL,check=True)
  with open(str(base)+'_bfs.txt','w')as out,open(str(base)+'_bfs.log','w')as err:pr=subprocess.run(['/tmp/dcv_anchored_bfs',str(base)+'.dat','50000000'],stdout=out,stderr=err)
  line=Path(str(base)+'_bfs.txt').read_text().splitlines()[0];tests.append({'mask':cand,'result':line});hit='EXHAUSTED_NO_HIT'in line
  if hit:mask=cand;last=str(base)
  print('CASE',idx,'remove',points[j],'keep',not hit,'cells',mask.bit_count(),'seconds',round(time.time()-t,2),line,flush=True)
 result.append({'index':idx,'start_mask':startmask,'final_mask':mask,'points':[list(p)for j,p in enumerate(points)if mask>>j&1],'prefix':last,'tests':tests})
 (P/'summary.json').write_text(json.dumps({'status':'pending independent audit','results':result},indent=2));print('CASE_DONE',idx,'cells',mask.bit_count(),'prefix',last,flush=True)
