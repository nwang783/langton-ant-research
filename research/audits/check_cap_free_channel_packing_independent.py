from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'cap_free_actual_channel_packing_and_voltage_cycles.md':'e75edaf9b4601b780c0b139e2fc2719299b66330d8c4762fa3ee38620a338d04','actual_channel_packing_requires_event_disjoint_components.md':'d24e02e97a69baed4812c0189fd011b88124f55938a923e1728147270281c3f8','check_actual_channel_packing.py':'145b65bca9c3af1aadc837ef84a84a5edb9a49fe1d3198e2fd20a5e47e7c6dd6','check_actual_channel_packing.json':'68dad62072ee740c7ed69a6f98ddea48ed717dba44a51224a80e5467432ec186'}
for f,h in files.items():assert sha(D/f)==h
J=json.loads((D/'check_actual_channel_packing.json').read_text());z=J['zero_winding_countercontrol'];assert z['relaxed_starts']=={'A':0,'B':0}and 12>=4
assert sum(e['w']for e in z['edges'])==26 and sum(e['nu']for e in z['edges'])==0
cal=[]
for row in J['positive_winding_controls']:
 P=row['P'];s=row['starts'];edges=row['edges'];assert -sum(e['nu']for e in edges)==row['temporal_winding']in [1,2]
 for e in edges:assert s[e['target']]-s[e['source']]>=e['w']+e['nu']*P
 phases=[(s[c]+q)%P for c in ['A','B']for q in range(13)];assert len(set(phases))==26 and P-len(phases)==6
 assert(s['B']+12-s['A'])%4==0 and(s['A']+12+row['temporal_winding']*P-s['B'])%4==0
 cal.append(dict(P=P,winding=row['temporal_winding'],phase_count=26,unfilled=6))
# Independent exact algebra checks across canonical representative voltages.
checks=0
for P in [17,32,104]:
 for ma,mb in [(1,1),(5,7),(13,13)]:
  for qa in range(ma):
   for qb in range(mb):
    for ka,kb in [(-3,-2),(-1,2),(0,0),(2,-3)]:
     for gap in [1,4,9]:
      nu=kb-ka;w=max(ma,gap+qa-qb);si=0;sj=w+nu*P
      startA=si-ka*P;startB=sj-kb*P;tu=si+qa-ka*P;tv=sj+qb-kb*P
      assert startB>=startA+ma and tv-tu>=gap
      sj-=1;assert (sj-kb*P<startA+ma)or(sj+qb-kb*P-tu<gap)
      checks+=1
# Mandatory scope counterexample: arbitrary distinct windows can overlap legitimately.
A=list(range(0,5));B=list(range(2,7));assert A!=B and set(A)&set(B)and A[0]<B[-1]and B[0]<A[-1]
out=dict(status='PASS event-disjoint actual successor COMPONENT packing, WITH mandatory d24e02e9 qualifier',files=files,script=sha(S),positive_calendars=cal,representative_algebra_checks=checks,overlapping_windows_not_covered=[A,B],analytic_review=[
'Original Section1 was overbroad for arbitrary distinct contiguous windows. Mandatory d24e02e9 explicitly restricts to event-disjoint literal successor COMPONENT occurrences or a verified event-disjoint subchannel partition. Without it overlapping windows of one cursor are legal and the claimed packing implication is false. Both originals are retained and jointly bound.',
'For event-disjoint actual contiguous blocks, an overlap at an integer time would identify two different read events. Hence one genuine cross-block rank order determines their entire interval order. Within one occurrence, check offsets/rank gaps instead; no artificial whole-channel self precedence is added. Finite DAG topological placement gives only an injective abstract clock, not exterior color/connector completion.',
'One canonical physical cell representative for all its ranks is essential. T(u)=S_i+q-kappa_u P, so physically aligned starts are S_i-kappa_u P. Whole-block packing and a valid event gap g yield S_j-S_i>=max(m_i,g+q-r)+(kappa_v-kappa_u)P. Different open components partition class sets; different translates of one component cannot share actual events since its classes are distinct and full drift is nonzero.',
'Summing a directed quotient cycle gives kP>=sumw with k=-sum nu. Only k<=0 is impossible for every positiveP. Positive temporal winding is retained exactly, including2; neither primitive-drift reduction nor forced winding1 is permitted. Named positive calendars satisfy all26 distinct phases with6 unknown phases and are not physical fronts.',
'A CLOSED known actual-successor component ofm distinct event classes and full voltagea has aP=m>0. Since m<=P, a=1 and m=P. Any required outside event contradicts the single fullP orbit. This clause does not apply to lifetime, repaired, b-path or mere port-flow cycles.',
'No cap/color/stream-height premise is used by this chronological lemma. It does not exclude the signed OPEN79 calendar, which already has disjoint whole-channel phases, and it supplies no universal period/age or lifetime fuel bound.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
