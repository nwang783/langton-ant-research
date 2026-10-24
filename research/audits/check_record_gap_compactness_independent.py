from pathlib import Path
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'RECORD_GAP_COMPACTNESS_MANIFEST.json'
assert sha(MF)=='f9336d6755b0de327381255365b0275d92222b6bb379159309e013c0c34bd968';mf=json.loads(MF.read_text())
for kind in ('files','dependencies'):
 for f,h in mf[kind].items():assert sha(D/f)==h
J=json.loads((D/'RECORD_GAP_COMPACTNESS_CHECKED.json').read_text());A=json.loads((D/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());Rj=json.loads((D/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text())
ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);K,xy,geometry,sim,cert,key,future=[ns[k] for k in ('K','xy','geometry','sim','cert','key','future')]
enc=lambda q:sorted(map(xy,q));dec=lambda q:{complex(*p)for p in q};d=2+2j;W=sim(K,104)['word'];qm=202+201j;r=8470;kernel=dec(A['T_kernel']);T=A['T_recovery'];pure=cert(sim(kernel,len(T),0j,0,T,cuts={r}),A['T_tail_word']);B,p,h=pure['snap'][r];assert(p,h)==(3+33j,0)
local={q for q,i in B.items() if i in pure['dead']};assert len(local)==296 and enc(local)==J['local_pruning'];assert max(q.imag for q in pure['pts'][:r])==32 and max(q.imag for q in pure['pts'])==33
remote=dec(A['exact_entry_pruning']['remote']);assert len(remote)==786
assert max(pure['dead'][i] for q,i in B.items() if q in local)<21004
assert min(q.real for q in B)>=-38
L={q-p for q in local};assert enc(L)==J['limit']['seed'] and max(max(abs(q.real),abs(q.imag))for q in L)==48 and all(q.imag<0 for q in L)
lim=cert(sim(L,len(T)-r,0j,0,T[r:]),J['limit']['tail_word']);assert enc(lim['B'])==J['limit']['complete_output_black'] and [xy(lim['p']),lim['h']]==J['limit']['output_pose'] and lim['tests']==J['limit']['parity_tests'] and lim['d']==-d
assert all(-i-1 in lim['dead'] for i in range(len(L)))
lq,lh,_,_=geometry(lim['p'],lim['h'],lim['tail']);assert max(q.imag for q in lim['pts']+lq)==0 and lim['d'].imag<0
# Reconstruct the entire infinite normalized record-limit field, not a bounded box.
Q,H,_,_=geometry(0j,1,W);assert Q[13]==2+1j and H[13]==0
anchors=[q-Q[13]+(0 if i<13 else -1)*d-(3+33j) for i,q in enumerate(Q)]
fixed={a*d for a in(0,1,3,5,6)}
for q in pure['pts'][:r]:fixed.symmetric_difference_update({q})
fixed={q-3-33j for q in fixed}
assert list(map(xy,anchors))==J['full_record_limit']['backward_ray_anchors'] and enc(fixed)==J['full_record_limit']['finite_XOR_mask']
assert max(q.imag for q in anchors+list(fixed))<0
v=-d

def along(q,p,step):
 x=(q-p).real/step.real
 return int(x) if x==int(x) and q-p==int(x)*step else None

def color(q,extra=()):
 bit=int(q in fixed)^int(q in extra)
 for a in anchors:
  k=along(q,a,v)
  if k is not None and k>=0:bit^=1
 return bit
# Verify initial-color equality between full infinite field and finite296 pruning
# at EVERY finite future read and every future translated tail ray.
for q in lim['pts']:assert color(q,L)==0
raychecks=0
for q in lq:
 tests={0}
 for a in anchors:
  t=along(q,a,v)
  if t is not None:tests.add(max(0,-t))
 for a in fixed^L:
  k=along(a,q,v)
  if k is not None and k>=0:tests.update((k,k+1))
 for k in tests:assert color(q+k*v,L)==0,(q,k)
 raychecks+=len(tests)
# Whole field-difference support at all n: cancel the identical free flight
# and T prefix, bounding both preflight fields BEFORE those common updates.
pre_fixed=W*100+W[:13]+Rj['modes']['M']['recovery_word'];base_seed=K|{qm+a*d for a in(0,1,6,8)};old=sim(base_seed,len(pre_fixed),expected=pre_fixed)
assert old['p']==qm+26+28j and old['h']==H[41]
assert max(q.imag for q in old['B'])==232
phase41_anchors=[old['p']+q-Q[41]+(0 if i<41 else -1)*d for i,q in enumerate(Q)]
assert max(q.imag for q in phase41_anchors)==232
flight=W[41:]+W[:41];fq,fh,end,hh=geometry(old['p'],old['h'],flight);assert end-old['p']==d and hh==old['h'];partial,_,pe,ph=geometry(old['p'],old['h'],flight[:76]);assert(pe,ph)==(qm+28+28j,0)
# Thus discrepancy y<=232 at preflight remains at same physical sites.
# At record head qT+(3,33), this is exactly normalized y<=-2n-30.
for n in (100,137,500):assert 232-(qm.imag+2*n+28+33)==-2*n-30
# Prior full head heights make the selected T record genuinely historical.
fp,_,_,_=geometry(0j,1,pre_fixed)
assert max(q.imag for q in fp)<qm.imag+228+33
assert max(q.imag for q in fq)-2 <= qm.imag+28+32
assert max(q.imag for q in partial)<=qm.imag+28+32
# Exact first record on the whole final NW future, all phase equations.
NW=A['controls'][0]['complete_future_certificate']['tail_word'];nq,nh,_,_=geometry(155+215j,1,NW);hits=[]
for i,q in enumerate(nq):
 if (263-int(q.imag))%2==0:
  c=(263-int(q.imag))//2;assert c+100>=0;hits.append(dict(phase=i,period_offset=c,time_offset=104*c+i,phase_point=xy(q),heading=nh[i]))
hits.sort(key=lambda z:z['time_offset']);assert hits==J['all_next_N_phase_equations'] and hits[0]==dict(phase=43,period_offset=22,time_offset=2331,phase_point=[158,219],heading=0)
# Postcollision recovery is at fixed absolute pose; every read remains below250.
# Reconstruct the independently signed n100 event rather than guessing the frame.
a100=A['controls'][0]
print('full infinite limit checked',raychecks,'critical ray tests',flush=True)
controls=[];total=0
for row in J['controls']:
 n=row['n'];qt=qm+(n+14)*d;seed=base_seed|{qt+a*d for a in(0,1,3,5,6)};assert len(seed)==22 and enc(seed)==row['seed']
 pre=pre_fixed+flight*n+flight[:76];tT=len(pre);last=tT+r;assert tT==21201+104*n and last==29671+104*n
 word=pre+T+A['T_tail_word']*(n-7)+A['T_tail_word'][:100]+'L'+A['postcollision_word'];term=len(word);assert term==80270+208*n
 nextcut=term+104*(n+22)+43;full=word+NW*(n+22)+NW[:43];assert len(full)==nextcut==82601+312*n and nextcut-last==52930+208*n
 z=cert(sim(seed,len(full),expected=full,cuts={last,term}),row['tail_word']);bf,p,h=z['snap'][last]
 assert p==qt+3+33j and h==0 and sorted([[xy(q),i]for q,i in bf.items()])==row['whole_last_N_black']
 assert max(z['dead'][i]for i in range(-len(seed),0))==tT+6000 and all(i>=0 for i in bf.values())
 assert max(q.imag for q in seed)<p.imag and max(q.imag for q in z['pts'][:last])==p.imag-1 and all(q.imag<p.imag for q in bf)
 assert max(q.imag for q in z['pts'][last:])==p.imag and z['p'].imag==p.imag+1 and z['h']==0
 C={q for q,i in bf.items()if i in z['dead']};assert C=={qt+q for q in local}|remote and enc(C)==row['entire_last_N_pruning'] and len(C)==1082
 rho=max(max(abs((q-p).real),abs((q-p).imag)) for q in C);assert rho==2*n+100==row['last_rho']
 # Exact entire discrepancy support against infinite limit, not just author81x81 box.
 nf={q-p for q in bf};threshold=-2*n-30
 for q in nf:
  if q.imag>threshold:assert color(q)==1
 for a in anchors:
  k=0
  while (a+k*v).imag>threshold:
   q=a+k*v;assert (q in nf)==bool(color(q));k+=1
 for q in fixed:
  if q.imag>threshold:assert(q in nf)==bool(color(q))
 poststart=term-len(A['postcollision_word']);assert max(q.imag for q in z['pts'][poststart:term])==250
 assert z['snap'][term][1:]==(155+215j,1)
 assert enc(z['B'])==row['whole_next_black'] and [xy(z['p']),z['h']]==row['next_pose'] and z['p']==114-2*n+(263+2*n)*1j
 _,_,deaths,tests=future(z['B'],z['p'],z['h']);NC={q for q,i in z['B'].items()if i in deaths};assert enc(NC)==row['next_entire_pruning'] and len(NC)==13 and max(max(abs((q-z['p']).real),abs((q-z['p']).imag)) for q in NC)==5
 assert z['tail']==W[14:]+W[:14] and z['d']==-2+2j and z['tests']==row['infinite_parity_tests'] and all(q.imag<z['p'].imag for q in z['B'])
 controls.append(dict(n=n,reads=len(full),last=last,next=nextcut,gap=nextcut-last,rho=rho,next_relevance=13,next_rho=5));total+=len(full)
assert total==477747
O=dict(status='PASS fixed-axis bounded-record-gap compactness bridge and all-n nonclosedness control only',manifest=sha(MF),script=sha(S),limit_relevant_count=296,limit_relevant_radius=48,infinite_limit_critical_ray_tests=raychecks,all_n_full_difference_upper_y='-2n-30',old_field_and_synthetic_max_y=232,controls=controls,full_reads=total,analytic_review=[
'For infinitely many records in one fixed signed axis, unit steps give consecutive record levels. If every sufficiently late gap is<=H, choose tau_k<=b<tau_(k+1),tau_j<=d<tau_(j+1) for the same-cell R birth/L death. At death the head has retreated at most H-1 from j; birth coordinate<=k, so j<=k+H-1 and d<b+H^2. This uses actual integer cuts and no nesting/resource hypothesis.',
'Choose the threshold record beyond the finite original black hull. Every current old bit then has axis coordinate<k0. At every cut after tau_(k0+H), the head coordinate is>=k0+1, so no old-at-threshold bit is ever read again. Entire C* thereafter consists of late-born bounded-age lifetimes and rho<H^2. The onset bound tau_k0+H^2 is valid. Finite normalized relevant-state recurrence forces a translator; infinite positive-axis records force positive drift, not zero or opposite drift. The state count bounds recurrence after this onset, not a uniform initial waiting time or an effective C* computation.',
'The converse can be seen directly: in a late actual translator, p_(tau_k+P)=p_(tau_k)+d with positive axis projection, hence tau_(k+1)<=tau_k+P. Directions with only finitely many records are excluded. Nontranslation therefore forces unbounded consecutive record gaps in each infinite-record direction; no canonical104 uniqueness follows.',
'Normalized genuine pristine record states have head0 and incoming heading equal to the signed axis, with the whole forward closed half-plane WHITE. Finite-time crossing domains are clopen in the compact old-side product space. A compact accumulation set entirely in the open next-record domain has one finite uniform crossing horizon, and eventually all sequence points share it. Conversely unbounded gaps supply a never-crossing accumulation point. Its support may be infinite and its future may capture inward or tangentially; it is not an attraction counterexample.',
'An outward translating limit reads only finitely many old-side sites: each tail ray has positive axis speed and contributes the stated finite ceiling count. Agreement on those initial colors and the pristine forward half-plane forces the whole future, and deleting all other initiallyBLACK sites produces a finite realizing board. Thus the outward-translator basin is open relative to record states. Infinite old-side exposure conversely prevents any finite initial spatial cylinder from forcing that exact whole word, since one uninspected first-read bit can be flipped.',
'The complete all-n MT control is rebuilt from its signed full source. At T+8470 the north record is genuine and all originals already died by T+6000. True relevant set is296 local+786 fixed remote, rho2n+100. Pure local lifetimes die before the earliest remote collision; other local bits lie east of the whole postreturn quadrant, while all786 old inputs remain unread until feedback. Next record is exactly phase43/periodn+22 of the fixed NW tail, giving gap52930+208n, then trueC13/radius5 and canonical phase14.',
'The full infinite local-limit field is reconstructed as104 backward rays XOR the exact finite mask. Crucially, both actual complete preflight field and phase41 synthetic past have max absolutey232. Cancelling the common arbitrary free flight and T prefix yields the ENTIRE difference support normalizedy<=-2n-30. Independently checked all finite future reads and every infinite tail-ray critical parity against the finite296 pruning; the infinite limit truly has the same nonreturning SW future, not merely the same bounded initial box.',
'Three full histories477747 reads retain complete boards, all lifetime owners, first-next-record chronology and exact infinite futures. Across-family diverging waits and the nonclosed next-record domain do not yield a single nontranslating finite orbit, a universal record-gap bound, or canonical translating-front uniqueness.'
]);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
