"""Complete finite five-cell continuation, including both old-a endpoint returns.
The old prefix is an audited dependency; every new local read and eternal tail
is checked against the full retained field with two unbounded parameters.
"""
import sys,json,hashlib
from pathlib import Path
R=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'scattering/fixed_core_rectangle'))
from bivariate import A,infinite_tail
sys.path.insert(0,str(R/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,plan
OFF={15:10,45:13,72:13};E={15:(64,59),45:(58,65),72:(36,65)}
M=(1,0,100);J=(0,1,200)
def c(v):return (0,0,v)
def main(r,bindings_only=False):
 off=OFF[r];K=A.add(J,c(off));N=A.add(M,K)
 def nn(a,b):return A.add(A.scale(N,a),c(b))
 def jj(a,b):return A.add(A.scale(J,a),c(b))
 O=(A.add(A.scale(M,-2),c(-62)),A.add(A.scale(M,2),c(2)))
 oldpath=R/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'
 I=json.loads((HERE/'strip_interface.json').read_text());assert I['source_template_sha256']==hashlib.sha256(oldpath.read_bytes()).hexdigest() and I['pre_core_read_upper']=={'u':58,'z':71}
 assert r in I['fresh_phases']
 old=json.loads(oldpath.read_text());field=A.Field([(nn(-2,-33),nn(-2,-14)),(nn(-2,-33),nn(2,41))])
 p=A.point(0,0);h=0;prefix=c(0)
 for i,s in enumerate(old['segments'][:7]):
  assert s['word'] and set(s['word'])<={'R','L'}
  _,odd,end,eh=A.word_data(s['word'],h)
  if s['type']=='finite':field.add_points(A.translate_local(q,p,0) for q in odd);p=A.translate_local(end,p,0);prefix=A.add(prefix,c(len(s['word'])))
  else:
   count=A.add(A.scale(N,s['count'][0]),c(s['count'][1]));assert len(s['word'])==104 and eh==h and A.nonneg(A.sub(count,A.ONE))
   field.add_rays([A.translate_local(q,p,0) for q in odd],end,count,'old'+str(i));p=A.padd(p,(A.scale(count,end[0]),A.scale(count,end[1])));prefix=A.add(prefix,A.scale(count,104))
  h=eh
 assert p==(nn(-2,-62),nn(2,2)) and h==2
 assert old['segments'][7]['word']==W and old['segments'][7]['count']==[1,7]
 _,odd,end,eh=A.word_data(W,h);assert end==(2,-2) and eh==h
 field.add_rays([A.translate_local(q,p,0) for q in odd],end,K,'return_SE');p=A.padd(p,(A.scale(K,2),A.scale(K,-2)))
 prefix=A.add(prefix,A.scale(K,104));assert p==O
 assert prefix==A.add(A.sub(A.scale(N,416),A.scale(M,104)),c(122376))
 # Normalize the complete old finite field, preserving EVERY point and ray.
 field.points={A.psub(q,O) for q in field.points}
 field.rays=[(A.psub(b,O),d,count,label) for b,d,count,label in field.rays]
 initial_source_points=len(field.points);initial_source_rays=len(field.rays)
 Q,_,_,_=plan(W,(0,0),2);core=A.point(*Q[r]);e=E[r]
 opposite=(jj(2,e[0]),jj(2,e[1]))
 remote_c=(jj(2,e[0]),A.add(A.add(A.scale(M,-4),A.scale(K,-2)),c(-16)))
 # These added corners were already present but unread on the inherited prefix.
 actual_c_u=A.sub(A.add(O[0],remote_c[0]),A.add(O[1],remote_c[1]))
 actual_d_z=A.add(A.add(O[0],opposite[0]),A.add(O[1],opposite[1]))
 assert A.negative(A.sub(c(58),actual_c_u)) and A.negative(A.sub(c(71),actual_d_z))
 assert A.add(O[1],opposite[1])==nn(2,41) # a and d share their required row
 field.add_points([core,opposite,remote_c])
 model=next(v for v in json.loads((HERE/'parallel_model_certificate.json').read_text())['records'] if v['phase']==r)
 assert model['opposite_exceptional_base']==list(e) and model['opposite_exceptional_parity']==[0,1]
 phase=model['word_phase'];partial,_,ref,rh=plan(W[phase:],tuple(model['local_pose'][0]),model['local_pose'][1]);assert rh==1 and (ref[0]+2,ref[1]+8)==e
 assert max(model['source_z_bounds'][1],max(x+y for x,y in partial))<sum(e)+800
 reads,_,drift,_=plan(W,(0,0),1);assert drift==(2,2)
 contact=[]
 for i,q in enumerate(reads):
  delta=(e[0]-ref[0]-q[0],e[1]-ref[1]-q[1])
  if delta[0]==delta[1] and delta[0]%2==0:
   shift=delta[0]//2;assert 200+shift>=0;contact.append(104*shift+i)
 assert min(contact)==72
 first_d_time=jj(104,model['local_capture']+104-phase+72)
 if bindings_only:
  binding=dict(status='all inherited source and first-contact bindings passed',phase=r,first_d_read_source_time=first_d_time,first_d_phase=72,old_template_sha256=hashlib.sha256(oldpath.read_bytes()).hexdigest())
  (HERE/f'full_opposite_bindings_r{r}.json').write_text(json.dumps(binding,indent=2)+'\n');print(json.dumps(binding));return
 templatepath=HERE/f'full_opposite_template_r{r}.json';T=json.loads(templatepath.read_text());assert T['phase']==r and T['offset']==off
 for key in A.STATS:A.STATS[key]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear()
 p=A.point(0,0);h=2;elapsed=c(0);records=[]
 standard={W[j:]+W[:j] for j in range(104)}
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'};data=A.word_data(word,h)
  if s['type']=='finite':p=A.apply_finite(field,data,p,0,'new_finite'+str(i));elapsed=A.add(elapsed,c(len(word)))
  else:
   count=jj(*s['count']);assert word in standard and data[3]==h and A.nonneg(A.sub(count,A.ONE))
   p=A.apply_periods(field,data,p,0,count,'new_period'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[p,h]));print(json.dumps(records[-1]),flush=True)
 tw=T['infinite_tail_word'];assert tw in standard;td=A.word_data(tw,h);assert td[3]==h
 assert td[2]==((-2,-2) if r==72 else (-2,2))
 tail=infinite_tail(field,td,p)
 # The remaining initial c is never read, including the entire final tail.
 for q in A.READ_POINTS:assert A.no_point_collision(q,remote_c)
 for b,d,count in A.READ_RAYS:assert not A.ray_membership(remote_c,b,d,count)
 for q in td[0]:
  b=A.translate_local(q,p,0);v=A.line_coordinate(A.psub(remote_c,b),td[2]);assert v is None or A.negative(v)
 actual_pose=A.padd(O,p);total=A.add(prefix,elapsed)
 out=dict(status='exact complete finite five-cell family with eternal standard tail',phase=r,domain=f'm>=100,k>=200,n=m+k+{off}',variables='u=m-100>=0,v=k-200>=0',initial_source_points=initial_source_points,initial_source_rays=initial_source_rays,first_d_read_source_time=first_d_time,first_d_phase=72,source_capture_time=elapsed,source_capture_pose=[p,h],total_capture_time=total,total_capture_pose=[actual_pose,h],tail=tail,tail_phase=next(j for j in range(104) if tw==W[j:]+W[:j]),remote_c_never_read=True,statistics=A.STATS.copy(),records=records,old_template_sha256=hashlib.sha256(oldpath.read_bytes()).hexdigest(),new_template_sha256=hashlib.sha256(templatepath.read_bytes()).hexdigest())
 (HERE/f'full_opposite_certificate_r{r}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main(int(sys.argv[1]),'--bindings-only' in sys.argv)
