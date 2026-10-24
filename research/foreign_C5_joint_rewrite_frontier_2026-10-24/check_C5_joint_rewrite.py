"""One exact E5 cohort rewrite and source-hole reverse precondition."""
from pathlib import Path
from collections import Counter
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
F15={(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1),(-4,1),(-4,2),(-3,2),(-2,1),(-2,-1)}
old13=F15-{(2,0),(2,1)};HK={(-1,-1),(-2,-1),(-3,-1),(-3,-2)}
UCT=l.trace(W['U']+l.M);UR=l.trace(W['U']);UO=set(map(tuple,l.literal_geometry(W['U'])['outputs']))

def conflicts(A,p,field):
 ct=l.trace(W[A]+l.M);out=[]
 for g in sorted(field):
  q=local(g,p);f=ct['first'].get(q)
  if q in l.K or f and f[0]=='R':out.append(dict(original=g,local=q,first=f,reason='ENTRY_CORE'if q in l.K else'first_WHITE'))
 return out

def first_losses(field,exit0=None):
 rows=[]
 for g in sorted(field):
  for A in'DVU':
   ct=l.trace(W[A]+l.M)
   for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
    p=(*sub(g,l.rot(slot,1)),1);row=dict(original=g,consumer=A,ENTRY=p,true_input=slot,actual_L=o.describe(A,ct['first'][slot][1]))
    if(sum(p[:2])+1)%2:route='sector'
    else:
     bad=conflicts(A,p,field);row['field_conflicts']=bad
     if bad:route='held_field'
     elif exit0 and(p[0]<exit0[0]or p[1]>exit0[1]):route='behind_actual_E_exit'
     else:route='possible_first_loss'
    row['route']=route;rows.append(row)
 return rows
cases=[];total=0
for kind,f0,gate in[('F',old13,(-3,-2,1)),('QB',old13|HK,(-4,-3,1))]:
 before=first_losses(f0);kept=[z for z in before if z['route']=='possible_first_loss']
 assert all(z['consumer']=='U'and z['ENTRY']==gate for z in kept)
 spent={g for g in f0 if local(g,gate)in UCT['first']or local(g,gate)in l.K}
 expected={(-2,-1),(-1,-1)}if kind=='F'else{(-3,-2)}
 assert spent==expected=={z['original']for z in kept}
 ep=after(W['U'],gate);survive=f0-spent
 for g in survive:
  assert local(g,gate)not in UR['last']and local(g,ep)not in l.K
 new={add(gate[:2],l.rot(q,1))for q in UO};assert not new&survive
 f1=survive|new;renew=first_losses(f1,ep)
 assert not[z for z in renew if z['route']=='possible_first_loss']
 assert len(f1)==(20 if kind=='F'else 23)
 for g in spent:
  q=local(g,gate);assert UR['first'][q][0]=='L'
  assert UR['first'][q][1]<28 # genuine physical deaths, not only CORE capture
 # Prepared local completed rewrite: no actual source FOREIGN/U ancestry claimed.
 ctx=UCT;seed={add(gate[:2],l.rot(q,1))for q,(c,t)in ctx['first'].items()if c=='L'}|f0
 B=set(seed);ids={g:('prepared_initial',g)for g in B};p=gate;reads=[];cuts=[]
 for t,c in enumerate(W['U']+l.M):
  q=p[:2];assert(q in B)==(c=='L')
  prior=ids.get(q)
  if c=='L':B.remove(q);ids.pop(q)
  else:B.add(q);ids[q]=('new_R',t)
  reads.append(dict(tick0=t,cell=q,turn=c,prior_identity=prior));p=after(c,p)
  if t+1 in[28,39]:cuts.append(dict(actual_read_count=t+1,pose=p,complete_BLACK=sorted(B),surviving_old_ids=[dict(cell=g,identity=ids.get(g),CURRENT=g in B and local(g,p)not in l.K)for g in sorted(survive)],all9_new_ids=[dict(cell=g,identity=ids.get(g),CURRENT=g in B and local(g,p)not in l.K)for g in sorted(new)]))
 assert all(z['CURRENT']for c in cuts for z in c['surviving_old_ids']+c['all9_new_ids'])
 deaths=[dict(original=g,own_physical_L=o.describe('U',UR['first'][local(g,gate)][1]))for g in sorted(spent)]
 newbirths=[dict(cell=g,source_local=local(g,gate),own_final_RAW_R=o.describe('U',UR['last'][local(g,gate)][1]))for g in sorted(new)]
 cases.append(dict(source_kind=kind,pre_field=sorted(f0),gate=gate,actual_U_RAW_EXIT=ep,all_pre_E5_first_loss_rows=before,pre_counts=dict(Counter(z['route']for z in before)),physically_spent_old_identities=deaths,all_untouched_current_old=sorted(survive),all9_genuine_new_R_births=newbirths,post_field=sorted(f1),all_post_E5_first_loss_rows=renew,post_counts=dict(Counter(z['route']for z in renew)),prepared_local_rewrite=dict(scope='Isolated actual U+M in prepared field only; no earlier sourceFOREIGN/U ancestry',ENTRY=gate,complete_seed=sorted(seed),mass=len(seed),all39_reads=reads,actual_cuts=cuts)))
 total+=len(before)+len(renew)
assert total==568
# Selected exact pre-rewrite source holes, including all final-R CORE writes.
funders=[]
for hole in[(-2,0),(-4,-2)]:
 for h in[2,1,0,3]:
  for A in'DCVU':
   ct=l.trace(W[A]+l.M)
   for q,(c,t)in l.trace(W[A])['last'].items():
    if c!='R':continue
    p=(*sub(hole,l.rot(q,h)),h);ep=after(W[A],p);row=dict(hole=hole,heading=h,producer=A,ENTRY=p,RAW_EXIT=ep,final_R=o.describe(A,t),first_turn=ct['first'][q][0],first_read=o.describe(A,ct['first'][q][1]),hole_in_EXIT_CORE=local(hole,ep)in l.K)
    if(sum(p[:2])+h)%2:route='sector'
    else:
     bad=conflicts(A,p,old13|HK);row['pre_rewrite_field_conflicts']=bad;route='held_field'if bad else'possible_funder'
    row['route']=route;funders.append(row)
assert len(funders)==288
assert not[z for z in funders if z['hole']==(-2,0)and z['route']=='possible_funder']
hfund=[z for z in funders if z['hole']==(-4,-2)and z['route']=='possible_funder']
assert len(hfund)==5
assert[(z['producer'],z['ENTRY'])for z in hfund if z['first_turn']=='R']==[('C',(-6,-2,0))]
assert all(z['first_turn']=='L'and z['heading']==3 for z in hfund if z['producer']!='C'or z['heading']!=0)
for A in'QB':
 tr=l.trace(W[A]);assert tr['last'][(-2,0)]==('L',48)
assert l.trace(W['Q'])['last'][(-4,-2)]==('L',56)
assert l.trace(W['B'])['last'][(-4,-2)]==('R',64)
# All physically surviving original hooks after the QB rewrite: no nextFOREIGN
# can first delete one. Pure entry masks suffice, including marker-only loss.
post=cases[1];field=set(map(tuple,post['post_field']));spent={(-3,-2)};ep=tuple(post['actual_U_RAW_EXIT']);goals={}
for A in'FQB':
 ct=l.trace(W[A]+l.M)
 for q,(c,t)in ct['first'].items():
  if c!='L':continue
  for g in HK:
   p=(*sub(g,l.rot(q,1)),1)
   if(sum(p[:2])+1)%2:continue
   goals.setdefault((A,p),[]).append(dict(original=g,local=q,actual_first_L=o.describe(A,t)))
goalrows=[]
for(A,p),wit0 in sorted(goals.items()):
 wit=[z for z in wit0 if z['original']not in spent];row=dict(actor=A,ENTRY=p,candidate_old_first_L=wit)
 if not wit:route='old_candidate_already_physically_spent'
 elif p[0]<ep[0]or p[1]>ep[1]:route='behind_actual_E_rewrite_exit'
 else:
  bad=conflicts(A,p,field);assert bad,(A,p);row['post_field_conflicts']=bad;route='post_field'
 row['route']=route;goalrows.append(row)
assert len(goalrows)==71 and Counter(z['route']for z in goalrows)=={'old_candidate_already_physically_spent':3,'behind_actual_E_rewrite_exit':54,'post_field':14}
D=['foreign_C4_joint_hook_reserve_2026-10-24/manifest.json','audits/check_FOREIGN_C4_joint_reserve_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Any actual sourceF/Q/B ENTRY0N plus ordinary RAW section with exactly5 Cs and actual complete contexts. Guaranteed retained old field at E5 start has at most ONE possible first CURRENT loss: the listed actual U. Its post-field is stable at every remaining completed E5 cut. No source-U ancestry, simple proxy, first-contact or rail-length bound. These gates are necessary interfaces, not attained sourceFOREIGN histories.',all568_pre_post_joint_loss_rows=cases,all288_QB_pre_rewrite_hole_last_R_rows=funders,pre_rewrite_hole_conclusions=['While the initial old13+hook field is intact, sourceQ/B L48 hole(-2,0) has no compatible completed final-R origin in any ordinary heading and remains physically WHITE at completed cuts.','SourceQ ONLY L56 hole h=(-4,-2), while that field is intact, can first become BLACK only at the actual C3 atom ENTRY(-6,-2,N), own commonR8, RAWEXIT(-6,-1,W). Four W final-R9 funders first require h BLACK at L5 and cannot be its first repair. All CORE writes are included. This is a necessary actual precondition, not a history or a prohibition of that C3.'],all71_post_rewrite_next_FOREIGN_old_hook_first_L_rows=goalrows,post_rewrite_foreign_conclusion='If the Q/B E5 rewrite actually occurs, the lower original hook is physically spent at ownU L14; all three other original hooks remain CURRENT with the renewed field through the ordinary E tail. No complete nextFOREIGN+M can physically first-delete one of those remaining SAME originals, by the exact71 outgoing first-L pose inventory. A partial attempted FOREIGN can still delete an original before another requirement fails. For sourceF the rewrite physically spends both protected originals, so no old protected original remains for a later first deletion.',limits=['The Q-only L56-hole conclusion does NOT apply to sourceB: B actually writes that coordinate at R64.','No actual sourceFOREIGN-to-rewrite realization is claimed; both isolated local controls are prepared only.','No C5 full four-hook transfer: the lower Q/B original may die at the ordinary U rewrite.','The C3 h-funder remains unresolved and all earlier-history/core obligations remain explicit.','No full-state quotient, C6/furtherFOREIGN induction, arbitrary-tail simplicity, language coverage or capture.'],dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest()for p in D})
(H/'C5_joint_rewrite.json').write_text(json.dumps(out,indent=2)+'\n')
print('568 E5 joint-loss rows; one genuine U rewrite with stable post-field; 288 hole final-R rows; 71 post-rewrite recipient poses closed. No source-history attainment.')
