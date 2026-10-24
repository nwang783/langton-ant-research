"""All-history three-C transfer of eleven genuine F/Q/B output identities.
The apparent W first-loss U gate is excluded by the source's actual L28 hole.
"""
from pathlib import Path
from collections import Counter
import importlib.util,json,hashlib
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
NE={(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1)}
FIELD=NE|{(-2,-1)};hole=(0,2);N_gate=(3,-1,0);W_gate=(2,3,3)
source=[]
for a in'FQB':
 tr=l.trace(W[a]);O=set(map(tuple,l.literal_geometry(W[a])['outputs']))
 assert FIELD<=O and tr['last'][hole]==('L',28) and tr['last'][(-2,-1)]==('R',47)
 source.append(dict(source=a,ENTRY=(0,0,0),EXIT=after(W[a]),all11_actual_source_R_births=[dict(cell=g,own_tick0=tr['last'][g][1])for g in sorted(FIELD)],hole_actual_last_L_own_tick0=28))
roles=[]
for h in(0,3):
 for g in sorted(FIELD):
  for a in'DVU':
   tr=l.trace(W[a]+l.M)
   for slot in map(tuple,l.literal_geometry(W[a])['inputs']):
    p=(*sub(g,l.rot(slot,h)),h);row=dict(heading=h,original=g,consumer=a,true_input=slot,ENTRY=p,actual_L=o.describe(a,tr['first'][slot][1]))
    if(sum(p[:2])+h)%2:route='sector'
    else:
     bad=[]
     for held in sorted(FIELD):
      q=l.rot(sub(held,p[:2]),(-h)%4);f=tr['first'].get(q)
      if q in l.K or f and f[0]=='R':bad.append(dict(original=held,local=q,reason='ENTRY_CORE'if q in l.K else'first_WHITE',actual_first=f))
     route='held_field'if bad else'first_loss_gate';row['conflicts']=bad
    row['route']=route;roles.append(row)
assert len(roles)==176
assert Counter(r['route']for r in roles if r['heading']==0)=={'sector':42,'held_field':44,'first_loss_gate':2}
assert Counter(r['route']for r in roles if r['heading']==3)=={'sector':46,'held_field':41,'first_loss_gate':1}
kept=[r for r in roles if r['route']=='first_loss_gate']
assert {(r['consumer'],r['ENTRY'],r['original'])for r in kept}=={('U',N_gate,(2,0)),('U',N_gate,(2,1)),('U',W_gate,(1,2))}
# The source L28 hole is the W gate's earlier q requirement, before its
# apparent old-NE a input. No internal R repair precedes this first L.
slot=l.rot(sub(hole,W_gate[:2]),1);wt=l.trace(W['U']+l.M)
assert slot==(-1,2) and wt['first'][slot]==('L',13)
# Before an unspent-NE first loss, signed158's actual N2 last-R table
# leaves exactly these three hole funders, including CORE writes.
N_funders=[]
for a in'DVU':
 tr=l.trace(W[a]);ct=l.trace(W[a]+l.M)
 for slot,(c,t)in tr['last'].items():
  if c!='R':continue
  p=(*sub(hole,slot),0)
  if sum(p[:2])%2:continue
  bad=[]
  for held in sorted(NE):
   q=sub(held,p[:2]);f=ct['first'].get(q)
   if q in l.K or f and f[0]=='R':bad.append(held)
  if not bad:N_funders.append(dict(producer=a,ENTRY=p,actual_R_own_tick0=t,RAW_EXIT=after(W[a],p)))
assert {(r['producer'],r['ENTRY'],r['RAW_EXIT'])for r in N_funders}=={('D',(-2,2,0),(-1,3,0)),('V',(-2,2,0),(-1,5,0)),('U',(-2,2,0),(-2,6,0))}
assert all(r['RAW_EXIT'][1]+1>W_gate[1]for r in N_funders)
# ALL physical R writes, not just external outputs: a completed W D/V/U
# producer of h exits at x<=h_x=0. C3 is N-oriented and every one of its
# physical R slots has x>=0, so it also exits at x<=0 after writing h.
R_bounds=[]
for a in'DCVU':
 p=(0,0,0);ep=after(W[a]);rr=[]
 for t,c in enumerate(W[a]):
  if c=='R':
   q=p[:2]
   if a=='C':
    assert q[0]>=0
    producer=(*sub(hole,q),0);ex=after(W[a],producer)
    assert ex[0]<=0
    kind='C3_N_to_W'
   else:
    assert q[1]<=ep[1]
    producer=(*sub(hole,l.rot(q,3)),3);ex=after(W[a],producer)
    assert ex[0]<=0
    kind='completed_W_DVU'
   rr.append(dict(own_tick0=t,physical_R_local=q,producer_ENTRY=producer,actual_RAW_EXIT=ex,exit_x_at_most_hole_x=ex[0]<=hole[0],kind=kind))
  p=after(c,p)
 R_bounds.append(dict(atom=a,all_actual_R_supports=rr))
# These are exhaustive full-cut funders. A writer begun before the
# deleting/source packet cannot complete later because actual RAWs do not
# overlap. An alive-CORE residual export still needs a genuine physical R.
for a in'DVU':
 for slot in map(tuple,l.literal_geometry(W[a])['inputs']):
  assert slot[1]>=1 and slot[0]>=-1
  assert after(W[a],(0,0,3))[1]>=0
newO={add(N_gate[:2],tuple(q))for q in l.literal_geometry(W['U'])['outputs']}
old9=FIELD-{(2,0),(2,1)}
assert len(old9)==len(newO)==9 and not(old9&newO) and max(g[1]for g in old9|newO)==2
assert after(W['U'],N_gate)==(3,3,0)
for g in old9:
 assert sub(g,N_gate[:2])not in l.trace(W['U']+l.M)['first']
D=['foreign_two_C_pair_hole_transfer_2026-10-24/manifest.json','audits/check_foreign_two_C_pair_hole_independent.json','foreign_two_C_north_frontier_2026-10-24/manifest.json','audits/check_foreign_two_C_frontier_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Any actual source F/Q/B ENTRY(0,0,N), then ordinary RAW D/C/V/U with real marker contexts and at most three actual Cs. No foreign occurs after source before the protected cut. No U-entry, earlier-history, simplicity or bounded-length premise.',all3_source_output_and_hole_interfaces=source,all176_joint_first_loss_roles=roles,all3_N2_CORE_inclusive_hole_funders=N_funders,all_actual_physical_R_bounds_for_C3_and_W=R_bounds,
 first_loss_proof='The tracked eleven originals have y>=-1. S0 true input y<=source_EXIT_y-1<=-3 and E1 input y<=source_EXIT_y<=-2, so all remain CURRENT. At the earliest loss among all eleven, the actual N/W tables are exhaustive and retain simultaneous TRUE inputs. N2 leaves only U(3,-1,N), which consumes exactly common(2,0) and q(2,1). Its actual exit(3,3,N) puts all eighteen retained/new outputs at y<=2, below later N inputs y>=4 and later W inputs y>=3. Thus no further tracked loss is possible through W3. If no N loss occurred, W3 leaves only U(2,3,W). But its own L13 first requires the physical source L28 hole (0,2) BLACK.',
 W_gate_hole_funding_proof='S0/E1 physical R supports miss h=(0,2). With NE still unspent, any completed N2 last-R repair is one of the three listed funders; each exits y>=3, so C3 forces W heads y>=4, above gate y=3. Any R repair inside C3 exits at x<=h_x=0, because every C R slot has nonnegative x. Every completed W D/V/U R writer also exits at x<=h_x=0, including all CORE writes, because its local R y never exceeds its RAW exit y. W motion cannot increase x, so none can precede gate x=2. Distinct actual RAW packets do not overlap. The first gate request to h is L13, with no earlier internal R. Hence this apparent W first-loss gate is impossible.',
 transfer_dichotomy=dict(unspent='All eleven SAME source outputs remain CURRENT.',spent='The sole possible first loss is actual N2 U(3,-1,N). Exactly the two old originals die; nine remaining originals and all nine new U outputs are CURRENT through every later real ordinary cut through W3.',nine_retained_originals=sorted(old9),nine_new_U_outputs=sorted(newO),different_q_identity_at_same_cell=(2,1)),
 generic_two_tag_corollary='The SAME source R46(-1,-1) and R47(-2,-1) are CURRENT through every such ordinary cut with at most three Cs, for source F as well as Q/B. This is an ordinary-prefix statement only, not preservation through a next foreign reader.',
 not_claimed=['No preservation of all NE originals: the paired N2 rewrite is genuinely attained.','No next-foreign preservation of the eleven outputs or F two-tag pair.','No four-C or later-foreign extension, global simplicity, trajectory coverage, resource budget or capture.'],dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in D})
(HERE/'three_C_NE_reserve.json').write_text(json.dumps(out,indent=2)+'\n')
print('Any sourceFORE through ordinaryC3:176 joint roles leave N2 paired gate only; W3 U gate blocked by actual L28 hole. Either11 originals CURRENT or9 old+9 new CURRENT. Generic R46/R47 current through3, not through nextFORE.')
