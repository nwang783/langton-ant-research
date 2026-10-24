"""Replay physical finite controls through producer-label abstractions, independently updating labels."""
from pathlib import Path
import json,subprocess,sys
P=Path(__file__).resolve().parent;W=P.parent/'word_stabilization';M=json.loads((W/'seven_sub_dcv_port_quotient.json').read_text())['macro_words'];G=json.loads((W/'dcv_residual_core_resources.json').read_text())['geometry'];controls=json.loads((W/'dcv_observed19_witnesses.json').read_text())['controls'];HFILE=Path(sys.argv[1])if len(sys.argv)>1 else P/'producer_labels_hypothesis_202.tsv';controls=[c for c in controls if len(sys.argv)<3 or c['target_packet_index']-c['source_packet_index']==1];D=((0,1),(1,0),(0,-1),(-1,0));records=[]
def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def walk(w,p,h,B,check=True):
 seen=set()
 for c in w:
  if check:assert(c=='L')==(p in B),(p,h,c)
  seen.add(p)
  if p in B:B.remove(p)
  else:B.add(p)
  h=(h+(1 if c=='R'else-1))%4;d=D[h];p=(p[0]+d[0],p[1]+d[1])
 return p,h,seen
for ci,c in enumerate(controls,1):
 a,b,x,y,h,qx,qy=c['tuple'];pre=f'producer_control_{ci:02d}';subprocess.run(['python',str(P/'generate_protected_transfer_patch.py'),*map(str,[a,b,x,y,h,qx,qy]),pre,'both'],check=True,capture_output=True,text=True);J=json.loads((P/(pre+'.json')).read_text());Q=[(qx,qy)];outpre=P/(pre+'_labels');subprocess.run(['python',str(P/'add_protected_producer_labels.py'),str(P/(pre+'.json')),str(outpre),str(HFILE),';'.join(f'{x},{y}'for x,y in Q)],check=True,capture_output=True,text=True);L=json.loads(outpre.with_suffix('.json').read_text());B={tuple(z)for z in c['initial_seed_normalized_at_source']};p=(0,0);h=0;p,h,_=walk(M[a]['word'],p,h,B);codes=[z['outer_code']for z in L['producer_labels']];pos={tuple(z):i for i,z in enumerate(L['poses'])};targetgap=c['target_packet_index']-c['source_packet_index'];assert len(c['factor_packet_types'])>targetgap
 def state():return sum((1<<i)for i,z in enumerate(L['points'])if tuple(z)in B)|sum(v<<lab['offset']for v,lab in zip(codes,L['producer_labels']))
 s=state();assert(s&L['start'][1])==L['start'][2];assert pos.get((*p,h),L['out'])==L['start'][0];near=far=0
 for j,a in enumerate(c['factor_packet_types'][1:targetgap+1],1):
  sid=pos.get((*p,h),L['out']);goal=j==targetgap;before=state();assert before==s
  if sid==L['out']:
   assert not goal;far+=1
  else:
   near+=1;T=[t for t in L['transitions']if t[0]==sid and t[-1]==a and bool(t[-2])==goal and(before&t[2])==t[3]];assert len(T)==1,(ci,j,a,p,h,len(T));t=T[0]
  pp,hh=p,h;_,_,seen=walk(M[a]['word']+M[a]['end_marker'],p,h,set(B));p,h,_=walk(M[a]['word'],p,h,B)
  for k,lab in enumerate(L['producer_labels']):
   q=tuple(lab['cell'])
   if q in seen:codes[k]=0
   z=rot((q[0]-pp[0],q[1]-pp[1]),-hh)
   if list(z)in G[a]['outputs']:
    hits=[ii for ii,ll in enumerate(lab['codes'])if ii and not ll['outer_origin']and ll['packet']==a and ll['slot']==G[a]['outputs'].index(list(z))and ll['pose']==[*pp,hh]];assert len(hits)==1;codes[k]=hits[0]
  s=state();nextpos=pos.get((*p,h),L['out'])
  if sid==L['out']:
   assert s==before
   if nextpos!=L['out']:assert nextpos in L['reentry']
  else:assert s==(((before^t[4])&~t[5])|(t[6]&t[5])) and nextpos==t[1]
 records.append({'control':ci,'tuple':c['tuple'],'watched':Q,'near_steps':near,'far_steps':far,'status':'LITERAL_PATH_PRESERVED'})
(P/('producer_label_adjacent_outer_exemption_controls.json'if len(sys.argv)>2 else'producer_label_observed19_controls.json')).write_text(json.dumps(records,indent=2));print('All',len(records),'literal controls survive producer-label graphs with',str(HFILE),'hypotheses.')
