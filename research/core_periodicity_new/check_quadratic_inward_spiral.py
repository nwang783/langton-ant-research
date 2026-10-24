"""Exact finite controls for the all-n inward-spiral proof."""
from collections import Counter
import hashlib,json
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0));S='RLLR'
raw=json.loads((Path(__file__).parent.parent/'recovered_bundle/ant_global/root/standard.json').read_text())
W=raw['word'];digest=hashlib.sha256(W.encode()).hexdigest()
assert digest=='9772fa0cced75fab3a1d336c6a1326e0e4be8f4e471a3807e0778fccc94c1f04'
F={(W+W)[i:i+10] for i in range(104)};assert len(F)==84
Sf={ (S*4)[i:i+10] for i in range(4)};assert Sf.isdisjoint(F)
def circuit_reads(n,k):
 T=2*n-k;out={}
 def put(p,a):assert p not in out;out[p]=a
 for y in range(k,T):put((-k,y),'R');put((1-k,y),'L')
 put((-k,T),'L')
 for x in range(-2*n+k,-k):put((x,T),'R');put((x,T+1),'L')
 B=(-2*n+k-1,T);put(B,'R');put((B[0],B[1]+1),'L');put((B[0]-1,B[1]+1),'L')
 for y in range(k+1,T+1):put((-2*n+k-2,y),'R');put((-2*n+k-3,y),'L')
 put((-2*n+k-2,k),'L')
 for x in range(-2*n+k-1,-k-1):put((x,k),'R');put((x,k-1),'L')
 put((-k-1,k),'L');return out
CAP={(1,-1),(1,0),(-1,1),(0,1),(-3,0),(-3,1),(-2,-1),(-1,-1),(-2,1)}
def final_profile(n):
 B=set(CAP)
 for j in range(2,n+1):B.update({(j,-j),(j,j-1),(j-1,j),(-j-2,1-j),(-j-2,j),(-j-1,-j),(j-2,-j)})
 assert len(B)==7*n+2
 return {(x-n,y+n) for x,y in B}
def test(n):
 words=[S*j+'L'+S*j+'RLL'+S*j+'L'+S*j+'L' for j in range(n,0,-1)]
 word=''.join(words);last={};vis=Counter();seed=set();p=(0,0);h=0;prior=None
 for k,w in enumerate(words):
  assert (p,h)==((-k,k),0);seen={}
  for a in w:
   assert p not in seen;seen[p]=a
   if p in last:assert last[p]!=a
   elif a=='L':seed.add(p)
   last[p]=a;vis[p]+=1;h=(h+(1 if a=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
  assert seen==circuit_reads(n,k)
  if prior is not None:
   overlap=prior.keys()&seen.keys();assert len(overlap)==8*(n-k)+2
   assert all(prior[q]=='R' and seen[q]=='L' for q in overlap)
  prior=seen
 assert (p,h)==((-n,n),0) and len(word)==8*n*n+14*n
 assert len(seed)==11*n+2 and max(vis.values())<=2
 assert sum(v==2 for v in vis.values())==4*n*n-2*n-2
 assert len(vis)==4*n*n+16*n+2
 # Independent literal replay from the extracted full initial board.
 B=set(seed);p=(0,0);h=0
 for a in word:
  assert ('L' if p in B else 'R')==a
  B.symmetric_difference_update({p});h=(h+(1 if a=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 assert B==final_profile(n) and len(B)==7*n+2
 # Only events whose complete eleven-read history lies within this prefix.
 K=sum(word[t-10:t] not in F and word[t-9:t+1] not in F for t in range(10,len(word)))
 assert K>=8*max(n-2,0)**2
 return {'n':n,'mass':len(seed),'turns':len(word),'final_mass':len(B),'max_reads':max(vis.values()),'internal_K':K,'K_lower_bound':8*max(n-2,0)**2,
         **({'entry_seed':sorted(seed),'final_board':sorted(B)} if n<=3 else {})}
out={'standard_sha256':digest,'bad_S_ten_factors':sorted(Sf),'cases':[test(n) for n in [1,2,3,4,5,8,13,20,50,100,200]]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
