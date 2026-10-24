"""First-atom creator interface excludes one-foreign returned V/VC at clock4.
No new V-retirement inventory or prefix enumeration.
"""
from pathlib import Path
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)};VEL=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def center(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def derive(w):
 p=(0,0);h=0;par=set();rq={};rd={}
 for t,ch in enumerate(w):
  b=(ch=='L')^(p in par);assert p not in rq or rq[p]==b;rq[p]=b;rd.setdefault(p,[]).append([t,ch]);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEL[h])
 return rq,par,p,h,rd
rp=(0,4);rh=2;target=center(rp,rh);assert target==(1,9);r=(0,4);rows=[]
for gi in(4,5):
 pr,_,_,_,prd=derive(G[gi]['word']+M);assert pr[(0,3)]is True and prd[(0,3)][0]==[19,'L'];assert at((0,3),rp,rh)==(0,1)
 for j in(4,5,6):
  _,_,ep,dh,_=derive(W[j]['word']);assert dh==2;ap=sub(rp,ep);ar,_,_,_,ard=derive(W[j]['word']+M);assert not L&{at(q,ap,0)for q in ar};local=sub(r,ap);assert ar[local]is False
  x,y=ap;solutions=[]
  for d in range(x+1):
   v=x-d;rem=y-4-d-3*v
   if rem<0 or rem%4:continue
   u=rem//4;last=[a for a,count in(('D',d),('V',v),('U',u))if count and(a in('V','U')if j in(4,5)else a=='U')]
   solutions.append(dict(d=d,v=v,u=u,allowed_last=last))
  assert all(not z['allowed_last']for z in solutions)
  rows.append(dict(foreign='DCVUFQB'[j],foreign_pose=[*ap,0],returned_packet=G[gi]['name'],returned_pose=[0,4,2],old_original_w=[0,1],first_physical_old_w_read=[19,'L'],physical_owner='following word RAW phase1; returned V exit-core absorption'if gi==4 else'returned VC C-tail RAW phase1',foreign_terminal_center=target,required_first_atom_cell=r,foreign_cell_local=local,foreign_first_before_white_read=ard[local][0],zero_C_head_solutions=solutions,necessary_foreign_C_age_at_least=8))
# Exhaust the FIRST actual atom after the creating U base, with source clock0.
# Internal C is permitted only for actual creating UC/UCC, not a ghost full cut.
interfaces=[]
for i in range(4):
 _,_,ep,dh,rd=derive(W[i]['word']);start=(0,4);end=at(ep,start,0);endh=dh
 if i in(0,1):
  assert center(end,endh)==target
  why='older_first_D_or_C_endpoint_equals_foreign_terminal_center'
 else:
  assert rd[(0,0)][-1]==[4,'R'];assert r==at((0,0),start,0)
  if i==3:
   assert r in{at(q,start,0)for q in L};why='first_U_genuine_permanent_left_star_contains_before_white_cell'
  else:why='first_V_genuine_r_first_retirement_exact_age5_exceeds_foreign_clock4'
 interfaces.append(dict(first_actual_atom='DCVU'[i],actual_start=[0,4,0],actual_end=[*end,endh],old_chord_terminal_center=center(end,endh),actual_source_entry_C_clock=0,exclusion=why))
for gi in(4,5,6):
 assert(0,0)in set(map(tuple,G[gi]['outputs']));_,_,_,_,rd=derive(G[gi]['word']);assert rd[(0,0)][-1]==[4,'R']
for gi in(7,8,9):
 assert L<=set(map(tuple,G[gi]['outputs']));_,_,_,_,rd=derive(G[gi]['word']);assert rd[(0,0)][-1]==[4,'R']
D=[GP,QP,R/'foreign_U_port_interfaces_2026-10-23/manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'seven_word_spatial_return_2026-10-23/first_foreign_all_source_join_manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='A genuine creating U/UC/UCC followed by actual complete eight, first foreign COMPLETE context missing original star, and returned V/VC(0,4,S) needs foreign source-entry C clock>=8. Clock0 exact head/last-base equations and clock4 exhaustive FIRST-atom D/C/V/U interface. Simple repaired proxy used only through first foreign, V/U identity permanence only preforeign. No attained reentry, returned simplicity or further age iteration.',six_returned_V_VC_cases=rows,four_first_actual_atom_cases=interfaces,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'return_V_clock.json').write_text(json.dumps(o,indent=2)+'\n');print('All6 returned V/VC cases need foreign clock>=8: clock0 head/last-base equations; clock4 first-atom D/C geometry or V-r/U-star identity.')
