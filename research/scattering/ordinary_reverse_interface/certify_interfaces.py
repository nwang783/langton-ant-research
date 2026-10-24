"""Coverage, exact half-plane transfer, and all-distance adverse archive bits."""
import sys,json,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import P,D,W,plan,step,certify_period,multiple,canonical_source
FRESH=[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,75,89]
GOOD=[15,29,32,38,45,46,47,55,56,57,61,62,71]
BAD=[13,14,27,28,60,70,75,89]
SOURCE=ROOT/'continuation_2026-10-22/ant_continuation/one_bit_certificate_restored.json'
TFILE=ROOT/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'
u=lambda p:p[0]-p[1];z=lambda p:sum(p)
def scalar(a,k):return a[0]*k+a[1]
def at(p,k):return scalar(p[0],k),scalar(p[1],k)
def main():
 rows=[json.loads((HERE/f'certificate_r{r}.json').read_text()) for r in FRESH];assert len(rows)==21
 assert [r['phase'] for r in rows if r['whole_future_forward_guard']]==GOOD
 assert [r['phase'] for r in rows if not r['whole_future_forward_guard']]==BAD
 negative=[];standard={W[j:]+W[:j] for j in range(104)}
 for r in rows:
  assert r['source_sha256']==hashlib.sha256(SOURCE.read_bytes()).hexdigest()
  assert r['template_sha256']==hashlib.sha256((HERE/f"template_r{r['phase']}.json").read_bytes()).hexdigest()
  assert r['domain']=='integer k>=100' and r['input_old_deposit_count']==42
  T=json.loads((HERE/f"template_r{r['phase']}.json").read_text());word=T['infinite_tail_word'];assert word in standard and word==W[r['tail_phase']:]+W[:r['tail_phase']]
  if r['phase'] not in BAD:assert r['full_future_u_lower']>=-160;continue
  p,h=r['capture_pose'];d=tuple(r['tail']['drift']);assert d==(-2,2) and [p[0][0],p[1][0]]==[2,-2]
  delta=(72-r['tail_phase'])%104;offset=plan(word[:delta],(0,0),h)[2]
  # At epoch k+1000, the reverse front reads this FIXED old bit. The k
  # dependence of its starting pose cancels exactly against its return.
  marker=(p[0][1]+offset[0]+1000*d[0],p[1][1]+offset[1]+1000*d[1]);assert u(marker)<-160 and z(marker)>max(map(z,D))
  qs,_,_,_=plan(word,(0,0),h);candidates=[]
  for i,q in enumerate(qs):
   v=(marker[0]-p[0][1]-q[0],marker[1]-p[1][1]-q[1]);a=multiple(v,d)
   if a is not None:
    # Actual epoch = k+a. All candidates lie in the genuine infinite tail.
    assert 100+a>=0;candidates.append((104*a+i,i))
  first=min(candidates);assert first[0]==104000+delta and word[first[1]]=='R'
  # The prefix stays above the plane, so no pre-tail read sees this bit.
  assert r['prefix_u_lower']>=-160
  total=[r['capture_time'][0]+104,r['capture_time'][1]+first[0]]
  negative.append(dict(phase=r['phase'],fixed_old_bit=marker,first_changed_time=total,reference_letter='R',actual_letter='L',future_behavior='not asserted after the first changed read'))
 # Explicit finite-seed bridge: the blank prefix reaches the exact canonical
 # SW phase-zero core, retaining its complete 702-cell stationary archive.
 assert hashlib.sha256(TFILE.read_bytes()).hexdigest()=='16246ec40cbdd4ad94c35698992582b27a942dc7d539683f1b3684892cd5687d'
 old=json.loads(TFILE.read_text());prefix=old['segments'][0]['word'];assert len(prefix)==9977 and set(prefix)<={'R','L'}
 B=set();p=(0,0);h=0;reads=[]
 for ch in prefix:reads.append(p);p,h,actual=step(B,p,h);assert actual==ch
 assert p==(-15,10) and h==3 and certify_period(B,p,h,W)
 rotate=lambda q:(q[1],-q[0]);core={(p[0]+rotate(q)[0],p[1]+rotate(q)[1]) for q in P};E=B^core
 assert len(E)==702 and (min(map(z,E)),max(map(z,E)))==(-21,35)
 assert (min(map(z,reads)),max(map(z,reads)))==(-21,35)
 # At age m, O=(-15-2m,10-2m). Rotating to canonical coordinates sends the
 # whole E to u<=16-4m, and the extra older canonical deposits to u<=5-4m.
 assert 16-4*100 < -160
 B0=set(P);p0=(0,0);h0=2
 for ch in W:p0,h0,actual=step(B0,p0,h0);assert actual==ch
 assert p0==(2,-2) and h0==2 and B0=={(x+2,y-2) for x,y in P}^D
 Q,_,_,_=plan(W,(0,0),2)
 fresh=[i for i,q in enumerate(Q) if not any((j:=multiple((b[0]-q[0],b[1]-q[1]),(2,-2))) is not None and (j>0 or j==0 and ii<i) for ii,b in enumerate(Q))]
 assert fresh==sorted(FRESH+[72])
 old_transverse=(min(map(z,Q)),max(map(z,Q)));blank_rows=[]
 kernel,kp,kh=canonical_source(42,0);assert len(kernel)==517 and kp==(0,0) and kh==2
 for r in rows:
  first=Q[r['phase']];assert first not in kernel and -5-4*100-u(first)<-21
  q2=r['second_marker_affine'];slope=(q2[0][0],q2[1][0]);base=(q2[0][1],q2[1][1]);q2_at100=at(q2,100)
  for black in kernel|{first}:
   collision=multiple((black[0]-base[0],black[1]-base[1]),slope)
   assert collision is None or collision<100
  # The pre-source blank trace cannot hit the second marker: outside its
  # finite transient by z, then outside its earlier standard phase rays.
  assert u(slope)>=0 and -5-400-u(q2_at100)<-21
  if u(slope)>0:assert u(q2_at100)>max(map(u,Q))
  else:
   assert z(slope)!=0
   assert z(q2_at100)>old_transverse[1] if z(slope)>0 else z(q2_at100)<old_transverse[0]
  if r['phase'] in GOOD:
   a,b=r['capture_time'];blank_rows.append(dict(phase=r['phase'],initial_core_base=[-15+Q[r['phase']][1],10-Q[r['phase']][0]],initial_core_per_m=[-2,-2],second_marker_base=[-15+base[1],10-base[0]],second_marker_per_m=[-2,-2],second_marker_per_k=[slope[1],-slope[0]],capture_time_m_k_constant=[104,a,9977+b],whole_future_z_upper_m=[-4,-5-r['full_future_u_lower']]))
 out=dict(status='exact 21-channel interface coverage and adverse-history controls',domain='k>=100; blank realization also m>=100 independently',protected_phases=GOOD,unprotected_backward_phases=BAD,common_protected_halfplane='u>=-160',adverse_history_controls=negative,blank_realizations=blank_rows,blank_stationary_archive_z_bounds=[-21,35],blank_archive_canonical_u_upper_m=[-4,16],scope='The thirteen protected rules allow arbitrary finite changes below the plane. The eight controls disprove only unchanged-future protection, not highway convergence or a general renewal theorem.')
 (HERE/'interfaces.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
