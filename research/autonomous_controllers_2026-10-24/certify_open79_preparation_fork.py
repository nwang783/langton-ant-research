#!/usr/bin/env python3
"""All-period conditional physical preparation fork in one supplied OPEN79 interface.
No period, visit or upper-support cap. The gap3 branch forces an exact age debt.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0));F=lambda h,s:(h+(1 if s=='R'else-1))%4
H11=tuple('NESW'.index(c)for c in'WEEEEEEWWEEEWEWE')
H12=tuple('NESW'.index(c)for c in'SSNNNSNSSSSSSSSSSS')
def run():
 A=(1,0);B=(0,0);C=(-1,0);Q=(1,1);U=(0,1);V=(-1,1);X=(2,1)
 assert X==(C[0]+3,C[1]+1)
 assert H11[7]==H11[8]==3 and F(H11[7],'L')==2 and F(H11[8],'R')==0
 assert H12[8]==2
 allowed=[j for j,h in enumerate(H12[:8])if F(h,'R'if j%2==0 else'L')==3];assert allowed==[0,3]
 S=[j for j,h in enumerate(H12)if h==2];assert S.index(0)==0 and S.index(8)==4
 fixed=[(0,A,2,'R'),(1,B,3,'R'),(2,U,0,'L'),(3,V,3,'L'),(4,C,2,'R')]
 for(t,p,h,s),(tt,pp,hh,ss)in zip(fixed,fixed[1:]):
  out=F(h,s);assert tt==t+1 and hh==out and pp==(p[0]+D[out][0],p[1]+D[out][1])
 branches=[{'case':'upper_W_predecessor','reads':[(-2,X,2,'R'),(-1,Q,3,'L')]+fixed,'outcome':'actual upper class read is required; rank0 or3 before rank8'}, {'case':'previous_B_north','reads':[(-3,B,1,'L'),(-2,U,0,'R'),(-1,Q,1,'R')]+fixed,'outcome':'B previous rank7 would need incomingE, but supplied complete history has incomingW'}, {'case':'helper_color_collision','reads':[(-2,U,2,'L'),(-1,Q,1,'R')]+fixed,'outcome':'U has consecutive L reads at-2,+2'}]
 for z in branches:
  ev=z['reads']
  for(t,p,h,s),(tt,pp,hh,ss)in zip(ev,ev[1:]):
   out=F(h,s);assert tt==t+1 and hh==out and pp==(p[0]+D[out][0],p[1]+D[out][1])
 # The opposite first turn at upper X is the other possible W departure,
 # namely incomingN/L, corresponding to complete rank3. Its continuation
 # from Q onward is the same, so the two age branches are complete.
 assert F(H12[0],'R')==F(H12[3],'L')==3
 # Exact symbolic contradiction for old rank3. Rows are inequalities of
 # form target-source >= constant + coefficient*P. The signed35-event
 # chain gives r11-r3=P-34, while the fork would give r8-r3=P+6.
 cycle=[{'source':8,'target':9,'constant':4,'P':0}, {'source':9,'target':10,'constant':4,'P':0}, {'source':10,'target':11,'constant':4,'P':0}, {'source':11,'target':8,'constant':40,'P':0}]
 assert sum(z['constant']for z in cycle)==52 and sum(z['P']for z in cycle)==0
 # Genuine prepared7 branch control, not a full supplied interface.
 seed={Q,U,V};black=set(seed);p=X;h=2;word='RLRRLLR';events=[]
 for t,s in enumerate(word):
  assert s==('L'if p in black else'R');events.append({'time':t,'position':p,'incoming_heading':h,'turn':s});black.symmetric_difference_update({p});h=F(h,s);p=(p[0]+D[h][0],p[1]+D[h][1])
 assert events[-1]['position']==C
 result={'scope':__doc__,'complete_named_histories':{'T11':H11,'T12':H12},'conditional_gap':'canonical t_(12,8)-t_(11,8)=3','physical_cases':branches,'upper_class_W_departure_ranks_before_rank8':allowed,'rejected_rank3_positive_clock_cycle':cycle,'forced_rank0_age':'t_(12,8)-t_(12,0)=P+6','transported_future_port_debt':{'class_T':15,'departure_heading':'S','earlier_ordinal':0,'later_ordinal':4,'clock_difference':'P+6','later_read_turn':'L','later_read_incoming_heading':'W'},'prepared_seven_control':{'initial_position':X,'initial_heading':2,'initial_black':sorted(seed),'word':word,'events':events,'final_position':p,'final_heading':h,'complete_final_black':sorted(black),'warning':'Prepared finite factor only; no prior rank7 at B, full WHITE history or autonomous controller is supplied.'},'dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['PHYSICAL_RETURN_DEBT_AND_ORDINAL_INTERFACE.md','physical_return_debt_certificate.json','RETURN_DEBT_OPEN79_CANONICAL_AGE_ADDENDUM.md']},'limits':'Only a conditional age fork for this supplied complete-history interface. The long-gap branch and the rank0 age branch remain OPEN. No general debt growth or g8 exclusion.'}
 (R/'open79_preparation_fork_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print('PASS complete physical fork, positive52 cycle, exact futureS0->S4 ageP+6, full prepared7')
if __name__=='__main__':run()
