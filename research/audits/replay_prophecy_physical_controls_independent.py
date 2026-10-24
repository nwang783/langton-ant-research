"""Match every real finite witness to its exact producer/prophecy graph path."""
from pathlib import Path
import re,json,hashlib
from check_target_suffix_models_independent import geometry,rotation,xy,ROOT
W=ROOT/'word_stabilization';C=ROOT/'core_periodicity_new/prophecy_physical_controls'
data=json.loads((W/'dcv_observed19_witnesses.json').read_text())['controls'];words={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR'};results=[]
for index,control in enumerate(data,1):
 path=C/f'case{index:02}_product.json';J=json.loads(path.read_text());F=json.loads(Path(J['forward_model_file']).read_text())
 assert(J['source'],J['target'],*J['target_pose'],*J['protected_q'])==tuple(control['tuple'])
 blocks=[m.group()for m in re.finditer('[DV]C*',control['factor_macro_word'])];ti=control['target_packet_index']-control['source_packet_index'];assert ti>0
 p=0j;h=0;black={complex(*z)for z in control['initial_seed_normalized_at_source']};poses=[];boards=[];contexts=[];types=[]
 for block in blocks[:ti+1]:
  poses.append((p,h));boards.append(black.copy());a=(0 if block[0]=='D'else 4)+len(block)-1;types.append(a)
  contexts.append({p+rotation(z,h)for z in geometry[a]['context']})
  for turn in ''.join(words[z]for z in block):
   assert(p in black)==(turn=='L');black.symmetric_difference_update({p});h=(h+(1 if turn=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 points=[complex(*z)for z in J['points']];posemap={tuple(z):i for i,z in enumerate(J['poses'])};Q=[complex(*z)for z in J['prophecy_cells']]
 labels=F['producer_labels'];codes=[L['outer_code']for L in labels]
 def state(i):
  value=sum((z in boards[i])<<j for j,z in enumerate(points))
  for L,code in zip(labels,codes):value|=code<<L['offset']
  for j,q in enumerate(Q):
   if all(q not in context for context in contexts[i:ti]):value|=1<<(J['prophecy_offset']+j)
  return value
 def pose(i):return posemap.get((*xy(poses[i][0]),poses[i][1]),J['out'])
 value=state(1);position=pose(1);sp,sk,sv=J['start'];assert position==sp and value&sk==sv
 checks=0
 for i in range(1,ti):
  origin,heading=poses[i];a=types[i];old=value
  for j,L in enumerate(labels):
   q=complex(*L['cell']);local=rotation(q-origin,-heading)
   if q in contexts[i]:codes[j]=0
   if local in geometry[a]['outputs']:
    slot=geometry[a]['outputs'].index(local)
    matches=[n for n,lab in enumerate(L['codes'])if lab and not lab['outer_origin']and(lab['packet'],lab['slot'],*lab['pose'])==(a,slot,*xy(origin),heading)]
    assert len(matches)==1;codes[j]=matches[0]
  value=state(i+1);destination=pose(i+1)
  if position==J['out']:
   assert old==value and(destination==position or destination in J['reentry'])
  else:
   matches=[]
   for sid,to,k,v,f,rm,rv,g,aa in J['transitions']:
    if sid==position and to==destination and not g and aa==a and old&k==v and((old^f)&~rm)|rv==value:matches.append(1)
   assert matches,(index,i)
  position=destination;checks+=1
 assert any(sid==position and g and value&k==v for sid,to,k,v,f,rm,rv,g,a in J['transitions'])
 results.append({'control':index,'tuple':control['tuple'],'strict_packets_replayed':checks,'goal_reached':True,'model_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
out={'status':'PASS all19 physical finite-seed witnesses survive exact producer/prophecy graphs','controls':results}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
