"""Exact live-path pruning with explicit identity OUT edges, independent audit."""
from pathlib import Path
from collections import defaultdict
import json,sys
from check_record_far_height_independent import check as farcheck,datacheck,invariant,OUT
from check_dcuv_producer_model_independent import ROOT,digest,resolve_file

def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text());assert J['format']=='guarded_reset_live_pruning_v1'
 bp=resolve_file(path,J['base_model_file']);assert digest(bp)==J['base_model_sha256'];B=json.loads(bp.read_text())
 if B['format']=='guarded_reset_global_record_far_height_dfa_v1':farcheck(bp)
 elif B['format']=='guarded_reset_global_record_far_height_first_funding_v1':
  from check_record_far_first_independent import check as firstcheck
  firstcheck(bp)
 elif B['format']=='guarded_reset_global_record_far_transverse_bands_v1':
  from check_record_transverse_independent import check as transversecheck
  transversecheck(bp)
 else:raise AssertionError('Unreviewed live-pruning base '+B['format'])
 rows=B['transitions']+[[B['out'],q,0,0,0,0,0,0,99]for q in B['reentry']]
 fwd=defaultdict(set);back=defaultdict(set);goals=set()
 for a,b,k,v,f,c,r,g,w in rows:
  assert v&~k==r&~c==0 and not((k|v|f|c|r)>>B['n'])
  if g:goals.add(a)
  else:fwd[a].add(b);back[b].add(a)
 def fixed(start,adj):
  done=set(start);todo=set(start)
  while todo:
   new=set.union(set(),*(adj[a]for a in todo))-done;done|=new;todo=new
  return done
 reachable=fixed([B['start'][0]],fwd);coaccessible=fixed(goals,back);live=sorted(reachable&coaccessible);assert B['start'][0]in live
 ids={p:i for i,p in enumerate(live)};out=len(live)
 expected=[[ids[a],ids.get(b,out),k,v,f,c,r,g,w]for a,b,k,v,f,c,r,g,w in rows if a in ids and(g or b in ids)]
 for k,val in [('reachable_ignoring_guards',sorted(reachable)),('coaccessible_ignoring_guards',sorted(coaccessible)),('retained_old_positions',live),('transitions',expected),('out',out),('start',[ids[B['start'][0]],*B['start'][1:]]),('reentry',[]),('n',B['n'])]:assert J[k]==val,k
 datacheck(path,J);result={'status':'PASS independent exact live-path pruning','variables':B['n'],'positions':out+1,'edges':len(expected),'hashes':{str(p.relative_to(ROOT)):digest(p)for p in[path,path.with_suffix('.dat'),bp]}}
 invariant(path,result);(OUT/(path.stem+'.model_check.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True);return result
if __name__=='__main__':
 for p in sys.argv[1:]:check(p)
