import json,time,collections
from smt_inflation_refinement import HERE,refinement
D=json.load(open(HERE/'free_inflations_k9.json'))
O=next(z['images']for z in D['results']if z['scale']==[3,0]);words=O['R']+O['L'];C=collections.Counter();start=time.time()
with open(HERE/'smt_all_coarse81.jsonl','w')as f:
 for index,line in enumerate(open(HERE/'free_nine_coarse81_prefixes.csv')):
  ids=list(map(int,line.split(',')));fixed=[words[i]for i in ids];coarse=''.join(fixed)
  out=refinement(coarse,fixed,O,1000);out.update(index=index,initial_choices=ids);C[out['status']]+=1
  f.write(json.dumps(out)+'\n');f.flush()
  if index%50==0 or out['status']!='unsat':print(index,dict(C),round(time.time()-start,2),flush=True)
  if out['status']=='sat':break
summary=dict(counts=dict(C),seconds=time.time()-start,processed=sum(C.values()),total=1280)
(HERE/'smt_all_coarse81_summary.json').write_text(json.dumps(summary,indent=2));print(summary,flush=True)
