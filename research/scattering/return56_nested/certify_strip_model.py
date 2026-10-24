"""Complete phase56 packet identity on -100<=z<=100, all n,p>=100."""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];SRC=HERE.parent/'opposite_cycle_interfaces'
sys.path.insert(0,str(HERE.parent/'fixed_core_rectangle'));from bivariate import A
from ant_exact import W,P,D,plan
C=lambda v:(0,0,v);N=(1,0,100);M=(0,1,100)
def linear(a,b,c):return A.add(A.add(A.scale(N,a),A.scale(M,b)),C(c))
def geometry():
 cp=SRC/'backward_certificate_r56.json';cert=json.loads(cp.read_text());tp=SRC/'template_r56.json';assert cert['template_sha256']==hashlib.sha256(tp.read_bytes()).hexdigest();T=json.loads(tp.read_text());points=[tuple(tuple(v) for v in q) for q in cert['initial']];rays=[];base=A.point(0,0);h=2
 for seg in T['segments']:
  assert seg['type'] in ['finite','periods'];w=seg['word'];assert w and set(w)<={'R','L'};data=A.word_data(w,h)
  odd=[A.translate_local(q,base,0) for q in data[1]]
  if seg['type']=='finite':points.extend(odd);base=A.padd(base,A.point(*data[2]))
  else:
   count=linear(*seg['count_np']);assert len(w)==104 and data[3]==h and A.nonneg(A.sub(count,A.ONE));rays.extend((q,data[2],count) for q in odd);base=A.padd(base,(A.scale(count,data[2][0]),A.scale(count,data[2][1])))
  h=data[3]
 assert [list(v) for v in base]==cert['capture_pose'][0] and h==cert['capture_pose'][1]==0 and cert['tail_phase']==0 and base==A.point(2,24)
 return cert,points,rays

def main():
 cert,points,rays=geometry();B=set();inside=outside=0
 def toggle(q):
  if q in B:B.remove(q)
  else:B.add(q)
 for q in points:
  u=A.sub(q[0],q[1]);z=A.add(q[0],q[1]);assert u[:2]==(0,0)
  if A.negative(A.sub(z,C(-100))) or A.negative(A.sub(C(100),z)):outside+=1;continue
  assert z[:2]==(0,0) and -100<=z[2]<=100;assert all(v[:2]==(0,0) for v in q);toggle(tuple(v[2] for v in q));inside+=1
 for q,d,count in rays:
  assert d in [(2,2),(-2,-2)];u=A.sub(q[0],q[1]);z=A.add(q[0],q[1]);assert u[:2]==(0,0) and all(v%4==0 for v in z[:2]);end=A.add(z,A.scale(A.sub(count,A.ONE),sum(d)));lo=A.minimum(z,end);hi=A.maximum(z,end)
  if A.negative(A.sub(hi,C(-100))) or A.negative(A.sub(C(100),lo)):continue
  if A.nonneg(A.sub(C(-100),lo)):low=-100
  else:assert lo[:2]==(0,0);low=lo[2]
  if A.nonneg(A.sub(hi,C(100))):high=100
  else:assert hi[:2]==(0,0);high=hi[2]
  assert -100<=low<=high<=100
  for zz in range(low,high+1):
   if (zz-z[2])%4==0:
    assert (zz+u[2])%2==0;toggle(((zz+u[2])//2,(zz-u[2])//2))
 digest=hashlib.sha256(json.dumps(sorted(B),separators=(',',':')).encode()).hexdigest();out=dict(status='exact complete packet equality throughout the entire z strip',domain='all independent n,p>=100',strip_z=[-100,100],packet_cells=sorted(B),packet_mass=len(B),packet_sha256=digest,source_certificate_sha256=hashlib.sha256((SRC/'backward_certificate_r56.json').read_bytes()).hexdigest(),source_template_sha256=cert['template_sha256'],fixed_point_terms=inside,uniformly_outside_point_terms=outside,ray_terms=len(rays),scope='The unchanged canonical infinite old rail is retained separately; only the finite packet XOR is clipped.')
 (HERE/'strip_model.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='packet_cells'},indent=2));return B
if __name__=='__main__':main()
