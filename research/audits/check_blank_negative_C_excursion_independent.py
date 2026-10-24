from pathlib import Path
from collections import defaultdict
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files={'BLANK_NEGATIVE_FIRST_C_DISCOVERY_EXCURSION.md':'c563553da500eb3a08970930876a3c09f0ffd7d87ce5c01399033491d80903ca','certify_blank_negative_discovery_excursion.py':'e3854745944f99eabc237dc955d1647d120bb2e28a5254cca1e9de76b8a741d2','blank_negative_discovery_excursion_certificate.json':'b36aa7211310982123f81276028447e1a944947f5c3c0e2600a1127f05a3877f'}
for f,h in files.items():assert sha(D/f)==h
ref=json.loads((D/'blank_negative_discovery_excursion_certificate.json').read_text())
for f,h in ref['dependency_hashes'].items():assert sha(D/f)==h
V=(1j,1,-1j,-1);off=(-1j,-1-1j,-1,0);xy=lambda p:[int(p.real),int(p.imag)];B={};p=0j;h=0;E=[];hist=defaultdict(list);faces=defaultdict(list);states=[]
for t in range(599):
 if t in[0,581,593,594,598]:states.append(dict(time=t,whole_black_field=sorted(map(xy,B)),head=xy(p),heading=h))
 if t==598:break
 face=p+off[h];c='L'if p in B else'R';e=dict(time=t,position=xy(p),incoming_heading=h,turn=c,active_C_face=xy(face))
 if c=='L':e['actual_R_owner']=B.pop(p)
 else:B[p]=t
 E.append(e);hist[p].append(e);faces[face].append(e);h=(h+(1 if c=='R'else-1))%4;p+=V[h]
assert E==ref['all598_literal_reads_and_R_owners']and states==ref['whole_checkpoint_fields'];word=''.join(e['turn']for e in E[581:593]);assert word=='RRLLLLRLLLLR';assert hist[7+2j][:2]==ref['root_first_two_reads']and [x['time']for x in hist[7+2j][:2]]==[581,593];assert E[581]['incoming_heading']==E[593]['incoming_heading']==1 and E[593]['actual_R_owner']==581
assert faces[7+2j][0]==ref['child_C_first_activation']and faces[6+1j][0]==ref['parent_C_first_activation'];assert faces[7+2j][0]['time']==594 and faces[6+1j][0]['time']==579
old=[e for e in E[581:593]if e['turn']=='L'and e['actual_R_owner']<581];inside=[e for e in E[581:593]if e['turn']=='L'and e['actual_R_owner']>=581];assert old==ref['six_inputs_at_excursion_entry_with_actual_prior_R_owners']and inside==ref['two_internal_consumptions'];assert [e['actual_R_owner']for e in old]==[579,572,577,580,553,554]
bef=set(map(tuple,states[1]['whole_black_field']));aft=set(map(tuple,states[2]['whole_black_field']));read={tuple(e['position'])for e in E[581:593]};assert len(aft)-len(bef)==-4 and bef-read==aft-read==set(map(tuple,ref['complete_untouched_field_during_excursion']))
out=dict(status='PASS literal blank-derived negative-growth first-C discovery excursion only',sources=files,full_literal_reads=598,whole_cut_masses=[(x['time'],len(x['whole_black_field']))for x in states],word=word,old_inputs=[(e['time'],e['actual_R_owner'])for e in old],internal_inputs=[(e['time'],e['actual_R_owner'])for e in inside],analytic_review=['The root first two physical reads are SAME-heading R581 and L593, with no intervening root visit; the12-update factor returns the entire head pose. The child C face is genuinely first activated only after L593, while its parent was active at579.','All six imported BLACK lifetimes were written earlier in the same literal EMPTY-seed run. Their presence at the factor entry is retained, along with every untouched BLACK cell and full fields. Growth is -4, but the factor is not a complete translating WHITE-front excursion.','This excludes only generic finite blank-discovery positivity. It does not refute a periodic WHITE component theorem, supply a repeatable controller, or imply a component output lower bound.'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
