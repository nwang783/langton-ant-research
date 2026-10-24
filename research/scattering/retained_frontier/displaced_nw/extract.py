"""Three-sample bivariate candidate extraction, not a proof."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation2/planar_structure')
from extract_exceptional_template import long_runs

def word(r,m,n):
 with gzip.open(HERE/f'word_r{r}_m{m}_n{n}.txt.gz','rt') as f:return f.read()

def main():
 for phase in [70,75]:
  words=[word(phase,*p) for p in [(100,200),(101,201),(100,201)]];runs=[long_runs(w) for w in words];assert len(set(map(len,runs)))==1
  lasts=[0,0,0];segments=[]
  for trip in zip(*runs):
   gaps=[w[last:a] for w,last,(a,count) in zip(words,lasts,trip)];assert len(set(gaps))==1
   if gaps[0]:segments.append(dict(type='finite',word=gaps[0]))
   periods=[w[a:a+104] for w,(a,count) in zip(words,trip)];assert len(set(periods))==1
   counts=[t[1] for t in trip];aff=[counts[1]-counts[0],counts[2]-counts[0],counts[0]]
   segments.append(dict(type='periods',word=periods[0],count=aff));lasts=[a+104*count for a,count in trip]
  gaps=[w[last:] for w,last in zip(words,lasts)];assert len(set(gaps))==1
  if gaps[0]:segments.append(dict(type='finite',word=gaps[0]))
  # Two independent unused samples are still discovery controls, not proof.
  for m,n in [(102,202),(100,300)]:
   u,v=m-100,n-m-100
   generated=''.join(s['word']*(sum(a*b for a,b in zip(s['count'],(u,v,1))) if s['type']=='periods' else 1) for s in segments)
   assert generated==word(phase,m,n)
  out=dict(status='candidate only; requires complete affine-field verification',phase=phase,variables='u=m-100,v=n-m-100',segments=segments,infinite_tail_word=words[0][-104:])
  (HERE/f'template_r{phase}.json').write_text(json.dumps(out,indent=2)+'\n')
  print(json.dumps(dict(phase=phase,segments=[dict(type=s['type'],length=len(s['word']),count=s.get('count')) for s in segments]),indent=2))
if __name__=='__main__':main()
