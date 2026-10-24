from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry']
def rot(p,h):x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
assert G[8]['endpoint']==[0,5,3]and G[9]['endpoint']==[-1,5,2]
zero=[];turn=[]
for a in[0,4,7]:
 dx,dy,_=G[a]['endpoint'];w=rot((dx,dy),3);s=rot((dx,dy),2);assert w[0]<=-1 and s[0]<=0 and s[1]<0
 zero.append(dict(type=a,W_endpoint=w,S_endpoint=s))
for a in[1,5,8]:
 dx,dy,dh=G[a]['endpoint'];w=rot((dx,dy),3);assert dh==3 and w[0]<=-2
 turn.append(dict(type=a,W_to_S_endpoint=w))
D=[GP,Path(__file__).resolve(),W/'U_recycled_q_consumer_frozen_20261023_1954/manifest.json']
R=dict(status='AUTHOR_Q_SOURCE_HISTORY_PENDING_AUDIT',scope='Genuine UC recycled-q output(-1,2) never retires inside retained factor: its only signed V/VC consumer would be at(-1,5,S), age2, but UC exit(0,5,W) atclock1 cannot reach it with exactlyone remaining C. Every UCC recycled-q consumer must be the IMMEDIATELY following V/VC, at actual UCC exit(-1,5,S), clock2. No statement of plain-U q permanence or all UCC-output permanence.',UC_exit=G[8]['endpoint'],UCC_exit=G[9]['endpoint'],only_q_consumer_pose=[-1,5,2],forced_age=2,UC_required_strict_displacement=[-1,0],UC_remaining_C=1,zero_C_cones=zero,one_C_turns=turn,UC_actual_max_possible_x_displacement=-2,UCC_empty_S_zero_run_necessary=True,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U_q_source_history.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(R,indent=2))
