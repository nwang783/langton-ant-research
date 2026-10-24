"""Concrete V1 funding use of the signed three-C shadow cone."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';RP=R/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json';CP=R/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';G=json.loads(GP.read_text())['geometry'];RJ=json.loads(RP.read_text());T={(a,h):v for a,h,v in RJ['created_peaks']};A=RJ['core_offsets'];IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};K=set(map(tuple,json.loads(GP.read_text())['core']));target=(-1,0,1);bud=(1,-1);S=2*sum(target[:2])+T[4,1];assert S==24
rot=lambda q,h:((q[0],q[1]),(q[1],-q[0]),(-q[0],-q[1]),(-q[1],q[0]))[h]
assert tuple(target[i]+rot((1,2),1)[i]for i in(0,1))==bud
rows=[]
for a in IDS:
 c=G[a]['name'].count('C');h=(-G[a]['endpoint'][2])%4;e=rot(G[a]['endpoint'][:2],h);p=(-e[0],-e[1]);o=[tuple(z)for z in G[a]['outputs']if tuple(p[i]+rot(z,h)[i]for i in(0,1))==bud];assert len(o)==1;o=o[0]
 rel=rot((target[0]-p[0],target[1]-p[1]),-h);dh=(1-h)%4;key=(mp[a],mp[4],*rel,dh,*o,3+c)
 row=dict(predecessor=a,pose=[*p,h],bud_output=o,bud_age=3+c,relative_target=[*rel,dh],counted_query=key,counted_excluded=key in COUNT)
 if c==2:
  core=2*sum(p)+A[h];assert core==28>S;row.update(reason='EARLIER_ENTRY_CORE_FUNDS',entry_core=core,margin=core-S)
 elif c==1:
  assert key in COUNT;row.update(reason='SELECTED_PRODUCED_EXACT_AGE4_COUNTED_EXCLUDED')
 elif a in(4,7):
  assert key in COUNT;row.update(reason='ZERO_C_V_OR_U_EXACT_AGE3_COUNTED_EXCLUDED')
 else:
  assert a==0 and rel==(0,1)and dh==1 and key not in COUNT
  # If this P were noninitial, common-marker cone consequence forbids its
  # relative B=(0,1,E),3C. Thus it must be first and consume an initial I.
  q=tuple(p[i]+rot(G[a]['inputs'][0],h)[i]for i in(0,1));activation=28+2*sum(q);assert activation==26>S
  row.update(reason='D_MUST_BE_FIRST_BY_SIGNED_MARKER_NEAR_RETURN_THEN_FUNDS',initial_input=q,I28_activation=activation,margin=activation-S)
 rows.append(row)
first=[]
for a in IDS:
 assert all(tuple(z)not in K for z in G[a]['inputs'])
 hs=[sum(z)for z in G[a]['inputs']];value=28+2*max(hs);assert value>=30>S
 first.append(dict(source_if_first=a,initial_input_heights=hs,max_I28_activation=value,margin=value-S))
J=dict(status='AUTHOR_V1_THREE_C_LEFT_RETURN_FUNDING_PASS',scope='Any markedA(0,0,N), later Vgoal(-1,0,E), exactly3C, complete recurrent8 prefix andI>=28. Signed cone plus exact counted clauses forces funding atV1score24. No old goal-output survival assumed, not allV1.',target_pose=target,target_score=S,selected_input_is_exact_predecessor_bud=bud,predecessor_cases=rows,source_first_cases=first,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,RP,CP,Path(__file__).resolve()]})
(R/'chronology_dcuv/V1_three_C_left_return_funding.json').write_text(json.dumps(J,indent=2)+'\n');print(dict(target_score=S,predecessor_cases=len(rows),counted_cuts=sum(r['counted_excluded']for r in rows),source_first_min_activation=min(r['max_I28_activation']for r in first)))
