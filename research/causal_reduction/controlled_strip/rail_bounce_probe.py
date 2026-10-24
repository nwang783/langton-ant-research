"""Finite rail controls for a regenerative half-plane builder target."""
import json,sys
D=((0,1),(1,0),(0,-1),(-1,0))
n=int(sys.argv[1]) if len(sys.argv)>1 else 32; B={(x,-1) for x in range(2*n)};out=[]
def runs(B):
 rows={}
 for x,y in sorted(B,key=lambda p:(p[1],p[0])):
  a=rows.setdefault(y,[])
  if a and a[-1][1]+1==x:a[-1][1]=x
  else:a.append([x,x])
 return rows
for k in range(12):
 x=y=0;h=1;w=[];poses=[]
 while x>=0 and len(w)<200000:
  poses.append((x,y,h));p=x,y;b=p in B;w.append('L' if b else 'R')
  if b:B.remove(p)
  else:B.add(p)
  h=(h+(-1 if b else 1))%4;dx,dy=D[h];x+=dx;y+=dy
 rec=dict(k=k,status='LEFT' if x<0 else 'UNKNOWN',exit=[x,y,h],steps=len(w),word=''.join(w),poses=poses,field=sorted(B),rows=runs(B))
 out.append(rec);print(k,rec['exit'],len(w),len(B),rec['rows'],flush=True)
 if x>=0:break
json.dump(dict(n=n,records=out),open(f'/workspace/shared/langton/causal_reduction/controlled_strip/rail_bounce_n{n}.json','w'))
