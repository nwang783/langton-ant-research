"""Archive geometry and gap-based mass-five coupling for phase28."""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent;OLD=HERE.parent/'blank_return_cap';SRC=HERE.parent/'ordinary_reverse_interface'
sys.path.insert(0,str(HERE.parent/'fixed_core_rectangle'));from bivariate import A
from ant_exact import W,plan,canonical_source
C=lambda v:(0,0,v);M=(1,0,100);K=(0,1,100)
def lin(a,b,c):return A.add(A.add(A.scale(M,a),A.scale(K,b)),C(c))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 R=json.loads((HERE/'certificate.json').read_text());assert R['whole_future_bounds']=={'u_lower':-84,'z_upper':35};assert R['capture_time']==list(lin(416,416,173038)) and R['capture_pose']==[[[0,0,25],[0,0,-61]],2] and R['tail_phase']==0
 assert sha(OLD/'r28_complete_certificate.json')=='97ed7332cd4d1883d0bf168baa6946a37429fb49fa8e5e59f4d7376995f9ed0f';old=json.loads((OLD/'r28_complete_certificate.json').read_text());tp=OLD/'r28_complete_template.json';assert sha(tp)==old['template_sha256']=='7e38c882ba3eb9c21b8376f503e0c500d0c41f944d5ec697273fb6d5ef1f4ce0';T=json.loads(tp.read_text());assert T['segments']==json.loads((HERE/'template.json').read_text())['segments'][:9]
 base=A.point(0,0);h=0;us=[];zupper=-10**9
 for index,seg in enumerate(T['segments']):
  if index==3:
   assert base==(lin(-2,0,-21),lin(-2,0,6)) and h==3 and seg['word']==W[102:]+W[:102]
  word=seg['word'];assert word and set(word)<={'R','L'} and seg['type'] in ['finite','periods'];qs,_,d,eh=plan(word,(0,0),h);n=C(1) if seg['type']=='finite' else lin(*seg['count_mk'])
  if seg['type']=='periods':assert len(word)==104 and eh==h and d[0]==d[1]
  for q in qs:
   p=A.padd(base,A.point(*q));last=tuple(A.add(v,A.scale(A.sub(n,C(1)),di)) for v,di in zip(p,d))
   for v in [p,last]:
    u=A.sub(*v);z=A.add(*v);assert u[:2]==(0,0);us.append(u[2]);assert z[0]<=0 and z[1]<=0;zupper=max(zupper,z[2])
  base=tuple(A.add(v,A.scale(n,di)) for v,di in zip(base,d));h=eh
 assert base==(lin(-2,0,45),lin(-2,0,-26)) and h==3 and T['infinite_tail_word']==W[99:]+W[:99]
 B,p0,h0=canonical_source(0,99);assert h0==h;core_u=[71+(x-p0[0])-(y-p0[1]) for x,y in B];archive_lower=min(us+core_u+[-27,-21]);archive_upper=max(us+core_u+[-27,-21]);assert archive_lower==-84 and archive_upper==80 and zupper==35
 # The old parent's entire SE tail also obeys the same exterior wedge.
 qs,_,d,eh=plan(T['infinite_tail_word'],(0,0),h);assert d==(2,-2) and eh==h
 for q in qs:
  v=A.padd(base,A.point(*q));assert A.nonneg(A.add(A.sub(*v),C(84))) and A.nonneg(A.sub(C(35),A.add(*v)))
 # All possible exceptional contacts have these exact rays.
 q72=plan(T['segments'][3]['word'][:74],(-21,6),3)[2];assert q72==(-24,-3);assert (-24-2,-3-2)==(-26,-5)
 c72=plan(T['infinite_tail_word'][:77],(45,-26),3)[2];assert c72==(53,-31);assert (53-26,-31+26)==(27,-5)
 assert list(A.add(A.add(lin(104,0,16313),A.scale(A.add(K,C(1)),104)),C(74)))==R['first_contacts']['Q']
 assert list(A.add(A.add(lin(312,208,111801),A.scale(A.sub(K,C(13)),104)),C(77)))==R['first_contacts']['C']
 # No absolute-coordinate sign is assumed for the other row: only its gap.
 # A=(Q.x,Q.y+g1), D=(C.x,Q.y+g2), g1,g2 -> +infinity.
 # Q.u=-21 and C.x+Q.y=-4m+22, hence A.u=-21-g1,D.z=-4m+22+g2.
 assert -26-(-5)==-21 and 27+(-5)==22
 out=dict(status='exact complete-history archive and recurrence interface for initial-SW phase28',domain='all independent m,k>=100 for the three-cell theorem; m fixed and all exposed axial gaps divergent for recurrence',capture_time_m_k_constant=[416,416,173038],capture_pose=[[25,-61],2],capture_phase=0,whole_future_bounds=R['whole_future_bounds'],old_two_bit_archive_u_bounds=[archive_lower,archive_upper],old_two_bit_whole_future={'u_lower':-84,'z_upper':35},first_remote_Q='(-2m-2k-26,-2m-2k-5)',second_exceptional_C='(-2m+2k+27,-2m-2k-5)',remaining_corner_guards={'NW_A':'u=-21-g1 -> -infinity, with g1=A.y-Q.y -> +infinity','NE_D':'z=-4m+22+g2 -> +infinity, with g2=D.y-Q.y -> +infinity and m fixed'},old_complete_certificate_sha256=sha(OLD/'r28_complete_certificate.json'),certificate_sha256=sha(HERE/'certificate.json'))
 (HERE/'interface.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
