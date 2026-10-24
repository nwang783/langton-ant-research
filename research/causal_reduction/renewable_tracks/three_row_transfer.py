"""Exact candidate transfer with cap reads in[-1,5]. Random orbit discovery only.
Input A/B on nonnegative rows-1/0; arbitrary finite C on row1.
Output rows3/4(nonnegative) and5(all x). No cycle is inferred from finite runs.
"""
from two_row_transfer import *
import random

def step(state,budget=10000):
 ab,C=state;D={(x,1)for x in C};M=(ab.bit_length()+1)//2
 for x in range(M):
  if ab>>(2*x)&1:D.add((x,-1))
  if ab>>(2*x+1)&1:D.add((x,0))
 x=y=0;h=1;w=[]
 for t in range(budget):
  c=((y==0 and x<0)^((x,y)in D));w.append('L'if c else'R');D.symmetric_difference_update({(x,y)});h=(h+(-1 if c else 1))%4;dx,dy=((0,1),(1,0),(0,-1),(-1,0))[h];x+=dx;y+=dy
  if y<-1 or y>5:return None,'HEIGHT_EXIT',None
  if (x,y,h)==(0,0,1):
   reg=lambda a,b:(b==0 and(a<=-2 or a==0))or(b==1 and a<=0)or(b in(2,3)and a<=-1)
   if {p for p in D if reg(*p)}=={(0,0),(0,1),(-1,2)} and not any(b==4 and a<0 for a,b in D):
    outab=sum(1<<(2*a+b-3)for a,b in D if a>=0 and b in(3,4));outC=tuple(sorted(a for a,b in D if b==5));return (outab,outC),'TRANSFER',''.join(w)
  if y==0 and h==0 and x<=-2 and not any((b==0 and a<=x)or(b==-1 and a<=x-1)for a,b in D):return None,'S_ESCAPE',None
  if y==0 and h==1 and x<=-2:
   reg=lambda a,b:(b==0 and(a<=x-2 or a==x))or(b==1 and a<=x)or(b in(2,3)and a<=x-1)
   if {p for p in D if reg(*p)}=={(x,1),(x-1,2)}:return None,'W_ESCAPE',None
 return None,'UNKNOWN',None
if __name__=='__main__':
 N=int(sys.argv[1])if len(sys.argv)>1 else 20000;rng=random.Random(271828);cache={};counts=Counter();best=[];cycles=[];t0=time.time();maxdepth=0
 for i in range(N):
  state=(rng.getrandbits(20)|2,tuple(x for x in range(-4,10)if rng.random()<.3));seen={};chain=[]
  for depth in range(100):
   if state in seen:
    cycles.append(dict(initial=chain[0]if chain else state,states=chain[seen[state]:],period=depth-seen[state]));break
   seen[state]=depth;chain.append(state)
   if state not in cache:
    cache[state]=step(state);counts[cache[state][1]]+=1
   nxt,st,w=cache[state]
   if nxt is None:break
   state=nxt
  if len(chain)>maxdepth:maxdepth=len(chain);best=chain;print('DEPTH',maxdepth,'sample',i,'status',st,flush=True)
  if cycles:break
  if i and i%5000==0:print('INPUTS',i,'states',len(cache),'seconds',time.time()-t0,flush=True)
 out=dict(samples=i+1,states=len(cache),counts=dict(counts),max_chain=maxdepth,best_chain=best,cycles=cycles,seconds=time.time()-t0)
 (HERE/'three_row_random_orbits.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
