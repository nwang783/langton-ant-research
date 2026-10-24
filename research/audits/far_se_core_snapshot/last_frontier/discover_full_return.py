"""Literal complete five-cell discovery after the final NW retained-core hit."""
import sys,json,gzip
from pathlib import Path
R=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,plan,step,PHASES,certify_period
Q,_,_,_=plan(W,(0,0),0)
def run(r,m,n,cap=2000000):
 o=(37+2*m,25-2*m);q=(-33-2*n,-14-2*n);a=(-33-2*n,41+2*n);s=(o[0]+Q[r][0],o[1]+Q[r][1]);T=624*n-104*m+195082
 cc=(8+2*n,q[1]);d=(cc[0],a[1]);initial={q,a,s,cc,d};B=set(initial);p=(0,0);h=0;word=[];last='';hits={}
 for t in range(cap):
  if p in initial and p not in hits:hits[p]=t
  p,h,ch=step(B,p,h);word.append(ch);last=(last+ch)[-312:]
  if t%400000==399999:print('progress',r,m,n,t+1,p,h,flush=True)
  if t>T+100000 and t%1664==1663 and last[-104:] in PHASES and last==last[-104:]*3:
   cert=certify_period(B,p,h,last[-104:])
   if cert:
    name=f'full_return_r{r}_m{m}_n{n}.txt.gz'
    with gzip.open(HERE/name,'wt') as f:f.write(''.join(word))
    return dict(r=r,m=m,n=n,postcore_time=t+1-T,capture=t+1,pose=[p,h],certificate=cert,word_file=name,hits=[(p,t) for p,t in hits.items()],initial=sorted(initial))
 return dict(r=r,m=m,n=n,status='cap',pose=[p,h],hits=[(p,t) for p,t in hits.items()])
if __name__=='__main__':
 rows=[]
 for r in (28,60,61,70,75):
  for m,n in [(100,400),(101,400),(100,401),(101,401)]:
   row=run(r,m,n);rows.append(row);print(json.dumps(row),flush=True)
   (HERE/'full_return_discovery.json').write_text(json.dumps(rows,indent=2)+'\n')
