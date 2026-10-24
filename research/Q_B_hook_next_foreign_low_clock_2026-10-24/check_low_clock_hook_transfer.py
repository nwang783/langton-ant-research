"""Generic sourceQ/B to nextFOREIGN hook transfer atC0/C1, plus a
qualified disjoint-clock join with independently signed exactC2. No
standalone C-FOREIGN ban, initialU or ordinary-prefix simplicity premise.
"""
from pathlib import Path
from collections import Counter
from functools import lru_cache
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

def spell(s):return ''.join(W[a]for a in s)
def owner(word,t):
 off=0
 for i,a in enumerate(word):
  if t<off+len(W[a]):return dict(atom_index0=i,atom=a,own_tick0=t-off,own_read_number1=t-off+1,turn=W[a][t-off])
  off+=len(W[a])
 return dict(owner='actual following word via M11',next_tick0=t-off,next_read_number1=t-off+1,turn=l.M[t-off])
@lru_cache(None)
def perms(d,v,u):
 if d+v+u==0:return ('',)
 out=[]
 if d:out+=['D'+s for s in perms(d-1,v,u)]
 if v:out+=['V'+s for s in perms(d,v-1,u)]
 if u:out+=['U'+s for s in perms(d,v,u-1)]
 return tuple(out)
NE={(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1)};HOOK={(-1,-1),(-2,-1),(-3,-1),(-3,-2)};field=NE|HOOK
frames=[]
for A in'QB':
 ep=after(W[A]);t=l.trace(W[A]);assert HOOK<=set(map(tuple,l.literal_geometry(W[A])['outputs']));frames.append(dict(source=A,ENTRY=(0,0,0),EXIT=ep,all4_own_hook_R_births=[dict(cell=q,R_tick0=t['last'][q][1])for q in sorted(HOOK)]))
classifications={};remainders={}
for c,h in[(0,2),(1,1)]:
 goals={}
 for A2 in'FQB':
  t=l.trace(W[A2]+l.M)
  for tag in HOOK:
   for slot in map(tuple,l.literal_geometry(W[A2])['inputs']):
    p=(*sub(tag,l.rot(slot,h)),h)
    if(sum(p[:2])+h)%2:continue
    goals.setdefault((A2,p),[]).append(dict(source_hook=tag,true_input=slot,physical_first_L=o.describe(A2,t['first'][slot][1])))
 rows=[];keep=[]
 for(A2,p),rs in sorted(goals.items()):
  t=l.trace(W[A2]+l.M);bad=[]
  for g in sorted(field):
   loc=l.rot(sub(g,p[:2]),-h);f=t['first'].get(loc)
   if loc in l.K or f and f[0]=='R':bad.append(dict(SAME_CURRENT=g,local=loc,role='ENTRY_CORE'if loc in l.K else'initial_WHITE',first=f))
  row=dict(C_count=c,next_foreign=A2,entry=p,input_witnesses=rs)
  if bad:row.update(classification='CURRENT_FIELD_CORE_WHITE',conflicts=bad)
  else:row['classification']='endpoint_route';keep.append(row)
  rows.append(row)
 classifications[c]=rows;remainders[c]=keep
assert len(classifications[0])==57 and Counter(q['classification']for q in classifications[0])=={'CURRENT_FIELD_CORE_WHITE':51,'endpoint_route':6}
assert len(classifications[1])==56 and Counter(q['classification']for q in classifications[1])=={'CURRENT_FIELD_CORE_WHITE':41,'endpoint_route':15}
# C0 heads never increase y from the negative sourceFOREIGN S exit.
zero=[]
for A in'QB':
 ep=after(W[A]);assert ep[1]<=-4
 for q in remainders[0]:
  p=q['entry'];assert p[1]>ep[1];zero.append(dict(source=A,next_foreign=q['next_foreign'],target=p,source_S_EXIT=ep,route='unreachable_S_zero_C_target_above_start'))
assert len(zero)==12
# C1 S/E endpoint equations have an actual finite vertical budget for each
# of the15 field-compatible poses. No arbitrary word-depth bound is used.
tuples=[];words={};endpointrows=[]
for A in'QB':
 ep=after(W[A])
 for q in remainders[1]:
  A2=q['next_foreign'];p=q['entry'];dy=ep[1]-1-p[1];nsol=0
  if dy>=0:
   for vs in range(dy//3+1):
    for us in range(dy//4+1):
     for ds in range(dy-3*vs-4*us+1):
      rem=dy-ds-3*vs-4*us
      for ve in range(rem+1):
       de=rem-ve;dx=p[0]-ep[0]+ds+vs-de-3*ve
       if dx<0 or dx%4:continue
       ue=dx//4;nsol+=1;tuples.append(dict(source=A,next_foreign=A2,target=p,S_counts=(ds,vs,us),E_counts=(de,ve,ue)))
       for pre in perms(ds,vs,us):
        for post in perms(de,ve,ue):
         word=A+pre+'C'+post+A2;assert after(spell(word[:-1]))==tuple(p);words[word]=dict(source=A,next_foreign=A2,ordinary_section=pre+'C'+post,target=p)
  endpointrows.append(dict(source=A,next_foreign=A2,target=p,exact_vertical_budget=dy,nonnegative_count_tuple_count=nsol))
assert len(words)==12 and{(w[0],d['ordinary_section'])for w,d in words.items()}=={('B','C'),('B','DC'),('Q','CD'),('Q','DCD')}
failures=[]
for word,meta in sorted(words.items()):
 t=l.trace(spell(word)+l.M);assert not t['feasible'];failures.append(dict(word=word,endpoint_data=meta,immutable_conflict=t,previous_owner=owner(word,t['previous_read']),conflicting_owner=owner(word,t['conflict_read'])))
# Positive scope controls preserve literal C->FOREIGN legality, including
# the principal-wrap situation. They are prepared C-entry, not U ancestry.
rawCF=[]
for A in'FQB':
 word='C'+A;t=l.trace(spell(word)+l.M);assert t['feasible'];seed={q for q,(c,t)in t['first'].items()if c=='L'}; board=set(seed); p=(0,0,0)
 for c in spell(word)+l.M:
  assert(p[:2]in board)==(c=='L')
  if c=='L':board.remove(p[:2])
  else:board.add(p[:2])
  p=after(c,p)
 rawCF.append(dict(word=word,feasible=True,complete_seed=sorted(seed),seed_mass=len(seed),scope='Actual standalone RAW-C/foreign word; not a complete8 C-tail. No universal rawC-toFOREIGN ban used.'))
D=[R/'foreign_two_C_north_frontier_2026-10-24/manifest.json',R/'audits/check_foreign_two_C_frontier_independent.json',R/'foreign_hook_four_C_maturity_2026-10-24/manifest.json',R/'audits/check_hook_four_C_maturity_independent.json',R/'Q_B_hook_two_C_foreign_transfer_2026-10-24/manifest.json',R/'audits/check_QB_two_C_hook_transfer_independent.json',R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='ANY actual sourceQ/B then ONLYordinaryRAW connector containing0,1or2 actualCs, then NEXT completeF/Q/B+actualM. No U/firstforeign/globalSIMPLE/lengthbound premise. All4 SAME sourcehook IDs remainCURRENT through nextFOREIGN EXIT. New checks coverC0/C1; C2 is imported only from independently signed63c1fb62 with its exact premises.',all2_source_hook_frames=frames,all57_C0_true_hook_loss_pose_field_checks=classifications[0],all56_C1_true_hook_loss_pose_field_checks=classifications[1],all12_typed_C0_endpoint_contradictions=zero,all30_typed_C1_endpoint_count_solutions=endpointrows,all_C1_nonnegative_tuples=tuples,all12_C1_whole_word_immutable_conflicts=failures,all3_legal_raw_C_FOREIGN_scope_controls=rawCF,endpoint_completeness='C0 ordinary S cannotraiseY from sourceEXIT. In C1, S rail,C(0,-1),E rail gives dS+3vS+4uS+dE+vE=exitY-1-targetY and4uE=targetX-exitX+dS+vS-dE-3vE. The real nonnegative target budget bounds allcounts. Every ordering generated, emptyrails included. Only B(C),B(DC),Q(CD),Q(DCD) survive endpoints; whole source+section+nextFOREIGN traces allfailimmutable. This does not prohibit standalone CFOREIGN or discard actual previousC wrap.',qualified_disjoint_clock_join='The new independent C0/C1 cases and signed exactC2 cases are disjoint by actual ordinaryC count. All use SOURCE-ENTRY frame and true source lastR IDs. Thus any first loss of these original hook IDs at the nextFOREIGN needs at least3 actual ordinaryCs in between; no theorem for3+Cs or a furtherFOREIGN is inferred.',CURRENT_completion='Signed ordinaryhook lifetime4 covers pre-next cut. Every possible FOREIGN firstCURRENT loss is a trueI firstL including markerexitCOREcapture; initialCORE/firstWHITE poses are impossible with currentoldhooks. Since all such poses are excluded atC0/C1/C2, SAME originals remainBLACKoutside nextEXITCORE. No marker is called a completed nextword.',not_claimed=['No preservation through another FOREIGN after this nextone.','No sourceF two-tag extension.','No sourceoutputseal, foreign-count spending bound, arbitrarytail simplicity, languagecoverage orcapture.'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'low_clock_hook_transfer.json').write_text(json.dumps(out,indent=2)+'\n');print('ANY Q/B hook across NEXTFOREIGN C<=2: C0 57=51field+6unreachable; C1 56=41field+15endpoint ->12 immutable words; exactC2 separately signed63. RawCF/CQ/CB positive controls retained.')
