"""Discover controlled builders with a fixed nearest-row feedback policy.
No finite survival is an infinite certificate.
"""
import sys,json,time,random,pathlib
HERE=pathlib.Path(__file__).resolve().parent

def play(H,policy,entry,cap=20000):
 B=0;mx=0;steps=0;ports=[];exits=[];seen=set()
 for ep in range(cap):
  ports.append(entry);x=0;y=entry;dx=1
  while x>=0:
   i=x*H+y;a=1-2*(B>>i&1);B^=1<<i;z=y-dx*a;steps+=1
   if z<0 or z>=H:return dict(H=H,policy=policy,start=ports[0],excursions=ep+1,max_x=mx,status='VERTICAL',steps=steps)
   i=x*H+z;b=1-2*(B>>i&1);B^=1<<i;dx=-dx*a*b;y=z;x+=dx;steps+=1;mx=max(mx,x)
   if steps>10000000 or x>=1000:return dict(H=H,policy=policy,start=ports[0],excursions=ep+1,max_x=mx,status='UNKNOWN',ports=ports,board_hex=hex(B),steps=steps)
  if B in seen:raise AssertionError('finite-field controlled loop')
  seen.add(B);exits.append(y);entry=y+1 if y==0 or policy>>(y//2)&1 else y-1
 return dict(H=H,policy=policy,start=ports[0],excursions=cap,max_x=mx,status='SURVIVAL_CAP',ports=ports,exits=exits,board_hex=hex(B),steps=steps)
if __name__=='__main__':
 rng=random.Random(314159);res=[];best=0;t0=time.time()
 for H in(12,16,24,32,64):
  policies=list(range(1<<(H//2)))if H<=16 else[0,(1<<(H//2))-1]+[rng.getrandbits(H//2)for _ in range(2000)]
  for policy in policies:
   r=play(H,policy,1+2*((H//2)//2));res.append(r)
   if r['excursions']>best:best=r['excursions'];print('BEST',best,r['max_x'],H,policy,r['status'],flush=True)
   if r['status']!='VERTICAL':print('CANDIDATE',r,flush=True)
 out=dict(results=res,seconds=time.time()-t0);(HERE/'feedback_ports.json').write_text(json.dumps(out,indent=2));print('DONE',len(res),time.time()-t0,flush=True)
