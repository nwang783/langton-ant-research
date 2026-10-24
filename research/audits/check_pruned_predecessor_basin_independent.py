from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'PRUNED_PREDECESSOR_BASIN_MANIFEST.json';assert sha(MF)=='740f80efcd08d4c7c0bad3ee4f41cb35fa2f08fd3e9309e4f072248ae49612ae';mf=json.loads(MF.read_text())
for f,h in mf['sha256'].items():assert sha(D/f)==h
J=json.loads((D/'PRUNED_PREDECESSOR_BASIN_CHECKED.json').read_text())
for f,h in J['source_hashes'].items():assert sha(D/f)==h
ns={};exec(S.with_name('check_return_permanent_debt_independent.py').read_text().split('def check_case')[0],ns);verify,vec,xy,G,twenty,ray=[ns[k]for k in('verify_future','vec','pair','G','twenty','ray_k')]
def step(B,p,h,t):
 old=B.pop(p,None)
 if old is None:B[p]=t;h=(h+1)%4;c='R'
 else:h=(h-1)%4;c='L'
 return p+vec[h],h,c,old

def run(seed,N,cuts):
 B={q:-i-1 for i,q in enumerate(sorted(seed,key=lambda z:(z.real,z.imag)))};p=0j;h=1;deaths={};snap={};word=[];reads=[]
 for t in range(N):
  if t in cuts:snap[t]=(B.copy(),p,h)
  reads.append(p);p,h,c,old=step(B,p,h,t);word.append(c)
  if old is not None:deaths[old]=t
 w,dr,future,tests=verify(B,p,h);deaths.update({i:N+t for i,t in future.items()});return dict(B=B,p=p,h=h,word=''.join(word),reads=reads,deaths=deaths,snap=snap,w=w,dr=dr,tests=tests)
def geom(p,h,w):
 arr=[]
 for c in w:arr.append(p);h=(h+(1 if c=='R'else-1))%4;p+=vec[h]
 return arr,p,h
ref=run(G,390,{60,61,182});U=ref['word'][182:286];assert ref['word'][286:390]==ref['w']==U and ref['dr']==2+2j and min(q.real for q in ref['reads'])==0;tail,_,_=geom(ref['p'],ref['h'],U);assert min(q.real for q in tail)>=0
B,p,h=ref['snap'][182];counts=Counter();norms=set();branchchecks=0
for phase,row in enumerate(J['canonical_roots']):
 w,dr,fate,tests=verify(B,p,h);C={q for q,i in B.items()if i in fate};r=p-vec[h];reads,_,_=geom(p,h,w);times=[104*k+i for i,q in enumerate(reads)if(k:=ray(r-q,dr))is not None and k>=0];hit=min(times)if times else None
 assert row['phase_in_G_U']==phase and row['root_pose']==[xy(p),h]and row['word']==w==U[phase:]+U[:phase]and row['root_pruning']==sorted(map(xy,C))and row['full_root_black']==sorted(map(xy,B))and row['predecessor_cell']==xy(r)and row['first_future_read_of_predecessor']==hit and row['root_parity_tests']==tests
 norm=tuple(sorted(tuple(xy((q-p)*(1j)**h))for q in C));assert norm==tuple(map(tuple,row['normalized_heading_N_pruning']))and norm not in norms;norms.add(norm)
 if r in C:kind='unique relevant-R';branches=[('relevant-R',C-{r},(h-1)%4)]
 else:
  kind='unique L'if hit is not None else'double L/permanent-R';branches=[('L',C|{r},(h+1)%4)]
  if hit is None:branches.append(('permanent-R',C.copy(),(h-1)%4))
 assert kind==row['type'];counts[kind]+=1;assert len(branches)==len(row['branches'])
 for(name,pre,ph),saved in zip(branches,row['branches']):
  B0={q:-i-1 for i,q in enumerate(sorted(pre,key=lambda z:(z.real,z.imag)))};post=B0.copy();pp,hh,ch,old=step(post,r,ph,10**9);assert(pp,hh)==(p,h)and ch==('L'if name=='L'else'R');fw,dd,fd,ft=verify(post,p,h);assert fw==w and dd==dr;preC={q for q,i in B0.items()if i==old or i in fd};postC={q for q,i in post.items()if i in fd};assert preC==pre and postC==C and((10**9 in fd)==(name=='relevant-R'));assert saved==dict(branch=name,pre_black=sorted(map(xy,pre)),pre_pose=[xy(r),ph],turn=ch,post_full_black=sorted(map(xy,post)),post_pruning=sorted(map(xy,postC)),full_future_parity_tests=ft);branchchecks+=1
 p,h,ch,old=step(B,p,h,182+phase)
assert len(norms)==104 and branchchecks==126 and dict(counts)==J['branch_type_counts']=={'double L/permanent-R':22,'unique relevant-R':46,'unique L':36}
# Independent all-n affine displacement list relative to the common cut61 head(0,3).
origins=[((1,-1),(1,0),0),((-1,0),(3,-4),3),((-5,5),(-1,0),2),((-3,0),(-3,8),1)];affine=[]
for ax,ay,hh in origins:
 for g in sorted(G,key=lambda z:(z.real,z.imag)):
  off=g*((-1j)**(hh-1));coords=((ax[0],ax[1]+int(off.real)),(ay[0],ay[1]+int(off.imag)-3));witnesses=[]
  for axis,(a,b)in enumerate(coords):
   for sign in(-1,1):
    slope=sign*a-1;intercept=sign*b+2
    if slope>=0 and 20*slope+intercept>=0:witnesses.append((axis,sign,slope,intercept))
  assert witnesses;affine.append(dict(origin=[ax,ay,hh],offset=xy(g),relative_coordinates=coords,witness=witnesses[0]))
assert json.loads(json.dumps(affine))==J['remote_affine_exclusion_guards']and any(z['relative_coordinates']==((1,-2),(1,-2))for z in affine)
B61,p61,h61=ref['snap'][61];C61={q for q,i in B61.items()if i in ref['deaths']};assert(p61,h61)==(3j,0)and B61[2j]==60 and len(B61)==15 and len(C61)==11 and 60 not in ref['deaths'];assert max(max(abs((q-p61).real),abs((q-p61).imag))for q in ref['reads'][:61])<18
controls=[]
for row in J['controls']:
 n=row['n'];Q=twenty(n);P=G|{-n+1j*j for j in range(16)};assert len(Q)==len(P)==20 and sorted(map(xy,Q))==row['initial_live']and sorted(map(xy,P))==row['initial_permanent'];live=run(Q,row['live_complete_reads'],{60,61});dead=run(P,row['permanent_complete_reads'],{60,61});LB,lp,lh=live['snap'][61];DB,dp,dh=dead['snap'][61];assert(lp,lh)==(dp,dh)==(p61,h61)and live['word'][:61]==dead['word'][:61]==ref['word'][:61]and live['word'][60]==dead['word'][60]=='R';assert set(LB)^set(DB)==(Q-G)^(P-G)and len(LB)==len(DB)==31
 dist=lambda q:max(abs((q-p61).real),abs((q-p61).imag));diff=set(LB)^set(DB);assert min(map(dist,diff))==n-2 and{q for q in LB if dist(q)<=n-3}=={q for q in DB if dist(q)<=n-3};LC={q for q,i in LB.items()if i in live['deaths']};DC={q for q,i in DB.items()if i in dead['deaths']};assert LC==set(LB)and DC==C61 and live['deaths'][60]==624*n-1516 and 60 not in dead['deaths']
 for label,state,cutB in(('live',live,LB),('permanent',dead,DB)):
  full=[dict(cell=xy(q),identity=i,death=state['deaths'].get(i))for q,i in sorted(cutB.items(),key=lambda z:(z[0].real,z[0].imag))];assert full==row[label+'_full']and sorted(map(xy,state['B']))==row[label+'_tail_black']and[xy(state['p']),state['h']]==row[label+'_tail_pose']and state['w']==row[label+'_tail_word']and state['tests']==row[label+'_tail_tests']
 controls.append(dict(n=n,identical_radius=n-3,nearest_difference=n-2,live_pruning=len(LC),permanent_pruning=len(DC),marked_death=live['deaths'][60],full_reads=row['live_complete_reads']+row['permanent_complete_reads']))
# The all-n relevant-cap/lifetime theorem is explicitly required, not only named samples.
stock=D/'TWENTY_RELEVANT_STOCK_MANIFEST.json';sr=R/'audits/twenty_relevant_stock_independent.json';assert sha(stock)=='0727f6d758e43ccb6c7585545f9b46c5512f5db137348eaeb0e16c8055137d18'
addendum=D/'PRUNED_PREDECESSOR_DEPENDENCY_ADDENDUM.json';assert sha(addendum)=='88b7adefbf7de43b48e68319362d3a0b48a0ba825f069905190a74d40e4f83f9'
for f,h in json.loads(addendum.read_text())['sha256'].items():assert sha(D/f)==h
out=dict(status='PASS exact pruned predecessor law, canonical ancestry parametrization and all-n local-branch obstruction WITH mandatory dependency addendum',dependency_addendum=sha(addendum),manifest=sha(MF),script=sha(S),required_all_n_stock_manifest=sha(stock),required_all_n_stock_audit=sha(sr),canonical_roots=104,branches=branchchecks,branch_counts=dict(counts),root_mass_range=J['canonical_root_mass_range'],controls=controls,analytic_review=['Full inverse is unique and local at r=p-vh. Pruning quotient preimages exhaust every full target C union unread archive: if r belongs to C, relevantR removes it; if r absent, L always adds it; permanentR is possible iff the COMPLETE future from C never reads r. A future WHITE visit still forbids permanentR. Two quotient branches have different full successor boards, not two inverses of one board.','Every displayed predecessor is genuinely pruned. Its other C cells retain the same complete future, added L input is consumed immediately, and new permanentR is never read. Starting from104 certified canonical phase roots and prepending these transitions yields an effective ancestry parametrization up to genuine translations/quarter-rotations, carrying a known finite-prefix plus periodic-ray future. It does not prune arbitrary unknown states or establish basin coverage/well-foundedness.','Independent all-n affine bounds put all16 circuit remote cells outside radius n-3, with one at exact distance n-2, relative to common head0,3. The common first61 reads lie strictly inside distance18. P_n far-left x=-n bits are forever unread because the whole reference prefix and every positive-x tail ray stayx>=0. Thus full fields agree locally with equal initial20/cut31 masses for all even n>=20.','Signed all-n twenty-stock proof supplies actual marked consumption624n-1516, whole cut61 relevance31, and all-time relevant cap132; P_n inherits cap22. Named n20/80/400 complete-board/fate/infinite-tail replays independently confirm the difference. Local full-board data cannot determine exact quotient branch degree at any fixed radius even with these mass/cap bounds. This does not refute a rule given the actual C* oracle, an orbit-dependent radius, canonical capture, or full-state reversibility.','Original checker accidentally named nonexistent TWENTY_CELL_RELEVANT_STOCK_MANIFEST and silently omitted it. The mandatory immutable88b7adef addendum binds the exact all-n manifest, note and independent report; original740f80ef is preserved. All bindings are checked. No mathematical counterexample was found.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
