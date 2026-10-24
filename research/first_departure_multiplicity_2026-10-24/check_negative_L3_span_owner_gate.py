"""Literal negative-supplier channels, raw short returns and exact12 frames.
No period/drift/radius search; these are finite minimal-word geometry controls.
"""
from pathlib import Path
from itertools import product
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def walk(word,p,h):
 tr=[];early=[];start=p
 for i,a in enumerate(word):
  tr.append((p,h,a));h=H[(H.index(h)+(1 if a=='R'else-1))%4];p=p[0]+V[h][0],p[1]+V[h][1]
  if p==start and i<len(word)-1:early.append(i+1)
 return p,h,tr,early
rows=[]
for d,r in[('WEE','NNS'),('WEEW','NNSS')]:
 hs={(0,0):'NNSS',(0,1):'EWW',(1,0):'EEWW',(1,1):'SNNS',(2,1):d,(2,0):r};su={}
 for p,h in hs.items():
  for dr,v in V.items():
   q=p[0]+v[0],p[1]+v[1]
   if q not in hs:continue
   sr=[i for i in range(len(h))if out(h,i)==dr];tr=[i for i,a in enumerate(hs[q])if a==dr];assert len(sr)==len(tr)
   su.update({(p,a):(q,b)for a,b in zip(sr,tr)})
 paths=[[((2,0),1),((1,0),2),((1,1),2),((2,1),1)],[((1,1),3),((2,1),2),((2,0),2),((1,0),3)]]
 assert all(su[a]==b for path in paths for a,b in zip(path,path[1:]))
 assert all(''.join('R'if i%2==0 else'L'for p,i in path)=='LRRL'for path in paths)
 rows.append(dict(D=d,R=r,paths=paths,span_equation='A23(X)=A23(Y)+4'))
short={}
for n in[4,8]:
 rr=[]
 for tail in product('LR',repeat=n-1):
  w='L'+''.join(tail);p,h,tr,early=walk(w,(0,0),'E')
  if p==(0,0)and h=='E'and not early:rr.append(w)
 assert all('LRRL'not in w for w in rr);short[n]=rr
assert len(short[4])==1 and len(short[8])==5
C='LRRLLLLRRL';p,h,tr,_=walk(C,(2,0),'N');assert p==(1,-1)and h=='S'
frames=[]
for i in[1,2]:
 for pre in product('LR',repeat=i):
  for post in product('LR',repeat=2-i):
   if pre[0]!='L':continue
   delta=sum(1 if a=='R'else-1 for a in pre);hi=H[(-delta)%4]
   pp,hh,_,_=walk(''.join(pre),(0,0),hi);assert hh=='N';root=(2-pp[0],-pp[1])
   w=''.join(pre)+C+''.join(post);p,h,trace,early=walk(w,root,hi)
   if p==root and h==hi and not early:frames.append(dict(root=root,incoming=hi,prefix=''.join(pre),word=w,trace=trace))
assert len(frames)==2 and {(tuple(z['root']),z['incoming'])for z in frames}=={((2,-1),'E'),((1,-1),'S')}
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,negative_channels=rows,raw_short_returns=short,fused_ten_word=C,only_twelve_frames=frames,exclusions=['second LEFT crossing','flow2 crossing after flat X']),indent=2)+'\n');print('PASS two supplier pairs; raw4/8 lists; exact two12 frames')
