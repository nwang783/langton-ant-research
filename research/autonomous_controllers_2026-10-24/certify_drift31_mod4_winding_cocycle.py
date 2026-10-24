#!/usr/bin/env python3
"""Exact 24-state turn-position cocycle and its full-WHITE odd-inventory law.
No period/multiplicity cap. Discovery through weighted transfer is not premise.
"""
from pathlib import Path
from itertools import product
import json,hashlib
from check_extremal_read_coupling import event_word,quotient,front,D
R=Path(__file__).resolve().parent
WEIGHT=(0,1,3,1,2,2,2,3,1,3,0,0)
PSI={(0,0):0,(0,2):0,(1,1):2,(1,3):0,(2,0):3,(2,2):1,(3,1):2,(3,3):0,(4,0):0,(4,2):0,(5,1):2,(5,3):2,(6,0):0,(6,2):0,(7,1):0,(7,3):2,(8,0):3,(8,2):1,(9,1):0,(9,3):2,(10,0):0,(10,2):0,(11,1):0,(11,3):0}
def T(p):return 3*p[1]-p[0]
def kinematic(w,h=0,p=(0,0)):
 ev,d,hend=event_word(w,h,p);total=sum(WEIGHT[T(e['p'])%12]*(1 if e['c']=='R'else-1)for e in ev)
 end=(p[0]+d[0],p[1]+d[1]);rhs=d[1]+PSI[T(end)%12,hend]-PSI[T(p)%12,h]
 assert(total-rhs)%4==0;return ev,d,hend,total%4

def main():
 transitions=[]
 for(t,h),v in sorted(PSI.items()):
  assert t%2==h%2
  for sig in(-1,1):
   hh=(h+sig)%4;dx,dy=D[hh];tt=(t+3*dy-dx)%12;lhs=(PSI[tt,hh]-v)%4;rhs=(WEIGHT[t]*sig-dy)%4;assert lhs==rhs
   transitions.append({'source':[t,h],'turn_sign':sig,'target':[tt,hh],'dy':dy,'potential_difference':lhs,'weighted_turn_minus_dy':rhs})
 assert len(transitions)==48
 count={}
 for P in(6,10,14):
  n=0
  for chars in product('RL',repeat=P):
   w=''.join(chars);ev,d,hend,total=kinematic(w)
   if d==(3,1)and hend==0:assert total==1;n+=1
  count[P]=n
 assert count=={6:2,10:30,14:420}
 # Actual finite-support standard control. Translate its start by(1,0) so
 # horizontal incoming headings lie on odd T. Three periods preserve T mod12.
 sp=R.parent/'recovered_bundle/ant_global/root/standard.json';std=json.loads(sp.read_text());w=std['word']*3;summary=front(w,std['heading']);assert summary['complete_white']
 ev,d,hend,total=kinematic(w,std['heading'],(1,0));assert d==(-6,-6)and(3*d[1]-d[0])%12==0
 H={}
 for e in ev:
  q,k=quotient(e['p'],d);H.setdefault(q,[]).append((e['t']-k*len(w),e))
 odd=[]
 for q,es in H.items():
  es.sort();turns=[e['c']for t,e in es];assert turns==['R'if i%2==0 else'L'for i in range(len(es))]
  if len(es)%2:odd.append(q)
 assert sum(WEIGHT[T(q)%12]for q in odd)%4==d[1]%4==2
 # Prepared six-read positive drift control, explicitly NOT a WHITE front.
 pw='RLRRLL';pe,pd,ph,pt=kinematic(pw);assert pd==(3,1)and ph==0
 black={e['p']for e in pe if e['c']=='L'};initial=sorted(black);p=(0,0);h=0
 for e in pe:
  assert p==e['p']and h==e['hi'];turn='L'if p in black else'R';assert turn==e['c'];black.symmetric_difference_update({p});h=e['ho'];p=(p[0]+D[h][0],p[1]+D[h][1])
 assert len(initial)==3 and len(black)==3
 # Full middle-short family: algebraic parity controls with huge parameters,
 # supplemented by the symbolic formula in the note, not extrapolation.
 pc=[]
 for c,a in[(2,2),(3,3),(2,3),(3,10),(10**30,10**30+7),(10**30+1,10**30+100)]:
  O=[0,1,2,6,7,6*c+1,6*a+2,6*a+4];z=sum(WEIGHT[t%12]for t in O)%4;assert z==(3+2*c)%4
  pc.append({'a':a,'c':c,'full_odd_levels':O,'weighted_sum_mod4':z,'passes_necessary_winding':z==1})
 result={'scope':__doc__,'weight_by_T_mod12':WEIGHT,'potential24_states':[{'state':k,'value':v}for k,v in sorted(PSI.items())],'all48_transition_checks':transitions,'literal_geometric_controls':count,'actual_standard312_control':{'source_sha256':hashlib.sha256(sp.read_bytes()).hexdigest(),'word':w,'heading':std['heading'],'start_position':[1,0],'full_drift':d,'complete_white_summary':summary,'all_odd_class_representatives':odd,'weighted_sum_mod4':2,'warning':'Three standard periods, not a new primitive controller and not drift(3,1).'},'prepared_six_read_control':{'word':pw,'start_position':[0,0],'start_heading':0,'initial_black':initial,'events':pe,'final_position':p,'final_heading':h,'complete_final_black':sorted(black),'signed_turn_weight_sum':pt,'incorrect_all_WHITE_odd_sum':sum(WEIGHT[T(e['p'])%12]for e in pe)%4,'warning':'Finite prepared factor only. Repetition needs BLACK-first classes forever, so it is not a finite-seed controller.'},'middle_short_symbolic_formula':'weighted_sum = 3+2*c modulo4; exact full winding1 forces c odd, hence c>=3. a>=c remains unrestricted.','parameter_controls':pc,'limits':'This is a necessary full-odd-inventory obstruction. No exclusion of all odd c, no period bound, no new finite controller.'}
 (R/'drift31_mod4_winding_cocycle_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print('PASS48 transitions;',count,'standard312 and finite prepared6; middle c must be odd')
if __name__=='__main__':main()
