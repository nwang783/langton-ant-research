"""Discovery only: a retained bit on the SE return, beside the older NW rail.
No finite-seed theorem follows from an infinite-background output alone.
"""
import sys,json,gzip
from pathlib import Path
R=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'continuation_2026-10-22/ant_continuation'))
sys.path.insert(0,str(R/'scattering/transverse'))
from ant_exact import P,D,W,DRIFT,plan,canonical_source,PHASES
import crossing as c
F=json.loads((R/'scattering/retained_frontier/ordinary_interfaces.json').read_text())
PHASE_LIST=sorted([v['phase'] for v in F['rows']]+[72])
QS,_,_,_=plan(W,(0,0),2)
OFFSET=(47,27);NW=(-2,2)
OLD=[((OFFSET[0]-d[0],OFFSET[1]-d[1]),NW,None,None) for d in D]

def run(r,mature,cap=600000):
 if mature:
  rays=OLD+[((d[0]-DRIFT[0],d[1]-DRIFT[1]),NW,0,None) for d in D]
  B=set(P)
 else:rays=OLD;B=canonical_source(100,0)[0]
 B.symmetric_difference_update({QS[r]})
 f=c.Field(rays,B);p=(0,0);h=2;word=[];last='';reads=set();contacts=[]
 for t in range(cap):
  reads.add(p)
  if t<r:assert f.color(p)==(W[t]=='L')
  if t==r:assert f.color(p)!=(W[t]=='L')
  if any(c.multiple(c.minus(p,b),d) is not None for b,d,_,_ in OLD):
   if len(contacts)<5:contacts.append((t,p))
  p,h,ch=f.step(p,h);word.append(ch);last=(last+ch)[-312:]
  if t>r+312 and (t-r)%104==0:
   w=last[-104:]
   if w in PHASES and last==w*3:
    cert=c.tail(f,p,h,w)
    if cert:
     name=f'word_r{r}_mature{int(mature)}.txt.gz'
     with gzip.open(HERE/name,'wt') as out:out.write(''.join(word))
     return dict(r=r,mature=mature,status='exact infinite-background tail found',capture=t+1,pose=[p,h],tail_word=w,phase=PHASES[w],drift=cert['drift'],word_file=name,first_old_rail_contacts=contacts,u_bounds=[min(x-y for x,y in reads),max(x-y for x,y in reads)],z_bounds=[min(x+y for x,y in reads),max(x+y for x,y in reads)],flips=len(f.changes))
 return dict(r=r,mature=mature,status='cap',time=cap,pose=[p,h],first_old_rail_contacts=contacts)
if __name__=='__main__':
 rows=[]
 for mature in (False,True):
  for r in PHASE_LIST:
   row=run(r,mature);rows.append(row);print(json.dumps({k:v for k,v in row.items() if k!='tail_word'}),flush=True)
   (HERE/'parallel_model_discovery.json').write_text(json.dumps(rows,indent=2)+'\n')
