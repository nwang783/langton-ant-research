#!/usr/bin/env python3
"""Constructive turn-path search for a STATIC, not color-legal, flow control."""
import itertools,json,math
D=((0,1),(1,0),(0,-1),(-1,0));A='RRLRRRRL'
def test(word):
 x=y=h=0;events=[]
 for i,c in enumerate(word):
  hh=(h+(1 if c=='R' else -1))%4;events.append(((x,y),h,hh,c));dx,dy=D[hh];x+=dx;y+=dy;h=hh
 if h or not x or not y:return
 if x<0:events=[((-p[0],-p[1]),(hi+2)%4,(ho+2)%4,c) for p,hi,ho,c in events];x=-x;y=-y
 hist={}
 for p,hi,ho,c in events:
  k=p[0]//x;q=(p[0]-k*x,p[1]-k*y);hist.setdefault(q,[]).append((hi,ho,c))
 mm=max(map(len,hist.values()))
 if mm>3:return
 for hs in hist.values():
  if sum(1 if c=='R' else -1 for hi,ho,c in hs)!=len(hs)%2:return
  if len(hs)==3:
   inc=[sum(hi==a for hi,ho,c in hs) for a in range(4)];out=[sum(ho==a for hi,ho,c in hs) for a in range(4)]
   if max(inc)>2 or max(out)>2:return
   di=inc.index(2);do=out.index(2)
   if (do-di)%4!=3:return
 return dict(word=word,drift=[x,y],classes=len(hist),max_multiplicity=mm)
if __name__=='__main__':
 found=[];tested=0
 for ns in itertools.product(range(8),repeat=4):
  if not ns[0]>ns[2] or ns[1]==ns[3]:continue
  for bridges in [('R','R','R','R'),('L','L','L','L'),('RRR','R','RRR','R'),('R','RRR','R','RRR')]:
   word=''.join(A*n+b for n,b in zip(ns,bridges));tested+=1;r=test(word)
   if r:found.append(r);print(json.dumps(r),flush=True);break
  if found:break
 out=dict(tested=tested,status='STATIC_WITNESS' if found else'NO_WITNESS_BOUNDED_FAMILY',found=found)
 print(json.dumps(out));open(__file__.replace('.py','.json'),'w').write(json.dumps(out,indent=2)+'\n')
