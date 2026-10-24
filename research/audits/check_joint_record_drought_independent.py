from pathlib import Path
from bisect import bisect_left,bisect_right
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'JOINT_RECORD_DROUGHT_MANIFEST.json';assert sha(MF)=='279631813c510c23d6939b3ef97d417f72b727e6820e243846e06cbc135adf80';mf=json.loads(MF.read_text())
for kind in ('files','dependencies'):
 for f,h in mf[kind].items():assert sha(D/f)==h
J=json.loads((D/'JOINT_RECORD_DROUGHT_CHECKED.json').read_text());A=json.loads((D/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());RR=json.loads((D/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text())
ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);K,xy,geometry,sim,cert,key,future=[ns[k]for k in ('K','xy','geometry','sim','cert','key','future')]
V=(1j,1,-1j,-1);proj=lambda q:(int(q.imag),int(q.real),-int(q.imag),-int(q.real));enc=lambda b:sorted([[xy(q),i]for q,i in b.items()]);d=2+2j;W=sim(K,104)['word'];CAN={W[i:]+W[:i]for i in range(104)}
# Fresh complete simulations and independent sparse-table interval maxima.
controls=[];reads=completed=0
for row in J['controls']:
 name=row['name'];seed={complex(*q)for q in row['seed']};N=row['physical_reads'];targets={int(k)for k in row['named_full_snapshots']};z=cert(sim(seed,N,cuts=targets));assert z['tail']in CAN
 assert [xy(z['p']),z['h']]==row['terminal_pose']and enc(z['B'])==row['terminal_full_field']and xy(z['d'])==row['tail_drift']and z['tests']==row['infinite_parity_tests']
 pts=z['pts']+[z['p']];head=z['heads']+[z['h']];ext=[max(proj(q)[a]for q in seed|{0j})for a in range(4)];hext=[0]*4;record=[];headrecord=[];hulls={}
 for t,p in enumerate(pts):
  vv=proj(p)
  for a in range(4):
   if vv[a]>hext[a]:assert vv[a]==hext[a]+1 and head[t]==a;hext[a]=vv[a];headrecord.append([t,a])
   if vv[a]>ext[a]:
    assert vv[a]==ext[a]+1 and head[t]==a
    if t<N:assert z['word'][t]=='R'
    else:assert p not in z['B']
    ext[a]=vv[a];record.append([t,a])
  if t in targets:hulls[t]=list(ext)
 assert record==row['pristine_support_hull_records']and headrecord==row['ordinary_head_records']
 for t,ref in row['named_full_snapshots'].items():
  t=int(t);b,p,h=z['snap'][t];assert enc(b)==ref['full_field']and [xy(p),h]==ref['pose']and hulls[t]==ref['hull']
 rt=[t for t,a in record];dirs=[[t for t,a in record if a==u]for u in range(4)];gap=[b-a for a,b in zip(rt,rt[1:])];sparse=[gap]
 while sparse[-1]and len(sparse[-1])>1:
  k=len(sparse)-1;step=1<<k;prior=sparse[-1]
  if len(gap)<2*step:break
  sparse.append([max(prior[i],prior[i+step])for i in range(len(gap)-2*step+1)])
 def rmq(a,b):
  if a>=b:return 0
  k=(b-a).bit_length()-1;return max(sparse[k][a],sparse[k][b-(1<<k)])
 def check(s,t,q):
  if s==t:return 0,0
  lo=bisect_right(rt,s);hi=bisect_left(rt,t)
  H=max(rt[lo]-s,t-rt[hi-1],rmq(lo,hi-1))if lo<hi else t-s
  rows=[]
  for a,L in enumerate(dirs):
   i=bisect_right(L,s);j=bisect_left(L,t)
   if i<j:rows.append((L[j-1],a,j-i))
  rows.sort();later=0
  for ell,a,n in reversed(rows):
   dis=proj(pts[ell])[a]-proj(q)[a];assert n<=dis<=t-ell<=H*(1+later);later+=n
  assert later==hi-lo<=(H+1)**len(rows)-1 and t-s<=H*(hi-lo+1)<=H*(H+1)**len(rows)<=H*(H+1)**4
  return H,len(rows)
 count=0;maxage=maxH=0;marked=[]
 for b,c in enumerate(z['word']):
  if c!='R' or b not in z['dead'] or z['dead'][b]>=N:continue
  end=z['dead'][b];H,m=check(b,end,pts[b]);count+=1;maxage=max(maxage,end-b);maxH=max(maxH,H)
  if any(a['start']==b for a in row['marked_intervals']):marked.append((b,end,H,m))
 assert count==row['completed_R_lifetimes_checked']and maxage==row['max_completed_age']and maxH==row['max_local_record_drought']
 for ref in row['marked_intervals']:assert(ref['start'],ref['end'],ref['H'],len(ref['directions']))in marked
 for ref in row['seed_input_open_interval_checks']:
  q=complex(*ref['endpoint']);assert q in seed;H,m=check(0,ref['end'],q);assert H==ref['H']and m==len(ref['directions'])
 if name.startswith('MT_'):
  n=int(name[3:]);s=29671+104*n;t=88368+208*n
  assert [r for r in record if s<=r[0]<=t]==[[s,0],[t,3]]and [r for r in headrecord if s<=r[0]<=t]==[[s,0],[t,3]]
  assert max(z['dead'][i]for i in range(-len(seed),0))==27201+104*n
  assert hulls[s]==[262+2*n,250+2*n,0,1]and pts[t]==-2+372j and head[t]==3 and t-s==58697+104*n
 controls.append(dict(name=name,reads=N,completed=count,max_age=maxage,max_local_gap=maxH,marked=marked,record_count=len(record),parity_tests=z['tests']));reads+=N;completed+=count
 print(name,N,count,maxage,maxH,flush=True)
assert reads==921933 and completed==416187
# Independent all-n geometric cover: every block/period endpoint, no interpolation.
qm=202+201j;pre=W*100+W[:13]+RR['modes']['M']['recovery_word'];P,H,pend,ph=geometry(0j,1,pre);assert len(pre)==21125 and(pend,ph)==(228+229j,0)
flight=W[41:]+W[:41];F,FH,_,_=geometry(pend,ph,flight);T=A['T_recovery'];TP,TH,te,th=geometry(0j,0,T);SW=A['T_tail_word'];SQ,SH,_,_=geometry(te,th,SW);post=A['postcollision_word'];PQ,PH,pe,ph=geometry(207+229j,1,post);NW=A['controls'][0]['complete_future_certificate']['tail_word'];NQ,NH,_,_=geometry(155+215j,1,NW)
ineq=Counter()
def bound(q,ax,ay,label):
 # q + n*(ax+i ay), against [-1,2n+250] x [0,2n+262].
 x,y=int(q.real),int(q.imag)
 for a,b in[(ax,x+1),(2-ax,250-x),(ay,y),(2-ay,262-y)]:assert a>=0 and 100*a+b>=0;ineq[label]+=1
for q in P:bound(q,0,0,'prefix')
assert min(q.real for q in P)==-1 and min(q.imag for q in P)==0
for q in F:bound(q,0,0,'first_flight');bound(q-d,2,2,'last_flight')
for q in F[:76]:bound(q,2,2,'partial_flight')
assert(F[76],FH[76])==(230+229j,0)
for q in TP:bound(230+229j+q,2,2,'T_all')
assert max(q.real for q in TP[:8471])==20 and max(q.imag for q in TP[:8470])==32 and TP[8470]==3+33j
for q in SQ:bound(230+229j+q,2,2,'SW_first');bound(246+245j+q,0,0,'SW_last')
for q in SQ[:100]:bound(244+243j+q,0,0,'SW_partial')
assert(SQ[100],SH[100])==(-38-14j,2)
for q in PQ:bound(q,0,0,'post')
assert(pe,ph)==(155+215j,1)
NWQ,NWH,endpoint,eh=geometry(pe,ph,NW*77+NW[:90]);assert len(NWQ)==8098 and(endpoint,eh)==(-2+372j,3)
for q in NWQ:bound(q,0,0,'NW_before_first_W')
assert sum(ineq.values())==358044
# Finite hull includes every initial seed point and all earlier actual head cuts.
for q in K|{qm+a*d for a in(0,1,6,8)}:bound(q,0,0,'initial_seed')
for a in(0,1,3,5,6):bound(qm+14*d+a*d,2,2,'initial_T_seed')
# Every stage's exact update count, including actual differing L at feedback.
assert len(T)==11232 and len(post)==48464
assert 21125+76+11232-7*104+100+1+len(post)==80270
assert 80270+8098==88368 and 21201+8470==29671
# Literal first-W ray equation independently finds unique earliest hit, not just tested77 periods.
hits=[]
for i,q in enumerate(NQ):
 # NW drift(-2,+2); first integer k with x<-1.
 k=max(0,(int(q.real)+1)//2+1);assert q.real-2*k<-1 and(k==0 or q.real-2*(k-1)>=-1)
 hits.append((104*k+i,k,i,q+k*(-2+2j),NH[i]))
best=min(hits);assert best==(8098,77,90,-2+372j,3)
O=dict(status='PASS all-direction endpoint-record theorem, conditional explicit rectangle evacuation/translation, and exact all-n simultaneous drought control',manifest=sha(MF),script=sha(S),full_reads=reads,completed_R_intervals=completed,controls=controls,all_n_affine_checks=sum(ineq.values()),affine_stage_counts=dict(ineq),first_W_tail_hit=[best[0],best[1],best[2],xy(best[3]),best[4]],analytic_review=[
'For any unit latticewalk and q=p_t in the earlierclosedrectangleR_s, last recordell_a has coordinateM_a(s)+n_a >= a.q+n_a. Hence n_a<=t-ell_a. Ordering atmostfour occurringnormals bylastoccurrence gives suffixbound t-ell_a<=H(1+sumlater n). Exact backwardrecursion Snew<=H+(H+1)S yields N<=(H+1)^m-1 and duration<=H(H+1)^m. Noant/color/nesting premise is hidden; endpointtisnotrecord, startsexcluded, no-recordcaseH=duration.',
'Global uniongaps<=H from anactualrecordT with infinitelymanylaterrecords dominate all endpointsubgaps for every s>=T. Thus noheadreturns anywhere inR_s afters+G(H), G=H(H+1)^4, independentlyofrectanglesize. CruciallyR_s includes ENTIREfiniteinitialBLACK plusheadhistory, so everyoldcurrentBLACK identity atT isinside. Futureconsumedoldidentities die byT+G; fromnextcut everyrelevantidentity islateRborn and has totalage<=G. Entire rho<=G, not merelyselectedcohort/activecomponent.',
'Finite normalized exactpruning recurrence then gives eventualturn/pose translation while allpermanentarchive remains. Infiniteunionrecords exclude zerodrift. Converselyatranslatorhas a positiveaxis and nextrecordwithinP afteroldextrema, soeventualuniongapsbounded. Ordinaryheadrecords differfromaugmentedrecords byonlyfinitelymanylevels, possiblyverylate; no uniform conversionthresholdisclaimed. Signedfinite-antunboundedness supplies infiniteunionrecords.',
'Contrapositive is arbitrarylate simultaneous FOUR-side droughts in a nontranslator. It is stronger thanseparateaxiswaits but not anoccurrenceproof, a canonical104classification, or a resourcepayment. The polynomial boundalsoappliesto eachcompletedRage and yields H>=(age/16)^(1/5), withnooptimalityclaim.',
'Ninefreshwholefiniteorbits retainallfields and initial/R identities. Reconstructed everypristine augmentedrecord andordinaryheadrecord, all416187completedR intervals, strongeropenintervals tooriginalinputs, namedwholeboards andallfuturecanonicalparity. Theproofisanalytic; controlsarenot promotedfromsamplemaxima.',
'For allintegern>=100 the complete22cellMT source/flight/T/SW/actualL/postrecovery/NW decomposition is inherited from signedfullfieldfamilies and independently rechecked geometrically. Affineendpointbounds coverevery phaseof everyunboundedperiod interval. StartNrecord is29671+104n at(233+2n,262+2n), oldaugmentedhull[-1,2n+250]x[0,2n+262]; alloriginalsdied2470updatesearlier. Everyfollowingheadcut until88368+208n staysinthatrectangle. ExactNW104ray equations give firstW atperiod77phase90,(-2,372),W; gap58697+104n.',
'Acrossfamilyunboundeddrought withfixed22seedsize, nooriginalsleft andcurrentrelevance1082 refutesonlyuniformresetclock proposals. Everymembercaptures. Thisdoesnotproduceonefiniteorbitwitharbitrarylateunboundeddroughts orproveuniversaltranslation.'
]);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
