from pathlib import Path
from itertools import product
from fractions import Fraction as F
from collections import Counter
import math,json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'V_postforeign_pair_rail_reserve_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert sha(D/'manifest.json')=='35815d85cf5ba7a05f39ef0e70ebda5deeb3210cf389b90376c0a709e8518e25'
for f,h in json.loads((D/'manifest.json').read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'pair_rail_reserve.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,G,rot,center,xy,meet,pieces,cross=[ns[k]for k in('W','M','K','tr','G','rot','center','xy','meet','pieces','cross')];raw=lambda seq:''.join(W[a]for a in seq);full=('D','DC','V','VC','VCC','U','UC','UCC')
def inventory(s):
 z=tr(raw(s));ct=tr(raw(s)+M);ek={z['p']+rot(z['h'])*q for q in K};ii={q for q,b in ct['req'].items()if b and q not in K};oo={q for q,(c,t)in z['last'].items()if c=='R'and q not in ek}
 for q in ek-K:assert q in ct['req']and(q in ii or ct['req'][q]is False)
 return z,ct,ii,oo,ek
inv={s:inventory(s)for s in full+('C','F','Q','B')};assert not inv['C'][2]
# Every old residual-to-CORE export is covered by a true full input or a first-WHITE contradiction.
geo=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
for s in full:
 g=next(x for x in geo if x['name']==s);assert inv[s][2]=={complex(*q)for q in g['inputs']}and inv[s][3]=={complex(*q)for q in g['outputs']}
r=0j;B=1+0j;C=2+1j;bud=2+2j;bridge=[3-1j,1+1j,-1-1j];bc=Counter();bg=[];rcontext=Counter()
for src in('V','VC','VCC'):
 for cell,tick in((r,4),(B,9),(C,7),(bud,16)):assert inv[src][0]['last'][cell]==('R',tick)and cell in inv[src][3]
 for atom in'DVU':
  for h,inp in product(range(4),inv[atom][2]):
   p=B-rot(h)*inp;localr=-p/rot(h);z=tr(W[atom],p,h);ch=(center(p,h),center(z['p'],z['h']))
   if(int(p.real+p.imag)+h)%2:why='wrong_sector'
   elif localr in inv[atom][1]['req']:
    if localr in inv[atom][2]:assert any(meet(*ch,*old)is not None for old in pieces(src))
    why='held_r_complete_context_contact';rcontext['CORE'if localr in K else'WHITE'if inv[atom][1]['req'][localr]is False else'INPUT']+=1
   elif any(meet(*ch,*old)is not None for old in pieces(src)):why='source_contact'
   else:
    why='one_of_four_geometric_B_gates_WITH_upper_U_RETAINED';assert(atom,p,h)in(('D',1-1j,0),('V',1-3j,0),('U',2-2j,0),('U',2-4j,0));prefix=(ch[0],bridge[0])
    assert meet(*prefix,bridge[0],bridge[1])==(F(1),F(0))and meet(*prefix,bridge[1],bridge[2])is None
    for i,old in enumerate(pieces(src)):
     assert meet(*old,bridge[0],bridge[1])is None
     assert meet(*old,bridge[1],bridge[2])==((F(0),F(1))if i==0 else None)
    first=next(i for i,(q,hh,c)in enumerate(inv[atom][1]['reads'])if q==inp);bg.append((src,atom,tuple(xy(p)+[h]),tuple(xy(inp)),first))
   bc[why]+=1
assert bc==Counter(wrong_sector=48,held_r_complete_context_contact=36,one_of_four_geometric_B_gates_WITH_upper_U_RETAINED=12)
print('held-r complete context types',rcontext)
for row in J['all12_plain_B_bridge_gates']:
 key=(row['actual_old_source_full'],row['consumer'],tuple(row['pose']),tuple(row['input_cell']),row['actual_first_B_input_read']['context_tick0']);assert key in bg
# Independently bind earlier PLAIN r loss cover, including simultaneous-pair exclusion at ENTRY.
rref=json.loads((R/'audits/check_V_r_postforeign_clock_independent.json').read_text());assert rref['plain_RAW_first_loss_cover']=={'sector':48,'source_contact':39,'gate':9}
for src,atom,p,first in rref['all9_source_tail_gates']:
 p=complex(*p);local=(B-p)/rot(3);assert local not in inv[atom][2]and(local in K or inv[atom][1]['req'].get(local)is False)
# Actual principal turns: consumer pi/2-aH -> NW -> SW -> source pi/2-beta.
for beta in(F(1,4),F(1,2),F(3,4)):
 for atom in'DVU':
  aH={'D':F(1),'V':beta,'U':F(0)}[atom];close=[1+aH,F(2),-3-beta];assert all(-4<x<4 for x in close)and sum(close)==aH-beta
  for k in range(10):assert(2*k+4+beta-aH)+sum(close)==2*k+4
assert[k for k in range(20)if 2*k+4 in(-8,8)]==[2]
COUNT={tuple(map(int,l.split()[:8]))for l in(R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()};young={}
for src in('V','VC','VCC'):
 for cell in(C,bud):
  for n in range(4):
   h=(-n)%4
   for co in full:
    for inp in inv[co][2]:
     p=cell-rot(h)*inp;key=(full.index(src),full.index(co),*xy(p),h,*xy(cell),n);why='sector'if(int(p.real+p.imag)+h)%2 else'signed_COUNT5'
     if why=='signed_COUNT5':assert key in COUNT
     young[key]=why
assert len(young)==552 and Counter(young.values())==Counter(sector=276,signed_COUNT5=276);assert young=={tuple(x['key']):x['reason']for x in J['all552_C_and_bud_age0_through3_queries']}
# Plain W rail and all bud loss exits, with actual marker ownership.
cports=[];bports=[]
for atom in'DVU':
 for inp in inv[atom][2]:
  p=C-rot(3)*inp;z=tr(W[atom],p,3);first=next(i for i,(q,hh,c)in enumerate(inv[atom][1]['reads'])if q==inp)
  if(int(p.real+p.imag)+3)%2:why='sector'
  elif p==3+2j:
   assert atom=='U'and meet(*pieces('V')[0],center(p,3),center(z['p'],z['h']))is not None;why='contact'
  else:assert(atom,p)==('U',4+1j)and inv[atom][1]['req'][(B-p)/rot(3)]is False;why='B_WHITE'
  cports.append((atom,tuple(xy(inp)),tuple(xy(p)+[3]),first,why))
  pp=bud-rot(3)*inp;zz=tr(W[atom],pp,3);assert zz['p'].real<=2;bports.append((atom,tuple(xy(inp)),tuple(xy(pp)+[3]),tuple(xy(zz['p'])+[zz['h']]),first))
assert Counter(x[-1]for x in cports)==Counter(sector=6,contact=1,B_WHITE=1)
assert {a:tuple(xy(tr(W[a],h=3)['p']))for a in'DVU'}=={'D':(-1,1),'V':(-3,1),'U':(-4,0)}
# Independently reconstruct all signed angles, closed contact boxes and inverse foreign poses.
angles=[x for x in json.loads((R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json').read_text())['all831_conditional_preFOREIGN_old_source_angle_interfaces']if x['old_source']=='V'and x['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age']in(3,4)];assert len(angles)==66
old=pieces('V')[0];u=old[1]-old[0];nposes=0;rows={};classes=Counter()
def status(cell,atom,p,h):
 local=(cell-p)/rot(h);ct=inv[atom][1]
 return'CORE'if local in K else'MISS'if local not in ct['req']else'L'if ct['req'][local]else'R'
for ag in angles:
 b1,b2,b3=ag['first'],ag['second'],ag['third'];n=ag['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age'];KK=n+(b1+b2).count('C');assert KK==ag['total_ordinary_C_before_third'];h=(2-KK)%4;ha=(-n)%4;assert(h,ha)==(ag['third_heading_relative_old'],ag['true_FOREIGN_heading_relative_old'])
 z=tr(W[b3],h=h);c=center(0,h);v=center(z['p'],z['h'])-c;den=cross(u,v);assert den
 corners=[(old[0]+s*u-c-t*v)/2 for s,t in product((0,1),repeat=2)]
 for x in range(math.floor(min(p.real for p in corners)),math.ceil(max(p.real for p in corners))+1):
  for y in range(math.floor(min(p.imag for p in corners)),math.ceil(max(p.imag for p in corners))+1):
   if(x+y-KK)%2:continue
   p=x+y*1j;zz=c+2*p-old[0];ss=F(cross(zz,v),den);tt=F(cross(zz,u),den)
   if not(0<=ss<1 and 0<tt<=1):continue
   nposes+=1
   for A in'FQB':
    dz=tr(raw(A+b1+b2),h=ha);pa=p-dz['p'];assert dz['h']==h;pair=[r]if n==4 else[r,B];before=[status(q,A,pa,ha)for q in pair];end=[status(q,b3,p,h)for q in pair];local=tr(raw(A+b1+b2+b3)+M)
    if local['bad']is not None:why='immutable_local_literal_conflict'
    elif any(q in('R','CORE')for q in before):why='preFOREIGN_same_r_B_before_state_conflict'
    else:
     assert set(before)=={'MISS'}
     if any(q in('R','CORE')for q in end):why='postFOREIGN_r_persistence_candidate_core_or_WHITE'if n==4 else'postFOREIGN_r_B_pair_candidate_core_or_WHITE'
     else:
      assert n==KK==3 and b1 in'DVU'and b2 in'DVU';cb=[status(q,A,pa,ha)for q in(C,bud)]
      if any(q in('R','CORE')for q in cb):why='preFOREIGN_same_C_bud_before_state_conflict'
      else:
       assert set(cb)=={'MISS'}
       if status(C,b3,p,h)in('R','CORE'):why='pinned_original_C_W_rail_candidate_conflict'
       else:assert(b3,p,h)==('U',3+2j,3)and status(bud,b3,p,h)=='R';why='same_bud_W_exit_monotonicity_candidate_WHITE'
    key=(A,b1,b2,b3,n,KK,tuple(xy(pa)+[ha]),tuple(xy(p)+[h]));assert key not in rows;rows[key]=why;classes[why]+=1
assert nposes==165 and len(rows)==495 and dict(classes)==J['exact_disjoint_classification'];assert rows=={(q['foreign'],q['first'],q['second'],q['third'],q['true_preFOREIGN_age'],q['totalK'],tuple(q['foreign_pose']),tuple(q['third_pose'])):q['classification']for q in J['all495_FOREIGN_typed_mask_cases']}
out=dict(status='PASS portable SAME V pair/rail reserves and scoped THIRD old-V true-preforeign ages3/4 closure',manifest=sha(D/'manifest.json'),B_plain_loss_cover=dict(bc),held_r_context_types=dict(rcontext),all12_B_gates=bg,current_young_counts=dict(Counter(young.values())),C_W_roles=cports,bud_W_exits=bports,angle_count=66,pose_count=165,mask_count=495,classification=dict(classes),analytic_review=[
'Independent full RAW+M inventory verifies every old residual CORE capture is a true input or first-WHITE contradiction; C has no input. Genuine V/VC/VCC R4r/R9B/R7C/R16bud identities remain original outside their actual full exitK.',
'The earlier signed PLAIN r cover has only9 noncontact gates, all requiring B already WHITE or ENTRYCORE and never taking B as an external input. Thus neither r-first nor simultaneous r/B CURRENT loss can occur with B held at ENTRY. Fresh96Broles retain all heldr complete-context cases. Any simultaneous external r-input in that set is independently an actual old-source chord contact, already excluded for an earlier loss atom. Other cases are genuine CORE/WHITE. The upperU B gate is retained.',
'With r+B held, current-edge and repaired-FIRSTforeign barriers protect both physical bridge edges. Each actual source FULL tail meets only E; each consumer partial chord meets only Z. Under simplicity THROUGH an earlier loss atom, their arc and held two-edge bridge form Jordan. Correct principal closure is aH-aV, giving TOTALK2, impossible after true preAage>=3. No postforeign maturation or unexecuted consumerCtail is used.',
'Persistence is only to ENTRY of a global FIRST-contact target; its own loss/contact is not assumed simple. CompleteFOREIGN MISS retains identities despite marker core timing; a before-WHITE first read in futureM is an initial-color contradiction, not already executed at foreign RAWexit.',
'Pinned C W loss has only oldV-contact or heldB-WHITE routes. All bud W input consumers have actual RAWexitx<=2, including marker-owned capture, and every subsequent plainW base strictly decreasesx. Thus originalbud survives until candidateheadx3. These are geometry/input arguments afterA, not source-age claims.',
'All66 angle records/165 outgoing-owned poses/495 inverse masks reconstructed from exact endpoints, with n distinct from totalK=n+both returnedC indicators. n4 uses only originalr law5 preA plus signed TOTALr-loss3; n3 uses originalr/B and C/bud preA guarantees followed by literal transfer. All3fullsource tails complete at these ages.',
'Only oldV GLOBAL-FIRST THIRD contact at truepreA3/4 closes; lowerages, oldD and complete THIRD simplicity remain outside this theorem.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
