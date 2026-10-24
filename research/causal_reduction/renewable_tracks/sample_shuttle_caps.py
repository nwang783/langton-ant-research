"""Candidate discovery from actual finite-seed trajectories, then exact caps.
A sampled failure is never a cap nonexistence theorem.
"""
from mixed_shuttle_caps import *
import random

def fast_test(w,side):
 cap,en=walk(w,(0,0,1));assert en==((0,4,1) if side=='left' else (0,0,1))
 I,O=(WE,SE) if side=='left' else (SE,WE);step=2 if side=='left' else -2;OY=4 if side=='left' else 0
 xs=[p[0] for p,h,c in cap]+[p[0]+step for p,h,c in I]+[p[0] for p,h,c in O]
 lo=min(xs)-4;hi=max(xs)+4;groups=defaultdict(list)
 for i,((x,y),h,c) in enumerate(cap):groups[x,y%4].append((-y,0,i,c))
 for x in range(lo,hi+1):
  for i,((a,b),h,c) in enumerate(I):
   z=x-a
   if z%step==0 and z//step>=1:
    k=z//step;groups[x,b%4].append((-b,-1,-len(I)*k+i,c))
  for i,((a,b),h,c) in enumerate(O):
   z=x-a
   if z%step==0 and z//step>=0:
    k=z//step;B=b+OY;groups[x,B%4].append((-B,1,len(O)*k+i,c))
 for cl,g in groups.items():
  g.sort();prev='L'
  for a,b,c,z in g:
   if z==prev:return False
   prev=z
 return True

if __name__=='__main__':
 seeds=int(sys.argv[1]) if len(sys.argv)>1 else 40;steps=int(sys.argv[2]) if len(sys.argv)>2 else 50000
 rng=random.Random(902391);seen={'left':set(),'right':set()};sol=[];t0=time.time();D=((0,1),(1,0),(0,-1),(-1,0));maxlen=2048
 for seedid in range(seeds):
  board={(x,y) for x in range(-8,9) for y in range(-8,9) if rng.random()<.25} if seedid else set()
  x=y=h=0;poses=defaultdict(list);poses[x,y,h]=[0];trace=[];charge=[0]
  for t in range(steps):
   p=x,y;c='L' if p in board else 'R';board.symmetric_difference_update({p});trace.append(c);charge.append(charge[-1]+(1 if c=='R' else -1));h=(h+(1 if c=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy;now=t+1
   for side in ['right','left']:
    if side=='right':key=x,y,h;delta=8
    else:
     dx,dy=D[(h-1)%4];key=x-4*dx,y-4*dy,h;delta=4
    for start in poses.get(key,[]):
     if now-start>maxlen or charge[now]-charge[start]<delta:continue
     w=''.join(trace[start:now])
     if w in seen[side]:continue
     seen[side].add(w)
     if fast_test(w,side):
      r=test(w,side);assert not r['bad_count'];sol.append(dict(seedid=seedid,start=start,stop=now,side=side,certificate=r));print('CANDIDATE',json.dumps(sol[-1]),flush=True)
   key=x,y,h;poses[key].append(now);poses[key]=poses[key][-8:]
  print('SEED',seedid,'tested',{k:len(v) for k,v in seen.items()},'solutions',len(sol),'seconds',time.time()-t0,flush=True)
 out=dict(seeds=seeds,steps=steps,maxlen=maxlen,retained_pose_times=8,counts={k:len(v) for k,v in seen.items()},candidates=sol,seconds=time.time()-t0)
 (HERE/f'sampled_caps_{seeds}_{steps}.json').write_text(json.dumps(out,indent=2))
 (HERE/f'sampled_caps_{seeds}_{steps}_words.json').write_text(json.dumps({k:sorted(v,key=lambda w:(len(w),w)) for k,v in seen.items()},indent=2))
