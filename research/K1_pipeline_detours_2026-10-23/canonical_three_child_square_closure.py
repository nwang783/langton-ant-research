"""Complete necessary closure around a putative canonical three-child fork.
Four actual maximum faces and all their physical shared edges. No K1 order.
"""
from pathlib import Path
from itertools import product
import json
base=json.loads(Path(__file__).with_name('canonical_max_face_child_ports.json').read_text())['rows']
H='NESW';V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0))
cp=dict(A=(1,0),Z=(0,0),Y=(0,1),B=(1,1))
op=dict(A=(1,-1),Z=(-1,-1),Y=(-1,1),B=(1,1))
def rot(p,q):
 x,y=p
 for _ in range(q%4):x,y=-y,x
 return x,y
# q is counterclockwise quarter turns.
def pose(row,ll,q):
 def cell(p):
  a,b=rot((2*p[0]-1,2*p[1]-1),q);return ((a+1)//2+ll[0],(b+1)//2+ll[1])
 def face(p):return cell(p)
 hh={cell(cp[k]):''.join(H[(H.index(x)-q)%4]for x in s)for k,s in row['headings'].items()}
 # Face LL transforms about center(.5,.5), so face centers need the other rule.
 def fc(p):
  a,b=rot(p,q);return (a+ll[0],b+ll[1])
 heights={ll:0}
 for k,p in op.items():
  x=row['other'].get(k,'M');heights[fc(p)]=0 if x=='M'else-int(x[2:])
 entry=cell(cp['A'])
 # Direction of the four oriented F boundary edges, source cell coordinates.
 bd=[(cell(cp[k]),H[(H.index(o)-q)%4])for k,o in [('A','W'),('Z','N'),('Y','E'),('B','S')]]
 return hh,heights,entry,bd
# Correct face LL rotations: for a face indexed p, center relative central face is p.
def outs(h):return [H[(H.index(x)+(1 if r%2==0 else-1))%4]for r,x in enumerate(h)]
def check(packages):
 hh={};heights={};births=[]
 for row,ll,q in packages:
  hs,fs,e,bd=pose(row,ll,q)
  for p,h in hs.items():
   if p in hh and hh[p]!=h:return
   hh[p]=h
  for p,h in fs.items():
   if p in heights and heights[p]!=h:return
   heights[p]=h
  births.append((e,bd))
 ns=[(p,r)for p,h in hh.items()for r in range(len(h))];es=[]
 for p,h in hh.items():
  for r in range(len(h)-1):es.append(((p,r),(p,r+1),4))
 oo={p:outs(h)for p,h in hh.items()}
 for p,h in hh.items():
  axis='EW'if h[0]in'NS'else'NS'
  for o in axis:
   dx,dy=V[o];w=(p[0]+dx,p[1]+dy)
   if w not in hh:continue
   a=[(p,r)for r,x in enumerate(oo[p])if x==o];b=[(w,r)for r,x in enumerate(hh[w])if x==o]
   if len(a)!=len(b):return
   for x,y in zip(a,b):es.extend([(x,y,1),(y,x,-1)])
 for e,bd in births:
  first=[]
  for p,o in bd:
   a=[(p,r)for r,x in enumerate(oo[p])if x==o]
   if not a:return
   first.append(a[0])
  if (e,1)not in first:return
  for x in first:
   if x!=(e,1):es.append(((e,1),x,1))
 d={x:0 for x in ns}
 for _ in ns:
  change=False
  for x,y,k in es:
   if d[y]<d[x]+k:d[y]=d[x]+k;change=True
  if not change:break
 else:return
 off=d[(1,0),1]
 return dict(headings={str(p):h for p,h in hh.items()},heights={str(p):h for p,h in heights.items()},minimum_clocks={str(p):[d[p,r]-off for r in range(len(h))]for p,h in hh.items()})
rows=[];candidates=0
forks=[r for r in base if len(r['potential_children'])==3]
for f in forks:
 options=[]
 for cname,ll,q in [('Z',(-1,-1),1),('Y',(-1,1),0),('B',(1,1),3)]:
  known=f['headings'][cname]
  opts=[r for r in base if pose(r,ll,q)[0][cp[cname]]==known]
  options.append(opts)
 for z,y,b in product(*options):
  candidates+=1
  c=check([(f,(0,0),0),(z,(-1,-1),1),(y,(-1,1),0),(b,(1,1),3)])
  if c is not None:rows.append(dict(main=f['headings'],child_profiles=[z['headings'],y['headings'],b['headings']],**c))
r=dict(scope=__doc__,fork_profiles=len(forks),candidates=candidates,count=len(rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items()if k!='rows'},indent=2))
print('first profiles',json.dumps([dict(main=x['main'],children=x['child_profiles'])for x in rows[:5]],indent=2))
