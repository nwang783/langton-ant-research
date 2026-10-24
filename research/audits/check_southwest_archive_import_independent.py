from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'SOUTHWEST_ARCHIVE_IMPORT_MANIFEST.json'
assert sha(MF)=='bbd355881af85e24445f23d7d99d1eba88d5519ec5487c920b07f39892c5cf66'
m=json.loads(MF.read_text())
for kind in ('files','dependencies'):
 for f,h in m[kind].items():assert sha(D/f)==h
J=json.loads((D/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());MJ=json.loads((D/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text())
ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns)
K,V,xy,future,phases,geometry,sim,cert,key=[ns[k]for k in('K','V','xy','future','phases','geometry','sim','cert','key')]
enc=lambda q:sorted(map(xy,q));dec=lambda q:{complex(*p)for p in q};normal=lambda q:int(q.real-q.imag);d=2+2j
W=sim(K,104)['word'];assert W==MJ['W'];Q,H,_,_=geometry(0j,1,W);assert Q[13]==2+1j and H[13]==0
# Fresh southern complete comparison board, all prior rays, no author implementation.
B=set()
for i,p in enumerate(Q):
 r=p-Q[13]
 for a in range(-((int(r.imag)+15)//2),1 if i<13 else 0):B.symmetric_difference_update({r+a*d})
A={a*d for a in (0,1,3,5,6)};assert not A&B;seedT=B|A;assert len(seedT)==117 and enc(seedT)==J['T_kernel']
T=cert(sim(seedT,11232,0j,0,J['T_recovery']),J['T_tail_word']);assert(T['p'],T['h'],T['d'])==(-36-10j,0,-d)and enc(T['B'])==J['T_output_black']and T['tests']==J['T_parity_tests']
TQ,TH,_,_=geometry(T['p'],T['h'],T['tail']);assert min(p.imag for p in T['pts'])==-15 and (min(map(normal,TQ)),max(map(normal,TQ)))==(-32,-22)
assert (min(normal(p-Q[13])for p in Q),max(normal(p-Q[13])for p in Q))==(-8,2)
assert all(-8<=normal(p)-1<=2 for p in K)
local={q for i,q in enumerate(sorted(seedT,key=key))if -i-1 in T['dead']};assert len(local)==99 and max(max(abs(q.real),abs(q.imag))for q in local)==18 and all(T['dead'][-i-1]<11232 for i,q in enumerate(sorted(seedT,key=key))if q in local)
assert enc(local)==J['exact_entry_pruning']['local'] and [T['first'][a*d]for a in (0,1,3,5,6)]==[0,124,672,5984,6000]and [T['first'][a*d]for a in (2,4)]==[632,4028]
# Reconstruct M, actual output lifetimes, and all exact return-ray intersections.
M=cert(sim(dec(MJ['modes']['M']['kernel']),10712,0j,0,MJ['modes']['M']['recovery_word']),W[41:]+W[:41]);assert len(M['B'])==719 and M['B'][4+28j]==9752 and 9752 not in M['dead']
assert max(q.imag for q in M['B'])==31
FQ,FH,_,_=geometry(M['p'],M['h'],M['tail']);assert all(-8<=normal(p)<=2 for p in FQ)
assert max(M['p'].imag+Q[i].imag-Q[41].imag+(0 if i<41 else-2)for i in range(104))<=31
hits=[]
for r,iid in sorted(M['B'].items(),key=lambda z:key(z[0])):
 for i,s in enumerate(TQ):
  u=r-28*(1+1j)-s
  if u.real==u.imag and int(u.real)%2==0:
   off=-int(u.real)//2;assert 100+off>=0;hits.append(dict(cell=xy(r),identity=iid,phase=i,period_offset=off,time_offset=11232+104*off+i))
hits.sort(key=lambda z:z['time_offset']);assert hits==J['all_affine_old_output_hits'] and len(hits)==384
assert hits[0]==dict(cell=[4,28],identity=9752,phase=100,period_offset=-7,time_offset=10604)and hits[1]['time_offset']>10604 and TH[100]==2 and T['tail'][100]=='R'
qm=202+201j;TM=10413;source=W*100+W[:13];base_seed=K|{qm+a*d for a in (0,1,6,8)};baseword=source+M['word'];base=sim(base_seed,len(baseword),expected=baseword)
assert enc(base['B'])==J['base_after_M']['full_black'] and base['B'][qm+4+28j]==TM+9752
strip=lambda q:-32<=normal(q-qm)<=-22
actual={p-qm:i-TM for p,i in base['B'].items()if strip(p)};ref={p:i for p,i in M['B'].items()if -32<=normal(p)<=-22};assert actual==ref and len(ref)==82
# Stronger outside-standard restriction proves no other old defect can precede those hits.
assert {p-qm for p in base['B']if not -8<=normal(p-qm)<=2}=={p for p in M['B']if not -8<=normal(p)<=2}
def odd(P):
 B=set()
 for p in P:B.symmetric_difference_update({p})
 return B
def shift(B,p):return {q+p for q in B}
def segments(n):
 qt=qm+(n+14)*d
 return ([(p,0j,1)for p in sorted(base['B'],key=key)]+[(qt+a*d,0j,1)for a in (0,1,3,5,6)]+[(qm+p,d,n)for p in sorted(odd(FQ),key=key)]+[(qm+p+n*d,0j,1)for p in sorted(odd(FQ[:76]),key=key)]+[(qt+p,0j,1)for p in sorted(odd(T['pts']),key=key)]+[(qt+p,-d,n-7)for p in sorted(odd(TQ),key=key)]+[(qt+p-(n-7)*d,0j,1)for p in sorted(odd(TQ[:100]),key=key)])
def expand(ts):
 B=set()
 for p,v,n in ts:
  for i in range(n):B.symmetric_difference_update({p+i*v})
 return B
qt0=qm+114*d
C=shift(A,qt0)^shift(odd(FQ[:76]),qm+100*d)^shift(odd(T['pts']),qt0)
D0=shift(odd(FQ),qm+100*d)^shift(odd(TQ),qt0+d)
assert enc(C)==J['all_n_difference']['cap']and enc(D0)==J['all_n_difference']['strand']and min(p.real for p in C|D0)==392
# Algebraic reindexing: SW train has n-7 terms at qt_n-j*d.
# Its common low endpoint qt_n-(n-8)*d = qm+22*d is n-independent.
# New high terms for n=100+k are qt0+(r+1)*d, 0<=r<k.
for n in (100,101,137,500,10**9):
 assert qm+(n+14)*d-(n-8)*d==qm+22*d
 assert qm+(n+14)*d-(n-7)*d==qm+21*d
 assert n-7>0
post=(D/'SOUTHWEST_POSTIMPORT_WORD.txt').read_text().strip();assert len(post)==48464 and post==J['postcollision_word']
B100=expand(segments(100));controls=[];remote=None;mfixed=None;future_max=None
for row in J['controls']:
 n=row['n'];qt=qm+(n+14)*d;seed=base_seed|shift(A,qt);assert len(seed)==22 and enc(seed)==row['initial_seed'];tT=TM+10788+104*n;ev=TM+21392+208*n
 prefix=baseword+M['tail']*n+M['tail'][:76]+T['word']+T['tail']*(n-7)+T['tail'][:100];assert len(prefix)==ev and hashlib.sha256(prefix.encode()).hexdigest()==row['prefix_sha256'];full=prefix+'L'+post
 z=cert(sim(seed,len(full),expected=full,cuts={TM,tT,ev,ev+1}),row['complete_future_certificate']['tail_word']);assert(z['p'],z['h'],z['d'])==(155+215j,1,-2+2j)
 MB,mp,mh=z['snap'][TM];B,p,h=z['snap'][tT];pre,ep,eh=z['snap'][ev];after,ap,ah=z['snap'][ev+1]
 assert(p,h)==(qt,0)and{q-qt for q in B if q.imag>=qt.imag-15}==seedT
 assert(ep,eh)==(qm+4+28j,2)and pre[ep]==TM+9752 and z['events'][ev]==TM+9752 and z['dead'][TM+9752]==ev and(ap,ah)==(207+229j,1)
 assert sorted([[xy(q),i]for q,i in B.items()])==row['whole_contact_black']and sorted([[xy(q),i]for q,i in pre.items()])==row['whole_pre_event_black']and enc(after)==row['whole_post_event_black']
 ts=segments(n);assert [[xy(p),xy(v),k]for p,v,k in ts]==row['symbolic_terms']and expand(ts)==set(pre)
 delta=C^shift(C,(n-100)*d)^expand([(p,d,n-100)for p in D0]);assert set(pre)^B100==delta and all(q.real>=392 for q in delta)
 tq,_,_,_=geometry(z['p'],z['h'],z['tail']);assert max(q.real for q in z['pts'][ev+1:]+tq)==240 and z['d'].real<0
 assert enc(z['B'])==row['complete_future_certificate']['terminal_full_black']and z['tests']==row['complete_future_certificate']['full_parity_tests']and len(full)==80270+208*n
 Cstar={q for q,i in B.items()if i in z['dead']};assert enc(Cstar)==row['actual_entire_entry_pruning']and len(Cstar)==885
 loc=shift(local,qt);rem=Cstar-loc;assert loc<=Cstar and len(rem)==786
 assert (min(q.real for q in rem),max(q.real for q in rem),min(q.imag for q in rem),max(q.imag for q in rem))==(158,225,162,229)
 if remote is None:remote=rem
 assert rem==remote and max(max(abs((q-qt).real),abs((q-qt).imag))for q in Cstar)==2*n+72
 mc={q for q,i in MB.items()if i in z['dead']};fixed=mc-shift(A,qt)
 if mfixed is None:mfixed=fixed
 assert fixed==mfixed and len(mc)==259 and len(fixed)==254 and enc(mc)==row['actual_first_M_entry_pruning']and max(max(abs((q-qm).real),abs((q-qm).imag))for q in mc)==2*n+40
 mref=shift(dec(MJ['modes']['M']['entire_comparison_pruning']),qm);assert mref<=fixed and len(fixed-mref)==128 and sum(p.real>=qm.real-23 for p in fixed-mref)==21
 assert {p-qm for p in fixed if p.real>=qm.real-23}==dec(MJ['modes']['M']['kernel'])
 assert [z['first'][qm+a*d]for a in(0,1,6,8)]==[TM+i for i in(0,124,1272,5028)]and [z['first'][qt+a*d]for a in(0,1,3,5,6)]==[tT+i for i in(0,124,672,5984,6000)]
 assert [dict(cell=xy(q),time=z['first'][q])for q in sorted(seed,key=key)]==row['original_first_reads']
 if n==100:
  # The entire pre-T field at x<=240 is stable for ALL larger n: new flight
  # terms start at min(qm+100d+FQ)>240, moving partial/cap still farther east.
  assert min(q.real for q in shift(set(FQ),qm+100*d))>240
  assert min(q.real for q in shift(A,qt0)|shift(set(FQ[:76]),qm+100*d))>240
  assert max(q.imag for q in MB if q not in shift(A,qt))<qt.imag-15
  assert max(q.real for q in base['B'])<min(q.real for q in shift(set(TQ),qt0+d))
 controls.append(dict(n=n,full_reads=len(full),old_age=ev-TM-9752,T_relevant=len(Cstar),M_relevant=len(mc),radii=[2*n+40,2*n+72],parity_checks=z['tests']))
assert enc(remote)==J['exact_entry_pruning']['remote']and enc(mfixed)==J['exact_entry_pruning']['first_M_fixed_cohort']
# Pure no-M all-k branch: source/synthetic prestart lies below guard for k>=11,
# and entirely in the incoming transverse strip, disjoint from the later SW rays.
assert max(max(q.imag for q in K),max(q.imag for q in Q)-2)==6
assert 2*11+1-15==8>6
pure=[]
for row in J['pure_controls']:
 n=row['n'];qt=2*n+2+(2*n+1)*1j;seed=K|shift(A,qt);prefix=W*n+W[:13]+T['word'];z=cert(sim(seed,len(prefix),expected=prefix),T['tail']);assert enc(seed)==row['seed']and enc(z['B'])==row['complete_terminal_black']and[xy(z['p']),z['h']]==row['terminal_pose']and xy(z['d'])==row['tail_drift']and z['tests']==row['parity_tests'];pure.append(dict(n=n,reads=len(prefix),parity_checks=z['tests']))
huge=J['huge_symbolic_control'];n=huge['n'];assert n==10**9 and [[xy(p),xy(v),k]for p,v,k in segments(n)]==huge['full_pre_event_terms']and len(segments(n))==huge['term_count']and huge['event_relative_T']==104*n+10604 and huge['age']==208*n+11640
out=dict(status='PASS all-n southwest archive-import, whole-field capture and exact rho increase',manifest=sha(MF),script=sha(S),return_intersections=len(hits),T_kernel=len(seedT),T_pruning=len(local),remote_pruning=len(remote),all_n_difference_min_x=392,all_future_max_x=240,controls=controls,pure_controls=pure,analytic_review=[
'All-n prefix transfer is an ENTIRE southern-half-plane equality. Every pre-flight actual M/source or omitted synthetic phase41 cell has bounded y<=qM.y+31, while T guard is qM.y+2n+13. Fresh phase13 ray ordering prevents earlier paid-marker reads. No discarded archive is assumed WHITE.',
'Outside the incoming standard strip the complete actual fixed source output equals the M719 comparison. The SW strip is disjoint from the incoming standard strip. All384 exact ray encounters are compared; the unique first is real M R9752 at phase100,k=n-7, reference R versus actual L. Reference-never-read does NOT mean actual permanent.',
'The complete XOR formula is derived by parity of every executed read, retaining source, moving paid T bits, incoming train and partial phase, finite T recovery, backward train and partial phase. Reindexing the SW train gives fixed lower endpoint qm+22d and new high endpoints qt100+(r+1)d. Its final partial mask has fixed origin qm+21d. Thus the exact parameter difference is C XOR translatedC XOR forwardDtrain, with all support x>=392. The complete n100 postcollision future has x<=240 including its infinite NW rays. First-difference induction transfers the literal48464 word and full infinite tail to EVERY n>=100, not just the three finite replays.',
'At T entry all varying incoming-strip cells can be read only by the finite local prefix, which consumes exactly99. The returning strip cannot consume remaining incoming-strip current cells; its extra high periods for larger n are beyond the fixed M output. The pre-T board in x<=240 is parameter-independent, and the entire postcollision future is fixed there. Therefore all786 other future-consumed current cells are the same physical set, not a sampled extrapolation. At M entry the finite fixed board is below every T guard; only the five paid T inputs move. The same finite/reference/return/postfuture partition proves the fixed254+5 input decomposition.',
'Exact full C* radii are2n+40 then2n+72, an increase32 even across an outward paid packet step. All nine original packet bits are actually first-read and all full fields retained. This defeats extending the specific NE S/M sampled clipped-radius potential over this T exit, not arbitrary mode-dependent potentials or eventual compact recurrence.',
'Three complete22-cell controls and three pure18-cell controls pass fresh vector-heading simulation and independent all-ray parity certificates. All-n capture is sufficient at80270+208n, not asserted earliest. No arbitrary archive closure, autonomous regeneration, global occurrence or attraction conclusion.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')));print(controls)
