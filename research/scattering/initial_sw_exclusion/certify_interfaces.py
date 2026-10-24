"""Exact geometry/parity corollary of five audited complete return parents."""
import hashlib,json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,P,D,plan,multiple,step
BASE=HERE.parent/'ordinary_reverse_interface'
PHASES=[15,45,46,47,57];FRESH=[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89];GOOD=[14,28,32,38,46,56,60,62,70,72]
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
scale=lambda a,k:tuple(x*k for x in a)
def pointadd(p,q):return add(p[0],q[0]),add(p[1],q[1])
def off(p,q):return add(p[0],(0,q[0])),add(p[1],(0,q[1]))
def u(p):return add(p[0],scale(p[1],-1))
def z(p):return add(p[0],p[1])
def lower(v):assert v[0]>=0;return 100*v[0]+v[1]
def main():
 manifest=json.loads((BASE/'manifest.json').read_text());assert hashlib.sha256((BASE/'manifest.json').read_bytes()).hexdigest()=='2cd64e957de70ed25e5ab7bb58ac87ce36765cfc6a1c234c05d65441aa8550a1'
 blank=set();bp=(0,0);bh=0
 for _ in range(9977):bp,bh,_=step(blank,bp,bh)
 assert bp==(-15,10) and bh==3 and len(blank)==715
 E=blank^{(bp[0]+y,bp[1]-x) for x,y in P}
 assert max(x-y for x,y in E)==48 and min(x-y for x,y in E)>=-34 and bp[0]-bp[1]==-25
 assert min(x-y+25 for x,y in E)>=-9>-73
 assert min(x+y for x,y in D)==-3
 Q=plan(W,(0,0),2)[0]
 rows=[]
 for r in PHASES:
  certfile=BASE/f'certificate_r{r}.json';Tfile=BASE/f'template_r{r}.json'
  # Source JSON is pinned by the already audited package manifest.
  assert hashlib.sha256(certfile.read_bytes()).hexdigest()==manifest['files'][certfile.name]
  cert=json.loads(certfile.read_text());T=json.loads(Tfile.read_text());assert cert['template_sha256']==hashlib.sha256(Tfile.read_bytes()).hexdigest()
  assert cert['phase']==r and cert['whole_future_forward_guard'] and cert['tail']['drift']==[-2,-2]
  p=((0,0),(0,0));h=2;time=(0,0);us=[];zs=[]
  def collect(q):
   uv=u(q);assert uv[0]==0;us.append(uv[1]);zs.append(lower(z(q)))
  for seg in T['segments']:
   word=seg['word'];assert set(word)<={'R','L'};qs,hs,e,eh=plan(word,(0,0),h)
   assert seg['type'] in ['finite','periods']
   if seg['type']=='finite':
    for q in qs:collect(off(p,q))
    p=off(p,e);time=add(time,(0,len(word)))
   else:
    n=tuple(seg['count']);assert len(word)==104 and word in {W[j:]+W[:j] for j in range(104)} and lower(add(n,(0,-1)))>=0 and eh==h
    for q in qs:
     first=off(p,q);last=pointadd(first,(scale(add(n,(0,-1)),e[0]),scale(add(n,(0,-1)),e[1])))
     collect(first);collect(last)
    p=pointadd(p,(scale(n,e[0]),scale(n,e[1])));time=add(time,scale(n,104))
   h=eh
  assert [list(p[0]),list(p[1])]==cert['capture_pose'][0] and h==cert['capture_pose'][1] and list(time)==cert['capture_time']
  phase=cert['tail_phase'];tw=T['infinite_tail_word'];assert tw==W[phase:]+W[:phase]
  # Move to canonical phase zero, retaining all read/write bounds.
  skip=(104-phase)%104;qs,_,e,h=plan(tw[:skip],(0,0),h)
  for q in qs:collect(off(p,q))
  p=off(p,e);assert h==3 and p[0][0]==p[1][0]==0
  p0=(p[0][1],p[1][1]);qs,_,end,eh=plan(W,p0,h);assert eh==h and tuple(end[i]-p0[i] for i in range(2))==(-2,-2)
  for q in qs:assert q[0]-q[1] in range(min(us)-100,max(us)+101)
  tailu=[q[0]-q[1] for q in qs];umin=min(us+tailu);umax=max(us+tailu)
  fresh=[]
  for i,q in enumerate(qs):
   if not any((k:=multiple((v[0]-q[0],v[1]-q[1]),(-2,-2))) is not None and (k>0 or k==0 and j<i) for j,v in enumerate(qs)):fresh.append(i)
  assert fresh==FRESH and (sum(p0)+h)%2==0
  second=cert['second_marker_affine'];assert [a[0] for a in second]==[2,2]
  parity=[a[1]%2 for a in second];assert sum(parity)%2==1
  opposite=[1-b for b in parity];allowed=[i for i in fresh if sum(qs[i])%2==1];assert allowed==GOOD
  exceptional=[v%2 for v in qs[72]];assert exceptional!=opposite
  # Complete blank history, expressed in source coordinates, has z>=-73:
  # z_source=u_actual+25, and blank-prefix reads have u_actual>=-34.
  # Thus its true lower bound is at least-9; -73 is deliberately conservative.
  # The omitted canonical old deposits have z>=-3. The entire model prefix,
  # both initial toggles, and the phase-zero core are also bounded below.
  assert min(x+y for x,y in P)>=-3
  coremin=min(y-x for x,y in P)+sum(p0) # clockwise rotate canonical SE P to SW.
  initial_toggle_lower=min(sum(Q[r]),lower(add(tuple(second[0]),tuple(second[1]))))
  archive_lower=min(-73,min(zs),coremin,initial_toggle_lower)
  assert archive_lower==-73
  assert (min(zs),umin,umax)=={15:(-29,-128,74),45:(-29,-140,62),46:(-31,-104,64),47:(-31,-104,64),57:(-31,-100,68)}[r]
  rows.append(dict(phase=r,prefix_z_lower=min(zs),canonical_future_u_bounds=[umin,umax],archive_z_lower=archive_lower,phase_zero_pose=[p0,h],first_remote_parity=parity,opposite_corner_parity=opposite,returned_exceptional_ray_parity=exceptional,favorable_fresh_phases=allowed,certificate_sha256=hashlib.sha256(certfile.read_bytes()).hexdigest()))
 out=dict(status='exact five-parent strip, complete-archive and parity interfaces',domain='fixed blank-front age m>=100; independent remote age k>=100',rows=rows,scope='Analytic mass-five recurrence coupling is in PROOF.md; no arbitrary-core or whole-arm assertion.')
 (HERE/'interfaces.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
