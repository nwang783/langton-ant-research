import json,random
D=[(0,1),(1,0),(0,-1),(-1,0)]
def static(B,p,h):
 start=(p,h); out=[]
 while True:
  out.append((p,h)); h=(h+(-1 if p in B else 1))%4;d=D[h];p=(p[0]+d[0],p[1]+d[1])
  if (p,h)==start: return out
  if len(out)>100000:raise RuntimeError('nonfinite')
def measure(B,p,h):
 C=static(B,p,h);curv=sum(-1 if x in B else 1 for x,h in C)
 # area based cell-center loop
 area=sum(C[i][0][0]*C[(i+1)%len(C)][0][1]-C[(i+1)%len(C)][0][0]*C[i][0][1] for i in range(len(C)))
 return len(C),curv,area
B=set();p=(0,0);h=0
out=[]
for t in range(100):
 out.append((t,len(B),p,h,*measure(B,p,h)))
 h=(h+(-1 if p in B else 1))%4; B.symmetric_difference_update([p]);d=D[h];p=(p[0]+d[0],p[1]+d[1])
print(json.dumps(out))
