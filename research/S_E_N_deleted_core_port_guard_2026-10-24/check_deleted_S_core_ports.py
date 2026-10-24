"""Unbounded S/E/N two-C deleted-port restoration obstruction.
Physical WHITE before N is distinguished from N external-input unavailability.
"""
from pathlib import Path
import json,hashlib,importlib.util
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
slots=[(-1,0),(-1,-1),(0,-1)]
deletions=[]
for A in'DVU':
 tr=l.trace(W[A]);ep=after(W[A]);assert ep[1]>=1
 for q in slots:
  assert tr['first'][q]==tr['last'][q]==('L',{(-1,0):1,(-1,-1):2,(0,-1):3}[q])
  g=l.rot(q,2);assert g[1]>=0
  deletions.append(dict(deleting_S_atom=A,ENTRY=(0,0,2),deleted_hole_relative_to_ENTRY=g,source_local=q,actual_last_L=o.describe(A,tr['last'][q][1]),S_RAW_EXIT=after(W[A],(0,0,2))))
# Every physical R, not merely residual O: includes all EXIT CORE funding.
Rroles=[]
for A in'DCVU':
 p=(0,0,0);ep=after(W[A])
 for t,c in enumerate(W[A]):
  if c=='R':
   q=p[:2];assert q[1]>=0 and q[0]>=-1
   if A=='C':assert q[0]>=0
   Rroles.append(dict(atom=A,own_tick0=t,local_R=q,S_R_y_minus_ENTRY_y=-q[1],E_R_y_minus_ENTRY_y=-q[0]))
  p=after(c,p)
assert len(Rroles)==41
# The entire no-C N epoch's genuine residual I/O interface. A previously
# CORE-only BLACK cell can first emerge externally only through O; all O
# are actual final RAW R births, never a carried untracked CORE identity.
ledger=[]
for A in'DVU':
 geo=l.literal_geometry(W[A]);ep=after(W[A]);raw=l.trace(W[A]);ctx=l.trace(W[A]+l.M)
 inputs=[];outputs=[];entry_core=[]
 for q in map(tuple,geo['inputs']):
  assert q[1]>=1
  inputs.append(dict(local=q,y=q[1],actual_first_L=o.describe(A,ctx['first'][q][1]),marker_owned=q not in raw['first']))
 for q in map(tuple,geo['outputs']):
  assert q[1]<=ep[1]and raw['last'][q][0]=='R'
  outputs.append(dict(local=q,y=q[1],actual_final_RAW_R=o.describe(A,raw['last'][q][1])))
 for q in sorted(l.K):
  assert q in raw['last']
  exitcore=l.rot(sub(q,ep[:2]),(-ep[2])%4)in l.K
  if not exitcore and raw['last'][q][0]=='R':assert list(q)in geo['outputs']
  entry_core.append(dict(entry_CORE=q,actual_last_RAW=raw['last'][q],in_RAW_EXIT_CORE=exitcore,export_if_BLACK_requires_actual_final_R=(not exitcore and raw['last'][q][0]=='R')))
 ledger.append(dict(atom=A,N_RAW_EXIT=ep,all_true_external_inputs=inputs,all_external_O_final_R_births=outputs,all5_entry_CORE_export_checks=entry_core))
assert sum(len(z['all_true_external_inputs'])for z in ledger)==8
assert sum(len(z['all_external_O_final_R_births'])for z in ledger)==16
# Whole-field actual U-entry regression. It reaches the required S deleting
# V and N reader ENTRY with real M11; requested reader U fails at external q.
labels='UQDDDDVCDCV';candidate=labels+'UUC';desired=''.join(W[A]for A in candidate)+l.M
bad=l.trace(desired);assert not bad['feasible']and bad['conflict_read']==221 and bad['previous_read']==133 and tuple(bad['cell'])==(-7,-4)and bad['turn']=='L'
raw=''.join(W[A]for A in labels);assert len(raw)==208
actual=raw+W['U'][:13];tr=l.trace(actual);assert tr['feasible']and len(actual)==221
seed={q for q,(c,t)in tr['first'].items()if c=='L'};B=set(seed);ids={q:('initial_BLACK',q)for q in B};p=(0,0,0);reads=[];cuts=[];boundaries={};off=0
for index,A in enumerate(labels):
 boundaries[off+len(W[A])]=(index,A);off+=len(W[A])
for t,c in enumerate(actual):
 q=p[:2];assert(q in B)==(c=='L')
 prior=ids.get(q)
 if c=='L':B.remove(q);ids.pop(q)
 else:B.add(q);ids[q]=('new_R',t)
 reads.append(dict(tick0=t,cell=q,turn=c,prior_identity=prior));p=after(c,p)
 if t+1 in boundaries or t+1 in[219,221]:
  cuts.append(dict(actual_read_count=t+1,boundary=boundaries.get(t+1),pose=p,complete_BLACK=sorted(B),hole_BLACK=(-7,-4)in B,hole_identity=ids.get((-7,-4))))
assert all(not z['hole_BLACK']for z in cuts if z['actual_read_count']>=150)
assert p[:2]==(-7,-4)and p[2]==3 and p[:2]not in B # actual next turn is R, not the requested L
assert after(raw)==(-6,-6,0)and local((-7,-4),after(raw))==(-1,2)
source_v=next(z for z in cuts if z['boundary']and z['boundary']==(6,'V'))
assert source_v['actual_read_count']==150
reader=o.describe('U',13);source_owner=o.describe('V',1)
reg=dict(scope='Genuine complete finite U-entry seed and actual prefix. Last marked V has actual U[:11]=M11 supplied; extra U ticks11/12 also execute. The requested U tick13 fails, so no completed reader U or C3 restoration is claimed.',candidate_labels=candidate,actual_prefix_labels=labels,actual_partial_U_read_count=13,complete_seed=sorted(seed),mass=len(seed),all221_actual_reads=reads,all_completed_RAW_and_partial_cuts=cuts,source_death=dict(actual_GLOBAL_tick0=133,source_V_own=source_owner,world_cell=(-7,-4)),requested_reader=dict(ENTRY=after(raw),true_external_q=(-1,2),world_cell=(-7,-4),actual_owner=reader,failed_GLOBAL_tick0=221,real_next_turn='R'))
D=['word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Any actual S-facing D/V/U RAW, then an arbitrary ordinary S rail, C1, arbitrary E rail, C2, arbitrary N rail, with actual complete RAW+M contexts and no intervening FOREIGN or extra C. Each of that S source RAWs actual L1/L2/L3 entry-core holes cannot supply any later N TRUE EXTERNAL BLACK input. No simplicity, initial-U ancestry, total rail-length bound, CURRENT-age theorem or field quotient. A real U-entry selected-source control is included separately.',all9_actual_source_deletions=deletions,all41_CORE_inclusive_physical_R_supports=Rroles,all3_N_RAW_external_export_ledgers=ledger,
 proof=['Let Y be the S deleting atom ENTRYy. Its three holes have global y>=Y and last reads L1/L2/L3, with no later R in that source RAW. Its RAW EXITy<=Y-1. Every remaining S RAW R has globaly<=its ENTRYy<=Y-1. The actual C1 likewise writes at/below its S ENTRYy, and exits E at y<=Y-2.',
 'Every E rail RAW physical R has globaly<=ENTRYy+1<=Y-1, since all local physicalRx>=-1. E motion cannot raise y. The actual C2 has localRx>=0 on every R, so also misses the holes. Thus each hole is physically WHITE at N-stage ENTRY. This includes all CORE R writes and all arbitrary finite S/E word orders.',
 'On any zero-C N rail, every genuine new external O lies at/below its producer RAW EXITy; all true external inputs, including marker-only captures, lie strictly above their consumer ENTRYy. N heads never decrease y. Any previously WHITE hole that later becomes external BLACK must first be a genuine O final-R export at a completed cut. Even a CORE-to-external export is such an actual new final-R O event, not an inherited identity exception. Its y<=producerEXITy<=readerENTRYy is incompatible with any true external input requiring y>=readerENTRYy+1. Rebirths or repeated CORE writes do not change this argument.',
 'Therefore these deleted S ports are unavailable as N external BLACK inputs. Do NOT strengthen this to physical WHITE permanence throughout N: temporary CORE R births remain possible. Do NOT apply it to an N ENTRY CORE obligation, an additional C, a foreign, or an incomplete terminal marker.'],selected_reachable_source_and_failed_reader_control=reg,limits=['The exact Q C3(-6,-2,N) funding target remains open: this guards histories whose actual N external input matches one of these genuinely S-deleted ports, not all possible histories.','No every-S/N-rail obstruction or completeness of a deleted-port matching relation.','No physical WHITE promise during N, no CORE-input prohibition, no simplicity/capture/language-coverage conclusion.'],dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest()for p in D})
(H/'deleted_S_core_ports.json').write_text(json.dumps(out,indent=2)+'\n')
print('9 real S-core deletions;41 physical-R supports;8 N inputs/16 newO/15 CORE export checks. Genuine',len(seed),'cell221-read source/reader control, desired U q fails at221.')
