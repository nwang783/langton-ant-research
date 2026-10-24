"""One all-age U-family origin/context/record calculation after star permanence.
Necessary templates only, not actual origin assignments or a funding closure.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry']
MP=W/'atomic_core_record_interface_frozen_20261023_1359/04_root_out.json';M=json.loads(MP.read_text());A=M['core_offsets'];T={(a,h):v for a,h,v in M['created_peaks']};AP=W/'atomic_core_record_interface_frozen_20261023_1359/02_atomic_core_record_interface.json';AR=json.loads(AP.read_text());TS={(r['packet'],r['global_phase']):r['enlarged_peak']for r in AR['rows']}
CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)};L={(0,0),(0,1),(1,0),(1,1)};I=list(map(tuple,G[7]['inputs']));GC={tuple(z[:2])for z in G[7]['requirements']}
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def cross(p,q):return p[0]*q[1]-p[1]*q[0]
def on(p,a,b):return cross(sub(p,a),sub(b,a))==0 and sum((p[i]-a[i])*(p[i]-b[i])for i in range(2))<=0
def contact(A,B):
 p,q=A;r,s=B;x=cross(sub(q,p),sub(r,p));y=cross(sub(q,p),sub(s,p));u=cross(sub(s,r),sub(p,r));v=cross(sub(s,r),sub(q,r));return((x>0>y or y>0>x)and(u>0>v or v>0>u))or any(on(z,*e)for z,e in[(p,B),(q,B),(r,A),(s,A)])
def chords(a,p,h):
 e=G[7]['endpoint'];C=[];A0=add((2*p[0],2*p[1]),rot((-1,-1),h));p=add(p,rot(e[:2],h));B=add((2*p[0],2*p[1]),rot((-1,-1),h));C.append((A0,B))
 for _ in range(G[a]['name'].count('C')):
  A0=B;p=add(p,rot((0,1),h));h=(h-1)%4;B=add((2*p[0],2*p[1]),rot((-1,-1),h));C.append((A0,B))
 return C
TC=chords(7,(0,0),0);rows=[];needed=set()
for a in[7,8,9]:
 for oi,o0 in enumerate(G[a]['outputs']):
  o=tuple(o0)
  for si,t in enumerate(I):
   for h in range(4):
    p=sub(t,rot(o,h));phase=(h+1)%4;H=p[1]-p[0];r=dict(source=a,source_output_slot=oi,source_output=o,goal_input_slot=si,goal_input=t,source_pose=[*p,h],source_entry=2*H+A[phase],source_created=2*H+T[a,phase],source_enlarged=2*H+TS[a,phase])
    if(sum(p)+h)%2:r['reason']='wrong_sector'
    else:
     stars={add(p,rot(l,h))for l in L};hits=sorted(stars&GC)
     if hits:r.update(reason='permanent_source_L_star_meets_goal_complete_context',star_hits=hits)
     elif o in[(2,0),(2,1)]:r['reason']='signed_original_U1_east_pair_origin_exclusion'
     elif max(r['source_entry'],r['source_created'])>=30:r['reason']='old_source_record_already_funds_goal'
     elif any(contact(c,t)for c in chords(a,p,h)for t in TC):r['reason']='source_atomic_chord_contacts_later_goal'
     else:
      ages=[k for k in[3,4]if k%4==h and(si<2)];ages.append(5)
      # Count class5 is overflow>=5; heading fixes the actual congruence.
      v=rot(sub((0,0),p),-h);keys=[(mp[a],mp[7],*v,(-h)%4,*o,k)for k in ages]
      r.update(reason='pending_count_classes',age_classes=ages,count_query_keys=keys)
      needed.update(keys)
    rows.append(r)
found=set()
with CP.open()as f:
 for line in f:
  z=tuple(map(int,line.split()[:8]))
  if z in needed:found.add(z)
for r in rows:
 if r['reason']!='pending_count_classes':continue
 allowed=[k for k,key in zip(r['age_classes'],r['count_query_keys'])if tuple(key)not in found]
 r['unexcluded_count_classes']=allowed
 r['reason']='necessary_origin_template_not_attainment'if allowed else'signed_count5_excludes_all_possible_age_classes'
 r['also_survives_enlarged_history']=bool(allowed)and max(r['source_entry'],r['source_enlarged'])<30
counts=dict(Counter(r['reason']for r in rows));keep=[r for r in rows if r['reason']=='necessary_origin_template_not_attainment'];atomic=[r for r in keep if r['also_survives_enlarged_history']]
D=[GP,MP,AP,CP,W/'U_left_star_permanence_frozen_20261023_1918/manifest.json',W/'U1_east_pair_origin_frozen_20261023_1852/manifest.json',Path(__file__).resolve()]
R=dict(status='ALL_AGE_NECESSARY_ORIGIN_DIAGNOSTIC_NO_CLOSURE',scope=__doc__,counts=counts,original_U1_necessary_template_count=len(keep),enlarged_history_necessary_template_count=len(atomic),original_U1_necessary_templates=keep,enlarged_history_necessary_templates=atomic,all_alignments=rows,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U1_U_origins_after_permanence.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(dict(counts=counts,original_survivors=len(keep),atomic_survivors=len(atomic),original_by_goal_slot=dict(Counter(r['goal_input_slot']for r in keep)),atomic_by_goal_slot=dict(Counter(r['goal_input_slot']for r in atomic))),indent=2))
