"""Search all negative-real k8 roots for a512-turn refinement.
A SAT model is a finite witness only; completed UNSAT statuses need a separate
proof certificate and independent encoding replay before a theorem claim.
"""
import sys,pathlib,json,time,collections
ROOT=pathlib.Path('/workspace/shared/langton');HERE=ROOT/'computability'
sys.path.insert(0,str(ROOT/'causal_reduction/morphic_candidates'))
from position_only_refinement import solve
q=json.loads((HERE/'negative_eight_prefixes.json').read_text());assert q['status']=='COMPLETE'
counts=collections.Counter();start=time.time();survivor=None
with open(HERE/'negative_eight_refinements.jsonl','w') as log:
 for i,p in enumerate(q['prefixes']):
  r=solve(8,(-2,-2),p['word'],p['choices'],timeout=10000);r['index']=i;counts[r['status']]+=1
  log.write(json.dumps({k:v for k,v in r.items() if k not in ('word','choices','entry_headings','seed')})+'\n');log.flush()
  if r['status']=='sat':
   survivor=i;(HERE/'negative_eight_refinement_survivor.json').write_text(json.dumps(r,indent=2));print('SAT',i,r['seed_size'],flush=True);break
  if i%100==0:print(i,dict(counts),time.time()-start,flush=True)
 summary=dict(status='DISCOVERY_ONLY',counts=dict(counts),tested=i+1,total=len(q['prefixes']),complete=i+1==len(q['prefixes']),survivor=survivor,seconds=time.time()-start)
 (HERE/'negative_eight_refinement_summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
