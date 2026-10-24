from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();ROOT=P.parents[1];D=ROOT/'K1_pipeline_detours_2026-10-23'
steps=(1j,1,-1j,-1)
def enumerate_factors(n,deep):
 found=[]
 def go(p,h,word,history):
  t=len(word);nr=len(history.get(0j,[]))
  if p==0j and t:
   if nr==2:
    if t==n and h==0:found.append(word)
    return
   if nr!=1 or h!=0:return
  if t>=n or abs(p.real)+abs(p.imag)>n-t:return
  old=history.get(p,[])
  if deep:
   if p.real+p.imag>0:return
   if p!=0j and p.real+p.imag==0:
    if p.real<=0 or h!=0 or old:return
    opts=('L',)
   elif p!=0j and old:
    if len(old)>=(4 if old[0]=='R'else 3):return
    opts=('L'if old[-1]=='R'else'R',)
   else:opts=None
  else:opts=None
  if p==0j:opts=('R'if nr==0 else'L',)
  elif opts is None:opts=('L'if old[-1]=='R'else'R',)if old else('R','L')
  for c in opts:
   nh=(h+(1 if c=='R'else-1))%4
   history[p]=old+[c];go(p+steps[nh],nh,word+c,history)
  if old:history[p]=old
  else:history.pop(p,None)
 go(0j,2,'',{})
 return sorted(found)
rows=[]
for n in(8,12,16):
 sol=enumerate_factors(n,False);assert(len(sol)==(2 if n==16 else 0));rows.append(dict(span=n,unrestricted=sol))
assert rows[-1]['unrestricted']==sorted(['RRRLRRLRRLRRLLLL','RLLLLRRLRRLRRLRR'])
for row in rows:
 sol=enumerate_factors(row['span'],True);assert not sol;row['deep']=sol
sol20=enumerate_factors(20,True);assert sol20==['RLRRRRLLLLRLLRLLRLLR']
# Check explicit positive-net-black deep factor INCLUDING final root read.
word='RLRRRRLLLLRLRRRRLRLLRLLRR';seed={complex(*q)for q in[(-1,-3),(-1,0),(0,-3),(0,-1),(1,-2),(1,-1)]};board=set(seed);p=0j;h=2;vis={}
for i,c in enumerate(word):
 assert(p in board)==(c=='L');old=vis.get(p,[])
 if p.real+p.imag==0 and p!=0j:assert p.real>0 and h==0 and c=='L'and not old
 assert p.real+p.imag<=0;vis[p]=old+[(h,c)];board.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=steps[h]
assert vis[0j]==[(2,'R'),(0,'L'),(0,'R')]
assert board=={complex(*q)for q in[(-3,-2),(-3,-1),(-2,-1),(-2,0),(-1,-2),(-1,-1),(0,-2),(0,-1),(0,0)]}
for q,hs in vis.items():assert len(hs)<=(4 if hs[0][1]=='R'else 3)
out=dict(status='PASS independent short-factor controls for strict-straight K1 deep-port reduction',note_sha256=hashlib.sha256((D/'strict_straight_K1_port_reduction.md').read_bytes()).hexdigest(),short_factors=rows,span20=sol20,positive_net_black=3,scope='Analytic local ordinal/chronology forcing independently reviewed under complete-white cap4, selected straight diagonal maximum-face curve, K=1, and strict LEFT C neighbors. Necessary deep-port history excludes spans8/12/16, so stage>=24 and P>=30ell. No bent/branched/K>1 exclusion, sustainable deep machine or fresh-fuel claim.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
