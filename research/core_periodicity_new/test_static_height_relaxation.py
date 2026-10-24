import numpy as np,json,sys
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
D=[(0,1),(1,0),(0,-1),(-1,0)]
def check(w,b):
 x=y=h=0;v={}
 for a in w:
  v[x,y]=v.get((x,y),0)+(1 if a=='R' else -1)
  h=(h+(1 if a=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
 X=[(x,y) for x in range(-b,b+1) for y in range(-b,b+1)]
 Q=[(x,y) for x in range(-b,b+2) for y in range(-b,b+2)]
 ii={q:i for i,q in enumerate(Q)};A=lil_matrix((len(Q),len(X)))
 for j,(x,y) in enumerate(X):
  s=1 if (x+y)%2 else -1
  for q in [(x,y),(x+1,y),(x,y+1),(x+1,y+1)]:A[ii[q],j]=s
 if not set(v)<=set(Q):return {'error':'box too small'}
 vv=np.array([v.get(q,0) for q in Q],float)
 res=milp(np.ones(len(X)),integrality=np.ones(len(X)),bounds=Bounds(0,np.inf),constraints=LinearConstraint(A.tocsr(),-vv,1-vv),options={'time_limit':20})
 out={'word':w,'box':b,'status':int(res.status),'message':res.message}
 if res.x is not None:
  kk=np.rint(res.x).astype(int);bb=vv+A@kk
  assert min(bb)>=0 and max(bb)<=1 and np.max(abs(bb-np.rint(bb)))<1e-5
  out['K']=[[*q,int(kk[j])] for j,q in enumerate(X) if kk[j]]
  out['B']=[q for i,q in enumerate(Q) if round(bb[i])]
  out['sumK']=sum(kk).item()
 return out
if __name__=='__main__':
 w=sys.argv[1] if len(sys.argv)>1 else 'RRRLRRR'
 out=[]
 for b in range(2,7):
  z=check(w,b);print(json.dumps(z),flush=True);out.append(z)
  if 'K' in z:break
 open('/workspace/shared/langton/core_periodicity_new/static_height_relaxation.json','w').write(json.dumps(out,indent=2))
