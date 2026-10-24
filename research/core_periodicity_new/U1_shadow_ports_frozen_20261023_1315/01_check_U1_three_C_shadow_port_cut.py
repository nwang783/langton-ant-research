"""Direct unfunded-U1 consequences of the typed exit-bud halfplane law."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';RP=R/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json';CP=R/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';G=json.loads(GP.read_text())['geometry'];RJ=json.loads(RP.read_text());A=RJ['core_offsets'];T={(a,h):v for a,h,v in RJ['created_peaks']};IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};K=set(map(tuple,json.loads(GP.read_text())['core']));rot=lambda q,h:((q[0],q[1]),(q[1],-q[0]),(-q[0],-q[1]),(-q[1],q[0]))[h]
black=[];white=[];sector=[]
for w in G[7]['requirements']:
 if w[1]<1:continue
 # A0,N→B(1-v,u-1,E) at3C; this B must lie in the valid marked sector.
 B=(1-w[1],w[0]-1,1)
 if sum(B)%2:sector.append(dict(local_cell=w[:2],B_pose=B));continue
 if not w[2]:
  SS=2*sum(B[:2])+T[7,1];entry_upper=[28+2*(sum(B[:2])+sum(rot(z,1)))for z in G[7]['inputs'][2:]];assert min(entry_upper)>SS
  white.append(dict(local_white_cell=w[:2],B_pose=B,U_goal_score=SS,if_Afirst_goal_Cclock=3,upper_produced_min_age=5,forced_entry_upper_activations=entry_upper));continue
 assert w[:2]in G[7]['inputs'];S=2*sum(B[:2])+T[7,1];assert S in(20,24)
 cases=[]
 for p in IDS:
  c=G[p]['name'].count('C');h=(-G[p]['endpoint'][2])%4;e=rot(G[p]['endpoint'][:2],h);P=(-e[0],-e[1]);o=[z for z in G[p]['outputs']if tuple(P[i]+rot(z,h)[i]for i in(0,1))==(1,-1)];assert len(o)==1;o=o[0]
  rel=rot((B[0]-P[0],B[1]-P[1]),-h);key=(mp[p],mp[7],*rel,(1-h)%4,*o,3+c)
  if c<2:assert key in COUNT;cases.append(dict(predecessor=p,pose=[*P,h],age=3+c,query=key,reason='EXACT_COUNTED_EXCLUDED'))
  else:
   core=2*sum(P)+A[h];assert core==28>S;cases.append(dict(predecessor=p,pose=[*P,h],age=5,entry_core=core,reason='EARLIER_CORE_FUNDS'))
 first=[]
 for p in IDS:
  assert all(tuple(z)not in K for z in G[p]['inputs']);val=28+2*max(sum(z)for z in G[p]['inputs']);assert val>=30>S;first.append(dict(source=p,first_source_max_activation=val))
 black.append(dict(U_input=w[:2],B_pose=B,U_goal_score=S,predecessor_cases=cases,source_if_first=first))
assert len(white)==5 and len(black)==3
# In actual goal coordinates U(0,0,N), earlier AheadingW is goalcell-(1,1).
ports=[]
for w in G[7]['requirements']:
 if w[1]>=1 and(sum(w[:2])%2):
  ports.append(dict(earlier_A_pose=[w[0]-1,w[1]-1,3],bud_goal_cell=w[:2],before_black=w[2],reason='SIGNED_HALFPLANE_WHITE_CONTRADICTION'if not w[2]else'FORCED_BUD_ORIGIN_COUNTED_OR_CORE_FUNDS'))
assert len(ports)==8
J=dict(status='AUTHOR_U1_3C_EIGHT_PORT_BARRIER_PASS',scope='Full unfundedU1 I>=28; markedA exactly3C before Ugoal. The8 listed earlierAposes impossible. Applies if such marked clockexists;2C packets can skip it. Not allU1, no finitebox/capture.',target_goal=[0,0,0],target_score=30,record_phase=1,goal_input_cases=black,white_cases=white,sector_impossible_geometry=sector,all8_forbidden_A_ports=ports,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,RP,CP,Path(__file__).resolve()]})
(R/'chronology_dcuv/U1_three_C_shadow_port_cut.json').write_text(json.dumps(J,indent=2)+'\n');print(dict(white_ports=len(white),input_ports=len(black),exact_queries=sum(sum(c['reason']=='EXACT_COUNTED_EXCLUDED'for c in r['predecessor_cases'])for r in black),earlier_core_funding_cases=6,all8_A_ports=[r['earlier_A_pose']for r in ports]))
