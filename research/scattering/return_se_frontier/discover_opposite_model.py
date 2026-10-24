"""Discovery of the three compatible opposite-corner returns in the strip model."""
import sys,json,gzip
from pathlib import Path
R=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'continuation_2026-10-22/ant_continuation'))
sys.path.insert(0,str(R/'scattering/transverse'))
from ant_exact import W,P,D,plan,PHASES
import crossing as c
Q,_,_,_=plan(W,(0,0),2)
E={15:(64,59),45:(58,65),72:(36,65)}
NW=(-2,2);RAYS=[((d[0]-2,d[1]+2),NW,0,None) for d in D]+[((47-d[0],27-d[1]),NW,None,None) for d in D]
def run(r,k,cap=1500000):
 e=E[r];op=(e[0]+2*k,e[1]+2*k)
 f=c.Field(RAYS,set(P)^{Q[r],op});p=(0,0);h=2;word=[];last='';readset=set();first=None
 for t in range(cap):
  readset.add(p)
  if p==op and first is None:first=t
  p,h,ch=f.step(p,h);word.append(ch);last=(last+ch)[-312:]
  if first is not None and t>first+312 and (t-r)%104==0:
   w=last[-104:]
   if w in PHASES and last==w*3:
    cert=c.tail(f,p,h,w)
    if cert:
     name=f'opposite_r{r}_k{k}.txt.gz'
     with gzip.open(HERE/name,'wt') as out:out.write(''.join(word))
     return dict(r=r,k=k,status='exact infinite-model tail found',capture=t+1,pose=[p,h],tail_word=w,phase=PHASES[w],drift=cert['drift'],word_file=name,opposite_first_read=first,u_bounds=[min(x-y for x,y in readset),max(x-y for x,y in readset)],z_bounds=[min(x+y for x,y in readset),max(x+y for x,y in readset)])
 return dict(r=r,k=k,status='cap',time=cap,pose=[p,h],opposite_first_read=first,u_bounds=[min(x-y for x,y in readset),max(x-y for x,y in readset)])
if __name__=='__main__':
 rows=[]
 for r in (15,45,72):
  for k in (200,201,202):
   row=run(r,k);rows.append(row);print(json.dumps({k:v for k,v in row.items() if k!='tail_word'}),flush=True)
   (HERE/'opposite_model_discovery.json').write_text(json.dumps(rows,indent=2)+'\n')
