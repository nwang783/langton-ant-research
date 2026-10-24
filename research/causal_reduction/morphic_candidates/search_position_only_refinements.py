"""Look for exact deeper critical-area models; stop at the first SAT survivor.
UNSAT is scoped to one root prefix. Only a completed all-prefix run is exhaustive.
"""
import json,pathlib,sys,time
from position_only_refinement import solve,HERE
k=int(sys.argv[1]);a=tuple(map(int,sys.argv[2].split(',')))
sources=json.load(open(HERE/f'position_only_prefixes_k{k}_a{a[0]}_{a[1]}.json'))
assert sources['status']=='COMPLETE'
stem=f'position_only_refinements_k{k}_a{a[0]}_{a[1]}'
start=time.time();counts={};survivors=[]
with open(HERE/(stem+'.jsonl'),'w') as log:
 for i,prefix in enumerate(sources['prefixes']):
  result=solve(k,a,prefix['word'],prefix['choices']);result['index']=i
  counts[result['status']]=counts.get(result['status'],0)+1
  small={key:value for key,value in result.items() if key not in ('word','choices','entry_headings','seed')}
  log.write(json.dumps(small)+'\n');log.flush()
  if result['status']=='sat':
   (HERE/(stem+'_survivor.json')).write_text(json.dumps(result,indent=2));survivors.append(i);print('SAT',i,result['seed_size'],flush=True);break
  if i%100==0:print(i,counts,round(time.time()-start,2),flush=True)
 out=dict(k=k,scale=a,counts=counts,tested=i+1,total=len(sources['prefixes']),survivors=survivors,complete=i+1==len(sources['prefixes']),seconds=time.time()-start)
 (HERE/(stem+'_summary.json')).write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
