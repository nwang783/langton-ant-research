"""Discovery-only controls for the conjectured reduced-curvature upper budget.
Not a proof, nor evidence for highway attraction. Records explicit violations.
"""
import random,json
D=[(0,1),(1,0),(0,-1),(-1,0)]
def check(seed,steps):
 B=set(seed);x=y=h=0;st=[];cur=0;high=(0,0);low=(0,0)
 for t in range(steps):
  q=x,y;a=-1 if q in B else 1
  if q in B:B.remove(q)
  else:B.add(q)
  if st and st[-1][0]==a:
   st[-1][1]+=1;cur+=a
   if st[-1][1]==4:st.pop();cur-=4*a
  else:st.append([a,1]);cur+=a
  if cur>high[0]:high=(cur,t+1)
  if cur<low[0]:low=(cur,t+1)
  h=(h+a)%4;dx,dy=D[h];x+=dx;y+=dy
  if cur>len(seed)+3:return {'seed':sorted(seed),'m':len(seed),'time':t+1,'curvature':cur,'max':high,'failed':True}
 return {'m':len(seed),'steps':steps,'max':high,'min':low,'failed':False}
random.seed(8823)
out=[check(set(),100000)]
for n in range(100):
 seed={(x,y) for x in range(-5,6) for y in range(-5,6) if random.random()<.3}
 r=check(seed,20000);out.append(r)
 if r['failed']: print(json.dumps(r));break
else:print('NO VIOLATION',out[0],max(r['max'][0]-r['m'] for r in out))
open('/workspace/shared/langton/core_periodicity_new/core_signed_curvature_controls.json','w').write(json.dumps(out,indent=2))
