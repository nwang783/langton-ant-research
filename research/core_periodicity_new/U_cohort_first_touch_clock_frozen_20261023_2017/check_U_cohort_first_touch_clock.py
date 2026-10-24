"""Exact current-cohort first-touch clocks and U-consumer older upper support.
No trajectory search:3312 literal port alignments and finite15-edge graph paths.
"""
from pathlib import Path
exec((Path(__file__).resolve().parent/'literal_helpers.py').read_text())
from collections import Counter
L={(0,0),(0,1),(1,0),(1,1)}
def endpoint(a,p,h):
 x,y,dh=G[a]['endpoint'];return place((x,y),p,h),(h+dh)%4
def singleton(hit,p):return hit==[[str(p[0]),str(p[1])]]or hit==[list(p)]
def graph_paths(adj,s,t):
 todo=[(s,[s])]
 while todo:
  v,p=todo.pop()
  if v==t:yield p;continue
  for z in adj.get(v,[]):
   if z not in p:todo.append((z,p+[z]))
def diagangle(v):
 x,y=v;assert abs(x)==abs(y)and x
 return 1 if x>0 and y>0 else 3 if x<0<y else 5 if x<0 and y<0 else 7
def principal(a,b):
 # Angle is (a+b*A)*pi/4, A=4*atan(3)/pi in the exact interval(1,2).
 if b==0:return((a+3)%8-3,0)
 good=[]
 for k in range(-4,5):
  x=a+8*k;lo=x+(b if b>0 else 2*b);hi=x+(2*b if b>0 else b)
  if lo>=-4 and hi<=4:good.append((x,b))
 assert len(good)==1,(a,b,good);return good[0]
def addpair(u,v):return u[0]+v[0],u[1]+v[1]
rows=[];cases={}
for s in(7,8,9):
 R=set(map(tuple,G[s]['outputs']));src=chords(s);se,sh=endpoint(s,(0,0),0);adj={}
 for q in R:
  u,v=edge(q);adj.setdefault(u,[]).append(v);adj.setdefault(v,[]).append(u)
 for a in IDS:
  for h in range(4):
   for z in sorted(R):
    for slot,inp in enumerate(G[a]['inputs']):
     p=sub(z,rot(inp,h));ins={place(q,p,h)for q in G[a]['inputs']};ctx={place(q[:2],p,h)for q in G[a]['requirements']};cc=chords(a,p,h);row=dict(source=s,consumer=a,head=[*p,h],source_cell=z,slot=slot)
     if(sum(p)+h)%2:row['reason']='wrong_sector'
     elif ctx&(R-ins):row.update(reason='other_current_cohort_identity_in_context',hits=sorted(ctx&(R-ins)))
     else:
      bad=False
      for i,ch in enumerate(src):
       for j,new in enumerate(cc):
        hit=contact(*ch,*new)
        if hit and not(i==len(src)-1 and j==0 and(p,h)==(se,sh)and singleton(hit,ch[1])):bad=True
      if bad:row['reason']='past_source_chord_contact'
      else:
       row['reason']='mixed_first_touch_clock_gate';key=(s,a,p,h)
       if key not in cases:
        bridges=[];base=(1,0)if a in(0,1)else(0,1)if a in(4,5,6)else(2,0)
        for E in adj:
         if not on(E,*cc[0]):continue
         for path in graph_paths(adj,E,W):
          valid=True
          for i,(u,v)in enumerate(zip(path,path[1:])):
           hit=contact(*cc[0],u,v)
           if hit and not(i==0 and singleton(hit,E)):valid=False
           for j,(x,y)in enumerate(src):
            if j==0:x=W
            hit=contact(x,y,u,v)
            if hit and not(i==len(path)-2 and j==0 and singleton(hit,W)):valid=False
           for j,(x,y)in enumerate(zip(path,path[1:])):
            if j>i+1 and contact(u,v,x,y):valid=False
          if not valid:continue
          angles=[(base[0]-2*h,base[1])]+[(diagangle(sub(v,u)),0)for u,v in zip(path,path[1:])]+[(2,0)]
          turns=[principal(v[0]-u[0],v[1]-u[1])for u,v in zip(angles,angles[1:])];closing=(sum(t[0]for t in turns),sum(t[1]for t in turns));const=addpair(closing,(base[0]-2,base[1]));assert const[1]==0 and const[0]%2==0;offset=const[0]//2
          ages=[n for n in(4-offset,-4-offset)if n>=0 and n%4==(-h)%4];assert len(ages)==1
          bridges.append(dict(contact_vertex=E,path=path,closing_turns_coefficients=turns,closing_sum_coefficients=closing,closed_turn_C_offset=offset,forced_C_age=ages[0]))
        assert bridges,(s,a,p,h)
        ages={b['forced_C_age']for b in bridges};assert len(ages)==1;n=next(iter(ages));c=G[s]['name'].count('C');assert n<=c+5
        cases[key]=dict(source=s,consumer=a,head=[*p,h],consumed_cohort_cells=sorted(ins&R),outside_cells=sorted(ins-R),forced_C_age=n,relative_full_birth_age=n-c,bridges=bridges)
     rows.append(row)
assert len(rows)==3312 and len(cases)==56
Y0={tuple(q)for a in IDS for q in G[a]['outputs']if q[1]==0};assert Y0=={(0,0),(1,0),(2,0)}
for a in IDS:assert all(q[1]>=0 for q in G[a]['outputs'])
for a in(0,4,7):assert G[a]['endpoint'][1]>0 and G[a]['endpoint'][2]==0
oldness=[];exclusions=[]
for key,case in sorted(cases.items()):
 s,a,p,h=key
 if a not in(7,8,9):continue
 R=set(map(tuple,G[s]['outputs']));consumed=set(map(tuple,case['consumed_cohort_cells']))
 if(-1,2)in consumed:exclusions.append(dict(source=s,consumer=a,head=[*p,h],reason='signed_recycled_q_cannot_feed_U'));continue
 if len(consumed)>3:exclusions.append(dict(source=s,consumer=a,head=[*p,h],reason='signed_max_three_from_one_full_producer'));continue
 upper={place(q,p,h)for q in G[a]['inputs'][2:]}-R;assert upper
 n=case['forced_C_age'];c=G[s]['name'].count('C');fp,fh=endpoint(s,(0,0),0);witnesses=[]
 for q in sorted(upper):
  v=rot(sub(q,fp),-fh)
  if n-5<c:reason='producer_deadline_precedes_source_full_exit'
  elif n-5==c and(v[1]<0 or(v[1]==0 and v not in Y0)):reason='same_clock_later_producer_misses_zero_C_forward_output_frontier'
  else:continue
  witnesses.append(dict(cell=q,in_full_exit_frame=v,reason=reason))
 assert witnesses,(key,n,c,upper)
 oldness.append(dict(source=s,consumer=a,head=[*p,h],forced_C_age=n,source_c=c,latest_upper_producer_clock=n-5,witnesses_current_at_source_entry=witnesses))
assert len(oldness)==27 and len(exclusions)==13
D=[GP,Path(__file__).resolve(),HERE/'literal_helpers.py']+[ROOT/x/'manifest.json'for x in('U_entry_simplicity_frozen_20261023_1616','current_residual_barrier_frozen_20261023_1822','U_renewal_exact_clock_frozen_20261023_1902','U_recycled_q_return_frozen_20261023_1939','U_max_three_cohort_frozen_20261023_1805','chronology_dcuv/critical_ucc_count5/age_five_queries')]
out=dict(status='AUTHOR_U_COHORT_FIRST_TOUCH_CLOCK_AND_OLDER_UPPER_PENDING_INDEPENDENT_AUDIT',scope='First consumer of a genuine U-family output cohort, if any, starts no later than five C units after that source full exit. If this first consumer is U-family, at least one upper input outside the source cohort was already current before source entry. The latter is not a distinct-original-component theorem or global U birth bound.',counts=dict(Counter(r['reason']for r in rows)),first_touch_clock_cases=list(cases.values()),U_oldness_cases=oldness,U_excluded_cases=exclusions,rows=rows,normal_output_y0_cells=sorted(Y0),dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(HERE/'U_cohort_first_touch_clock.json').write_text(json.dumps(out,indent=2)+'\n');print(out['counts']);print('clock cases',len(cases),'oldness',len(oldness),'U excluded',len(exclusions))
