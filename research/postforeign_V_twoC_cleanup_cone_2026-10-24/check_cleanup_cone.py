"""All-length ordinary TWO-C connector guardian for the first postforeign V.
Finite RAW-offset support, no endpoint-word enumeration or postforeign age law.
"""
from pathlib import Path
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def raw(T):return ''.join(W[a]for a in T)
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h

def reads(a):
 pose=(0,0,0);out=[]
 for t,c in enumerate(W[a]):out.append(dict(atom=a,tick0=t,read_number1=t+1,cell=pose[:2],turn=c));pose=after(c,pose)
 return out
support=[]
for a in'DVU':
 ep=after(W[a]);assert ep[2]==0 and ep[1]in(1,3,4)
 for q in reads(a):
  x,y=q['cell'];N=3+y;WW=4+x;SS=4+ep[1]-y;assert N>=2 and WW>=3 and SS>=4
  support.append(dict(**q,N_head_y_at_least3_cell_y_at_least=N,W_head_y_at_least4_cell_y_at_least=WW,S_actual_EXIT_y_at_least4_cell_y_at_least=SS,actual_zero_C_EXIT_vector=ep))
C_support=[]
for q in reads('C'):
 x,y=q['cell'];assert 3+y>=2 and 4+x>=3;C_support.append(dict(**q,first_C_N_head_y_at_least3_cell_y_at_least=3+y,second_C_W_head_y_at_least4_cell_y_at_least=4+x))
helper=(0,4,2);helper_exit=after(W['V'],helper);assert helper_exit==(-1,1,2);helper_read=[]
for q in reads('V'):
 p=add(helper[:2],l.rot(tuple(q['cell']),2));assert p[1]>=1;helper_read.append(dict(**q,actual_helper_cell=p))
source=l.trace(W['V']);A=(0,1);assert source['last'][A]==('R',11);helper_local_A=l.rot(sub(A,helper[:2]),2);assert helper_local_A==(0,3)and helper_local_A not in l.trace(W['V'])['first']and l.trace(W['V']+l.M)['first'][helper_local_A]==('L',19)
Khelper={add(helper_exit[:2],l.rot(q,2))for q in l.K};assert A in Khelper
# All support is for EXECUTED RAW reads. Actual markers between atoms are
# prefixes of the next RAW, so none are silently omitted from these stages.
# The final helper's following M11 is left to the actual next-context table.
guards={};fields=[]
for fore in'FQB':
 ep=after(W[fore]);ft=l.trace(W[fore]);facts=[]
 for nxt in'DCVUFQB':
  if nxt=='D':cell=(-1,0);color=False;birth=1;kind='first_V_entry_CORE_hole';expected=('L',11)
  elif nxt in'UFQB':cell=(-1,-1);color=False;birth=2;kind='first_V_entry_CORE_hole';expected=('L',12)
  elif nxt=='C':
   cell=(-2,-1)if fore=='F'else(-1,-2);color=True;birth=47 if fore=='F'else 57 if fore=='Q'else 67;kind='SAME_foreign_R_shadow';expected=('R',13 if fore=='F'else 23)
  elif fore=='B':cell=(-2,-1);color=False;birth=1;kind='actual_mandatory_preFOREIGN_U_entry_CORE_hole';expected=('L',13)
  else:
   cell=(-3,-2)if fore=='F'else(-3,-3);color=True;birth=45 if fore=='F'else 46;kind='SAME_foreign_R_shadow';expected=('R',15 if fore=='F'else 24)
  assert cell[1]<=0
  if kind=='first_V_entry_CORE_hole':assert source['last'][cell]==('L',birth)
  else:
   assert cell not in source['first']
   if color:
    physical=add(ep[:2],l.rot(cell,ep[2]));assert ft['last'][physical]==('R',birth)
   else:
    # PlainU is mandatory immediately before firstB after actualG8. In its
    # own chart physical(-1,0) was deleted by U L1; B and the firstV miss it.
    bp=after(raw('UB'));physical=add(bp[:2],l.rot(cell,bp[2]));assert physical==(-1,0)and l.trace(raw('UB'))['last'][physical]==('L',1)
  loc=l.rot(sub(cell,helper_exit[:2]),2);tr=l.trace(W[nxt]+l.M);assert tr['feasible']and tr['first'][loc]==expected;assert color!=(expected[0]=='L')
  fields.append(dict(foreign=fore,next_seven_atom=nxt,actual_first_V_chart_guard=cell,actual_guard_BLACK=color,actual_guard_origin=kind,actual_guard_origin_tick0=birth,no_intervening_read_by_arbitrarily_long_connector='All prior connector RAW reads y>=2; final helper RAW reads y>=1, while this guard has y<=0.',next_atom_local_guard=loc,actual_first_required_read=dict(turn=expected[0],context_tick0=expected[1],context_read_number1=expected[1]+1,canonical=o.describe(nxt,expected[1])),direct_required_color_contradiction=True))
assert len(fields)==21
pairs=[]
for full in('D','DC','V','VC','VCC','U','UC','UCC'):
 tr=l.trace(raw(full+'B')+l.M);pairs.append(dict(full=full,feasible=tr['feasible'],conflict=None if tr['feasible']else tr))
assert [q['full']for q in pairs if q['feasible']]==['U']
paths=[R/'first_foreign_VCCV_terminal_ports_2026-10-24/manifest.json',R/'audits/check_VCCV_terminal_ports_independent.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_ALL_LENGTH_TWO_C_POSTFOREIGN_V_CLEANUP_CONE_PENDING_REVIEW',scope='FIRSTFOREIGN after actualcomplete8, immediate first ordinaryV at0N, then ANY ordinary connector with exactly TWO Cs reaching a helperV at(0,4,S). No bound on N/W/S zero-C run length or order; no other foreign within connector. The helper RAW completes; conclusion excludes a next complete seven-atom RAW+actualM11. Not arbitrary A-loss classification, arbitrary-tail simplicity or arbitrary erosion terminality.',stage_proof=['After firstV RAW, N head is(1,3). Until actualC1, zero-C N motion never lowers y, so all N/C1 RAW reads y>=2.','C1 changes N toW and raises heady by1, hence every W head has y>=4. Zero-C W D/V increase y and U preserves it. C2 W RAW reads y>=3.','C2 changes W toS without changing heady. Every completed S zero-C atom before stipulated helperV must EXIT at y>=4, since the remaining S run cannot increase y. Relative actual EXIT, every D/V/U RAW read has y>=0. Thus all S-run RAW reads y>=4.','Stipulated helperV0,4S RAW reads y>=1. Therefore all guards at y<=0 retain their exact physical colors/identities. The original firstV A at(0,1) is untouched by preceding connector y>=2 and helperRAW misses it; it is aliveCORE at helperEXIT, not current.','No unseen marker is omitted: executed internal M11 reads belong to these actual consecutive RAW atoms. The following helperM11 is not pre-executed; actual next-context contradictions are listed separately.'],all56_zero_C_RAW_read_support_records=support,all15_C_RAW_read_support_records=C_support,all18_final_helper_RAW_read_records=helper_read,original_A_identity=dict(birth_tick0=11,original_cell=A,helper_local=helper_local_A,helper_RAW_misses=True,aliveCORE_at_helper_EXIT=True,actual_next_word_physical_death_tick0=1,death_read_number1=2),all21_terminal_guard_obligations=fields,all8_actual_G8_to_FIRSTB_predecessor_queries=pairs,conclusion='Every stipulated two-C cleanup endpoint has the same physical negative-halfplane port obstruction as literal A,VCCV. All21 next complete seven-atom RAW+actualM11 targets contradict a preserved guard. Thus arbitrarily long N/W/S connector rails cannot repair this specific boundary debt while retaining the cleanup endpoint; actual CORE repairs elsewhere remain allowed.',no_first_contact_or_simple_prefix_assumption_needed=True,no_postFOREIGN_age_or_historical_wire_or_full_source_relabel=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'cleanup_cone.json').write_text(json.dumps(out,indent=2)+'\n');print('All-length two-C cleanup:56 zero-C RAW offsets,15 C offsets,18 helper offsets; N>=2/W>=3/S>=4/helper>=1. All21 negative-port next contexts fail, mandatoryB<-U retained. No run-length cap, postA age or arbitrary A-loss classification.')
