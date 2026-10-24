"""Exact five-C negative-x next-FOREIGN hole frontier.
No rail-length, ancestry, proxy simplicity or physical WHITE persistence at W cuts.
"""
from pathlib import Path
import importlib.util,json,hashlib
from collections import Counter
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',ROOT/'word_stabilization/check_foreign_return_interfaces.py')
o=load('owner',ROOT/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return (*q,h)
def local(g,p):return l.rot(sub(g,p[:2]),(-p[2])%4)
F15={(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1),(-4,1),(-4,2),(-3,2),(-2,1),(-2,-1)}
old13=F15-{(2,0),(2,1)};a=(-3,3);r=(-4,3);target=(-5,-2,1)
assert len(old13)==13 and max(q[1]for q in old13)==2
source=[]
for A in'FQB':
 tr=l.trace(W[A]);assert tr['last'][a]==('L',34)and tr['last'][r]==('L',35)
 ep=after(W[A]);assert ep[2]==2 and ep[1]<=-2
 source.append(dict(source=A,actual_RAW_EXIT=ep,a_last_read=o.describe(A,34),r_last_read=o.describe(A,35),initial_a_r_WHITE=True))
# ALL final physical R writes, including every write into EXIT CORE.
# N2 includes C3, W3 includes C4, and S4 includes C5.
rows=[];groups={}
for hole in[a,r]:
 for h in[0,3,2]:
  group=[]
  for atom in'DCVU':
   tr=l.trace(W[atom]);ct=l.trace(W[atom]+l.M)
   for slot,(turn,tick)in sorted(tr['last'].items()):
    if turn!='R':continue
    p=(*sub(hole,l.rot(slot,h)),h);ep=after(W[atom],p)
    row=dict(hole=hole,epoch_heading=h,producer=atom,ENTRY=p,RAW_EXIT=ep,final_R_slot=slot,own_final_R=o.describe(atom,tick),own_first_requirement=o.describe(atom,ct['first'][slot][1]),first_turn=ct['first'][slot][0],hole_in_EXIT_CORE=local(hole,ep)in l.K)
    if(sum(p[:2])+h)%2:route='sector'
    else:
     bad=[]
     for g in sorted(old13):
      q=local(g,p);f=ct['first'].get(q)
      if q in l.K or f and f[0]=='R':bad.append(dict(SAME_current_original=g,local=q,first=f,reason='ENTRY_CORE'if q in l.K else'first_WHITE'))
     row['current_conflicts']=bad;route='held_old13'if bad else'possible_funder'
    row['route']=route;group.append(row);rows.append(row)
  groups[(hole,h)]=group
  assert len(group)==36
  expected={(a,0):dict(sector=18,held_old13=14,possible_funder=4),(r,0):dict(sector=18,held_old13=14,possible_funder=4),(a,3):dict(sector=18,held_old13=15,possible_funder=3),(r,3):dict(sector=18,held_old13=16,possible_funder=2),(a,2):dict(sector=18,held_old13=18),(r,2):dict(sector=18,held_old13=17,possible_funder=1)}[(hole,h)]
  assert dict(Counter(q['route']for q in group))==expected
kept=lambda g,h:[z for z in groups[(g,h)]if z['route']=='possible_funder']
# Both N2/C3 holes: every possible funding RAW first needs r BLACK at L5.
for g in[a,r]:
 for z in kept(g,0):
  assert z['ENTRY']==(-5,3,0)
  assert l.trace(W[z['producer']]+l.M)['first'][local(r,z['ENTRY'])]==('L',5)
# Real W repairs are deliberately retained, not called impossible.
for z in kept(r,3):
 assert z['RAW_EXIT']==(-5,4,3)and local(r,z['RAW_EXIT'])==(-1,-1)
 assert z['ENTRY'][0]>-5
for atom in'DCVU':
 tr=l.trace(W[atom]);assert tr['first'][(-1,-1)]==tr['last'][(-1,-1)]==('L',2)
for z in kept(a,3):assert z['RAW_EXIT'][0]<=-5
S=kept(r,2);assert len(S)==1
s=S[0];assert s['producer']=='U'and s['ENTRY']==(-4,4,2)and s['RAW_EXIT']==(-4,0,2)
assert l.trace(W['U']+l.M)['first'][local(a,s['ENTRY'])]==('L',14)
assert kept(a,2)==[]
# CURRENT old13 at every S4 hole funder ENTRY, not throughout arbitrary S4.
# Any earlier first CURRENT loss exits at/below the tag's y<=2; S cannot
# climb back to a physical R producer head y>=3. Marker capture is included.
first_loss_exits=[]
for atom in'DVU':
 ep=after(W[atom]);ct=l.trace(W[atom]+l.M)
 for slot in map(tuple,l.literal_geometry(W[atom])['inputs']):
  assert slot[1]<=ep[1]
  first_loss_exits.append(dict(atom=atom,true_input=slot,own_L=o.describe(atom,ct['first'][slot][1]),S_RAW_EXIT_y_minus_old_tag_y=slot[1]-ep[1]))
assert len(first_loss_exits)==8 and l.literal_geometry(W['C'])['inputs']==[]
R_support=[]
for atom in'DCVU':
 ep=after(W[atom]);p=(0,0,0)
 for t,c in enumerate(W[atom]):
  if c=='R':
   q=p[:2];assert q[1]>=0 and q[0]>=-1
   if atom=='C':assert q[0]>=0
   else:assert q[1]<=ep[1]
   R_support.append(dict(atom=atom,own_tick0=t,local_R=q,N_RAW_EXIT=ep))
  p=after(c,p)
# The target's first requirement of r is in its own RAW, not supplied M.
recipients=[]
for A in'FQB':
 q=local(r,target);ct=l.trace(W[A]+l.M)
 assert q==(-5,1)and q not in l.K and ct['first'][q]==('L',38)
 recipients.append(dict(actor=A,ENTRY=target,r_local=q,first_requires_BLACK=o.describe(A,38),hook_first_requirements=[dict(cell=g,local=local(g,target),first=ct['first'].get(local(g,target)))for g in[(-3,-2),(-3,-1),(-1,-1),(-2,-1)]]))
# A finite PREPARED local regression preserving old13 but having no asserted
# earlier FOREIGN. It demonstrates the real W CORE repair and its next RAW L2.
regword='VC';regp=(-2,3,3);raw=''.join(W[x]for x in regword);ct=l.trace(raw+l.M);assert ct['feasible']
seed={add(regp[:2],l.rot(q,regp[2]))for q,(c,t)in ct['first'].items()if c=='L'}|old13
assert a not in seed and r not in seed
B=set(seed);ids={q:dict(kind='prepared_initial',cell=q)for q in B};p=regp;history=[];cuts=[]
for t,c in enumerate(raw+l.M):
 q=p[:2];assert(q in B)==(c=='L'),(t,q,c)
 prior=ids.get(q)
 if c=='R':B.add(q);ids[q]=dict(kind='new_R',tick0=t)
 else:B.remove(q);ids.pop(q)
 history.append(dict(tick0=t,cell=q,turn=c,prior_identity=prior))
 p=after(c,p)
 if t+1 in[len(W['V']),len(raw),len(raw+l.M)]:
  tags=[]
  for g in[a,r]:tags.append(dict(cell=g,BLACK=g in B,identity=ids.get(g),CURRENT=g in B and local(g,p)not in l.K,alive_CORE=g in B and local(g,p)in l.K))
  cuts.append(dict(actual_read_count=t+1,pose=p,tags=tags,complete_BLACK=sorted(B)))
assert cuts[0]['tags'][1]['alive_CORE']and cuts[0]['tags'][1]['identity']==dict(kind='new_R',tick0=12)
assert not cuts[1]['tags'][1]['BLACK']and history[20]['turn']=='L'and history[20]['cell']==r
assert all(z['tags'][0]['CURRENT']for z in cuts)
regression=dict(scope='PREPARED local VC+actualM only, no preceding FOREIGN or U ancestry claimed',word=regword,ENTRY=regp,complete_seed=sorted(seed),mass=len(seed),all_actual_reads=history,actual_cuts=cuts)
D=['C4_foreign_original_hook_loss_2026-10-24/manifest.json','audits/check_C4_original_hook_loss_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='ANY actual source F/Q/B ENTRY0N followed by an ordinary-only RAW section with EXACTLY5 Cs cannot complete a next F/Q/B RAW at ENTRY(-5,-2,E). No U ancestry, simple proxy, global-first condition or bound on any ordinary epoch length. A partial recipient can delete an earlier hook before its own L38 failure; no through-recipient hook permanence is claimed.',source_births=source,always_CURRENT_through_C3_old13=sorted(old13),all216_CORE_inclusive_last_RAW_R_roles=rows,all8_S_first_CURRENT_loss_EXIT_inequalities=first_loss_exits,all_ordinary_physical_R_supports=R_support,all3_recipient_own_RAW_r_BLACK_requests=recipients,prepared_transient_CORE_repair_regression=regression,
 proof_steps=[
 'S0 physical R writes cannot reach y3 from source EXIT y<=-2. After C1, E1 heads remain y<=-3 and physical R localx>=-1 gives globaly<=-2. C2 likewise misses both y3 holes. Both holes start WHITE by actual source L34/L35 last reads, including arbitrary dormant archives.',
 'In N2, old13 are CURRENT by signed b961. Every last-R origin of either hole has an earlier first BLACK request on r at ownL5. A first completed N2/C3 repair of r is therefore impossible, and then a is impossible too. Every CORE write is retained in the 36-row per-hole table.',
 'At W3 cuts r may genuinely be alive CORE: the two compatible last-R producers end at (-5,4,W) with r at exitCORE(-1,-1). Every next actual ordinary RAW deletes it at its sole L2. No later W producer can replace it, because both producer heads have x>-5 while W x only decreases. C4 has no compatible last-R role at all. Thus r is WHITE at S4 start, not at every W3 cut.',
 'Any possible W3 last-R birth of a exits at x<=-5. W motion, C4 and S motion cannot increase x. This is an x frontier, not a y bound: W can increase y, and a may genuinely remain external and BLACK.',
 'At an S4 physical last-R producer of either y3 hole, heady>=3. All old13 are still CURRENT there: their first S current-loss exits have y<=their y<=2, and S cannot climb back. All last-R a producers are cut. The sole r producer U(-4,4,S) requires a BLACK at ownL14, but no W birth can reach its headx=-4 and no S a birth exists. Its partial R11 can occur before the incompatible L14; no complete U or r-at-marked-cut follows.',
 'Therefore r is WHITE throughout the remaining S4 marked cuts. A C5 R write of r has RAW EXITx>=r_x=-4. Any E5 D/V/U R write likewise exitsx>=r_x using localRy<=exitY. Remaining E motion cannot decrease x to nextFOREIGN headx=-5. Hence r is WHITE at that recipient ENTRY, and its own first L38/read39 cannot execute. This last step includes CORE writes and requires no fabricated marker.'
 ],limits=['No all-C5 source-hook seal or classification.','No physical WHITE invariance at every W3 cut; the explicit prepared CORE repair is real.','No claim the paired external a repair is dead; it can remain CURRENT.','No automatic one-FOREIGN transfer iteration, initial-star conclusion, arbitrary-tail simplicity, language coverage or capture.'],dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in D})
(HERE/'C5_left_hole.json').write_text(json.dumps(out,indent=2)+'\n')
print('216 final-R rows; N2 WHITE lock, real W CORE repair, S4 a/r x-frontier, 9 source/recipient C5 exclusions. Prepared VC regression',len(seed),'cells',len(raw+l.M),'reads.')
