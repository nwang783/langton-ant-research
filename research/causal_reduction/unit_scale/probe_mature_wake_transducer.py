"""Prepared mature104 diagonal rail, one geometric cross-section of head poses.
This is a bi-infinite prepared profile probe, NOT a finite-seed construction.
Exact periodic verification permits a periodic background plus finite XOR.
"""
from pathlib import Path
import sys,json,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import multiplier
from certify_highway_wake_reflector import trace
W=set(map(tuple,json.loads((P/'shifted_reverse104_bulk.json').read_text())['wake_black_classes']))
D=((0,1),(1,0),(0,-1),(-1,0))
def base(p):return(p[0]-p[1],p[0]%2)in W

def exact(flip,p,h,w):
 rows,end,eh=trace(w,p,h);d=(end[0]-p[0],end[1]-p[1]);P=len(w)
 if eh!=h or d==(0,0):return 'invalid'
 qs=[q for q,_,_ in rows];ans=None
 for i,q in enumerate(qs):
  thresholds=[];tests={0,1}
  for j,qj in enumerate(qs):
   k=multiplier((qj[0]-q[0],qj[1]-q[1]),d)
   if k is not None and(k>0 or(k==0 and j<i)):
    thresholds.append(k);tests.update((k,k+1))
  for b in flip:
   k=multiplier((b[0]-q[0],b[1]-q[1]),d)
   if k is not None and k>=0:tests.update((k,k+1))
  nd=d[0]-d[1];z=q[0]-q[1]
  if nd:
   for zz,ee in W:
    if(zz-z)%nd:continue
    k=(zz-z)//nd
    if k>=0:tests.update((k,k+1))
  for k in sorted(tests):
   at=(q[0]+k*d[0],q[1]+k*d[1]);bit=base(at)^(at in flip)^(sum(t<=k for t in thresholds)%2)
   if bit!=(w[i]=='L'):
    tt=k*P+i;ans=tt if ans is None else min(ans,tt);break
 return ans

def run(z,e,h,limit=30000):
 p=(e,e-z);start=p;flip=set();word=[];check_after=1000;events=[]
 for t in range(limit):
  bit=base(p)^(p in flip);c='L'if bit else'R';word.append(c)
  if p in flip:flip.remove(p)
  else:flip.add(p)
  h=(h+(-1 if bit else 1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
  if t+1>=check_after and(t+1)%200==0:
   tail=''.join(word[-2400:])
   for per in range(2,min(400,len(tail)//6)+1,2):
    w=tail[-per:]
    if tail[-6*per:]!=w*6:continue
    rows,end,eh=trace(w,p,h);dr=(end[0]-p[0],end[1]-p[1])
    if eh!=h or dr==(0,0):continue
    bad=exact(flip,p,h,w)
    events.append(dict(time=t+1,period_length=per,word=w,drift=dr,bad=bad))
    if bad is None:
     return dict(start=[*start,h0],time=t+1,status='EXACT_PREPARED_PERIODIC_TAIL',pose=[*p,h],period=w,drift=dr,flip_count=len(flip),events=events)
    check_after=t+1+bad+1000;break
 return dict(start=[*start,h0],time=limit,status='UNKNOWN_HORIZON',pose=[*p,h],flip_count=len(flip),events=events)

if __name__=='__main__':
 st=time.monotonic();res=[]
 for z in range(-8,5):
  for e in range(2):
   for h0 in range(4):
    if(z+h0)%2!=1:continue
    row=run(z,e,h0);res.append(row);print(z,e,h0,row['status'],row['time'],row.get('drift'),flush=True)
    (P/'mature_wake_transducer_probe.json').write_text(json.dumps(dict(scope=__doc__,results=res,seconds=time.monotonic()-st),indent=2)+'\n')
 print('DONE',len(res),time.monotonic()-st)
