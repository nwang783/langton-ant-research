"""Complete old-history transport and the phase61 recurrence interface."""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];SRC=HERE.parent/'ordinary_reverse_interface'
sys.path.insert(0,str(HERE.parent/'fixed_core_rectangle'));from bivariate import A
from ant_exact import P,D,W,plan,step,canonical_source
C=lambda v:(0,0,v);N=(1,0,100);lin=lambda a,b:A.add(A.scale(N,a),C(b))
def rot(p,j):
 for _ in range(j%4):p=(p[1],-p[0])
 return p

def main():
 R=json.loads((HERE/'certificate.json').read_text());assert R['whole_future_bounds']=={'u_lower':-108,'z_upper':65};assert R['capture_time']==list(lin(520,263262)) and R['capture_pose']==[[list(lin(-2,-17)),list(lin(-2,-73))],2] and R['tail_phase']==0
 old=json.loads((SRC/'certificate_r61.json').read_text());assert hashlib.sha256((SRC/'certificate_r61.json').read_bytes()).hexdigest()==R['source_certificate_sha256'];tp=SRC/'template_r61.json';T=json.loads(tp.read_text());assert hashlib.sha256(tp.read_bytes()).hexdigest()==old['template_sha256']
 base=A.point(0,0);h=2;zs=[]
 for s in T['segments']:
  word=s['word'];assert word and set(word)<={'R','L'} and s['type'] in ['finite','periods'];qs,_,d,eh=plan(word,(0,0),h);count=C(1) if s['type']=='finite' else lin(*s['count'])
  if s['type']=='periods':assert len(word)==104 and eh==h
  for q in qs:
   p=A.padd(base,A.point(*q));z=A.add(*p);last=A.add(z,A.scale(A.sub(count,C(1)),sum(d)));assert z[:2]==last[:2]==(0,0);zs.extend([z[2],last[2]])
  base=tuple(A.add(v,A.scale(count,dv)) for v,dv in zip(base,d));h=eh
 assert base==A.point(-36,-19) and h==3 and (min(zs),max(zs))==(-109,61)
 B,p,h=canonical_source(0,100);core={tuple(v+w for v,w in zip((-36,-19),rot((x-p[0],y-p[1]),3-h))) for x,y in B}
 blank=set();p=(0,0);h=0;blank_reads=[]
 for _ in range(9977):blank_reads.append(p);p,h,ch=step(blank,p,h)
 E=blank^{tuple(v+w for v,w in zip(p,rot(q,1))) for q in P};assert p==(-15,10) and h==3
 assert max(-sum(q)-5 for q in E)==16 and (min(x-y+25 for x,y in E),max(x-y+25 for x,y in E))==(-9,73)
 omitted_u=max(x-y for x,y in D)-4*43;assert omitted_u==-163
 old_E_u=16-4*100;assert old_E_u==-384 and max(omitted_u,old_E_u)<-160<-108
 archive_z_lower=min(min(zs),min(map(sum,P)),min(map(sum,D)),min(map(sum,core)),-9);assert archive_z_lower==-109
 # The three input sites are inert through the literal blank transient.
 blank_z_lower=min(map(sum,blank_reads));blank_u_lower=min(x-y for x,y in blank_reads);assert blank_z_lower==-21 and blank_u_lower==-34
 assert -14-4*100<blank_z_lower and -71<blank_u_lower and -4*100-120<blank_u_lower
 # The SW phase72 contact is forced by the shared source y of q2 and q3.
 p0,h0=plan((W[100:]+W[:100])[:4],(-36,-19),3)[2:];b72=plan(W[:72],p0,h0)[2];assert b72==(-40,-27) and h0==3
 assert (b72[0]-2*7,b72[1]-2*7)==(-54,-41)
 out=dict(status='exact all-age complete-history interface for phase61',domain='m>=100,n>=100; recurrence conclusion takes m fixed then remote coordinates divergent',source_future={'u_lower':-108,'z_upper':65},actual_future={'u_upper':40,'z_upper_m_constant':[-4,103]},capture_time_m_n_constant=[104,520,273239],capture_pose_x_m_n_constant=[-2,-2,-88],capture_pose_y_m_n_constant=[-2,2,27],capture_heading=3,capture_phase=0,capture_drift=[-2,-2],old_two_bit_archive_z_lower=-109,omitted_deposit_u_upper=-163,old_E_u_upper_at_m100=-384,remaining_corner_guards={'NW_source':'u=-2n-54-y -> -infinity','NE_source':'z=2n-5+y -> +infinity'},certificate_sha256=hashlib.sha256((HERE/'certificate.json').read_bytes()).hexdigest())
 (HERE/'interface.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
