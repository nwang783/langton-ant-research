"""Two exact foreign targets, genuine atomic V common-R8 before-age3."""
from pathlib import Path
import hashlib,json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent;BP=R/'U_star_one_foreign_return_transfer_2026-10-24/check_U_star_corner_transfer.py';n={'__file__':str(BP)};exec(BP.read_text().split('# Exactly twelve constant local suffixes.')[0],n)
W=n['W'];mp=n['mp'];M=n['M'];K=n['K'];at=n['at'];rot=n['rot'];sub=n['sub'];literal=n['literal'];center=n['center'];meet=n['meet'];z=(2,0)
sources=[]
for typ in('V','VC','VCC'):
 d=literal(''.join(W[mp[a]]['word']for a in typ));ep=tuple(d['endpoint'][:2]);eh=d['endpoint'][2];outs={q for q,v in d['requirements'].items()if v^(q in d['parity'])}-{at(q,ep,eh)for q in K}
 assert z in outs and d['reads'][z]==[[8,'R']]
 sources.append(dict(actual_source_full=typ,original_common_cell=z,original_base_birth_tick0=8,own_C_tails_preserve_SAME_identity=True,source_full_C_count=typ.count('C'),FOREIGN_C_clock=2,signed_min_first_retirement_from_atomic_ENTRY=3))
cases=[]
for A,p,p2,tick,s,t in(('B',(-2,-4),(1,2,3),72,'4/5','2/5'),('F',(-2,-2),(2,1,3),52,'3/5','4/5')):
 h=2;d=literal(W[mp[A]]['word']+M);raw=literal(W[mp[A]]['word']);loc=rot(sub(z,p),-h);assert d['requirements'][loc]is False and raw['reads'][loc][0]==[tick,'R'];assert loc not in K
 full=literal(W[mp[A]]['word']+W[mp['C']]['word']);actual=at(tuple(full['endpoint'][:2]),p,h);ah=(h+full['endpoint'][2])%4;assert[*actual,ah]==list(p2)
 v=literal(W[mp['V']]['word']);end=at(tuple(v['endpoint'][:2]),p2[:2],p2[2]);eh=(p2[2]+v['endpoint'][2])%4;contact=meet((-1,-1),(1,5),center(p2[:2],p2[2]),center(end,eh));assert tuple(map(str,contact))==(s,t)
 cases.append(dict(foreign=A,FOREIGN_pose=[*p,h],true_old_V_entry_to_FOREIGN_C_age=2,FIRST_ordinary='C',SECOND_ordinary='V',SECOND_pose=p2,source_common_cell=z,common_FOREIGN_local=loc,common_required_before_WHITE=True,first_common_physical_read=dict(owner='own FOREIGN RAW',tick0=tick,read_number1=tick+1,turn='R'),FOREIGN_RAW_has_no_earlier_common_read=True,common_outside_FOREIGN_entryK=True,contact_source_s=s,contact_second_t=t,contradiction='Original common-R8 is CURRENT BLACK before atomicENTRY age3, but at age2 FOREIGN first read requiresWHITE. No old law applied after FOREIGN.'))
D=[BP,R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',R/'second_old_sources_age2_bud_2026-10-24/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Two exact oldV trueFOREIGNage2 residual targets B(-2,-4,S),C,V(1,2,W) andF(-2,-2,S),C,V(2,1,W) are impossible by genuine source commonR8. Standalone guard needs no FIRST-contact premise. Complete oldV2 closure additionally requires independent signed beta-interface exhaustiveness.',actual_three_source_roles=sources,two_targets=cases,no_postFOREIGN_maturity=True,no_actual_countercontrol_claimed=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'common_port_guard.json').write_text(json.dumps(o,indent=2)+'\n');print('Two residual oldV2 targets excluded by SAME common(2,0) R8 min3: ownB RAW72R / ownF RAW52R attrueFOREIGNage2.')
