"""Candidate two-variable word extraction; not a proof."""
import json,gzip,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation2/planar_structure')
from extract_exceptional_template import long_runs
for r in [29,32,38,55,56,62,71]:
 coords=[(100,100),(101,100),(100,101)];words=[gzip.open(HERE/f'r{r}_n{n}_p{p}.txt.gz','rt').read() for n,p in coords];runs=[long_runs(w,208) for w in words];assert len(set(map(len,runs)))==1;last=[0]*3;segments=[]
 for j in range(len(runs[0])):
  fixed=[w[e:rr[j][0]] for w,e,rr in zip(words,last,runs)];assert len(set(fixed))==1,(r,j,'fixed')
  if fixed[0]:segments.append(dict(type='finite',word=fixed[0]))
  periods=[w[rr[j][0]:rr[j][0]+104] for w,rr in zip(words,runs)];assert len(set(periods))==1
  if j==len(runs[0])-1:tail=periods[0];break
  counts=[rr[j][1] for rr in runs];a=counts[1]-counts[0];b=counts[2]-counts[0];c=counts[0]-100*a-100*b
  segments.append(dict(type='periods',word=periods[0],count_np=[a,b,c]));last=[rr[j][0]+104*rr[j][1] for rr in runs]
 out=dict(status='candidate pending complete bivariate replay',phase=r,segments=segments,infinite_tail_word=tail)
 (HERE/f'template_r{r}.json').write_text(json.dumps(out,indent=2)+'\n');print(r,[(s['type'],len(s['word']),s.get('count_np')) for s in segments])
