"""Literal full five-cell controls for compatible opposite-corner continuations."""
import sys,json,gzip
from pathlib import Path
R=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,plan,step,PHASES,certify_period
Q,_,_,_=plan(W,(0,0),2);E={15:(64,59),45:(58,65),72:(36,65)};OFF={15:10,45:13,72:13}
def run(r,m,k,cap=1500000):
 n=m+k+OFF[r];o=(-62-2*m,2+2*m);q=(-33-2*n,-14-2*n);a=(-33-2*n,41+2*n);s=(o[0]+Q[r][0],o[1]+Q[r][1]);e=E[r];d=(o[0]+e[0]+2*k,o[1]+e[1]+2*k);cc=(d[0],q[1]);assert d[1]==a[1]
 initial={q,a,s,cc,d};B=set(initial);p=(0,0);h=0;word=[];last='';hits={}
 for t in range(cap):
  if p in initial and p not in hits:hits[p]=t
  p,h,ch=step(B,p,h);word.append(ch);last=(last+ch)[-312:]
  if t%200000==199999:print('progress',r,m,k,t+1,p,h,flush=True)
  if t>416*n-104*m+122376+100000 and t%1664==1663 and last[-104:] in PHASES and last==last[-104:]*3:
   cert=certify_period(B,p,h,last[-104:])
   if cert:
    name=f'full_opposite_r{r}_m{m}_k{k}.txt.gz'
    with gzip.open(HERE/name,'wt') as f:f.write(''.join(word))
    return dict(r=r,m=m,k=k,n=n,capture=t+1,pose=[p,h],certificate=cert,word_file=name,hits=[(p,t) for p,t in hits.items()],initial=sorted(initial))
 return dict(r=r,m=m,k=k,status='cap',pose=[p,h],hits=[(p,t) for p,t in hits.items()])
if __name__=='__main__':
 rows=[]
 for r in (15,45,72):
  for m,k in [(100,200),(101,200),(100,201),(101,201)]:
   row=run(r,m,k);rows.append(row);print(json.dumps(row),flush=True)
   (HERE/'full_opposite_discovery.json').write_text(json.dumps(rows,indent=2)+'\n')
