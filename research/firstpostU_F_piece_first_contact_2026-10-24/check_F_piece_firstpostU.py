"""F proper-piece GLOBAL-first contact closure with immediate post-F U.
The F reserve is rebuilt with fresh U LEFT, not lifted from the V title.
"""
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
 return*q,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
# Reuse the unchanged signed exact rational hit primitive only, not a V
# state theorem. No old frozen checker is run or rewritten.
P=R/'firstpostV_F_piece_first_contact_2026-10-24/check_F_piece_contact.py';ns={};exec(P.read_text().split('Ssets=')[0],ns);hit=ns['hit']
LEFT={(0,0),(0,1)};tags={(-3,-1),(-2,-1)};FORE=((-7,-3),(-1,-1));source=chord('U',(0,0,0));fr=l.trace(W['F']);fe=after(W['F']);fO=set(map(tuple,l.literal_geometry(W['F'])['outputs']));births=[]
for g in sorted(tags):
 q=add(fe[:2],l.rot(g,fe[2]));assert q in fO and fr['last'][q][0]=='R';births.append(dict(postF_cell=g,F_entry_cell=q,F_last_R_tick0=fr['last'][q][1]))
assert sorted(q['F_last_R_tick0']for q in births)==[46,47]
# Actual immediate-U context preserves the SAME F tags, physically and as
# external current residuals at its RAW EXIT. No hypothetical future marker.
ut=l.trace(W['U']+l.M);ue=after(W['U']);uK={add(ue[:2],q)for q in l.K}
assert tags.isdisjoint(ut['first'])and tags.isdisjoint(uK)
roles=[]
for g in sorted(tags):
 for a in'DCVU':
  geo=l.literal_geometry(W[a]);t=l.trace(W[a]+l.M)
  for slot in map(tuple,geo['inputs']):
   for hd in range(4):
    p=(*sub(g,l.rot(slot,hd)),hd);row=dict(F_original=g,consumer=a,input_slot=slot,entry=p,physical_first_L=o.describe(a,t['first'][slot][1]))
    if(sum(p[:2])+hd)%2:why='sector'
    else:
     bad=[]
     for held in sorted(LEFT|tags):
      q=l.rot(sub(held,p[:2]),-hd);f=t['first'].get(q)
      if q in l.K or f and f[0]=='R':bad.append(dict(SAME_held=held,local=q,role='ENTRY_CORE'if q in l.K else'first_WHITE',actual_first=f))
     if bad:why='held_LEFT_or_F_pair_CORE_WHITE';row['conflicts']=bad
     else:
      c=hit(*FORE,*chord(a,p));assert c is not None;assert p!=(0,0,0);why='earlier_actual_F_proxy_contact';row['contact']=list(map(str,c))
    row['classification']=why;roles.append(row)
assert len(roles)==64 and Counter(q['classification']for q in roles)=={'sector':32,'held_LEFT_or_F_pair_CORE_WHITE':26,'earlier_actual_F_proxy_contact':6}
# Reconstruct the same62 affine F contact heads and the purely coordinate
# lower-output proof. Execute only the geometry prefix, BEFORE old result
# construction/file output; it has no source-V input except a route LABEL
# for its terminal2, which is replaced explicitly below.
gn={};exec(P.read_text().split('result=dict')[0],gn)
assert gn['total']==62 and dict(gn['cols'])=={'CORE':27,'WHITE':28,'compatible':7}
proper=gn['proper'];terminal=gn['terminal'];assert len(proper)==5 and len(terminal)==2
for q in terminal:
 q['actual_outgoing_owner']='firstpostU_at_FOREIGN_EXIT_not_incomingF';q['route']='signed_actual_U_base_cut_G8_bridge_8a311a4c'
for q in proper:assert q['exact_ordinary_C_clock']in(2,3)and q['initial_SAME_FOREIGN_output_reserve']['postforeign_cell'][1]<=-1
assert len(gn['ports'])==8
# Genuine initial-U/F/new-U plus two real own Cs regression. All four
# protected identities are traced at actual RAW cuts, not inferred by mass.
word='UFUCC';raw=''.join(W[a]for a in word);tt=l.trace(raw+l.M);assert tt['feasible'];seed={q for q,(c,k)in tt['first'].items()if c=='L'};B={q:('initial',q)for q in seed};p=(0,0,0);tick=0;current={};cuts=[]
for i,a in enumerate(word):
 if i==1:
  fp=p;fstart=tick;fexit=after(W['F'],p)
  current.update({add(fexit[:2],l.rot(q,fexit[2])):tick+fr['last'][add(fe[:2],l.rot(q,fe[2]))][1]for q in tags})
 if i==2:
  up=p;ustart=tick;ut0=l.trace(W['U']);current.update({add(p[:2],l.rot(q,p[2])):tick+ut0['last'][q][1]for q in LEFT})
 for c in W[a]:
  cell=p[:2];assert(cell in B)==(c=='L')
  if c=='L':del B[cell]
  else:B[cell]=tick
  p=after(c,p);tick+=1
 if i>=2:
  core={add(p[:2],l.rot(q,p[2]))for q in l.K};assert all(B.get(q)==birth and q not in core for q,birth in current.items());cuts.append(dict(after_atom_index0=i,atom=a,RAW_cut_tick0=tick,actual_head=p,SAME_current_ids=[dict(cell=q,birth_tick0=birth)for q,birth in sorted(current.items())]))
for c in l.M:
 cell=p[:2];assert(cell in B)==(c=='L')
 if c=='L':del B[cell]
 else:B[cell]=tick
 p=after(c,p);tick+=1
D=[P,R/'firstpostV_F_piece_first_contact_2026-10-24/manifest.json',R/'audits/check_F_piece_firstpostV_independent.json',R/'fresh_RAW_U_LEFT_all_length_2026-10-24/manifest.json',R/'audits/check_fresh_U_LEFT_all_length_independent.json',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/manifest.json',R/'audits/check_RAW_G8_base_cut_bridge_independent.json',R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual U-entry complete-eight prefix then FIRST F, immediate ordinary RAW U, then any finite ordinary RAW D/C/V/U suffix with actual terminal M11. A GLOBAL first new proxy contact cannot have outgoing source in the original F piece. No fixed ordinary length, no later foreign. Initial history retained to match signed C-window interface; fresh-U reserve itself needs no old-eight age transfer.',firstpostU_same_LEFT_current_source='signed fresh aa6a04d0 at simple completed cuts/global-first ENTRY, no foreign after source U',genuine_F_pair_births=births,actual_immediate_U_complete_context_MISS_F_pair=True,all64_F_pair_FIRST_CURRENT_loss_roles=roles,exact_reserve_counts=dict(Counter(q['classification']for q in roles)),coupled_induction='Choose first loss of either F46/F47 AFTER actual immediate U. Before it both are CURRENT, and fresh U LEFT remains CURRENT at its entry because it precedes GLOBAL first contact.32 sector+26 actual field cuts leave6 earlier F contacts. Thus no pair loss precedes GLOBAL first contact, so both SAME F tags are CURRENT at candidate ENTRY. TRUE simultaneous F inputs during candidate remain legal.',all62_F_closed_contact_heads=62,exact_current_field_context_counts=dict(gn['cols']),all5_proper_F_source_coordinate_guards=proper,all2_FOREIGN_EXIT_contacts_outgoing_b1U=terminal,all8_actual_input_RAW_exit_bounds=gn['ports'],source_V_premise_NOT_used='The old geometry prefix is regenerated only because its four held physical coordinates are IDENTICAL. Fresh U LEFT and the newly checked64 F roles replace both V state premises. The terminal route is replaced by signed8a311 source-U base-cut G8 simplicity. No V r/A theorem, V-hole reserve or nonterminal V title is imported.',positive_regression=dict(word=word,complete_seed=sorted(seed),all_physical_reads=tick,F_start_tick0=fstart,new_U_start_tick0=ustart,new_U_entry=up,actual_current_cut_states=cuts),not_claimed=['No F firstpostD/C closure.','No contact exclusion for earlier sources before F or later ordinary sources.','No pair persistence through a candidate contact.','No arbitrary-tail simplicity, second foreign, coverage or capture.'],dependencies={str(q.relative_to(R)):hashlib.sha256(q.read_bytes()).hexdigest()for q in D})
(H/'F_piece_firstpostU.json').write_text(json.dumps(out,indent=2)+'\n');print('FirstpostU F reserve:64=32sector+26heldfield+6earlierF contacts; identical62 geometry=55 current cuts+2 outgoingU+5 coordinate exclusions. Genuine UFUCC replayed.')
