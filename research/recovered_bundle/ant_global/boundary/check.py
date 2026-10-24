from collections import Counter,defaultdict
DIR=[(1,0),(0,-1),(-1,0),(0,1)] # E,S,W,N
def run(seed,head=(0,-4),d=2,steps=24):
 b=set(seed); ev=[]; x,y=head
 for t in range(steps):
  c=(x,y) in b; e=(d+(-1 if c else 1))%4
  ev.append((t,x,y,d,int(c),e))
  if c:b.remove((x,y))
  else:b.add((x,y))
  dx,dy=DIR[e];x+=dx;y+=dy;d=e
 return ev,b,(x,y,d)
if __name__=='__main__':
 ev,b,end=run({(1,-3)})
 print('end',end)
 for e in ev: print(e)
 for lev in range(0,-4,-1):
  ee=[e for e in ev if e[1]+e[2]==lev]
  print(lev,len(ee),sum(1-2*e[4] for e in ee))
