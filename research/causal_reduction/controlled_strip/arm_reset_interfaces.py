"""Exact finite controls for paired inverse horizontal arms near the right end.
The far-left turnaround is deliberately omitted and must be supplied separately.
"""
import json,pathlib
D=((0,1),(1,0),(0,-1),(-1,0));S='RLLR';W='LLRLRRRRLRRRRLLLLRLL';REV=lambda w:w[::-1].translate(str.maketrans('RL','LR'))
HERE=pathlib.Path(__file__).resolve().parent

def trace(w,p):
 x,y,h=p;out=[]
 for c in w:
  out.append(((x,y),c));h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 return out,(x,y,h)

def iface(a,h,b,n=20):
 # Outward from right endpoint toward the left; return on reverse-complement.
 out,p=trace(a*n,(0,0,h));back=REV(a);q=(p[0],p[1],(h+2)%4);inc,end=trace(back*(n+b//2),q)
 assert end==(b,0,(h+2)%4),(a,b,end)
 hist={}
 for pt,c in out+inc:
  if pt[0]>=-12:hist.setdefault(pt,[]).append(c)
 bad={pt:''.join(cs)for pt,cs in hist.items()if any(x==y for x,y in zip(cs,cs[1:]))}
 # The far-right finite guard is obtained relative to the solid row0 input.
 # x<-6 is retained as a bulk control, not included in the interface guard.
 first={pt:cs[0]=='L'for pt,cs in hist.items()if pt[0]>=-6}
 flip=[pt for pt,cs in hist.items()if len(cs)%2 and pt[0]>=-6]
 return dict(kind='W'if a==W else'S',offset=b,entry_heading=h,exit_heading=(h+2)%4,bad=[(p,w)for p,w in bad.items()],guard=sorted((p,int(v))for p,v in first.items()),flip=sorted(flip),bulk_histories=sorted((p,''.join(cs))for p,cs in hist.items()if -12<=p[0]<=-8))
rows=[]
for a,h in[(W,1),(REV(S),3)]:
 for b in range(-6,8,2):
  z=iface(a,h,b);rows.append(z);print(z['kind'],b,'bad',z['bad'],'flip',z['flip'])
(HERE/'arm_reset_interfaces.json').write_text(json.dumps(rows,indent=2))
