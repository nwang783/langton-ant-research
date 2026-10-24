"""Small fresh RAW donor supplement: V/U right R9 throughC3, C outputs
through one postEXIT C. No old-eight maturity import or K4 right-port claim.
"""
from pathlib import Path
from collections import Counter
import json,hashlib,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h
right=[]
for src,anchors in(('V',{(0,0)}),('U',{(0,0),(0,1)})):
 st=l.trace(W[src]);assert st['last'][(1,0)]==('R',9)and[1,0]in l.literal_geometry(W[src])['outputs'];rows=[]
 for atom in'DCVU':
  geo=l.literal_geometry(W[atom]);tr=l.trace(W[atom]+l.M)
  for slot in map(tuple,geo['inputs']):
   for hd in range(4):
    p=(*sub((1,0),l.rot(slot,hd)),hd);q=dict(actual_source_RAW=src,consumer=atom,slot=slot,pose=p)
    if(sum(p[:2])+hd)%2:q['classification']='sector'
    else:
     hits=[]
     for tag in sorted(anchors):
      loc=l.rot(sub(tag,p[:2]),-hd);f=tr['first'].get(loc)
      if f:hits.append(dict(SAME_anchor=tag,local=loc,actual_first=f,owner=o.describe(atom,f[1]),TRUE_input_not_intrinsically_invalid_but_original_anchor_must_remain_CURRENT=True))
     if hits:q.update(classification='would_touch_independently_guarded_anchor',hits=hits)
     else:q['classification']='N0_endpoint_obligation'
    rows.append(q)
  assert l.literal_geometry(W['C'])['inputs']==[]
 assert len(rows)==32 and Counter(q['classification']for q in rows)=={'sector':16,'would_touch_independently_guarded_anchor':12,'N0_endpoint_obligation':4}
 keep=[q for q in rows if q['classification']=='N0_endpoint_obligation'];assert {(q['consumer'],tuple(q['pose']))for q in keep}=={('D',(1,-1,0)),('V',(1,-3,0)),('U',(2,-2,0)),('U',(2,-4,0))};ep=after(W[src]);assert ep[1]in(3,4)
 right.append(dict(actual_source_RAW=src,SAME_right_cell=(1,0),last_R_birth_tick0=9,birth_read_number1=10,current_anchor_source='signed freshV r throughC4'if src=='V'else'signed freshU LEFT throughC3',all32_earliest_RIGHT_CURRENT_loss_roles=rows,deadline_proof='Before protected cutK<=3, independent anchors are CURRENT at every earlier simple cut. A first right-loss consumer mustMISS them in COMPLETE context, including marker CORE absorption. The four remaining N gates forceK0 and have negativeheady; creating RAW exitsy3or4 and zero-C N motion never lowersy. Thus no such loss occurs by3.',scope='SIMPLE ordinary source-prefix and actualmarkers; no foreign afterbirth. Earlier foreign permitted. NoK4 or all-age right permanence.'))
# A fresh C's three outputs lie strictly right of both initial W and first S
# input cones. This fact needs no proxy simplicity or old producer age law.
cgeo=l.literal_geometry(W['C']);ctr=l.trace(W['C']);cep=after(W['C']);assert cep==(0,1,3);cO=list(map(tuple,cgeo['outputs']));assert len(cO)==3 and all(q[0]>=1 for q in cO)
c_birth=[dict(SAME_source_C_output=q,birth_tick0=ctr['last'][q][1],birth_read_number1=ctr['last'][q][1]+1)for q in cO];inputcones=[]
for atom in'DCVU':
 geo=l.literal_geometry(W[atom])
 for slot in map(tuple,geo['inputs']):
  wx=-slot[1];sx=-1-slot[0];assert wx<=-1 and sx<=0
  inputcones.append(dict(ordinary_consumer=atom,input_slot=slot,actual_physical_L=o.describe(atom,l.trace(W[atom]+l.M)['first'][slot][1]),W_head_x_at_most0_input_x_at_most=wx,S_head_x_at_most_minus1_input_x_at_most=sx))
assert len(inputcones)==8
assert after(W['C'],(0,0,3))==(-1,0,2)
reader=(2,0,2);Kreader={add(reader[:2],l.rot(q,reader[2]))for q in l.K};assert(1,0)in Kreader and(2,0)in Kreader
paths=[R/'fresh_RAW_V_U_early_donor_guards_2026-10-24/manifest.json',R/'audits/check_fresh_RAW_donors_independent.json',R/'postforeign_V_rA_nonterminal_guardian_2026-10-24/manifest.json',R/'audits/check_postforeign_V_pair_guardian_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_FRESH_RAW_DONOR_RIGHT_AND_C_PORT_SUPPLEMENT_PENDING_REVIEW',all2_fresh_V_U_RIGHT_R9_guard_proofs=right,fresh_C_all3_output_births=c_birth,all8_plain_input_coordinate_supports=inputcones,C_output_proof='Actual sourceC ENTRYclock0 becomes EXITclock1 at head0,1W. Until the nextC, W headsx<=0 and every true input hasx<=-1. The one possible postEXITC movesheadx downby1 and turnsS; thereafter S headsx<=-1 and every true input hasx<=0. All3 genuine sourceC O cells have x>=1, so no CURRENT loss through one postEXITC (sourceENTRYclock2). C hasI0. This includes marker-owned CORE absorption; it is not physical WHITE permanence.',C_scope='Fresh actual RAW C, ordinarysuffix, actualmarkers, noforeign aftersource. Earlierforeign permitted. No proxy simplicity needed for this C-only coordinate reserve.',reader_C_source_relative=dict(actual_reader_RAW='C',pose=reader,actual_ENTRY_CORE=sorted(Kreader),V_U_current_RIGHT_R9_cell=(1,0),C_current_common_R8_cell=(2,0),true_source_ENTRY_age=2,C_true_postEXIT_age=1,contradiction='A CURRENT original donor tag lies in the actual C reader ENTRY CORE. Do not call this a BLACK-versus-L conflict.'),conclusion='Fresh V B and fresh U a stay CURRENT through trueC3 under independently guarded simple ordinary source-prefix; freshC O3 stay CURRENT through one actual postEXITC without simplicity. In particular allthree donors block readerC2,0S at trueSOURCEENTRYage2, with C clockshift retained.',no_old8_age_transfer_or_K4_U_right_claim_or_physical_CORE_omission=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'right_C_ports.json').write_text(json.dumps(out,indent=2)+'\n');print('Fresh RIGHT supplement: V/U64roles, each16sector12anchortouch4 N0-unreachable. RIGHT R9 throughC3. FreshC O3 protected by8 W/S input cones throughpostEXITC1. ReaderC2,0S CURRENT/CORE contradiction, actualCclockshift retained.')
