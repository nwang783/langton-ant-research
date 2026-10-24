"""Candidate extraction only; remove arbitrary trailing discovery periods."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation2/planar_structure')
from extract_exceptional_template import long_runs
PARAMS=[(100,400),(101,400),(100,401),(101,401)]
def main(r):
 words=[];runs=[]
 for m,n in PARAMS:
  w=gzip.open(HERE/f'full_return_r{r}_m{m}_n{n}.txt.gz','rt').read()[624*n+104*m+195082:];words.append(w);runs.append(long_runs(w,208))
 assert len({len(x) for x in runs})==1
 last=[0]*4;segments=[];tail=None
 for j in range(len(runs[0])):
  blocks=[w[end:rr[j][0]] for w,end,rr in zip(words,last,runs)];assert len(set(blocks))==1,(r,j,'fixed block mismatch')
  if blocks[0]:segments.append(dict(type='finite',word=blocks[0]))
  pwords=[w[rr[j][0]:rr[j][0]+104] for w,rr in zip(words,runs)];assert len(set(pwords))==1,(r,j,'period mismatch')
  if j==len(runs[0])-1:tail=pwords[0];break
  counts=[rr[j][1] for rr in runs];am=counts[1]-counts[0];an=counts[2]-counts[0];b=counts[0]-400*an-100*am;assert counts[3]==an*401+am*101+b
  segments.append(dict(type='periods',word=pwords[0],count_nm=[an,am,b]))
  last=[rr[j][0]+104*rr[j][1] for rr in runs]
 out=dict(status='candidate; exact full-field proof required',phase=r,segments=segments,infinite_tail_word=tail)
 (HERE/f'full_return_template_r{r}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(dict(phase=r,segments=[dict(type=s['type'],length=len(s['word']),count=s.get('count_nm')) for s in segments]),indent=2))
if __name__=='__main__':
 for r in (28,38,46,60,61,70,75):main(r)
