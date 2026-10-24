from probe_stitched_continuation import *
from return_guide_geometry import cells_of,xy,endpoints,connected,component
from collections import deque
import heapq
uv=lambda v:((v[0]+v[1]-2)//4,(v[0]-v[1])//4)
DIR4=((1,0),(0,1),(-1,0),(0,-1))
def cell(u,v):return next(iter(cells_of([u,v])))
def add(u,v):return(u[0]+v[0],u[1]+v[1])
def joins(A,k):
 g={}
 for e in A:
  u,v=endpoints(e,k);g.setdefault(u,[]).append(v);g.setdefault(v,[]).append(u)
 tips=[uv(u)for u in g if len(g[u])==1];J=set()
 for u in tips:
  for v in tips:
   if abs(u[0]-v[0])+abs(u[1]-v[1])==1:
    e=cell(u,v)
    if e not in A:J.add(e)
 return J

def get_history(z):
 B=set(map(tuple,z['initial']));p,h=tuple(z['entry'][0]),z['entry'][1];hist={}
 for t,c in enumerate(''.join(z['words'])):
  hist.setdefault(p,[]).append((t,c));p,h=step(B,p,h)
 return hist

def synth(q):
 B,p,h,z=final(q);k=wwhich(p,h);A={tuple(x)for x,s in z['labels']if s=='second'};J=joins(A,k);hist=get_history(z)
 assert not(J&set(hist));base=B|J
 root=uv(cursors(p,h)[1]);sg=1 if q%4==1 else -1
 cyclevs=[add(root,(sg*x,sg*y)) for x,y in [(0,0),(0,-1),(1,-1),(1,0),(0,0)]]
 cycle=set(cell(u,v)for u,v in zip(cyclevs,cyclevs[1:]))
 assert not(cycle&(set(hist)|base))
 entrybase=base|cycle
 p1,h1=p,h;startbase=set(entrybase)
 for c in 'RL':
  assert c==('L'if p1 in startbase else'R')
  p1,h1=step(startbase,p1,h1)
 start=uv(cursors(p1,h1)[1]);prev=(start[0]-root[0],start[1]-root[1]);a0=DIR4.index(prev)
 base=startbase
 target=(0,-2);enddir=3
 lo=min(min(u)for e in base for u in map(uv,endpoints(e,k)))-10;hi=max(max(u)for e in base for u in map(uv,endpoints(e,k)))+10
 heap=[(0,(start,a0))];dist={(start,a0):0};par={};goal=None
 while heap:
  cost,(u,a)=heapq.heappop(heap)
  if cost!=dist[u,a]:continue
  if u==target and a==enddir:goal=(u,a);break
  for turn in(-1,0,1):
   b=(a+turn)%4;v=add(u,DIR4[b])
   if not(lo<=v[0]<=hi and lo<=v[1]<=hi)or v==root or v==(1,-2):continue
   e=cell(u,v)
   if (e in hist and e not in base)or e in A|J:continue
   r=1+turn
   arms=[cell(u,add(u,DIR4[(a-1+j)%4]))for j in range(r)]
   if any(e in base for e in arms):continue
   nc=cost+1+r*.001
   if nc<dist.get((v,b),float('inf')):dist[v,b]=nc;par[v,b]=(u,a);heapq.heappush(heap,(nc,(v,b)))
 if goal is None:print('NO STATIC ROUTE',q,'states',len(dist),'start',start,'range',min(v[0]for v,a in dist),max(v[0]for v,a in dist),min(v[1]for v,a in dist),max(v[1]for v,a in dist),'targets',[(v,a)for v,a in dist if abs(v[0]-target[0])+abs(v[1]-target[1])<3]);return
 states=[goal]
 while states[-1]!=(start,a0):states.append(par[states[-1]])
 states.reverse();K=[s[0]for s in states]+[(1,-2)];guide=set(cell(u,v)for u,v in zip(K,K[1:]));guide-=base;assert not(guide&(set(hist)|base))
 extras=guide|J|cycle;bb=set(map(tuple,z['initial']))|extras;pp,hh=tuple(z['entry'][0]),z['entry'][1]
 for t,c in enumerate(''.join(z['words'])):
  assert c==('L'if pp in bb else'R'),('prefix changed',q,t)
  pp,hh=step(bb,pp,hh)
 assert(bb,pp,hh)==(entrybase|guide,p,h)
 first_r=1+(prev[0]*(K[1][1]-K[0][1])-prev[1]*(K[1][0]-K[0][0]))
 ret='RL'+path_word(K,first_r);bad=None
 for t,c in enumerate(ret):
  actual='L'if pp in bb else'R'
  if c!=actual:bad=(t,pp,c,actual);break
  pp,hh=step(bb,pp,hh)
 print(dict(q=q,static_path_edges=len(K)-1,simple=len(K)==len(set(K)),extra=len(extras),return_word_length=len(ret),bad=bad,pose=[pp,hh],expected_target=[(-1,4),0]),flush=True)
 out=dict(q=q,K=K,extra=sorted(extras),guide=sorted(guide),stitches=sorted(J),return_word=ret,bad=bad,arrival_pose=[pp,hh])
 if bad is None:
  assert(pp,hh)==((-1,4),0)
  assert A<=bb
  vs=ordered_path(A|J,k,xy((1,-2)));ww=path_word(list(map(uv,vs)),2)
  d=[];r=0;ordinary=True
  for t,c in enumerate(ww):
   actual='L'if pp in bb else'R'
   if c!=actual:bad=(t,pp,c,actual);break
   if c=='L':
    ordinary &= r<=2 and not connected(bb-{pp},k,*endpoints(pp,k));d.append(pp);r=0
   else:r+=1
   pp,hh=step(bb,pp,hh)
  out.update(third_word=ww,third_bad=bad,third_ordinary=ordinary,third_gain=ww.count('R')-ww.count('L'),all_second_consumed=A<=set(d),final=sorted(bb),final_pose=[pp,hh])
  print(dict(q=q,third_bad=bad,ordinary=ordinary,gain=out['third_gain'],all_second_consumed=out['all_second_consumed']),flush=True)
 (OUT/f'third_return_synthesis_v5_q{q}.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':
 for q in(3,5,7):synth(q)
