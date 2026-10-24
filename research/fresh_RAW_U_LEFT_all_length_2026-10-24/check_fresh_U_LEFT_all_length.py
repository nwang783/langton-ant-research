"""Zero-foreign fresh RAW U SAME-LEFT contact-or-persistence interface.
All-length conditional proof; no old-eight source lifetime is imported.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
def meet(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);de=det(u,v)
 if de:
  s,t=Q(det(q,v),de),Q(det(q,u),de)
  return dict(old_s=str(s),new_t=str(t),point=[str(Q(a[k])+s*u[k])for k in(0,1)])if 0<=s<=1 and 0<=t<=1 else None
 if det(q,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
 return dict(collinear_old_interval=[str(max(Q(0),lo)),str(min(Q(1),hi))])if max(0,lo)<=min(1,hi)else None
LEFT={(0,0),(0,1)};a=(1,0);source=l.trace(W['U']);sourceO=set(map(tuple,l.literal_geometry(W['U'])['outputs']));assert LEFT|{a}<=sourceO
assert source['last'][(0,0)]==('R',4)and source['last'][(0,1)]==('R',19)and source['last'][a]==('R',9)
old=chord('U',(0,0,0));assert old==((-1,-1),(-1,7))
# Rebuild the exact 64 input-role table, including marker-only inputs whose
# first CURRENT loss is previous RAW EXIT CORE capture.
loss=[]
for tag in sorted(LEFT):
 for atom in'DCVU':
  cg=l.literal_geometry(W[atom]);tr=l.trace(W[atom]+l.M)
  for slot in map(tuple,cg['inputs']):
   for hd in range(4):
    p=(*sub(tag,l.rot(slot,hd)),hd);q=dict(tag=tag,atom=atom,slot=slot,entry=p,physical_first_L_owner=o.describe(atom,tr['first'][slot][1]))
    if(sum(p[:2])+hd)%2:why='sector'
    else:
     bad=[]
     for held in sorted(LEFT):
      loc=l.rot(sub(held,p[:2]),-hd);f=tr['first'].get(loc)
      if loc in l.K or f and f[0]=='R':bad.append(dict(held=held,local=loc,requirement='ENTRY_CORE'if loc in l.K else'WHITE',first=f))
     if bad:why='held_LEFT_CORE_or_WHITE';q['conflicts']=bad
     elif meet(*old,*chord(atom,p))is not None:why='nonadjacent_source_U_contact';q['contact']=meet(*old,*chord(atom,p))
     else:why='sole_N_U_gate'
    q['classification']=why;loss.append(q)
assert len(loss)==64 and Counter(q['classification']for q in loss)=={'sector':32,'held_LEFT_CORE_or_WHITE':18,'nonadjacent_source_U_contact':12,'sole_N_U_gate':2}
keep=[q for q in loss if q['classification']=='sole_N_U_gate'];assert all(q['atom']=='U'and tuple(q['entry'])==(1,-1,0)for q in keep)
target=(1,-1,0);tt=l.trace(W['U']+l.M);local_a=l.rot(sub(a,target[:2]),-target[2]);assert local_a==(0,1)and tt['first'][local_a]==('R',11)
# Earlier original-right-a CURRENT loss while LEFT is held. Both LEFT tags
# must MISS its complete context, not merely its physical RAW.
right=[]
for atom in'DCVU':
 cg=l.literal_geometry(W[atom]);tr=l.trace(W[atom]+l.M)
 for slot in map(tuple,cg['inputs']):
  for hd in range(4):
   p=(*sub(a,l.rot(slot,hd)),hd);q=dict(tag=a,atom=atom,slot=slot,entry=p,exit=after(W[atom],p),physical_first_L_owner=o.describe(atom,tr['first'][slot][1]))
   if(sum(p[:2])+hd)%2:why='sector'
   elif any(l.rot(sub(held,p[:2]),-hd)in l.K for held in LEFT|{a}):why='held_CURRENT_in_ENTRY_CORE'
   elif any(l.rot(sub(held,p[:2]),-hd)in tr['first']for held in LEFT):why='not_complete_context_MISS_LEFT'
   elif meet(*old,*chord(atom,p))is not None:why='nonadjacent_source_U_contact'
   else:why='right_N_gate'
   q['classification']=why;right.append(q)
ports=[q for q in right if q['classification']=='right_N_gate'];assert len(right)==32 and len(ports)==4
assert sorted((q['atom'],tuple(q['entry']),tuple(q['exit']))for q in ports)==[('D',(1,-1,0),(2,0,0)),('U',(2,-4,0),(2,0,0)),('U',(2,-2,0),(2,2,0)),('V',(1,-3,0),(2,0,0))]
# The genuine physical w edge closes the simple source-to-first-loss subarc.
B=(-1,3);E=(1,1);edge=(B,E);gate=chord('U',target);assert gate==((1,-3),(1,5))
assert meet(B,old[1],*edge)['point']==['-1','3'];assert meet(gate[0],E,*edge)['point']==['1','1']
fine=[]
for label,word,p,t in [('source_after_w_last_R',W['U'],(0,0,0),20),('consumer_before_w_L13',W['U'],target,13)]:
 q=after(word[:t],p);fine.append(dict(label=label,reads_already_executed=t,head=q,corrected_center=z(q)))
assert tuple(fine[0]['corrected_center'])==B and tuple(fine[1]['corrected_center'])==E
assert source['last'][(0,1)]==('R',19)
# This is algebra, not a sampled clock bound: K*pi/2=+/-2pi gives K=+/-4.
assert 4>=0 and -4<0
zero=[]
for atom in'DVU':
 q=after(W[atom]);assert q[2]==0 and q[0]>=0 and q[1]>=1;zero.append(dict(atom=atom,N_increment=q))
assert l.literal_geometry(W['C'])['inputs']==[]
bar=json.loads((R/'postforeign_V_rA_nonterminal_guardian_2026-10-24/rA_guardian.json').read_text())['fresh_plain_RAW_current_edge_barrier'];assert len(bar)==4
D=[R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'fresh_RAW_V_U_early_donor_guards_2026-10-24/manifest.json',R/'audits/check_fresh_RAW_donors_independent.json',R/'postforeign_V_rA_nonterminal_guardian_2026-10-24/manifest.json',R/'audits/check_postforeign_V_pair_guardian_independent.json',R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Any genuinely fresh RAW U, then only actual ordinary RAW D/C/V/U atoms with actual next-word M11 contexts and no later foreign. Earlier foreign or other history before this U is allowed. If the source-relative expanded proxy remains SIMPLE through a completed ordinary cut, SAME original LEFT is CURRENT there. In particular LEFT is CURRENT at ENTRY of a GLOBAL first-contact atom. No persistence through contact or global simplicity is claimed.',current='SAME source-R BLACK identity outside actual marked-cut CORE. Alive CORE is a CURRENT loss, not physical death. All true inputs include actual next-word marker ownership.',source_births=[dict(cell=q,last_R_tick0=source['last'][q][1])for q in sorted(LEFT|{a})],all64_LEFT_first_loss_roles=loss,LEFT_counts=dict(Counter(q['classification']for q in loss)),sole_LEFT_loss_gate=dict(atom='U',entry=target,WHITE_original_a=dict(cell=a,local=local_a,owner=o.describe('U',11))),all32_prior_a_loss_roles=right,a_counts=dict(Counter(q['classification']for q in right)),four_prior_a_N_loss_ports=ports,physical_bridge=dict(w=(0,1),source_chord=old,consumer_chord=gate,edge=edge,fine_endpoints=fine,ordinary_open_turn='K*pi/2; no foreign lies after this fresh U',closing_joins_pi_over_4=[1,-1],Jordan_equation='K=+4 or -4; K>=0 forces K4',earlier_a_loss_clock='Its N heading gives m=0 modulo4 with 0<=m<=4. At m0 all negative-y heads are unreachable from actual U RAW EXIT(0,4,N); hence m4.',final_endpoint='No C remains. Every possible prior-a consumer exits at N head x2,y0 or2. A subsequent N zero-C run cannot reach LEFT-loss U head(1,-1,N).'),all_N_zero_C_increments=zero,RAW_barrier=bar,completion_qualification='The gate is a plain actual RAW U. Own source or consumer C tails are actual later C atoms in K, never pre-executed. For a marker-only a-loss, CURRENT capture is at that preceding RAW EXIT; its next actual read2 is ordered before the later LEFT-loss gate. No hypothetical future M or internal full-eight producer is introduced.',not_claimed=['No LEFT survival through the global first-contact atom.','No unconditional all-tail simplicity.','No foreign after the fresh U source.','No automatic exclusion of source-U entry/foreign-terminal contacts whose actor takes LEFT as TRUE inputs.','No old-eight source age law is used after foreign.'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
# A complete genuine U-entry control with an earlier foreign and a NEW U
# source after it. This is a regression only, not an all-length proof sample.
control_word='UQUCCV';control_raw=''.join(W[b]for b in control_word);ct=l.trace(control_raw+l.M);assert ct['feasible']
seed={q for q,(c,t)in ct['first'].items()if c=='L'};board={q:('initial',q)for q in seed};p=(0,0,0);tick=0;records=[];source_start=None;tags={}
for idx,atom in enumerate(control_word):
 if idx==2:
  assert atom=='U';source_start=tick;source_pose=p;tags={add(p[:2],l.rot(q,p[2])):tick+source['last'][q][1]for q in LEFT}
 for c in W[atom]:
  cell=p[:2];assert(cell in board)==(c=='L')
  if c=='L':del board[cell]
  else:board[cell]=tick
  p=after(c,p);tick+=1
 if idx>=2:
  core={add(p[:2],l.rot(q,p[2]))for q in l.K};assert all(board.get(q)==birth and q not in core for q,birth in tags.items());records.append(dict(after_atom_index0=idx,atom=atom,actual_RAW_cut_tick0=tick,head=p,SAME_LEFT_CURRENT=[dict(cell=q,birth_tick0=birth)for q,birth in sorted(tags.items())]))
for c in l.M:
 cell=p[:2];assert(cell in board)==(c=='L')
 if c=='L':del board[cell]
 else:board[cell]=tick
 p=after(c,p);tick+=1
out['positive_regression']=dict(word=control_word,source_atom_index0=2,source_start_tick0=source_start,source_entry=source_pose,complete_seed=sorted(seed),all_physical_reads=tick,source_and_later_RAW_cut_states=records,scope='A genuine complete finite U-entry word with Q BEFORE the NEW selected RAW U; its own two Cs are real later RAW atoms. This regression does not replace the arbitrary-length proof.')
(H/'fresh_U_LEFT_all_length.json').write_text(json.dumps(out,indent=2)+'\n')
print('Fresh U LEFT all-length:64 roles leave U1,-1N; held-w zero-foreign Jordan K4; prior a loss has m0/4, N endpoints exclude both. Conditional current-at-entry, not through-contact.')
