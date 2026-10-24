from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math
S=Path(__file__).resolve();R=S.parents[1];D=R/'second_old_D_age1_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();man=D/'manifest.json';assert sha(man)=='e7297345939ce70cd22d41bd678e9b5c0d35d0bb8e5a6a0d3e91b5a206394b0e';m=json.loads(man.read_text())
for p,h in m['files'].items():assert sha(D/p)==h
for p,h in m['dependencies'].items():assert sha(R/p)==h
ref=json.loads((D/'D_age1_first_contact.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,V,xy,rot,center,cross,tr,G,meet,pieces=[ns[k]for k in('W','M','K','V','xy','rot','center','cross','tr','G','meet','pieces')]
G8=('D','DC','V','VC','VCC','U','UC','UCC');roles=[]
for P in G8:
 word=''.join(W[a]for a in P);t=tr(word);beta=t['p']+(1-1j)*rot(t['h']);ek={t['p']+z*rot(t['h'])for z in K};assert t['last'][beta]==('R',len(word)-2)and beta not in ek;c=P.count('C');roles.append(dict(previous_full=P,ownCs=c,previous_full_entry_clock=-c,full_source_age_at_FOREIGN=1+c,actual_post_EXIT_age_at_FOREIGN=1,original_beta_full_output=xy(beta),actual_last_R_tick0=len(word)-2))
assert roles==ref['all8_actual_previous_full_FINAL_bud_roles']
for src in('D','DC'):
 t=tr(''.join(W[a]for a in src));assert t['last'][2+0j]==('R',8)
# Independently enumerate all16 exact contact boxes, including same-direction collinear first onset.
a=-1-1j;u=2+2j;geo=[];already=[]
for b1 in'DCVU':
 N=1+(b1=='C');h=(2-N)%4
 for b2 in'DCVU':
  c=center(0j,h);z=G[b2];v=center(z['p']*rot(h),(h+z['h'])%4)-c;den=cross(u,v);corners=[(a+s*u-c-t*v)/2 for s in(0,1)for t in(0,1)]
  for x in range(math.floor(min(z.real for z in corners)),math.ceil(max(z.real for z in corners))+1):
   for y in range(math.floor(min(z.imag for z in corners)),math.ceil(max(z.imag for z in corners))+1):
    if(x+y+h)%2:continue
    q=complex(x,y);zz=c+2*q-a
    if den:
     s=F(cross(zz,v),den);t=F(cross(zz,u),den)
     if not(0<=s<1 and 0<t<=1):continue
    else:
     if cross(zz,u):continue
     start=F(int(zz.real),int(u.real));mul=F(int(v.real),int(u.real));assert mul>0
     if 0<=start<1:already.append((b1,b2,x,y,h));continue
     if start>=1:continue
     s=F(0);t=-start/mul
     if not(0<t<=1):continue
    geo.append(dict(first=b1,second=b2,second_pose=[x,y,h],old_s=[s.numerator,s.denominator],new_t=[t.numerator,t.denominator]))
canon=lambda z:json.dumps(z,sort_keys=True);assert len(geo)==23 and set(map(canon,geo))==set(map(canon,ref['all23_b1_typed_contact_poses']))
rows=[];rem=[]
for z in geo:
 b1,b2=z['first'],z['second'];p2=complex(*z['second_pose'][:2])
 for A in'FQB':
  dp=tr(W[A]+W[b1],h=3);pa=p2-dp['p'];full=tr(W[A]+W[b1]+W[b2]+M);why='keep'
  if full['bad']:why='local_conflict'
  else:
   for guard in(2+0j,1-1j):
    loc=(guard-pa)/rot(3)
    if loc in K:why='guardian_in_A_K';break
    if full['req'].get(loc)is False:why='guardian_before_WHITE';break
  row=dict(foreign=A,first=b1,second=b2,foreign_pose=[*xy(pa),3],second_pose=z['second_pose'],classification=why);rows.append(row)
  if why=='keep':rem.append(row)
assert len(rows)==69 and Counter(z['classification']for z in rows)=={'keep':45,'guardian_before_WHITE':18,'local_conflict':6};assert set(map(canon,rows))==set(map(canon,ref['all69_foreign_alignments']))
def perms(d,v,u):
 cnt={'D':d,'V':v,'U':u};out=[]
 def go(pre):
  if sum(cnt.values())==0:out.append(pre);return
  for a in'DVU':
   if cnt[a]:cnt[a]-=1;go(pre+a);cnt[a]+=1
 go('');return out
counts=[];words={}
for z in rem:
 A,b1,b2=z['foreign'],z['first'],z['second'];x,y,h=z['foreign_pose'];rhs=y-2
 for dn in range(max(rhs+1,0)):
  for vn in range(max(rhs//3+1,0)):
   for un in range(max(rhs//4+1,0)):
    left=rhs-dn-3*vn-4*un
    if left<0:continue
    for dw in range(left+1):
     vw=left-dw;num=1+dn+vn-dw-3*vw-x
     if num<0 or num%4:continue
     uw=num//4
     if dw+vw+uw==0:continue
     counts.append(dict(foreign=A,first=b1,second=b2,foreign_pose=z['foreign_pose'],second_pose=z['second_pose'],dN=dn,vN=vn,uN=un,dW=dw,vW=vw,uW=uw))
     for X in perms(dn,vn,un):
      for Y in perms(dw,vw,uw):
       if Y[-1]not in('VU'if A in'FQ'else'U'):continue
       seq='D'+X+'C'+Y+A+b1+b2;old=tr(''.join(W[a]for a in'D'+X+'C'+Y));alltr=tr(''.join(W[a]for a in seq)+M)
       if old['bad']:why='old_literal_conflict'
       else:
        assert all(p not in(2+0j,1-1j)for p,h,c in old['reads'][10:]);why='full_literal_conflict'if alltr['bad']else'FULL_FEASIBLE_PREPARED_D_ENTRY'
       words[seq]=why
assert len(counts)==142 and set(map(canon,counts))==set(map(canon,ref['exact142_endpoint_count_solutions']));assert len(words)==347 and Counter(words.values())==ref['word_classification'];assert words=={''.join(z['tokens']):z['classification']for z in ref['all347_exact_whole_words']}
positives=sorted(w for w,c in words.items()if c=='FULL_FEASIBLE_PREPARED_D_ENTRY');assert len(positives)==42 and Counter('DC'if w.startswith('DC')else'D'for w in positives)=={'DC':22,'D':20}and sum('U'in w for w in positives)==36
# Fresh physical replays of all42 base boards INCLUDING unread prepared beta, and all42 D-prepended boards.
controls=[]
for group,addbeta in(('all42_complete_prepared_D_entry_controls',True),('all42_complete_D_prepend_controls',False)):
 for z in ref[group]:
  seq=''.join(z['tokens']);raw=''.join(W[a]for a in seq);t=tr(raw+M);assert t['bad']is None;seed={p for p,c in t['req'].items()if c};
  if addbeta:seed.add(1-1j)
  assert seed=={complex(*p)for p in z['complete_initial_black']};B=set(seed);rawcut=None
  for i,(p,h,c)in enumerate(t['reads']):
   assert(p in B)==(c=='L');B.symmetric_difference_update({p})
   if i+1==len(raw):rawcut=set(B)
  assert rawcut=={complex(*p)for p in z['RAW_exit']['complete_black']}and B=={complex(*p)for p in z['actual_M11_exit']['complete_black']};assert[*xy(t['p']),t['h']]==z['actual_M11_exit']['head'];controls.append(dict(word=seq,seed_mass=len(seed),all_fine_reads=len(t['reads']),full_final_mass=len(B),prepared_beta=addbeta))
# Stronger atomic reverse superlanguage: all7, not merely full8. Natural closure only.
closure=[];querymap={}
for seq in positives:
 todo=[seq];seen=set();edges=[]
 while todo:
  w=todo.pop();assert w not in seen;seen.add(w);allow=[]
  for a in'DCVUFQB':
   trial=a+w;t=tr(''.join(W[c]for c in trial)+M);ok=t['bad']is None;querymap[(w,a)]=ok
   if ok:allow.append(a);todo.append(trial)
  edges.append((w,allow))
 assert edges==[(seq,['D']),('D'+seq,[])];closure.append(edges)
assert len(querymap)==588 and sum(querymap.values())==42 and len({w for w,a in querymap})==84
for row in ref['all588_closed_seven_atom_reverse_queries']:
 label=row['suffix_node'];w='D'+label[2:]if label.startswith('D+')else label;assert querymap[w,row['predecessor']]==row['feasible']
out=dict(status='PASS exact old-D true-age1 SECOND first-contact slice excluded for U-entry history',manifest=sha(man),signed_atomic_exit_report=sha(S.with_name('check_atomic_exit_bud_independent.json')),signed_atomic_common_report=sha(S.with_name('check_atomic_common_four_C_independent.json')),all8_actual_FINAL_predecessor_roles=roles,contact_geometries=geo,already_old_parallel_starts=already,classification_counts=dict(Counter(z['classification']for z in rows)),count_solution_count=142,wholeword_counts=dict(Counter(words.values())),prepared_controls=controls,all84_natural_reverse_nodes=closure,analytic_review=[
'The selected oldD is after the original U-family factor entry, hence has an actual previous atom. Because it is a base/fullpacket boundary, only the FINAL atomic roles of the eight real predecessor packets apply. Each full predecessor with c ownCs starts at -c; foreign full-source age is1+c, but actual postEXIT age is exactly1. Fresh full output beta at lastR length-2 and the inverse normalization to(1,-1) are reconstructed. Signed1325 is used at postEXIT1, not a reset fullsource clock.',
'SelectedD common t=(2,0) is actualR8 and preserved by its own optionalC. Signed common and exit-bud laws hold only before foreignA. Complete A+b1+b2+actualM entry masks retain later rewrites, giving18 guardianWHITE cuts and6 intrinsic conflicts among69 alignments.',
'Exact sixteen head parallelograms, active sector, outgoing0<=s<1/new0<t<=1 and positive collinear onset independently give23 typed contact poses. Starts already on oldD are excluded by signed prior one-return simplicity; terminal oldD belongs to its true following atom. No second simplicity premise.',
'Every age1 body has actualD,X_N,C1,Y_W. EmptyX means selectedDC; nonemptyX means selectedplainD and genuine FIRSTtail of the last X base. Nonnegative y equation bounds all counts exceptuW, fixed byx. All142 relaxed nonempty-W count solutions, then actual lastVU/U filtering and every multiset order give347 distinct whole words.145 oldRAW and160 wholeRAW/M conflicts leave42 prepared positives.',
'All84 complete finite boards,42 base plus42D-prefix, are freshly replayed at every read with full raw/M exits. Prepared unread beta remains explicitly black on base controls. These controls are not promoted here to proxy-simple U-entry trajectories; their literal feasibility is retained.',
'All seven atomic predecessors are tested at every naturally reached suffix, a superlanguage covering every possible full-eight predecessor. Each base permits onlyrawD, each D extension none:84 distinct nodes588queries42edges, no cutoff. This closes earlier U ancestry of the selectedD for every exhausted body.36 positives do contain laterU, whose subfactor does not contain that selected firstD.',
'Only the true age1 oldD outgoing-source branch is excluded. OtherD ages, oldC/V branches, general second simplicity and global capture remain open.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(Counter(words.values()),'physical',len(controls),'queries',len(querymap))
