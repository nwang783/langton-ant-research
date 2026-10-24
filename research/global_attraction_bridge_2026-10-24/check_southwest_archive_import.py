"""One exact all-parameter archive-import interface, not postcollision classification."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,future
from certified_comparison_perturbation import reference,geometry
P=Path(__file__).parent;J=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());K=set(map(tuple,J['canonical_source']));W=J['W'];Q,_,_,_=geometry((0,0),1,W);QM=(202,201);TM=10413;A=[0,1,3,5,6]
def run(seed,p,h,N,expected=None):
 B={q:-i-1 for i,q in enumerate(sorted(seed))};word=[];reads=[];birth={};death={};first={}
 for t in range(N):
  reads.append(p);first.setdefault(p,t);old=B.pop(p,None)
  if old is None:B[p]=t;birth[t]=p;h=(h+1)%4;c='R'
  else:death[old]=t;h=(h-1)%4;c='L'
  if expected is not None:assert c==expected[t]
  word.append(c);p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 return dict(B=B,p=p,h=h,word=''.join(word),reads=reads,birth=birth,death=death,first=first)
def mature_y(g):
 B=set()
 for i,(x,y)in enumerate(Q):
  x-=2;y-=1
  for a in range(-((y-g)//2),1 if i<13 else 0):B.symmetric_difference_update({(x+2*a,y+2*a)})
 return B
seedT=mature_y(-15)|{(2*a,2*a)for a in A};T=run(seedT,(0,0),0,11232);TW,td,tdie,tests=future(T['B'],T['p'],T['h']);assert(T['p'],T['h'],td)==((-36,-10),0,(-2,-2));ref=reference(seedT,(0,0),0,T['word'],TW);assert min(y for x,y in T['reads'])==-15
normal=lambda q:q[0]-q[1]
assert(min(map(normal,ref['Q'])),max(map(normal,ref['Q'])))==(-32,-22)
assert(min(normal(q)-1 for q in Q),max(normal(q)-1 for q in Q))==(-8,2)
assert all(-8<=normal(q)-1<=2 for q in K)
M=run(set(map(tuple,J['modes']['M']['kernel'])),(0,0),0,10712,J['modes']['M']['recovery_word']);mw,md,mdie,mtests=future(M['B'],M['p'],M['h']);assert M['birth'][9752]==(4,28)and M['B'][(4,28)]==9752 and 9752 not in mdie
assert max(y for x,y in M['B'])==31
flightword=W[41:]+W[:41];FQ,_,_,_=geometry(M['p'],M['h'],flightword);assert all(-8<=normal(q)<=2 for q in FQ)
# All old-output intersections with every SW tail ray. Time=104*n+constant.
hits=[]
for r,iid in sorted(M['B'].items()):
 for i,s in enumerate(ref['Q']):
  dx=r[0]-28-s[0];dy=r[1]-28-s[1]
  if dx==dy and dx%2==0:
   koffset=-dx//2;assert 100+koffset>=0
   hits.append(dict(cell=r,identity=iid,phase=i,period_offset=koffset,time_offset=11232+104*koffset+i))
hits.sort(key=lambda x:x['time_offset']);assert hits[0]==dict(cell=(4,28),identity=9752,phase=100,period_offset=-7,time_offset=10604)
assert ref['QH'][100]==2 and TW[100]=='R'
# Exact whole actual board after fixed first M, without the later T inputs.
sourceprefix=W*100+W[:13];base_seed=K|{(QM[0]+2*a,QM[1]+2*a)for a in[0,1,6,8]};baseword=sourceprefix+M['word'];base=run(base_seed,(0,0),1,len(baseword),baseword)
assert base['B'][(QM[0]+4,QM[1]+28)]==TM+9752
assert{(x-QM[0],y-QM[1]):iid-TM for(x,y),iid in base['B'].items()if -32<=x-y-1<=-22}=={r:iid for r,iid in M['B'].items()if -32<=normal(r)<=-22}
# Finite XOR algebra for the ENTIRE collision field, not just relevant pieces.
def odd(reads):
 B=set()
 for q in reads:B.symmetric_difference_update({q})
 return B
def terms(n):
 qt=(QM[0]+2*n+28,QM[1]+2*n+28);d=(2,2);sw=(-2,-2)
 out=[(q,(0,0),1)for q in sorted(base['B'])]
 out.extend(((qt[0]+2*a,qt[1]+2*a),(0,0),1)for a in A)
 out.extend(((QM[0]+r[0],QM[1]+r[1]),d,n)for r in sorted(odd(FQ)))
 out.extend(((QM[0]+r[0]+2*n,QM[1]+r[1]+2*n),(0,0),1)for r in sorted(odd(FQ[:76])))
 out.extend(((qt[0]+r[0],qt[1]+r[1]),(0,0),1)for r in sorted(odd(ref['P'])))
 out.extend(((qt[0]+r[0],qt[1]+r[1]),sw,n-7)for r in sorted(odd(ref['Q'])))
 out.extend(((qt[0]+r[0]-2*(n-7),qt[1]+r[1]-2*(n-7)),(0,0),1)for r in sorted(odd(ref['Q'][:100])))
 return out
def materialize(ts):
 B=set()
 for(x,y),(dx,dy),n in ts:
  for k in range(n):B.symmetric_difference_update({(x+dx*k,y+dy*k)})
 return B
postword=(P/'SOUTHWEST_POSTIMPORT_WORD.txt').read_text().strip();assert len(postword)==48464
# All-n difference after the SAME physical collision: two translated caps and a forward segment train.
n0=100;qt0=(QM[0]+228,QM[1]+228)
cap={(qt0[0]+2*a,qt0[1]+2*a)for a in A}
cap.symmetric_difference_update((QM[0]+r[0]+200,QM[1]+r[1]+200)for r in odd(FQ[:76]))
cap.symmetric_difference_update((qt0[0]+r[0],qt0[1]+r[1])for r in odd(ref['P']))
strand={(QM[0]+r[0]+200,QM[1]+r[1]+200)for r in odd(FQ)}
strand.symmetric_difference_update((qt0[0]+r[0]+2,qt0[1]+r[1]+2)for r in odd(ref['Q']))
assert min(x for x,y in cap|strand)>240
def delta(k):return[(q,(0,0),1)for q in cap]+[((q[0]+2*k,q[1]+2*k),(0,0),1)for q in cap]+[(q,(2,2),k)for q in strand]
base_event=materialize(terms(100))
controls=[];remote_reference=None;M_entry_fixed=None
T_fates=dict(T['death']);T_fates.update({i:11232+tt for i,tt in tdie.items()});localC={q for i,q in enumerate(sorted(seedT))if -i-1 in T_fates};assert len(localC)==99
assert all(-i-1 in T['death']for i,q in enumerate(sorted(seedT))if q in localC)
for n in[100,137,500]:
 qt=(QM[0]+2*n+28,QM[1]+2*n+28);seed=base_seed|{(qt[0]+2*a,qt[1]+2*a)for a in A};assert len(seed)==22
 flight=flightword*n+flightword[:76];to_contact=baseword+flight;prefix=to_contact+T['word']+TW*(n-7)+TW[:100];event=len(prefix);assert event==TM+21392+208*n
 z=run(seed,(0,0),1,event,prefix);hit=(QM[0]+4,QM[1]+28);assert(z['p'],z['h'])==(hit,2)and z['B'][hit]==TM+9752
 assert materialize(terms(n))==set(z['B'])
 assert set(z['B'])^base_event==materialize(delta(n-100))
 entry=run(seed,(0,0),1,len(to_contact),to_contact);rel={(x-qt[0],y-qt[1]):iid for(x,y),iid in entry['B'].items()};assert{r for r in rel if r[1]>=-15}==seedT
 for a,tt in zip([0,1,6,8],[0,124,1272,5028]):assert z['first'][(QM[0]+2*a,QM[1]+2*a)]==TM+tt
 assert all(z['first'][(qt[0]+2*a,qt[1]+2*a)]>=len(to_contact)for a in A)
 # Genuine collision and true post-L whole board/pose.
 zz=run(seed,(0,0),1,event+1,prefix+'L');assert zz['death'][TM+9752]==event and(zz['p'],zz['h'])==((hit[0]+1,hit[1]),1)
 complete=run(seed,(0,0),1,event+1+len(postword),prefix+'L'+postword);fw,fd,die,ptests=future(complete['B'],complete['p'],complete['h']);assert(complete['p'],complete['h'],fd)==((155,215),1,(-2,2))
 tailQ,_,_,_=geometry(complete['p'],complete['h'],fw);assert max(x for x,y in complete['reads'][event+1:]+tailQ)==240
 fates=dict(complete['death']);fates.update({i:event+1+len(postword)+tt for i,tt in die.items()});entireC={q for q,i in entry['B'].items()if i in fates}
 actualrho=max(max(abs(q[0]-qt[0]),abs(q[1]-qt[1]))for q in entireC)
 local={(qt[0]+x,qt[1]+y)for x,y in localC};assert local<=entireC;remote=entireC-local
 assert len(remote)==786 and max(x for x,y in remote)<=240 and min(x for x,y in remote)==158 and min(y for x,y in remote)==162
 if remote_reference is None:remote_reference=remote
 assert remote==remote_reference and actualrho==2*n+72
 mentry=run(seed,(0,0),1,TM,sourceprefix);mentryC={q for q,i in mentry['B'].items()if i in fates};mrad=max(max(abs(q[0]-QM[0]),abs(q[1]-QM[1]))for q in mentryC);assert mrad==2*n+40 and actualrho-mrad==32
 tmarkers={(qt[0]+2*a,qt[1]+2*a)for a in A};mfix=mentryC-tmarkers
 if M_entry_fixed is None:M_entry_fixed=mfix
 assert mfix==M_entry_fixed and len(mfix)==254
 mref={(QM[0]+x,QM[1]+y)for x,y in J['modes']['M']['entire_comparison_pruning']};extra=mfix-mref
 assert len(extra)==128 and sum(x>=QM[0]-23 for x,y in extra)==21
 controls.append(dict(n=n,initial_seed=sorted(seed),T_origin=qt,T_contact=len(to_contact),T_kernel=sorted(seedT),whole_contact_black=[[q,i]for q,i in sorted(entry['B'].items())],original_first_reads=[dict(cell=q,time=z['first'][q])for q in sorted(seed)],event_cut=event,event_pose=[z['p'],z['h']],marked_birth=TM+9752,marked_cell=hit,marked_age=event-TM-9752,rho_entry_lower_bound=2*n+24,whole_pre_event_black=[[q,i]for q,i in sorted(z['B'].items())],whole_post_event_black=sorted(zz['B']),post_event_pose=[zz['p'],zz['h']],prefix_sha256=hashlib.sha256(prefix.encode()).hexdigest(),symbolic_terms=terms(n),complete_future_certificate=dict(terminal_cut=event+1+len(postword),terminal_pose=[complete['p'],complete['h']],terminal_full_black=sorted(complete['B']),tail_word=fw,tail_drift=fd,full_parity_tests=ptests),actual_entire_entry_pruning=sorted(entireC),actual_entry_radius=actualrho,actual_first_M_entry_radius=mrad,actual_first_M_entry_pruning=sorted(mentryC)))
 print('n',n,'first archive hit',event-len(to_contact),'age',event-TM-9752,'full post mass',len(zz['B']),flush=True)
# Pure-wake comparison for the same terminal packet, including all full retained old fields.
pure=[]
for n in[11,100,500]:
 qt=(2*n+2,2*n+1);seed=K|{(qt[0]+2*a,qt[1]+2*a)for a in A};prefix=W*n+W[:13]+T['word'];z=run(seed,(0,0),1,len(prefix),prefix);pw,pd,pdeath,ptests=future(z['B'],z['p'],z['h']);assert pw==TW and pd==(-2,-2)
 pure.append(dict(n=n,seed=sorted(seed),terminal_cut=len(prefix),complete_terminal_black=sorted(z['B']),terminal_pose=[z['p'],z['h']],tail_word=pw,tail_drift=pd,parity_tests=ptests))
files=['RECURSIVE_PHASE13_PACKET_MANIFEST.json','RECURSIVE_PHASE13_PACKET_CHECKED.json','../audits/check_recursive_phase13_packet_independent.json','certified_comparison_perturbation.py','check_return_permanent_output_debt.py','SOUTHWEST_POSTIMPORT_WORD.txt']
# Require exact audit filename, with no silent skip.
for f in files:assert(P/f).exists(),f
out=dict(status='AUTHOR all-n first-contact theorem; independent audit pending',scope='All n>=100 constant22 finite seeds: exact old-written-input return and capture at80270+208n. Pure terminal comparison all n>=11. No arbitrary packet closure.',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files},T_kernel=sorted(seedT),T_recovery=T['word'],T_output_black=sorted(T['B']),T_output_pose=[T['p'],T['h']],T_tail_word=TW,T_tail_drift=td,T_parity_tests=tests,T_initial_first_reads=[dict(cell=q,time=T['first'].get(q))for q in sorted(seedT)],T_all_ray_first_reads=[[a,T['first'].get((2*a,2*a))]for a in range(11)],M_marked_birth=9752,M_marked_cell=(4,28),M_marked_never_read_by_NE_comparison=True,M_output_relevant_transverse_cells=[q for q in M['B']if -32<=normal(q)<=-22],all_affine_old_output_hits=hits,base_after_M=dict(full_black=sorted(base['B']),pose=[base['p'],base['h']],time=len(baseword)),controls=controls,pure_controls=pure,exact_entry_pruning=dict(first_M_fixed_cohort=sorted(M_entry_fixed),first_M_extra_vs_NE_reference=sorted(extra),local=sorted(localC),remote=sorted(remote_reference),total=885,radius='2n+72',first_M_entry_radius='2n+40',increase=32),postcollision_word=postword,all_n_difference=dict(base_n=100,cap=sorted(cap),strand=sorted(strand),minimum_x=min(x for x,y in cap|strand),complete_future_maximum_x=240,formula='B_n XOR B_100 = cap XOR (cap+2k,2k) XOR XOR_r<k(strand+2r,2r), k=n-100'),huge_symbolic_control=dict(n=10**9,event_relative_T=104*10**9+10604,age=208*10**9+11640,term_count=len(terms(10**9)),full_pre_event_terms=terms(10**9)))
(P/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
