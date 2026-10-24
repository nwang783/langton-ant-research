from pathlib import Path
from collections import Counter
import hashlib,json
SELF=Path(__file__).resolve();R=SELF.parents[1];p=SELF.parent/'check_returned_V_source_reduction_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('mins=')[0],ns)
walk,W,M,xy,raw,ctx,I,outputs,K=[ns[x]for x in('walk','W','M','xy','raw','ctx','I','outputs','K')];D=R/'seven_word_spatial_return_2026-10-23';pairs=[]
for n in raw:
 for source in('D','DC'):
  word=''.join(W[c]for c in n+source)+M;a=walk(word);ep=raw[n]['p'];h=-raw[n]['h']%4;e=-ep*(-1j)**h
  if a['feasible']:assert n not in('VCC','UCC');z={'feasible':True}
  else:
   assert n in('VCC','UCC');off=a['i']-sum(len(W[c])for c in n);assert off==11
   z={'feasible':False,'absolute_tick0':a['i'],'cell':xy(a['q']),'following_D_context_tick0':off,'physical_owner':'following actual word tick1/read2'if source=='D'else'own C1 tick1/read2'}
  pairs.append({'predecessor':n,'source':source,'predecessor_pose':[xy(e),h],**z})
assert len(pairs)==16 and sum(not q['feasible']for q in pairs)==4
assert raw['U']['p']==4j and raw['U']['h']==0
Uentry=-4j;east={2-4j,2-3j}
for q in(2,2+1j):
 assert q in outputs['U'];assert[(i,c)for i,(p,h,c)in enumerate(raw['U']['reads'])if p==q][-1][1]=='R'
cat=json.loads((D/'first_returned_atom_contact.json').read_text())['old_source_contact_cases'];cases=[]
for ix,source in [(15,'D'),(15,'DC'),(30,'D'),(30,'DC'),(75,'DC')]:
 r=cat[ix];fp=complex(*r['foreign_pose'][:2]);fh=r['foreign_pose'][2]
 if r['source_atom']=='C':fp+=raw['D']['p']
 assert r['source_to_foreign_C_age']==3 and r['foreign']=='F'and fh==1
 core={fp+q*(-1j)for q in K};hit=sorted(east&core,key=xy);assert hit
 checks=[]
 for q in hit:
  loc=(q-fp)*1j;rd=next((i,c)for i,(p,h,c)in enumerate(walk(W['F'])['reads'])if p==loc);assert rd[1]=='L';checks.append((xy(q),xy(loc),rd[0],rd[0]+1))
 cases.append({'catalogue':ix,'source':source,'U_entry':xy(Uentry),'foreign_entry':xy(fp),'U_entry_C_age':3,'first_cycle_break_age':4,'current_east_identity_core_hits':checks})
for f,fp in [('Q',5-4j),('B',6-3j)]:assert not east&{fp+q*(-1j)for q in K}
beta=1-1j;assert beta not in raw['DC']['req'];oldports=[]
for f,fp in [('F',3-4j),('Q',5-4j),('B',6-3j)]:
 loc=(beta-fp)*1j;rr=walk(W[f]);cc=walk(W[f]+W['C']+M);assert loc not in rr['req']and cc['req'][loc]is True
 rd=next((i,c)for i,(p,h,c)in enumerate(cc['reads'])if p==loc);assert rd==(len(W[f])+1,'L');oldports.append((f,xy(fp),xy(beta),rd))
mp=D/'D_family_immediate_U_F_guard_manifest.json';mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='6bdd9307aa52c13b02df4b101236834f9202001f247fe62a8b6c3463d3807315';manifest=json.loads(mp.read_text())
for f,h in manifest['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in manifest['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
# Independently inspect the accompanying five-label set/role join.
front=json.loads((D/'first_returned_five_label_frontier.json').read_text());assert Counter(r['source_atom']for r in cat)==front['disjoint_source_counts'];assert front['remaining_catalogue_IDs']==[15,30,75,76,77]
for row in front['all_five_necessary_labels_with_actual_fullsource_roles']:
 ix=row['catalogue_case'];assert all(row[k]==cat[ix][k]for k in cat[ix]);roles=row['remaining_actual_containing_fullsource_roles']
 assert [q['full_packet']for q in roles]==(['D','DC']if ix in(15,30)else['DC'])and all(q['full_source_C_age']==3 for q in roles)
for q in ('check_returned_D_source_join_independent','check_returned_C_source_reduction_independent','check_returned_C_double_tail_independent','check_earliest_W_portal_guard_independent','check_returned_C_UC_F_core_guard_independent','check_returned_C_VC_UC_guard_lift_independent','check_returned_V_residual_guards_independent','check_returned_U_source_join_independent'):
 assert json.loads((R/'audits'/f'{q}.json').read_text())['status'].startswith('PASS')
fm=D/'first_returned_five_label_frontier_manifest.json';fmanifest=json.loads(fm.read_text())
for f,h in fmanifest['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in fmanifest['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS narrow immediate plain-U predecessor exclusion for two F targets; accompanying five-label dependency join verified','manifest_sha256':mh,'five_label_join_manifest_sha256':hashlib.sha256(fm.read_bytes()).hexdigest(),'all16_predecessor_pairs':pairs,'five_actual_role_guards':cases,'retained_old_beta_ports':oldports,'analytic':['An immediately preceding PLAIN U starts(0,-4,N), has no C word, and ends at selected D/DC entry(0,0,N). Its source-entry clock and selected D entry clock therefore agree. Old C1 of DC also begins at that clock, after the zero-C D base. All five foreign entries are exactly age3 from this genuine U, not a shifted full-source clock.','The two original east-cycle last-R identities are genuine U outputs and are preserved until the first old-eight cycle retirement, which has exact age4 by the signed renewal law. At the age3 foreign cut they are still current residual identities. No persistence is asserted after the foreign.','Each target F entry core contains at least one of these current residuals. The previous actual full eight packet already recognizes the common entry marker and requires residual/core disjointness, so this is a preforeign impossibility, not an inference merely from the fact that the physical F read is BLACK. The raw first-L checks only identify the concrete core cells.','Q/B cores miss the two identities and remain open; an immediate UC predecessor has a different creator clock/heading and is not covered. The all16 literal pair table excludes only VCC/UCC necessary prefixes at actual D context11, with correct tail/next-word read2 ownership.','For the three C-channel DC-source poses, beta=(1,-1) is RAW-unread by DC and the foreign and is required by returnedC read2. It can be an older surviving identity; no source-deletion or fresh-origin premise is fabricated.','The five-label join is only the disjoint signed-source partition371-(148+112+48+58)=5, with retained D/DC and DC-C1 roles. Existing positive fixed D-entry controls have no U-entry lift, but this does not close alternative U-entry histories at these five targets.'],'scope':'Immediate plain-U predecessor cut only. No all-target closure, returned simplicity, second-foreign induction, bi-exterior premise or global capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
