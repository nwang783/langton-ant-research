"""Discovery only for the three NE-output rays and their phase72 opposite corner."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation')
from ant_exact import step,certify_period,PHASES
B={29:(-16,33),56:(-21,33),62:(-22,32)}
E={29:(2,57),56:(4,59),62:(2,45)}
def seed(r,m,n,k,full):
 bx,by=B[r];ex,ey=E[r];s=(bx-2*m,by+2*m);q=(-33-2*n,-14-2*n);d=(ex-2*m+2*k,ey+2*m+2*k)
 return {q,s,d}|({(q[0],d[1]),(d[0],q[1])} if full else set())
def run(r,m,n,k,full,cap=3000000):
 initial=seed(r,m,n,k,full);field=set(initial);p=(0,0);h=0;word=[];last='';contacts={}
 for t in range(cap):
  if p in initial and p not in contacts:contacts[p]=t
  p,h,ch=step(field,p,h);word.append(ch);last=(last+ch)[-312:]
  if t>1000 and t%104==103 and last[-104:] in PHASES and last==last[-104:]*3:
   cert=certify_period(field,p,h,last[-104:])
   if cert:
    with gzip.open(HERE/f'word_r{r}_m{m}_n{n}_k{k}_full{int(full)}.txt.gz','wt') as f:f.write(''.join(word))
    return dict(r=r,m=m,n=n,k=k,full=full,capture=t+1,pose=[p,h],certificate=cert,contacts=[(q,t) for q,t in contacts.items()],final_mass=len(field))
 return dict(r=r,m=m,n=n,k=k,full=full,status='cutoff',pose=[p,h],contacts=[(q,t) for q,t in contacts.items()])
if __name__=='__main__':
 rows=[]
 for r in (29,56,62):
  for m,n,k,full in [(100,200,200,False),(100,200,200,True),(101,201,201,True),(100,201,200,True),(100,200,201,True)]:
   row=run(r,m,n,k,full);rows.append(row);print(json.dumps(row),flush=True)
   (HERE/'discovery.json').write_text(json.dumps(rows,indent=2)+'\n')
