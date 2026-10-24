from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction as F
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'first_foreign_three_ordinary_simplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='2e5de83785cd3720f2de465b19a119c931489f01ada037277e70c2ce3b276720';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,tr,pieces,meet,rot,center,xy,cross=[ns[k]for k in('W','M','tr','pieces','meet','rot','center','xy','cross')];raw=lambda ts:''.join(W[a]for a in ts)
J=json.loads((D/'three_ordinary_simplicity.json').read_text());local=[];conflicts=[]
for h,A,b1,b2,b3 in product(range(4),'FQB','DCVU','DCVU','DCVU'):
 ts=A+b1+b2+b3;segments=[(p*rot(h),q*rot(h))for p,q in pieces(ts)];vertices=[xy(segments[0][0])]+[xy(q)for p,q in segments];hits=[]
 for j,(a,b)in enumerate(segments[:-1]):
  c,d=segments[-1];u=b-a;v=d-c;den=cross(u,v);off=c-a
  if den:
   ss,tt=F(cross(off,v),den),F(cross(off,u),den)
   if not(0<=ss<=1 and 0<=tt<=1):continue
   top=tt
  else:
   if cross(off,u):continue
   co=lambda z:int(z.real)if v.real else int(z.imag)
   lo,hi=sorted((F(co(a-c),co(v)),F(co(b-c),co(v))));tt=max(F(0),lo);top=min(F(1),hi)
   if tt>top:continue
   point=c+tt*v;co2=lambda z:int(z.real)if u.real else int(z.imag);ss=F(co2(point-a),co2(u))
  if j==len(segments)-2:assert(ss,tt,top)==(1,0,0)
  else:
   assert not(tt==0 and top>0)
   if tt>0:hits.append((tt,j,ss))
 row=next(z for z in J['all768_rotation_checked_local_closed_segment_interfaces']if(z['heading'],z['foreign'],z['first'],z['second'],z['third'])==(h,A,b1,b2,b3));assert row['true_piece_vertices']==vertices
 if hits:
  t=min(x[0]for x in hits);owners={j+int(s==1)for tt,j,s in hits if tt==t};assert len(owners)==1;owner=owners.pop();assert owner<len(segments)-2
  rr=tr(raw(ts)+M,h=h);fail,prev,q,ch=rr['bad'];start=len(raw(ts[:-1]));assert start<=fail<len(raw(ts))
  assert row['first_local_contact_time']==[t.numerator,t.denominator]and row['outgoing_owner_index0']==owner
  if ts=='FCCV':assert(t,owner,fail-start,ch)==(F(3,4),0,15,'R')
  else:assert ts in('FCCU','QCCU','BCCU')and(t,owner,fail-start,ch)==(F(1,2),len(pieces(A)),12,'L')
  conflicts.append((h,ts,str(t),owner,fail-start,xy(q),ch))
 else:assert 'first_local_contact_time'not in row
 local.append((h,ts))
assert len(local)==768 and len(conflicts)==16
assert Counter(z[1]for z in conflicts)==dict.fromkeys(('FCCV','FCCU','QCCU','BCCU'),4)
marker=[]
for b1,b2,b3 in product('DCVU',repeat=3):
 word=raw(b1+b2+b3)+M;o1=len(W[b1]);o2=o1+len(W[b2]);assert word[o1:o1+11]==M and word[o2:o2+11]==M
 marker.append((b1,b2,b3,min(11,len(W[b3])),max(0,11-len(W[b3]))))
assert len(marker)==64
# Fresh specialization of the signed Jordan source-relative window, not a bound guessed from the catalogue.
rk={'U':0,'V':1,'D':2,'C':2};angles=[]
for old,b1,b2,b3 in product('DCVU',repeat=4):
 for n in range(5):
  N=n+int(b1=='C')+int(b2=='C')
  if old=='C'and n==0:continue
  if N>4 or(N==0 and rk[old]<=rk[b3])or(N==4 and rk[old]>=rk[b3]):continue
  angles.append(dict(old_source=old,first=b1,second=b2,third=b3,true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age=n,first_returned_C_indicator=int(b1=='C'),second_returned_C_indicator=int(b2=='C'),total_ordinary_C_before_third=N,true_FOREIGN_heading_relative_old=(-n)%4,third_heading_relative_old=(2-N)%4))
canon=lambda x:json.dumps(x,sort_keys=True);original=json.loads((R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json').read_text())['all831_conditional_preFOREIGN_old_source_angle_interfaces'];assert len(angles)==len(set(map(canon,angles)))==831 and set(map(canon,angles))==set(map(canon,original))
for i,row in enumerate(J['all831_original_angle_IDs_and_exact_source_exclusions']):assert row['original831_angle_index0']==i and row['exact_original_angle']==original[i]
counts=Counter(a['old_source']for a in angles);assert counts=={'D':206,'C':160,'V':229,'U':236}
load=lambda p:json.loads((R/p).read_text())
C=load('third_old_C_monotone_reserves_2026-10-24/old_C_third_closure.json');U=load('old_U_third_source_join_2026-10-24/U_third_join.json');V=load('old_V_third_source_join_2026-10-24/V_third_join.json')
for old,claimed in [('C',[x['exact_original_angle']for x in C['all160_exact_original_C_angle_boxes']]),('U',U['all236_signed_old_U_angle_rows']),('V',[x['angle']for x in V['all229_exact_V_angle_routes']])]:assert len(claimed)==len(set(map(canon,claimed)))and set(map(canon,claimed))=={canon(a)for a in angles if a['old_source']==old}
# D's old source certificate stores mask keys, not exact angle objects. Reconstruct every rational box and full-source key.
D0=load('old_D_third_young_endpoint_2026-10-24/D_third_young_endpoint.json');D3=load('old_D_third_age3_beta_loss_2026-10-24/D_third_age3_beta_loss.json');old=pieces('D')[0];u=old[1]-old[0];dkeys=set();geo=0
for ag in angles:
 if ag['old_source']!='D':continue
 n=ag['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age'];N=ag['total_ordinary_C_before_third'];h=ag['third_heading_relative_old'];ha=ag['true_FOREIGN_heading_relative_old'];b1,b2,b3=(ag[k]for k in('first','second','third'));zz=tr(W[b3],h=h);c=center(0,h);v=center(zz['p'],zz['h'])-c;den=cross(u,v);corners=[(old[0]+s*u-c-t*v)/2 for s,t in product((0,1),repeat=2)]
 for x in range(math.floor(min(q.real for q in corners)),math.ceil(max(q.real for q in corners))+1):
  for y in range(math.floor(min(q.imag for q in corners)),math.ceil(max(q.imag for q in corners))+1):
   if(x+y-N)%2:continue
   p=x+y*1j;off=c+2*p-old[0]
   if den:ss,tt=F(cross(off,v),den),F(cross(off,u),den)
   else:
    if cross(off,u):continue
    co=lambda z:int(z.real)if u.real else int(z.imag);ratio=F(co(v),co(u));q=F(co(off),co(u));assert ratio>0
    if q>=0:continue
    ss,tt=F(0),-q/ratio
   if not(0<=ss<1 and 0<tt<=1):continue
   geo+=1
   for A in'FQB':
    z=tr(raw(A+b1+b2),h=ha);pa=p-z['p'];assert z['h']==h
    for source,nxt in [('DC',None)]+[('D',s)for s in('D','DC','V','VC','VCC','U','UC','UCC')]:dkeys.add((n,b1,b2,b3,A,tuple(xy(pa)+[ha]),tuple(xy(p)+[h]),source,nxt))
key=lambda r:(r['n'],r['b1'],r['b2'],r['b3'],r['A'],tuple(r['pa']),tuple(r['p3']),r['source'],r['nextfull'])
assert geo==293 and len(dkeys)==7911 and dkeys==set(map(key,D0['typed_rows']))
assert{r for r in dkeys if r[0]==3}==set(map(key,D3['typed_rows']))and len(D3['typed_rows'])==1458
assert dkeys=={tuple(x[:5])+tuple(map(tuple,x[5:7]))+tuple(x[7:])for x in J['direct7911_genuine_old_D_source_nextFULL_keys']}
assert not any(r['why']=='NECESSARY'and r['n']==2 for r in D0['typed_rows'])
# Bound mandatory qualifications explicitly, including the independent correction to earlier prose.
for f in ['old_V_third_young_complete_ancestry_2026-10-24/mandatory_qualifications_manifest.json','old_V_third_young_complete_ancestry_2026-10-24/collinear_metadata_qualification_manifest.json','audits/check_old_V_third_young_contact_qualification_independent.json','V_postforeign_pair_rail_reserve_2026-10-24/simultaneous_input_qualification_manifest.json','second_contact_signed_obligations_2026-10-24/core_status_qualification_manifest.json']:assert f in mf['dependencies']
out=dict(status='PASS actual U-entry G8 prefix, FIRST foreign and exactly THREE immediate ordinary RAW atoms with actual final M11 have a SIMPLE OPEN corrected-center proxy',manifest_sha256=sha(MF),script_sha256=sha(S),dependencies=mf['dependencies'],rotated_local_cases=768,actual_RAW_local_conflicts=conflicts,actual_marker_supplies=marker,original_angles=831,source_counts=dict(counts),independently_rebuilt_D_outgoing_geometries=293,actual_D_full_source_keys=7911,D_age3_keys=1458,analytic_review=[
'The signed two-RAW simple prefix is actual: b3 plus only its real following final prefix supplies the required M11, including D10 using exactly one real next read. Internal Q/B F56 bends are geometric pieces, not new marked cores.',
'All closed local segment contacts were recomputed in all four headings. The new third chord meets b2 only at genuine adjacency, including collinear singleton adjacency, and no nonadjacent positive overlap starts at its entry. The four remaining local types fail within actual third RAW, never in a hypothetical future marker. QCCU tail overlap begins at the outgoing b1C-owned vertex and is retained.',
'After those local removals, compactness of the finite already-simple old arc gives a first positive new contact. Every old interior or initial vertex is included; an internal vertex is assigned its actual outgoing atom. The old terminal is the foreign entry and is already locally excluded. At same-direction overlap the first onset is kept; opposite-direction entry would have met the outgoing segment earlier. New terminal t=1 remains included. Thus genuine source ownership is exactly 0<=s<1, 0<t<=1.',
'The actual old subarc and new prefix to first contact form the Jordan loop required by the separately signed repaired turn window. True preforeign n and both returned C indicators are kept separate; actual previous-C bit zero follows the signed full-eight/foreign adjacency. This yields exactly the freshly reconstructed831 necessary keys, not an assumed unrestricted-tail law.',
'All831 original IDs bind disjoint source exclusions D206/C160/V229/U236. D independently rebuilt293 rational outgoing poses and all7911 genuine D/DC-nextFULL keys, with exact1458 age3 subset. C retains seven real containing roles and true C2 shifts. V binds both mandatory young collinear/prose and simultaneous-r qualifications. U retains actual creating-family tails and same-original identity obligations. Each exclusion has the same chronological FIRST contact premise.',
'The source claims exclude eligible U-entry ancestry containing the selected source; later internal U in prepared positive words is not falsely treated as such ancestry. Original prepared positives remain valid. Young-V180 ordinary collinear joins are legitimate adjacency; the withdrawn earlier-contact prose is not a premise. Nine simultaneous-r input rows are geometric contact alternatives, not color conflicts.',
'CURRENT is external ledger status, not physical death; old identities may remain alive in CORE. All producer-age facts end before FOREIGN unless a separate physical transfer proves more. Actual fourth-RAW erosion controls and the withdrawn full-output seal remain untouched. This is a three-RAW theorem only, not an iterative seal.'
],not_claimed=['fine-walk selfavoidance','fourth ordinary RAW','completion of later C tails','second foreign','arbitrary-tail simplicity','global seven-atom coverage','global capture'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
