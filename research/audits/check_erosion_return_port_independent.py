from pathlib import Path
from fractions import Fraction as F
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'postforeign_erosion_return_port_restoration_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='38cbb8729852cc54c79de0c7e59488b89fa33296840f8144336307dea448efdc';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
J=json.loads((D/'return_ports.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,tr,K,rot,center,xy,meet,pieces=[ns[k]for k in('W','M','tr','K','rot','center','xy','meet','pieces')];raw=lambda ts:''.join(W[a]for a in ts);vec=[1j,1,-1j,-1];beta=1-1j;facts=[]
for a in'DCVUFQB':
 z=tr(W[a]);q=z['p']+rot(z['h'])*beta;assert z['last'][q]==('R',len(W[a])-2)and q not in{z['p']+rot(z['h'])*k for k in K}
 r=next(r for r in J['all7_atomic_real_EXIT_beta_birth_facts']if r['actual_previous_atom']==a);assert xy(q)==r['physical_beta_slot_in_previous_chart']and r['SAME_last_R_birth_tick0']==len(W[a])-2;facts.append((a,xy(q),len(W[a])-2))
loop=J['complete9_black_prepared_loop_and_boundary_obstruction'];T=loop['tokens'];assert T=='DCVCCVV';z=tr(raw(T)+M);assert z['bad']is None and z['req'][beta]is False
vis=[(i,ch)for i,(q,h,ch)in enumerate(z['reads'])if q==beta];assert vis[0]==(98,'R');seed={q for q,b in z['req'].items()if b};assert len(seed)==9 and sorted(map(xy,seed))==loop['complete_seed'];seg=pieces(T);assert meet(*seg[1],*seg[-1])==(F(1,2),F(1,2))
for a in'DCVUFQB':assert tr(raw(a+T)+M)['bad']is not None
B=set(seed);p=0j;h=0
for t,ch in enumerate(raw(T)+M):
 assert(ch=='L')==(p in B);r=loop['all_RAW_plus_actual_M11_reads'][t];assert(r['cell'],r['turn'],r['tick0'])==(xy(p),ch,t);B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=vec[h]
controls=[]
for r in J['two_genuine_U_entry_output_erosion_but_hole_not_restored_controls']:
 prefix=r['genuine_U_entry_prefix'];assert prefix in('UQVCCV','UBVCCV');assert tr(raw(prefix)+M)['bad']is None;attempt=prefix+'U';result=tr(raw(attempt)+M);fail,prev,hole,ch=result['bad'];vstart=len(raw(prefix[:2]));uv=tr(raw(prefix[:2]));vpose=(uv['p'],uv['h']);nextstart=len(raw(prefix));nextpose=tr(raw(prefix));qA=uv['p']+rot(uv['h'])*1j
 assert fail==nextstart+12 and prev==vstart+2 and hole==uv['p']+rot(uv['h'])*(-1-1j)and ch=='L'
 assert(hole-nextpose['p'])/rot(nextpose['h'])==2j;assert tr(raw('VCCV'))['last'][-1-1j]==('L',2)
 ct=tr(raw(attempt)[:fail]);seed={q for q,b in ct['req'].items()if b};assert sorted(map(xy,seed))==r['complete_finite_seed_for_actual_valid_partial_run'];B={q:('initial',None)for q in seed};p=0j;h=0;birth=vstart+11;death=nextstart+1
 for t,c in enumerate(raw(attempt)[:fail]):
  before=B.get(p);assert(c=='L')==(before is not None)
  if c=='L':B.pop(p);h=(h-1)%4
  else:B[p]=('R',t);h=(h+1)%4
  row=r['executed_actual_fine_reads_before_divergence'][t];assert row['cell']==xy(p)and row['turn']==c and row['before_identity']==(list(before)if before else None)and row['after_identity']==(list(B[p])if p in B else None)
  if t==birth:assert p==qA and c=='R'
  if t==death:assert p==qA and c=='L'and before==('R',birth)
  p+=vec[h]
  if str(t+1)in r['exact_physical_snapshots']:
   snap=r['exact_physical_snapshots'][str(t+1)];core={p+rot(h)*k for k in K};alive=B.get(qA)==('R',birth)
   assert(snap['original_A_physically_alive'],snap['original_A_CORE'],snap['original_A_CURRENT'],snap['hole_WHITE'])==(alive,qA in core,alive and qA not in core,hole not in B)
 assert p==hole and p not in B;h=(h+1)%4;p+=vec[h];assert xy(p)+[h]==r['actual_next_pose']
 controls.append(dict(prefix=prefix,actual_reads_before_divergence=fail,A_birth=birth,A_death=death,hole_deleted=prev,required_hole_L=fail,actual_divergent_turn='R'))
# Portable proof uses only the actual VCCV factor, irrespective of upstream foreign/source identities.
z=tr(raw('VCCV'));assert(z['p'],z['h'])==(-1+1j,2);assert z['last'][-1-1j]==('L',2)
old=pieces('V')[0];start=center(z['p'],z['h']);assert start==-1+3j
for a in'DVU':
 q=tr(W[a],z['p'],2);end=center(q['p'],q['h']);assert q['h']==2
 if a in'DV':assert end.real<start.real and meet(*old,start,end)is None
 else:assert end.real==start.real and meet(*old,start,end)==(0,F(1,2))and tr(raw('VCCVU'))['bad']==(len(raw('VCCV'))+12,2,-1-1j,'L')
out=dict(status='PASS exact atomic EXIT beta and postforeign erosion-versus-hole-restoration interfaces; zero-C S lane only',manifest_sha256=sha(MF),script_sha256=sha(S),atomic_beta_facts=facts,prepared_loop_reads=len(loop['all_RAW_plus_actual_M11_reads']),genuine_erosion_controls=controls,analytic_review=['All seven actual atoms freshly leave SAME beta physically BLACK outside next-entry core at their penultimate RAW R. The nine-black DCVCCVV factor is genuinely feasible and recontacts its oldC midpoint, but its first beta readR98 has no preceding read, so no actual immediately preceding atom can supply that exact boundary.','Both genuine UQ/UB VCCV histories retain the old A R identity aliveCORE at fourthRAWexit and kill it at the actual nextU tick1/read2. The distinct firstV entry-core hole was deleted at Vtick2/read3 and never reread in CCV; attempted nextU needs itL12/read13 but the real board isWHITE and takesR. Complete fields and every fine identity were replayed.','CORE absorption is not physical death. A future actualR at the deleted hole, including an active-core write, would count as restoration; no residual-only origin or postforeign age restriction is imposed.','The portable VCCV zero-C S continuation starts corrected(-1,3). D/V immediately move strictly left of the entire oldV x-range[-1,1], and all later zero-C S D/V/U cannot increase x. ImmediateU is the only possible oldV contact and fails at the deleted hole. This closes only that source and heading lane; other old pieces and laterC turns remain unrestricted.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
