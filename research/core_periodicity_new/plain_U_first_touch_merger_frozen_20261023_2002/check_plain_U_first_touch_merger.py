"""Finite current-guard proof: a reset plain-U component must merge on first touch."""
from pathlib import Path
exec((Path(__file__).resolve().parent/'literal_helpers.py').read_text())
from collections import Counter
R=set(map(tuple,G[7]['outputs']));z=(2,4);source=chords(7);rows=[];startup=[]
def singleton(hit,p):return hit==[[str(p[0]),str(p[1])]]or hit==[list(p)]
def whole_endpoint(a,p,h):
 x,y,dh=G[a]['endpoint'];return place((x,y),p,h),(h+dh)%4
for first in IDS:
 fp=(0,4);fh=0;fc=chords(first,fp,fh);outs={place(q,fp,fh)for q in G[first]['outputs']};entry=dict(first=first)
 if first in(7,8,9):
  star={place(q,fp,fh)for q in[(0,0),(0,1),(1,0),(1,1)]};ctx={place(q[:2],(2,3),3)for q in G[0]['requirements']};hits=star&ctx;assert hits
  entry.update(reason='new_permanent_U_star_blocks_both_future_helpers',hits=sorted(hits));startup.append(entry);continue
 assert z in outs
 # Verify all optional source C tails preserve this exact D/V base output.
 p,h=fp,fh
 for tick,ch in enumerate(G[first]['word']):
  if tick>=len(G[0 if first in(0,1)else 4]['word']):assert p!=z
  h=(h+(-1 if ch=='L'else 1))%4;p=place((0,1),p,h)
 for goal in(0,1):
  gp=(2,3);gh=3;gc=chords(goal,gp,gh);ctx={place(q[:2],gp,gh)for q in G[goal]['requirements']};ins={place(q,gp,gh)for q in G[goal]['inputs']};assert z in ctx-ins
  survivors=[]
  for a in IDS:
   for h in range(4):
    for si,q in enumerate(G[a]['inputs']):
     p=sub(z,rot(q,h));cc=chords(a,p,h);end,eh=whole_endpoint(a,p,h);row=dict(first=first,goal=goal,consumer=a,head=[*p,h],slot=si)
     if(sum(p)+h)%2:row['reason']='wrong_sector'
     elif {place(q[:2],p,h)for q in G[a]['requirements']}&R:row['reason']='unchanged_source_U_output_in_context'
     else:
      bad=False
      for block,bp,bh in[(7,(0,0),0),(first,fp,fh)]:
       old=chords(block,bp,bh);be,bh2=whole_endpoint(block,bp,bh)
       for i,ch in enumerate(old):
        for j,new in enumerate(cc):
         hit=contact(*ch,*new)
         if hit and not(i==len(old)-1 and j==0 and(p,h)==(be,bh2)and singleton(hit,ch[1])):bad=True
      if bad:row['reason']='past_source_or_first_successor_chord'
      else:
       bad=False
       for i,ch in enumerate(cc):
        for j,new in enumerate(gc):
         hit=contact(*ch,*new)
         if hit and not(i==len(cc)-1 and j==0 and(end,eh)==(gp,gh)and singleton(hit,ch[1])):bad=True
       if bad:row['reason']='future_first_helper_chord'
       else:
        assert h==3 and p[1]in(4,5),(first,goal,a,p,h)
        # Heading W fixes the consumer's source-entry C clock to1 mod4.
        # It must begin strictly before first helper at clock5, or at clock5
        # with zero C cost. Clock1 has head y>=6 from literal monotonicity.
        c=G[a]['name'].count('C');assert end[1]>=5
        row.update(reason='clock1_head_too_low_or_clock5_exit_too_high',possible_clocks=[1,5],full_c=c,full_endpoint=[*end,eh]);survivors.append(row)
     rows.append(row)
  assert survivors
 entry.update(reason='fresh_guard_clearance_impossible',guard=z);startup.append(entry)
# Unbounded zero-C runs are handled by exact monotone endpoint inequalities.
zeros=[];turns=[]
for a in(0,4,7):
 dx,dy,dh=G[a]['endpoint'];assert dh==0 and dy>0;wx,wy=rot((dx,dy),3);assert wy>=0
 zeros.append(dict(type=a,N_y=dy,W_y=wy))
for a in(1,5,8):
 dx,dy,dh=G[a]['endpoint'];assert dh==3 and dy>=2;turns.append(dict(type=a,N_to_W_y=dy))
# Immediate U-family output stars are independently permanent.
D=[GP,Path(__file__).resolve(),HERE/'literal_helpers.py',ROOT/'U_first_helper_ports_frozen_20261023_1954/manifest.json',ROOT/'U_left_star_permanence_frozen_20261023_1918/manifest.json']
out=dict(status='AUTHOR_PLAIN_U_FIRST_TOUCH_MERGER_PENDING_INDEPENDENT_AUDIT',scope='Reset at a genuine plain U entry, so new component consists exactly of nine fresh outputs. First later packet consuming any of those identities, if it occurs within retained-eight, must also consume an outside component identity. Not a merger statement for an arbitrary unrestarted historical component, nor for UC/UCC.',startup_cases=startup,counts=dict(Counter(r['reason']for r in rows)),guard_clearer_rows=rows,zero_C_y_bounds=zeros,one_C_turn_y_bounds=turns,dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(HERE/'plain_U_first_touch_merger.json').write_text(json.dumps(out,indent=2)+'\n');print(out['counts']);print([(r['first'],r['reason'])for r in startup])
