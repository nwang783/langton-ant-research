from pathlib import Path
from itertools import product
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'old_V_third_age2_genuine_field_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='9d08fdee0f915412c738a808b03729be4fd5e9b32f0aef8a81e44295cd023bf1'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'age2_field.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,G,rot,center,xy,meet,pieces,cross=[ns[k]for k in('W','M','K','tr','G','rot','center','xy','meet','pieces','cross')];raw=lambda seq:''.join(W[a]for a in seq);full=('D','DC','V','VC','VCC','U','UC','UCC')
def inv(s):
 z=tr(raw(s));ct=tr(raw(s)+M);ek={z['p']+rot(z['h'])*q for q in K};ii={q for q,b in ct['req'].items()if b and q not in K};oo={q for q,(c,t)in z['last'].items()if c=='R'and q not in ek}
 for q in ek-K:assert q in ct['req']and(q in ii or ct['req'][q]is False)
 return z,ct,ii,oo,ek
I={s:inv(s)for s in full};fixed={0j,1,2,2+1j,2+2j,1-1j};AA=1j;beta=1-1j
for src in('V','VC','VCC'):
 assert beta not in I[src][0]['req']and fixed-{beta}|{AA}<=I[src][3]
 for q,t in[(0j,4),(1,9),(2,8),(2+1j,7),(2+2j,16),(AA,11)]:assert I[src][0]['last'][q]==('R',t)
 assert src.count('C')<=2
prior=[]
for s in full:
 z=I[s][0];slot=z['p']+rot(z['h'])*beta;assert slot in I[s][3]and z['last'][slot]==('R',len(raw(s))-2)
 row=next(z for z in J['all8_genuine_previous_full_final_EXIT_bud_roles']if z['actual_previous_full']==s)
 assert row['previous_full_ENTRY_clock']==-s.count('C')and row['actual_full_ENTRY_age_at_FOREIGN']==2+s.count('C')and row['actual_final_atomic_EXIT_clock']==0 and row['true_post_EXIT_age_at_FOREIGN']==2 and row['actual_previous_full_output_slot']==xy(slot)
 prior.append((s,xy(slot),-s.count('C'),2+s.count('C')))
helper={4j-q for q in I['V'][3]};assert helper=={4j,3j,-1+4j,-2+4j,-2+3j,-2+2j}
assert helper=={complex(*z['SAME_genuine_helper_output_cell'])for z in J['all6_genuine_helper_R_output_facts']}
for z in J['all6_genuine_helper_R_output_facts']:
 q=complex(*z['helper_base_output_slot']);assert I['V'][0]['last'][q]==('R',z['helper_R_tick0'])and z['helper_R_read_number1']==z['helper_R_tick0']+1
query=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text());assert min(z['certified_minimum_C_age']for z in query['slots'].values())>=2
angles=[a for a in json.loads((R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json').read_text())['all831_conditional_preFOREIGN_old_source_angle_interfaces']if a['old_source']=='V'and a['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age']==2];assert len(angles)==62
old=pieces('V')[0];u=old[1]-old[0];rows={};poses=0;classes=Counter();kinds=Counter()
def key(row):return(row['foreign'],row['first'],row['second'],row['third'],row['totalK'],tuple(row['foreign_pose']),tuple(row['third_pose']))
cert={key(z):z for z in J['all411_FOREIGN_typed_two_branch_before_mask_cases']};assert len(cert)==411
def hits(cells,local,p,h):
 ans=[]
 for q in cells:
  v=(q-p)/rot(h)
  if v in K:ans.append((tuple(xy(q)),'CORE',None))
  elif local['req'].get(v)is False:
   tick=next(i for i,(a,hh,c)in enumerate(local['reads'])if a==v);ans.append((tuple(xy(q)),'WHITE',tick))
 return set(ans)
for a in angles:
 b1,b2,b3=a['first'],a['second'],a['third'];KK=2+(b1+b2).count('C');h=(2-KK)%4;ha=2;assert KK==a['total_ordinary_C_before_third']and(h,ha)==(a['third_heading_relative_old'],a['true_FOREIGN_heading_relative_old'])
 z=tr(W[b3],h=h);c=center(0,h);v=center(z['p'],z['h'])-c;den=cross(u,v);corners=[(old[0]+s*u-c-t*v)/2 for s,t in product((0,1),repeat=2)]
 for x in range(math.floor(min(q.real for q in corners)),math.ceil(max(q.real for q in corners))+1):
  for y in range(math.floor(min(q.imag for q in corners)),math.ceil(max(q.imag for q in corners))+1):
   if(x+y-KK)%2:continue
   p=x+y*1j;off=c+2*p-old[0]
   if den:ss,tt=F(cross(off,v),den),F(cross(off,u),den)
   else:
    assert b3=='V'and KK==2 and v==u
    if cross(off,u):continue
    ss=F(0);tt=-F(int(off.real),int(u.real))
   if not(0<=ss<1 and 0<tt<=1):continue
   poses+=1;kinds['transverse'if den else'parallel onset']+=1
   for A in'FQB':
    dz=tr(raw(A+b1+b2),h=ha);pa=p-dz['p'];assert dz['h']==h;tokens=A+b1+b2+b3;local=tr(raw(tokens)+M);kk=(A,b1,b2,b3,KK,tuple(xy(pa)+[ha]),tuple(xy(p)+[h]));r=cert[kk]
    assert str(ss)==r['old_s']and str(tt)==r['third_t']
    why='immutable_local_literal_conflict'if local['bad']is not None else'both_genuine_before_FOREIGN_A_states_excluded'
    assert why==r['classification'];classes[why]+=1;rows[kk]=why
    if local['bad']is None:
     for cells,label in[(fixed|{AA},'original_A_CURRENT_branch'),(fixed|helper,'original_A_absent_FORCED_genuine_plainV_helper_branch')]:
      actual=hits(cells,local,pa,ha);assert actual
      supplied={(tuple(z.get('SAME_CURRENT_cell',z.get('SAME_preFOREIGN_BLACK_cell'))),'CORE'if'ENTRY core'in z['contradiction']else'WHITE',z.get('combined_tick0'))for z in r[label]};assert actual==supplied
      for z in r[label]:
       if 'combined_tick0'not in z:continue
       t=z['combined_tick0'];start=0
       for index,atom in enumerate(tokens):
        if t<start+len(W[atom]):owner=z['actual_owner'];assert owner['actual_atom_index0']==index and owner['actual_atom']==atom;break
        start+=len(W[atom])
       else:assert z['actual_owner']['actual_atom']=='next actual word'and z['actual_owner']['tick0']==t-start and z['actual_owner']['turn']==M[t-start]
assert poses==137 and len(rows)==411 and classes==Counter(immutable_local_literal_conflict=105,both_genuine_before_FOREIGN_A_states_excluded=306)
out=dict(status='PASS oldV THIRD true-prefage2 genuine two-field closure only',manifest=sha(MF),source_full_types=['V','VC','VCC'],genuine_prior_EXIT_roles=prior,helper_current_output_cells=sorted(map(xy,helper)),angles=62,poses=poses,contact_kinds=dict(kinds),mask_count=len(rows),classification=dict(classes),analytic_review=[
'OldV is noninitial in genuineU-family-start complete8 factor, so an actual previous FULL packet exists. All8 full types have genuine fresh final atomic EXIT beta at their actual len-2 R; full-entry clock minus ownCcount and postEXIT0 are distinguished. The oldV RAW and both possible ownCtails literally miss beta, so signed postEXIT min3 protects it at foreignclock2.',
'Five fixed same base outputs r/B/common/C/bud are external CURRENT at preFOREIGN2 under their signed minima/query guards. Actual V/VC/VCC source completion is0/1/2 and own tails preserve the exact birth identities. Young facts are used ONLY beforeFOREIGN.',
'If originalA is notCURRENT, signed earliest loss supplies actual V/VC helper0,4S atclock2. Complete-beforeFOREIGNclock2 excludes helperVC and all unfinished tails; actual plainV six outputs are fresh current at age0 by min2. No assumption that oldA physically died or isWHITE is made; it may be aliveCORE at FOREentry.',
'Independent full I/O inventories cover residual-to-CORE absorption, exact62 angle/parallelogram domains and137 outgoing-owned poses include parallel first positive onset with old s0. True n2 and totalK2+returnedCcount are distinct. All411 inverse masks and physical first-R/actualM ownership checked;105 local contradictions and306 cuts in BOTH genuine fields, not hypothetical arbitrary masks.',
'All3full source types share the proved fields. This closes only oldV THIRD truepreA2, not other ages/sources or fullTHIRDsimplicity; no postA age or A-death identification.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
