"""Discovery controls for lowering the retained-core threshold; no extrapolation."""
import sys,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation')
from ant_exact import step,certify_period
T=json.loads((HERE/'template.json').read_text())

def run(m):
 n=m+100;S=(-23-2*m,31+2*m);B={S,(-33-2*n,-14-2*n),(-33-2*n,41+2*n),(8+2*n,-14-2*n),(8+2*n,41+2*n)}
 counts={1:n+8,3:n+7,5:m,7:m+2,9:n-20,11:n+m+10};p=(0,0);h=0;t=0
 for i,s in enumerate(T['segments']):
  for _ in range(counts[i] if s['type']=='periods' else 1):
   for expected in s['word']:
    before=p,h;p,h,ch=step(B,p,h)
    if ch!=expected:return dict(m=m,n=n,status='template mismatch',t=t,segment=i,pose=before,expected=expected,actual=ch)
    t+=1
 assert t==416*n+312*m+197704 and p==(-2*m-28,2*m+68) and h==0
 assert certify_period(B,p,h,T['infinite_tail_word'])
 return dict(m=m,n=n,status='literal word and tail pass',capture=t)
if __name__=='__main__':
 out=[]
 for m in range(0,101,5):
  r=run(m);out.append(r);print(json.dumps(r),flush=True)
 (HERE/'small_core_discovery.json').write_text(json.dumps(out,indent=2)+'\n')
