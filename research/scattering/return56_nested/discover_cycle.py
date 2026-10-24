"""Discovery only: fourth and fifth corners after the fixed phase56 local return."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent;SRC=HERE.parent/'opposite_cycle_interfaces';sys.path.insert(0,str(SRC));from discover_return56 import model
from ant_exact import W,PHASES,step,certify_period
from crossing import tail

def main(n):
 p=n+38;F,pos,h=model(n,p);q4=(2*n+98,-2*n-30);q5=(-2*n-19,2*n+25)
 F.changes.symmetric_difference_update([q4,q5]);B=set(F.changes)
 for base,d,lo,hi in F.rays:
  assert lo==0 and hi is None
  for j in range(200):B.symmetric_difference_update({(base[0]+j*d[0],base[1]+j*d[1])})
  assert base[0]-base[1]+200*(d[0]-d[1])<-250
 w=[];umin=umax=pos[0]-pos[1];zmin=zmax=sum(pos);hits={};lowz=[]
 for t in range(1000000):
  u=pos[0]-pos[1];z=sum(pos);umin=min(umin,u);umax=max(umax,u);zmin=min(zmin,z);zmax=max(zmax,z)
  if u<-250:lowz.append(z)
  for name,q in [('q4',q4),('q5',q5)]:
   if pos==q and name not in hits:hits[name]=t
  pos,h,ch=step(B,pos,h);w.append(ch)
  if t>=100000 and (t+1)%104==0:
   tw=''.join(w[-104:])
   if tw in PHASES and ''.join(w[-312:])==tw*3:
    cert=certify_period(B,pos,h,tw)
    if cert:cert['phase']=next(j for j in range(104) if tw==W[j:]+W[:j])
    if cert:
     file=f'return56_corner_n{n}.txt.gz'
     with gzip.open(HERE/file,'wt') as f:f.write(''.join(w))
     out=dict(status='complete finite kernel discovery only',n=n,p=p,capture=t+1,pose=[pos,h],tail=cert,u_bounds=[umin,umax],z_bounds=[zmin,zmax],low_u_z_bounds=[min(lowz),max(lowz)] if lowz else None,first_hits=hits,word_file=file);break
 else:out=dict(status='limit',n=n,time=len(w),pose=[pos,h],u_bounds=[umin,umax],z_bounds=[zmin,zmax],first_hits=hits)
 (HERE/f'return56_corner_n{n}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main(int(sys.argv[1]))
