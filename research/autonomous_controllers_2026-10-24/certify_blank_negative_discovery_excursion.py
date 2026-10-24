#!/usr/bin/env python3
"""A finite blank-derived negative-growth first-C discovery excursion."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
from check_extremal_read_coupling import D,event_word
from certify_active_C_entry_exit_forests import active_C
R=Path(__file__).resolve().parent

def main():
 B={};p=(0,0);h=0;E=[];H=defaultdict(list);C=defaultdict(list);states=[]
 for t in range(599):
  if t in[0,581,593,594,598]:states.append({'time':t,'whole_black_field':sorted(B),'head':p,'heading':h})
  if t==598:break
  turn='L'if p in B else'R';e={'time':t,'position':p,'incoming_heading':h,'turn':turn,'active_C_face':active_C(p,h)}
  if turn=='L':e['actual_R_owner']=B.pop(p)
  else:B[p]=t
  E.append(e);H[p].append(e);C[e['active_C_face']].append(e);h=(h+(1 if turn=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 word=''.join(e['turn']for e in E[581:593]);assert word=='RRLLLLRLLLLR';assert word.count('R')-word.count('L')==-4
 root=(7,2);assert[H[root][i]['time']for i in[0,1]]==[581,593];assert E[581]['incoming_heading']==E[593]['incoming_heading']==1
 assert C[(7,2)][0]['time']==594 and E[593]['active_C_face']==(6,1);assert E[594]['active_C_face']==(7,2)
 assert all(e['position']!=root for e in E[582:593]);assert E[593]['actual_R_owner']==581
 inputs=[e for e in E[581:593]if e['turn']=='L'and e['actual_R_owner']<581];assert[e['actual_R_owner']for e in inputs]==[579,572,577,580,553,554]
 internal=[e for e in E[581:593]if e['turn']=='L'and e['actual_R_owner']>=581];assert[e['actual_R_owner']for e in internal]==[582,587]
 before=next(a for a in states if a['time']==581);after=next(a for a in states if a['time']==593);assert len(after['whole_black_field'])==len(before['whole_black_field'])-4
 read={e['position']for e in E[581:593]};unread=set(before['whole_black_field'])-read;assert unread==set(after['whole_black_field'])-read
 out={'status':'AUTHOR complete literal replay; independent audit pending','scope':'Finite transient from the empty seed, not a translating complete-WHITE front or a per-exit-component counterexample. It rejects a proposed general local positivity premise, not a periodic classification statement.',
  'full_initial_seed':[],'all598_literal_reads_and_R_owners':E,'whole_checkpoint_fields':states,'root_first_two_reads':H[root][:2],
  'child_C_first_activation':C[(7,2)][0],'parent_C_first_activation':C[(6,1)][0],
  'excursion_word':word,'excursion_start':581,'excursion_end_excluded':593,'excursion_growth':-4,
  'six_inputs_at_excursion_entry_with_actual_prior_R_owners':inputs,'two_internal_consumptions':internal,
  'complete_untouched_field_during_excursion':sorted(unread),'dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in['ACTIVE_C_FIRST_ENTRY_LAST_EXIT_OWNERSHIP.md','C_CYCLE_EXCURSIONS_AND_STANDARD_SELF_FEEDING.md','PHYSICAL_EXIT_COMPONENT_COLOR_TURN_AND_BOUNDARY_FLUX.md']}}
 dest=R/'blank_negative_discovery_excursion_certificate.json';dest.write_text(json.dumps(out,indent=2)+'\n');print('PASS empty-seed E12 negative first-C excursion',[(a['time'],len(a['whole_black_field']))for a in states]);print(hashlib.sha256(dest.read_bytes()).hexdigest())
if __name__=='__main__':main()
