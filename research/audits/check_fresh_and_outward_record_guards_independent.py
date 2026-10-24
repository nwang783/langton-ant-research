from pathlib import Path
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
mb={}
for fn in ['FRESH_RECORD_TRAP_BRIDGE_MANIFEST.json','OUTWARD_RECORD_GUARDS_MANIFEST.json']:
 m=json.loads((P/fn).read_text());mb[fn]=m
 for k,h in m.items():assert sha(P/k)==h,(k,sha(P/k))
# Exact independent finite replay and all-infinite-phase change-point engine from the signed11-cell audit.
x={'__file__':str(S.parent/'check_eleven_cell_terminal_trap_independent.py')};s=(S.parent/'check_eleven_cell_terminal_trap_independent.py').read_text();exec(s[:s.index('B,p,h,reads,dead=replay(I,0j,2,C)')],x)
replay=x['replay'];tail=x['tail'];multiple=x['multiple'];xy=x['xy'];V=x['V'];C11=x['C'];H=x['H'];I11=x['I'];J={0+2j,0+3j,1+1j,2+4j,3+2j,3+3j};C=C11[46:]
fresh=json.loads((P/'FRESH_RECORD_TRAP_BRIDGE_CHECKED.json').read_text());outward=json.loads((P/'OUTWARD_RECORD_GUARDS_CHECKED.json').read_text())
# Actual strict record at source46, not just an assigned favorable half-plane.
B46,p46,h46,prior,_=replay(I11,0j,2,C11[:46]);assert p46==-9-3j and h46==2
assert min(q.imag for q in I11|set(prior))>=-2 and min((q-p46).imag for q in B46)>=1
B,p,h,reads,_=replay(J,0j,2,C);assert len(C)==232 and(p,h)==(-2j,2);qs,d,tc=tail(B,p,h);assert d==2-2j and max(z.imag for z in qs)==-1
G={q for q in set(reads+qs)if q.imag>=1};assert len(G)==29 and J<=G and G<=set(reads);assert {q-p46 for q in B46}&G==J and len(B46)==15
F='RRRRLR';GG='RRRLLLLRLR';assert C[:16]==F+GG
assert all(q.imag>-1 for q in reads[:6])and reads[6]==1-1j and all(q.imag>-2 for q in reads[:16])and reads[16]==2-2j
assert sum(V[(2+sum(1 if c=='R'else-1 for c in C[:t+1]))%4].imag==1 for t in range(16))==3
old16={q for q in reads[:16]if q.imag>=1};assert old16=={-1+1j,1j,1+1j};free=G-old16;assert len(free)==26 and len(free&J)==5
variants=[]
for q in sorted(free,key=xy):
 t=reads.index(q);initial=J^{q};bb,pp,hh,rr,_=replay(initial,0j,2,C[:t]);assert pp==q and ('L'if q in bb else'R')!=C[t]
 # Every perturbation has the same sharp prefix, and has a genuine preceding L sponsor.
 _,end,heading,_,_=replay(initial,0j,2,C[:16]);assert(end,heading)==(2-2j,2)
 jj,pp,hh,_,_=replay(initial|{1j},1j,3,'L');assert(jj,pp,hh)==(initial,0j,2)
 variants.append({'cell':list(xy(q)),'required_black':q in J,'first_disagreement':t,'initial_black':sorted(map(list,map(xy,initial)))})
assert variants==fresh['sharp_two_record_prefix']['one_bit_controls']
source={1j,2j,3j,2+4j,3+2j,3+3j};prefix='RL'+C;bb,pp,hh,rr,_=replay(source,1+1j,2,prefix);assert(bb,pp,hh)==(B,p,h)
assert min(z.real+z.imag for z in source)==1 and rr[12]==1+1j and all(z!=1+1j for z in rr[1:12])
_,pr,hr,r12,_=replay(source,1+1j,2,prefix[:12]);assert(pr,hr)==(1+1j,0)and prefix[1:7]=='LRRRRL'and sum(z.real+z.imag==-1 for z in r12)==2
base=5-4j;preparams=sorted({multiple(z-base,d)for z in rr if multiple(z-base,d)is not None});assert preparams==[-3,-2,-1]
ray=[]
for i,q in enumerate(qs):
 k=multiple(base-q,d)
 if k is not None:ray.append((i,k,104*k+i))
assert min(z[2]for z in ray)==45 and all(k>=0 for _,k,_ in ray)and qs[45]==base and H[45]=='R'
assert sorted(t for _,_,t in ray)==[45,49,53,65,109,185,201]
controls=[]
for K in(0,1,2,11,40):
 a=base+K*d;word=prefix+H*K+H[:45];b,head,heading,_,_=replay(source|{a},1+1j,2,word);assert len(source|{a})==7 and head==a and a in b and len(word)==279+104*K
 controls.append({'K':K,'cell':xy(a),'first_actual_R_to_L_disagreement':len(word)})
# For ALL K, each candidate tail hit has epoch K+k>=0 and time234+104K+(104k+i).
# All prefix hits have negative parameter, so the minimum45 is exact and independent of K.
axis=fresh['six_cell_axis_pristine_criterion'];assert set(map(tuple,axis['guard']))==set(map(xy,G))and axis['prefix']==C and axis['period']==H
assert set(map(tuple,axis['guard_required_black']))==set(map(xy,J))and{(tuple(q),t)for q,t in axis['guard_first_reads']}=={(xy(q),reads.index(q))for q in G}
# Complete record catalogue from literal geometry, then exact full-board controls.
_,dd,hh,Q,_=replay([],0j,2,H,False);assert dd==d and hh==2;headings=[];hh=2
for c in H:headings.append(hh);hh=(hh+(1 if c=='R'else-1))%4
catalog=[];flipcount=0;fullfields=[]
for tab in outward['normal_catalog']:
 n=complex(*tab['outward_normal']);f=lambda z:int(n.real*z.real+n.imag*z.imag);a=f(d);assert a>0
 peak=max(map(f,Q));record=[i for i,q in enumerate(Q)if f(q)>max([peak-a]+[f(z)for z in Q[:i]])]
 assert record==tab['complete_strict_record_phases']
 K0=tab['valid_from_epoch'];board,head,heading,hist,_=replay(J,0j,2,C+H*K0);past=set(J)|set(hist)
 for i,c in enumerate(H):
  if i in record:
   z=next(r for r in tab['records']if r['phase']==i);assert head==complex(*z['actual_control_pose'][0])and heading==z['normalized_heading']==headings[i]
   assert f(head)>max(map(f,past)) and all(f(q)<f(head)for q in board)
   assert board==set(map(lambda q:complex(*q),z['full_actual_control_board']))
   W=H[i:]+H[:i];_,end,hw,vs,_=replay([],0j,heading,W,False);assert end==d and hw==heading
   guard={v+k*d for v in vs for k in range(max(0,(-1-f(v))//a+1))};first={}
   for v in guard:
    times=[(104*k+j,W[j])for j,q in enumerate(vs)if(k:=multiple(v-q,d))is not None and k>=0];first[v]=min(times)
   black={q for q,(t,c0)in first.items()if c0=='L'}
   # Use the same independent exact ray engine with this cyclic word, not sampled repetition.
   oldH=x['H'];x['H']=W;vcheck,dd,proof=tail(black,0j,heading);x['H']=oldH
   assert dd==d and vcheck==vs
   assert{q-head for q in board}&guard==black
   assert len(guard)==z['guard_size']and len(black)==z['black_size']and max(t for t,c0 in first.values())==z['max_old_read_time']
   assert set(map(xy,guard))==set(map(tuple,z['old_guard']))and set(map(xy,black))==set(map(tuple,z['required_black']))
   assert{(tuple(q),t,c0)for q,t,c0 in z['guard_first_reads']}=={(xy(q),t,c0)for q,(t,c0)in first.items()}
   rec={'normal':xy(n),'phase':i,'guard':len(guard),'black':len(black),'white':len(guard-black),'last_old_first_read':max(t for t,c0 in first.values()),'full_actual_board_mass':len(board),'all_infinite_ray_tests':sum(len(t['all_change_point_tests'])for t in proof)}
   if 'fresh_first_return_comparison'in z:
    v=z['fresh_first_return_comparison'];start=-1+1j;sponsor=-1+0j;probe=1j;initial=(black-{start})|{sponsor};duration=8 if i==45 else 12
    word='RL'+W[:duration-2];br,pr,hr,rp,_=replay(initial,start,1,word);assert(pr,hr)==(start,3)and all(q!=start for q in rp[1:])
    assert word==('RLRRRRLL'if i==45 else'RLRRRRLRRRRL')
    old={q for q in rp if f(q)<0};assert old=={start,sponsor,probe}and sum(f(q)==1 for q in rp)==(1 if i==45 else 2)
    assert set(map(xy,initial))==set(map(tuple,v['base_initial_black']))
    changes=[]
    for q in sorted(guard-old,key=xy):
     bb,pp,hh,rp2,_=replay(initial^{q},start,1,word);assert rp2==rp and(pp,hh)==(pr,hr)
     t,c0=first[q];_,_,_,_,_=replay(black^{q},0j,heading,(W*((t//104)+1))[:t])
     b2,p2,h2,_,_=replay(black^{q},0j,heading,(W*((t//104)+1))[:t]);assert p2==q and('L'if p2 in b2 else'R')!=c0
     changes.append({'flip_cell':list(xy(q)),'required_black':q in black,'first_disagreement_from_record_cut':t})
    assert changes==v['one_bit_controls'];flipcount+=len(changes);rec['literal_unchanged_first_return_flip_controls']=len(changes)
   catalog.append(rec)
  past.add(head);board,head,heading,_,_=replay(board,head,heading,c)
assert len(catalog)==8 and flipcount==43
assert [(r['phase'],r['guard'],r['black'])for r in catalog]==[(61,44,19),(71,55,19),(14,29,13),(28,35,14),(45,19,15),(46,25,16),(55,30,15),(56,36,16)]
out={'status':'PASS two universal sufficient record-guard constructions, all-K constant-mass tangent obstruction, eight exact H record guards; no universal attraction','bindings':mb,'source46_actual_strict_record':{'head':xy(p46),'heading':h46,'full_normalized_black':sorted(map(xy,{q-p46 for q in B46})),'six_guard_black':sorted(map(xy,J))},'six_black_guard':{'size':29,'black':6,'white':23,'unconstrained_after_sharp_two_record_prefix':26,'black_unconstrained':5,'white_unconstrained':21},'all_K_tangent_proof':{'prefix_ray_parameters':preparams,'all_tail_phase_epoch_time_offsets':ray,'minimum_time_offset':45,'tail_entry':234,'formula':'279+104K for every integer K>=0','literal_additional_controls':controls},'outward_record_catalogue':catalog,'unchanged_true_record_return_flip_controls':flipcount,'analytic_review':[
'The actual11-cell source reaches strict new south record at time46 with15 actual black cells after translation, six matching guard blacks and nine unread exterior cells, all at y>=1. Its232-step prefix and infinite H tail are verified by all phase-pair/initial-bit change points. All29 old-side queried cells occur in the finite prefix; later H footprints remainy<=-1 and translate outward. First-difference induction proves the sufficient guard for arbitrary unread old-side background, and first queried bit proves necessity only for this EXACT proposed future.',
'The sharp FG16 prefix fixes only three old bits. All26 independent flips retain that actual prefix, strict crossings and an explicit preceding-L sponsor, then disagree at the exact first query. This refutes inferring this guard from that itinerary, not eventual capture of the perturbed seeds.',
'The diagonal six-cell seed realizes actual sponsor and two-top first-return geometry. One extra old-boundary cell gives a seven-cell ALL-K family. Prefix intersections with its drift line have only negative indices; the exhaustive7 tail phase-ray offsets have minimum45 and nonnegative epoch shifts. Therefore first disagreement occurs EXACTLY279+104K for allK, not merely in the five fresh finite controls. Drift is tangent to the pristine diagonal cap, which cannot clear old-side rays. No noncapture is asserted.',
'For any fixed legal future C H-infinity and arbitrary finite old-side extensions, an initial finite-bit guard forces that EXACT future iff the old-side future read set is finite. If infinite, a cell outside any finite guard/seed is queried and one added black bit changes its first turn. Strict outward drift gives finite intersection; tangent drift works only if all tail rays lie on the pristine side.',
'All strict record phases for the THREE NAMED normals are obtained from the exact preceding-period maximum and all earlier same-period phases. Not a catalogue of every normal. Eight actual complete finite-board cuts, including all older unread wake, are independently replayed and verified strict against entire seed plus read history.',
'Each old-side guard is derived from every ray and the integer bound k<=floor((-1-n.v)/(n.d)). Every first-read bit, exact infinite tail, and normalized complete actual field is verified. The smallest phase45 guard has19 bits15black4white. Its one-top return leaves16 free guard bits; phase55 two-top return leaves27. All43 flips preserve the actual full first return then force a first discrepancy. Their component connectivity is not assumed preserved.',
'These are explicit sufficient outward record patterns and precise noncoverage controls. No finite-seed trajectory is shown to reach such a pattern merely from unboundedness, record costs, component bounds, or ancestry. No global capture, all-q family extension, or noncapture theorem is inferred.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
