"""All local cap-four G3 circle corners with middle outgoing L1.
Reconstruct four rotations of two exact geometric types; no front scan.
"""
from pathlib import Path
from itertools import product
import json
H='NESW'
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else -1))%4]
def rot(h,k):return ''.join(H[(H.index(x)+k)%4]for x in h)
base=[]
for h0 in product('EW',repeat=4):
 h=''.join(h0);inc={p:[r for r,x in enumerate(h)if x==p]for p in 'EW'};outs={p:[r for r in range(4)if out(h,r)==p]for p in 'NS'}
 ip=[p for p,rs in inc.items()if len(rs)==3];op=[p for p,rs in outs.items()if len(rs)==3]
 if len(ip)!=1 or len(op)!=1:continue
 pin,pout=ip[0],op[0];ir,orr=inc[pin],outs[pout]
 if orr[1]!=1:continue
 assert ir[1]==2
 turn='RIGHT'if(H.index(pout)-H.index(pin))%4==1 else'LEFT'
 s='LEFT'if turn=='RIGHT'else'RIGHT'
 # At a negative middle corner R0 is on the high/right track or other RIGHT port;
 # L3 is on the low/left track or other LEFT port. These port-rank identities
 # expose both same-side turns rather than dropping boundary-tangent contacts.
 r0=dict(incoming='RIGHT'if 0 not in ir else ('RIGHT'if ir.index(0)==0 else'ERROR'),outgoing='RIGHT'if 0 not in orr else('RIGHT'if orr.index(0)==0 else'ERROR'))
 l3=dict(incoming='LEFT'if 3 not in ir else('LEFT'if ir.index(3)==2 else'ERROR'),outgoing='LEFT'if 3 not in orr else('LEFT'if orr.index(3)==2 else'ERROR'))
 assert set(r0.values())=={'RIGHT'}and set(l3.values())=={'LEFT'}
 base.append(dict(headings=h,gamma_incoming=pin,gamma_outgoing=pout,incoming_ranks=ir,outgoing_ranks=orr,turn=turn,off_circle_side=s,R0=r0,L3=l3,L1='side to middle departure',R2='middle arrival to side'))
assert len(base)==4 and {r['headings']for r in base}=={'EWEE','EWWW','WEEE','WEWW'}
rows=[]
for b in base:
 for k in range(4):
  r=dict(b);r.update(headings=rot(b['headings'],k),gamma_incoming=rot(b['gamma_incoming'],k),gamma_outgoing=rot(b['gamma_outgoing'],k));rows.append(r)
uniq={r['headings']:r for r in rows};assert len(uniq)==8
# Prescribed NE staircase profiles: N->E RIGHT, E->N LEFT.
assert uniq['NSNN']['gamma_incoming']=='N'and uniq['NSNN']['gamma_outgoing']=='E'
assert uniq['WEEE']['gamma_incoming']=='E'and uniq['WEEE']['gamma_outgoing']=='N'
obj=dict(scope=__doc__,base_rows=base,all_rotated_rows=list(uniq.values()),example_NE_staircase=['NSNN','WEEE'],warning='Local complete histories and analytic cycle rigidity only; no attained translating front is asserted.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(dict(base_count=len(base),rotated_count=len(uniq)),indent=2))
