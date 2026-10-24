"""Whole-history bounds and corner-parity obstruction for cap60 and cap70."""
import json,hashlib,gzip,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,P,plan,multiple,step
SRC=HERE.parent/'ordinary_reverse_interface';CAP=HERE.parent/'blank_return_cap'
C=lambda a:(0,0,a);M=(1,0,100);K=(0,1,100)
add=lambda a,b:tuple(x+y for x,y in zip(a,b));scale=lambda a,k:tuple(x*k for x in a)
def plus(p,q):return add(p[0],q[0]),add(p[1],q[1])
def off(p,q):return plus(p,(C(q[0]),C(q[1])))
def coord(p,sgn):return add(p[0],scale(p[1],sgn))
def main():
 for path,digest in [(SRC/'manifest.json','2cd64e957de70ed25e5ab7bb58ac87ce36765cfc6a1c234c05d65441aa8550a1'),(CAP/'manifest.json','2827291464278a15841e21a0430de38d18f990f01827f7adb0d43cfb5dbe9237')]:assert hashlib.sha256(path.read_bytes()).hexdigest()==digest
 sm=json.loads((SRC/'manifest.json').read_text())['files'];cm=json.loads((CAP/'manifest.json').read_text())['files']
 for name in ['fixed_caps.json','bridge.json']:assert hashlib.sha256((CAP/name).read_bytes()).hexdigest()==cm[name]
 caps=json.loads((CAP/'fixed_caps.json').read_text())['rows'];bridges=json.loads((CAP/'bridge.json').read_text())['rows']
 rows=[]
 for r in [60,70]:
  certpath=SRC/f'certificate_r{r}.json';assert hashlib.sha256(certpath.read_bytes()).hexdigest()==sm[certpath.name]
  cert=json.loads(certpath.read_text());Tfile=SRC/f'template_r{r}.json';assert hashlib.sha256(Tfile.read_bytes()).hexdigest()==cert['template_sha256'];T=json.loads(Tfile.read_text())
  cap=next(x for x in caps if x['phase']==r);bridge=next(x for x in bridges if x['phase']==r);assert bridge['permanent_transfer'] and bridge['packet_certificate_sha256']==hashlib.sha256(certpath.read_bytes()).hexdigest()
  p=(add(scale(M,-2),C(-15)),add(scale(M,-2),C(10)));h=3;us=[];zu=[];elapsed=add(scale(M,104),C(9977))
  def collect(q):
   u=coord(q,-1);z=coord(q,1);assert u[:2]==(0,0);us.append(u[2]);assert z[0]<=0 and z[1]<=0;zu.append(z[2])
  def segment(word,count=None):
   nonlocal p,h,elapsed
   assert word and set(word)<={'R','L'};qs,_,e,eh=plan(word,(0,0),h)
   if count is None:
    for q in qs:collect(off(p,q))
    p=off(p,e);elapsed=add(elapsed,C(len(word)))
   else:
    assert len(word)==104 and eh==h and all(x>=0 for x in add(count,C(-1)))
    for q in qs:
     b=off(p,q);collect(b);collect(plus(b,(scale(add(count,C(-1)),e[0]),scale(add(count,C(-1)),e[1]))))
    p=plus(p,(scale(count,e[0]),scale(count,e[1])));elapsed=add(elapsed,scale(count,104))
   h=eh
  for s in T['segments']:
   assert s['type'] in ['finite','periods'];segment(s['word'],None if s['type']=='finite' else add(scale(K,s['count'][0]),C(s['count'][1])))
  assert cert['tail_phase']==0 and h==1
  segment(W,add(add(M,K),C(-20)))
  assert [[p[0][2],p[1][2]],h]==cap['start'] and p[0][:2]==p[1][:2]==(0,0)
  a,b,c=bridge['cap_entry_time_m_k_constant'];assert elapsed==add(add(scale(M,a),scale(K,b)),C(c))
  word=gzip.open(CAP/f'word_r{r}.txt.gz','rt').read();assert len(word)==cap['capture'] and hashlib.sha256(word.encode()).hexdigest()==cap['word_sha256'];segment(word)
  assert [[p[0][2],p[1][2]],h]==cap['pose'];phase=cap['tail_phase'];tw=W[phase:]+W[:phase];skip=(104-phase)%104
  if skip:segment(tw[:skip])
  p0=(p[0][2],p[1][2]);assert p[0][:2]==p[1][:2]==(0,0);qs,_,end,eh=plan(W,p0,h);dr=tuple(end[i]-p0[i] for i in range(2));assert dr==tuple(cap['drift']) and eh==h
  fresh=[]
  for i,q in enumerate(qs):
   if not any((k:=multiple((v[0]-q[0],v[1]-q[1]),dr)) is not None and (k>0 or k==0 and j<i) for j,v in enumerate(qs)):fresh.append(i)
  assert fresh==[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89]
  qpar=[(-15+cert['second_marker_affine'][1][1])%2,(10-cert['second_marker_affine'][0][1])%2];assert sum(qpar)%2==1
  target=[qpar[0],1-qpar[1]] if r==60 else [1-qpar[0],1-qpar[1]]
  allowed=[i for i in fresh if sum(qs[i])%2==sum(target)%2];assert allowed==[14,28,32,38,46,56,60,62,70,72]
  raypar=[v%2 for v in qs[72]];assert raypar!=target
  # Phase-zero standard core, with every original blank-history cell included.
  rot={0:lambda p:(-p[0],-p[1]),1:lambda p:(-p[1],p[0])}[h]
  core=[(p0[0]+rot(q)[0],p0[1]+rot(q)[1]) for q in P]
  prefixu=[min([-34]+us),max([48]+us)];prefixz=max([35]+zu)
  archive_u_lower=min(prefixu[0],min(x-y for x,y in core));archive_z_upper=max(prefixz,max(x+y for x,y in core))
  tailu=[x-y for x,y in qs];tailz=[x+y for x,y in qs]
  if r==60:assert dr==(-2,2);future=dict(u_upper=max(prefixu[1],max(tailu)),z_upper=max(prefixz,max(tailz)),cross_u_bounds=prefixu,cross_tail_z_bounds=[min(tailz),max(tailz)])
  else:assert dr==(2,2);future=dict(u_bounds=[min(prefixu[0],min(tailu)),max(prefixu[1],max(tailu))])
  assert (archive_u_lower,archive_z_upper,prefixu,prefixz)=={60:(-96,41,[-96,48],41),70:(-98,59,[-98,60],59)}[r]
  rows.append(dict(phase=r,first_remote_parity=qpar,remaining_corner_parity=target,exceptional_ray_parity=raypar,favorable_phases=allowed,phase_zero_pose=[p0,h],complete_archive_u_lower=archive_u_lower,complete_archive_z_upper=archive_z_upper,finite_prefix_u_bounds=prefixu,finite_prefix_z_upper=prefixz,whole_future=future))
 # Independently bind the original blank prefix support bounds used above.
 blank=set();p=(0,0);h=0;bu=[];bz=[]
 for _ in range(9977):bu.append(p[0]-p[1]);bz.append(sum(p));p,h,_=step(blank,p,h)
 assert p==(-15,10) and h==3 and [min(bu),max(bu)]==[-34,48] and max(bz)==35
 qs,_,_,_=plan(W,p,h);assert min(x-y for x,y in qs)>=-34 and max(x-y for x,y in qs)<=48 and max(map(sum,qs))<=35
 out=dict(status='exact complete-history cap60/cap70 interfaces',domain='all independent m,k>=100',rows=rows,scope='Retained-core recurrence reduction uses fixed m and k tending to infinity.')
 (HERE/'cap_interfaces.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
