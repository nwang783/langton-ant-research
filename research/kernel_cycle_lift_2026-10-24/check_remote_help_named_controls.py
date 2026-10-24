"""Two named controls for the conjectural remote-old-cohort route predicate.
No seed scan; a pass is NOT evidence of a universal linear constant.
"""
from pathlib import Path
import sys,json
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'reframe_finite_seed_2026-10-24'))
sys.path.insert(0,str(ROOT/'renewal_input_placement_2026-10-23'))
from active_flight import rot,cursor,ends,step
from probe_renewal_input_ages import FullGraph

def edges(G,w):
 seen={w};todo=[w];E=set()
 for v in todo:
  for u,q in G.g.get(v,{}).items():
   E.add(q)
   if u not in seen:seen.add(u);todo.append(u)
 return E

def run(name,B,p,h,k,target,d,c):
 B=set(B);G=FullGraph(B,k);cohort=None;old=[];M=0;R=0;active_runs=[]
 for t in range(c+1):
  C=edges(G,cursor(p,h))
  if t>=d-1:M=max(M,len(C))
  if t==d:
   origin=p;cohort=set(B);remaining=set(B);D=edges(G,ends(target,k)[0]);assert target in D and target not in C
  if t>=d:
   R=max(R,abs(p[0]-origin[0]),abs(p[1]-origin[1]));on=target in C
   if not active_runs or active_runs[-1]['active']!=on:active_runs.append(dict(active=on,start=t,length=0))
   active_runs[-1]['length']+=1
  q=p;c0='L'if q in B else'R'
  if t==c:assert q==target and c0=='L'
  if cohort is not None and c0=='L'and q in remaining:
   remaining.remove(q);old.append(dict(update=t,cell=q,distance=max(abs(q[0]-origin[0]),abs(q[1]-origin[1]))))
  if c0=='L':G.delete(q)
  else:G.add(q)
  p,h=step(B,p,h)
 helpers=[x for x in old if x['distance']>4*M]
 return dict(name=name,departure_cut=d,marked_consumption=c,marked_cell=target,departure_head=origin,departure_full_mass=len(cohort),initial_frozen_component=sorted(D),actual_active_max=M,head_excursion=R,far_threshold=16*M,old_helper_threshold=4*M,qualifies_far=R>16*M,old_remote_lifetime_consumptions=helpers,old_consumption_count=len(old),marker_activity_runs=active_runs,route_hypothesis_falsified=R>16*M and not helpers)

G0={(0,-1),(1,1),(2,2),(1,3)};n=400
poses=[((0,0),1),((n-1,n),0),((-n,3*n-4),3),((-5*n+5,-n),2),((-3*n,-3*n+8),1)];B=set()
for p,h in poses:B|={(p[0]+v[0],p[1]+v[1])for q in G0 for v in[rot(q,(h-1)%4)]}
feedback=run('signed20-cell feedback, named n400',B,(0,0),1,0,(0,2),173,624*n-1516)
compact=run('compact4-cell real RL+T branch fixture',{(-1,0),(0,-2),(0,-1),(2,1)},(-1,-1),0,1,(-1,-1),2,8)
out=dict(status='AUTHOR named route-hypothesis diagnostics, not a proof',controls=[feedback,compact],scope='Only two explicit seeds, all complete fields and lifetime cohorts retained. Multiple marked unproductive reactivations are allowed before consumption. RH16/4 remains conjectural; nonqualifying compact controls do not test its far-feedback case.')
(OUT/'remote_help_named_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'controls':[{k:v for k,v in a.items()if k not in['marker_activity_runs','initial_frozen_component']}for a in out['controls']]},indent=2))
