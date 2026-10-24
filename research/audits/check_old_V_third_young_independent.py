from pathlib import Path
from itertools import product
from fractions import Fraction as F
from collections import Counter
from functools import lru_cache
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'old_V_third_young_complete_ancestry_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='4d13250d51eba9f6ad0c5c653f4bac2ea6a9eaa704d7990ffdea5d31371df59f'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'young_ancestry.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,rot,center,xy,meet,pieces,cross=[ns[k]for k in('W','M','K','tr','rot','center','xy','meet','pieces','cross')];raw=lambda seq:''.join(W[a]for a in seq);full=('D','DC','V','VC','VCC','U','UC','UCC');beta=1-1j
O={}
for src in ('V','VC'):
 z=tr(raw(src));ek={z['p']+rot(z['h'])*q for q in K};O[src]={q for q,(c,t)in z['last'].items()if c=='R'and q not in ek};assert beta not in z['req']and len(O[src])==(6 if src=='V'else 9)
for s in full:
 z=tr(raw(s));q=z['p']+rot(z['h'])*beta;assert z['last'][q]==('R',len(raw(s))-2)
qmin=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text());assert all(q['certified_minimum_C_age']>=2 for q in qmin['slots'].values())
angles=[a for a in json.loads((R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json').read_text())['all831_conditional_preFOREIGN_old_source_angle_interfaces']if a['old_source']=='V'and a['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age']in(0,1)];assert Counter(a['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age']for a in angles)=={0:37,1:64}
old=pieces('V')[0];u=old[1]-old[0];mask={};cnt=Counter();oblig=[];npos=0
key=lambda r:(r['src'],r['n'],r['A'],r['b1'],r['b2'],r['b3'],tuple(r['pa']),tuple(r['p3']),r['totalK'])
cert={key(r):(i,r)for i,r in enumerate(J['all1419_actual_source_typed_before_masks'])};assert len(cert)==1419
for ag in angles:
 b1,b2,b3=ag['first'],ag['second'],ag['third'];n=ag['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age'];KK=n+(b1+b2).count('C');h=(2-KK)%4;ha=(-n)%4;assert(KK,h,ha)==(ag['total_ordinary_C_before_third'],ag['third_heading_relative_old'],ag['true_FOREIGN_heading_relative_old'])
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
   npos+=1
   for A in'FQB':
    dz=tr(raw(A+b1+b2),h=ha);pa=p-dz['p'];assert dz['h']==h;local=tr(raw(A+b1+b2+b3)+M)
    for src in ('V','VC'):
     if src.count('C')>n:continue
     kk=(src,n,A,b1,b2,b3,tuple(xy(pa)+[ha]),tuple(xy(p)+[h]),KK);idx,row=cert[kk];assert str(ss)==row['old_s']and str(tt)==row['third_t']
     if local['bad']:why='immutable_local_literal_conflict'
     else:
      cuts=set()
      for q in O[src]|{beta}:
       lc=(q-pa)/rot(ha)
       if lc in K:cuts.add((tuple(xy(q)),'CORE',None))
       elif local['req'].get(lc)is False:cuts.add((tuple(xy(q)),'WHITE',next(i for i,(p,hh,ch)in enumerate(local['reads'])if p==lc)))
      supplied={(tuple(r.get('SAME_CURRENT_cell',r.get('SAME_preFOREIGN_BLACK_cell'))),'CORE'if 'entry K'in r['reason']else'WHITE',r.get('combined_tick0'))for r in row['all_initial_field_conflicts']};assert cuts==supplied
      why='genuine_preFOREIGN_field_cut'if cuts else'endpoint_obligation'
     assert why==row['classification'];mask[kk]=why;cnt[n,src,why]+=1
     if why=='endpoint_obligation':oblig.append((idx,row))
assert len(mask)==1419 and len(oblig)==225
@lru_cache(None)
def perms(d,v,u):
 if d+v+u==0:return ('',)
 ans=[]
 for i,a in enumerate('DVU'):
  q=[d,v,u]
  if q[i]:q[i]-=1;ans.extend(a+s for s in perms(*q))
 return tuple(ans)
assert tr(W['C']+W['U'])['bad']is not None
records=[];counts=[]
for idx,r in oblig:
 n=r['n'];x,y,h=r['pa'];sol=[]
 if n==0:
  assert h==0
  for vn in range(max(0,x)):
   dn=x-1-vn;rem=y-3-dn-3*vn
   if rem>=0 and rem%4==0:sol.append((dn,vn,rem//4,0,0,0))
 else:
  assert h==3
  for un in range(max(0,(y-4)//4+1)):
   for vn in range((y-4-4*un)//3+1):
    for dn in range(y-4-4*un-3*vn+1):
     if(r['src']=='VC')!=(dn+vn+un==0):continue
     rem=y-4-4*un-3*vn-dn
     for vw in range(rem+1):
      dw=rem-vw;num=1+dn+vn-dw-3*vw-x
      if num>=0 and num%4==0 and dw+vw+num//4:sol.append((dn,vn,un,dw,vw,num//4))
 for dn,vn,un,dw,vw,uw in sol:
  c=dict(rowid=idx,n=n,dN=dn,vN=vn,uN=un)
  if n:c.update(dW=dw,vW=vw,uW=uw)
  counts.append(c)
  for N in perms(dn,vn,un):
   for WR in perms(dw,vw,uw):
    rail=WR if n else N
    if n and WR[0]=='U':continue
    if rail and rail[-1]not in('VU'if r['A']in'FQ'else'U'):continue
    if not rail and r['A']=='B':continue
    body=('VC'if r['src']=='VC'else'V'+N+('C'if n else''))+WR
    z=tr(raw(body));assert xy(z['p'])+[z['h']]==r['pa']
    T=body+r['A']+r['b1']+r['b2']+r['b3'];records.append((idx,N,WR,T))
can=lambda x:json.dumps(x,sort_keys=True);assert Counter(map(can,counts))==Counter(map(can,J['all_exact_endpoint_count_solutions']))
assert set(records)=={(r['rowid'],r['Nrun'],r['Wrun'],r['T'])for r in J['all189_endpoint_exhaustive_whole_words']}and len(records)==189
positive=[]
for rec in J['all189_endpoint_exhaustive_whole_words']:
 z=tr(raw(rec['T'])+M);assert(z['bad']is None)==rec['feasible']
 if z['bad']:
  t,p,q,c=z['bad'];f=rec['conflict'];assert(t,p,xy(q),c)==(f['conflict_read'],f['previous_read'],f['cell'],f['turn'])
 else:positive.append(rec['T'])
assert len(positive)==len(set(positive))==50
query_count=0;nodes=set()
for tree in J['all50_naturally_closed_complete_predecessor_trees']:
 T=tree['original_positive'];assert T in positive
 for node in tree['naturally_closed_nodes']:
  text=node['actual_word'];assert text in(T,'D'+T);nodes.add(text);surv=[]
  for q in node['all8_complete_predecessor_queries']:
   pre=q['actual_full_predecessor'];z=tr(raw(pre+text)+M);assert(z['bad']is None)==q['feasible'];query_count+=1
   if z['bad']:
    t,p,at,c=z['bad'];f=q['conflict'];assert(t,p,xy(at),c)==(f['conflict_read'],f['previous_read'],f['cell'],f['turn'])
   else:surv.append(pre)
  assert surv==node['complete_survivor_set']==(['D']if text==T else[])
assert len(nodes)==100 and query_count==800
# All100 COMPLETE boards retain true source-output and incoming-beta identities.
previous_contact_controls=0;collinear_adjacent_flag_corrections=[]
for control in J['all100_complete_board_controls']:
 T=control['tokens'];assert T in nodes;seed={complex(*q)for q in control['complete_seed']};B={q:('initial',None)for q in seed};p=0j;h=0;starts=[];time=0
 for atom in T:starts.append((time,p,h));z=tr(W[atom],p,h);p,h=z['p'],z['h'];time+=len(W[atom])
 source=control['actual_selected_old_source_index0'];assert source in(0,1);ts,ps,hs=starts[source];src=control['actual_selected_full_source'];birth={ps+rot(hs)*q:ts+tr(raw(src))['last'][q][1]for q in O[src]};bc=ps+rot(hs)*beta;cut=control['source_foreign_cut']['cut_before_tick0'];p=0j;h=0
 for t,ch in enumerate(raw(T)+M):
  if t==cut:
   ek={p+rot(h)*q for q in K};assert all(B.get(q)==('R',born)and q not in ek for q,born in birth.items())and bc not in ek
   assert B[bc]==(('R',8)if source else('initial',None));assert list(B[bc])==control['source_foreign_cut']['beta_identity']
  assert(ch=='L')==(p in B);row=control['all_actual_RAW_plus_M11_reads'][t];before=B.get(p)
  if ch=='L':B.pop(p)
  else:B[p]=('R',t)
  assert row['tick0']==t and row['read_number1']==t+1 and row['cell']==xy(p)and row['turn']==ch and row['before_identity']==(list(before)if before else None)and row['after_identity']==(list(B[p])if p in B else None)
  h=(h+(1 if ch=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 assert len(seed)==control['initial_black_mass']and len(raw(T)+M)==control['total_executed_reads']
 old=(center(ps,hs),center(ps+rot(hs)*tr(W['V'])['p'],hs));nt,np,nh=starts[-1];new=(center(np,nh),center(tr(W[T[-1]],np,nh)['p'],tr(W[T[-1]],np,nh)['h']));assert meet(*old,*new)==(F(0),F(1))
 pieces0=pieces(T);assert len(pieces0)==len(control['repaired_proxy_pieces'])
 for (a,b),rec in zip(pieces0,control['repaired_proxy_pieces']):assert xy(a)==rec['a']and xy(b)==rec['b']
 extra=False
 for rec in control['all_proxy_pair_checks']:
  i,j=rec['old_piece'],rec['new_piece'];contact=meet(*pieces0[i],*pieces0[j]);assert(contact is not None)==(rec['contact']is not None);adj=j==i+1 and contact==(F(1),F(0));
  if adj!=rec['true_adjacent_endpoint']:
   assert adj and not rec['true_adjacent_endpoint']and rec['contact']=={'collinear_old_interval':['1','1']};collinear_adjacent_flag_corrections.append((T,i,j))
  if contact is not None and not adj and j<len(pieces0)-1:extra=True
 previous_contact_controls+=extra
out=dict(status='PASS oldV THIRD trueprefage0/1 endpoint exhaustion and complete ancestry closure',manifest=sha(MF),angle_count=101,pose_count=npos,source_masks=1419,mask_partition={str(k):v for k,v in cnt.items()},endpoint_obligations=225,whole_words=189,positives=50,natural_reverse_nodes=100,complete_queries=800,complete_boards=100,controls_with_earlier_nonadjacent_contacts=previous_contact_controls,collinear_adjacent_nonparallel_flag_false=collinear_adjacent_flag_corrections,analytic_review=[
'Genuine U-entry factor makes selectedV noninitial. All8 previous-full finalEXIT buds have actual fresh R identity and correct ownC shifts; V/VC literally missbeta. SourceV atn0 and V/VC atn1 complete, and every full output staysCURRENT by universalmin2 used onlybeforeA. No initial root is called a source birth.',
'Independent101 signed angles/closed rational boxes and outgoing endpoint ownership reconstruct all1419 masks, including parallel firstpositive onset. All225 endpoint obligations retained. n0 has exact oneNrail, permitting selectedV itself beforeF/Q but notB; n1 plainV requiresnonemptyNrail beforefirstC while sourceVC has emptyextraNrail. Wrailnonempty, firstD/V by literalCU failure, lastV/U by actualFOREadjacency.',
'Independent nonnegative endpoint elimination and multiset orders match all77+112 whole words with no prefix-length cutoff. All189 literal results and earliest conflicts rechecked. Fifty positives each have onlyplainD parent; eachD-prependedword has none amongall8 fullpackets.100nodes/800queries exhaust the naturallyclosed ancestry relation, not a chosen depth.',
'Every100 complete board and fine-read identity ledger replayed. Source R outputs remain SAME and outside actualFOREentrycore. BareT controls carry explicit initialbeta; D+T beta is genuine precedingD R8. ThirdD terminal hitsoldVSTART, outgoingowned byV notincomingD. Full proxy pairs confirm some earliercontacts, preserved rather than silently promoted to first-contact controls.',
'Mandatory metadata qualification: the author true_adjacent_endpoint flag recognizes NONPARALLEL endpoint joins only. Its false value for a recorded collinear interval[1,1] at consecutive pieces does NOT establish a nonadjacent contact. All such actual adjacent joins are separately listed in this report; actual nonadjacent-contact count excludes them. No simple-control theorem depends on the flag.',
'Any U-family entry before the selected initialV must appear in the complete predecessor relation; none does. LaterU in these positivewords is real but doesnotcontainselectedV as anoldsource. Only oldV trueprefage0/1 THIRD source closure follows, not overallTHIRDsimplicity or postFOREIGN maturation.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
