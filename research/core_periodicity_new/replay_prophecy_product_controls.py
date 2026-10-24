"""Independently choose actual suffix flags and replay19 finite controls through products."""
from pathlib import Path
import json,subprocess
P=Path(__file__).resolve().parent;W=P.parent/'word_stabilization';OUT=P/'prophecy_physical_controls';OUT.mkdir(exist_ok=True);M=json.loads((W/'seven_sub_dcv_port_quotient.json').read_text())['macro_words'];G=json.loads((W/'dcv_residual_core_resources.json').read_text())['geometry'];controls=json.loads((W/'dcv_observed19_witnesses.json').read_text())['controls'];D=((0,1),(1,0),(0,-1),(-1,0));records=[]
def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def walk(w,p,h,B):
 seen=set()
 for c in w:
  assert(c=='L')==(p in B),(p,h,c)
  seen.add(p)
  if p in B:B.remove(p)
  else:B.add(p)
  h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return p,h,seen
for ci,c in enumerate(controls,1):
 row=c['tuple'];a,b,x,y,h,qx,qy=row;pre=OUT/f'case{ci:02d}';base=Path(str(pre)+'_base');lab=Path(str(pre)+'_labels');prod=Path(str(pre)+'_product')
 for cmd in[['python',str(P/'generate_protected_transfer_patch.py'),*map(str,row),str(base),'both'],['python',str(P/'add_protected_producer_labels.py'),str(base)+'.json',str(lab),str(P/'producer_labels_hypothesis_202.tsv'),f'{qx},{qy}',str(W/'dcv_companion_closed_family.tsv')],['python',str(P/'add_target_prophecy_product.py'),str(lab)+'.json',str(prod),str(P/'producer_labels_hypothesis_202.tsv'),str(W/'dcv_companion_closed_family.tsv')]]:subprocess.run(cmd,check=True,capture_output=True,text=True)
 J=json.loads(prod.with_suffix('.json').read_text());gap=c['target_packet_index']-c['source_packet_index'];B={tuple(z)for z in c['initial_seed_normalized_at_source']};p=(0,0);h=0;p,h,_=walk(M[a]['word'],p,h,B);states=[];seen_context=[]
 for a in c['factor_packet_types'][1:gap+1]:
  states.append((p,h,set(B),a));_,_,seen=walk(M[a]['word']+M[a]['end_marker'],p,h,set(B));seen_context.append(seen);p,h,_=walk(M[a]['word'],p,h,B)
 flags=[0]*gap;flags[-1]=(1<<len(J['prophecy_cells']))-1
 for i in range(gap-2,-1,-1):
  flags[i]=flags[i+1]
  for j,q in enumerate(J['prophecy_cells']):
   if tuple(q)in seen_context[i]:flags[i]&=~(1<<j)
 codes=[lab['outer_code']for lab in J['producer_labels']];poses={tuple(z):i for i,z in enumerate(J['poses'])};previous=None;checks=0
 for i,(p,h,B,a)in enumerate(states):
  s=sum(1<<j for j,z in enumerate(J['points'])if tuple(z)in B)|sum(v<<l['offset']for v,l in zip(codes,J['producer_labels']))|(flags[i]<<J['prophecy_offset']);sid=poses.get((*p,h),J['out']);goal=i==gap-1
  if i==0:assert sid==J['start'][0]and(s&J['start'][1])==J['start'][2]
  if previous is not None:
   pp,ss,edge=previous
   if pp==J['out']:assert s==ss and(sid==J['out']or sid in J['reentry'])
   else:assert any(t[1]==sid and(((ss^t[4])&~t[5])|(t[6]&t[5]))==s for t in edge)
  if sid==J['out']:assert not goal;edge=[]
  else:edge=[t for t in J['transitions']if t[0]==sid and t[-1]==a and bool(t[-2])==goal and(s&t[2])==t[3]];assert edge,(ci,i,a,p,h)
  checks+=1;previous=(sid,s,edge)
  for k,L in enumerate(J['producer_labels']):
   q=tuple(L['cell'])
   if q in seen_context[i]:codes[k]=0
   z=rot((q[0]-p[0],q[1]-p[1]),-h)
   if list(z)in G[a]['outputs']:
    hit=[j for j,l in enumerate(L['codes'])if j and not l['outer_origin']and l['packet']==a and l['slot']==G[a]['outputs'].index(list(z))and l['pose']==[*p,h]];assert len(hit)==1;codes[k]=hit[0]
 records.append({'control':ci,'tuple':row,'steps':checks,'prophecy_cells':J['prophecy_cells'],'suffix_flag_sequence':flags,'status':'ACTUAL_SUFFIX_PATH_PRESERVED'})
(P/'prophecy_product_observed19_controls.json').write_text(json.dumps(records,indent=2));print('All19 literal controls preserve their independently computed suffix-prophecy paths.')
