"""Candidate word extraction from two discoveries. Not a proof."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation2/planar_structure')
from extract_exceptional_template import long_runs
from discover import FRESH
for r in FRESH:
 words=[gzip.open(HERE/f'r{r}_k{k}.txt.gz','rt').read() for k in (100,101)]
 runs=[long_runs(w,208) for w in words];assert len(runs[0])==len(runs[1]);last=[0,0];segments=[]
 for j in range(len(runs[0])):
  blocks=[w[e:rr[j][0]] for w,e,rr in zip(words,last,runs)];assert blocks[0]==blocks[1],(r,j,'fixed block')
  if blocks[0]:segments.append(dict(type='finite',word=blocks[0]))
  w=[ww[rr[j][0]:rr[j][0]+104] for ww,rr in zip(words,runs)];assert w[0]==w[1]
  if j==len(runs[0])-1:tail=w[0];break
  counts=[rr[j][1] for rr in runs];a=counts[1]-counts[0];b=counts[0]-100*a
  segments.append(dict(type='periods',word=w[0],count=[a,b]));last=[rr[j][0]+104*rr[j][1] for rr in runs]
 out=dict(status='candidate; complete all-k proof required',phase=r,segments=segments,infinite_tail_word=tail)
 (HERE/f'template_r{r}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(r,[(s['type'],len(s['word']),s.get('count')) for s in segments],flush=True)
