import json
D=[(0,1),(1,0),(0,-1),(-1,0)]
B=set();x=y=h=0;st=[]
for t in range(30000):
 a='L' if (x,y) in B else 'R'
 if a=='L':B.remove((x,y))
 else:B.add((x,y))
 if st and st[-1][0]==a:
  st[-1][1]+=1
  if st[-1][1]==4:st.pop()
 else:st.append([a,1])
 h=(h+(1 if a=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
# Ignore initial/end exceptional syllables. Dual face center as midpoint average of four a-turn cycle.
x=y=h=0;cent=[]
for idx,(a,e) in enumerate(st):
 xx,yy,hh=x,y,h;pts=[]
 for j in range(4):
  pts.append((xx,yy));hh=(hh+(1 if a=='R' else -1))%4;dx,dy=D[hh];xx+=dx;yy+=dy
 cent.append((sum(q[0] for q in pts)/4,sum(q[1] for q in pts)/4))
 for j in range(e):h=(h+(1 if a=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
last={};loops=[]
for i,p in enumerate(cent):
 if p in last:
  j=last[p]
  if i-j>=4 and i<1000:
   path=cent[j:i+1];area=sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(path,path[1:]))/2
   # geometric signed turn clockwise, no immediate reversal expected
   cc=0
   for k in range(j+1,i+1):
    aa,ee=st[k]
    if ee==1:cc+=1 if aa=='L' else -1
   loops.append({'start':j,'end':i,'area':area,'curvature':cc,'path':path,'core':st[j:i+1]})
 last[p]=i
pos=[L for L in loops if L['curvature']>0]
print('stages',len(st),'loopcount',len(loops),'positive',len(pos),'maxcurve',max((L['curvature'] for L in loops),default=0))
print(json.dumps(pos[:1]))
open('/workspace/shared/langton/core_periodicity_new/core_loop_controls.json','w').write(json.dumps({'stage_count':len(st),'positive':pos[:5],'loops':loops[:30]},indent=2))
