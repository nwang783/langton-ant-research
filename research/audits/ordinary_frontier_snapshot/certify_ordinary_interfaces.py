"""Full ordinary one-bit replay, then uniform q-parent archive coupling bounds.
The q-parent's already audited all-n prefix theorem is an explicit dependency.
No new simulation cutoff is used to prove a trajectory or an infinite age.
"""
import json,sys,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,D,P,DRIFT,step,plan,canonical_source,certify_period,avoids_old_tail,multiple
SOURCE=ROOT/'continuation_2026-10-22/ant_continuation/one_bit_certificate_restored.json'
PARENT=ROOT/'continuation_2026-10-22/ant_continuation2/chronology/mass4_later_collision_guards_audit.json'
FR=[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89]
BASE=(-15,29);M0=100

def rot(p,j):
 for _ in range(j%4):p=p[1],-p[0]
 return p

def place_source(q):return BASE[0]-q[0],BASE[1]-q[1]
def u(q):return q[0]-q[1]
def z(q):return q[0]+q[1]

def main():
 source=json.loads(SOURCE.read_text());parent=json.loads(PARENT.read_text())['prefixes'][0]
 assert parent['W0_pose']==[list(BASE),0] and parent['tail_drift']==[-2,2]
 assert parent['residual_archive_u_bounds']==[-82,58]
 assert parent['all_n_prefix_read_bounds']=={'u':{'minimum':-82,'maximum':58},'z':{'minimum':None,'maximum':39}}
 # Reconstruct the canonical incoming NW period and all frontier classes.
 incoming,heads,end,eh=plan(W,BASE,0);assert end==(BASE[0]-2,BASE[1]+2) and eh==0
 frontier=[]
 for i,q in enumerate(incoming):
  prior=False
  for j,p in enumerate(incoming):
   k=multiple((p[0]-q[0],p[1]-q[1]),(-2,2))
   if k is not None and (k>0 or k==0 and j<i):prior=True
  if not prior:frontier.append(i)
 assert frontier==FR
 # Canonical q-parent core adds no worse archive bound than the prefix itself.
 C0,cp,ch=canonical_source(0,0);assert cp==(0,0) and ch==2
 qcore={place_source(q) for q in C0};assert min(map(u,qcore))>=-82 and max(map(z,qcore))<=39
 assert certify_period(set(P),(0,0),2,W)['drift']==DRIFT
 one=set(P);op=(0,0);oh=2
 for letter in W:
  op,oh,got=step(one,op,oh);assert got==letter
 assert op==DRIFT and oh==2
 shifted={(q[0]+DRIFT[0],q[1]+DRIFT[1]) for q in P}
 assert not shifted.intersection(D) and one==shifted|D
 deposit={place_source(q) for q in D}
 rows=[]
 for r in FR:
  if r==72:continue
  N=source['thresholds'][r];assert N<M0
  R=next(x for x in source['cases'] if x['n']==N and x['r']==r)
  B,p,h=canonical_source(N,r);impact=p;assert p not in B
  assert place_source(impact)==incoming[r]
  B.symmetric_difference_update({p});reads=[]
  for _ in range(R['steps']):
   reads.append(p);p,h,_=step(B,p,h)
  assert list(p)==R['position'] and h==R['heading']
  assert hashlib.sha256(repr(sorted(B)).encode()).hexdigest()==R['field_sha256']
  tw=W[R['phase']:]+W[:R['phase']];assert len(tw)==104 and set(tw)<={'R','L'}
  tail=certify_period(B,p,h,tw);assert tail and list(tail['drift'])==R['tail']['drift']
  assert avoids_old_tail(set(reads),p,h,tw,N)
  treads,_,end,eh=plan(tw,p,h);drift=tuple(-a for a in tail['drift']);assert eh==h
  # All 21 ordinary channels lie in a nonincreasing u half-plane.
  mapped_reads=[place_source(q) for q in reads];mapped_tail=[place_source(q) for q in treads]
  post_u_upper=max(map(u,mapped_reads+mapped_tail));assert drift[0]-drift[1]<=0
  assert post_u_upper-4*M0 < -82
  core_base=incoming[r];assert u(core_base)-4*M0 < -82 and u(core_base)-4*M0 < -34
  # Exact canonical outgoing clean state at the certified phase and pose.
  CB,cp,ch=canonical_source(0,R['phase']);turns=(h-ch)%4;cp=rot(cp,turns);shift=(p[0]-cp[0],p[1]-cp[1])
  clean={(rot(q,turns)[0]+shift[0],rot(q,turns)[1]+shift[1]) for q in CB}
  assert certify_period(clean,p,h,tw)
  field0=[place_source(q) for q in B|clean]
  # E_m consists of older deposit copies at epochs k=0,...,m-N-1.
  # Their z is constant and their lowest u is -4m + u(deposit)+4(N+1).
  archive_z_upper=max(39,max(map(z,field0)),max(map(z,deposit)))
  archive_u_lower_constant=min(-82+4*M0,min(map(u,field0)),min(map(u,deposit))+4*(N+1))
  prefix_u_lower_constant=min(-82+4*M0,min(map(u,incoming)),min(map(u,mapped_reads)))
  prefix_u_upper=max(58,max(map(u,incoming)),max(map(u,mapped_reads))-4*M0)
  prefix_z_upper=max(39,max(map(z,incoming)),max(map(z,mapped_reads)))
  ep=place_source(p);eh=(h+2)%4;outtail,_,eend,ehead=plan(tw,ep,eh)
  assert (eend[0]-ep[0],eend[1]-ep[1])==drift and ehead==eh
  exc=plan(tw[:(72-R['phase'])%104],ep,eh)[2]
  if drift==(-2,-2):classification='SW escape: no remaining remote site can meet parent'
  elif drift==(-2,2) and exc[0]%2==0:classification='NW: exceptional a parity excluded'
  elif drift==(2,2) and tuple(a%2 for a in exc)==(1,0):classification='NE: exceptional d parity excluded'
  elif drift==(-2,2):classification='remaining NW exceptional a branch'
  elif drift==(2,2):classification='remaining NE exceptional d branch; independent d depth'
  else:raise AssertionError(('unexpected ordinary drift',r,drift))
  if drift==(2,2):assert tuple(a%2 for a in exc) in ((1,0),(0,1))
  tail_fixed={}
  if drift[0]-drift[1]==0:tail_fixed['u']=[-4,min(map(u,outtail)),max(map(u,outtail))]
  if sum(drift)==0:tail_fixed['z']=[min(map(z,outtail)),max(map(z,outtail))]
  if drift==(-2,-2):assert max(map(z,outtail))<=archive_z_upper+20
  rows.append(dict(phase=r,core_ray_base=core_base,drift=[-2,2],minimum_m=M0,source_age=N,source_record_field_sha256=R['field_sha256'],capture_time_coefficients_n_m_constant=[208,104,70738+r+R['steps']],capture_pose_constant=[ep,eh],capture_translation_per_m=[-2,2],tail_phase=R['phase'],outgoing_drift=drift,ordinary_postcore_u_upper=[-4,post_u_upper],finite_prefix_u_bounds={'lower':[-4,prefix_u_lower_constant],'upper':prefix_u_upper},finite_prefix_z_upper=prefix_z_upper,complete_future_z_upper=(max(prefix_z_upper,max(map(z,outtail))) if sum(drift)<=0 else None),archive_u_lower=[-4,archive_u_lower_constant],archive_z_upper=archive_z_upper,tail_fixed_normals=tail_fixed,exceptional_ray_base_constant=exc,exceptional_translation_per_m=[-2,2],classification=classification))
 easy=[r['phase'] for r in rows if not r['classification'].startswith('remaining')]
 assert easy==[15,28,32,38,45,46,47,55,57,60,61,71] and len(rows)==21
 out=dict(status='all21ordinary recovery interfaces replayed and q-archive separation proved',scope='coupling to the audited q_n parent, n>=200,m>=100; fixed m when applying sparse recurrence',source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),q_parent_bounds_sha256=hashlib.sha256(PARENT.read_bytes()).hexdigest(),easy_phases=easy,rows=rows)
 (HERE/'ordinary_interfaces.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
