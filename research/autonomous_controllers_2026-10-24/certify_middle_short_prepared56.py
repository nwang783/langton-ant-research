#!/usr/bin/env python3
"""One exact non-dictionary exterior return, and its all-unread suffix trap."""
from pathlib import Path
import json,hashlib
from certify_middle_short_return_dictionary import literal
from certify_active_C_entry_exit_forests import active_C
from check_extremal_read_coupling import event_word,D
R=Path(__file__).resolve().parent
PRE='RRRRLRRRRLLLLRLLRRRRLLRLLRRRRLLR';E='RRRLLRLRRLRRLRRLRLLR';G='LLLL';W=PRE+E+G;ROOT=(-8,0)
def main():
 z=literal(W);assert z['legal']and len(W)==56 and z['final_position']==ROOT and z['final_heading']==2
 assert len(z['full_minimal_initial_black'])==6 and len(z['full_final_black'])==12
 assert z['full_minimal_initial_black']==[(-10,1),(-9,-1),(-9,4),(-8,2),(-8,4),(-7,1)]
 B={p:None for p in z['full_minimal_initial_black']};states=[];events=[]
 for e in z['events']:
  t=e['t'];p=e['p'];row={**e}
  if t in[0,32,52]:states.append({'time':t,'whole_black_field':sorted(B),'head':p,'heading':e['hi']})
  if e['c']=='L':assert p in B;row['actual_R_owner_within_factor']=B.pop(p);row['input_lifetime']=row['actual_R_owner_within_factor']is None
  else:assert p not in B;B[p]=t
  events.append(row)
 states.append({'time':56,'whole_black_field':sorted(B),'head':ROOT,'heading':2})
 assert len(states[1]['whole_black_field'])==12 and len(states[2]['whole_black_field'])==16
 assert events[54]['p']==(-7,1) and events[54]['c']=='L'and events[54]['input_lifetime']
 ee,dd,hh=event_word(E,h=2,p=ROOT);assert dd==(0,0)and hh==2 and all(e['p']!=ROOT for e in ee[1:])
 levels=[3*active_C(e['p'],e['hi'])[1]-active_C(e['p'],e['hi'])[0]for e in ee];assert min(levels)>=7
 assert ''.join(e['c']for e in events[52:])==G
 # All prefix-read cells have determined colors; only the first new T7 copy branches.
 fixed={e['p']for e in z['events']};known={p:p in B for p in fixed};branches=[]
 for choice in ['R','L']:
  board=dict(known);p=ROOT;h=2;trace=[];new=[]
  for t in range(20):
   cface=active_C(p,h);lev=3*cface[1]-cface[0]
   if lev in[1,3,5]:
    assert t>0 and p!=ROOT;branches.append({'chosen_turn_at_only_unknown_cell':choice,'actual_prefix':trace,'forced_next_read':{'position':p,'heading':h,'C_face':cface,'C_level':lev,'relative_time':t},'new_cell_decisions':new});break
   if p not in board:
    assert p==(-10,-1)and t==3;new.append({'position':p,'relative_time':t,'chosen_turn':choice});c=choice
   else:c='L'if board[p]else'R'
   trace.append({'relative_time':t,'position':p,'heading':h,'turn':c,'C_face':cface,'C_level':lev});board[p]=c=='R';h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1]);assert p!=ROOT
  else:assert False
 assert [b['forced_next_read']['relative_time']for b in branches]==[7,4]
 assert [b['forced_next_read']['C_level']for b in branches]==[3,5]
 out={'status':'AUTHOR checked, independent audit pending','scope':'One complete prepared56 factor, not a complete front or controller. Its exact prefix cannot be followed by the required core-avoiding E2, even after arbitrary changes to every unread initial cell.',
  'word':W,'initial_pose':[ROOT,0],'whole_initial_black':z['full_minimal_initial_black'],'whole_final_black':z['full_final_black'],'final_pose':[ROOT,2],
  'all56_events_with_exact_input_or_R_owners':events,'whole_checkpoint_fields':states,'nonstandard_E1':{'word':E,'length':20,'growth':4,'active_C_levels':levels},
  'G_word':G,'retained_unpaid_T10_lifetime':events[54],'all_two_unread_continuation_branches':branches,
  'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in['MIDDLE_SHORT_RETURN_INTERFACE_AND_STANDARD_DICTIONARY_OBSTRUCTION.md','middle_short_return_dictionary_certificate.json','MIDDLE_SHORT_C_CORE_FOUR_CHANNEL_OWNER_INTERFACE.md']}}
 p=R/'middle_short_prepared56_certificate.json';p.write_text(json.dumps(out,indent=2)+'\n');print('PASS prepared56 full6->12 field, E20, both arbitrary-unread continuation branches',hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
