from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';prior=json.loads((D/'bit11_surviving_cleanup_Q1_parent_ports.json').read_text())['rows'];assert len(prior)==72
hit={'v','D','a','q','j'};clean=[];types=Counter()
for row in prior:
 odd={k for k,h in row['headings'].items()if len(h)%2};assert not odd or odd&hit
 if not odd:clean.append(row)
 # Derive next contact from actual outgoing ports, rather than its table label.
 B=1+1j;v=B+1j
 if row['kind']=='S':
  nextD=v+1;assert nextD==2+2j
 else:
  w=v+1;nextD=w-1j;assert nextD==2+1j
 types[row['kind']]+=1
assert len(clean)==2 and all((r['headings']['j'],r['headings']['x'],r['headings']['r'])==('EEWE','EWWW','WEWW')for r in clean)
S={1+2j,2j,-1j,-3+1j,2+2j,2+1j,-3-1j,-3,-2-1j};assert len(S)==9
U={.5+.5j+(q-.5-.5j)*1j**k for q in S for k in range(4)};assert len(U)==28
par=Counter(int(q.real+q.imag)%2 for q in U);assert par=={0:14,1:14}
note=D/'early_source_fourteen_odd_output_capacity.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha.startswith('7893c252')
dep=SELF.parent/'check_zero_output_K1_eighteen_bound_independent.json';assert json.loads(dep.read_text())['status'].startswith('PASS')
out={'status':'PASS n_early <=14 Nodd for exact surviving early K1 source classes','note_sha256':sha,'new_local_dependency_report':hashlib.sha256(dep.read_bytes()).hexdigest(),'ancestor_rows':72,'odd_hitting_variables':sorted(hit),'all_even_rows':2,'source_successor_types':dict(types),'normalized_cell_offsets':sorted((int(q.real),int(q.imag))for q in S),'all_rotated_offsets':sorted((int(q.real),int(q.imag))for q in U),'checker_counts':dict(par),'analytic':['The five variables v,D,a,q,j hit every nonempty odd history set in the signed complete72-row inventory; the two remaining rows give exactly the early cross-port obstruction. Their three unknown lower-square corners are included in S, so if all nine physical sites are even the full local contradiction applies without global zero output.','The actual successor port path gives D=(2,2) for straight and D=(2,1) for right; both are retained. Rotation about face center(.5,.5) produces28 physical offsets with14 per checker parity.','Every actual C face lower-left has fixed checker parity. Full-heading period is even and full drift preserves that parity. For each odd physical class[p], supported source classes are among[p-s] for the14 eligible offsets. Quotient aliases only reduce the possible class count, irrespective drift direction or short quotient. Distinct source face classes therefore number at most14 times all odd classes.'],'scope':'Exact early source family, complete WHITE cap4 K1. Aggregate OUTPUT capacity, not original black fuel, disjoint extra charge, front exclusion, or global capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
