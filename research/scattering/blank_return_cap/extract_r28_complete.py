"""Candidate extraction only, not an all-parameter validation."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation2/planar_structure')
from extract_exceptional_template import long_runs
params=[(100,100),(101,100),(100,101),(101,101)]
words=[gzip.open(HERE/f'r28_complete_m{m}_k{k}.txt.gz','rt').read() for m,k in params];runs=[long_runs(w,208) for w in words];assert len({len(r) for r in runs})==1
last=[0]*4;segments=[]
for j in range(len(runs[0])):
 blocks=[w[e:r[j][0]] for w,e,r in zip(words,last,runs)];assert len(set(blocks))==1,(j,'fixed block')
 if blocks[0]:segments.append(dict(type='finite',word=blocks[0]))
 ws=[w[r[j][0]:r[j][0]+104] for w,r in zip(words,runs)];assert len(set(ws))==1
 if j==len(runs[0])-1:tail=ws[0];break
 counts=[r[j][1] for r in runs];a=counts[1]-counts[0];b=counts[2]-counts[0];c=counts[0]-100*a-100*b;assert counts[3]==101*a+101*b+c
 segments.append(dict(type='periods',word=ws[0],count_mk=[a,b,c]));last=[r[j][0]+104*r[j][1] for r in runs]
out=dict(status='candidate: requires exact bivariate full-field check',segments=segments,infinite_tail_word=tail)
(HERE/'r28_complete_template.json').write_text(json.dumps(out,indent=2)+'\n')
print([(s['type'],len(s['word']),s.get('count_mk')) for s in segments])
