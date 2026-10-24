import subprocess,json,time,hashlib
from pathlib import Path
P=Path('dcv_anchored_transfer');B=json.load(open('dcv_conditional_confinement_optimized.json'))['unproved_bad_transfers'];solved={};pending=[]
for i,g in enumerate(B,1):
 mode='source' if g['source_packet']!=5 else 'nearest18';base=P/f'protected_patch_{i:02d}_{mode}';result=(base.parent/(base.name+'_bfs.txt')).read_text().splitlines()[0]
 if 'EXHAUSTED_NO_HIT' in result:solved[i]={'stage':0,'prefix':str(base),'result':result}
 else:pending.append(i)
for stage in range(1,10):
 tag=f'r{stage}';extra=P/f'{tag}_extra.tsv'
 rows=[]
 for i in solved:
  g=B[i-1];rows.append([g['source_packet'],g['target_packet'],*g['target_pose'],*g['source_output']])
 extra.write_text(''.join(' '.join(map(str,row))+'\n' for row in rows));new=[]
 for i in pending:
  g=B[i-1];mode='source' if g['source_packet']!=5 else 'nearest18';base=P/f'protected_patch_{i:02d}_{mode}_{tag}';t=time.time()
  subprocess.run(['python','generate_dcv_anchored_transfer_staged.py',str(i),mode,tag],check=True,stdout=subprocess.DEVNULL)
  with open(str(base)+'_bfs.txt','w')as out,open(str(base)+'_bfs.log','w')as err:r=subprocess.run(['/tmp/dcv_anchored_bfs',str(base)+'.dat','50000000'],stdout=out,stderr=err)
  result=Path(str(base)+'_bfs.txt').read_text().splitlines()[0];print('STAGE',stage,'CASE',i,'return',r.returncode,'seconds',round(time.time()-t,3),result,flush=True)
  if 'EXHAUSTED_NO_HIT'in result:solved[i]={'stage':stage,'prefix':str(base),'result':result};new.append(i)
 pending=[i for i in pending if i not in new];print('STAGE_FINISH',stage,'new',len(new),'total',len(solved),'pending',pending,flush=True)
 (P/'staged_summary.json').write_text(json.dumps({'status':'discovery results pending independent audit','solved':solved,'pending':pending,'last_stage':stage},indent=2))
 if not new or not pending:break
