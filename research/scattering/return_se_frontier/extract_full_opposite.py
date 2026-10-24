"""Candidate extraction only; final artificial discovery stopping periods removed."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation2/planar_structure')
from extract_exceptional_template import long_runs
OFF={15:10,45:13,72:13}
def load(r,m,k):
 n=m+k+OFF[r];w=gzip.open(HERE/f'full_opposite_r{r}_m{m}_k{k}.txt.gz','rt').read()
 return w[416*n-104*m+122376:]
def main():
 for r in (15,45,72):
  w0,w1=load(r,100,200),load(r,100,201);runs0,runs1=long_runs(w0,208),long_runs(w1,208)
  assert len(runs0)==len(runs1)
  # The last run is a true discovered permanent tail; omit its arbitrary
  # sampling-dependent number of trailing periods from the finite template.
  assert len(w0)-(runs0[-1][0]+104*runs0[-1][1])<104
  assert len(w1)-(runs1[-1][0]+104*runs1[-1][1])<104
  segments=[];last0=last1=0;tw=None
  for j,((a0,c0),(a1,c1)) in enumerate(zip(runs0,runs1)):
   assert w0[last0:a0]==w1[last1:a1]
   if a0>last0:segments.append(dict(type='finite',word=w0[last0:a0]))
   assert w0[a0:a0+104]==w1[a1:a1+104]
   if j==len(runs0)-1:tw=w0[a0:a0+104];break
   slope=c1-c0;assert slope>=0
   segments.append(dict(type='periods',word=w0[a0:a0+104],count=[slope,c0-200*slope]))
   last0=a0+104*c0;last1=a1+104*c1
  assert load(r,101,200)[:runs0[-1][0]]==w0[:runs0[-1][0]]
  assert load(r,101,201)[:runs1[-1][0]]==w1[:runs1[-1][0]]
  out=dict(status='candidate; exact full-field replay required',phase=r,domain='m>=100,k>=200,n=m+k+offset',offset=OFF[r],segments=segments,infinite_tail_word=tw)
  (HERE/f'full_opposite_template_r{r}.json').write_text(json.dumps(out,indent=2)+'\n')
  print(json.dumps(dict(phase=r,segments=[dict(type=s['type'],length=len(s['word']),count=s.get('count')) for s in segments]),indent=2))
if __name__=='__main__':main()
