from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from itertools import product
import json,hashlib,math
P=Path(__file__);R=P.parent.parent;D=R/'second_old_C_age2_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='ff5b8e1bf29425e1ff74fac11c004a4e1cf94b7a6e1c2941aac2f9d507381d9f';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
bp=P.with_name('check_old_V_second_age1_independent.py');ns={'__file__':str(bp)};exec(bp.read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,G,meet,cross=[ns[k]for k in('W','M','K','tr','rot','xy','center','G','meet','cross')]
raw=lambda s:''.join(W[a]for a in s);canon=lambda x:json.dumps(x,sort_keys=True);ref=json.loads((D/'C_age2_first_contact.json').read_text())
def perms(d,v,u):
 if not d+v+u:yield '';return
 for a,n in(('D',d),('V',v),('U',u)):
  if n:
   for s in perms(d-(a=='D'),v-(a=='V'),u-(a=='U')):yield a+s
# Exact boxes from all directed source/target endpoint differences; no position scan bound chosen.
a=center(0j,0);u=center(G['C']['p'],G['C']['h'])-a;geos=[];boxes=[];types=[]
for b1,b2 in product('DCVU',repeat=2):
 if b1=='C'and b2=='U':continue
 N=2+int(b1=='C');h=(2-N)%4;c=center(0j,h);v=center(G[b2]['p']*rot(h),(h+G[b2]['h'])%4)-c;den=cross(u,v);corners=[(a+s*u-c-t*v)/2 for s in(0,1)for t in(0,1)];bounds=[(math.floor(min(z.real for z in corners)),math.ceil(max(z.real for z in corners))),(math.floor(min(z.imag for z in corners)),math.ceil(max(z.imag for z in corners)))];boxes.append({'first':b1,'second':b2,'exact_rational_corners':[[[F(z.real).numerator,F(z.real).denominator],[F(z.imag).numerator,F(z.imag).denominator]]for z in corners],'integer_bounds':[list(z)for z in bounds]})
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
   pose=[x,y,h];geos.append({'first':b1,'second':b2,'second_pose':pose,'old_s':[s.numerator,s.denominator],'new_t':[t.numerator,t.denominator]})
   for A in'FQB':
    disp=tr(W[A]+W[b1],h=2);ap=p-disp['p'];assert disp['h']==h
    if ap.real>-1:continue
    end=tr(W[A],ap,2);bend=tr(W['F'],ap,2);verts=[center(ap,2),center(bend['p'],bend['h'])]
    if A!='F':verts.append(center(end['p'],end['h']))
    if any(meet(a,a+u,l,r)is not None for l,r in zip(verts,verts[1:])):continue
    be=tr(W[b1],end['p'],end['h'])
    if meet(a,a+u,center(end['p'],end['h']),center(be['p'],be['h']))is not None:continue
    if tr(W[A]+W[b1]+W[b2]+M)['bad']:continue
    types.append({'foreign':A,'first':b1,'second':b2,'foreign_pose':[*xy(ap),2],'second_pose':pose})
assert len(boxes)==15 and set(map(canon,boxes))==set(map(canon,ref['all15_exact_remaining_contact_parallelograms']))
assert len(geos)==19 and set(map(canon,geos))==set(map(canon,ref['all19_outgoing_owned_b1_typed_contact_poses']))
assert len(types)==57 and set(map(canon,types))==set(map(canon,ref['all57_local_feasible_source_clear_FOREIGN_alignments']))
cu=tr(W['C']+W['U']+M);assert cu['bad'][:2]==(29,1)
counts=[];words={};maxsize=0
for z in types:
 A,b1,b2=z['foreign'],z['first'],z['second'];x,y,h=z['foreign_pose'];budget=-1-x
 for dw in range(budget+1):
  for vw in range((budget-dw)//3+1):
   for uw in range((budget-dw-3*vw)//4+1):
    left=budget-dw-3*vw-4*uw
    for vs in range(left+1):
     ds=left-vs;num=1+dw+vw-ds-3*vs-y
     if num<0 or num%4:continue
     us=num//4
     if not ds+vs+us:continue
     counts.append(dict(foreign=A,first=b1,second=b2,foreign_pose=z['foreign_pose'],W_counts=dict(D=dw,V=vw,U=uw),S_counts=dict(D=ds,V=vs,U=us)));maxsize=max(maxsize,dw+vw+uw+ds+vs+us)
     for X,Y in product(perms(dw,vw,uw),perms(ds,vs,us)):
      if Y[-1]not in('VU'if A in'FQ'else'U'):continue
      old=tr(raw('C'+X+'C'+Y));assert[*xy(old['p']),old['h']]==z['foreign_pose'];T='C'+X+'C'+Y+A+b1+b2;whole=tr(raw(T)+M);kind='positive'if not whole['bad']else'old_conflict'if old['bad']else'whole_conflict';words[T]=(kind,whole,X,Y,z)
assert len(counts)==438 and maxsize==9 and set(map(canon,counts))==set(map(canon,ref['all438_exact_W_S_endpoint_count_tuples']))and len(words)==1510
sup={''.join(z['tokens']):z for z in ref['all1510_distinct_all_order_body_words']};assert len(sup)==1510 and set(sup)==set(words)
def check_bad(T,t,z):
 i,prev,p,c=t['bad'];w=z['exact_conflict'];assert(i,prev,xy(p),c)==(w['conflict_read'],w['previous_read'],w['cell'],w['turn'])
 for tick,field in((prev,'previous_actual_owner'),(i,'failing_actual_owner')):
  lo=0;found=False;owner=z[field]
  for j,a in enumerate(T):
   if tick<lo+len(W[a]):assert owner['actual_atom_index0']==j and owner['actual_atom']==a and owner['atom_start_tick0']==lo and owner['canonical']['context_tick0']==tick-lo;found=True;break
   lo+=len(W[a])
  if not found:assert owner['actual_atom']=='next actual word'and owner['next_word_tick0']==tick-lo and owner['next_word_read_number1']==tick-lo+1 and owner['turn']==M[tick-lo]
for T,(kind,t,X,Y,z)in words.items():
 assert sup[T]['classification']==kind and ''.join(sup[T]['old_W_run'])==X and ''.join(sup[T]['old_S_run'])==Y
 if kind!='positive':check_bad(T,t,sup[T])
stats=Counter(z[0]for z in words.values());assert stats==ref['exact_word_counts']=={'positive':87,'old_conflict':749,'whole_conflict':674}
controls={''.join(z['tokens']):z for z in ref['all87_actual_complete_prepared_RAW_C_controls']};positive={T for T,z in words.items()if z[0]=='positive'};assert len(controls)==87 and set(controls)==positive
for T,z in controls.items():
 t=words[T][1];B={complex(*p)for p in z['complete_initial_BLACK']};assert B=={p for p,b in t['req'].items()if b}and K<=B and len(B)==z['initial_mass'];cut=None
 for i,(p,h,c)in enumerate(t['reads']):
  assert(p in B)==(c=='L');B.symmetric_difference_update({p})
  if i+1==len(raw(T)):cut=set(B)
 rawexit=tr(raw(T));assert sorted(map(xy,cut))==z['RAW_exit']['complete_BLACK']and[*xy(rawexit['p']),rawexit['h']]==z['RAW_exit']['pose']
 assert sorted(map(xy,B))==z['actual_final_M11_exit']['complete_BLACK']and[*xy(t['p']),t['h']]==z['actual_final_M11_exit']['pose']and len(t['reads'])==z['physical_reads']
roles=[]
for full in('DC','VC','VCC','UC','UCC'):
 for j in range(full.count('C')):
  pref=full[0]+'C'*j;t=tr(raw(pref));roles.append((full,j+1,pref,[*xy(t['p']),t['h']],-j,2+j,full.count('C')-j,full.count('C')==2 and j==0))
assert len(roles)==7
for a,z in zip(roles,ref['all7_real_containing_source_roles']):assert a==(z['containing_full_packet'],z['selected_C_index1'],z['literal_prefix_query'],z['actual_selected_C_pose_in_full_frame'],z['containing_full_entry_clock'],z['containing_full_entry_age_at_FOREIGN'],z['containing_full_completion_clock'],z['mandatory_empty_W_rail'])
queries={(''.join(z['raw_C_body_tokens']),z['literal_containing_prefix']):z for z in ref['all435_necessary_literal_containing_prefix_queries']};assert len(queries)==435
for T,pref in product(sorted(positive),('D','V','U','VC','UC')):
 z=queries[T,pref];trial=pref+T;assert ''.join(z['trial_tokens'])==trial;t=tr(raw(trial)+M);assert t['bad'];check_bad(trial,t,z)
out={'status':'PASS genuine outgoing old-C atomic age2 FIRST SECOND-RAW contact excluded','manifest_sha256':sha(mf),'dependencies':m['dependencies'],'boxes':15,'outgoing_owned_poses':19,'foreign_alignments':57,'endpoint_count_tuples':438,'derived_max_rail_atoms':9,'whole_words':1510,'literal_outcomes':dict(stats),'prepared_complete_controls':87,'necessary_prefix_queries':435,'actual_roles':roles,'analytic_review':['Geometry uses true selected atomic C age2 and effective N=2+[b1=C], never containing-entry age or postforeign maturity. All fifteen exact rational boxes, sector parities, same-direction positive collinear onsets, outgoing old endpoint0<=s<1/new0<t<=1 and earlier foreign/b1 clearance were independently rebuilt. The sixteenth rawCU case fails literally at29 versus1.','After selected C only an arbitrary W rail, one actual C, and arbitrary S rail remain. The bounded target x supplies all W and S-D/V count bounds; y fixes S-U. Every438 tuple and1510 actual all-order words with mandatory final V/U or U are regenerated. Derived maximum9 is a consequence, not a search cap. Zero-length W and mandatory immediate second source tail are retained.','Every1423 immutable conflict is independently replayed with exact actual RAW/following-word ownership. All87 prepared RAW-C positives are actual complete finite boards, replayed through final M11 and both full fields, but not asserted genuine containing sources or simple old histories.','All seven genuine C roles require one of five literal prefixes D,V,U,VC,UC. C1 of VCC/UCC additionally needs empty W; retaining all positive bodies in those necessary-prefix tests is a safe superset. C2 full entry=-1/foreign age3/completion1 is explicit. All435 prefix queries fail on any initial field. No ancestry depth or source-free rawC exclusion is imported.','Only this chronological first second-RAW contact source/atomic-age slice is excluded. Other sources/ages, later returned tails and general second simplicity remain open.']};P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(P),sha(P.with_suffix('.json')))
