from pathlib import Path
import json,hashlib
P=Path(__file__);R=P.parent.parent;S=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
man=json.loads((S/'PRISTINE_ONE_INPUT_BUDGET_MANIFEST.json').read_text())
for n,h in man.items():assert sha(S/n)==h
A=json.loads((S/'OUTWARD_RECORD_GUARDS_CHECKED.json').read_text());H=A['canonical_period'];C=json.loads((S/'PRISTINE_ONE_INPUT_BUDGET_CHECKED.json').read_text())
assert sha(R/'audits/check_fresh_and_outward_record_guards_independent.json')=='b286b57ae82dd38f729c59fde0ae07041e909307390ac3d42482c57d2703e8a4'
D=[(0,1),(1,0),(0,-1),(-1,0)];N=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
add=lambda p,q:(p[0]+q[0],p[1]+q[1]);dot=lambda p,q:p[0]*q[0]+p[1]*q[1]
def rot(q,k):
 for _ in range(k):q=(q[1],-q[0])
 return q
def trace(w,h):
 p=(0,0);out=[]
 for c in w:
  out.append(p);h=(h+(1 if c=='R' else -1))%4;p=add(p,D[h])
 return out,p,h
catalog={};guardchecks=[]
for cat in A['normal_catalog']:
 for r in cat['records']:
  w=r['cycle_word'];qs,d,h=trace(w,r['normalized_heading']);n=tuple(cat['outward_normal']);v=dot(n,d);assert v>0
  first={}
  for i,q in enumerate(qs):
   # Strict old half-plane dot(q+k*d,n)<0, k>=0. Exact finite bound.
   top=(-dot(n,q)-1)//v
   for k in range(top+1):
    z=(q[0]+k*d[0],q[1]+k*d[1]);t=104*k+i
    if z not in first or t<first[z]:first[z]=t
  assert set(first)==set(map(tuple,r['old_guard']))
  assert {q for q,t in first.items()if w[t%104]=='L'}==set(map(tuple,r['required_black']))
  assert {q for q,t in first.items()if w[t%104]=='R'}==set(map(tuple,r['required_white']))
  assert max(first.values())==r['max_old_read_time']<=270
  guardchecks.append([list(n),r['phase'],len(first),max(first.values())])
  for k in range(4):
   key=((r['normalized_heading']+k)%4,w,rot(n,k));assert key not in catalog;catalog[key]=(list(n),r['phase'],k)
cover=[]
for h in range(4):
 for i in range(104):
  w=H[i:]+H[:i];qs,d,he=trace(w,h);assert he==h
  for n in N:
   # These are exactly the previous 104 head cuts relative to current cut zero.
   if max(dot(n,(q[0]-d[0],q[1]-d[1]))for q in qs)<0:
    assert dot(n,d)>0 and (h,w,n)in catalog
    cover.append((h,i,n,catalog[h,w,n]))
assert len(cover)==len(catalog)==32
assert {(h,i,n)for h,i,n,_ in cover}=={(r['heading'],r['cyclic_phase'],tuple(r['normal']))for r in C['complete_previous104_phase_direction_cover']}
# Length-independent fringe proof: at most 104 early and 270 late cuts; conservative 375.
for length in range(1500):assert sum(t<104 or length-t<271 for t in range(length))<=min(length,374)
old=R/'audits/check_one_black_budget_independent.json';T=json.loads(old.read_text());assert sha(old)==C['source_audit_sha256']
source=R/'nonlinear_global_budget_2026-10-23/one_black_uniform_defect_budget.md';assert sha(source)==C['source_note_sha256']
L=[106258,9977,9977+15209,9977+62345,9977+64978,9977+64978+7994];ss=[1,1,1,1,2,3]
assert [r['arbitrary_length_bound']for r in C['signed_one_black_decomposition_cases']]==L
assert [r['standard_piece_bound']for r in C['signed_one_black_decomposition_cases']]==ss
assert max(x+375*y for x,y in zip(L,ss))==106633 and 8*106633==853064
LS=R/'sources/kehao95-core/one_black/lean/OneBlack';sem=(LS/'Semantics.lean').read_text();sc=(LS/'Scattering.lean').read_text();rev=(LS/'PhaseReverse.lean').read_text()
assert 'def HasStandardWord' in sem and '∧ HasStandardWord s' in sem and 'run 9977 white' in sem
assert 'ordinaryReturn' in sc and 'exceptionalReturn' in sc and 'Phase.lane_reaches' in sc and 'spectrum.exceptionalReturn positive' in sc
assert 'phase.reverseAccepted' in rev
out=dict(status='PASS standard-word interior guard and fixed-entry-cohort bound before SECOND distinct old lifetime consumption',sources=man,retained_one_black_source_hashes={n:sha(LS/n)for n in ['Semantics.lean','Terminal.lean','Scattering.lean','Universal.lean','PhaseReverse.lean','PhaseChecks.lean','Pristine.lean','ActualHistory.lean']},signed_decomposition_audit=sha(old),guard_dependency_audit=sha(R/'audits/check_fresh_and_outward_record_guards_independent.json'),complete_phase_heading_normal_cases=32,old_guard_reconstructions=guardchecks,guard_max_first_read=270,arbitrary_lengths=L,standard_pieces=ss,bad_pristine_cut_bound=106633,direction_marked_bound=853064,analytic_review=['Every singleton position and initial pose is retained: prefix1376, active27, inert, all22 frontier channels=21 ordinary plus exceptional; no 21-of22 gap imported.','PermanentP104 explicitly includes canonical HasStandardWord, and exceptional spatially opposite flight is forward canonical via accepted terminal normalization, not time reversal.','This report uses the signed complete-history decomposition, not a new Lean build or fresh1376-table replay. Entire715-cell historical field and opposite-flight archive recovery are retained in that premise.','Until second C0 consumption, compare to one-black board at the FIRST consumed C0 cell at original chosen cut; never restart at contact. Unread extras remain untouched BLACK and absent from parent.','Truncating at second input increases neither arbitrary length nor standard pieces. Head at terminal second input is BLACK, hence not pristine. Guard horizon270 lies strictly before cutoff when271 following moves are available.','Current full-board pristine half-plane, rather than parent or initial hull, makes every unqueried forward-side cell WHITE. Any extra old guard cell would be read within270 and contradict second-contact horizon.','Counts are time cuts, not directions; no physical-time bound, no original-mass induction, no universal capture or third-input extension.'])
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS 32 complete standard-interior cases; fixed cohort bound106633 before second input, using signed ALL22 canonical one-black decomposition')
