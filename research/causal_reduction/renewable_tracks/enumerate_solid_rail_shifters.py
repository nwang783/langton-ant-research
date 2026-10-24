"""Exact periodic-background solid-line shifter synthesis, all bounded words.
No finite-seed claim: the input rail is infinite. A shifter has one solid input
row, one solid output row, and white elsewhere before and after passage.
"""
from search_spiral_caps import *
from collections import defaultdict,Counter
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'front_surgery'))
from search_reverse_rail_fronts import necklaces

def classify(w):
 if w.count('R')!=w.count('L'):return None
 ev,en=walk(w);x,y,h=en
 if h or (x==0)==(y==0):return None
 p=abs(x+y)
 for h in range(4):
  ev,en=walk(w,(0,0,h))
  if en[:2]==(-p,0):break
 groups=defaultdict(list)
 for i,((x,y),hh,c) in enumerate(ev):groups[(x%p,y)].append((-(x//(-p)),i,c))
 start=set();finish=set()
 for cl,g in groups.items():
  g.sort();cs=[c for a,i,c in g]
  if any(cs[j]==cs[j-1] for j in range(1,len(cs))):return None
  if cs[0]=='L':start.add(cl)
  if cs[-1]=='R':finish.add(cl)
 if len(start)!=p or len(finish)!=p:return None
 ys={y for x,y in start};yt={y for x,y in finish}
 if len(ys)!=1 or len(yt)!=1:return None
 src=next(iter(ys));dst=next(iter(yt))
 if src==dst:return None
 assert start=={(x,src) for x in range(p)} and finish=={(x,dst) for x in range(p)}
 return dict(word=w,period=len(w),drift=[-p,0],initial_pose=[0,-src,h],input_row=0,output_row=dst-src)

if __name__=='__main__':
 hi=int(sys.argv[1]) if len(sys.argv)>1 else 24;out=[];start=time.time()
 assert classify('LLRLRRRRLRRRRLLLLRLL')['output_row']==3
 for n in range(2,hi+1,2):
  cnt=0;sol=[]
  for w in necklaces(n):
   cnt+=1;r=classify(w)
   if r is not None:sol.append(r);print('SHIFTER',json.dumps(r),flush=True)
  out.append(dict(length=n,necklaces=cnt,shifters=sol));print('LENGTH',n,len(sol),time.time()-start,flush=True)
  (HERE/f'solid_rail_shifters_{hi}.json').write_text(json.dumps(dict(results=out,seconds=time.time()-start),indent=2))
