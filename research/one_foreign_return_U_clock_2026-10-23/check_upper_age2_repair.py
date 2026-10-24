"""Separate causal guard for the exact age-two VC upper input left by51018788.
The false universal V minimum3 is explicitly rejected, never reused.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
G=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];W=json.loads((R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json').read_text())['macro_words'];M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};VEL=((0,1),(1,0),(0,-1),(-1,0));L={(0,0),(0,1),(1,0),(1,1)}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def derive(w):
 p=(0,0);h=0;par=set();rq={};rd={}
 for t,ch in enumerate(w):
  b=(ch=='L')^(p in par);assert p not in rq or rq[p]==b;rq[p]=b;rd.setdefault(p,[]).append([t,ch]);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEL[h])
 return rq,par,p,h,rd
# Bind the actual signed minima, not a vague all-V lower bound.
QP=R/'audits/dcuv_count5_replay/queries.json';Q=json.loads(QP.read_text());assert Q['status'].startswith('PASS')
minima={k:v['certified_minimum_C_age']for k,v in Q['slots'].items()}
assert minima['4:(0, 3)']==2 and minima['5:(0, 3)']==2 and minima['6:(0, 3)']==5
assert minima['4:(1, 2)']==3 and minima['5:(1, 2)']==3
for k in('0:(0, 1)','1:(0, 1)'):assert minima[k]==3
for b in(7,8,9):
 for z in('(-1, 4)','(0, 2)','(0, 3)'):assert minima[f'{b}:{z}']==5
# Original note's sole S C3 V-parent requires a FIRST tail: VC or VCC.
# VCC is excluded by upper minimum5; VC remains at upper age exactly2.
p=(2,8);h=2;upper=(2,5);selected=(1,6);raw,_,_,_,rd=derive(G[5]['word']+M)
assert at((0,3),p,h)==upper and at((1,2),p,h)==selected
assert raw[(0,3)]is True and rd[(0,3)][0]==[19,'L']
assert raw[(1,2)]is True and rd[(1,2)][0]==[13,'L']
# Both known initial colors come from the real source's actual first atom.
ur,_,_,_,urd=derive(W[3]['word']);assert upper not in ur and selected not in ur
first=[]
for i in range(4):
 rq,_,_,_,rd0=derive(W[i]['word']);assert rq[(2,1)]is False and rd0[(2,1)][0]==[7,'R'];first.append(dict(first_actual_atom='DCVU'[i],global_upper=upper,first_read=[7,'R']))
# If the containing original creator is UC/UCC, C1 is the first actual atom.
# It forces selected=(1,6) initially white via local(1,2) R13.
cr,_,_,_,crd=derive(W[1]['word']);assert cr[(1,2)]is False and crd[(1,2)][0]==[13,'R']
creators=[]
for gi in(7,8,9):
 present=upper in set(map(tuple,G[gi]['outputs']))
 assert present==(gi in(8,9))
 creators.append(dict(original_creator=G[gi]['name'],upper_is_full_output=present,reason='creator_C1_forces_selected_16_initially_white_thus_age_at_most2_below_selected_min3'if present else'plain_creator_U_does_not_output_25'))
# Any produced upper has birthclock>=0, and VC clock2 upper minimum2 forces
# exact birthclock0. Exhaust EVERY full-eight output alignment at heading N.
# A later clock0 N head obeys x>=0, y>=4+x and y-4-x even; zero-C counts
# moreover solve x=d+v,y-4=d+3v+4u. These equations force the two admitted
# heads(0,4) or(1,5), the latter reached by exactly one plain D.
origins=[];surv=[]
for gi in(0,1,4,5,6,7,8,9):
 for slot in map(tuple,G[gi]['outputs']):
  bp=sub(upper,slot);x,y=bp;solutions=[]
  if(sum(bp))%2:why='wrong_active_sector'
  else:
   for d in range(max(x+1,0)):
    v=x-d;rem=y-4-d-3*v
    if rem>=0 and rem%4==0:solutions.append(dict(d=d,v=v,u=rem//4))
   if not solutions:why='no_clock0_N_head_count_solution_after_creator_U_base'
   else:
    assert gi in(4,5,6,7,8,9)and(bp,slot)in(((0,4),(2,1)),((1,5),(1,0)))
    if bp==(0,4):assert solutions==[dict(d=0,v=0,u=0)]
    else:assert solutions==[dict(d=1,v=0,u=0)]
    guardian=bp # genuine local r=(0,0), born R4 in this actual full producer.
    local=rot(sub(guardian,p),-h);assert raw[local]is False
    _,_,_,_,srd=derive(G[gi]['word']);assert srd[(0,0)][-1]==[4,'R']
    why='genuine_V_r_first_retirement_age5_or_U_star_permanence_vs_actual_VC_before_white'
    surv.append(dict(producer=G[gi]['name'],full_entry=[*bp,0],full_entry_C_clock=0,upper_output_slot=slot,guardian=guardian,guardian_VC_local=local,first_VC_before_white_read=rd[local][0],head_count_solutions=solutions,identity_law='V_r_exact_first_retirement5'if gi in(4,5,6)else'U_left_star_permanent_old_eight'))
  origins.append(dict(producer=G[gi]['name'],output_slot=slot,full_entry=[*bp,0],head_count_solutions=solutions,reason=why))
assert len(surv)==12 and Counter(tuple(r['full_entry'][:2])for r in surv)=={(0,4):6,(1,5):6}
D=[H/'manifest.json',H/'rejected_candidate_correction_manifest.json',QP,R/'audits/check_dcuv_count5_queries_independent.py',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Separate repair of ONLY the age-two VC(2,8,S) upper(2,5) origin branch in rejected51018788. Its initial-white upper needs an exact clock0 full producer. Original UC/UCC C1 origin makes selected(1,6) initially white and too young; all later clock0 origin heads are0,4 or1,5, carrying genuine r/star guardians required WHITE by actual VC. No false universal V minimum3, no postforeign age law, no attained history.',actual_signed_input_minima=minima,exact_surviving_VC_parent=dict(pose=[2,8,2],entry_C_clock=2,upper_cell=upper,upper_input_slot=[0,3],upper_minimum_age=2,selected_cell=selected,selected_input_slot=[1,2],selected_minimum_age=3),first_actual_atom_upper_initial_color=first,original_creator_cases=creators,all_clock0_fullproducer_upper_output_alignments=origins,twelve_actual_guardian_origins=surv,dependencies={str(f.relative_to(R)):hashlib.sha256(f.read_bytes()).hexdigest()for f in D})
(H/'upper_age2_repair.json').write_text(json.dumps(o,indent=2)+'\n');print('Exact age2 VC upper branch excluded by original-C1 selected repair or12 genuine r/star clock0 origins, not by false upper age3.')
