"""Exact actual-atom three-C V-left-step has an entry-clock-zero boundary source.
The current incoming bud is protected by the signed atomic predecessor halfplane.
No first-contact or record-score premise; no arbitrary atomic-word language.
"""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent
GP=W/'chronology_dcuv/literal_residual_geometry.json'
HP=W/'chronology_dcuv/protected_patch2.tsv'
CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
AP=W/'atomic_exit_bud_frozen_20261023_1325/02_atomic_exit_bud_maturation.json'
PP=W/'atomic_predecessor_halfplanes_frozen_20261023_1505/manifest.json'
RP=W/'atomic_common_4C_frozen_20261023_1344/manifest.json'
EP=W/'C_first_E_crossing_frozen_20261023_1428/manifest.json'
G=json.loads(GP.read_text())['geometry']
HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()}
COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()}
IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)}
roles=json.loads(AP.read_text())['roles']
def rot(z,h):
 x,y=z;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
queries=[];openrows=[];closed={}
for r in roles:
 a=r['full_producer'];j=r['atomic_prefix_C'];ex=r['atomic_exit'];ah=ex[2]
 A=tuple(ex[:2]);B=add(A,rot((-1,0),ah));bh=(ah+1)%4;o=tuple(r['bud_full_output_slot'])
 assert rot(sub(o,A),-ah)==(1,-1)
 assert rot(sub(o,B),-bh)==(1,2)
 c=G[a]['name'].count('C');internal=j<c
 for b in[4,5,6]:
  assert [1,2]in G[b]['inputs']
  n=j+3;q=B;dh=bh;key=(a,b,*q,dh,*o);ck=(mp[a],mp[b],*q,dh,*o,min(n,5))
  row=dict(previous_full=a,atomic_prefix_C=j,source_full_C=c,A_full_relative_pose=[*A,ah],B_full_relative_pose=[*B,bh],incoming_bud_full_output=o,full_source_included_C_age=n,A_is_internal_to_full_source=internal,HB_key=key,count5_key=ck)
  if key in HB:reason='SIGNED_HB'
  elif ck in COUNT:reason='SIGNED_COUNT5'
  else:
   if internal:
    assert (a,j)==(1,0)and b in[4,5]
    # A is first C of this full DC; the separately signed C/E3 law applies.
    reason='SIGNED_C_E3_SOURCE_FULL_DC_MUST_BE_FACTOR_FIRST'
   elif a in[6,9]:
    # The immediately preceding full packet ended at A; its last C entered at B,
    # one C before A, giving an exact 4-C atomic full-pose return.
    base=4 if a==6 else 7;L=tuple(G[base]['endpoint'][:2]);lh=G[base]['endpoint'][2]
    L=add(L,rot((0,1),lh));lh=(lh-1)%4
    assert (L,lh)==(B,bh)
    row['last_C_entry_clock_relative_A']=-1
    row['later_B_entry_clock_relative_A']=3
    reason='SIGNED_ATOMIC_FOUR_C_FULL_POSE_NONRETURN'
   else:
    assert (a,j)==(0,0)and b in[4,5]
    reason='PLAIN_D_MUST_BE_FACTOR_FIRST_BY_ITS_OLDER_BUD_WHITE'
   openrows.append(row)
  row['reason']=reason;closed[reason]=closed.get(reason,0)+1;queries.append(row)
assert len(queries)==45 and len(openrows)==10
assert closed=={'PLAIN_D_MUST_BE_FACTOR_FIRST_BY_ITS_OLDER_BUD_WHITE':2,'SIGNED_C_E3_SOURCE_FULL_DC_MUST_BE_FACTOR_FIRST':2,'SIGNED_COUNT5':35,'SIGNED_ATOMIC_FOUR_C_FULL_POSE_NONRETURN':6}
# At the full-D predecessor entry P=(-1,-1,N), an incoming bud would be (0,-2).
# Three-C E halfplane persistence keeps it at B=(-1,0,E), where it is WHITE.
P=(-1,-1);older=add(P,(1,-1));Bn=(-1,0)
white=[]
for b in[4,5]:
 local=rot(sub(older,Bn),-1);req={tuple(t[:2]):bool(t[2])for t in G[b]['requirements']}
 assert local==(2,1)and req[local]is False
 assert sub(Bn,P)==(0,1)
 white.append(dict(target=b,plain_D_predecessor_pose=[*P,0],older_incoming_bud=older,target_local=local,target_requirement='WHITE',C_gap=3,signed_halfplane_X=0))
paths=[GP,HP,CP,AP,PP,RP,EP,Path(__file__).resolve()]
O=dict(status='AUTHOR_ATOMIC_THREE_C_LEFT_STEP_BOUNDARY_CLOCK_ZERO_PASS',scope='Actual atomic cuts inside one complete recurrent-eight factor only. If A is followed after exactly3 atomic entry Cs by full V/VC/VCC at A+rot_h(-1,0),headingh+1, then A has the factor-entry C clock. More precisely A is the first complete packet entry, the second complete entry after a factor-first plain D, or the first C entry inside a factor-first DC. The latter two require target V/VC. No first-contact/funding premise; first-cut exemption explicit. Not arbitrary atomic words, all-gap nonreturn, finite fuel or confinement.',A_normalized_pose=[0,0,0],B_normalized_pose=[-1,0,1],all45_actual_incoming_atom_role_queries=queries,query_counts=closed,plain_D_older_bud_white_cases=white,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
OUT=W/'chronology_dcuv/atomic_three_C_left_step_boundary.json';OUT.write_text(json.dumps(O,indent=2)+'\n');print(closed)
