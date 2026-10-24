"""All-age, four-phase necessary birth-subset automata for q-youngest U inputs.
This finite construction uses no C-age bound or unknown-word depth cutoff.
"""
from pathlib import Path
import hashlib,json
W=Path(__file__).resolve().parent
GP=W/'chronology_dcuv/literal_residual_geometry.json'
RP=W/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json'
G=json.loads(GP.read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9)
R=json.loads(RP.read_text());A=R['core_offsets'];T={(a,h):v for a,h,v in R['created_peaks']}
assert A==[0,22,20,10] and R['target']==7 and R['target_global_phase']==1 and R['record_threshold']==30
cells=[(-1,1),(-1,2),(-1,4),(0,2),(0,3)]
def rot(p,h):
 x,y=p
 return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
PP=Path(R['potential_file']);values=json.loads(PP.read_text())['values']
assert (values['ax'],values['ay'])==(1,1)
def literal_A(h):
 return sum(rot((-1,1),h))+values[f'c{h%4}']
def literal_T(b,h):
 dx,dy,dh=G[b]['endpoint']
 return max([2*sum(rot((dx,dy),h))+literal_A(h+dh)]+
            [2*sum(rot(o,h))+values[f'w_{b}_{i}_{h}']for i,o in enumerate(G[b]['outputs'])])
assert [literal_A(h)for h in range(4)]==A
assert all(literal_T(b,h)==T[b,h]for b in IDS for h in range(4))
def phase(h,record=False):
 placements=[]
 for b in IDS:
  poses={(t[0]-rot(o,h)[0],t[1]-rot(o,h)[1])for t in cells for o in G[b]['outputs']}
  for p in sorted(poses):
   if(sum(p)+h)%2:continue
   ctx={(p[0]+rot(z[:2],h)[0],p[1]+rot(z[:2],h)[1])for z in G[b]['requirements']}
   O={(p[0]+rot(o,h)[0],p[1]+rot(o,h)[1])for o in G[b]['outputs']}
   got=sum(1<<i for i,t in enumerate(cells)if t in O)
   hit=sum(1<<i for i,t in enumerate(cells)if t in ctx)
   dx,dy=rot(G[b]['endpoint'][:2],h)
   entry=2*(p[1]-p[0])+A[(h+1)%4];created=2*(p[1]-p[0])+T[b,(h+1)%4]
   placements.append(dict(packet=b,head=[*p,h],exit=[p[0]+dx,p[1]+dy,(h+G[b]['endpoint'][2])%4],
                          output_mask=got,context_mask=hit,C=G[b]['name'].count('C'),
                          U1_entry_core=entry,U1_created_peak=created,U1_strict_record_permitted=max(entry,created)<30))
 def reaches(p,t):
  dx,dy=rot((t[0]-p[0],t[1]-p[1]),-h)
  if dx<0 or dy<0:return False
  return any(dy-dx-2*v>=0 and (dy-dx-2*v)%4==0 for v in range(dx+1))
 pairs=[[i,j]for i,p in enumerate(placements)for j,t in enumerate(placements)if reaches(p['exit'],t['head'])]
 can=set(map(tuple,pairs));cases=[];completions=[]
 for old in range(32):
  if old&2:continue
  states=[(old,-1,0)];idx={states[0]:0};arcs=[];todo=[0]
  while todo:
   si=todo.pop();born,last,stages=states[si]
   if born==31:continue
   for pi,p in enumerate(placements):
    if record and not p['U1_strict_record_permitted']:continue
    if p['context_mask']&born:continue
    if last>=0 and (last,pi)not in can:continue
    fresh=p['output_mask']&~born;sub=fresh
    while sub:
     nb=born|sub
     if nb==31 or p['C']==0:
      z=(nb,pi,stages+1)
      if z not in idx:idx[z]=len(states);states.append(z);todo.append(idx[z])
      arcs.append([si,idx[z],pi,sub])
     sub=(sub-1)&fresh
   assert all(z[2]<=5 for z in states)
  finals=[i for i,z in enumerate(states)if z[0]==31]
  for fi in finals:
   _,last,n=states[fi]
   completions.append(dict(older_input_mask=old,minimum_age_input_mask=31^old,
                           birth_packets=n,last_producer=placements[last]))
  cases.append(dict(older_input_mask=old,states=states,arcs=arcs,completed_states=finals))
 summary=dict(heading=h,strict_U1_record=record,placements=len(placements),allowed_placements=sum(not record or p['U1_strict_record_permitted']for p in placements),states=sum(len(r['states'])for r in cases),
              arcs=sum(len(r['arcs'])for r in cases),completed_states=len(completions),
              max_relevant_birth_packets=max((r['birth_packets']for r in completions),default=0),
              allowed_older_masks=sorted({r['older_input_mask']for r in completions}))
 return dict(heading=h,placements=placements,exact_zero_C_endpoint_pairs=pairs,
             birth_subset_DAGs=cases,completed_abstract_states=completions,summary=summary)
phases=[phase(h)for h in range(4)]
record_phases=[phase(h,True)for h in range(4)]
assert [p['summary']['allowed_older_masks']for p in phases]==[[0,1,24,28],[1,20,28],[5],[4,28]]
assert [p['summary']['max_relevant_birth_packets']for p in phases]==[2,1,1,1]
assert [p['summary']['allowed_older_masks']for p in record_phases]==[[28],[20],[5],[4,28]]
assert [p['summary']['completed_states']for p in record_phases]==[4,3,3,6]
assert all(p['summary']['max_relevant_birth_packets']==1 for p in record_phases)
O=dict(status='AUTHOR_ALL_AGE_Q_YOUNGEST_PHASE_COHORT_DAGS_PASS',
       scope='Produced q has age k>0 and every other U input has age>=k or infinity. Producer heading=k modulo4. Complete necessary finite same-clock birth abstraction, not physical attainment or record exclusion.',
       slot_order=cells,phases=phases,U1_strict_record_phases=record_phases,
       dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in [GP,RP,PP,Path(__file__).resolve()]})
P=W/'chronology_dcuv/u_minimum_clock_cohort_by_phase.json'
P.write_text(json.dumps(O,indent=2)+'\n')
for p in phases+record_phases:print(p['summary'])
