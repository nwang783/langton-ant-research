"""Finite literal-mask and age arithmetic behind the signed-boundary V1 reuse."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';RP=R/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json';G=json.loads(GP.read_text())['geometry'];RJ=json.loads(RP.read_text());T={(a,h):v for a,h,v in RJ['created_peaks']};K=set(map(tuple,json.loads(GP.read_text())['core']));H=1;S=2*H+26;tau=0
rot=lambda q,h:((q[0],q[1]),(q[1],-q[0]),(-q[0],-q[1]),(-q[1],q[0]))[h]
# Helper E head=(-4-g,1+g). Every listed cell is affine in integer g>=0.
I=[tuple(q)for q in G[7]['inputs']];rows=[]
new_min={( -1,1):4,(-1,2):4,(-1,4):5,(0,2):5,(0,3):5}
DCI=set(map(tuple,G[1]['inputs']));DCO=set(map(tuple,G[1]['outputs']));assert DCI=={(0,1)}
for inp in I:
 dx,dy=rot(inp,1);p=(-4+dx,1+dy);height=sum(p);assert height in(H-2,H-1,H+1)
 # q_g=(p_x-g,p_y+g). Equality to a fixed DC cell needs g=p_x-cell_x.
 for old in DCI|DCO:
  gv=p[0]-old[0];assert gv<0 or p[1]+gv!=old[1]
 m=new_min[inp];entry_excluded_at_I28=28+2*height>=S;entry_excluded_at_I30=30+2*height>=S
 rows.append(dict(input=inp,affine_cell_at_g0=p,g_coefficient=[-1,1],height=height,produced_min_age_at_helper=m,minimum_age_at_preDC_cut=m-3,latest_birth_clock_relative_tau=3-m,entry_excluded_I28=entry_excluded_at_I28,entry_excluded_I30=entry_excluded_at_I30))
assert sorted(r['minimum_age_at_preDC_cut']for r in rows)==[1,1,2,2,2]
assert sum(r['entry_excluded_I28']for r in rows)==3 and all(r['entry_excluded_I30']for r in rows)
# If young lower age3 exists,1230+1146 make its V-family source factor-first.
# Relative source(0,0,N), helperU(0,-1,E); in V1 normalization helperheightH-4.
source_head_height=H-3;initial_heights=[source_head_height+sum(q)for q in G[4]['inputs']];assert initial_heights==[H,H]
assert all(q not in K for q in map(tuple,G[4]['inputs']))
activation_I28=[28+2*v for v in initial_heights];assert activation_I28==[S+2,S+2]
assert 2*(H-4)+T[7,1]==S-4
# All five helper identities predate DC: old entries do; produced helper ages
# >=4 prohibit every strict later birth (goal/helper clocktau+3; afterDCtau+1).
# Every source output and source input is disjoint from the five affine masks.
# Hence at preDC:5 helpers+DCinput=6; immediately postDC:5 helpers+4newO=9.
assert len(DCO)==4
assert all(28+2*sum(q)>=S+2 for q in DCI)
J=dict(status='AUTHOR_V1_U_HELPER_PRE_DC_CUT_PASS',scope='Only signedDC-age3→V1 last-U-helper branch, full unfundedI>=28. Boundary theorem supplies conditional lower4. No fresh roots, rank, recurrence, V1 closure or capture.',normalization=dict(H=H,S=S,DC_birth_clock=tau,U_helper_head_affine=[-4,1],goal_head=[0,1,1],helper_C_clock=3,helper_peak=S-4),young3_source_first_activation=dict(source_head_height=source_head_height,initial_input_heights=initial_heights,I28_activations=activation_I28,outer_score=S),five_helper_inputs=rows,pre_DC_required_live_identities=6,post_DC_required_live_identities=9,pre_DC_produced_at_I28_at_least=4,post_DC_produced_at_I28_at_least=7,pre_DC_produced_at_I30=6,post_DC_produced_at_I30=9,meaning='At preDC the five eventual U-helper identities coexist with DCinput; their produced ages are >=1,1,2,2,2, entry identities exempt. At I28 three helpers forced produced; at I30 all five. No helper identity is a DC I/O; all four fresh DC outputs add to the immediate postDC cut.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,RP,Path(__file__).resolve()]})
(R/'chronology_dcuv/v1_U_helper_preDC_cut.json').write_text(json.dumps(J,indent=2)+'\n');print(dict(pre_DC=6,post_DC=9,pre_DC_helper_ages=sorted(r['minimum_age_at_preDC_cut']for r in rows),source_first_I28_activations=activation_I28,S=S))
