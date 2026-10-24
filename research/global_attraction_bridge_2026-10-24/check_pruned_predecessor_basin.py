"""Bounded exact controls for pruning-quotient preimages and nonlocality.
No unknown trajectory is accepted from finite sampled repetition.
"""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,rot,twenty,future
from blank_collision_operator import H
P=Path(__file__).parent
G={(0,-1),(1,1),(1,3),(2,2)}

def advance(B,p,h,t):
 old=B.pop(p,None)
 if old is None:B[p]=t;h=(h+1)%4;turn='R'
 else:h=(h-1)%4;turn='L'
 return (p[0]+DXY[h][0],p[1]+DXY[h][1]),h,turn,old

def trace(seed,N,snapcuts):
 B={q:-i-1 for i,q in enumerate(sorted(seed))};p=(0,0);h=1;word=[];snap={};deaths={};positions=[]
 for t in range(N):
  if t in snapcuts:snap[t]=(dict(B),p,h)
  positions.append(p);p,h,ch,old=advance(B,p,h,t);word.append(ch)
  if old is not None:deaths[old]=t
 w,dr,tail,tests=future(B,p,h);deaths.update({i:N+t for i,t in tail.items()})
 return dict(B=B,p=p,h=h,word=''.join(word),snap=snap,deaths=deaths,positions=positions,tail_word=w,drift=dr,ray_tests=tests)

def ray_first(q,reads,dr):
 hit=[]
 for i,r in enumerate(reads):
  dx,dy=q[0]-r[0],q[1]-r[1]
  if dx%dr[0]==0 and dy==(dx//dr[0])*dr[1]and dx//dr[0]>=0:hit.append(104*(dx//dr[0])+i)
 return min(hit)if hit else None

def geometry(p,h,w):
 reads=[]
 for ch in w:
  reads.append(p);h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 return reads,p,h

ref=trace(G,390,{60,61,182})
U=ref['word'][182:286];assert U in {H[i:]+H[:i]for i in range(104)}
assert ref['word'][286:390]==U and ref['tail_word']==U and ref['drift']==(2,2)
assert min(q[0]for q in ref['positions'])==0
Q,end,eh=geometry(ref['p'],ref['h'],U);assert min(q[0]for q in Q)>=0
B,p,h=ref['snap'][182];roots=[];counts={};seen=set()
for phase in range(104):
 w,dr,dead,tests=future(B,p,h);assert w==U[phase:]+U[:phase]
 C={q for q,i in B.items()if i in dead};r=(p[0]-DXY[h][0],p[1]-DXY[h][1])
 reads,_,_=geometry(p,h,w);hit=ray_first(r,reads,dr)
 if r in C:kind='unique relevant-R';branches=[('relevant-R',C-{r},(h-1)%4)]
 else:
  kind='unique L'if hit is not None else'double L/permanent-R';branches=[('L',C|{r},(h+1)%4)]
  if hit is None:branches.append(('permanent-R',set(C),(h-1)%4))
 counts[kind]=counts.get(kind,0)+1
 norm=tuple(sorted(rot((q[0]-p[0],q[1]-p[1]),-h)for q in C));assert norm not in seen;seen.add(norm)
 results=[]
 for name,pre,ph in branches:
  full={q:-i-1 for i,q in enumerate(sorted(pre))};target,th,ch,old=advance(full,r,ph,10**9)
  assert(target,th)==(p,h)and ch==('L'if name=='L'else'R')
  fw,fdr,fdead,ft=future(full,p,h);assert fw==w and fdr==dr
  relevant_pre={q for q,i in sorted({q:-i-1 for i,q in enumerate(sorted(pre))}.items())if i==old or i in fdead};assert relevant_pre==pre
  postC={q for q,i in full.items()if i in fdead};assert postC==C
  assert (10**9 in fdead)==(name=='relevant-R')
  results.append(dict(branch=name,pre_black=sorted(pre),pre_pose=[r,ph],turn=ch,post_full_black=sorted(full),post_pruning=sorted(postC),full_future_parity_tests=ft))
 roots.append(dict(phase_in_G_U=phase,full_root_black=sorted(B),root_pose=[p,h],root_pruning=sorted(C),normalized_heading_N_pruning=norm,word=w,drift=dr,root_parity_tests=tests,predecessor_cell=r,first_future_read_of_predecessor=hit,type=kind,branches=results))
 p,h,ch,old=advance(B,p,h,182+phase)
assert counts=={'double L/permanent-R':22,'unique relevant-R':46,'unique L':36}
# Exact symbolic exclusion of all16 remote circuit cells from radius n-3.
# Represent each coordinate as a*n+b and prove signed coordinate >= n-2 for n>=20.
origins=[((1,-1),(1,0),0),((-1,0),(3,-4),3),((-5,5),(-1,0),2),((-3,0),(-3,8),1)]
affine=[]
for ax,ay,hh in origins:
 for g in sorted(G):
  dx,dy=rot(g,hh-1);coords=[(ax[0],ax[1]+dx),(ay[0],ay[1]+dy-3)]
  witnesses=[]
  for axis,(a,b)in enumerate(coords):
   for sign in(-1,1):
    slope=sign*a-1;constant=sign*b+2
    if slope>=0 and 20*slope+constant>=0:witnesses.append((axis,sign,slope,constant))
  assert witnesses;affine.append(dict(origin=[ax,ay,hh],offset=g,relative_coordinates=coords,witness=witnesses[0]))
assert any(row['relative_coordinates']==[(1,-2),(1,-2)]for row in affine)

B61,p61,h61=ref['snap'][61];C61={q for q,i in B61.items()if i in ref['deaths']};q=(0,2)
assert(p61,h61)==((0,3),0)and B61[q]==60 and len(B61)==15 and len(C61)==11 and q not in C61
controls=[]
for n in(20,80,400):
 live_seed=twenty(n);dead_seed=G|{(-n,j)for j in range(16)};assert len(live_seed)==len(dead_seed)==20
 live=trace(live_seed,624*n-1516+983,{60,61});dead=trace(dead_seed,390,{60,61})
 LB,lp,lh=live['snap'][61];DB,dp,dh=dead['snap'][61]
 assert(lp,lh)==(dp,dh)==(p61,h61)and live['word'][:61]==dead['word'][:61]==ref['word'][:61]
 assert set(LB)^set(DB)==(live_seed-G)^(dead_seed-G)
 radius=n-3;inside=lambda S:{z for z in S if max(abs(z[0]-p61[0]),abs(z[1]-p61[1]))<=radius}
 assert inside(LB)==inside(DB)and len(LB)==len(DB)==31
 dist=min(max(abs(z[0]-p61[0]),abs(z[1]-p61[1]))for z in set(LB)^set(DB));assert dist==n-2
 LC={z for z,i in LB.items()if i in live['deaths']};DC={z for z,i in DB.items()if i in dead['deaths']}
 assert LC==set(LB)and DC==C61 and live['deaths'][60]==624*n-1516 and 60 not in dead['deaths']
 # Genuine previous update is R on BOTH full boards. Quotient branching differs only after retrospective pruning.
 assert live['word'][60]==dead['word'][60]=='R'
 controls.append(dict(n=n,initial_live=sorted(live_seed),initial_permanent=sorted(dead_seed),cut=61,pose=[p61,h61],identical_neighborhood_radius=radius,nearest_full_field_difference=dist,live_full=[dict(cell=z,identity=i,death=live['deaths'].get(i))for z,i in sorted(LB.items())],permanent_full=[dict(cell=z,identity=i,death=dead['deaths'].get(i))for z,i in sorted(DB.items())],live_pruning=sorted(LC),permanent_pruning=sorted(DC),marked_cell=q,marked_birth=60,marked_live_death=live['deaths'][60],live_quotient_predecessor_degree=1,permanent_quotient_predecessor_degree=2,live_complete_reads=len(live['word']),live_tail_pose=[live['p'],live['h']],live_tail_word=live['tail_word'],live_tail_black=sorted(live['B']),live_tail_tests=live['ray_tests'],permanent_complete_reads=len(dead['word']),permanent_tail_pose=[dead['p'],dead['h']],permanent_tail_word=dead['tail_word'],permanent_tail_black=sorted(dead['B']),permanent_tail_tests=dead['ray_tests']))
 print('n',n,'same radius',radius,'different degree1/2','late death',live['deaths'][60],flush=True)
source_names=['TWENTY_CELL_RELEVANT_STOCK_MANIFEST.json','RETURN_PERMANENT_OUTPUT_DEBT_MANIFEST.json','check_return_permanent_output_debt.py','WRITTEN_WAKE_PORT_OBSTRUCTION_MANIFEST.json']
out=dict(status='AUTHOR exact pruning-quotient predecessor law and bounded literal controls; independent audit requested',scope='Canonical basin parametrization plus a local-branch-test countercontrol. Not two inverses of one full board, not universal basin coverage, not noncapture undecidability.',source_hashes={s:hashlib.sha256((P/s).read_bytes()).hexdigest()for s in source_names if(P/s).exists()},canonical_root_count=len(roots),branch_type_counts=counts,canonical_root_mass_range=[min(len(r['root_pruning'])for r in roots),max(len(r['root_pruning'])for r in roots)],canonical_roots=roots,reference61=dict(full_black=sorted(B61),pose=[p61,h61],pruning=sorted(C61),prefix=ref['word'][:182],tail_word=U,all_future_x_min=0),remote_affine_exclusion_guards=affine,controls=controls)
(P/'PRUNED_PREDECESSOR_BASIN_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print('root types',counts,'root mass',out['canonical_root_mass_range'],flush=True)
