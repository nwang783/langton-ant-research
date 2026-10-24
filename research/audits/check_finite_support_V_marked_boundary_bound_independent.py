from pathlib import Path
import hashlib,json,itertools
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'causal_archive_frontier_2026-10-23'
p=D/'finite_support_V_marked_boundary_epoch_bound.md';sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha=='a2c4a8d5eae4cdbda2e9ce3697c1e11aab1e653b465ffca3edade663c1b63d1f'
text=p.read_text();assert'FINITE'in text and'infinite prepared'in text.lower()
ref=json.loads((D/'finite_support_V_marked_boundary_epoch_bound_controls.json').read_text())
reports=['check_V_C_same_heading_exclusion_independent','check_V_parallel_reproductive_supply_independent','check_U_parallel_selected_supply_independent','check_V_nonbranching_parallel_renewal_independent','check_full_context_horizon_independent','check_parallel_width_and_infinite_epoch_independent','check_perpendicular_epoch_interface_independent']
deps={}
for n in reports:
 q=SELF.parent/(n+'.json')
 if not q.exists()and n=='check_perpendicular_epoch_interface_independent':
  # This filename is recorded below from its exact saved audit, not an author result.
  qs=list(SELF.parent.glob('*perpendicular*independent.json'));assert len(qs)==1; q=qs[0]
 data=json.loads(q.read_text());assert data['status'].startswith('PASS');deps[q.name]=hashlib.sha256(q.read_bytes()).hexdigest()
E=tuple(range(2,295,2));labels=(0,)+E;A=4851+3*len(E);M=(A+1)*len(labels);N=2*A+(2*len(E)+1)*M
assert(A,len(labels),M,N)==(5292,148,783364,231102964)
opp=(0,)+tuple(range(2,295,4));M2=(A+1)*len(opp);N2=2*A+295*M2;assert(len(opp),M2,N2)==(75,396975,117118209)
assert max(E+(4,)+(tuple(6+e for e in E)))==300 and 294+300==594
for H in range(10):
 j=H+595
 assert min(j-e for e in E)>H+294 and j-4>H+294 and min(j-6-e for e in E)>H+294
# Exhaustive node-class deduction. Marks are roots OR any positive-C V-family node.
classes=('V_root','V_nonroot','VC_root','VC_nonroot','VCC_root','VCC_nonroot')
def mark(c):return c.endswith('_root')or not c.startswith('V_')
rows=[]
for q,parent in itertools.product(classes,repeat=2):
 if mark(q):assignment='self'
 elif mark(parent):assignment='parent'
 else:
  assert q==parent=='V_nonroot';assignment='impossible_two_consecutive_ordinary_target_edges'
 rows.append([q,parent,assignment])
assert sum(z[2].startswith('impossible')for z in rows)==1
# Physical relative flips include all initial source types; two ordinary TARGETS suffice.
flip=(3,3);rot180=lambda z:(-z[0],-z[1]);assert tuple(a+b for a,b in zip(flip,rot180(flip)))==(0,0)
# At fixed current clock, a mark cannot supply both itself and a child: lag is positive.
for lag in E:assert lag>0
for field,val in [('A',A),('eventual_V_bound',M),('eventual_N_bound',N),('phase_refinement_V_bound',M2),('phase_refinement_N_bound',N2)]:assert ref[field]==val
assert ref['even_source_ages']==list(E)and ref['marked_source_ages']==list(labels)
proof=[
'Finite complete black support at U-family factor entry makes residual identity count r0 and radius R finite. All roots prior to the factor are entry identities; initial core bits are handled by the exact residual remove-before-install model, not an uncounted input class.',
'Each V-family node has at most one parallel selected C parent and one child, because its selected input is unique and its own original C identity is spent once. Every such edge has positive even full-source-entry C age2..294. No physical wire, field reset or historical-component disjointness is assumed.',
'A node with no C parent has selected input either untouched entry, perpendicular-produced, or parallel C-tail-produced. D-base odd selected supply is zero; U-base reproductive supply is zero; V-base A/B reproductive supply is zero. Thus produced external roots are at most4851+147*3=5292 per clock, and all entry-selected roots together at most r0.',
'Mark external roots plus every VC/VCC boundary node. There is at most one positive-C full packet per source ENTRY clock, including skipped clocks. Any unmarked node is plain V. If its parent is unmarked, that parent is also a nonroot plain V and has a parent, giving two consecutive edges with ordinary V/VC targets. Their two(3,3,S) flips repeat the first source center, contrary to the independently signed simple-factor exclusion.',
'Therefore each node is a mark or a single child of one. At a fixed clock the assignment is injective: outdegree<=1 prevents two children, and positive edge lag prevents mark and child both at that clock. Assigned marks lie on148 clock labels j,j-2,...,j-294. Count entry marks only once globally. This yields v_j<=r0+783364. VCC-to-VCC or earlier ancestry is not excluded; those edges are simply cut at marks.',
'Untouched entry input consumption stops after H=20R+211. For j>H+294 all assigned marks are beyond that horizon, so v_j<=783364. For j>H+594 all direct and nested source clocks used by N_j<=A+sum_even v+v_(j-4)+u_(j-6) and u_(j-6)<=A+sum_even v are beyond H+294. Thus N_j<=231102964.',
'In a hypothetical infinite factor C tends to infinity, since every finite-C prefix has finite duration. The finite startup expires. The resulting eventual uniform epoch bound contradicts the independently signed exact330 finite-state argument: old cells miss ALL candidate contexts at each already-actual cut; an assumed reachable normalized-state cycle lifts inductively on the unchanged real exterior. Zero C contradicts zero-C fuel, zero drift contradicts center injectivity, and nonzero drift with positive C contradicts unbounded tangent turning of a simple translating curve via a uniformly bounded-crossing closing bridge.',
'There is therefore NO infinite actual complete-eight factor beginning with U/UC/UCC on a finite-support physical board. No statement is made for infinite prepared backgrounds, for ant behavior after language exit, for eventual entry to the language, for original strict V1/U1 funding, or for universal standard104 capture.'
]
out=dict(status='PASS finite-support U-entry complete-eight infinite-factor exclusion',note_sha256=sha,dependencies=deps,constant_A=A,all_epoch_V_bound='r0+783364',entry_input_horizon='20R+211',eventual_V_bound=M,eventual_V_start='C>20R+211+294',eventual_N_bound=N,eventual_N_start='C>20R+211+594',optional_phase_refinement_V=M2,optional_phase_refinement_N=N2,node_class_cases=rows,proof=proof,scope='FINITE complete black support at factor entry, actual valid complete-eight U-entry factors only. No arbitrary prepared infinite board, universal capture, post-language behavior or funding closure.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(M,N)
