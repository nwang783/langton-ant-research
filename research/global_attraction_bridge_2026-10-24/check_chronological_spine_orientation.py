"""Exact periodic last-exit quotient, reversal endpoints, and all-n MT tree layering."""
from pathlib import Path
from collections import Counter,defaultdict
import hashlib,json
from check_return_permanent_output_debt import future
P=Path(__file__).parent;D=((0,1),(1,0),(0,-1),(-1,0))
R=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());A=json.loads((P/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());J=json.loads((P/'JOINT_RECORD_DROUGHT_CHECKED.json').read_text())
W=R['W'];K0=set(map(tuple,R['canonical_source']));V=A['T_tail_word'];NW=A['controls'][0]['complete_future_certificate']['tail_word']

def geo(p,h,w):
 Q=[];after=[]
 for c in w:
  Q.append(p);h=(h+(1 if c=='R'else -1))%4;after.append(h);p=(p[0]+D[h][0],p[1]+D[h][1])
 return Q,after,p,h

def spine_tree(pos,initial_heading):
 root=pos[-1];last={q:i for i,q in enumerate(pos[:-1])};parent={q:pos[i+1]for q,i in last.items()if q!=root}
 height={root:0}
 for q in sorted(parent,key=lambda q:last[q],reverse=True):
  assert parent[q]in height;height[q]=height[parent[q]]+1
 reverse_first={};seen={root}
 for i in range(len(pos)-2,-1,-1):
  q=pos[i]
  if q not in seen:reverse_first[q]=pos[i+1];seen.add(q)
 assert reverse_first==parent
 stack=[];ix={}
 for q in pos:
  if q in ix:
   j=ix[q]
   for z in stack[j+1:]:del ix[z]
   stack=stack[:j+1]
  else:ix[q]=len(stack);stack.append(q)
 pp=[pos[0]]
 while pp[-1]!=root:pp.append(parent[pp[-1]])
 assert pp==stack
 h=initial_heading;turns=[];cum=[0]
 for a,b in zip(stack,stack[1:]):
  nh=D.index((b[0]-a[0],b[1]-a[1]));d=(nh-h)%4;assert d in(1,3);z=1 if d==1 else -1;turns.append(z);cum.append(cum[-1]+z);h=nh
 return dict(root=root,last=last,parent=parent,height=height,spine=stack,spine_turns=turns,cumulative_turns=cum,spine_end_heading=h,reverse_first_equal=True)

def full_run(name,seed,N,cuts,expected_interval=None):
 B={q:-i-1 for i,q in enumerate(sorted(seed))};p=(0,0);h=1;pos=[];heads=[];word=[];snap={};vals=lambda q:(q[1],q[0],-q[1],-q[0]);ext=[max(vals(q)[i]for q in seed|{p})for i in range(4)];records=[]
 for t in range(N+1):
  z=vals(p)
  for a in range(4):
   if z[a]>ext[a]:assert p not in B and h==a;ext[a]=z[a];records.append((t,a))
  pos.append(p);heads.append(h)
  if t in cuts:snap[t]=(dict(B),p,h)
  if t==N:break
  old=B.pop(p,None);c='R'if old is None else'L'
  if old is None:B[p]=t
  h=(h+(1 if c=='R'else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1]);word.append(c)
 if expected_interval:
  s,t,ew=expected_interval;assert ''.join(word[s:t])==ew
 tail,dr,dead,tests=future(B,p,h)
 return dict(name=name,seed=seed,N=N,B=B,p=p,h=h,pos=pos,heads=heads,word=''.join(word),snap=snap,records=records,tail=tail,drift=dr,parity_tests=tests)

def inverse_check(z,s,t):
 B0,p0,h0=z['snap'][s];BT,pt,ht=z['snap'][t];B=set(BT);p=(pt[0]-D[ht][0],pt[1]-D[ht][1]);h=(ht+2)%4;rw=[]
 for k in range(t-1,s-1,-1):
  assert p==z['pos'][k];c='L'if p in B else'R';assert c!=z['word'][k];rw.append(c)
  if c=='L':B.remove(p)
  else:B.add(p)
  h=(h+(1 if c=='R'else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 assert B==set(B0)and p==(p0[0]-D[h0][0],p0[1]-D[h0][1])and h==(h0+2)%4
 return dict(interval=[s,t],reverse_start=[(pt[0]-D[ht][0],pt[1]-D[ht][1]),(ht+2)%4],reverse_end=[p,h],complete_reverse_word=''.join(rw),restored_entire_field=True)

# Canonical quotient: rays modulo the actual (2,2), not the primitive vector (1,1).
CQ,CH,cd,ch=geo((0,0),1,W);assert(cd,ch)==((2,2),1)
def standard_class(q):
 x=q[0]%2;r=(x,x-(q[0]-q[1]));return r,(q[0]-x)//2
classes=defaultdict(list)
for i,q in enumerate(CQ):r,a=standard_class(q);classes[r].append((i,a))
edge={};rows=[]
for r,ls in sorted(classes.items()):
 lam,i,a=max((i-104*a,i,a)for i,a in ls);step=D[CH[i]];target,delta=standard_class((r[0]+step[0],r[1]+step[1]));edge[r]=(target,delta,CH[i],lam,i)
for r,e in edge.items():assert 104*e[1]+edge[e[0]][3]-e[3]>=1
seen=set();cycles=[]
for r in edge:
 if r in seen:continue
 path=[];at={};q=r
 while q not in seen:seen.add(q);at[q]=len(path);path.append(q);q=edge[q][0]
 if q in at:
  cyc=path[at[q]:];shift=sum(edge[q][1]for q in cyc);assert shift>0
  hh=[edge[q][2]for q in cyc];turn=[1 if(hh[(i+1)%len(hh)]-h)%4==1 else -1 for i,h in enumerate(hh)]
  assert all((hh[(i+1)%len(hh)]-h)%4 in(1,3)for i,h in enumerate(hh))
  cycles.append(dict(classes=cyc,layer_shift=shift,headings=hh,turns=turn,turn_sum=sum(turn)))
assert len(classes)==22 and len(cycles)==2 and all(len(c['classes'])==4 and c['layer_shift']==1 and c['turn_sum']==0 for c in cycles)
for r,ls in sorted(classes.items()):rows.append(dict(representative=r,phase_offsets=ls,first_layer=min(a for i,a in ls),all_phases_layer=max(a for i,a in ls),last_phase=edge[r][4],last_time_offset=edge[r][3],parent_class=edge[r][0],parent_layer_shift=edge[r][1],parent_heading=edge[r][2]))

# Exact MT word from a pristine N record to its next union (W) record.
Aw=A['T_recovery'][8470:];Fw=V[:100]+'L'+A['postcollision_word']+NW*77+NW[:90]
AA,AH,po,ho=geo((433,462),0,Aw);VV,VH,pv,hv=geo(po,ho,V);FF,FH,fe,fh=geo((po[0]-186,po[1]-186),ho,Fw)
assert len(Aw)==2762 and(pv[0]-po[0],pv[1]-po[1])==(-2,-2)and hv==ho
assert(fe,fh)==((-2,372),3)
baseword=Aw+V*93+Fw;BP,BH,be,bh=geo((433,462),0,baseword);base=spine_tree(BP+[be],0)
assert len(baseword)==69097 and be not in BP and max(base['height'].values())==1337 and len(base['spine'])-1==1337
assert [q for q,d in base['height'].items()if d==1337]==[(433,462)]
assert len(base['last'])==9402

def mtclass(q):
 x=363 if q[0]%2 else 364;r=(x,x-(q[0]-q[1]));return r,(q[0]-x)//2
mc=defaultdict(list)
for i,q in enumerate(VV):r,a=mtclass(q);mc[r].append((a,i))
assert len(mc)==22 and min(a for ls in mc.values()for a,i in ls)==13 and max(a for ls in mc.values()for a,i in ls)==17
AL={q:i for i,q in enumerate(AA)};FL={q:i for i,q in enumerate(FF)};U={q for q in base['last']if q[0]>=365};L=set(base['last'])-U
assert min(q[0]for q in AA)==392 and max(q[0]for q in FF)==240
mtrows=[]
for r,ls in sorted(mc.items()):
 lo=min(a for a,i in ls)-92;hi=max(a for a,i in ls);assert lo<=0<hi
 assert max(a for a,i in ls)-min(a for a,i in ls)<93
 tau,i,a=max((104*a+i,i,a)for a,i in ls);v=D[VH[i]];rp,delta=mtclass((r[0]+v[0],r[1]+v[1]));assert delta in(-1,0,1)
 assert base['height'][r]==1+base['height'][rp]+4*delta
 rplus=(r[0]+2,r[1]+2);assert base['height'][rplus]==base['height'][r]+4
 mtrows.append(dict(representative=r,phase_offsets=ls,baseline_layer_low=lo,baseline_layer_high=hi,
  final_phase=i,last_time_constant=2762+tau,parent_representative=rp,parent_layer_shift=delta,
  baseline_depth=base['height'][r],next_layer_depth=base['height'][rplus]))

# Every upper and lower cap node has the same exact last-parent edge for every K.
cap_records=[]
for typ,QS in [('upper',U),('lower',L)]:
 for q in sorted(QS):
  r,layer=mtclass(q);hits=mc.get(r,[]);candidates=[]
  if typ=='upper':
   assert q[0]>240 and all(a-layer<=16 for a,i in hits)
   if q in AL:
    i=AL[q];candidates.append((i,D[AH[i]],'T'))
   for a,i in hits:
    j=a-layer
    if j>=0:assert j<=92;candidates.append((2762+104*j+i,D[VH[i]],'SW'))
  else:
   assert q[0]<392 and all(a-layer>=13 for a,i in hits)
   for a,i in hits:
    j=a-layer
    if j<=92:candidates.append((2762+104*j+i,D[VH[i]],'SW'))
   if q in FL:
    i=FL[q];candidates.append((2762+104*93+i,D[FH[i]],'fixed'))
  tt,v,src=max(candidates);assert tt==base['last'][q]
  parent=(q[0]+v[0],q[1]+v[1]);assert parent==base['parent'][q]
  if typ=='lower'and parent[0]>=365:
   rr,ll=mtclass(parent);assert ll==1 and base['height'][parent]==base['height'][rr]+4
  if typ=='upper'and parent[0]<=364:
   rr,ll=mtclass(parent);assert ll==0 and parent in mc
  cap_records.append((typ,q,tt,parent,base['height'][q],src))
UH=Counter(base['height'][q]for q in U);LH=Counter(base['height'][q]for q in L|{be});residue=Counter(base['height'][r]%4 for r in mc)
assert max(UH.values())==8 and max(LH.values())==25 and max(residue.values())==6
assert min(UH)==1037 and max(UH)==1337 and max(LH)==1040
width_bound=max(UH.values())+max(LH.values())+max(residue.values());assert width_bound==39

# Exact start-to-root spine template. Parent/depth proof above validates the full tree.
S=base['spine'];q=S[300];C=[(S[300+i][0]-q[0],S[300+i][1]-q[1])for i in range(5)]
assert q==(365,394)and C==[(0,0),(-1,0),(-1,-1),(-2,-1),(-2,-2)]
assert min(z[0]for z in S[:301])==365 and max(z[0]for z in S[301:])==364
assert sum(base['spine_turns'][:300])==2 and base['spine_turns'][300:304]==[1,-1,1,-1]
assert sum(base['spine_turns'])==3 and(min(base['cumulative_turns']),max(base['cumulative_turns']))==(0,5)
assert min(z[1]for z in S)==182 and sum(1 if c=='R'else -1 for c in baseword)==3827
for i in range(4):
 zz=(q[0]+C[i][0],q[1]+C[i][1]);r,l=mtclass(zz);row=next(z for z in mtrows if z['representative']==r)
 step=D[VH[row['final_phase']]];assert(zz[0]+step[0],zz[1]+step[1])==(q[0]+C[i+1][0],q[1]+C[i+1][1])

def prescribed_spine(K):
 out=[(z[0]+2*K,z[1]+2*K)for z in S[:301]]
 for k in range(K,0,-1):out.extend((q[0]+z[0]+2*k,q[1]+z[1]+2*k)for z in C[1:])
 return out+S[301:]

controls=[];inverse_controls=[];physical=0
for n in[100,137,500]:
 seed=set(map(tuple,next(c['seed']for c in J['controls']if c['name']==f'MT_{n}')));assert seed==K0|{(202+2*a,201+2*a)for a in[0,1,6,8]}|{(2*n+230+2*a,2*n+229+2*a)for a in[0,1,3,5,6]} and len(seed)==22;s=29671+104*n;t=88368+208*n;K=n-100;ew=Aw+V*(n-7)+Fw
 z=full_run(f'MT_{n}',seed,t,{s,t},(s,t,ew));physical+=t
 assert [r for r in z['records']if s<=r[0]<=t]==[(s,0),(t,3)]
 tree=spine_tree(z['pos'][s:t+1],z['heads'][s]);assert tree['spine']==prescribed_spine(K)
 expect=L|{(a+2*K,b+2*K)for a,b in U}|{(a+2*k,b+2*k)for a,b in mc for k in range(1,K+1)}
 assert set(tree['last'])==expect and len(expect)==9402+22*K
 for a,b in expect:
  if(a,b)in L:pred=base['height'][(a,b)]
  elif a>=365+2*K:pred=base['height'][(a-2*K,b-2*K)]+4*K
  else:r,k=mtclass((a,b));assert 1<=k<=K;pred=base['height'][r]+4*k
  assert tree['height'][(a,b)]==pred
 hh=max(tree['height'].values());hist=Counter(tree['height'].values());assert hh==4*n+937 and max(hist.values())<=39
 assert t-s==26*hh+34335 and sum(tree['spine_turns'])==3 and(min(tree['cumulative_turns']),max(tree['cumulative_turns']))==(0,5)
 actual_turn=sum(1 if c=='R'else -1 for c in ew);assert actual_turn==12*n+2627 and actual_turn-3==4*(3*n+656)
 if n==100:inverse_controls.append(inverse_check(z,s,t))
 controls.append(dict(name=z['name'],n=n,seed=sorted(seed),start=s,end=t,complete_prefix_word=z['word'],
  full_start_field=sorted(z['snap'][s][0].items()),start_pose=[z['pos'][s],z['heads'][s]],
  full_end_field=sorted(z['B'].items()),end_pose=[z['p'],z['h']],tail_word=z['tail'],tail_drift=z['drift'],whole_tail_parity_tests=z['parity_tests'],
  interval_records=[r for r in z['records']if s<=r[0]<=t],full_interval_tree=sorted(tree['parent'].items()),
  height=hh,depth_histogram=sorted(hist.items()),spine=tree['spine'],spine_turns=tree['spine_turns'],actual_turn=actual_turn,minimum_spine_y=min(a[1]for a in tree['spine'])))
 print('MT',n,'height',hh,'width',max(hist.values()),'turn3/range05',flush=True)

# Literal full canonical source and the blank Hall controls.
cz=full_run('canonical_K13',K0,4160,{0,1040,2080,4160});physical+=4160;assert cz['word']==W*40
canonical_controls=[]
for t in[1040,2080,4160]:
 tr=spine_tree(cz['pos'][:t+1],1)
 # The two fixed vertices lie on distinct infinite quotient cycles at a mature layer.
 q1=(12,12);q2=(13,12);paths=[]
 for start in[q1,q2]:
  pp=[start]
  while pp[-1]!=tr['root']:pp.append(tr['parent'][pp[-1]])
  paths.append(pp)
 common=set(paths[1]);merge=next(q for q in paths[0]if q in common)
 canonical_controls.append(dict(cut=t,full_field=sorted(cz['snap'][t][0].items()),pose=[cz['pos'][t],cz['heads'][t]],
  whole_tree_vertices=len(tr['height']),height=max(tr['height'].values()),two_stable_vertices=[q1,q2],finite_merge=merge,paths=paths))
blank=full_run('blank',set(),9977,{0,1579,5710,6042});physical+=9977
# This cut is not canonical: only its previously signed complete continuation is used below.
blank_controls=[]
for s,t in[(0,1579),(5710,6042)]:
 tr=spine_tree(blank['pos'][s:t+1],blank['heads'][s]);inverse_controls.append(inverse_check(blank,s,t))
 blank_controls.append(dict(interval=[s,t],initial_full_field=sorted(blank['snap'][s][0].items()),final_full_field=sorted(blank['snap'][t][0].items()),
  initial_pose=[blank['pos'][s],blank['heads'][s]],final_pose=[blank['pos'][t],blank['heads'][t]],spine=tr['spine'],spine_turns=tr['spine_turns'],
  cumulative_turn_range=[min(tr['cumulative_turns']),max(tr['cumulative_turns'])],actual_turn=sum(1 if c=='R'else -1 for c in blank['word'][s:t]),
  whole_tree_height=max(tr['height'].values()),reverse_first_equal=tr['reverse_first_equal']))

fs=['RECURSIVE_PHASE13_PACKET_MANIFEST.json','../audits/check_recursive_phase13_packet_independent.json','SOUTHWEST_ARCHIVE_IMPORT_MANIFEST.json','../audits/check_southwest_archive_import_independent.json','JOINT_RECORD_DROUGHT_MANIFEST.json','../audits/check_joint_record_drought_independent.json','LEAF_HALL_INTERFACES_MANIFEST.json','../audits/check_leaf_Hall_interfaces_independent.json']
for f in fs:assert(P/f).exists(),f
out=dict(status='AUTHOR exact orientation and chronological forest results; independent audit pending',physical_reads=physical,
 canonical_quotient=dict(word=W,drift=[2,2],classes=rows,cycles=cycles,infinite_forward_components=sum(c['layer_shift']for c in cycles)),
 canonical_literal_controls=canonical_controls,canonical_terminal=dict(full_field=sorted(cz['B'].items()),pose=[cz['p'],cz['h']],tail_word=cz['tail'],tail_drift=cz['drift'],whole_tail_parity_tests=cz['parity_tests']),
 MT_all_n=dict(parameter='integer n>=100; K=n-100',source_words=dict(T_remaining=Aw,SW=V,fixed_suffix=Fw),base_start=[433,462],
  finite_caps=dict(T_min_x=392,fixed_suffix_max_x=240,upper_threshold=365,upper_nodes=len(U),lower_nodes=len(L)),
  phase_rows=mtrows,base_complete_tree=sorted(base['parent'].items()),base_depths=sorted(base['height'].items()),cap_last_parent_records=cap_records,
  upper_depth_histogram=sorted(UH.items()),lower_depth_histogram=sorted(LH.items()),middle_depth_residues=sorted(residue.items()),
  depth_width_bound=39,height='4n+937',read_vertices='22n+7202',drought='58697+104n = 26 height +34335',
  spine_base=S,spine_prefix_last_index=300,spine_anchor=q,inserted_cycle=C,spine_turn=3,spine_cumulative_turn_range=[0,5],minimum_spine_y=182,
  inward_depth_from_N_record='2n+80',actual_turn='12n+2627',actual_minus_spine_turn='4(3n+656)'),
 MT_controls=controls,blank_controls=blank_controls,physical_inverse_controls=inverse_controls,
 dependencies={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in fs},
 scope='Two forward components for certified standard tails; exact all-n temporal-tree countercontrol to uniform bounded-width/bounded-turn drought forcing. No physical Euler identity, nontranslation classification, or universal record-window occurrence.')
(P/'CHRONOLOGICAL_SPINE_ORIENTATION_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print('AUTHOR checks complete',physical,'reads, 2 canonical forward components, all-n height and width39')
