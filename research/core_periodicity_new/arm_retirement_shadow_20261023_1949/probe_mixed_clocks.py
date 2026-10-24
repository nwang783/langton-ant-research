from pathlib import Path
exec((Path(__file__).resolve().parent/'literal_helpers.py').read_text())
def ep(a,p,h):
 x,y,dh=G[a]['endpoint'];return place((x,y),p,h),(h+dh)%4
def single(hit,p):return hit==[[str(p[0]),str(p[1])]]or hit==[list(p)]
def paths(adj,s,t):
 todo=[(s,[s])]
 while todo:
  v,p=todo.pop()
  if v==t:yield p;continue
  for z in adj.get(v,[]):
   if z not in p:todo.append((z,p+[z]))
for s in(7,8,9):
 R=set(map(tuple,G[s]['outputs']));got={};adj={}
 for q in R:
  a,b=edge(q);adj.setdefault(a,[]).append(b);adj.setdefault(b,[]).append(a)
 for a in IDS:
  for h in range(4):
   for z in R:
    for inp in G[a]['inputs']:
     p=sub(z,rot(inp,h));ins={place(q,p,h)for q in G[a]['inputs']};ctx={place(q[:2],p,h)for q in G[a]['requirements']};cc=chords(a,p,h)
     if(sum(p)+h)%2 or ctx&(R-ins):continue
     se,sh=ep(s,(0,0),0);src=chords(s);bad=False
     for i,ch in enumerate(src):
      for j,new in enumerate(cc):
       hit=contact(*ch,*new)
       if hit and not(i==len(src)-1 and j==0 and(p,h)==(se,sh)and single(hit,ch[1])):bad=True
     if bad:continue
     good=[]
     for E in adj:
      if not on(E,*cc[0]):continue
      for path in paths(adj,E,W):
       valid=True
       for i,(u,v)in enumerate(zip(path,path[1:])):
        if contact(*cc[0],u,v)and not(i==0 and single(contact(*cc[0],u,v),E)):valid=False
        for j,(x,y)in enumerate(src):
         if j==0:x=W
         hit=contact(x,y,u,v)
         if hit and not(i==len(path)-2 and j==0 and single(hit,W)):valid=False
       if not valid:continue
       # A simple graph path need not geometrically be simple in arbitrary
       # graphs, but even-dual unit edges cross only at shared vertices.
       vv=[sub(cc[0][1],cc[0][0])]+[sub(v,u)for u,v in zip(path,path[1:])]+[(0,1)]
       closing=sum(math.atan2(cross(u,v),dot(u,v))for u,v in zip(vv,vv[1:]));alpha=math.pi/4 if a in(0,1)else math.atan(3)if a in(4,5,6)else math.pi/2
       mm=(closing+alpha-math.pi/2)/(math.pi/2);m=round(mm);assert abs(mm-m)<1e-10
       ages=[n for n in(4-m,-4-m)if n>=0 and n%4==(-h)%4]
       good.append((E,path,m,ages))
     got[(a,p,h)]=good
 print('SOURCE',s)
 for (a,p,h),good in sorted(got.items()):
  ages={n for gg in good for n in gg[3]};print(G[a]['name'],p,h,'clocks',ages,'bridges',len(good))
