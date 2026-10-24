"""Exact constants and node-class proof: finite black entry support is required."""
from pathlib import Path
import json,hashlib,itertools
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
E=list(range(2,295,2));A=4851+3*len(E)
assert len(E)==147 and A==5292
clock_labels=[0]+E;M=len(clock_labels)*(A+1)
assert len(clock_labels)==148 and M==783364
N=2*A+(len(E)+1+len(E))*M
assert N==231102964
Eopp=list(range(2,295,4));Mphase=(1+len(Eopp))*(A+1)
assert len(Eopp)==74 and Mphase==396975
assert 2*A+295*Mphase==117118209
# Every unmarked node must be plain V and nonroot. Its parent is either a
# root or positive-C boundary, else its own parent gives two ordinary-child
# edges. Table is a finite case distinction, NOT empirical path inference.
classes=['plain_V_root','plain_V_nonroot','VC','VCC'];table=[]
def marked(c):return c!='plain_V_nonroot'
for q in classes:
 for p in classes:
  if marked(q):
   table.append(dict(node=q,parent=p,assigned='self',legal=True))
  elif marked(p):
   table.append(dict(node=q,parent=p,assigned='parent',legal=True))
  else:
   table.append(dict(node=q,parent=p,assigned=None,legal=False,reason='parent has parent; two consecutive plain-V child edges'))
assert len([r for r in table if not r['legal']])==1
# Actual parent geometry for opposite ordinary V/VC child, normalized sourceN.
rot=lambda q,h:((q[0],q[1]),(q[1],-q[0]),(-q[0],-q[1]),(-q[1],q[0]))[h%4]
first=(3,3);second=rot((3,3),2)
assert(first[0]+second[0],first[1]+second[1])==(0,0)
# Startup: direct and one u_(j-6) nested source windows have maximal age300.
assert max(E+[6+e for e in E])==300
assert 294+300==594
# Each actual mark has at most one child, at strictly positive clock lag.
# Hence it can account for at most one V node of a fixed consumer clock,
# even when the mark itself is a V node at another clock.
deps=[ROOT/'core_periodicity_new/V_C_same_heading_exclusion_frozen_20261023_2043/manifest.json',ROOT/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',HERE/'U_sink_V_renewal_manifest.json',HERE/'parallel_transport_manifest.json',HERE/'perpendicular_manifest.json',HERE/'manifest.json']
out=dict(status='AUTHOR_MARKED_V_BOUNDARY_FINITE_U_ENTRY_FACTOR_PENDING_INDEPENDENT_AUDIT',scope='Actual U-entry retained-eight factors with FINITE COMPLETE BLACK SUPPORT at entry, finite r0 and R; no claim for infinitely prepared backgrounds, after language exit, or arbitrary finite-seed capture.',A=A,even_source_ages=E,marked_source_ages=clock_labels,mark_rate='A+1 produced-input roots/boundaries per clock plus r0 entry-input roots globally',all_epoch_V_bound='r0+783364',eventual_V_bound=M,eventual_V_start='C>20R+211+294',eventual_N_bound=N,eventual_N_start='C>20R+211+594',phase_refinement_ages=[0]+Eopp,phase_refinement_V_bound=Mphase,phase_refinement_N_bound=2*A+295*Mphase,node_class_table=table,conclusion='From finite complete black support at entry, no infinite actual complete-eight factor begins with U/UC/UCC.',dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(HERE/'finite_support_V_marked_boundary_epoch_bound_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in('status','eventual_V_bound','eventual_N_bound','conclusion')},indent=2))
