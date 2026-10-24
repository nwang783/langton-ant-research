"""Right-end dynamics with exact ideal paired-arm resets.
The omitted far-left turnaround is NOT an autonomous ant mechanism.
A relative cycle certifies only this right-local reset system, not a counterexample.
"""
import json,sys,pathlib
DIRE=((0,1),(1,0),(0,-1),(-1,0));S='RLLR';W='LLRLRRRRLRRRRLLLLRLL';REV=lambda w:w[::-1].translate(str.maketrans('RL','LR'))
HERE=pathlib.Path(__file__).resolve().parent
UP=int(sys.argv[1])if len(sys.argv)>1 else 6

def trace(w,p):
 x,y,h=p;out=[]
 for c in w:
  out.append(((x,y),c));h=(h+(1 if c=='R'else-1))%4;dx,dy=DIRE[h];x+=dx;y+=dy
 return out,(x,y,h)
def reset_template(a,h,b=-6,n=40):
 out,p=trace(a*n,(0,0,h));inc,end=trace(REV(a)*(n+b//2),(p[0],p[1],(h+2)%4));hist={}
 assert end==(b,0,(h+2)%4)
 for pt,c in out+inc:
  if pt[0]>=-20:hist.setdefault(pt,[]).append(c)
 assert all(all(c!=d for c,d in zip(cs,cs[1:]))for cs in hist.values())
 guard={p:cs[0]=='L'for p,cs in hist.items()if p[0]>=-12}
 flip={p for p,cs in hist.items()if len(cs)%2};assert min(x for x,y in flip)>-12
 rows={y for x,y in hist};assert all(cs[0]==('L'if p[1]==0 else'R')for p,cs in hist.items()if p[0]<=-13)
 return dict(guard=guard,flip=flip,rows=rows,offset=b)
TPL={1:reset_template(W,1),3:reset_template(REV(S),3)}
# Base is a pair of black left half-rows, with the first already rewritten
# by an incoming rightward sweep. Optional finite defects can be supplied.
BASE_ROWS={0,UP};diff=set()
if len(sys.argv)>2:diff={tuple(p)for p in json.load(open(sys.argv[2]))}
def base(p):return p[0]<0 and p[1]in BASE_ROWS
def color(p):return base(p)^(p in diff)
def flip(p):
 if p in diff:diff.remove(p)
 else:diff.add(p)
def canreset(x,y,h):
 t=TPL[h]
 rows={y+b for b in t['rows']}
 if BASE_ROWS.intersection(rows)!={y}:return False
 if any(color((x+a,y+b))!=v for(a,b),v in t['guard'].items()):return False
 # Every affected far-left row is uniform. Check all finite discrepancies,
 # plus the interval between the original and current base cut.
 cut=x-12
 if any(p[0]<cut and p[1]in rows and color(p)!=(p[1]==y)for p in diff):return False
 if cut>0 and any(not color((a,y))for a in range(cut)):return False
 return True
def normalize(x,y,h):
 z=set(diff)
 for a in range(min(0,x),max(0,x)):
  for yy in BASE_ROWS:
   p=a,yy
   if p in z:z.remove(p)
   else:z.add(p)
 return y,h,tuple(sorted((a-x,b)for a,b in z))
x=y=0;h=1;events=[];seen={};ordinary=0;cycle=None;MAX=1000000
for k in range(MAX):
 if y in BASE_ROWS and h in TPL and canreset(x,y,h):
  key=normalize(x,y,h)
  if key in seen:
   old=seen[key];cycle=dict(previous_event=old[0],event=len(events),drift=x-old[1],ordinary_steps=ordinary-old[2],head=[x,y,h]);print('RELATIVE_CYCLE',cycle,flush=True);break
  seen[key]=(len(events),x,ordinary)
  if len(events)<30:print('reset',len(events),'W'if h==1 else'S','pose',x,y,h,'diff',len(diff),'range',(min((p[0]for p in diff),default=0),max((p[0]for p in diff),default=0)),flush=True)
  events.append(dict(kind='W'if h==1 else'S',x=x,y=y,ordinary=ordinary,normalized=key))
  t=TPL[h]
  for a,b in t['flip']:flip((x+a,y+b))
  x+=t['offset'];h=(h+2)%4
  if len(events)>=10000:print('RESET_CAP',flush=True);break
 else:
  p=x,y;b=color(p);flip(p);h=(h+(-1 if b else 1))%4;dx,dy=DIRE[h];x+=dx;y+=dy;ordinary+=1
  if abs(y)>30 or abs(x)>1000 or len(diff)>10000:
   print('BOUND',x,y,h,ordinary,len(events),len(diff),flush=True);break
else:print('STEP_CAP',flush=True)
out=dict(upper_row=UP,events=events,cycle=cycle,ordinary=ordinary,final_pose=[x,y,h],diff=sorted(diff))
(HERE/f'reset_endpoint_upper{UP}.json').write_text(json.dumps(out));print('DONE',ordinary,len(events),cycle,flush=True)
