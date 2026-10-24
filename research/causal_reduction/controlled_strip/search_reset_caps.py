"""Search relative cycles of the ideal right-end reset system.
Any result is scoped to the reset system: omitted left turnarounds still need
an independent finite-arm/port construction. Bounds are UNKNOWN, not exclusion.
"""
import json,random,time,pathlib,sys,collections
HERE=pathlib.Path(__file__).resolve().parent
ns={'__file__':str(HERE/'reset_endpoint_probe.py')};exec((HERE/'reset_endpoint_probe.py').read_text().split('# Base is')[0],ns)
TPL=ns['TPL'];DIRE=ns['DIRE'];rng=random.Random(20261022)

def run(up,seed,stepcap=20000):
 rows0={0,up};diff=set(seed);x=y=0;h=1;seen={};events=[];path=[]
 def color(p):return (p[0]<0 and p[1]in rows0)^(p in diff)
 def flip(p):
  if p in diff:diff.remove(p)
  else:diff.add(p)
 def match():
  t=TPL[h];rows={y+b for b in t['rows']}
  if rows0.intersection(rows)!={y}:return False
  if any(color((x+a,y+b))!=v for(a,b),v in t['guard'].items()):return False
  cut=x-12
  if any(p[0]<cut and p[1]in rows and color(p)!=(p[1]==y)for p in diff):return False
  if cut>0 and any(not color((a,y))for a in range(cut)):return False
  return True
 def key():
  z=set(diff)
  for a in range(min(0,x),max(0,x)):
   for yy in rows0:
    p=a,yy
    if p in z:z.remove(p)
    else:z.add(p)
  return y,h,tuple(sorted((a-x,b)for a,b in z))
 for t in range(stepcap):
  if y in rows0 and h in TPL and match():
   z=key()
   if z in seen:
    old=seen[z];return dict(status='CYCLE',drift=x-old[1],from_event=old[0],to_event=len(events),from_path=old[2],to_path=len(path),events=events,path=path,final_pose=[x,y,h],seed=sorted(seed),upper=up,final_diff=sorted(diff))
   seen[z]=(len(events),x,len(path));events.append([x,y,h,len(path)])
   q=TPL[h];path.append(['RESET',x,y,h]);
   for a,b in q['flip']:flip((x+a,y+b))
   x+=q['offset'];h=(h+2)%4
  else:
   p=x,y;b=color(p);path.append('L'if b else'R');flip(p);h=(h+(-1 if b else 1))%4;dx,dy=DIRE[h];x+=dx;y+=dy
  if y<-10 or y>up+12 or abs(x)>160 or len(diff)>1200 or len(events)>300:
   return dict(status='BOUND',resets=len(events),steps=t,pose=[x,y,h],mass_defect=len(diff))
 return dict(status='STEP_CAP',resets=len(events),steps=stepcap)

def seedmake(up,n):
 d=set();rows={0,up}
 def c(p):return(p[0]<0 and p[1]in rows)^(p in d)
 # Adjacent equal-color pairs preserve signed column charge exactly.
 for _ in range(n):
  for attempt in range(100):
   x=rng.randrange(-5,6);y=rng.randrange(-2,up+3);a=x,y;b=x,y+1
   if c(a)==c(b):
    for p in(a,b):
     if p in d:d.remove(p)
     else:d.add(p)
    break
 return d
count=int(sys.argv[1])if len(sys.argv)>1 else 2000;results=[];tot=collections.Counter();start=time.time();best=[]
for i in range(count):
 up=(4,6,8,10)[i%4];seed=seedmake(up,1+(i//4)%16);r=run(up,seed);tot[r['status']]+=1
 if r['status']=='CYCLE':
  results.append(r);print('CYCLE',i,up,r['drift'],r['to_event']-r['from_event'],flush=True)
  if r['drift']>0:break
 else:
  rec=(r['resets'],r['steps'],i,up,sorted(seed),r)
  best.append(rec);best=sorted(best,reverse=True)[:12]
 if i%100==0:print('progress',i,dict(tot),'best',best[0][:4]if best else None,flush=True)
out=dict(trials=i+1,counts=dict(tot),cycles=results,best=best,seconds=time.time()-start)
(HERE/'random_reset_caps.json').write_text(json.dumps(out));print('DONE',out['trials'],dict(tot),out['seconds'],flush=True)
