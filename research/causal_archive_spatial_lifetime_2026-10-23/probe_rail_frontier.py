import json
G=json.load(open('/workspace/shared/langton/core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'))['geometry'];K=set(map(tuple,json.load(open('/workspace/shared/langton/core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'))['core']))
DIR=((0,1),(1,0),(0,-1),(-1,0))
def rot(z,h):
 x,y=z;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def run(n):
 w=[9]+[4]*n+[6]+[4]*(n-1);program=''.join(G[a]['word']for a in w)+G[0]['marker'];p=(0,0);h=0;par=set();need={}
 for t,ch in enumerate(program):
  b=(ch=='L')^(p in par)
  if p in need and need[p]!=b:return dict(N=n,legal=False,t=t,cell=p)
  need[p]=b
  if p in par:par.remove(p)
  else:par.add(p)
  h=(h+(-1 if ch=='L'else 1))%4;p=add(p,DIR[h])
 seed={q for q,b in need.items()if b};T={q:('entry',None,None)for q in seed-K};p=(0,0);h=0;c=0;ages=[];cut=None;at=0
 for j,a in enumerate(w):
  ii=[add(p,rot(tuple(i),h))for i in G[a]['inputs']]
  for q in ii:
   if q not in T:return dict(N=n,legal='raw but wrong ordered',j=j,cell=q)
   tag=T.pop(q)
   if tag[0]!='entry':ages.append((j,q,c-tag[1],tag[2]))
  for q in G[a]['outputs']:
   q=add(p,rot(tuple(q),h));assert q not in T;T[q]=('prod',c,j)
  dx,dy,dh=G[a]['endpoint'];p=add(p,rot((dx,dy),h));h=(h+dh)%4;c+=G[a]['name'].count('C')
  if j==n+1:cut=(p,h,c,len(T),list(T.items()))
 return dict(N=n,legal=True,m=len(seed),C=c,total=len(w),ages=ages,cut=cut[:4],future_produced=len([r for r in ages if r[0]>n+1]),first_return_source=next((r for r in ages if r[0]>n+1),None))
for n in (1,2,3,4,5,10,20,50,100):print(run(n))
