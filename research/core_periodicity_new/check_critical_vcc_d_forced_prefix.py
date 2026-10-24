"""Exact finite arithmetic/literal controls for one-C kinematic completeness."""
from pathlib import Path
import json,hashlib,itertools
R=Path(__file__).resolve().parent;gp=R/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(gp.read_text())['geometry'];DIR=((0,1),(1,0),(0,-1),(-1,0))
def trace(seq,withmarker=True):
 p=(0,0);h=0;first={};last={};events=[];seed=set();born={};q=(0,0);saved=[];bad=None;poses=[];t=0
 for j,a in enumerate(seq):
  poses.append([*p,h]);w=G[a]['word']
  if j==len(seq)-1 and withmarker:w+=G[a]['marker']
  for c in w:
   if p in last and last[p][1]==c:bad={'time':t,'cell':p,'turn':c,'previous_same_turn':last[p][0]};break
   if p not in first:
    first[p]=(t,c)
    if c=='L':seed.add(p)
   last[p]=(t,c);events.append((t,p,h,c));h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1]);t+=1
  if bad:break
 return {'feasible':bad is None,'bad':bad,'seed':sorted(seed),'poses':poses,'events':events}
# The nonnegative integer equations imply b+2c+d+2e+2f=1.
# Therefore c=e=f=0 and (b,d) is (1,0) or (0,1); a follows.
solutions=[]
for b,d in[(1,0),(0,1)]:
 c=e=f=0;a=1-b+d
 assert a+b-d-3*e-4*f==1 and a+3*b+4*c+d+e==3
 solutions.append({'pre_DVU':[a,b,c],'post_DVU':[d,e,f]})
assert solutions==[{'pre_DVU':[0,1,0],'post_DVU':[0,0,0]},{'pre_DVU':[2,0,0],'post_DVU':[1,0,0]}]
seqs=[[6,5,0],[6,0,1,0,0]];records=[]
for s in seqs:
 t=trace(s);t['packet_ids']=s;t['packet_names']=[G[a]['name']for a in s]
 t['events_at_protected_q']=[e for e in t.pop('events')if tuple(e[1])==(0,0)]
 records.append(t)
assert records[0]['feasible']and not records[1]['feasible'];assert records[1]['bad']['cell']==(0,3)
# Check strict VC complete context avoids source residual output(0,0).
p=(0,4);h=2
for q in G[5]['requirements']:
 x,y=q[:2];world=(p[0]-x,p[1]-y);assert world!=(0,0)
J={'status':'AUTHOR_ALL_PARAMETER_KINEMATIC_AND_LITERAL_PASS','scope':'Only source VCC output(0,0) feeding D input(0,1) at relativepose(-1,0,1), exact source-included C age3. No global genealogy or capture claim.','source':6,'target':0,'source_output':[0,0],'target_input':[0,1],'target_pose':[-1,0,1],'exact_C_age':3,'remaining_intermediate_C':1,'center_remaining_after_source_in_exit_frame':[2,4],'after_subtracting_unique_C':[1,3],'equations':['a+b-d-3e-4f=1','a+3b+4c+d+e=3'],'deduced_complete_constraint':'b+2c+d+2e+2f=1','all_nonnegative_solutions':solutions,'only_intermediate_packet_words':[[5],[0,1,0]],'records':records,'input_sha256':hashlib.sha256(gp.read_bytes()).hexdigest()}
out=R/'chronology_dcuv/critical_vcc_d_forced_prefix.json';out.write_text(json.dumps(J,indent=2)+'\n');print({'solutions':solutions,'feasible_word':seqs[0],'infeasible_word':seqs[1],'conflict':records[1]['bad'],'protected_events':records[0]['events_at_protected_q']})
