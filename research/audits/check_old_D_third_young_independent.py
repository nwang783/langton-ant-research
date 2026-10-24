from pathlib import Path
from itertools import product
from fractions import Fraction as F
from collections import Counter
from functools import lru_cache
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'old_D_third_young_endpoint_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='cd4cd0819d8ff15a425d4de5d5a80441058143544227f2798803d6b711a40e59';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'D_third_young_endpoint.json').read_text());ns={'__file__':str(S.with_name('check_old_D_third_age3_independent.py'))};exec(Path(ns['__file__']).read_text().split('angles=')[0],ns)
W,M,K,tr,rot,center,xy,meet,pieces,cross,raw,full,I,beta,common=[ns[k]for k in('W','M','K','tr','rot','center','xy','meet','pieces','cross','raw','full','I','beta','common')]
angles=[a for a in json.loads((R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json').read_text())['all831_conditional_preFOREIGN_old_source_angle_interfaces']if a['old_source']=='D'];assert len(angles)==206
old=pieces('D')[0];u=old[1]-old[0];poses=0;cases={};counts=Counter();physical={0:{},1:{}}
def key(r):return(r['n'],r['source'],r['nextfull'],r['b1'],r['b2'],r['b3'],r['A'],tuple(r['pa']),tuple(r['p3']))
cert={key(r):r for r in J['typed_rows']};assert len(cert)==7911
for ag in angles:
 b1,b2,b3=ag['first'],ag['second'],ag['third'];n=ag['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age'];KK=n+(b1+b2).count('C');h=(2-KK)%4;ha=(-n)%4;assert(KK,h,ha)==(ag['total_ordinary_C_before_third'],ag['third_heading_relative_old'],ag['true_FOREIGN_heading_relative_old'])
 z=tr(W[b3],h=h);c=center(0,h);v=center(z['p'],z['h'])-c;den=cross(u,v);corners=[(old[0]+s*u-c-t*v)/2 for s,t in product((0,1),repeat=2)]
 for x in range(math.floor(min(q.real for q in corners)),math.ceil(max(q.real for q in corners))+1):
  for y in range(math.floor(min(q.imag for q in corners)),math.ceil(max(q.imag for q in corners))+1):
   if(x+y-KK)%2:continue
   p=x+y*1j;off=c+2*p-old[0]
   if den:ss,tt=F(cross(off,v),den),F(cross(off,u),den)
   else:
    if cross(off,u):continue
    ratio=F(int(v.real),int(u.real));q=F(int(off.real),int(u.real));assert ratio>0
    if q>=0:continue
    ss=F(0);tt=-q/ratio
   if not(0<=ss<1 and 0<tt<=1):continue
   poses+=1
   for A in'FQB':
    dz=tr(raw(A+b1+b2),h=ha);pa=p-dz['p'];assert dz['h']==h;local=tr(raw(A+b1+b2+b3)+M)
    ep=pa;hh=ha;verts=[center(ep,hh)];f=tr(W['F'],ep,hh);verts.append(center(f['p'],f['h']));a=tr(W[A],ep,hh);ep,hh=a['p'],a['h']
    if A!='F':verts.append(center(ep,hh))
    for atom in(b1,b2):z0=tr(W[atom],ep,hh);ep,hh=z0['p'],z0['h'];verts.append(center(ep,hh))
    early=any(meet(*old,a,b)is not None for a,b in zip(verts,verts[1:]));base='earlier_contact'if early else'local_immutable'if local['bad']else'live'
    for source,nxt in [('DC',None)]+[('D',s)for s in full]:
     facts={common};why=base;cuts=set()
     if n<=2:facts.add(beta)
     if source=='DC':
      facts|={2+3j,3+1j,3+2j}
      if n<1:why='full_source_uncompleted'
     else:
      if nxt.count('C')>n:why='actual_next_full_uncompleted'
      facts|=({3+1j}if nxt[0]=='D'else{1+1j,2+1j,3+2j}if nxt[0]=='V'else{1+1j,1+2j,2+1j,2+2j})
     if why=='live':
      fore=tr(W[A]+M)
      if source=='D'and nxt[0]=='U'and any((q-pa)/rot(ha)in fore['req']for q in{1+1j,1+2j,2+1j,2+2j}):why='young_nextU_FOREIGN_star_effect'
      else:
       cuts={q for q in facts if(q-pa)/rot(ha)in K or local['req'].get((q-pa)/rot(ha))is False};why='CURRENT_cut'if cuts else'NECESSARY'
     kk=(n,source,nxt,b1,b2,b3,A,tuple(xy(pa)+[ha]),tuple(xy(p)+[h]));r=cert[kk];assert why==r['why']and cuts=={complex(*q)for q in r['cuts']};cases[kk]=why;counts[why]+=1
     if why=='NECESSARY':
      assert n!=2
      if n in physical:physical[n][(A,tuple(xy(pa)+[ha]),b1,b2,b3,tuple(xy(p)+[h]))]=kk
assert poses==293 and len(cases)==7911 and dict(counts)==J['initial_partition']and[len(physical[n])for n in(0,1)]==[138,135]
@lru_cache(None)
def permutations(d,v,u):
 if d+v+u==0:return ('',)
 ans=[]
 for i,a in enumerate('DVU'):
  q=[d,v,u]
  if q[i]:q[i]-=1;ans.extend(a+s for s in permutations(*q))
 return tuple(ans)
records={};tuples=[]
for n,pdict in physical.items():
 for (A,pa,b1,b2,b3,p3),_ in pdict.items():
  x,y,h=pa; solutions=[]
  if n==0:
   assert h==0
   for v in range(max(0,x)):
    d=x-1-v;rr=y-1-d-3*v
    if rr>=0 and rr%4==0 and d+v+rr//4:solutions.append((0,0,0,d,v,rr//4))
  else:
   assert h==3
   # Independent order of elimination: uN, vN, dN, then vW; dW fixed by y, uW by x.
   for un in range(max(0,(y-2)//4+1)):
    for vn in range((y-2-4*un)//3+1):
     for dn in range(y-2-4*un-3*vn+1):
      rem=y-2-4*un-3*vn-dn
      for vw in range(rem+1):
       dw=rem-vw;num=1+dn+vn-dw-3*vw-x
       if num>=0 and num%4==0 and dw+vw+num//4:solutions.append((dn,vn,un,dw,vw,num//4))
  for cts in solutions:
   tuples.append((n,A,pa,(b1,b2,b3),cts));dn,vn,un,dw,vw,uw=cts
   for X in permutations(dn,vn,un):
    for Y in permutations(dw,vw,uw):
     if Y[-1]not in('VU'if A in'FQ'else'U'):continue
     source,nxt=('D',Y[0])if n==0 else('DC',None)if not X else('D',X[0]+('C'if len(X)==1 else''))
     kk=(n,source,nxt,b1,b2,b3,A,pa,p3);assert cases[kk]=='NECESSARY'
     pre='D'+X+('C'if n else'')+Y;z=tr(raw(pre));assert tuple(xy(z['p'])+[z['h']])==pa
     T=pre+A+b1+b2+b3
     rec=dict(n=n,source=source,nextfull=nxt,foreign=A,foreign_pose=list(pa),returns=[b1,b2,b3],X=X,Y=Y)
     if T in records:assert all(records[T][k]==v for k,v in rec.items())
     else:records[T]=rec
canon=lambda x:json.dumps(x,sort_keys=True)
assert Counter(tuples)==Counter((r['n'],r['foreign'],tuple(r['foreign_pose']),tuple(r['returns']),tuple(r['counts']))for r in J['endpoint_count_records'])
assert set(records)==set(J['whole_words'])and Counter(r['n']for r in records.values())=={0:684,1:3073}
def owner(T,tick):
 for j,a in enumerate(T):
  if tick<len(W[a]):return dict(kind='actual_RAW',atom=a,atom_index0=j,owner_tick0=tick,owner_read1=tick+1)
  tick-=len(W[a])
 return dict(kind='actual_following_word_M11_prefix',owner_tick0=tick,owner_read1=tick+1)
def check_word(T,r):
 z=tr(raw(T)+M);ok=z['bad']is None;assert ok==r['feasible']
 if not ok:
  t,prev,q,ch=z['bad'];bad=r['immutable_conflict'];assert(t,prev,xy(q),ch)==(bad['conflict_read'],bad['previous_read'],bad['cell'],bad['turn']);assert owner(T,t)==r['first_failure_owner']and owner(T,prev)==r['previous_request_owner']
 else:
  seed={q for q,c in z['req'].items()if c};B=set(seed);p=0j;h=0
  for ch in raw(T)+M:
   assert(ch=='L')==(p in B);B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
  ctrl=r['physical_control'];assert sorted(map(xy,seed))==ctrl['seed']and len(seed)==ctrl['seed_mass']and len(raw(T)+M)==ctrl['actual_reads']and xy(p)+[h]==ctrl['actual_exit']and len(B)==ctrl['exit_mass']
 return ok
positives=[]
for T,r in records.items():
 sr=J['whole_words'][T];assert all(sr[k]==v for k,v in r.items())
 if check_word(T,sr):positives.append(T)
assert Counter(records[T]['n']for T in positives)=={0:2,1:324};assert{T for T in positives if records[T]['n']==0}=={'DVFCDV','DDUQCDV'}
queries={(r['target'],r['predecessor']):r for r in J['complete_reverse_relation']};assert len(queries)==5216;todo=list(positives);seen=set(todo);edges=[]
while todo:
 T=todo.pop()
 for pre in full:
  ok=check_word(pre+T,queries[T,pre])
  if ok:
   edges.append((T,pre));assert pre=='D'and T in positives
   if pre+T not in seen:seen.add(pre+T);todo.append(pre+T)
assert len(seen)==652 and sorted(seen)==J['reverse_closed_nodes']and len(edges)==326 and len(queries)==8*len(seen)
out=dict(status='PASS young oldD THIRD endpoint completeness and natural full predecessor closure',manifest=sha(MF),allD_angles_in_conservative_pass=206,allD_heads=293,typed_masks=7911,mask_partition=dict(counts),necessary_physical_young={n:len(v)for n,v in physical.items()},endpoint_count_tuples=dict(Counter(z[0]for z in tuples)),whole_words=dict(Counter(r['n']for r in records.values())),positive_words=dict(Counter(records[T]['n']for T in positives)),all_actual_positive_controls=652,reverse_closed_nodes=652,all_full_predecessor_queries=5216,analytic_review=[
'Conservative mask reconstruction deliberately includes ALL206 oldD angles/ages0..3, not just young ages. SourceDC, plainD actualnext8 full types and their completion priorities retained. Exact293 outgoing-owned poses,7911 masks and full seven-way partition agree; noage2 survives. Genuine prior EXIT beta used onlyn<=2. MandatoryCORE qualification preserves physical aliveCORE possibilities outside guaranteedCURRENT facts.',
'At n0 the genuine old interval afterD is one nonemptyN rail. Exactd+v=x-1,d+3v+4u=y-1 bounds all counts, all multiset orders enumerated, and actualFORElastV/U orB-lastU enforced. At n1 every history isD X C Y with arbitraryN X, nonemptyW Y. y-2 bounds five counts; x fixesuW, so no empirical length cutoff. FirstC actual ownership is selectedDC iffXempty, otherwise lastXbase tail; actual nextfull gainsC iffXlength1.',
'Independent endpoint elimination/order enumeration matches184+655 count records and684+3073 complete whole words exactly. Source/nextFULL necessary-row membership checked per word. All3431 failures reproduce earliest actual global read conflicts and correct RAW/terminalM owners.',
'All326 positive words and326 D-prepended words replay on complete minimal finite boards with actual full terminal fields/masses. All8 complete predecessors of each base word give exactlyD, and all8 predecessors of D-prepended words fail; the graph naturally closes at652nodes/5216queries. This is not depth-truncated reverse search.',
'Any eligible initial U-entry before the SELECTED initialD would have to occur in this exhaustive full-packet predecessor relation. None does. Later U bases inside positive words remain actual but their subfactor excludes the selected earlierD. Rotating a whole prepended word preserves literal feasibility and correctly aligns the selectedsource frame.',
'The conclusion is only oldD trueprefage0/1/2 chronological FIRST THIRD source exclusion. Together with separate age3 theorem it closes oldD source, not fullTHIRD simplicity, anotherforeign, general languagecoverage orcapture.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
