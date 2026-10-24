"""A genuine U-family fresh output cohort has no all-cohort first consumer.
Finite port masks plus unbounded zero-C monotonicity; no prefix search.
"""
from pathlib import Path
exec((Path(__file__).resolve().parent/'literal_helpers.py').read_text())
from collections import Counter
PORT=ROOT/'U_first_helper_ports_frozen_20261023_1954/first_helper.json';CASES=json.loads(PORT.read_text())['cases'];L={(0,0),(0,1),(1,0),(1,1)}
def singleton(hit,p):return hit==[[str(p[0]),str(p[1])]]or hit==[list(p)]
def endpoint(a,p,h):
 x,y,dh=G[a]['endpoint'];return place((x,y),p,h),(h+dh)%4
rows=[];startup=[]
for s in(7,8,9):
 R=set(map(tuple,G[s]['outputs']));fp,fh=endpoint(s,(0,0),0);z=place((2,0),fp,fh);c=G[s]['name'].count('C')
 goals=[x for x in CASES if x['source']==s];assert len(goals)==2
 for first in IDS:
  fc=chords(first,fp,fh);outs={place(q,fp,fh)for q in G[first]['outputs']}
  for case in goals:
   goal=case['consumer'];gp=tuple(case['head'][:2]);gh=case['head'][2];gc=chords(goal,gp,gh);gctx={place(q[:2],gp,gh)for q in G[goal]['requirements']};gins={place(q,gp,gh)for q in G[goal]['inputs']};entry=dict(source=s,first=first,goal=goal,goal_head=case['head'])
   assert case['forced_nonnegative_C_age']-c==5
   if first in(7,8,9):
    hits={place(q,fp,fh)for q in L}&gctx;assert hits
    entry.update(reason='immediate_U_star_blocks_helper',hits=sorted(hits));startup.append(entry);continue
   assert z in outs and z in gctx-gins
   # Genuine fresh guard of the complete immediate successor, not touched by
   # its source-internal C tails.
   p,h=fp,fh
   for tick,ch in enumerate(G[first]['word']):
    if tick>=len(G[0 if first in(0,1)else 4]['word']):assert p!=z
    h=(h+(-1 if ch=='L'else 1))%4;p=place((0,1),p,h)
   survivors=[]
   for a in IDS:
    for h in range(4):
     for si,q in enumerate(G[a]['inputs']):
      p=sub(z,rot(q,h));cc=chords(a,p,h);end,eh=endpoint(a,p,h);row=dict(source=s,first=first,goal=goal,consumer=a,head=[*p,h],slot=si)
      if(sum(p)+h)%2:row['reason']='wrong_sector'
      elif {place(q[:2],p,h)for q in G[a]['requirements']}&R:row['reason']='unchanged_source_cohort_in_context'
      else:
       bad=False
       for block,bp,bh in[(s,(0,0),0),(first,fp,fh)]:
        old=chords(block,bp,bh);be,bh2=endpoint(block,bp,bh)
        for i,ch in enumerate(old):
         for j,new in enumerate(cc):
          hit=contact(*ch,*new)
          if hit and not(i==len(old)-1 and j==0 and(p,h)==(be,bh2)and singleton(hit,ch[1])):bad=True
       if bad:row['reason']='past_source_or_immediate_successor_chord'
       else:
        bad=False
        for i,ch in enumerate(cc):
         for j,new in enumerate(gc):
          hit=contact(*ch,*new)
          if hit and not(i==len(cc)-1 and j==0 and(end,eh)==(gp,gh)and singleton(hit,ch[1])):bad=True
        if bad:row['reason']='future_first_helper_chord'
        elif a in(7,8,9)and {place(q,p,h)for q in L}&gctx:
         row.update(reason='clearer_U_star_blocks_helper',hits=sorted({place(q,p,h)for q in L}&gctx))
        else:
         loc=rot(sub(p,fp),-fh);localend=rot(sub(end,fp),-fh);hr=(h-fh)%4
         assert hr==3 and loc[1]in(0,1)and localend[1]>=1,(s,first,goal,a,p,h,loc,localend)
         row.update(reason='relative_clock1_head_too_low_or_clock5_exit_too_high',head_in_source_exit_frame=[*loc,hr],exit_in_source_exit_frame=[*localend,(eh-fh)%4],possible_relative_C_clocks=[1,5]);survivors.append(row)
      rows.append(row)
   assert survivors
   entry.update(reason='fresh_guard_clearance_impossible',guard=z);startup.append(entry)
assert len(rows)==2760 and len(startup)==48
zeros=[];turns=[]
for a in(0,4,7):
 dx,dy,dh=G[a]['endpoint'];assert dh==0 and dy>0;wx,wy=rot((dx,dy),3);assert wy>=0;zeros.append(dict(type=a,N_y=dy,W_y=wy))
for a in(1,5,8):
 dx,dy,dh=G[a]['endpoint'];assert dh==3 and dy>=2;turns.append(dict(type=a,N_to_W_y=dy))
D=[GP,Path(__file__).resolve(),HERE/'literal_helpers.py',PORT,ROOT/'U_first_helper_ports_frozen_20261023_1954/manifest.json',ROOT/'U_left_star_permanence_frozen_20261023_1918/manifest.json']
out=dict(status='AUTHOR_U_COHORT_FIRST_TOUCH_REQUIRES_OUTSIDE_IDENTITY_PENDING_INDEPENDENT_AUDIT',scope='For any genuine U/UC/UCC full producer in a retained-eight factor, the first later packet consuming any one of its 9+3c fresh output identities, if any, has at least one input identity outside this exact producer cohort. Equivalently a genealogy reset at that U entry creates a component which must import an outside component at first touch. Not arbitrary historical-component merger or global U birth budget.',counts=dict(Counter(r['reason']for r in rows)),startup_cases=startup,guard_clearer_rows=rows,zero_C_y_bounds=zeros,one_C_turn_y_bounds=turns,dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(HERE/'U_cohort_first_touch.json').write_text(json.dumps(out,indent=2)+'\n');print(out['counts']);print('startup',len(startup))
