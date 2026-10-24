from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction as F
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'old_U_third_source_join_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert sha(D/'manifest.json')=='a4c841fddb3fcfdd7d5e003598eda4def5edf13377b62071cb64e38050b7e2d0'
for f,h in json.loads((D/'manifest.json').read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'U_third_join.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,G,rot,center,xy,meet,cross=[ns[k]for k in('W','M','K','tr','G','rot','center','xy','meet','cross')]
raw=lambda s:''.join(W[a]for a in s)
angles=[a for a in json.loads((R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json').read_text())['all831_conditional_preFOREIGN_old_source_angle_interfaces'] if a['old_source']=='U'];assert len(angles)==236 and angles==J['all236_signed_old_U_angle_rows']
LEFT={0j,1j};STAR=LEFT|{1+0j,1+1j};INITIAL=STAR|{1+3j};facts=[]
for src in ('U','UC','UCC'):
 z=tr(raw(src));ek={z['p']+rot(z['h'])*k for k in K}
 assert all(z['last'][q][0]=='R' and q not in ek for q in INITIAL)
 assert z['last'][1+3j]==('R',26)
 facts.append((src,[(xy(q),z['last'][q][1]) for q in sorted(INITIAL,key=lambda z:(z.real,z.imag))]))
for r in J['all3_actual_U_source_before_FOREIGN_tag_births']:
 assert r['actual_full_completion_clock']==r['actual_creating_full'].count('C')
 assert next(z for s,z in facts if s==r['actual_creating_full'])==[(t['cell'],t['source_actual_last_R_tick0']) for t in r['all5_genuine_before_FOREIGN_current_tags']]
a=center(0,0);b=center(G['U']['p'],G['U']['h']);geo={};parallel_omitted=[]
for target,total in sorted({(a['third'],a['total_ordinary_C_before_third']) for a in angles}):
 h=(2-total)%4;z=tr(W[target],h=h);c=center(0,h);d=center(z['p'],z['h']);den=cross(b-a,d-c);corners=[(a+s*(b-a)-c-t*(d-c))/2 for s,t in product((0,1),repeat=2)];rows=[]
 for x in range(math.floor(min(z.real for z in corners)),math.ceil(max(z.real for z in corners))+1):
  for y in range(math.floor(min(z.imag for z in corners)),math.ceil(max(z.imag for z in corners))+1):
   if(x+y-total)%2:continue
   p=complex(x,y)
   if den:
    hit=meet(a,b,c+2*p,d+2*p)
    if hit is None or not(0<=hit[0]<1 and 0<hit[1]<=1):continue
    ss,tt=hit
   else:
    assert target=='U' and total==2 and d-c==b-a
    zz=c+2*p-a
    if cross(zz,b-a):continue
    start=F(int(zz.imag),int((b-a).imag))
    if 0<=start<1:parallel_omitted.append((target,total,x,y,h,str(start)));continue
    ss,tt=F(0),-start
    if not 0<tt<=1:continue
   ctx=tr(W[target]+M);cuts=[q for q in LEFT if (q-p)/rot(h) in K or ctx['req'].get((q-p)/rot(h)) is False]
   if cuts:route='SAME_LEFT_at_global_FIRST_contact_ENTRY'
   elif h==1:route='signed_E_endpoint_guard_0e82a78e'
   elif (target,p,h)==('V',4j,2):route='S_pose_V_r_guard_277cedd1_or_CCv_direct'
   elif target in 'VU' and (p,h)==(3j,3):route='signed_W_arm_guard_bb6eb6b5'
   else:route='direct_genuine_preFOREIGN_before_state'
   rows.append((target,total,(x,y,h),str(ss),str(tt),route))
 geo[target,total]=rows
assert len(geo)==15 and sum(map(len,geo.values()))==50
flat=[r for rr in geo.values() for r in rr]
assert set(flat)=={(r['third'],r['totalK'],tuple(r['third_pose']),r['old_s'],r['new_t'],r['route']) for r in J['all50_unique_outgoing_owned_contact_geometries']}
route_counts=Counter(r[-1] for r in flat);assert route_counts['SAME_LEFT_at_global_FIRST_contact_ENTRY']==37
allrows={};direct={};cnt=Counter();actualowners=[]
for idx,angle in enumerate(angles):
 b1,b2,b3=[angle[k] for k in ('first','second','third')];total=angle['total_ordinary_C_before_third'];n=angle['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age'];ha=angle['true_FOREIGN_heading_relative_old']
 assert 0<=n<=total<=4 and total==n+(b1+b2).count('C') and ha==(-n)%4
 for atom,totalkey,pose,ss,tt,route0 in geo[b3,total]:
  p3=complex(*pose[:2])
  for A in 'FQB':
   de=tr(raw(A+b1+b2),h=ha);pa=p3-de['p'];assert de['h']==pose[2]
   route=route0
   if route=='S_pose_V_r_guard_277cedd1_or_CCv_direct':
    if n in (3,4):route='signed_S_pose_V_r_guard_277cedd1'
    else:assert n==2 and b1==b2=='C';route='direct_genuine_preFOREIGN_before_state'
   key=(idx,A,b1,b2,b3,n,total,tuple(xy(pa)+[ha]),pose);allrows[key]=route
   if route!='direct_genuine_preFOREIGN_before_state':continue
   tokens=A+b1+b2+b3;ctx=tr(raw(tokens)+M,pa,ha);ac=tr(W[A]+M,pa,ha)
   if ctx['bad']:why='immutable_complete_local_literal_conflict'
   elif any(q in ac['req'] for q in STAR):why='forbidden_firstFOREIGN_young_STAR_context_touch'
   else:
    ak={pa+rot(ha)*q for q in K};conflicts=[q for q in INITIAL if q in ak or ctx['req'].get(q) is False];assert conflicts
    why='genuine_preFOREIGN_current_or_BLACK_before_state_contradiction'
    for q in conflicts:
     if q in ak:continue
     tick=next(i for i,(pos,h,ch) in enumerate(ctx['reads']) if pos==q);lo=0
     for ii,token in enumerate(tokens):
      if tick<lo+len(W[token]):owner=(token,ii,tick-lo,tick-lo+1);break
      lo+=len(W[token])
     else:assert 0<=tick-lo<11;owner=('next_word',len(tokens),tick-lo,tick-lo+1)
     actualowners.append((key,xy(q),tick,owner))
   direct[key]=why;cnt[why]+=1
assert len(allrows)==2346 and len(direct)==291 and dict(cnt)==J['exact_direct_disjoint_classification']
def key(r):return(r['signed_angle_index0'],r['foreign'],r['first'],r['second'],r['third'],r['true_preFOREIGN_age'],r['totalK'],tuple(r['foreign_pose']),tuple(r['third_pose']))
assert allrows=={key(r):r['route'] for r in J['all2346_necessary_FOREIGN_typed_contact_labels_and_exhaustive_routes']}
assert direct=={key(r):r['classification'] for r in J['all291_direct_preFOREIGN_before_state_cases']}
# Bind each supplied first-WHITE witness to a genuinely owned actual read.
owner_map={(k,tuple(q)): (tick,owner) for k,q,tick,owner in actualowners}
for r in J['all291_direct_preFOREIGN_before_state_cases']:
 for w in r.get('exact_current_or_BLACK_conflicts',[]):
  if 'combined_tick0' not in w:continue
  tick,owner=owner_map[key(r),tuple(w['SAME_preFOREIGN_BLACK_cell'])];assert tick==w['combined_tick0']
  stored=w['actual_owner'];assert stored['actual_atom']==('next actual word' if owner[0]=='next_word' else owner[0])
report=dict(status='PASS complete genuine old-U outgoing source exclusion for chronological FIRST THIRD ordinary RAW contact only',manifest_sha256=sha(D/'manifest.json'),proof_sha256=sha(D/'U_third_join.md'),independent_checker_sha256=sha(S),signed_angles=236,exact_boxes=15,unique_geometries=50,typed_labels=2346,geometric_routes=dict(route_counts),parallel_already_contact_entries_omitted=parallel_omitted,direct_masks=291,direct_classes=dict(cnt),genuine_full_source_final_R_facts=facts,actual_first_WHITE_owners=actualowners,analytic_scope=['True preFOREIGN n and totalK=n+both returnedC indicators are separately rebuilt. Young complete-foreign STAR-MISS plus global-FIRST stopping at candidateENTRY permits SAMELEFT currentness, not all-four postforeign survival.','37 LEFT,4 signed E,1 S with n3/4 signedV-r and3 n2CCV direct labels,2 signed W-arm,6 direct poses exhaust every exact outgoing-owned geometry. Collinear positive onset and oldEND reassignment retained.','Direct291 masks use only genuinely PREFOREIGN SAMESTAR currentness and R26 bud current through4 for actual completed U/UC/UCC;73 literal,13 youngFOREstar touches,205 beforestate CORE/first-WHITE contradictions. First-WHITE tests constrain the original entry BLACK bit, not postforeign age or identity replacement.','Only old-U source closure. OldC separately signed; oldD/V and overall THIRD simplicity remain outside this join. No arbitrary suffix iteration or secondforeign.'])
S.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS',sha(S.with_suffix('.json')))
