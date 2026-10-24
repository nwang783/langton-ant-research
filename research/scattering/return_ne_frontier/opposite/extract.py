"""Univariate candidate extraction only."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent;OLD=HERE.parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation2/planar_structure');from extract_exceptional_template import long_runs
for phase in [70,75]:
 words=[gzip.open(OLD/f'opposite_r{phase}_k{k}.txt.gz','rt').read() for k in [100,101,102]];runs=[long_runs(w,208) for w in words];assert len(set(map(len,runs)))==1;last=[0]*3;segments=[]
 for j in range(len(runs[0])):
  fixed=[w[e:rr[j][0]] for w,e,rr in zip(words,last,runs)];assert len(set(fixed))==1
  if fixed[0]:segments.append(dict(type='finite',word=fixed[0]))
  periods=[w[rr[j][0]:rr[j][0]+104] for w,rr in zip(words,runs)];assert len(set(periods))==1
  if j==len(runs[0])-1:tail=periods[0];break
  counts=[rr[j][1] for rr in runs];a=counts[1]-counts[0];assert counts[2]==counts[0]+2*a;segments.append(dict(type='periods',word=periods[0],count_k_constant=[a,counts[0]-100*a]));last=[rr[j][0]+104*rr[j][1] for rr in runs]
 (HERE/f'template_r{phase}.json').write_text(json.dumps(dict(status='candidate pending symbolic all-k replay',segments=segments,infinite_tail_word=tail),indent=2)+'\n');print(phase,[(s['type'],len(s['word']),s.get('count_k_constant')) for s in segments])
