"""Necessary white-corner chronology for an outward rail-shift corner.
Incoming north S arm, cap K (heading east), outgoing east S arm. Successive
laps translate the corner (-1,+1). Complete classes in a central diagonal
band see the exact infinite-arm event set; truncated arm ends are discarded.
"""
from collections import defaultdict
from search_spiral_caps import *

def corner_check(K,M=None):
 M=M or max(10,len(K)*2)
 ev,end=walk(S*M+K+S*M,(0,-2*M,0));groups=defaultdict(list)
 for i,((x,y),h,c) in enumerate(ev):
  s=x+y
  if -M<=s<=M:groups[s].append((x,i,c,(x,y))) # rank=-x, descending rank -> x ascending
 bad=[];odd=[]
 for cl,g in groups.items():
  g.sort()
  if any(c!=('R' if j%2==0 else 'L') for j,(_,i,c,p) in enumerate(g)):bad.append((cl,''.join(c for x,i,c,p in g)))
  if len(g)%2:odd.append(cl)
 return dict(valid=not bad,bad=bad,odd_classes=odd)

if __name__=='__main__':
 maxlen=int(sys.argv[1]) if len(sys.argv)>1 else 17;out=[];tested=0;start=time.time()
 for K,end in words(maxlen,heading=1):
  tested+=1;r=corner_check(K)
  if r['valid']:
   rec=dict(word=K,end=end,check=r);out.append(rec);print('CORNER',json.dumps(rec),flush=True)
 print('DONE',tested,len(out),time.time()-start,flush=True)
 (HERE/f'corner_chronology_{maxlen}.json').write_text(json.dumps(dict(maxlen=maxlen,tested=tested,valid=out,seconds=time.time()-start),indent=2))
