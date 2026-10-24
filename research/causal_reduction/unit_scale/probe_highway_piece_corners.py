"""Discovery only: exact two-phase S-corner histories using cyclic subwords of the signed104.
No arbitrary word-length escalation; no whole-device claim from a local survivor.
"""
import sys,json,time,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'renewable_tracks'))
from periodic_corner_states import check_sequence,walk,feasible,S
from collections import defaultdict,Counter
H=json.loads(Path('/workspace/shared/langton/recovered_bundle/ant_global/root/standard.json').read_text())['word']
assert len(H)==104
start=time.time();byword={}
for phase in range(104):
 w=(H+H)[phase:phase+104]
 for n in range(1,105):
  K=w[:n]
  if (K.count('R')-K.count('L'))%4==1:
   byword.setdefault(K,[]).append((phase,n))
byend=defaultdict(list);failed=Counter();single=[]
for K,origins in byword.items():
 ev,end=walk(K)
 # Full finite arm overlap check; this horizon exceeds every cap coordinate.
 m=max([abs(x)+abs(y) for (x,y),h,c in ev]+[0])+3
 if feasible(S*m+K+S*m):
  byend[end].append(K)
  ans=check_sequence([K])
  if ans['valid']:single.append(dict(word=K,origins=origins,answer=ans))
 else:failed['one_lap_conflict']+=1
pairs=0;good=[];best=999;near=[]
for end,ks in byend.items():
 for i,K in enumerate(ks):
  for J in ks[i:]:
   pairs+=1;z=check_sequence([K,J]);b=len(z['bad'])
   if b<best:best=b;near=[]
   if b==best and len(near)<30:near.append(dict(words=[K,J],end=end,bad=z['bad'],odd=z['odd_classes']))
   if z['valid']:good.append(dict(words=[K,J],origins=[byword[K],byword[J]],end=end,answer=z))
out=dict(scope=__doc__,source104_sha256=hashlib.sha256(H.encode()).hexdigest(),distinct_subwords=len(byword),one_lap_feasible=sum(map(len,byend.values())),endpoints=len(byend),same_endpoint_pairs=pairs,fixed_survivors=single,two_phase_survivors=good,failures=failed,best_bad_count=best,near=near,seconds=time.time()-start)
P.joinpath('highway_piece_corners.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('near',)},indent=2))
