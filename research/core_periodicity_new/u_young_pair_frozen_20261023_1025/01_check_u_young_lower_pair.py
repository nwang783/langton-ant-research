"""Finite producer geometry plus exact ant controls for U lower C-age3 pairs."""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;LP=W/'chronology_dcuv/literal_residual_geometry.json';G0=json.loads(LP.read_text());G=G0['geometry'];K=set(map(tuple,G0['core']));IDS=(0,1,4,5,6,7,8,9);mp={a:i for i,a in enumerate(IDS)}
CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()}
a=(-1,1);q=(-1,2);UPPER={(-1,4),(0,2),(0,3)}
def rot(p,h):x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return(p[0]+q[0],p[1]+q[1])
def at_cell(cell,h,protected):
 out=[]
 for b in IDS:
  for oi,o in enumerate(G[b]['outputs']):
   z=rot(o,h);head=(cell[0]-z[0],cell[1]-z[1])
   if(sum(head)+h)%2:continue
   ctx={add(head,rot((x,y),h))for x,y,*_ in G[b]['requirements']}
   if ctx&protected:continue
   outputs={add(head,rot(t,h))for t in G[b]['outputs']}
   dx,dy,dh=G[b]['endpoint'];out.append(dict(packet=b,head=[*head,h],output_slot=oi,other_lower_is_output=a in outputs,exit=[*add(head,rot((dx,dy),h)),(h+dh)%4]))
 return out
Q=at_cell(q,3,UPPER);Qzero=[r for r in Q if r['packet']in(0,4,7)];assert{r['packet']for r in Qzero}=={0,4,7};assert all(r['head']==[-1,0,3]for r in Qzero)
A=at_cell(a,3,UPPER|{q});assert len(A)==11 and min(r['head'][0]for r in A)==0;assert max(r['exit'][0]for r in Qzero)==-2
cohort=[r for r in Q if r['other_lower_is_output']];assert{r['packet']for r in cohort}=={4,5,6,7,8,9};assert all(r['head']==[-1,0,3]for r in cohort)
queries=[]
for r in cohort:
 b=r['packet']
 for consumer in(7,8,9):
  for outslot in((1,0),(2,0)):
   key=(mp[b],mp[consumer],0,-1,1,*outslot,3);blocked=key in COUNT;assert blocked==(b in(7,8,9));queries.append(dict(source=b,consumer=consumer,source_output=outslot,tuple=key,excluded=blocked))
# Fully physical eleven-cell positive controls, including actual final marker.
seed=sorted(K|{(0,3),(1,2),(-1,2),(4,0),(2,-1),(3,-1)})
assert len(seed)==11
controls=[]
for consumer in(7,8,9):
 word=[6,5,0,consumer];program=''.join(G[b]['word']for b in word);rawlen=len(program);full=program+G[0]['marker'];B=set(seed);x=y=h=0;boundaries=[];lengths=[];n=0
 for b in word:n+=len(G[b]['word']);lengths.append(n)
 for ti,ch in enumerate(full):
  p=(x,y);black=p in B;assert('L'if black else'R')==ch,(consumer,ti,p,ch)
  if black:B.remove(p)
  else:B.add(p)
  h=(h+(-1 if black else 1))%4;dx,dy=((0,1),(1,0),(0,-1),(-1,0))[h];x+=dx;y+=dy
  if ti+1 in lengths:boundaries.append([ti+1,x,y,h,len(B)])
 assert boundaries[2][1:4]==[0,-1,1]
 controls.append(dict(word=word,initial_black_cells=seed,raw_length=rawlen,complete_check_reads=len(full),raw_boundaries=boundaries,lower_source_outputs=[[1,0],[2,0]],lower_birth_packet=0,consumer_packet=3,consumer_pose=[0,-1,1],lower_C_ages=[3,3],upper_entry_identities=[[4,0],[2,-1],[3,-1]]))
O=dict(status='AUTHOR_YOUNG_LOWER_PAIR_CLASSIFICATION_AND_PHYSICAL_CONTROLS_PASS',scope='Complete recurrent-eight factor; produced q C-age3 only, entry identities virtual-old. No individual age minimum is raised.',q_zero_C_producers=Qzero,a_producers_avoiding_q_and_uppers=A,same_birth_candidates=cohort,signed_count3_queries=queries,surviving_sources=[4,5,6],controls=controls,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[LP,CP,Path(__file__).resolve()]})
T=W/'chronology_dcuv/u_young_lower_pair.json';T.write_text(json.dumps(O,indent=2)+'\n');print('qzero',Qzero);print('a placements',len(A));print('same_birth6,surviving3, physicalcontrols3 PASS');print(T)
