"""Reader-independent N4 negative-y extension of the qualified fresh-D reserve."""
from pathlib import Path
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
old=json.loads((R/'original_F_piece_firstpost_DC_2026-10-24/F_piece_DC.json').read_text())['fresh_D_common_entry_reserve']
assert len(old['all16_plain_E3_sourceD_DC_common_queries'])==16
assert 'CURRENT through K3' in old['statement']and 'ACTUAL preceding seven-atom RAW'in old['statement']
q=(2,0);rows=[]
for A in'DVU':
 ct=l.trace(W[A]+l.M)
 for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
  p=(*sub(q,slot),0);ep=after(W[A],p)
  assert ep[1]>=0
  rows.append(dict(first_CURRENT_loss_actor=A,true_input=slot,ENTRY=p,RAW_EXIT=ep,actual_first_L=o.describe(A,ct['first'][slot][1]),active_sector=(sum(p[:2])%2==0),cannot_reach_any_later_N_cut_y_negative=True))
assert len(rows)==8
# A real UQ ordinary factor deliberately moved C1 far enough down that its
# own outputs miss the intended late V/U. A different old common blocks C5.
labels='UQDDDDDDCDDVVVCVUUUUCDUUCDDUU'
raw=''.join(W[A]for A in labels);assert len(raw)==558
actual=raw+W['C'][:12];tr=l.trace(actual);assert tr['feasible']and len(actual)==570
probe=l.trace(raw+W['C']+W['D']+W['U']+W['F']+l.M)
assert not probe['feasible']and probe['conflict_read']==570 and probe['previous_read']==130 and tuple(probe['cell'])==(-9,-3)and probe['turn']=='R'
source_entry=(-7,-3,2);assert after(raw[:122])==source_entry and raw[122:132]==W['D']
assert labels[:6]=='UQDDDD' and labels[6:].count('C')==4
reader_entry=after(raw);assert reader_entry==(-9,-1,2)
reader_relative=(*local(reader_entry[:2],source_entry),(reader_entry[2]-source_entry[2])%4)
assert reader_relative==(2,-2,0)and local((-9,-3),source_entry)==q
assert local((-9,-3),reader_entry)==(0,2)and l.trace(W['C']+l.M)['first'][(0,2)]==('R',12)
seed={p for p,(c,t)in tr['first'].items()if c=='L'};B=set(seed);ids={g:('initial',g)for g in B};p=(0,0,0);reads=[];cuts=[];ends={};off=0
for i,A in enumerate(labels):off+=len(W[A]);ends[off]=(i,A)
for t,c in enumerate(actual):
 g=p[:2];assert(g in B)==(c=='L')
 prior=ids.get(g)
 if c=='L':B.remove(g);ids.pop(g)
 else:B.add(g);ids[g]=('new_R',t)
 reads.append(dict(tick0=t,cell=g,turn=c,prior_identity=prior));p=after(c,p)
 if t+1 in ends or t+1 in[569,570]:
  current=(-9,-3)in B and local((-9,-3),p)not in l.K
  cuts.append(dict(actual_read_count=t+1,boundary=ends.get(t+1),pose=p,complete_BLACK=sorted(B),common_BLACK=(-9,-3)in B,common_identity=ids.get((-9,-3)),common_CURRENT=current))
assert reads[130]['turn']=='R'and reads[130]['cell']==(-9,-3)
assert all(r['cell']!=(-9,-3)for r in reads[131:])
assert all(z['common_CURRENT']and z['common_identity']==('new_R',130)for z in cuts if z['boundary']and z['actual_read_count']>=132)
assert p[:2]==(-9,-3)and p[:2]in B # actual next turn L, requested C ownR12 fails
lastcut=next(z for z in cuts if z['actual_read_count']==558);assert lastcut['common_CURRENT']
D=['original_F_piece_firstpost_DC_2026-10-24/manifest.json','original_F_piece_firstpost_DC_2026-10-24/partial_scope_qualification_manifest.json','audits/check_F_DC_partial_qualification_independent.json','immediate_U_FOREIGN_ordinary_tail_simplicity_2026-10-24/manifest.json','audits/check_immediate_U_FOREIGN_tail_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Select any actual fresh D RAW with a real preceding seven-atom RAW; follow it only by ordinary RAWs, SIMPLE as an executed source-prefix through a target N-facing marked cut at actual source-entry C clock4 and heady<0. Its SAME commonR8(2,0) is CURRENT at that ENTRY. No foreign after source; an earlier foreign is allowed. No persistence through a target TRUE input or RAW is claimed.',source_only_retained_qualified_common_interface=old,all8_marker_inclusive_N4_first_CURRENT_loss_ports=rows,proof='The independently qualified fresh-D common theorem retains SAME common through C3 under exactly this source-prefix simplicity and preceding-RAW premise. Any earlier N4 CURRENT loss, including marker-only CORE absorption, completes its genuine BASE RAW at y>=0 by all8 literal input/exit rows. Subsequent N-only motion cannot reach a later N-facing cut with y<0. An N4 C would already turn to W and cannot precede this same-clock N cut. Thus no earlier loss exists. The target actor itself may consume a TRUE input; the guard stops at ENTRY.',selected_actual_UQ_control=dict(scope='Genuine UQ ordinary prefix with real nextC first11=M and one additional C read. Candidate C5 ownR12 fails; no completed C5, targetFOREIGN or physical termination is claimed.',nominal_complete_labels=labels+'CDUF',actual_complete_RAW_labels=labels,actual_partial_C_read_count=12,complete_seed=sorted(seed),mass=len(seed),all570_actual_reads=reads,all_completed_RAW_and_partial_cuts=cuts,genuine_fourth_S_D_ENTRY=source_entry,source_common_birth_tick0=130,world_common_cell=(-9,-3),next_C5_ENTRY=reader_entry,reader_in_D_source_frame=reader_relative,requested_reader_C_R12=o.describe('C',12),failed_GLOBAL_tick0=570,real_next_turn='L',no_intervening_read_since_genuine_birth=True,simplicity_source='Separately signed488 special UQ arbitrary ordinary tail theorem, applied only to the actually completed RAW prefix and its real supplied M11. This new use does not alter any earlier frozen secondFOREIGN dependency.'),limits=['The rejected143d universal F-pair/full84 claim stays rejected. Only its independently retained fresh-D common-through-C3 sublemma is reused, with mandatory45 qualification.','No unconditional common survival after arbitrary previous ordinary self-contact; the simple source-prefix is essential.','No all-C5 target exclusion, unbounded family exhaustion, completed sourceFOREIGN loss, output fuel, repeatedFOREIGN transfer or capture.'],dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest()for p in D})
(H/'negative_N4_common.json').write_text(json.dumps(out,indent=2)+'\n')
print('FreshD N4 negative-y extension:8 exact CURRENT-loss exits. Actual',len(seed),'cell570-read UQ control, sourceR130 remainsSAME/CURRENT; C5 ownR12 fails at570.')
