"""Fresh FOREIGN northeast output frontier after an arbitrary two-C
ordinary connector. No initialU, GLOBAL-simple or earlier-history premise.
"""
from pathlib import Path
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h
NE={(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1)};sources=[]
for A in'FQB':
 g=l.literal_geometry(W[A]);tr=l.trace(W[A]);ep=after(W[A]);found={tuple(q)for q in g['outputs']if q[0]>=-1 and q[1]>=-1};assert found==NE and ep[0]<=-3 and ep[1]<=-2 and ep[2]==2
 sources.append(dict(actual_foreign=A,ENTRY=(0,0,0),actual_EXIT=ep,all10_SAME_ne_outputs=[dict(cell=q,actual_own_last_R_tick0=tr['last'][q][1],CURRENT_at_RAW_EXIT=True)for q in sorted(NE)]))
assert all([q['actual_own_last_R_tick0']for q in s['all10_SAME_ne_outputs']]==[46,45,30,4,27,9,26,25,8,7]for s in sources)
ports=[];capture=[]
for a in'DCVU':
 g=l.literal_geometry(W[a]);tr=l.trace(W[a]+l.M);rt=l.trace(W[a]);ep=after(W[a]);Kout={add(ep[:2],l.rot(q,ep[2]))for q in l.K}
 for q in sorted(Kout):
  if q not in l.K and q not in rt['last']:assert q in tr['first']and tr['first'][q][0]=='L'and list(q)in g['inputs']
  capture.append(dict(atom=a,actual_EXIT_CORE_cell=q,in_ENTRY_CORE=q in l.K,actual_RAW_last_read=rt['last'].get(q),complete_first_requirement=tr['first'].get(q)))
 for slot in map(tuple,g['inputs']):
  dx,dy=ep[0]-slot[0],ep[1]-slot[1];assert-slot[0]<=1 and dy>=0
  if dy==0:assert dx==1
  ports.append(dict(atom=a,true_input=slot,physical_L_owner=o.describe(a,tr['first'][slot][1]),S_input_x_minus_head_x=-slot[0],E_input_y_minus_head_y=-slot[0],N_RAW_EXIT_minus_original_tag=(dx,dy),equality_y_requires_exit_x_tag_plus1=dy==0))
assert len(ports)==8 and len(capture)==20 and l.literal_geometry(W['C'])['inputs']==[]
assert after(W['C'],(0,0,2))==(0,-1,1)and after(W['C'],(0,0,1))==(1,0,0)
for a in'DVU':
 s=after(W[a],(0,0,2));e=after(W[a],(0,0,1));n=after(W[a]);assert s[0]<=0 and s[1]<0 and e[1]<=0 and n[0]>=0 and n[1]>0
# All nine source-target letter pairs share this ACTUAL ownR14 request.
g=(2,0);target=(3,-1,0);white=[]
for A in'FQB':
 for B in'FQB':
  assert l.trace(W[A])['last'][g]==('R',8);loc=(g[0]-target[0],g[1]-target[1]);tr=l.trace(W[B]+l.M);assert loc==(-1,1)and tr['first'][loc]==('R',14)
  white.append(dict(source_foreign=A,next_foreign=B,source_common_cell=g,source_R_tick0=8,target_relative_source_ENTRY=target,target_local_cell=loc,actual_target_first_R=o.describe(B,14),frontier_cut_reason='targetHEADy-1 < sourceTAGy0, so SAMEoriginal remainsCURRENT outside actual targetENTRY CORE.'))
# Data-level frontier examples distinguish a guaranteed tag from one left
# genuinely unresolved by this one-sided lemma. They are NOT ant histories.
def protected(tag,head):return tag[1]>head[1]or tag[1]==head[1]and head[0]!=tag[0]+1
examples=[]
for head in[(3,-1),(2,0),(3,0),(0,1),(2,2),(3,3)]:
 examples.append(dict(N2_cut_HEAD=head,guaranteed_SAME_CURRENT=sorted(q for q in NE if protected(q,head)),unresolved_original_ports_NOT_discarded=sorted(q for q in NE if not protected(q,head))))
D=[R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='ANY actual F/Q/B normalized to its ENTRY0,0N, then only actual ordinaryRAW D/C/V/U until a real cut, with actualmarker contexts and exactly0/1/2 Cs. No earlierU/firstforeign/globalSIMPLE premise. Ten SAME sourceforeign northeast outputs persist through S0/E1. At an N2 cutHEAD(X,Y), each original g satisfying g_y>Y OR(g_y=Y and X!=g_x+1) is guaranteedCURRENT. The other original ports remain unresolved, not absent.',all3_actual_source_foreign_NE_birth_interfaces=sources,all8_complete_input_to_RAW_EXIT_supports=ports,all20_exitCORE_capture_checks=capture,first_loss_proof='Initially sourceFORE EXIT hasx<=-3,y<=-2. For every g inNE, gx>=-1,gy>=-1. S0 inputsx<=headx+1<=-2<gx, so no first loss. After actualC S->E, headY<=-3 and E inputY<=headY+1<=-2<gy, so no first loss. Cs haveI0. In N2 every firstlossRAW EXITY>=gy, and equality implies EXITX=gx+1. All subsequent N bases strictlyincreaseY. Thus a later cut belowrowgy, or onrowgy exceptatXgx+1, cannotfollow such a loss. First CURRENT loss includes COREcapture, and firstloss handles replacement/rebirth without assumingWHITE permanence.',frontier_is_NOT_strict_order='A lower-row original may remain dormant while another higher row is later consumed. There is no strict consumption ordering or automatic matching of all tags. Only the stated one-sided protected predicate is proved, and every unresolved lower/equality port must be retained.',all9_portable_two_C_foreign_gate_exclusions=white,finite_predicate_examples_NOT_ant_histories=examples,relation_to_reached_control='The genuine U-entry reached33-cell gate in956b495c has sourceF ENTRY(0,4,N), targetF ENTRY(3,3,N), so relative displacement is exactly(3,-1,N). That earlier control is an illustration, not a premise for this portable proof.',not_claimed=['No foreign occurs between sourceFOREIGN and protectedcut.','No claim for3+Cs, othernextFOREIGN poses or alltwoC erosion.','No physicalWHITE permanence or through-contact persistence under arbitraryFOREIGN.','No strictly ordered consumption, loss of unresolved dormantports, bounded-field/finite-state quotient, budget or capture.'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'foreign_N2_frontier.json').write_text(json.dumps(out,indent=2)+'\n');print('AnyFOREIGN 10-output NE frontier: S0/E1 current; N2 row-protected predicate with exact equality exit. All9 nextFOREIGN at relative3,-1,N blocked by SAME sourceR8 vs targetownR14. No U/globalSIMPLE premise.')
