"""Independent of bounded front graph: literal controls for the ladder formula."""
import json,pathlib
D=((0,1),(1,0),(0,-1),(-1,0));out=[]
for d in range(100):
 B={(-1,-i)for i in range(1,2*d+1)};x=y=0;h=1;w='RRLL'*d+'RRRR'+'LLRR'*d+'LR'+'RRRL'
 for t,c in enumerate(w):
  assert ((x,y)in B)==(c=='L'),(d,t,(x,y),c)
  B.symmetric_difference_update({(x,y)});h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
  if t==len(w)-5:assert (x,y,h)==(1,1,1) and {yy for xx,yy in B if xx==0}=={1,-2*d-1}
 assert (x,y,h)==(-1,1,3)
 out.append(dict(depth=d,length=len(w),end=(x,y,h)))
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print('PASS',len(out),'finite controls; the all-depth claim uses the analytic proof')
