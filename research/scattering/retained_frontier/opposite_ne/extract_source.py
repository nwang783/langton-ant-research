"""Extract a one-depth source-frame candidate; all-age proof is separate."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation2/planar_structure')
from extract_exceptional_template import long_runs

def sourceword(r,m,n,k):
 with gzip.open(HERE/f'word_r{r}_m{m}_n{n}_k{k}_full1.txt.gz','rt') as f:w=f.read()
 return w[208*n+104*m+70738:]
def main():
 for r in [29,56,62]:
  w0=sourceword(r,100,200,200);w1=sourceword(r,100,200,201)
  assert w0==sourceword(r,100,201,200)
  assert w1==sourceword(r,101,201,201)
  runs0,runs1=long_runs(w0),long_runs(w1);assert len(runs0)==len(runs1)
  last0=last1=0;segments=[]
  for (a0,c0),(a1,c1) in zip(runs0,runs1):
   assert w0[last0:a0]==w1[last1:a1]
   if a0>last0:segments.append(dict(type='finite',word=w0[last0:a0]))
   assert w0[a0:a0+104]==w1[a1:a1+104]
   slope=c1-c0;segments.append(dict(type='periods',word=w0[a0:a0+104],count=[slope,c0-200*slope]))
   last0=a0+104*c0;last1=a1+104*c1
  assert w0[last0:]==w1[last1:]
  if last0<len(w0):segments.append(dict(type='finite',word=w0[last0:]))
  out=dict(status='source-frame candidate; needs exact full-field and all-age verification',phase=r,source_age=100,parameter='k>=200',segments=segments,infinite_tail_word=w0[-104:])
  (HERE/f'source_template_r{r}.json').write_text(json.dumps(out,indent=2)+'\n')
  print(json.dumps(dict(phase=r,segments=[dict(type=s['type'],length=len(s['word']),count=s.get('count')) for s in segments]),indent=2))
if __name__=='__main__':main()
