"""No imported ant/clock code: exact eight-case oblique one-coordinate clock."""
from fractions import Fraction as F
import json,pathlib
D=((0,1),(1,0),(0,-1),(-1,0))
records=[]
for a,b in [(F(4),F(4)),(F(16),F(4)),(F(4),F(64)),(F(3,2),F(10))]:
 den=a*b-1;delta=(a*b-a-b-3)/den;gamma=(3*a*b+a+b-1)/den
 assert delta>0 and gamma>=delta
 M=2/delta;A=((a+1)/den,(b+1)/den,-b*(a+1)/den,-a*(b+1)/den)
 minima={}
 for h in range(4):
  for s in [1,-1]:
   low=None
   for x in range(-9,10):
    for y in range(-9,10):
     w=a**x*b**y
     hn=(h+s)%4;dx,dy=D[hn];wn=w*a**dx*b**dy
     f=lambda w:M*(w+1/w)-2
     head=lambda h,w:M*(A[h]*w+A[(h+2)%4]/w)
     gain=-((-1)**h)*s*f(w)+head(hn,wn)-head(h,w)
     expected=F(2)if ((-1)**h)*s==1 else M*((delta*w+gamma/w)if h in(0,1)else(gamma*w+delta/w))-2
     assert gain==expected,(a,b,h,s,x,y,gain,expected)
     assert gain>=2
     low=gain if low is None else min(low,gain)
   minima[str((h,s))]=str(low)
 records.append(dict(a=str(a),b=str(b),delta=str(delta),gamma=str(gamma),M=str(M),cases=8*19*19,minima=minima))
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2));print(json.dumps(records,indent=2))
