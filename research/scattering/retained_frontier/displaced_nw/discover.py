"""Candidate discovery only: fixed ordinary core followed by its forced NW a-hit."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation')
from ant_exact import step,certify_period,PHASES

BASE={70:(-22,30),75:(-21,30)}
AY={70:57,75:45}
def run(r,m,n,cap=2000000):
 x,y=BASE[r];seed={(x-2*m,y+2*m),(-33-2*n,-14-2*n),(-33-2*n,2*n+AY[r])}
 B=set(seed);p=(0,0);h=0;letters=[];contacts={};last=''
 for t in range(cap):
  if p in seed and p not in contacts:contacts[p]=t
  p,h,ch=step(B,p,h);letters.append(ch);last=(last+ch)[-312:]
  if t>1000 and t%104==103 and last[-104:] in PHASES and last==last[-104:]*3:
   cert=certify_period(B,p,h,last[-104:])
   if cert:
    with gzip.open(HERE/f'word_r{r}_m{m}_n{n}.txt.gz','wt') as f:f.write(''.join(letters))
    return dict(r=r,m=m,n=n,capture=t+1,pose=[p,h],certificate=cert,contacts=[(q,t) for q,t in contacts.items()],final_mass=len(B))
 return dict(r=r,m=m,n=n,status='cutoff',pose=[p,h],contacts=[(q,t) for q,t in contacts.items()],final_mass=len(B))
if __name__=='__main__':
 rows=[]
 for r in [70,75]:
  for m,n in [(100,200),(101,201),(100,201),(102,202),(100,300)]:
   row=run(r,m,n);rows.append(row);print(json.dumps(row),flush=True)
   (HERE/'discovery.json').write_text(json.dumps(rows,indent=2)+'\n')
