"""All-age selected parallel U-base supply: exactly one possible arm at C age6."""
from pathlib import Path
exec((Path(__file__).resolve().parent/'literal_helpers.py').read_text())
from collections import Counter
L={(0,0),(0,1),(1,0),(1,1)};BASE=set(map(tuple,G[7]['outputs']));roles={a:0 if a in(0,1,6)else 1 if a in(4,5)else 4 for a in IDS};rows=[];cases=[]
def ep(a,p,h):
 x,y,dh=G[a]['endpoint'];return place((x,y),p,h),(h+dh)%4
def single(hit,p):return hit==[[str(p[0]),str(p[1])]]or hit==[list(p)]
for s in(7,8,9):
 assert BASE<=set(map(tuple,G[s]['outputs']))
 src=chords(s);se,sh=ep(s,(0,0),0)
 for a in IDS:
  slot=roles[a]
  for h in(0,2):
   for z in sorted(BASE):
    p=sub(z,rot(G[a]['inputs'][slot],h));ctx={place(q[:2],p,h)for q in G[a]['requirements']};cc=chords(a,p,h);row=dict(source=s,consumer=a,head=[*p,h],source_base_output=z,distinguished_input_slot=slot)
    if(sum(p)+h)%2:row['reason']='wrong_sector'
    elif ctx&L:row.update(reason='permanent_left_star_context',hits=sorted(ctx&L))
    else:
     bad=False
     for i,old in enumerate(src):
      for j,new in enumerate(cc):
       hit=contact(*old,*new)
       if hit and not(i==len(src)-1 and j==0 and(p,h)==(se,sh)and single(hit,old[1])):bad=True
     if bad:row['reason']='past_source_chord_contact'
     else:
      assert(a,p,h,z)==(0,(1,3),2,(1,2));row['reason']='arm_to_plain_D_exact_age6';cases.append(row)
    rows.append(row)
assert len(rows)==432 and len(cases)==3
# Current bridge uses only three permanent left-star/held-arm identities,
# not any other old source output. Therefore this is not a first-touch law.
bridge=[(1,5),(3,3),(1,1),W];qs=[(1,2),(1,1),(0,1)]
for i,(u,v)in enumerate(zip(bridge,bridge[1:])):assert set(edge(qs[i]))=={u,v}
consumer=chords(0,(1,3),2)[0];assert consumer[1]==bridge[0]
for s in(7,8,9):
 for i,(u,v)in enumerate(zip(bridge,bridge[1:])):
  assert contact(*consumer,u,v)==([[str(bridge[0][0]),str(bridge[0][1])]]if i==0 else[])
  for j,(x,y)in enumerate(chords(s)):
   if j==0:x=W
   assert contact(x,y,u,v)==([[str(W[0]),str(W[1])]]if i==len(bridge)-2 and j==0 else[])
# D tangent is SW, closing bridge is SE,SW,NW, source tangent N.
# Exact closing joins(+2,-2,-2,-1)*pi/4 sum-3*pi/4.
turns=[2,-2,-2,-1];assert sum(turns)==-3
# Atomic lift n*pi/2 +alpha_D-alpha_U =n*pi/2-pi/4.
# Total(n-2)*pi/2=+/-2*pi forces the sole nonnegative solution n6.
D=[GP,Path(__file__).resolve(),HERE/'literal_helpers.py']+[ROOT/x/'manifest.json'for x in('U_left_star_permanence_frozen_20261023_1918','U_entry_simplicity_frozen_20261023_1616','current_residual_barrier_frozen_20261023_1822','U_renewal_exact_clock_frozen_20261023_1902','genealogy_role_speed_frozen_20261023_0840')]
out=dict(status='AUTHOR_U_BASE_PARALLEL_SELECTED_SUPPLY_PENDING_INDEPENDENT_AUDIT',scope='Any genuine U/UC/UCC base output feeding a later retained packet distinguished input at parallel or antiparallel heading is necessarily arm(1,2) into plain D(1,3,S), at exact source-entry C age6. No first-touch/full-cohort assumption. C-tail outputs are not classified.',roles=roles,counts=dict(Counter(r['reason']for r in rows)),rows=rows,surviving_cases=cases,bridge=bridge,bridge_identities=qs,closing_turns_pi_over_4=turns,atomic_turn='n*pi/2-pi/4',closed_turn='(n-2)*pi/2',forced_C_age=6,dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(HERE/'U_parallel_selected_supply.json').write_text(json.dumps(out,indent=2)+'\n');print(out['counts'])
