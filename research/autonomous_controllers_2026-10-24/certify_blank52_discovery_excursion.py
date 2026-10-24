#!/usr/bin/env python3
"""One genuine zero-input blank discovery module, not a translating controller."""
from pathlib import Path
from collections import defaultdict
import json,hashlib,sys
from certify_active_C_entry_exit_forests import active_C
from check_extremal_read_coupling import event_word,quotient
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parent/'computability'))
from periodic_tail_checker import first_mismatch
from check_rigid_reachability import State

def main():
 B={};p=(0,0);h=0;V=[(0,1),(1,0),(0,-1),(-1,0)];E=[];states={};firstC={}
 for t in range(60):
  if t in[0,1,53,54,59]:states[t]={'black':sorted(B),'head':p,'heading':h}
  firstC.setdefault(active_C(p,h),t);c='L'if p in B else'R';row={'time':t,'position':p,'heading':h,'turn':c,'active_C':active_C(p,h)}
  if c=='L':row['R_owner']=B.pop(p)
  else:B[p]=t
  E.append(row);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1])
 W=''.join(e['turn']for e in E[:54]);X=W[1:53]
 assert W=='RRRRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLLRRL'
 assert E[1]['position']==E[53]['position']==(1,0)and E[1]['heading']==E[53]['heading']==1 and E[53]['R_owner']==1
 assert all(e['position']!=(1,0)for e in E[2:53])and firstC[(1,0)]==54
 assert states[1]['black']==[(0,0)] and E[4]['R_owner']==0
 assert all(e.get('R_owner',1)>=1 for e in E[1:53]if e['turn']=='L'and e['time']!=4)
 assert states[54]['head']==(1,1)and states[54]['heading']==0 and len(states[54]['black'])==12
 assert len(X)==52 and X.count('R')-X.count('L')==12
 ev,d,h=event_word(W);H=defaultdict(list)
 for e in ev:q,k=quotient(e['p'],d);H[q].append({'canonical_time':e['t']-54*k,'period_lift':k,**e})
 for es in H.values():es.sort(key=lambda e:e['canonical_time'])
 witness=H[(0,-4)];assert [(e['canonical_time'],e['t'],e['c'])for e in witness]==[(-12,42,'R'),(36,36,'R')]
 assert first_mismatch(State(frozenset(),(0,0),0),W)==59 and E[59]['turn']=='L'and W[5]=='R'
 data={'status':'AUTHOR genuine blank discovery excursion and arbitrary-board repetition obstruction; independent audit pending',
  'scope':'A finite no-input R E52 L discovery module outside the four intrinsic standard words. NOT a repeatable controller or a counterexample to any highway conjecture.',
  'whole_module_word':W,'closed_excursion_word':X,'full_states':states,'all60_blank_events':E,'all_first_C_visits':[{'face':q,'first_time':t}for q,t in sorted(firstC.items())],
  'complete_root_history_through_return':[e for e in E[:54]if e['position']==(1,0)],
  'full_drift_stable_histories':[{'class':q,'reads':es}for q,es in sorted(H.items())],
  'arbitrary_board_repetition_conflict':{'class':[0,-4],'complete_history':witness},'exact_first_mismatch_from_blank':59,
  'dependencies':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in[R.parent/'computability/periodic_tail_checker.py',R.parent/'computability/check_rigid_reachability.py']}}
 dest=R/'blank52_discovery_excursion_certificate.json';dest.write_text(json.dumps(data,indent=2)+'\n');print('PASS empty seed R E52 L, first new C entry54, full12-cell output; repeated word impossible on every board');print(hashlib.sha256(dest.read_bytes()).hexdigest())
if __name__=='__main__':main()
