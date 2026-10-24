"""V left-core causal lock removes two odd parallel reproductive ports.
Simple-center retained factor required. Finite local masks, no prefix search.
"""
from pathlib import Path
exec((Path(__file__).resolve().parent/'literal_helpers.py').read_text())
from collections import Counter
R0=(0,0);A=(0,1);B=(1,0);C=(2,1);roles={a:0 if a in(0,1,6)else 1 if a in(4,5)else 4 for a in IDS}
def ep(a,p,h):
 x,y,dh=G[a]['endpoint'];return place((x,y),p,h),(h+dh)%4
def single(hit,p):return hit==[[str(p[0]),str(p[1])]]or hit==[list(p)]
def forbidden_source_contact(s,a,p,h):
 src=chords(s);cc=chords(a,p,h);se,sh=ep(s,(0,0),0)
 for i,old in enumerate(src):
  for j,new in enumerate(cc):
   hit=contact(*old,*new)
   if hit and not(i==len(src)-1 and j==0 and(p,h)==(se,sh)and single(hit,old[1])):return True
 return False
rootrows=[];rootcases=[];selectedrows=[];selectedcases=[]
for s in(4,5,6):
 assert{R0,A,B,C}<=set(map(tuple,G[s]['outputs']))
 for a in IDS:
  for h in range(4):
   for slot,q in enumerate(G[a]['inputs']):
    p=sub(R0,rot(q,h));row=dict(source=s,consumer=a,head=[*p,h],slot=slot)
    if(sum(p)+h)%2:row['reason']='wrong_sector'
    elif forbidden_source_contact(s,a,p,h):row['reason']='past_source_chord_contact'
    else:
     assert(a,p,h,slot)in((0,(1,0),3,0),(4,(3,0),3,0),(7,(4,1),3,2))
     req={place(z[:2],p,h):bool(z[2])for z in G[a]['requirements']};core={place(z,p,h)for z in K};ins={place(z,p,h)for z in G[a]['inputs']}
     assert req[A]is False and A not in ins;assert B in req and B not in ins;assert not req[B]or B in core
     row.update(reason='r_retirement_requires_both_A_and_B_already_absent',A_before_white=True,B_context='core'if B in core else'before_white');rootcases.append(row)
    rootrows.append(row)
 # A or B same identity still current => original r cannot previously retire,
 # and cannot retire simultaneously at that A/B-consuming packet either.
 for z in(A,B):
  for a in IDS:
   slot=roles[a]
   for h in(0,2):
    p=sub(z,rot(G[a]['inputs'][slot],h));ctx={place(q[:2],p,h)for q in G[a]['requirements']};row=dict(source=s,source_output=z,consumer=a,head=[*p,h],selected_slot=slot)
    if(sum(p)+h)%2:row['reason']='wrong_sector'
    elif R0 in ctx:row['reason']='causally_held_r_in_context'
    elif forbidden_source_contact(s,a,p,h):row['reason']='past_source_chord_contact'
    else:
     assert z==B and a in(0,1)and p==(1,-1)and h==0
     row.update(reason='B_to_D_or_DC_only_exact_age4',forced_C_age=4);selectedcases.append(row)
    selectedrows.append(row)
assert len(rootrows)==276 and len(rootcases)==9 and len(selectedrows)==96 and len(selectedcases)==6
# Exact bridge for every potential r retirement: source V entry E0 to
# consumer base exit L0 closes with held r edge L0->E0.
E0=(-1,-1);L0=(1,1);assert set(edge(R0))=={E0,L0}
for row in rootcases:
 s=row['source'];a=row['consumer'];p=tuple(row['head'][:2]);h=row['head'][2];cc=chords(a,p,h)[0];assert cc[1]==L0
 assert single(contact(*cc,L0,E0),L0)
 for i,ch in enumerate(chords(s)):
  assert contact(*ch,L0,E0)==([[str(E0[0]),str(E0[1])]]if i==0 else[])
# Atomic turn n*pi/2+alpha_consumer-alpha_V. Bridge closing turns sum
# alpha_V-alpha_consumer-pi/2, so(n-1)*pi/2=+/-2*pi gives n5.
# Exact held-r+B bridge for selected B->D/DC.
Z=(3,-1);bridge=[Z,L0,E0];assert set(edge(B))=={Z,L0}
for row in selectedcases:
 s=row['source'];a=row['consumer'];cc=chords(a,(1,-1),0)[0];assert cc[1]==Z
 for i,(u,v)in enumerate(zip(bridge,bridge[1:])):
  assert contact(*cc,u,v)==([[str(Z[0]),str(Z[1])]]if i==0 else[])
  for j,ch in enumerate(chords(s)):
   assert contact(*ch,u,v)==([[str(E0[0]),str(E0[1])]]if i==1 and j==0 else[])
# Closing joins +pi/2,+pi/2,alpha_V-5*pi/4 sum alpha_V-pi/4.
# Atomic lift n*pi/2+pi/4-alpha_V => total n*pi/2 => n4.
D=[GP,Path(__file__).resolve(),HERE/'literal_helpers.py']+[ROOT/x/'manifest.json'for x in('U_entry_simplicity_frozen_20261023_1616','current_residual_barrier_frozen_20261023_1822','U_renewal_exact_clock_frozen_20261023_1902','genealogy_role_speed_frozen_20261023_0840')]
out=dict(status='AUTHOR_V_BASE_ONE_PARALLEL_REPRODUCTIVE_PORT_PENDING_INDEPENDENT_AUDIT',scope='In a simple atomic-center retained-eight factor, each genuine V/VC/VCC source has at most one BASE output identity feeding a parallel/antiparallel V-family or U-family distinguished input: it must be C=(2,1). A=(0,1) has no parallel distinguished consumer; B=(1,0) has only D/DC at exact source-entry C age4. C-tail outputs separately charged.',roles=roles,r_retirement_counts=dict(Counter(r['reason']for r in rootrows)),r_retirement_rows=rootrows,r_retirement_cases=rootcases,r_forced_C_age=5,selected_counts=dict(Counter(r['reason']for r in selectedrows)),selected_rows=selectedrows,selected_cases=selectedcases,B_bridge=bridge,B_forced_C_age=4,dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(HERE/'V_parallel_reproductive_supply.json').write_text(json.dumps(out,indent=2)+'\n');print(out['r_retirement_counts']);print(out['selected_counts'])
