"""All four SAME fresh-U star IDs through an arbitrary ordinary RAW suffix.
This is exact G8 parsing plus a single terminal input-free C, not an old
maturity law transported through a foreign or a geometric-simple induction.
"""
from pathlib import Path
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h
STAR={(0,0),(0,1),(1,0),(1,1)};ut=l.trace(W['U']);uO=set(map(tuple,l.literal_geometry(W['U'])['outputs']));assert STAR<=uO
births=[dict(cell=q,last_R_tick0=ut['last'][q][1])for q in sorted(STAR)];assert [q['last_R_tick0']for q in births]==[4,19,9,18]
# An actual plain C has no external before-BLACK requirement. Every new
# exit CORE edge is either actual RAW-written or inherited ENTRY CORE;
# there is no silent absorption of a previous external CURRENT original.
cg=l.literal_geometry(W['C']);ct=l.trace(W['C']+l.M);cr=l.trace(W['C']);assert cg['inputs']==[];ce=after(W['C']);newK={add(ce[:2],l.rot(q,ce[2]))for q in l.K};capture=[]
for q in sorted(newK):
 if q not in l.K:assert q in cr['last']and cr['last'][q][0]=='R'
 capture.append(dict(C_EXIT_CORE_cell=q,in_ENTRY_CORE=q in l.K,actual_RAW_last_read=cr['last'].get(q),actual_first_requirement=ct['first'].get(q)))
assert {q for q,(c,t)in ct['first'].items()if c=='L'}==l.K
# Actual finite regression with earlier foreign, a selected new U and the
# exceptional terminal DCC. Track all four source IDs through real cuts.
controls=[]
for word,idx in [('UDCC',0),('UQUDCC',2),('UBUDCC',2),('UQUCCV',2)]:
 raw=''.join(W[a]for a in word);tt=l.trace(raw+l.M);assert tt['feasible'];seed={q for q,(c,t)in tt['first'].items()if c=='L'};B={q:('initial',q)for q in seed};p=(0,0,0);tick=0;ids={};cuts=[]
 for i,a in enumerate(word):
  if i==idx:
   assert a=='U';sourcep=p;sourcet=tick;ids={add(p[:2],l.rot(q,p[2])):tick+ut['last'][q][1]for q in STAR}
  for c in W[a]:
   cell=p[:2];assert(cell in B)==(c=='L')
   if c=='L':del B[cell]
   else:B[cell]=tick
   p=after(c,p);tick+=1
  if i>=idx:
   K={add(p[:2],l.rot(q,p[2]))for q in l.K};assert all(B.get(q)==b and q not in K for q,b in ids.items());cuts.append(dict(after_atom_index0=i,atom=a,RAW_cut_tick0=tick,head=p,all4_SAME_CURRENT=True))
 for c in l.M:
  cell=p[:2];assert(cell in B)==(c=='L')
  if c=='L':del B[cell]
  else:B[cell]=tick
  p=after(c,p);tick+=1
 controls.append(dict(word=word,selected_new_U_index0=idx,source_entry=sourcep,source_start_tick0=sourcet,complete_seed=sorted(seed),all_physical_reads=tick,SAME_star_births=[dict(cell=q,birth_tick0=b)for q,b in sorted(ids.items())],all_actual_selected_RAW_cuts=cuts))
D=[H/'manifest.json',R/'audits/check_RAW_G8_base_cut_bridge_independent.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'audits/check_U_left_star_permanence_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='A genuinely fresh actual RAW U, then any finite ordinary RAW D/C/V/U suffix with actual final M11. No foreign AFTER that U; arbitrary history, including an earlier foreign, is allowed before it. All four SAME source-U star IDs remain CURRENT at every real later ordinary RAW cut. No global proxy simplicity premise is needed.',source_births=births,grammar_dichotomy='The signed maximal-run local proof gives either exact chosenG8 parsing from initialU, or a single terminalDCC. Every internalD has a real priorRAW, so the incoming-bud obstruction has no factor-first exception here. No other unparsed ending is possible.',G8_invocation='The signed1918 star theorem holds for ANY actual completeG8 factor and ANY actual U-family packet inside it; it does not require a pre-factor U or globally simple history. Initial freshRAW U is the genuine base of ACTUAL U/UC/UCC. Its SAME last-R star is the star of that packet, since own C tails preserve it. Therefore all four are CURRENT through each actual full-packet boundary and source own C RAW cuts.',atomic_cut_qualification='For a protected intermediate C cut inside a genuine full packet, use the actual factor ending just before that C at its preceding RAW cut and the input-free C step below; or the literal own-tail preservation. No consumer full tail is assumed completed before its real time.',terminal_DCC_step='If selected factor endsDCC, remove only its FINAL C. The remaining actual factor ends in chosenDC and beginsU-family, with actual M11 supplied by this real finalC. Signed1918 supplies all four SAME originals CURRENT at the DC RAW cut. Plain C has I0 and no silent external-toCORE capture; any old external CURRENT BLACK cell mustMISS its completecontext and remainoutside exitCORE. Thus the finalC preserves all four. This uses a REAL executed C, not an assumed complete DCC packet.',all5_C_EXIT_CORE_capture_checks=capture,plain_C_external_input_set=cg['inputs'],all4_complete_finite_regressions=controls,not_claimed=['No foreign after the selected U.','No original preforeign star is carried across F/Q/B.','No arbitrary-tail proxy simplicity or disjointness from pre-U sources.','No physical WHITE permanence, source-output seal, trajectory-language coverage or capture.','An alive CORE original would be a CURRENT loss; the C step explicitly rules that out rather than ignoring it.'],dependencies={str(q.relative_to(R)):hashlib.sha256(q.read_bytes()).hexdigest()for q in D})
(H/'fresh_U_star_RAW_lift.json').write_text(json.dumps(out,indent=2)+'\n');print('Fresh U RAW all4 star: actualG8 or terminalDC+input-freeC dichotomy. No simple-prefix premise. Four full controls include UQ/UB U DCC terminal exceptions.')
