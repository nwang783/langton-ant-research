"""Test long structured periodic port sequences, without an infinite inference."""
import sys,json,time,pathlib
HERE=pathlib.Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))
def run(H,w,cap=10000):
 B=0;mx=0;steps=0;exits=[];snapshots=[]
 for j in range(cap):
  x=0;y=w[j%len(w)];dx=1
  while x>=0:
   i=x*H+y;a=1-2*((B>>i)&1);B^=1<<i;z=y-dx*a;steps+=1
   if z<0 or z>=H:return dict(H=H,ports=w,excursions=j+1,max_x=mx,status='VERTICAL',exit_y=z,steps=steps)
   i=x*H+z;b=1-2*((B>>i)&1);B^=1<<i;dx=-dx*a*b;y=z;x+=dx;steps+=1;mx=max(mx,x)
   if x>=1000 or steps>=10000000:return dict(H=H,ports=w,excursions=j+1,max_x=mx,status='UNKNOWN',board_hex=hex(B),steps=steps)
  exits.append(y)
  if (j+1)%len(w)==0 and len(snapshots)<20:snapshots.append(hex(B))
 return dict(H=H,ports=w,excursions=cap,max_x=mx,status='SURVIVAL_CAP',board_hex=hex(B),exit_rows=exits,snapshots=snapshots,steps=steps)
t0=time.time();out=[];best=0
for H in(32,64,128):
 for k in range(2,17):
  low=H//2-k
  if low%2==0:low+=1
  a=list(range(low,low+2*k,2));b=a[::-1]
  patterns=[a,b,a+b,b+a,a+b[1:-1],b+a[1:-1],[x for x in a for _ in range(2)],[x for x in b for _ in range(2)],a[::2]+a[1::2],a[1::2]+a[::2]]
  for w in patterns:
   r=run(H,w);out.append(r)
   if r['excursions']>best:best=r['excursions'];print('BEST',best,r['max_x'],H,w,r['status'],flush=True)
   if r['status']!='VERTICAL':print('CANDIDATE',r,flush=True)
(HERE/'structured_controllers.json').write_text(json.dumps(dict(results=out,seconds=time.time()-t0),indent=2));print('DONE',len(out),time.time()-t0,flush=True)
