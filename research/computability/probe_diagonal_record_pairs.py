"""Exact local pristine-row inventories for k8,a=2+2i diagonal records.
Necessary pair constraints only. No global exclusion inferred automatically.
"""
import itertools,json,pathlib,collections
D=((0,1),(1,0),(0,-1),(-1,0));HERE=pathlib.Path(__file__).resolve().parent

def trace(w,h):
 x=y=0;ev=[]
 for c in w:
  ev.append((x,y,h,c));h=(h+(1 if c=='R'else -1))%4;dx,dy=D[h];x+=dx;y+=dy
 return ev,(x,y,h)
by=collections.defaultdict(list)
for h in range(4):
 for w in map(''.join,itertools.product('RL',repeat=8)):
  ev,end=trace(w,h);last={};okay=True
  for x,y,H,c in ev:
   if last.get((x,y))==c:okay=False;break
   last[x,y]=c
  if okay:by[h,end[0],end[1]].append((w,ev,end[2]))
rows=[]
for typ,prev,nextd in [('N',(-2,2),(2,2)),('E',(2,2),(2,-2))]:
 for h in range(4):
  good=[]
  for u,eu,hu in by[h,*prev]:
   for v,ev,hv in by[hu,*nextd]:
    events=[(x-prev[0],y-prev[1],H,c) for x,y,H,c in eu]+ev;last={};okay=True;fresh=[]
    for t,(x,y,H,c) in enumerate(events):
     old=last.get((x,y))
     if old==c or (old is None and y>=0 and c=='L'):okay=False;break
     last[x,y]=c
     if y>=0:fresh.append(t)
    if okay:good.append(dict(previous=u,next=v,junction_heading=hu,first_upper=min(fresh),previous_upper=[t for t in fresh if t<8]))
  rows.append(dict(type=typ,entry_heading=h,pairs=good));print(typ,h,'pairs',len(good),'firstupper',collections.Counter(z['first_upper'] for z in good),'nexts',collections.Counter(z['next'] for z in good),flush=True)
(HERE/'diagonal_record_pairs.json').write_text(json.dumps(rows,indent=2))
