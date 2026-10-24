"""Exact single-head C5 next-FOREIGN original-hook loss frontier for Q."""
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
def center(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def local(g,p):return l.rot(sub(g,p[:2]),(-p[2])%4)
F15={(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1),(-4,1),(-4,2),(-3,2),(-2,1),(-2,-1)}
HK={(-1,-1),(-2,-1),(-3,-1),(-3,-2)};f0=(F15-{(2,0),(2,1)})|HK
rewrite=json.loads((R/'foreign_C5_joint_rewrite_frontier_2026-10-24/C5_joint_rewrite.json').read_text());qb=next(z for z in rewrite['all568_pre_post_joint_loss_rows']if z['source_kind']=='QB')
assert set(map(tuple,qb['pre_field']))==f0
assert qb['gate']==[-4,-3,1]
source=l.trace(W['Q']);assert source['last'][(-2,0)]==('L',48)and source['last'][(-4,-2)]==('L',56)and source['last'][(-3,-2)]==('R',57)
# This precise first repair is now excluded by the separately signed238
# relative two-turn theorem, not by a fixed failed connector family.
fund= rewrite['all288_QB_pre_rewrite_hole_last_R_rows']
h=[z for z in fund if z['hole']==[-4,-2]and z['route']=='possible_funder']
assert len(h)==5 and[(z['producer'],z['ENTRY'])for z in h if z['first_turn']=='R']==[('C',[-6,-2,0])]
assert all(z['first_turn']=='L'and z['heading']==3 for z in h if z['first_turn']!='R')
assert not[z for z in fund if z['hole']==[-2,0]and z['route']=='possible_funder']
# All hook first-L positions, including entry CORE and actual future M.
G={}
for A in'FQB':
 ct=l.trace(W[A]+l.M)
 for q,(c,t)in ct['first'].items():
  if c!='L':continue
  for g in HK:
   p=(*sub(g,l.rot(q,1)),1)
   if(sum(p[:2])+1)%2:continue
   G.setdefault((A,p),[]).append(dict(original_hook=g,local=q,actual_first_L=o.describe(A,t)))
assert len(G)==71
rows=[];remaining=[]
for(A,p),wit in sorted(G.items()):
 ct=l.trace(W[A]+l.M);row=dict(actor=A,ENTRY=p,possible_original_hook_first_L=wit)
 bad=[]
 for g in sorted(f0):
  q=local(g,p);c=ct['first'].get(q)
  if q in l.K or c and c[0]=='R':bad.append(dict(SAME_original=g,local=q,first=c,reason='ENTRY_CORE'if q in l.K else'first_WHITE'))
 if bad:row['conflicts']=bad;route='intact_pre_field'
 elif p[:2]==(-5,-4):
  g=(-2,0);q=local(g,p);assert ct['first'][q]==('L',35)
  row['WHITE_source_hole']=g;row['actual_BLACK_request']=o.describe(A,35);route='SOURCE_L48_no_funder'
 elif p[:2]in[(-6,-5),(-3,-6)]:
  g=(-4,-2);q=local(g,p);tick=17 if p[:2]==(-6,-5)else 51
  assert ct['first'][q]==('L',tick)
  row['WHITE_source_hole']=g;row['actual_BLACK_request']=o.describe(A,tick);route='SOURCE_L56_only_C3_repair_excluded'
 else:
  assert p==(-4,-7,1)
  assert len(wit)==1 and wit[0]['original_hook']==(-3,-2)and ct['first'][(-5,1)]==('L',38)
  assert l.trace(W[A])['last'][(-5,1)]==('L',38)
  ep=after(W[A],p)
  misses=[]
  for g in sorted(f0-{(-3,-2)}):
   assert local(g,p)not in ct['first']and local(g,ep)not in l.K
   misses.append(dict(SAME_original=g,physically_MISS_complete_recipient_context=True,outside_recipient_RAW_EXIT_CORE=True))
  row['all14_untouched_current_old']=misses;route='OPEN_exact_lower_hook_loss_gate';remaining.append((A,p))
 row['route']=route;rows.append(row)
assert Counter(z['route']for z in rows)=={'intact_pre_field':59,'SOURCE_L48_no_funder':3,'SOURCE_L56_only_C3_repair_excluded':6,'OPEN_exact_lower_hook_loss_gate':3}
# Last actual ordinary BASE is plainV/U by signed interval grammar. Keep all
# five actual typed interfaces; no fictitious C-ended fullpacket is inserted.
last=[]
for A,p in remaining:
 for b in'VU':
  tr=l.trace(W[b]+W[A]+l.M);ep=after(W[b],(0,0,1));pre=(*sub(p[:2],ep[:2]),1)
  if not tr['feasible']:
   assert b=='V'and A=='B';last.append(dict(previous=b,actor=A,previous_ENTRY=pre,FOREIGN_ENTRY=p,route='literal_VB_conflict',conflict=tr));continue
  last.append(dict(previous=b,actor=A,previous_ENTRY=pre,FOREIGN_ENTRY=p,route='OPEN_actual_plain_BASE_interface'))
assert sum(z['route'].startswith('OPEN')for z in last)==5
# Exact SOURCE-Q proxy MISS: all candidate FOREIGN pieces lie at doubled x
# <=-9 while SOURCE Q pieces have x>=-7. This is not whole-history simplicity.
oldq=[((-1,-1),(-7,-3)),((-7,-3),(-7,-7))];sep=[]
for A,p in remaining:
 z=center(p);deltas=[(-6,-2)]+([(0,-4)]if A=='Q'else[(2,-6)]if A=='B'else[])
 for j,v in enumerate(deltas):
  d=l.rot(v,p[2]);e=add(z,d)
  for i,(a,b)in enumerate(oldq):
   assert max(z[0],e[0])<min(a[0],b[0])
   sep.append(dict(actor=A,actor_piece=j,actor_segment=(z,e),old_Q_piece=i,old_segment=(a,b),strict_x_separation=True))
  z=e
 assert z==center(after(W[A],p))
assert len(sep)==10
# Prepared recipient-only controls deliberately KEEP the open local gate.
# Initial BLACK tags are not falsely identified with attained Q R births.
controls=[]
for A,p0 in remaining:
 ctx=l.trace(W[A]+l.M);seed={add(p0[:2],l.rot(q,p0[2]))for q,(c,t)in ctx['first'].items()if c=='L'}|f0
 BLACK=set(seed);ids={q:('prepared_initial',q)for q in BLACK};p=p0;reads=[];cuts=[]
 for t,c in enumerate(W[A]+l.M):
  q=p[:2];assert(q in BLACK)==(c=='L');prior=ids.get(q)
  if c=='L':BLACK.remove(q);ids.pop(q)
  else:BLACK.add(q);ids[q]=('new_R',t)
  reads.append(dict(tick0=t,cell=q,turn=c,prior_identity=prior));p=after(c,p)
  if t+1 in[len(W[A]),len(W[A]+l.M)]:cuts.append(dict(actual_read_count=t+1,pose=p,complete_BLACK=sorted(BLACK),all14_other_prepared_tag_identities=[dict(cell=g,identity=ids.get(g),CURRENT=g in BLACK and local(g,p)not in l.K)for g in sorted(f0-{(-3,-2)})]))
 assert reads[38]['cell']==(-3,-2)and reads[38]['turn']=='L'and reads[38]['prior_identity']==('prepared_initial',(-3,-2))
 assert(-3,-2)not in BLACK
 assert all(z['identity']==('prepared_initial',tuple(z['cell']))and z['CURRENT']for c in cuts for z in c['all14_other_prepared_tag_identities'])
 controls.append(dict(scope='PREPARED recipient-only complete board; NO earlier actual Q, ordinary5C connector or U ancestry. InitialBLACK is not claimed to be an attained sourceQ R57 identity.',actor=A,ENTRY=p0,complete_seed=sorted(seed),mass=len(seed),all_actual_reads=reads,all_RAW_and_M_fields=cuts,prepared_lower_tag_death_tick0=38))
D=['foreign_C5_joint_rewrite_frontier_2026-10-24/manifest.json','audits/check_FOREIGN_C5_rewrite_independent.json','ordinary_two_turn_noninterpenetration_2026-10-24/manifest.json','audits/check_two_turn_separation_independent.json','foreign_interval_packet_grammar_2026-10-24/manifest.json','audits/check_foreign_interval_grammar_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Any actual source Q ENTRY0N, ordinary-only section with exactly5 Cs, then a complete next F/Q/B RAW+actualM. If that next FOREIGN physically first-deletes any of the four SAME original source-Q hooks, it MUST be at ENTRY(-4,-7,E) and delete only lower originalR57(-3,-2) at ownL38. No U, earlier simple history, global-first or rail bound. This is an OPEN necessary loss gate, not attained history or no-loss theorem.',post_rewrite_branch='If the E5 ordinary U(-4,-3,E) rewrite happened, source lowerhook is already physically spent and signedff4 all71 post-rewrite recipient rows exclude a physical first deletion of any of the other3 originals. Therefore a NEXTFOREIGN old-hook first deletion must be in the intact pre-rewrite branch below.',pre_rewrite_SOURCE_hole_lift='The signed288 CORE-inclusive last-R inventory makes L48(-2,0) WHITE while the pre-field is intact. Q-only L56 h(-4,-2) can first be repaired only by completed C3(-6,-2,N)R8. Signed238 now excludes that exact completed actual C3 by a relative ordinary two-turn crossing contradiction. The four W funders first need hBLACK and cannot be its first repair. Thus h stays WHITE throughout this intact ordinary section. B is NOT included: its R64 at h remains real.',all71_intact_pre_rewrite_recipient_rows=rows,all6_last_BASE_types=last,all10_exact_SOURCE_Q_proxy_MISS_checks=sep,all3_prepared_recipient_only_positive_controls=controls,OPEN_mechanism='The three fixed recipient actors all physically read source-Q lowerhook at ownL38/read39, source-local recipient(-5,1), and last-read itL38. If attained, the originalR57 dies and its cell is WHITE after RAW; all14 other guaranteed retained IDs are complete-context-MISS and outside actual recipient exitCORE. Thus they remain SAME CURRENT at RAW EXIT and physicallySAME BLACK throughM. The candidate FOREIGN proxy itself MISSES every original Q piece by strict x separation; no GLOBAL first-contact or whole-prefix simplicity follows.',limits=['No actual source-Q to this gate history or fullfield is attained here.','No generic C5 hook transfer: one exact recipient head remains open.','Partial failed FOREIGN may physically delete hooks before later failure; completed word/M distinction retained.','No sourceB lift, furtherFOREIGN iteration, new producer-age law, arbitrary-tail simplicity, ant-language coverage or capture.'],dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest()for p in D})
(H/'Q_C5_frontier.json').write_text(json.dumps(out,indent=2)+'\n')
print('Q C5 nextFOREIGN original-hook loss:71=59+3+6+3. One OPEN head(-4,-7,E), five actual V/U interfaces;10 oldQ/newFOREIGN strict-x MISS checks.')
