from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'foreign_U_star_predecessors_2026-10-23'
p=R/'audits/check_foreign_U_tag_interfaces_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('results={}')[0],ns)
G,G8,W,M,K,L,Z,at,xy,points,oldcenter=(ns[k]for k in('G','G8','W','M','K','L','Z','at','xy','points','oldcenter'))
ns2={'__file__':str(R/'audits/check_foreign_kinked_barrier_turn_independent.py')};exec(Path(ns2['__file__']).read_text().split('geometries=[]')[0],ns2);meet=ns2['meet'];center=ns2['center'];F=ns2['F']
gates=set()
for a in'FQB':
 for tag in L:
  for slot in G[a]['I']:
   for h in range(4):
    p=tag-at(slot,0,h)
    if(int(p.real+p.imag)+h)%2 or L&{at(q,p,h)for q in K|G[a]['white']}or oldcenter(p,h):continue
    gates.add((a,int(p.real),int(p.imag),h))
assert len(gates)==69
E={2,2+1j};newL={q+3-1j for q in L};rows=[];survivors=set();guardposes=set();contacts=[]
for a,x,y,h in sorted(gates):
 p=complex(x,y);turn=(-1j)**h;bad={p+q*turn for q in K|G[a]['white']};east=bad&E;guardian=bad&newL
 for pred in'VU':
  sp=p-G[pred]['p']*turn;assert(pred,sp,h)!=('U',0j,0);hits=L&{sp+q*turn for q in G[pred]['ctx']};ep=sp+G[pred]['p']*turn
  hit=meet((-1,-1),(-1,7),tuple(xy(center(sp,h))),tuple(xy(center(ep,h))))
  adj=hit is not None and len(hit)==3 and isinstance(hit[0],F) and hit[:2]==(1,0)and(sp,h)==(4j,0)
  if a=='B'and pred=='V':why='literal_V_B_adjacency_conflict_RAW59'
  elif hits:why='old_permanent_U_star_in_predecessor_complete_context'
  elif hit and not adj:why='predecessor_chord_contacts_creating_U_chord';contacts.append((a,x,y,h,pred,xy(sp),str(hit)))
  elif east and guardian:why='forced_genuine_right_breaker_fresh_star_in_foreign_core_or_before_white';guardposes.add((a,x,y,h))
  else:why='necessary_interface_not_asserted_attained';survivors.add((a,x,y,h))
  rows.append((a,x,y,h,pred,*xy(sp),h,why))
counts=Counter(r[-1]for r in rows);assert counts=={'literal_V_B_adjacency_conflict_RAW59':23,'old_permanent_U_star_in_predecessor_complete_context':12,'predecessor_chord_contacts_creating_U_chord':2,'forced_genuine_right_breaker_fresh_star_in_foreign_core_or_before_white':20,'necessary_interface_not_asserted_attained':81}
a=json.loads((D/'foreign_U_star_predecessors.json').read_text());assert set(rows)=={(r['foreign'],*r['foreign_pose'],r['predecessor'],*r['predecessor_pose'],r['reason'])for r in a['rows']}
assert len(survivors)==50 and len(guardposes)==13
ownership=Counter()
for name,x,y,h in survivors:
 p=complex(x,y);tags=L&{at(q,p,h)for q in G[name]['I']};raw=[];spill=[]
 for q in tags:
  local=(q-p)/((-1j)**h);rr=G[name]['rawreads'].get(local,[])
  if rr:
   assert len(rr)%2==1 and rr[0][1]=='L';raw.append(q)
  else:
   assert G[name]['reads'][local][0]==(len(W[name])+1,'L');spill.append(q)
 ownership[(len(raw),len(spill))]+=1
assert ownership=={(1,0):41,(2,0):6,(0,1):3}
for name in('U','UC','UCC'):assert newL<={3-1j+q for q in G8[name]['O']}
manifest=D/'manifest.json';sha=hashlib.sha256(manifest.read_bytes()).hexdigest();assert sha=='51e1985a368a41f9412187acccf10b2072ae9a8e241425bbad95ff54f12ad8bc'
for name,value in json.loads(manifest.read_text())['files'].items():assert hashlib.sha256((D/name).read_bytes()).hexdigest()==value
out={'status':'PASS necessary first-foreign original-U-star erosion predecessor and actual renewal guardian interface','manifest_sha256':sha,'counts':dict(counts),'remaining_poses':len(survivors),'remaining_ownership':{str(k):v for k,v in ownership.items()},'strict_chord_cuts':contacts,'forced_guardian_poses':sorted(guardposes),'analytic':['All69 gates are regenerated from literal full foreign contexts and the original held-star interface, then paired with their unique actual plain V/U predecessor poses. No predecessor equals the original creator.','The old star must miss the predecessor COMPLETE context. Input/core absorption and white constraints are actual retained-eight constraints with a genuine foreign M11, not fictitious foreign-owned reads.','The two extra chord contacts are strict inside the old simple path; the physical source-exit adjacency exception is expressly retained.','An old east cell required absent by foreign entry core/before-white forces its actual genuine right-breaker. That producer installs the new permanent star, and its conflicting foreign core/before-white cells exclude the20 assignments. No star permanence crosses foreign RAW.','Surviving RAW-retired old tags are all white at exit; the three marker-only poses keep their physical tags black through foreign RAW and place them in exit core, with successor phase1 ownership.'],'scope':'81 necessary assignments at50 poses, not attained erosion, first-center-contact avoidance, postforeign permanence or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts)
