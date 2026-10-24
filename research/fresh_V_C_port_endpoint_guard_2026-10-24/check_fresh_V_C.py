"""Fresh V C=(2,1) reserve; no age rule is transported across a FOREIGN."""
from pathlib import Path
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return (*q,h)
def local(g,p):return l.rot(sub(g,p[:2]),(-p[2])%4)
def relative(p,source):return(*local(p[:2],source),(p[2]-source[2])%4)
r=(0,0);B=(1,0);C=(2,1);held={r,B,C}
Vraw=l.trace(W['V']);VO=set(map(tuple,l.literal_geometry(W['V'])['outputs']))
assert held<=VO and Vraw['last'][r]==('R',4)and Vraw['last'][B]==('R',9)and Vraw['last'][C]==('R',7)
# Signed fresh r throughC4 and B throughC3 give the two independent anchors
# at any hypothesized earlier first C loss, under this same simple prefix.
rows=[]
for h in range(4):
 for A in'DVU':
  ct=l.trace(W[A]+l.M)
  for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
   p=(*sub(C,l.rot(slot,h)),h);row=dict(clock_heading=h,first_C_loss_actor=A,input=slot,ENTRY=p,actual_first_L=o.describe(A,ct['first'][slot][1]))
   if(sum(p[:2])+h)%2:route='sector'
   else:
    bad=[]
    for g in sorted(held):
     q=local(g,p);f=ct['first'].get(q)
     if q in l.K or f and f[0]=='R':bad.append(dict(SAME_held=g,local=q,first=f,reason='ENTRY_CORE'if q in l.K else'first_WHITE'))
    if bad:row['held_r_B_first_C_conflicts']=bad;route='held_field'
    else:
     if h==0:
      assert p[1]<3;route='N0_below_actual_sourceV_EXIT_y3'
     elif h==3:
      assert p==(3,2,3)and A=='U';route='W1_below_actual_minimum_head_y4'
     else:raise AssertionError(('unexpected firstC loss',row))
   row['route']=route;rows.append(row)
assert len(rows)==32
assert Counter(z['route']for z in rows)=={'sector':16,'held_field':11,'N0_below_actual_sourceV_EXIT_y3':4,'W1_below_actual_minimum_head_y4':1}
# After source clock3, these literal exits alone control N4/W5 targets; the
# earlier r/B anchor theorem is NOT extended to those later clocks.
endpoints=[]
for h in[0,3]:
 for A in'DVU':
  ct=l.trace(W[A]+l.M)
  for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
   p=(*sub(C,l.rot(slot,h)),h);ep=after(W[A],p);assert ep[1]>=1
   endpoints.append(dict(heading=h,first_loss_actor=A,input=slot,ENTRY=p,RAW_EXIT=ep,actual_first_L=o.describe(A,ct['first'][slot][1]),exit_y_at_least1=True))
assert len(endpoints)==16 and l.literal_geometry(W['C'])['inputs']==[]
# Real mixed-V prefix. Marked vs body-only cuts are explicitly separated.
full_labels='UQVVCVUCVUUUCDUUCDDUUCDUF';nominal=''.join(W[A]for A in full_labels)+l.M
bad=l.trace(nominal);assert not bad['feasible']and bad['conflict_read']==509 and bad['previous_read']==117 and tuple(bad['cell'])==(-7,-4)and bad['turn']=='R'
actual=nominal[:509];tr=l.trace(actual);assert tr['feasible']
seed={q for q,(c,t)in tr['first'].items()if c=='L'};BLACK=set(seed);ids={q:('initial',q)for q in BLACK};p=(0,0,0);reads=[];cuts=[];ends={};off=0
for i,A in enumerate(full_labels):
 off+=len(W[A])
 if off<=509:ends[off]=(i,A)
for t,c in enumerate(actual):
 q=p[:2];assert(q in BLACK)==(c=='L');prior=ids.get(q)
 if c=='L':BLACK.remove(q);ids.pop(q)
 else:BLACK.add(q);ids[q]=('new_R',t)
 reads.append(dict(tick0=t,cell=q,turn=c,prior_identity=prior));p=after(c,p)
 if t+1 in ends or t+1==509:
  marked=t+1 in ends and t+12<=509 and actual[t+1:t+12]==l.M
  cuts.append(dict(actual_read_count=t+1,boundary=ends.get(t+1),context_complete_marked_RAW_cut=marked,pose=p,complete_BLACK=sorted(BLACK),V_C_BLACK=(-7,-4)in BLACK,V_C_identity=ids.get((-7,-4)),V_C_outside_actual_pose_CORE=local((-7,-4),p)not in l.K))
assert reads[117]['turn']=='R'and reads[117]['cell']==(-7,-4)
assert all(z['cell']!=(-7,-4)for z in reads[118:])
source=(-5,-3,2);assert after(nominal[:110])==source and nominal[110:128]==W['V']
reader=after(nominal[:493]);assert reader==(-9,-2,1)and relative(reader,source)==(4,-1,3)
assert local((-7,-4),reader)==(2,2)
assert l.trace(W['D']+l.M)['first'][(2,2)]==('R',16)
cut493=next(z for z in cuts if z['actual_read_count']==493);assert cut493['context_complete_marked_RAW_cut']and cut493['V_C_identity']==('new_R',117)and cut493['V_C_outside_actual_pose_CORE']
cut503=next(z for z in cuts if z['actual_read_count']==503);assert not cut503['context_complete_marked_RAW_cut'] # actual D body, not full D+M
assert p[:2]==(-7,-4)and p[:2]in BLACK # requested R fails; actual ant would turn L
D=['fresh_RAW_V_U_early_donor_guards_2026-10-24/manifest.json','audits/check_fresh_RAW_donors_independent.json','fresh_RAW_donor_right_C_ports_2026-10-24/manifest.json','audits/check_fresh_donor_right_C_ports_independent.json','immediate_U_FOREIGN_ordinary_tail_simplicity_2026-10-24/manifest.json','audits/check_immediate_U_FOREIGN_tail_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='A genuinely fresh actual RAW V, then only ordinary RAWs with real contexts and a SIMPLE executed source-prefix. SAME source C=(2,1), actual lastR7, staysCURRENT through source-entry Cclock3. It also staysCURRENT at an N4 or W5 target heady<=0 reached by that simple source-prefix. No foreign AFTER source; any earlier history/FOREIGN is allowed. No target-through-input persistence or oldG8 age imported afterFOREIGN.',all32_early_first_C_CURRENT_loss_rows=rows,all16_N4_W5_first_loss_RAW_exit_bounds=endpoints,
 proof=['The independently signed fresh r and rightB guards retain SAME r(0,0) throughC4 and B(1,0) throughC3. At the hypothesized first C loss throughC3, r/B and C are CURRENT at actorENTRY. All32 true-input alignments include marker-only CORE absorption.16 wrong sectors and11 CURRENT/CORE-or-firstWHITE conflicts are exact. The remaining four N0 actors have negativey, unreachable after actual creatingV EXIT(1,3,N). The remaining W1 U(3,2,W) is below the minimum W1 heady4 after C1. C hasI0, so no silent-C escape. Thus C isCURRENT throughC3. No simultaneous TRUE input is relabeled a color contradiction.',
 'For an N4 target y<=0, any earlier first C loss completes its actual N BASE RAW at y>=1; N cannot descend back. For W5, an earlier N4 loss must be followed by the remaining C5, which raisesy once, and W motion cannot lower it. A same-W5 firstloss also exitsy>=1. Neither reaches y<=0. No r/B persistence beyond their signed clocks is assumed. Actual C tails, marker-only capture and raw/full completion clocks are retained.'
 ],actual_mixed_V_control=dict(scope='Genuine complete finite seed and509 physical reads. Last fully context-complete marked cut is C5 RAWEXIT493. Actual subsequentD10 and U first6 execute, but D does NOT have its own fullM; requested U R6 fails at509. No completed D+M, U, nextFOREIGN or physical termination is asserted.',nominal_labels=full_labels,complete_seed=sorted(seed),mass=len(seed),all509_actual_reads=reads,all_RAW_body_and_context_marked_cuts=cuts,genuine_second_initial_V_ENTRY=source,genuine_C_R_birth_tick0=117,world_C_cell=(-7,-4),context_complete_reader_ENTRY=reader,reader_in_V_frame=(4,-1,3),reader_D_context_first_WHITE=o.describe('D',16),same_physical_read_U_owner=o.describe('U',6),failed_GLOBAL_tick0=509,actual_next_turn='L',source_simple_prefix_use='Signed488 applies to the actually marked UQ ordinary prefix ending atC5; its actual M is D10 plus U firstL. It is not invoked on the unvalidated later D+M or U.'),limits=['Not an all-age/full-six-output V seal; A can genuinely retire throughCORE atC2 in prepared/genuine VCCV controls.','No physical WHITE claim, no loss budget, no extraD/U proxy from partialfinalM, no postcontact maturity or secondFOREIGN transfer.','This guards one real mixed-rail producer; it is not an exhaustive mixedS-run C5 exclusion or attained SOURCEQ loss history.'],dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest()for p in D})
(H/'fresh_V_C.json').write_text(json.dumps(out,indent=2)+'\n')
print('FreshV C reserve:32 early roles=16sector+11field+5endpoint;16 late exits. Genuine',len(seed),'cell509-read mixedV control; D context16 / physical U6 fails, no borrowed D-M.')
