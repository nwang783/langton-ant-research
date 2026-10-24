"""One exact double-input canonical perturbation map, full causal sources and all-future ray footprint."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,future
P=Path(__file__).parent
D=json.loads((P/'ALL_LENGTH_TWO_SIDED_MINIMUM_CHECKED.json').read_text());K=set(map(tuple,D['base']));W=D['base_word'];V=D['rule']['recovery'];Q=[];heads=[];p=(0,0);h=1
for ch in W:Q.append(p);heads.append(h);h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
assert p==(2,2)and heads[13]==0

def run(seed,N,expected=None,snapcuts=(),p=(0,0),h=1):
 B={q:-i-1 for i,q in enumerate(sorted(seed))};first={};deaths={};events=[];reads=[];word=[];snaps={}
 for t in range(N):
  if t in snapcuts:snaps[t]=(dict(B),p,h)
  reads.append(p);first.setdefault(p,t);old=B.pop(p,None);events.append(old)
  if old is None:B[p]=t;h=(h+1)%4;ch='R'
  else:deaths[old]=t;h=(h-1)%4;ch='L'
  if expected is not None:assert ch==expected[t]
  word.append(ch);p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 return dict(B=B,p=p,h=h,first=first,deaths=deaths,events=events,reads=reads,word=''.join(word),snaps=snaps)

def cert(z):
 w,dr,dead,tests=future(z['B'],z['p'],z['h']);z['tail_word']=w;z['drift']=dr;z['tests']=tests;z['deaths'].update({i:len(z['word'])+t for i,t in dead.items()});return z

def geom(p,h,w):
 R=[]
 for ch in w:R.append(p);h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 return R,p,h

# Exact mature incoming field restricted by SOUTHERN, not western, guard.
g=-12;M=set()
for i,q in enumerate(Q):
 r=(q[0]-Q[13][0],q[1]-Q[13][1]);lo=-((r[1]-g)//2);hi=0 if i<13 else -1
 for a in range(lo,hi+1):M.symmetric_difference_update({(r[0]+2*a,r[1]+2*a)})
assert(0,0)not in M and(2,2)not in M
kernel=M|{(0,0),(2,2)};assert len(kernel)==96
z=cert(run(kernel,5915,p=(0,0),h=0));F2=z['word'];assert(z['p'],z['h'],z['drift'])==((-18,17),1,(-2,2))
TQ,_,_=geom(z['p'],z['h'],z['tail_word']);assert min(y for x,y in z['reads']+TQ)==-12
# Entire ray of later first-visit phase13 particles, no cutoff in tail epochs.
rayhits={}
for t,(x,y)in enumerate(z['reads']):
 if x==y and x%2==0 and x>=4:rayhits.setdefault(x//2,t)
tailray=[]
for i,(x,y)in enumerate(TQ):
 if (x+y)%4:continue
 a=(x+y)//4
 if a<2 or(x-2*a)%2:continue
 k=(x-2*a)//2
 if k>=0 and(x-2*k,y+2*k)==(2*a,2*a):tailray.append((a,k,i));rayhits[a]=min(rayhits.get(a,10**99),5915+104*k+i)
assert rayhits=={2:632,3:672,4:844,5:1248,6:1272}and tailray==[]
initial_relevant={q for i,q in enumerate(sorted(kernel))if -i-1 in z['deaths']}
assert len(initial_relevant)==71 and {(0,0),(2,2)}<=initial_relevant
old_relative_births={}
for q in M:
 candidates=[]
 for i,r in enumerate(Q):
  dx,dy=q[0]+Q[13][0]-r[0],q[1]+Q[13][1]-r[1]
  if dx%2==0 and dy==dx:
   a=dx//2;tt=104*a+i-13
   if tt<0:candidates.append((tt,a,i))
 tt,a,i=max(candidates);assert W[i]=='R'and a>=-9;old_relative_births[q]=tt
assert old_relative_births[(-4,-1)]==-17
id_to_cell={-i-1:q for i,q in enumerate(sorted(kernel))}
old_consumptions=[dict(cell=q,birth_relative=old_relative_births[q],death_relative=z['deaths'][-i-1])for i,q in enumerate(sorted(kernel))if q in M and -i-1 in z['deaths']]
assert len(old_consumptions)==69 and all(v['death_relative']<5915 for v in old_consumptions)
# The isolated western crop fails exactly at read203, not just after a geometric crossing.
small=set(map(tuple,D['rule']['input_kernel']))|{(2,2)}
a=run(small,203,p=(0,0),h=0);assert a['word']==F2[:203]and(a['p'],a['h'])==((-4,-1),3)and(-4,-1)not in a['B']
assert z['reads'][203]==(-4,-1)and F2[203]=='L'

# Finite bounds for composing after any number of retained isolated NE scatters.
VP,_,_=geom((0,0),heads[13],V)
assert max(y for x,y in VP)<=20 and max(q[1]-Q[13][1]for q in Q)<=20
# Nonmarker source and past writes before output all lie below current marker y+20.
synthetic_max=6+max(Q[i][1]-Q[97][1]+(0 if i<97 else-2)for i in range(104))
assert synthetic_max<=20 and 206-12>20
assert max(y for x,y in K)==6 and max(y for x,y in Q)-2<=6

Aindices=[7,8,9,10,11,17,10**6,10**9]
controls=[]
for name,k,m in [('k9',9,None),('k100',100,None),('k500',500,None),('prefix1',100,1),('prefix3',100,3)]:
 if m is None:
  q=(2*k+2,2*k+1);prefix=W*k+W[:13];singlemarkers=set()
 else:
  q=(202+206*m,201+206*m);prefix=W*100+W[:13]+(V+W[97:]+W*100+W[:13])*m;singlemarkers={(202+206*i,201+206*i)for i in range(m)}
 T=len(prefix);extras={(q[0]+2*a,q[1]+2*a)for a in Aindices};seed=K|singlemarkers|{q,(q[0]+2,q[1]+2)}|extras
 u=cert(run(seed,T+5915,prefix+F2,{T}));B0,p0,h0=u['snaps'][T]
 assert(p0,h0)==(q,0)and u['first'][q]==T and u['first'][(q[0]+2,q[1]+2)]==T+124
 assert all(a not in u['first']for a in extras)
 inside={ (x-q[0],y-q[1])for x,y in B0 if y>=q[1]-12 and(x,y)not in extras};assert inside==kernel
 assert u['tail_word']==z['tail_word']and u['drift']==(-2,2)
 C={v for v,i in B0.items()if i in u['deaths']};assert C=={(v[0]+q[0],v[1]+q[1])for v in initial_relevant}
 assert all(B0[(v[0]+q[0],v[1]+q[1])]==T+t for v,t in old_relative_births.items())
 imported=[dict(cell=v,birth=i,death=u['deaths'][i])for v,i in B0.items()if i>=0 and i in u['deaths']];assert len(imported)==69
 assert u['events'][T+203]==T-17 and u['reads'][T+203]==(q[0]-4,q[1]-1)
 # Every unused ORIGINAL cell is tested against the full infinite future, not just the finite prefix.
 assert all(-i-1 not in u['deaths']for i,v in enumerate(sorted(seed))if v in extras)
 controls.append(dict(name=name,k=k,isolated_prefix_count=m,seed=sorted(seed),extra_indices=Aindices,entry_time=T,entry_pose=[q,0],entry_complete_field=[dict(cell=v,identity=i,death=u['deaths'].get(i))for v,i in sorted(B0.items())],entry_entire_pruning=sorted(C),old_wake_imports=sorted(imported,key=lambda v:v['death']),first_marked_reads=[T,T+124],first_western_guard_failure=dict(time=T+203,cell=(q[0]-4,q[1]-1),genuine_R_birth=T-17),terminal_time=T+5915,terminal_pose=[u['p'],u['h']],terminal_full_black=sorted(u['B']),tail_word=u['tail_word'],tail_drift=u['drift'],full_future_parity_tests=u['tests']))
 print(name,'T',T,'full future at',T+5915,'true entry population',len(C),'old imports',len(imported),'all extras NEVER read',flush=True)

sourcefiles=['ALL_LENGTH_TWO_SIDED_MINIMUM_MANIFEST.json','ALL_LENGTH_TWO_SIDED_MINIMUM_CHECKED.json','../audits/check_all_length_two_sided_minimum_independent.json','check_return_permanent_output_debt.py']
out=dict(status='AUTHOR exact double-scatter map and composable finite class; independent audit requested',scope='All k>=9 source transfer; any finite arbitrary leftover phase13-ray cohort at indices>=7, with indices2..6 white. Any finite prefix of the specified isolated NE scatters is allowed. Not all perturbations, not arbitrary old archive inside the southern guard.',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in sourcefiles},south_guard=-12,kernel=sorted(kernel),kernel_entire_pruning=sorted(initial_relevant),kernel_old_birth_offsets=[dict(cell=q,time=t)for q,t in sorted(old_relative_births.items())],post_word=F2,terminal_pose=[z['p'],z['h']],terminal_full_black=sorted(z['B']),tail_word=z['tail_word'],tail_drift=z['drift'],full_future_parity_tests=z['tests'],prefix_bbox=[min(x for x,y in z['reads']),max(x for x,y in z['reads']),min(y for x,y in z['reads']),max(y for x,y in z['reads'])],remaining_ray_first_reads=rayhits,infinite_tail_additional_ray_hits=tailray,old_wake_consumptions=old_consumptions,isolated_crop_first_disagreement=dict(read=203,cell=[-4,-1],heading=3,cropped='R',actual='L',actual_birth=-17),composition_bounds=dict(older_nonmarker_history_y_max_relative_to_previous_marker=20,next_pair_south_guard_relative_to_previous_marker=194,synthetic_past_y_max=synthetic_max,maximum_initial_K_y=6,maximum_omitted_prestart_synthetic_y=max(y for x,y in Q)-2),controls=controls)
(P/'PHASE13_DOUBLE_SCATTER_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
