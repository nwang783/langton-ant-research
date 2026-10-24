from pathlib import Path
from collections import Counter,defaultdict
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'CHRONOLOGICAL_SPINE_ORIENTATION_MANIFEST.json';assert sha(MF)=='65a4b90707b05a417311fbb357e4f4f76eb0362265fc0cd6bdb87daa6614c997';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
J=json.loads((D/'CHRONOLOGICAL_SPINE_ORIENTATION_CHECKED.json').read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
lib=S.parent/'check_phase13_double_scatter_independent.py';N={'__file__':str(lib)};exec(lib.read_text().split('# Canonical source')[0],N);sim,geometry,future,K,xy,V,phases=[N[k]for k in('sim','geometry','future','K','xy','V','phases')];key=lambda q:(q.real,q.imag);encB=lambda B:[[xy(q),i]for q,i in sorted(B.items(),key=lambda z:key(z[0]))];encP=lambda B:[[xy(q),xy(p)]for q,p in sorted(B.items(),key=lambda z:key(z[0]))]
def geom(p,h,w):
 q,hh,ep,eh=geometry(p,h,w);return q,[(a+(1 if c=='R'else-1))%4 for a,c in zip(hh,w)],ep,eh
W=sim(K,104)['word'];assert W==J['canonical_quotient']['word']and W in phases
# Independent last-exit reconstruction and stack chronological loop erasure.
def tree(pts,hin):
 root=pts[-1];last={q:i for i,q in enumerate(pts[:-1])};par={q:pts[i+1]for q,i in last.items()if q!=root};dep={root:0}
 for q in par:
  chain=[];at=q
  while at not in dep:
   assert at not in chain;chain.append(at);p=par[at];assert p==root or last[p]>last[at];at=p
  for z in chain[::-1]:dep[z]=dep[par[z]]+1
 rev={};seen={root}
 for q,p in zip(pts[-2::-1],pts[:0:-1]):
  if q not in seen:rev[q]=p;seen.add(q)
 assert rev==par
 stack=[];where={}
 for q in pts:
  if q in where:
   i=where[q]
   for p in stack[i+1:]:del where[p]
   del stack[i+1:]
  else:where[q]=len(stack);stack.append(q)
 assert stack[0]==pts[0]and stack[-1]==root and all(par[q]==p for q,p in zip(stack,stack[1:]));h=hin;ts=[];cs=[0]
 for q,p in zip(stack,stack[1:]):
  hh=V.index(p-q);d=(hh-h)%4;assert d in[1,3];ts.append(1 if d==1 else-1);cs.append(cs[-1]+ts[-1]);h=hh
 return dict(root=root,last=last,parent=par,depth=dep,spine=stack,turns=ts,cum=cs,end_heading=h)
# Exact canonical quotient using FULL (2,2), not the primitive diagonal.
Q,H,ep,eh=geom(0j,1,W);assert(ep,eh)==(2+2j,1)
def cl(q):
 x=int(q.real)%2;r=complex(x,x-int(q.real-q.imag));return r,int((q.real-x)//2)
classes=defaultdict(list)
for i,q in enumerate(Q):r,a=cl(q);classes[r].append((i,a))
edges={};qrows=[]
for r,ls in classes.items():
 lam,i,a=max((i-104*a,i,a)for i,a in ls);rp,delta=cl(r+V[H[i]]);edges[r]=(rp,delta,lam,i,H[i]);ar=next(z for z in J['canonical_quotient']['classes']if z['representative']==xy(r));assert ar['phase_offsets']==list(map(list,ls))and ar['last_phase']==i and ar['last_time_offset']==lam and ar['parent_class']==xy(rp)and ar['parent_layer_shift']==delta and ar['parent_heading']==H[i];qrows.append([xy(r),xy(rp),delta,lam,i,H[i]])
for r,(p,k,lam,i,h)in edges.items():assert 104*k+edges[p][2]-lam>=1
seen=set();cycles=[]
for r in edges:
 if r in seen:continue
 chain=[];at={};q=r
 while q not in seen:seen.add(q);at[q]=len(chain);chain.append(q);q=edges[q][0]
 if q in at:
  cyc=chain[at[q]:];shift=sum(edges[q][1]for q in cyc);hh=[edges[q][4]for q in cyc];turn=[1 if(hh[(i+1)%len(hh)]-h)%4==1 else-1 for i,h in enumerate(hh)];assert shift==1 and len(cyc)==4 and sum(turn)==0;cycles.append(dict(classes=list(map(xy,cyc)),layer_shift=shift,headings=hh,turns=turn))
assert len(classes)==22 and len(cycles)==2
# General inverse identity, with complete board and the required one-cut shift.
def step(B,p,h):
 B=set(B);black=p in B;B.symmetric_difference_update({p});h=(h+(-1 if black else 1))%4;return B,p+V[h],h
def invJ(st):B,p,h=st;return set(B),p-V[h],(h+2)%4
for h in range(4):
 for bit in[0,1]:
  st=({0j}if bit else set(),0j,h);assert invJ(invJ(st))==st;assert invJ(step(*invJ(step(*st))))==st
A=json.loads((D/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());Aw=A['T_recovery'][8470:];SW=A['T_tail_word'];NW=A['controls'][0]['complete_future_certificate']['tail_word'];Fw=SW[:100]+'L'+A['postcollision_word']+NW*77+NW[:90];assert J['MT_all_n']['source_words']==dict(T_remaining=Aw,SW=SW,fixed_suffix=Fw)
AQ,AH,aend,ah=geom(433+462j,0,Aw);SQ,SH,send,sh=geom(aend,ah,SW);FQ,FH,fend,fh=geom(aend-186-186j,ah,Fw);assert len(Aw)==2762 and(send-aend,sh)==(-2-2j,ah)and(fend,fh)==(-2+372j,3);word=Aw+SW*93+Fw;BQ,BH,bend,bh=geom(433+462j,0,word);bt=tree(BQ+[bend],0);BD=bt['depth'];BL=bt['last'];BP=bt['parent'];assert len(word)==69097 and len(BL)==9402 and max(BD.values())==1337 and [q for q,d in BD.items()if d==1337]==[433+462j]
assert encP(BP)==J['MT_all_n']['base_complete_tree']and [[xy(q),d]for q,d in sorted(BD.items(),key=lambda z:key(z[0]))]==J['MT_all_n']['base_depths']
def mc(q):
 x=363 if int(q.real)%2 else 364;r=complex(x,x-int(q.real-q.imag));return r,int((q.real-x)//2)
ml=defaultdict(list)
for i,q in enumerate(SQ):r,a=mc(q);ml[r].append((a,i))
assert len(ml)==22 and min(a for ls in ml.values()for a,i in ls)==13 and max(a for ls in ml.values()for a,i in ls)==17
U={q for q in BL if q.real>=365};L=set(BL)-U;assert(len(U),len(L))==(1153,8249)and min(q.real for q in AQ)==392 and max(q.real for q in FQ)==240
AL={q:i for i,q in enumerate(AQ)};FL={q:i for i,q in enumerate(FQ)};mid=[]
for r,ls in ml.items():
 lo=min(a for a,i in ls)-92;hi=max(a for a,i in ls);assert lo<=0<hi and hi-min(a for a,i in ls)<93;score,i,a=max((104*a+i,i,a)for a,i in ls);rp,delta=mc(r+V[SH[i]]);assert delta in[-1,0,1]and BD[r]==1+BD[rp]+4*delta and BD[r+2+2j]==BD[r]+4
 ar=next(z for z in J['MT_all_n']['phase_rows']if z['representative']==xy(r));assert ar['phase_offsets']==list(map(list,ls))and ar['baseline_layer_low']==lo and ar['baseline_layer_high']==hi and ar['final_phase']==i and ar['last_time_constant']==2762+score and ar['parent_representative']==xy(rp)and ar['parent_layer_shift']==delta and ar['baseline_depth']==BD[r]and ar['next_layer_depth']==BD[r+2+2j];mid.append([xy(r),xy(rp),delta,BD[r],i])
# The cap candidate times are affine in K with COMMON slopes per cap.
caprows=[];boundary=[]
for typ,cap in[('upper',U),('lower',L)]:
 for q in sorted(cap,key=key):
  r,ell=mc(q);hits=ml.get(r,[]);cand=[]
  if typ=='upper':
   assert q.real>240 and all(a-ell<=16 for a,i in hits)
   if q in AL:ii=AL[q];cand.append((ii,V[AH[ii]],'T'))
   for a,i in hits:
    j=a-ell
    if j>=0:assert j<=92;cand.append((2762+104*j+i,V[SH[i]],'SW'))
  else:
   assert q.real<392 and all(a-ell>=13 for a,i in hits)
   for a,i in hits:
    j=a-ell
    if j<=92:cand.append((2762+104*j+i,V[SH[i]],'SW'))
   if q in FL:ii=FL[q];cand.append((2762+104*93+ii,V[FH[ii]],'fixed'))
  t,v,src=max(cand,key=lambda z:z[0]);assert t==BL[q]and q+v==BP[q];p=q+v
  if typ=='lower'and p.real>=365:
   rr,k=mc(p);assert k==1 and BD[p]==BD[rr]+4;boundary.append([typ,xy(q),xy(p),1])
  if typ=='upper'and p.real<=364:
   rr,k=mc(p);assert k==0 and p in ml;boundary.append([typ,xy(q),xy(p),0])
  caprows.append([typ,xy(q),t,xy(p),BD[q],src])
assert caprows==J['MT_all_n']['cap_last_parent_records']
uH=Counter(BD[q]for q in U);lH=Counter(BD[q]for q in L|{bend});res=Counter(BD[r]%4 for r in ml);assert(max(uH.values()),max(lH.values()),max(res.values()))==(8,25,6)and(min(uH),max(uH),max(lH))==(1037,1337,1040)
assert sorted(map(list,uH.items()))==sorted(J['MT_all_n']['upper_depth_histogram'])and sorted(map(list,lH.items()))==sorted(J['MT_all_n']['lower_depth_histogram'])and sorted(map(list,res.items()))==sorted(J['MT_all_n']['middle_depth_residues'])
sp=bt['spine'];anchor=sp[300];block=[0j,-1+0j,-1-1j,-2-1j,-2-2j];assert anchor==365+394j and sp[300:305]==[anchor+v for v in block];assert min(q.real for q in sp[:301])==365 and max(q.real for q in sp[301:])==364;assert bt['turns'][300:304]==[1,-1,1,-1]and bt['cum'][300]==2 and(min(bt['cum']),max(bt['cum']),bt['cum'][-1])==(0,5,3)and min(q.imag for q in sp)==182
for a,b in zip(block,block[1:]):r,k=mc(anchor+a);row=next(z for z in mid if z[0]==xy(r));assert anchor+a+V[SH[row[4]]]==anchor+b
# Full finite original-seed simulations and exact all-future fields, not crops.
def run(seed,N,cuts):
 z=sim(seed,N,cuts=cuts);z['snap'][N]=(dict(z['B']),z['p'],z['h']);w,d,dead,tests=future(z['B'],z['p'],z['h']);assert w in phases;z.update(tail=w,drift=d,tests=tests);return z
inverse=[]
def reverse(z,s,t):
 B0,p0,h0=z['snap'][s];Bt,pt,ht=z['snap'][t];B=set(Bt);p=pt-V[ht];h=(ht+2)%4;rw=[]
 for k in range(t-1,s-1,-1):
  assert p==z['pts'][k];c='L'if p in B else'R';assert c!=z['word'][k];rw.append(c);B,p,h=step(B,p,h)
 assert B==set(B0)and(p,h)==(p0-V[h0],(h0+2)%4);ar=next(a for a in J['physical_inverse_controls']if a['interval']==[s,t]);assert ar['reverse_start']==[xy(pt-V[ht]),(ht+2)%4]and ar['reverse_end']==[xy(p),h]and ar['complete_reverse_word']==''.join(rw);inverse.append([s,t,len(rw),xy(p),h])
controls=[];total=0
for row in J['MT_controls']:
 n=row['n'];k=n-100;s=29671+104*n;t=88368+208*n;seed=K|{202+201j+a*(2+2j)for a in[0,1,6,8]}|{2*n+230+(2*n+229)*1j+a*(2+2j)for a in[0,1,3,5,6]};assert sorted(map(xy,seed))==row['seed'];z=run(seed,t,{s});total+=t;assert z['word']==row['complete_prefix_word']and z['word'][s:t]==Aw+SW*(93+k)+Fw;assert encB(z['snap'][s][0])==row['full_start_field']and encB(z['B'])==row['full_end_field']and [xy(z['p']),z['h']]==row['end_pose'];assert(z['tail'],xy(z['drift']),z['tests'])==(row['tail_word'],row['tail_drift'],row['whole_tail_parity_tests']);pts=z['pts']+[z['p']];heads=z['heads']+[z['h']];pr=lambda p:(p.imag,p.real,-p.imag,-p.real);ext=[max(pr(q)[a]for q in seed|{0j})for a in range(4)];records=[]
 for tick,p in enumerate(pts):
  for a,x in enumerate(pr(p)):
   if x>ext[a]:assert heads[tick]==a and(tick==t or z['word'][tick]=='R');ext[a]=x;records.append([tick,a])
 assert [r for r in records if s<=r[0]<=t]==[[s,0],[t,3]]==row['interval_records'];assert max(z['dead'][i]for i in range(-22,0))==27201+104*n
 tt=tree(pts[s:t+1],heads[s]);expect=L|{q+k*(2+2j)for q in U}|{r+j*(2+2j)for r in ml for j in range(1,k+1)};assert set(tt['last'])==expect and len(expect)==9402+22*k and encP(tt['parent'])==row['full_interval_tree']
 for q in expect:
  if q in L:hd=BD[q]
  elif q.real>=365+2*k:hd=BD[q-k*(2+2j)]+4*k
  else:r,j=mc(q);assert 1<=j<=k;hd=BD[r]+4*j
  assert tt['depth'][q]==hd
 want=[q+k*(2+2j)for q in sp[:301]]
 for j in range(k,0,-1):want.extend(anchor+v+j*(2+2j)for v in block[1:])
 want+=sp[301:];assert tt['spine']==want and list(map(xy,want))==row['spine']and tt['turns']==row['spine_turns'];hist=Counter(tt['depth'].values());assert sorted(map(list,hist.items()))==row['depth_histogram'];assert max(hist)==row['height']==4*n+937 and max(hist.values())<=39 and t-s==26*max(hist)+34335;assert(min(tt['cum']),max(tt['cum']),sum(tt['turns']))==(0,5,3)and min(q.imag for q in want)==182
 actual=z['word'][s:t].count('R')-z['word'][s:t].count('L');assert actual==row['actual_turn']==12*n+2627 and tt['end_heading']==z['h'];controls.append(dict(n=n,reads=t,height=max(hist),width=max(hist.values()),all_tree_vertices=len(tt['depth']),canonical_phase=[i for i in range(104)if z['tail']==W[i:]+W[:i]],parity_tests=z['tests'],original_last_death_tick=27201+104*n))
 if n==100:reverse(z,s,t)
 print('MT',n,'PASS',flush=True)
cz=run(K,4160,{1040,2080});total+=4160;assert cz['word']==W*40 and encB(cz['B'])==J['canonical_terminal']['full_field']and(cz['tail'],xy(cz['drift']),cz['tests'])==(J['canonical_terminal']['tail_word'],J['canonical_terminal']['tail_drift'],J['canonical_terminal']['whole_tail_parity_tests'])
for row in J['canonical_literal_controls']:
 t=row['cut'];pts=cz['pts'][:t+1]if t<4160 else cz['pts']+[cz['p']];tt=tree(pts,1);paths=[]
 for start in[12+12j,13+12j]:
  p=[start]
  while p[-1]!=tt['root']:p.append(tt['parent'][p[-1]])
  paths.append(p)
 merge=next(q for q in paths[0]if q in set(paths[1]));assert merge==tt['root']and xy(merge)==row['finite_merge']and list(map(lambda p:list(map(xy,p)),paths))==row['paths'];assert encB(cz['snap'][t][0])==row['full_field']and len(tt['depth'])==row['whole_tree_vertices']and max(tt['depth'].values())==row['height']
bz=run(set(),9977,{0,1579,5710,6042});total+=9977
for row in J['blank_controls']:
 s,t=row['interval'];tt=tree(bz['pts'][s:t+1],bz['heads'][s]);assert list(map(xy,tt['spine']))==row['spine']and tt['turns']==row['spine_turns']and [min(tt['cum']),max(tt['cum'])]==row['cumulative_turn_range']and max(tt['depth'].values())==row['whole_tree_height'];assert encB(bz['snap'][s][0])==row['initial_full_field']and encB(bz['snap'][t][0])==row['final_full_field'];reverse(bz,s,t)
assert total==432537==J['physical_reads']
O=dict(status='PASS exact certified-translator limiting last-exit components, reversal endpoints and all-n MT height/width/turning control',manifest=sha(MF),script=sha(S),dependencies=J['dependencies'],canonical_22_quotient_edges=qrows,canonical_two_cycles=cycles,all22_middle_parent_rows=mid,all9402_cap_parent_records=caprows,cap_boundary_edges=boundary,upper_lower_residue_maxima=[8,25,6],full_controls=controls,full_original_seed_reads=total,physical_inverse_controls=inverse,blank_terminal=dict(field=encB(bz['B']),pose=[xy(bz['p']),bz['h']],canonical_phase=[i for i in range(104)if bz['tail']==W[i:]+W[:i]],parity_tests=bz['tests']),analytic_review=[
'For any finite path, strictly increasing last-departure times prove the full last-exit graph is a root tree, including deletion of an old final-root outgoing edge. Reversed-list first-entry edges coincide, and the path from the initial head is exactly stack loop erasure. The invariant sector ensures effective spine turns are quarter turns even when edges come from different visits.',
'Physical reversal is J(B,p,h)=(B,p-v_h,h+2), with J F J=F inverse. It reads the complementary turns in reverse order, starts at p_(t-1), and ends at p_s-v_(h_s), restoring the ENTIRE field. Both colors and four headings, plus all three full finite inverse factors, are independently checked. Plain path reversal is not silently called an ant orbit.',
'For a certified nonzero translator, use full Zd classes. Once all phases occur, the exact last time is N+Pk+max(i-Pa_i); its unique phase determines the successor. The inequality Pdelta+lambda_target-lambda_source>=1 makes every quotient cycle have positive integer shift m. Its mature lift has m forward rays. A finite prehistory can neither create extra forward components nor join distinct ones: every successor chain leaves the finite exceptional region, and connected vertices in an outdegree-one acyclic graph have eventually merging forward chains. Thus the exact component count is the sum of m, not the number of quotient cycles alone.',
'The literal W quotient has22 full-(2,2) classes and exactlytwo four-edge shift1 N/E zigzag cycles, each net turning0. Therefore every finite history entering standard104 has two limiting forward last-exit components. Finite-cut trees still have one root; local stabilization forces their connecting paths to escape every fixed finite set. The three literal K13 merge-at-root controls are finite examples, not an all-cut formula.',
'The signed all-n complete MT source supplies the actual A SW^(93+K) F word. Twenty-two SW classes have offsets13..17 and contiguous occupied layer intervals. A cap has x>=392, F has x<=240. This proves the exact disjoint readset L plus translatedU plus22K middle cells, with all original fields and archive retained.',
'Every one of9402 baseline cap parents is independently recomputed from its literal last A/SW/F hit. Upper candidate indices are independent ofK and at most16; lower SW/F times all shift104K, with availability unchanged. Middle last phases maximize104a+i and have parent layer delta in{-1,0,1}. Both lower-to-middle layer1 and upper-to-middle layerK interfaces are explicit. The22 depth identities and next-layer+4 identity make every actual parent reduce the proposed potential by1 for allK, includingK0 and both boundary cases.',
'The unique baseline height1337 at the start becomes4n+937. Upper/lower layer histograms have maxima8/25, and at most6 representatives share any depth residue mod4, proving conservative whole-tree layer width39. These are cutsets of the selected temporal tree only, not lattice barriers or future route separators.',
'The maximum-height spine has translated upper prefix, K exact four-edge SW zigzags and a fixed suffix. Literal parent edges validate it; each inserted block has RLRL effective turns at cumulative level2. Thus every n retains turn range[0,5], net3 and minimum y182, with inward depth2n+80. Actual turn12n+2627 differs by4(3n+656), not a count of independently chargeable loops.',
'All432537 original-seed updates, every supplied full field/tree/lifetime snapshot, all22 row identities and exact infinite canonical-tail parity are independently replayed. In MT the final original lifetime is consumed at read tick27201+104n and is absent after that update; the pristine drought starts29671+104n and ends88368+208n with no intervening record of any axis.',
'This refutes only a uniform completed-drought bound from fixed seed size22, tree-depth width39 and maximum-spine turning range5. All family members capture. No limiting forest for a general nontranslator, global clock-window occurrence, BLACK-graph Euler identification, gross leaf inequality or canonical uniqueness is inferred.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
