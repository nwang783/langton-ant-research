"""Finite complete birth-subset DAG at one C clock; no packet-depth cap.
Unobserved zero-C paths retain only exact endpoint feasibility, so this is a
necessary overapproximation, not a physical path search or attainment test.
"""
from pathlib import Path
import hashlib,json
W=Path(__file__).resolve().parent
GP=W/'chronology_dcuv/literal_residual_geometry.json'
RP=W/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json'
G=json.loads(GP.read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9)
cells=[(-1,1),(-1,2),(-1,4),(0,2),(0,3)]
assert all(set(cells)==set(map(tuple,G[b]['inputs']))for b in (7,8,9))
def rot(p):
 x,y=p
 return y,-x
placements=[]
for b in IDS:
 poses={(t[0]-rot(o)[0],t[1]-rot(o)[1])for t in cells for o in G[b]['outputs']}
 for p in sorted(poses):
  if(sum(p)+1)%2:continue
  ctx={(p[0]+rot(z[:2])[0],p[1]+rot(z[:2])[1])for z in G[b]['requirements']}
  O={(p[0]+rot(o)[0],p[1]+rot(o)[1])for o in G[b]['outputs']}
  got=sum(1<<i for i,t in enumerate(cells)if t in O)
  hit=sum(1<<i for i,t in enumerate(cells)if t in ctx)
  dx,dy=rot(G[b]['endpoint'][:2])
  placements.append(dict(packet=b,head=[*p,1],exit=[p[0]+dx,p[1]+dy,(1+G[b]['endpoint'][2])%4],
                         output_mask=got,context_mask=hit,C=G[b]['name'].count('C')))
assert len(placements)==103
# Only zero-C E endpoints are used between relevant births.
assert [tuple(rot(G[b]['endpoint'][:2]))for b in (0,4,7)]==[(1,-1),(3,-1),(4,0)]
def reaches(p,t):
 dx=t[0]-p[0];ny=p[1]-t[1]
 if dx<0 or ny<0:return False
 # v V steps, d=ny-v D steps, u=(dx-ny-2v)/4 U steps.
 return any(dx-ny-2*v>=0 and (dx-ny-2*v)%4==0 for v in range(ny+1))
reachable_pairs=[[i,j]for i,p in enumerate(placements)for j,t in enumerate(placements)
                 if reaches(p['exit'],t['head'])]
can=set(map(tuple,reachable_pairs));cases=[];completed=[]
for old in range(32):
 if old&2:continue # q must be born at this clock; all other inputs are >=5.
 start=(old,-1,0);states=[start];idx={start:0};arcs=[];todo=[0]
 while todo:
  si=todo.pop();born,last,stages=states[si]
  if born==31:continue
  for pi,p in enumerate(placements):
   if p['context_mask']&born:continue
   if last>=0 and (last,pi)not in can:continue
   fresh=p['output_mask']&~born
   sub=fresh
   while sub:
    nb=born|sub
    if nb==31 or p['C']==0:
     z=(nb,pi,stages+1)
     if z not in idx:idx[z]=len(states);states.append(z);todo.append(idx[z])
     arcs.append([si,idx[z],pi,sub])
    sub=(sub-1)&fresh
  # Each producer births at least one of only five chosen final identities.
  # Thus stage<=5 is an induction consequence, not an imposed cutoff.
  assert all(z[2]<=5 for z in states)
 finals=[i for i,z in enumerate(states)if z[0]==31]
 assert all(states[i][2]==1 for i in finals)
 for i in finals:
  _,pi,_=states[i];completed.append(dict(old_mask=old,source=placements[pi],
                                        cohort_mask=31^old))
 cases.append(dict(older_input_mask=old,states=states,arcs=arcs,completed_states=finals))
expected={(1,7,(-1,4,1)),(1,8,(-1,4,1)),(1,9,(-1,4,1)),
          (20,4,(-1,2,1)),(20,5,(-1,2,1)),(20,6,(-1,2,1)),
          (28,6,(-7,2,1)),(28,9,(-8,1,1))}
assert {(r['old_mask'],r['source']['packet'],tuple(r['source']['head']))for r in completed}==expected
R=json.loads(RP.read_text());T={(a,h):v for a,h,v in R['created_peaks']}
for r in completed:
 x,y,h=r['source']['head'];r['U1_created_peak']=2*(y-x)+T[r['source']['packet'],2]
 assert r['U1_created_peak']<30
O=dict(status='AUTHOR_U_AGE5_LATEST_CLOCK_SINGLE_COHORT_PASS',
       scope='Produced q age5 and a age>=5 (entry infinity permitted). All exact-age5 target inputs have one producer. Eight necessary cohorts, none asserted attainable.',
       slot_order=cells,producer_heading=1,placements=placements,
       exact_zero_C_endpoint_pairs=reachable_pairs,birth_subset_DAGs=cases,
       completed_cohorts=completed,summary=dict(placements=len(placements),cases=len(cases),
       states=sum(len(r['states'])for r in cases),arcs=sum(len(r['arcs'])for r in cases),
       completed_cohorts=len(completed),multi_packet_completions=0),
       dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in [GP,RP,Path(__file__).resolve()]})
P=W/'chronology_dcuv/u_age_five_latest_cohort.json'
P.write_text(json.dumps(O,indent=2)+'\n');print(O['summary'])
