"""Two-sample candidate extraction only; certify.py supplies the proof."""
import sys,json,gzip,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation2/planar_structure')
from extract_exceptional_template import long_runs

def main():
 base=200
 with gzip.open(HERE/f'word_{base}.txt.gz','rt') as f:w0=f.read()
 with gzip.open(HERE/f'word_{base+1}.txt.gz','rt') as f:w1=f.read()
 r0,r1=long_runs(w0),long_runs(w1)
 assert len(r0)==len(r1)
 last0=last1=0;segments=[]
 for (a0,c0),(a1,c1) in zip(r0,r1):
  assert w0[last0:a0]==w1[last1:a1],('fixed piece differs',a0,a1)
  if a0>last0:segments.append(dict(type='finite',word=w0[last0:a0]))
  assert w0[a0:a0+104]==w1[a1:a1+104]
  coefficient=c1-c0;constant=c0-coefficient*base
  segments.append(dict(type='periods',word=w0[a0:a0+104],count=[coefficient,constant]))
  last0=a0+104*c0;last1=a1+104*c1
 assert w0[last0:]==w1[last1:]
 if last0<len(w0):segments.append(dict(type='finite',word=w0[last0:]))
 out=dict(status='candidate, exact affine verification required',base=base,fixed_core=[-223,231],
  time=[len(w1)-len(w0),len(w0)-base*(len(w1)-len(w0))],segments=segments,infinite_tail_word=w0[-104:])
 (HERE/'template.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('segments','infinite_tail_word')},indent=2))
 print(json.dumps([dict(type=s['type'],length=len(s['word']),count=s.get('count')) for s in segments],indent=2))
if __name__=='__main__':main()
