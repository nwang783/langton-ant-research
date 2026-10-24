"""Independent exhaustive position-inflation prefix trees, no heading equality."""
from pathlib import Path
import itertools,json,time
R=Path(__file__).resolve().parents[1];P=R/'causal_reduction/morphic_candidates';D=((0,1),(1,0),(0,-1),(-1,0));start=time.time()
def trace(w,p=(0,0),h=0):
 reads=[];poses=[(p,h)]
 for c in w:reads.append((p,c));h=(h+(1 if c=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1]);poses.append((p,h))
 return reads,poses
mul=lambda a,p:(a[0]*p[0]-a[1]*p[1],a[1]*p[0]+a[0]*p[1])
def valid(w):
 seen={}
 for p,c in trace(w)[0]:
  if seen.get(p)==c:return False
  seen[p]=c
 return True
out=[]
for k in range(2,6):
 words=[''.join(w) for w in itertools.product('RL',repeat=k) if valid(''.join(w))];scales=set()
 for w in words:
  p=trace(w)[1][-1][0];sg=1 if w[0]=='R' else -1;a=sg*p[0],sg*p[1]
  if sum(v*v for v in a)>1:scales.add(a)
 source=json.loads((P/f'position_only_k{k}.json').read_text())['results'];assert scales=={tuple(z['scale']) for z in source}
 for row in source:
  if row['status']!='EXHAUSTED':continue
  a=tuple(row['scale']);nodes=0;maxdepth=0
  def dfs(n,w,poses,last):
   global nodes,maxdepth
   nodes+=1;maxdepth=max(maxdepth,n)
   for image in words:
    c=image[0] if n==0 else w[n]
    if n==0:head=(0,0);hc=0;hn=(hc+(1 if c=='R' else -1))%4;q=D[hn]
    else:q=poses[n+1][0]
    target=mul(a,q);rr,pp=trace(image,*poses[-1])
    if pp[-1][0]!=target:continue
    seen=last.copy()
    for p,letter in rr:
     if seen.get(p)==letter:break
     seen[p]=letter
    else:dfs(n+1,w+image,poses+pp[1:],seen)
  dfs(0,'',[((0,0),0)],{})
  assert nodes==row['nodes'] and maxdepth==row['max_macros'],(k,a,nodes,maxdepth,row)
  out.append({'k':k,'scale':a,'nodes':nodes,'max_macros':maxdepth});print(out[-1],flush=True)
result={'status':'Every claimed EXHAUSTED tree independently regenerated without a depth or node cutoff','cases':out,'scope':'Completes the finite-tree dependencies for position-only inflation k2..5. Surviving scales require the separately reviewed forward-owner finite-fuel lemma. No heading preservation assumed.','seconds':time.time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
