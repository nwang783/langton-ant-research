"""Candidate bivariate extraction; the independent symbolic replay is the proof."""
import json,gzip,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation2/planar_structure');from extract_exceptional_template import long_runs
coords=[(100,100),(101,100),(100,101),(101,101)];words=[gzip.open(HERE/f'actual_m{m}_k{k}.txt.gz','rt').read() for m,k in coords];runs=[long_runs(w,208) for w in words];assert len(set(map(len,runs)))==1;last=[0]*4;segments=[]
for j in range(len(runs[0])):
 fixed=[w[e:rr[j][0]] for w,e,rr in zip(words,last,runs)];assert len(set(fixed))==1
 if fixed[0]:segments.append(dict(type='finite',word=fixed[0]))
 periods=[w[rr[j][0]:rr[j][0]+104] for w,rr in zip(words,runs)];assert len(set(periods))==1
 if j==len(runs[0])-1:tail=periods[0];break
 counts=[rr[j][1] for rr in runs];a=counts[1]-counts[0];b=counts[2]-counts[0];assert counts[3]==counts[0]+a+b;c=counts[0]-100*a-100*b
 segments.append(dict(type='periods',word=periods[0],count_mk=[a,b,c]));last=[rr[j][0]+104*rr[j][1] for rr in runs]
out=dict(status='candidate pending complete bivariate replay',segments=segments,infinite_tail_word=tail);(HERE/'template.json').write_text(json.dumps(out,indent=2)+'\n');print([(s['type'],len(s['word']),s.get('count_mk')) for s in segments])
