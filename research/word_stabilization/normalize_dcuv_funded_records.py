from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];D=R/'core_periodicity_new/chronology_dcuv';cf=D/'observed_transfers_fast_depth11.json';rf=D/'record_head_offset_search/physical_controls_1_1.json';pf=D/'record_head_offset_search/head_1_1.json';controls=json.loads(cf.read_text())['witnesses'];report=json.loads(rf.read_text());v=json.loads(pf.read_text())['values'];geo=json.loads((D/'literal_residual_geometry.json').read_text());G=geo['geometry'];core={complex(*z)for z in geo['core']};turn=[1,-1j,-1,1j];I=report['I']
def point(z):return[int(z.real),int(z.imag)]
def L(z):return int(z.real+z.imag)
def A(h):return L(complex(-1,1)*turn[h%4])+v[f'c{h%4}']
def T(a,h):
 g=G[a];e=g['endpoint'];return 2*L(complex(*e[:2])*turn[h%4])+A(h+e[2])
output=[]
for ei,e in enumerate(report['bare_record_controls']):
 w=controls[e['witness']];start=e['factor_start'];goal=e['packet_index'];ph=e['phase'];path=w['packet_ids'];p=0j;h=0;board={complex(*z)for z in w['initial_black_seed']};poses=[];boards=[]
 for a in path:
  poses.append((p,h));boards.append(set(board))
  for c in G[a]['word']:
   assert (p in board)==(c=='L');board.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=1j*turn[h]
 gp,gh=poses[goal];np=lambda z:(z-gp)*turn[-gh%4];phase=(ph+gh)%4;threshold=T(path[goal],phase);tokens={z:None for z in boards[start]-{poses[start][0]+q*turn[poses[start][1]]for q in core}};activations=[];records=[]
 for k in range(start,goal+1):
  p,h=poses[k];a=path[k];g=G[a];old=[]
  for z in g['inputs']:
   q=p+complex(*z)*turn[h];who=tokens.pop(q);old.append(who)
   if who is None:activations.append({'packet_index':k-start,'cell':point(np(q)),'value':I+2*L(np(q)*turn[phase])})
  records.append({'packet_index':k-start,'packet':a,'pose':[*point(np(p)),(h-gh)%4],'entering_core':2*L(np(p)*turn[phase])+A(h+ph),'created_peak':2*L(np(p)*turn[phase])+T(a,h+ph),'input_producers':[None if z is None else z-start for z in old]})
  for z in g['outputs']:tokens[p+complex(*z)*turn[h]]=k
 assert records[-1]['created_peak']==threshold and all(z['created_peak']<threshold and z['entering_core']<threshold for z in records[:-1]);assert all(z is not None for z in records[-1]['input_producers']);funding=[a for a in activations if a['packet_index']<goal-start and a['value']>=threshold];assert funding
 source=min(records[-1]['input_producers']);sp,sh=poses[source+start];relative=(gp-sp)*turn[-sh%4];anchor_cells=[]
 for z,who in zip(G[path[goal]]['inputs'],records[-1]['input_producers']):
  if who==source:
   q=gp+complex(*z)*turn[gh];sq=(q-sp)*turn[-sh%4];anchor_cells.append([path[source+start],path[goal],*point(relative),(gh-sh)%4,*point(sq),(sh+ph)%4,threshold+2*L((gp-sp)*turn[ph])])
 output.append({'control':ei+1,'original_witness_index':e['witness'],'target_type':path[goal],'target_global_phase':phase,'record_threshold':threshold,'initial_head_pose':records[0]['pose'],'initial_black_seed':sorted([point(np(z))for z in boards[start]]),'packet_ids':path[start:goal+1],'following_packet_ids':path[goal+1:],'terminal_marker':w['terminal_marker'],'records':records,'activations':activations,'funding_activations':funding,'earliest_goal_producer_index':source,'scope':'Actual complete recurrent-eight factor in target frame; funded bare record, not an unfunded record'})
out=D/'record_head_offset_search/funded_record_controls15.json';out.write_text(json.dumps({'status':'Physical funded-record controls that current omitted-activation abstraction must preserve','potential_sha256':hashlib.sha256(pf.read_bytes()).hexdigest(),'source_controls_sha256':hashlib.sha256(cf.read_bytes()).hexdigest(),'I':I,'count':len(output),'controls':output},indent=2)+'\n');print(out,len(output))
