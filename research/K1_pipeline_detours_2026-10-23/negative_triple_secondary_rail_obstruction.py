"""Fixed secondary-rail closure of the homogeneous negative G3 staircase.
All1..4 WHITE histories at U and V; no front, period or drift scan.
"""
from itertools import product
from pathlib import Path
import json
H='NESW'
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else -1))%4]
def ports(h,p,kind):return[r for r in range(len(h))if(h[r]if kind=='in'else out(h,r))==p]
U=[];V=[]
for n in range(1,5):
 for hs in product('NS',repeat=n):
  h=''.join(hs)
  if len(ports(h,'S','in'))==len(ports(h,'W','out'))==1:
   ir=ports(h,'S','in')[0];orr=ports(h,'W','out')[0]
   # input S is beta+1, output W is alpha-3, beta-alpha>=4.
   # Thus input MUST be later local rank than output.
   U.append(dict(headings=h,incoming_S_rank=ir,outgoing_W_rank=orr,survives=ir>orr))
 for hs in product('EW',repeat=n):
  h=''.join(hs)
  if len(ports(h,'E','in'))==len(ports(h,'N','out'))==3:
   V.append(dict(headings=h,incoming_E_ranks=ports(h,'E','in'),outgoing_N_ranks=ports(h,'N','out')))
assert {r['headings']for r in U}=={'S','NNNS','NSNN'}
assert [r['headings']for r in U if r['survives']]==['NNNS']
assert {r['headings']for r in V}=={'EEWE','WEEE'}
u='NNNS';up_out=ports(u,'E','out');up_in=ports(u,'N','in')
assert up_out==[0,2,3]and up_in==[0,1,2]
for v in V:
 assert v['incoming_E_ranks'][2]==v['outgoing_N_ranks'][2]==3
 assert up_out[2]==3 and up_in[2]==2
obj=dict(scope=__doc__,main_gamma_profiles={'A':'NSNN','B':'WEEE'},coordinates={'A_k':['k','k'],'B_k':['k+1','k'],'U_k':['k+1','k-1'],'V_k':['k+2','k-1']},U_profiles=U,V_profiles=V,U_outgoing_E_ranks=up_out,U_next_incoming_N_ranks=up_in,forced_actual_factor='U_k.L3 -> V_k.L3 -> U_(k+1).R2',forced_time='T2(U_(k+1))=T3(U_k)+2>=T2(U_k)+6',full_quotient='gamma has NE displacement(a,a)=-d, so U_(k+a)=U_k-d and T2(U_(k+a))=T2(U_k)-P; contradiction.',warning='This excludes an exact necessary full-WHITE cap4 homogeneous-negative G3 mode, not arbitrary mixed-sign circles or higher-cap fronts.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(dict(U_profiles=U,V_profiles=V),indent=2))
