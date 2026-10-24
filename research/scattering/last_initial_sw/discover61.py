"""Discovery only: next adjacent corner after initial-SW core phase61."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];SRC=HERE.parent/'ordinary_reverse_interface'
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'));from ant_exact import W,PHASES,plan,step,canonical_source,certify_period

def main(n):
 old=json.loads((SRC/'certificate_r61.json').read_text());q1=plan(W,(0,0),2)[0][61];q2=tuple(a*n+b for a,b in old['second_marker_affine']);p,h=old['capture_pose'];assert all(v[0]==0 for v in p);p=tuple(v[1] for v in p);phase=old['tail_phase'];p0,h0=plan((W[phase:]+W[:phase])[:(-phase)%104],p,h)[2:];q30=plan(W[:72],p0,h0)[2];assert (q30[1]-q2[1])%2==0;epoch=(q30[1]-q2[1])//2;q3=(q30[0]-2*epoch,q30[1]-2*epoch);assert q3[1]==q2[1]
 B,p,h=canonical_source(200,0);B.symmetric_difference_update([q1,q2,q3]);w=[];bounds=[0,0,0,0];hits={}
 for t in range(1000000):
  u=p[0]-p[1];z=sum(p);bounds=[min(bounds[0],u),max(bounds[1],u),min(bounds[2],z),max(bounds[3],z)]
  for name,q in [('q2',q2),('q3',q3)]:
   if p==q and name not in hits:hits[name]=t
  p,h,c=step(B,p,h);w.append(c)
  if 'q3' in hits and t>=hits['q3']+1000 and (t+1)%104==0:
   tw=''.join(w[-104:])
   if tw in PHASES and ''.join(w[-312:])==tw*3:
    cert=certify_period(B,p,h,tw)
    if cert:
     phase=next(i for i in range(104) if tw==W[i:]+W[:i]);file=f'r61_n{n}.txt.gz'
     with gzip.open(HERE/file,'wt') as f:f.write(''.join(w))
     out=dict(status='finite-kernel discovery only',n=n,inputs=[q1,q2,q3],q3_ray_epoch=epoch,capture=t+1,pose=[p,h],phase=phase,tail=cert,bounds_u_z=bounds,first_hits=hits,word_file=file);break
 else:out=dict(status='limit',n=n,inputs=[q1,q2,q3],time=len(w),pose=[p,h],bounds_u_z=bounds,first_hits=hits)
 (HERE/f'r61_n{n}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main(int(sys.argv[1]))
