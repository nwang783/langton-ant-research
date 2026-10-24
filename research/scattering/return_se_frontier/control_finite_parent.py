"""Literal controls only. The replay is not an all-parameter proof."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent;R=HERE.parents[1]
sys.path.insert(0,str(R/'continuation_2026-10-22/ant_continuation'))
from ant_exact import step,plan,W,certify_period
ROWS=json.loads((HERE/'parallel_model_discovery.json').read_text())[:22]
Q,_,_,_=plan(W,(0,0),2)
def control(m,n):
 q=(-33-2*n,-14-2*n);a=(-33-2*n,41+2*n);origin=(-62-2*m,2+2*m)
 core={r['r']:(origin[0]+Q[r['r']][0],origin[1]+Q[r['r']][1]) for r in ROWS}
 B={q,a};p=(0,0);h=0;T=416*n-104*m+122376
 for t in range(T):
  assert p not in set(core.values()),(t,p)
  p,h,ch=step(B,p,h)
 assert (p,h)==(origin,2),(p,h,origin)
 results=[]
 for r in ROWS:
  f=set(B);f.add(core[r['r']]);p=origin;h=2
  word=gzip.open(HERE/r['word_file'],'rt').read()
  for t,expected in enumerate(word):
   p,h,ch=step(f,p,h);assert ch==expected,(r['r'],t,p,ch,expected)
  assert (p[0]-origin[0],p[1]-origin[1])==tuple(r['pose'][0]) and h==r['pose'][1]
  cert=certify_period(f,p,h,r['tail_word'])
  out=dict(r=r['r'],m=m,n=n,all_local_reads_match=True,local_capture=T+len(word),complete_finite_tail=cert)
  results.append(out);print(json.dumps(out),flush=True)
 return results
if __name__=='__main__':
 rows=control(100,400)+control(101,401)
 (HERE/'finite_parent_controls.json').write_text(json.dumps(rows,indent=2)+'\n')
