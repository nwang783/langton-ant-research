from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from itertools import product
import json,hashlib,math
P=Path(__file__);R=P.parent.parent;D=R/'second_old_sources_age2_bud_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='807e78d3c21b66fc8aa573bf1bd47c069f0d6354739ab67c65d2c612835836f3';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
bp=P.with_name('check_old_V_second_age1_independent.py');ns={'__file__':str(bp)};exec(bp.read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,G,meet,cross=[ns[k]for k in('W','M','K','tr','rot','xy','center','G','meet','cross')]
raw=lambda s:''.join(W[a]for a in s);canon=lambda z:json.dumps(z,sort_keys=True);ref=json.loads((D/'age2_incoming_bud.json').read_text());beta=1-1j;boxes=[];poses=[];rows=[]
def owner(T,t,o):
 lo=0
 for j,a in enumerate(T):
  if t<lo+len(W[a]):
   assert o['actual_atom_index0']==j and o['actual_atom']==a and o['atom_start_tick0']==lo and o['canonical']['context_tick0']==t-lo
   return
  lo+=len(W[a])
 assert o['actual_atom']=='next actual word'and o['next_word_tick0']==t-lo and o['next_word_read_number1']==t-lo+1 and o['turn']==M[t-lo]
sup={(z['old_source'],z['first'],z['second'],tuple(z['second_pose']),z['foreign']):z for z in ref['all186_foreign_typed_context_rows']};assert len(sup)==186
for old in'DCV':
 a=center(0j,0);u=center(G[old]['p'],G[old]['h'])-a
 for b1,b2 in product('DCVU',repeat=2):
  if b1=='C'and b2=='U':continue
  N=2+(b1=='C');h=(2-N)%4;c=center(0j,h);v=center(G[b2]['p']*rot(h),(h+G[b2]['h'])%4)-c;den=cross(u,v)
  cs=[(a+s*u-c-t*v)/2 for s in(0,1)for t in(0,1)];bounds=[(math.floor(min(z.real for z in cs)),math.ceil(max(z.real for z in cs))),(math.floor(min(z.imag for z in cs)),math.ceil(max(z.imag for z in cs)))];boxes.append(dict(old_source=old,first=b1,second=b2,rational_corners=[[[F(z.real).numerator,F(z.real).denominator],[F(z.imag).numerator,F(z.imag).denominator]]for z in cs],integer_bounds=[list(z)for z in bounds]))
  for x in range(bounds[0][0],bounds[0][1]+1):
   for y in range(bounds[1][0],bounds[1][1]+1):
    if(x+y-N)%2:continue
    p=complex(x,y);z=c+2*p-a
    if den:
     s,t=F(cross(z,v),den),F(cross(z,u),den)
     if not(0<=s<1 and 0<t<=1):continue
    else:
     if cross(z,u):continue
     axis=(lambda z:int(z.real))if u.real else(lambda z:int(z.imag));q,mul=F(axis(z),axis(u)),F(axis(v),axis(u));assert mul>0
     if q>=0:continue
     s,t=F(0),-q/mul
     if not 0<t<=1:continue
    pose=[x,y,h];poses.append(dict(old_source=old,first=b1,second=b2,second_pose=pose,old_s=[s.numerator,s.denominator],new_t=[t.numerator,t.denominator]))
    for A in'FQB':
     disp=tr(raw(A+b1),h=2);ap=p-disp['p'];assert disp['h']==h
     ee=tr(W[A],ap,2);ff=tr(W['F'],ap,2);verts=[center(ap,2),center(ff['p'],ff['h'])]
     if A!='F':verts.append(center(ee['p'],ee['h']))
     bbe=tr(W[b1],ee['p'],ee['h']);T=A+b1+b2;tt=tr(raw(T)+M)
     z=sup[old,b1,b2,tuple(pose),A];assert z['foreign_pose']==[*xy(ap),2]and z['true_preforeign_age']==2 and z['effective_geometric_N']==N
     if any(meet(a,a+u,l,r)is not None for l,r in zip(verts,verts[1:])):cl='foreign_already_contacts_source'
     elif meet(a,a+u,center(ee['p'],ee['h']),center(bbe['p'],bbe['h']))is not None:cl='first_return_already_contacts_source'
     elif tt['bad']:cl='immutable_local_context'
     else:
      local=(beta-ap)/rot(2);first=next(((ch,i)for i,(q,hh,ch)in enumerate(tt['reads'])if q==local),None);assert xy(local)==z['incoming_beta_FOREIGN_local']and(list(first)if first else None)==z['actual_combined_first_read']
      cl='CURRENT_beta_in_foreign_entry_core'if local in K else'CURRENT_beta_before_WHITE'if first and first[0]=='R'else'necessary_residue_only'
      if cl=='CURRENT_beta_before_WHITE':owner(T,first[1],z['actual_first_read_owner'])
     assert cl==z['classification'];rows.append((old,A,b1,b2,tuple(z['foreign_pose']),tuple(pose),cl))
assert len(boxes)==45 and set(map(canon,boxes))==set(map(canon,ref['all45_exact_angle_contact_boxes']))
assert len(poses)==62 and set(map(canon,poses))==set(map(canon,ref['all62_outgoing_owned_contact_poses']))
stats=Counter(z[-1]for z in rows);assert stats==ref['exact_row_classification']and len(rows)==186
res=[z for z in rows if z[-1]=='necessary_residue_only'];assert set((z[0],z[1],z[4],z[5])for z in res)=={('V','B',(-2,-4,2),(1,2,3)),('V','F',(-2,-2,2),(2,1,3))}
assert all(z[-1]=='CURRENT_beta_before_WHITE'for z in rows if z[0]in'DC')
roles=[]
for prev,z in zip(('D','DC','V','VC','VCC','U','UC','UCC'),ref['all8_actual_previous_full_FINAL_bud_roles_for_D_V_sources']):
 t=tr(raw(prev));q=t['p']+beta*rot(t['h']);assert t['last'][q]==('R',len(raw(prev))-2)and q not in{t['p']+x*rot(t['h'])for x in K};c=prev.count('C');assert(z['previous_actual_full'],z['previous_full_entry_clock'],z['previous_final_atomic_EXIT_clock'],z['post_EXIT_age_at_FOREIGN'],z['actual_full_entry_age_at_FOREIGN'],z['full_output_cell'],z['actual_final_R_tick0'])==(prev,-c,0,2,2+c,xy(q),len(raw(prev))-2);roles.append((prev,-c,2+c))
internal=[]
for full in('DC','VC','VCC','UC','UCC'):
 for j in range(full.count('C')):
  pref=full[0]+'C'*j;t=tr(raw(pref));q=t['p']+beta*rot(t['h']);f=tr(raw(full));tick=len(raw(pref))-2;assert f['last'][q]==('R',tick)and q not in{f['p']+x*rot(f['h'])for x in K};internal.append((full,j+1,pref,[*xy(t['p']),t['h']],-j,2+j,full.count('C')-j,xy(q),tick))
assert len(internal)==7
for a,z in zip(internal,ref['all7_actual_internal_C_previous_BASE_C1_bud_roles']):assert a==(z['containing_actual_full'],z['selected_C_index1'],z['actual_prefix_before_selected_C'],z['actual_selected_C_pose'],z['containing_full_entry_clock'],z['containing_full_entry_age_at_FOREIGN'],z['containing_full_completion_clock'],z['beta_in_actual_full_frame'],z['actual_beta_R_tick0'])and z['actual_previous_atomic_EXIT_clock']==0 and z['post_EXIT_age_at_FOREIGN']==2
assert tr(W['C']+W['U']+M)['bad'][:2]==(29,1)
out={'status':'PASS old D/C/V true age-two incoming atomic EXIT bud interface','manifest_sha256':sha(mf),'dependencies':m['dependencies'],'boxes':45,'poses_by_old_source':dict(Counter(z['old_source']for z in poses)),'classification':dict(stats),'residues':res,'previous_final_roles':roles,'internal_C_roles':internal,'analytic_review':['Rebuilt all exact rational endpoint boxes, outgoing source half-open/new positive ownership, parity and parallel positive onsets; all foreign and first-return pieces are tested before the second contact. No scan cutoff is imposed.','The actual preceding atomic EXIT exists for each old D/V in a U-entry factor and for all seven genuine internal C roles. Signed1325 measures postEXIT age2, not the previous full-entry age. All eight final and seven internal roles are reconstructed literally; own selected/later C tails preserve the same last-R bud outside exit core. C2 has containing-full age3.','The signed atomic EXIT minimum3 protects the current external identity up to foreign ENTRY only, including prevention of earlier input/core absorption. The later contradiction is the combined first requirement of WHITE, not a postforeign maturity claim. All174 witnesses and their RAW or actual following-word read ownership are checked directly.','Every D57 and C57 placement is excluded. V72 has60 beta-WHITE and10 earlier-contact exclusions, leaving exactly two necessary residues. No attainment, later-tail simplicity, or arbitrary-language conclusion follows.']};P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],dict(stats));print(sha(P),sha(P.with_suffix('.json')))
