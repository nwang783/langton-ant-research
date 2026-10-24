"""Selected V-base C cannot reproduce into same-heading V/VC; no prefix search."""
from pathlib import Path
exec((Path(__file__).resolve().parent/'literal_helpers.py').read_text())
from collections import Counter
r=(0,0);A=(0,1);B=(1,0);C=(2,1)
def ep(a,p,h):
 x,y,dh=G[a]['endpoint'];return place((x,y),p,h),(h+dh)%4
def single(hit,p):return hit==[[str(p[0]),str(p[1])]]or hit==[list(p)]
def past_bad(s,a,p,h):
 se,sh=ep(s,(0,0),0);src=chords(s);cc=chords(a,p,h)
 for i,old in enumerate(src):
  for j,new in enumerate(cc):
   hit=contact(*old,*new)
   if hit and not(i==len(src)-1 and j==0 and(p,h)==(se,sh)and single(hit,old[1])):return True
 return False
rows=[];cases=[]
for s in(4,5,6):
 for z in(A,B):
  for a in IDS:
   for h in range(4):
    for slot,q in enumerate(G[a]['inputs']):
     p=sub(z,rot(q,h));ctx={place(q[:2],p,h)for q in G[a]['requirements']};cc=chords(a,p,h);row=dict(source=s,source_output=z,consumer=a,head=[*p,h],slot=slot)
     if(sum(p)+h)%2:row['reason']='wrong_sector'
     elif r in ctx:row['reason']='causally_held_r_context'
     elif past_bad(s,a,p,h):row['reason']='past_source_chord_contact'
     else:
      if z==A:
       assert(a,p,h,slot)in((4,(0,4),2,0),(5,(0,4),2,0),(7,(-1,5),2,2),(8,(-1,5),2,2));n=2;bridge=[(-1,3),(0,2)];start=(0,2);assert on(start,*edge(A));proof='single_A_halfedge';E=bridge[0]
      else:
       assert(a,p,h,slot)in((0,(1,-1),0,0),(1,(1,-1),0,0),(4,(1,-3),0,0),(5,(1,-3),0,0),(7,(2,-2),0,1),(8,(2,-2),0,1),(9,(2,-2),0,1),(7,(2,-4),0,2),(8,(2,-4),0,2));n=4;bridge=[(3,-1),(1,1),(-1,-1)];start=(-1,-1);proof='held_r_plus_B';E=bridge[0]
      assert on(E,*cc[0]);prefix=(cc[0][0],E)
      for i,(u,v)in enumerate(zip(bridge,bridge[1:])):
       assert contact(*prefix,u,v)==([[str(E[0]),str(E[1])]]if i==0 else[])
       for j,(x,y)in enumerate(chords(s)):
        if j==0:x=start
        assert contact(x,y,u,v)==([[str(start[0]),str(start[1])]]if i==len(bridge)-2 and j==0 else[])
      row.update(reason='exact_A_age2_or_B_age4',forced_C_age=n,bridge=bridge,bridge_start_on_source_chord=start,consumer_contact=E,clock_proof=proof)
      if a in(7,8,9)and slot>=2:row['subreason']='upper_min5_excludes'
      elif z==B and a in(7,8,9):
       assert slot==1 and C in{place(q,p,h)for q in G[a]['inputs']};row['subreason']='consumes_original_C_simultaneously'
      elif z==B and a in(0,1):row['subreason']='repeats_future_C_consumer_entry'
      elif z==B:row['subreason']='V_helper_leaves_A_child_in_future_core'
      else:row['subreason']='only_V_or_VC_lower_A_survives'
      cases.append(row)
     rows.append(row)
assert len(rows)==552 and len(cases)==37
# B-helper H at(1,-3,N), source V/VC, leaves original fresh A_H in
# future P's core, so A_H must retire strictly before P.
H=(1,-3);child_A=add(H,A);P=(1,-1);
for typ in(4,5):
 req={place(z[:2],P,0):bool(z[2])for z in G[typ]['requirements']};assert req[B]is False and B not in{place(z,P,0)for z in G[typ]['inputs']}
Pcore={place(q,P,0)for q in K};assert child_A in Pcore
for htype in(4,5):assert child_A in{place(q,H,0)for q in G[htype]['outputs']}
# Above all-age A law forces H-child clearer V/VC at H+(0,4)=(1,1,S).
clearhead=(1,1);reverse=chords(4,clearhead,2)[0];target=chords(4,P,0)[0];assert reverse==(target[1],target[0])
# C-selected V/VC at relative headings N/S has exactly these literal poses.
Cposes=[]
for a in(4,5):
 for h in(0,2):
  p=sub(C,rot(G[a]['inputs'][1],h));assert p==((1,-1)if h==0 else(3,3));Cposes.append(dict(consumer=a,head=[*p,h]))
# Excluding the N pose leaves only flip at(3,3,S). A second such relative
# flip gives the original source pose and corrected center, forbidden.
first=(3,3);second=place((3,3),first,2);assert second==(0,0)
D=[GP,Path(__file__).resolve(),HERE/'literal_helpers.py']+[ROOT/x/'manifest.json'for x in('V_parallel_reproductive_supply_frozen_20261023_2036','U_entry_simplicity_frozen_20261023_1616','current_residual_barrier_frozen_20261023_1822','U_renewal_exact_clock_frozen_20261023_1902','chronology_dcuv/critical_ucc_count5/age_five_queries')]
out=dict(status='AUTHOR_SAME_HEADING_C_TO_V_VC_EXCLUSION_PENDING_INDEPENDENT_AUDIT',scope='Simple-center retained-eight factor. An original V-family base C=(2,1) cannot feed selected V/VC at same heading. Its only parallel selected V/VC pose is(3,3,S), so two consecutive such selected C-to-V/VC edges return to the original source pose and are impossible. Does not exclude VCC distinguished lower-input boundary transfers or perpendicular/other-origin support.',counts=dict(Counter(x['reason']for x in rows)),rows=rows,A_B_consumer_cases=cases,B_helper_A_child=child_A,future_P_core=sorted(Pcore),child_clearer_chord=reverse,future_P_chord=target,C_selected_V_VC_poses=Cposes,two_flip_return=second,dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(HERE/'V_C_same_heading_exclusion.json').write_text(json.dumps(out,indent=2)+'\n');print(out['counts']);print('surviving A/B cases',len(cases))
