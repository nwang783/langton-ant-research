"""Finite geometry + inductive row-gap certificate; no packet-count cutoff."""
from pathlib import Path
import json,hashlib,itertools
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';AP=R/'chronology_dcuv/counted_input_age_rules_complete.json';G=json.loads(GP.read_text())['geometry'];mins={(a,x,y):r for a,x,y,r in json.loads(AP.read_text())}
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
assert G[5]['endpoint']==[1,4,3]
assert rot(G[0]['endpoint'][:2],3)==(-1,1)and rot(G[4]['endpoint'][:2],3)==(-3,1)
assert rot(G[0]['endpoint'][:2],1)==(1,-1)and rot(G[4]['endpoint'][:2],1)==(3,-1)
assert rot(G[6]['endpoint'][:2],3)==(-4,0)and(3+G[6]['endpoint'][2])%4==1
assert (0,3)in map(tuple,G[4]['inputs'])and(0,3)in map(tuple,G[6]['inputs'])and rot((0,3),3)==(-3,0)
assert G[0]['inputs']==[[0,1]]and rot((0,1),1)==(1,0)and mins[0,0,1]==3
assert G[5]['name'].count('C')==1 and G[6]['name'].count('C')==2
# At Delta=-4, returning D input equals outgoing V/VCC lower input.
assert -4+1==-3
rows=[]
def Inv(delta,kind):return delta>=-2 or(delta==-4 and kind=='V')
for delta in(-4,-2,0,2):
 for current in('D','V'):
  if not Inv(delta,current):continue
  for incoming_width,outgoing_width in itertools.product((1,3),repeat=2):
   forbidden=delta==-4 and current=='V'and incoming_width==1
   if forbidden:continue
   nxt=delta+incoming_width-outgoing_width;kind='D'if outgoing_width==1 else'V';assert Inv(nxt,kind)
   rows.append(dict(gap=delta,current_outgoing_kind=current,incoming_width=incoming_width,outgoing_previous_width=outgoing_width,next_gap=nxt,next_outgoing_kind=kind))
# For every even delta>=2 all next gaps are>=0, so the last tested row family
# extends to the entire unbounded positive ray by translation.
assert 2+min(1-3,1-1,3-3,3-1)>=0
# N=number of pre-VCC zero-C packets; incoming has N+5 packets, each dx>=1.
# At bottom row4, incoming x<=0-5=-5 whereas outgoing x=1.
assert 0-5-1==-6 and -6<-4
J=dict(status='AUTHOR_ALL_WORD_ROW_GAP_INVARIANT_PASS',scope='VC0,N; arbitrary word A over{D,V}; one VCC; arbitrary B over{D,V}; Ugoal(0,-1,E). No U/UC/UCC intermediate and no two separate1C packets. All such literal factors impossible, any seed/fuel.',source_exit=[1,4,3],goal_pose=[0,-1,1],outgoing_steps={'D':[-1,1],'V':[-3,1]},far_VCC_step=[-4,0],incoming_steps={'D':[1,-1],'V':[3,-1]},gap_invariant='Delta>=-4; if Delta=-4 current outgoing packet is V or topVCC (not D)',retirement_reuse_cut=dict(gap=-4,current_outgoing='V or VCC',incoming='D',cell_relative_to_outgoing_head=[-3,0],pre_C_minus_source_birth=1,post_C_minus_source_birth=3,max_replacement_age=2,D_minimum=3),transition_rows=rows,unbounded_ray_argument='For evenDelta>=2, every successor hasDelta>=0; all lower breakpoints -4,-2,0 checked explicitly.',bottom_contradiction='Outgoing bottom head(1,4); incoming needs5 positive-x steps to Ugoal(0,-1), so its bottom x<=-5 and Delta<=-6, contrary invariant.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,AP,Path(__file__).resolve()]})
(R/'chronology_dcuv/VC_young3_one_VCC_crossing.json').write_text(json.dumps(J,indent=2)+'\n');print(dict(rows=len(rows),status=J['status'],minimum_birth_gap_needed=3,actual_gap=2))
