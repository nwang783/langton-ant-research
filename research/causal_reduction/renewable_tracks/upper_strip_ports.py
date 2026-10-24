"""Counterexample search in a conservative upper strip with arbitrary lower ports.
Bounds yield UNKNOWN, never a universal exclusion.
"""
import sys,json,time,collections,pathlib
HERE=pathlib.Path(__file__).resolve().parent
LO=int(sys.argv[1]) if len(sys.argv)>1 else 2
XMIN=-4;XMAX=8;HI=4;WIDTH=XMAX-XMIN+1
PORTS=[x for x in range(XMIN+1,XMAX) if (x+LO)%2==1]
D=((0,1),(1,0),(0,-1),(-1,0))
def idx(x,y):return (y-LO)*WIDTH+x-XMIN
def run(B,x):
 y=LO;h=0;w=[]
 for t in range(5000):
  if y<LO:return B,''.join(w),(x,y,h)
  if not XMIN<=x<=XMAX or y>HI:return None
  i=idx(x,y);c=B>>i&1;w.append('L' if c else 'R');B^=1<<i;h=(h+(-1 if c else 1))%4;dx,dy=D[h];x+=dx;y+=dy
 return None
def bad(B):
 a={x for x in range(XMIN,XMAX+1) if B>>idx(x,3)&1};b={x for x in range(XMIN,XMAX+1)if B>>idx(x,4)&1}
 if any(x<0 for x in a|b) or not b:return False
 s=min(b)
 if LO<=2 and {x for x in range(XMIN,0) if B>>idx(x,2)&1}!={-1}:return False
 if LO<=1 and (not(B>>idx(0,1)&1) or any(B>>idx(x,1)&1 for x in range(XMIN,0))):return False
 return all(x in a for x in range(s+1))
if __name__=='__main__':
 t0=time.time();seen={0:None};q=collections.deque([(0,0)]);witness=None;edges=0
 while q and len(seen)<200000:
  B,depth=q.popleft()
  if depth>=8:continue
  for p in PORTS:
   ans=run(B,p)
   if ans is None:continue
   C,w,ex=ans;edges+=1
   if C in seen:continue
   seen[C]=(B,p,w,ex);q.append((C,depth+1))
   if bad(C):witness=C;q.clear();break
 chain=[];C=witness
 while C is not None and seen.get(C) is not None:
  B,p,w,ex=seen[C];chain.append(dict(port=(p,LO,0),word=w,exit=ex,output=C));C=B
 chain.reverse();out=dict(lo=LO,ports=PORTS,states=len(seen),edges=edges,status='COUNTEREXAMPLE'if witness is not None else'UNKNOWN',chain=chain,seconds=time.time()-t0)
 (HERE/f'upper_strip_ports_lo{LO}.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
