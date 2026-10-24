from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();base=S.with_name('check_old_V_third_young_independent.json');assert sha(base)=='b13b262f9f18b4775a4f643d702c9f2fcb891de31a935bc6a5f300a6b51f00bb'
ns={'__file__':str(S.with_name('check_old_V_third_young_independent.py'))};exec(Path(ns['__file__']).read_text().split('out=dict(')[0],ns)
meet,pieces,J=ns['meet'],ns['pieces'],ns['J'];corrections=ns['collinear_adjacent_flag_corrections'];actual_earlier=[];terminal_contacts=[]
for z in J['all100_complete_board_controls']:
 pp=pieces(z['tokens'])
 for j in range(len(pp)):
  for i in range(j):
   h=meet(*pp[i],*pp[j])
   if h is None or(j==i+1 and h==(1,0)):continue
   if j<len(pp)-1 or h[0]=='OVERLAP' or h[1]<1:actual_earlier.append((z['tokens'],i,j,str(h)))
   else:terminal_contacts.append((z['tokens'],i,j,str(h)))
assert len(corrections)==180 and not actual_earlier
out=dict(status='MANDATORY correction of prepared-contact metadata/prose; main endpoint and ancestry PASS unchanged',base_report=sha(base),all100_complete_controls_rechecked=True,collinear_adjacent_joins_false_in_nonparallel_flag=180,actual_nonadjacent_contacts_before_third_terminal=0,terminal_contact_incidence_count=len(terminal_contacts),corrections=corrections,scope='The false true_adjacent_endpoint flags at collinear consecutive joins are not actual earlier contacts. The author prose and ONE analytic sentence in b13b262f saying some earlier contacts were confirmed are incorrect; this addendum explicitly replaces that sentence. The mathematical source exclusion rests on endpoint exhaustion and complete reverse ancestry, not a prepared-simple-history assumption. No stronger general simplicity theorem is promoted. Frozen source and base report remain unchanged.');S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
