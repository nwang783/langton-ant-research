"""Exact phase-rounded difference closure and forced-pose checks on local controls.
Not an actual exterior ant itinerary or translating-front realization.
"""
from pathlib import Path
from collections import Counter
import ast,json,math
H='NESW';V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0));INF=10**6
s=Path(__file__).with_name('canonical_three_child_square_closure.py').read_text();tree=ast.parse(s)
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)and x.name=='outs'],type_ignores=[]),'out','exec'))
def phase(p):return(2*(p[0]-1)+(0 if(p[0]+p[1])%2 else 3))%4
def check(row):
 hh={ast.literal_eval(p):h for p,h in row['headings'].items()};oo={p:outs(h)for p,h in hh.items()};ns=[(p,r)for p,h in hh.items()for r in range(len(h))];ii={n:i for i,n in enumerate(ns)};n=len(ns);es=[]
 for p,h in hh.items():
  for r in range(len(h)-1):es.append(((p,r),(p,r+1),4))
 for p,h in hh.items():
  for o in('EW'if h[0]in'NS'else'NS'):
   dx,dy=V[o];w=(p[0]+dx,p[1]+dy)
   if w not in hh:continue
   a=[(p,r)for r,x in enumerate(oo[p])if x==o];b=[(w,r)for r,x in enumerate(hh[w])if x==o]
   if len(a)!=len(b):return 'ports'
   for x,y in zip(a,b):es.extend([(x,y,1),(y,x,-1)])
 # Each of the five known faces has an ACTUAL specified canonical entry.
 for ll,entry in [((0,0),(1,0)),((-1,-1),(0,0)),((-2,0),(-1,0)),((-1,1),(-1,1)),((1,1),(1,1))]:
  x,y=ll
  bd=[((x+1,y),'W'),((x,y),'N'),((x,y+1),'E'),((x+1,y+1),'S')]
  for p,o in bd:
   f=next(((p,r)for r,z in enumerate(oo[p])if z==o),None)
   if f is None:return 'empty_boundary'
   if f!=(entry,1):es.append(((entry,1),f,1))
 d=[[-INF]*n for _ in range(n)]
 for i in range(n):d[i][i]=0
 for a,b,k in es:
  v=math.ceil((k-phase(b[0])+phase(a[0]))/4);i,j=ii[a],ii[b];d[i][j]=max(d[i][j],v)
 for k in range(n):
  dk=d[k]
  for i in range(n):
   z=d[i][k]
   if z<=-INF:continue
   di=d[i]
   for j in range(n):
    if dk[j]>-INF and di[j]<z+dk[j]:di[j]=z+dk[j]
 if any(d[i][i]>0 for i in range(n)):return 'phase_cycle'
 for i,(p,r)in enumerate(ns):
  for j,(w,s)in enumerate(ns):
   if i==j or d[i][j]<=-INF or d[j][i]<=-INF or d[i][j]+d[j][i]!=0:continue
   gap=4*d[i][j]+phase(w)-phase(p)
   if gap<0:continue
   if gap==0:return 'forced_same_time'
   dx,dy=V[oo[p][r]];first=(p[0]+dx,p[1]+dy)
   if gap==1:
    if first!=w or hh[w][s]!=oo[p][r]:return 'forced_consecutive_pose'
   # Any forced short interval must admit the actual initial departure and last arrival.
   elif gap<=8:
    cur={(first,oo[p][r])}
    for _ in range(gap-1):
     nxt=set()
     for(a,h)in cur:
      for turn in(-1,1):
       o=H[(H.index(h)+turn)%4];dx,dy=V[o];nxt.add(((a[0]+dx,a[1]+dy),o))
     cur=nxt
    if(w,hh[w][s])not in cur:return 'forced_short_pose'
 return 'retained'
src=Path(__file__).with_name('canonical_duplicator_local_parent_return.json');a=json.loads(src.read_text());counts=Counter();rows=[]
for r in a['rows']:
 c=check(r);counts[c]+=1
 if c=='retained':rows.append(r)
out=dict(scope=__doc__,source_count=len(a['rows']),counts=counts,rows=rows)
Path(__file__).with_name('canonical_duplicator_local_parent_return_allpairs_refinement.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='rows'},indent=2))
