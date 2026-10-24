from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'K1_pipeline_detours_2026-10-23'
ns={'__file__':str(SELF.parent/'check_zero_output_Q2_and_same_curve_ear_independent.py')}
exec(Path(ns['__file__']).read_text().split('def close(')[0],ns)
base,locate,outs=[ns[x]for x in('base','locate','outs')];even=[r for r in base if all(len(h)%2==0 for h in r[0])];assert len(base)==110 and len(even)==24
prior=json.loads((D/'bit11_surviving_cleanup_Q1_parent_ports.json').read_text())['rows'];assert len(prior)==72
prior_even=[r for r in prior if all(len(h)%2==0 for h in r['headings'].values())];assert len(prior_even)==2
assert {(r['headings']['j'],r['headings']['x'],r['headings']['r']) for r in prior_even}=={('EEWE','EWWW','WEWW')}
# Explicit physical port counts, independent of a desired canonical orientation.
assert outs('EEWE').count('S')==1 and 'EWWW'.count('E')==1
completions=[]
for r in even:
 for q in range(4):
  hh,ht,en,bd=locate(r,-3-1j,q)
  if hh[-3]not in('NNSN','SNNN')or hh[-2]!='EWWW':continue
  assert en==-3-1j
  completions.append((hh[-3-1j],hh[-3],hh[-2],hh[-2-1j]))
assert sorted(completions)==[('EEWE','NNSN','EWWW','NSSS'),('EEWE','NNSN','EWWW','SSNS')]
assert all(outs(r[3]).count('E')==3 for r in completions)and'WEWW'.count('E')==1
new=json.loads((D/'bit11_new_first_branch_full_ports.json').read_text())['rows'];assert len(new)==324
new_even=[r for r in new if all(len(h)%2==0 for h in r['headings'].values())];assert len(new_even)==6
modes=Counter(tuple(r['headings'][k]for k in('e','r','q','u','t','a'))for r in new_even)
assert modes=={('NNSN','WWWE','SSSN','EEWE','NNNS','EWEE'):3,('SNNN','WEWW','SSSN','EEWE','NNNS','EWEE'):3}
late=[]
for row in even:
 for q in range(4):
  hh,ht,en,bd=locate(row,-2,q)
  if hh[-1]!='NNSN'or hh[-1+1j]!='EEWE':continue
  assert en==-1
  late.append((hh[-2],hh[-2+1j],ht[-3+1j]))
assert sorted(late)==sorted([('WWWE','NNNS',-2),('WWWE','NSNN',-2),('WWEW','NSSS',0),('EWWW','SSNS',0)])
notes={}
for f,h in [('zero_output_early_R_ancestor_cross_port_obstruction.md','72a895af45f52e4a1fd2607725701ee9d37fa6b9a908e4d83c255fa312ad8930'),('zero_output_K1_all_branched_faces_are_exact_late.md','0991948603b2feac71dfef169c3f1c0be357519c4338e6ba2cd29663ffd843ea'),('zero_output_K1_front_eighteen_current_lower_bound.md','bcdebac2522ce6f6f8fd9506fb3a7c02b6b2c82d08aa1f2bcb8d706342ae0870')]:
 assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h;notes[f]=h
# Existing signed prior inventories and chain termination are dependencies, not
# recreated from a presumed generic branch classification.
deps={}
for f in ['check_canonical_birth_rank3_balance_independent.json','check_K1_cleanup_Q1_ancestor_independent.json','check_K1_bit11_two_branch_waits_independent.json','check_K1_all_early_zero_L3_supplier_independent.json','check_zero_output_half_turn_rail_independent.json','zero_output_late_Gamma_strict_pit_independent.json']:
 p=SELF.parent/f;z=json.loads(p.read_text());assert z['status'].startswith('PASS');deps[f]=hashlib.sha256(p.read_bytes()).hexdigest()
out={'status':'PASS local early cross-port exclusion, exact late reduction, and zero-output WHITE cap4 K1 bound P>=18||d||infinity','notes':notes,'signed_prior_reports':deps,'fresh_canonical_rows':110,'all_even_canonical_rows':24,'ancestor_prior_rows':72,'all_even_ancestor_rows':2,'lower_square_completions':completions,'cross_edge_required_departures':3,'available_arrivals':1,'new_branch_prior_rows':324,'all_even_rows':6,'exact_modes':[{'mode':k,'count':v}for k,v in modes.items()],'late_P0_completions':late,'analytic':['The local lower face F opposite P0 across EWWW is maximum. Its NW d is flat between two maxima. The complete physical adjacent edges supply one S input from j=EEWE and one E output into x=EWWW, forcing even d=NNSN or SNNN. Fresh canonical inventory, including flag0 entries and all four rotations, permits only two NNSN completions, both with three E departures at t, contradicting r=WEWW one E arrival. This requires no K1 or Gamma at the local step.','For an actual bit11 maximum-branched RIGHT, the old-first-branch mode contains odd q=SSS and vanishes when Nodd=0. The full new-J inventory leaves exactly early SNNN or late NNSN at e. Existing zero-L3 exclusions and genuine two-ancestor theorem reduce the early source-L3 case to the new 3-versus-1 obstruction, including elimination of singleton-W straight ancestor.','For the remaining e=NNSN, u=EEWE, all24 even canonical face profiles and rotations give exactly four P0 completions, every genuine birth at e. Thus p(P0)=J is proved. Neighboring f has equal C heights or difference2 and needs two R reads; zero odd output makes its history four-read, satisfying the precise late-route hypotheses.','The signed repeated-descendant/half-turn alternatives now apply to this actual late path. The independent full-history ancestry rail excludes half-turn, and finite unique-parent quotient terminates repeated descendants at a strict LEFT L pit. No spatial-only monotonicity or off-Gamma K1 order is introduced.','For global zero-output K1 scope, selected state rises reserve odd output, so no rises or falls; signed constant-zero exclusion forces state1. The signed LEFTMOST branch-existence theorem supplies a maximum LEFT branch, which constant1 geometry places at a bit11 RIGHT. The just-proved exact late reduction supplies its LEFT pit, and the signed reverse/three-physical-band current theorem gives P>=18||d||infinity.'],'scope':'Whole-period lower bound for complete WHITE cap4 translating K1 fronts with zero odd output. Not exclusion, existence, positive output fuel, per-branch additive payment, or universal finite-seed capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(completions,late)
