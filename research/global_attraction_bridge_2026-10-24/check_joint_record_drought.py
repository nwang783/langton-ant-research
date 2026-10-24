"""Full-field controls for the four-normal last-record recursion, not a global occurrence proof."""
from pathlib import Path
import bisect,hashlib,json
from check_return_permanent_output_debt import DXY,rot,future,twenty
from certified_comparison_perturbation import geometry
P=Path(__file__).parent
CANON=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text())['W']
CANONICAL={CANON[i:]+CANON[:i]for i in range(104)}

def max_tree(a):
 n=1
 while n<len(a):n*=2
 tree=[0]*(2*n);tree[n:n+len(a)]=a
 for i in range(n-1,0,-1):tree[i]=max(tree[2*i],tree[2*i+1])
 def query(l,r):
  z=0;l+=n;r+=n
  while l<r:
   if l&1:z=max(z,tree[l]);l+=1
   if r&1:r-=1;z=max(z,tree[r])
   l//=2;r//=2
  return z
 return query

def run(name,seed,N,target):
 B={q:-i-1 for i,q in enumerate(sorted(seed))};p=(0,0);h=1;births={};deaths={};pos=[];records=[];headrecords=[];snap={}
 checkpoints=set(target)
 if name.startswith('MT_'):
  n=int(name[3:]);checkpoints|={29671+104*n,88368+208*n}
 # normal order N,E,S,W, matching heading. Entire initial support is in hull.
 vals=lambda q:(q[1],q[0],-q[1],-q[0])
 ext=[max(vals(q)[a]for q in set(seed)|{p})for a in range(4)];hext=list(vals(p));initial_ext=list(ext)
 for t in range(N):
  v=vals(p)
  for a in range(4):
   if v[a]>hext[a]:assert v[a]==hext[a]+1 and h==a;hext[a]=v[a];headrecords.append((t,a))
   if v[a]>ext[a]:assert v[a]==ext[a]+1 and h==a and p not in B;ext[a]=v[a];records.append((t,a))
  if t in checkpoints:snap[t]=dict(pose=[p,h],full_field=[[q,i]for q,i in sorted(B.items())],hull=list(ext))
  pos.append(p);old=B.pop(p,None)
  if old is None:B[p]=t;births[t]=p;h=(h+1)%4
  else:deaths[old]=t;h=(h-1)%4
  p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 pos.append(p);v=vals(p)
 for a in range(4):
  if v[a]>hext[a]:assert v[a]==hext[a]+1 and h==a;hext[a]=v[a];headrecords.append((N,a))
  if v[a]>ext[a]:assert v[a]==ext[a]+1 and h==a and p not in B;ext[a]=v[a];records.append((N,a))
 w,dr,tail,tests=future(B,p,h);assert w in CANONICAL
 if name.startswith('MT_'):
  n=int(name[3:]);ss=29671+104*n;ee=88368+208*n
  assert [z for z in records if ss<=z[0]<=ee]==[(ss,0),(ee,3)]
  assert [z for z in headrecords if ss<=z[0]<=ee]==[(ss,0),(ee,3)]
  assert max(deaths[-i-1]for i in range(len(seed)))==27201+104*n<ss
  assert snap[ss]['hull']==[262+2*n,250+2*n,0,1]
  assert snap[ee]['pose']==[(-2,372),3] and ee-ss==58697+104*n

 R=[t for t,a in records];Rdir=[[t for t,a in records if a==j]for j in range(4)];gaps=[R[i+1]-R[i]for i in range(len(R)-1)];rmq=max_tree(gaps)
 def interval(s,t,q):
  assert s<=t
  if s==t:return dict(start=s,end=t,duration=0,H=0,record_count=0,directions=[])
  lo=bisect.bisect_right(R,s);hi=bisect.bisect_left(R,t);rr=R[lo:hi]
  H=max((rr[0]-s,t-rr[-1],rmq(lo,hi-1)))if rr else t-s
  dd=[]
  for a in range(4):
   aa=Rdir[a];i=bisect.bisect_right(aa,s);j=bisect.bisect_left(aa,t)
   if i<j:dd.append(dict(normal=a,count=j-i,last=aa[j-1]))
  dd.sort(key=lambda a:a['last']);later=0
  for row in reversed(dd):
   ell=row['last'];a=row['normal'];n=row['count']
   distance=vals(pos[ell])[a]-vals(q)[a]
   assert distance>=n and n<=t-ell<=H*(1+later)
   row.update(distance_from_endpoint=distance,remaining_time=t-ell,later_direction_count=later,recursion_bound=H*(1+later));later+=n
  assert later==len(rr)<=((H+1)**len(dd))-1
  assert t-s<=H*(len(rr)+1)<=H*((H+1)**len(dd))<=H*((H+1)**4)
  return dict(start=s,end=t,duration=t-s,H=H,record_count=len(rr),directions=dd,refined_upper=H*((H+1)**len(dd)),four_direction_upper=H*((H+1)**4))
 checked=0;targets=[];maxage=0;maxH=0;largest_ratio=None
 for b,q in births.items():
  d=deaths.get(b)
  if d is None:continue
  z=interval(b,d,q);checked+=1;maxage=max(maxage,d-b);maxH=max(maxH,z['H'])
  ratio=(d-b)/z['H']
  if largest_ratio is None or ratio>largest_ratio['ratio']:largest_ratio=dict(ratio=ratio,cell=q,**z)
  if b in target:targets.append(dict(cell=q,**z))
 # Stronger endpoint-in-old-hull lemma at named actual cuts, not only closed walks.
 # Seed cells are always in the time-zero hull; use their literal first deaths.
 open_examples=[]
 for q,i in ((q,-i-1)for i,q in enumerate(sorted(seed))):
  if i in deaths:open_examples.append(dict(endpoint=q,**interval(0,deaths[i],q)))
 longest=max([(0,R[0])] + [(R[i],R[i+1])for i in range(len(R)-1)]+[(R[-1],N)],key=lambda z:z[1]-z[0])if R else(0,N)
 out=dict(name=name,seed=sorted(seed),initial_hull=initial_ext,physical_reads=N,terminal_pose=[p,h],terminal_full_field=[[q,i]for q,i in sorted(B.items())],tail_word=w,tail_drift=dr,infinite_parity_tests=tests,pristine_support_hull_records=records,ordinary_head_records=headrecords,completed_R_lifetimes_checked=checked,max_completed_age=maxage,max_local_record_drought=maxH,largest_age_over_drought=largest_ratio,marked_intervals=targets,seed_input_open_interval_checks=open_examples,named_full_snapshots=snap,longest_observed_union_record_gap=dict(start=longest[0],end=longest[1],length=longest[1]-longest[0]))
 print(name,'reads',N,'R',checked,'records',len(R),'maxage',maxage,'maxH',maxH,'marked',[(z['duration'],z['H'],len(z['directions']))for z in targets],flush=True)
 return out

jobs=[]
for n in(20,80,400):jobs.append((f'twenty_{n}',twenty(n),624*n-1516+983+208,(60,)))
G={(0,-1),(1,1),(1,3),(2,2)}
for n in(20,40,80):
 poses=[((0,0),1),((7*n-1,7*n),0),((5*n,9*n-4),3),((n+5,5*n),2)];seed={(o[0]+rot(q,h-1)[0],o[1]+rot(q,h-1)[1])for o,h in poses for q in G}
 jobs.append((f'sixteen_{n}',seed,780*n-1207+8986+208,(156*n-59,)))
mt=json.loads((P/'RECORD_GAP_COMPACTNESS_CHECKED.json').read_text())
for c in mt['controls']:jobs.append((f"MT_{c['n']}",set(map(tuple,c['seed'])),c['next_N_record_cut'],(20165,)))
controls=[run(*j)for j in jobs]
# Universal MT drought, from exact affine phase endpoints, not interpolation.
A=json.loads((P/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());RR=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());W=RR['W'];qm=(202,201)
pre=W*100+W[:13]+RR['modes']['M']['recovery_word'];preQ,_,mend,mh=geometry((0,0),1,pre);assert len(pre)==21125 and (mend,mh)==((228,229),0)
FQ,FH,_,_=geometry(mend,mh,W[41:]+W[:41]);TP,TH,te,th=geometry((0,0),0,A['T_recovery']);SQ,SH,_,_=geometry(te,th,A['T_tail_word']);post,_,pe,ph=geometry((207,229),1,A['postcollision_word']);NW=mt['controls'][0]['tail_word'];NQ,NH,_,_=geometry((155,215),1,NW)
# mt next-record word is phase14; use the actual sufficient capture phase75 instead.
NW=A['controls'][0]['complete_future_certificate']['tail_word'];NQ,NH,_,_=geometry((155,215),1,NW)
ineq=[]
def nn(alpha,beta,label):
 assert alpha>=0 and 100*alpha+beta>=0,(label,alpha,beta)
 ineq.append((label,alpha,beta))
def inside(pt,label):
 # pt=((x slope,x constant),(y slope,y constant)); old hull x[-1,2n+250], y[0,2n+262].
 (ax,bx),(ay,by)=pt
 nn(ax,bx+1,label+'_W');nn(2-ax,250-bx,label+'_E');nn(ay,by,label+'_S');nn(2-ay,262-by,label+'_N')
for i,(x,y)in enumerate(preQ):inside(((0,x),(0,y)),f'pre{i}')
assert min(x for x,y in preQ)==-1 and min(y for x,y in preQ)==0
for i,(x,y)in enumerate(FQ):
 inside(((0,x),(0,y)),f'flight_first{i}');inside(((2,x-2),(2,y-2)),f'flight_last{i}')
for i,(x,y)in enumerate(FQ[:76]):inside(((2,x),(2,y)),f'flight_partial{i}')
assert (FQ[76],FH[76])==((230,229),0)
for i,(x,y)in enumerate(TP):inside(((2,230+x),(2,229+y)),f'T{i}')
assert max(x for x,y in TP[:8471])==20 and max(y for x,y in TP[:8470])==32 and TP[8470]==(3,33)
for i,(x,y)in enumerate(SQ):
 inside(((2,230+x),(2,229+y)),f'SW_first{i}');inside(((0,246+x),(0,245+y)),f'SW_last_full{i}')
for i,(x,y)in enumerate(SQ[:100]):inside(((0,244+x),(0,243+y)),f'SW_partial{i}')
assert(SQ[100],SH[100])==((-38,-14),2)
for i,(x,y)in enumerate(post):inside(((0,x),(0,y)),f'post{i}')
assert(pe,ph)==((155,215),1)
NWpre,_,ne,nh=geometry((155,215),1,NW*77+NW[:90])
for i,(x,y)in enumerate(NWpre):inside(((0,x),(0,y)),f'NW_before_W{i}')
assert(ne,nh)==((-2,372),3) and len(NWpre)==8098
alln=dict(parameter='integer n>=100',last_record='29671+104n, N',next_record='88368+208n, W',drought='58697+104n',last_original_death='27201+104n',old_hull='[-1,2n+250] x [0,2n+262]',next_pose=[[-2,372],3],affine_inequality_count=len(ineq),affine_inequality_sha256=hashlib.sha256(json.dumps(ineq,separators=(',',':')).encode()).hexdigest(),all_n_marked_ages={'twenty':'624n-1576','sixteen':'624n-1148','MT':'208n+11640'},universal_consequence='largest local pristine union-record gap H satisfies A<=H(H+1)^4 for each signed all-n returned lifetime')
files=['RECORD_GAP_COMPACTNESS_MANIFEST.json','../audits/check_record_gap_compactness_independent.json','TWENTY_RELEVANT_STOCK_MANIFEST.json','../audits/twenty_relevant_stock_independent.json','TRANSVERSE_FAR_MODULE_MANIFEST.json','../audits/check_transverse_far_module_independent.json','TRANSVERSE_PERMANENT_BUDGET_MANIFEST.json','../audits/check_transverse_permanent_budget_independent.json','../audits/relevant_radius_recurrence_bridge_2026-10-24_1018.md']
for f in files:assert(P/f).exists(),f
out=dict(status='AUTHOR exact joint-record excursion lemma; independent audit pending',scope='Universal finite-path inequality. Literal controls and inherited all-n ages; no universal bound on record drought.',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files},physical_reads=sum(c['physical_reads']for c in controls),completed_R_lifetimes_checked=sum(c['completed_R_lifetimes_checked']for c in controls),all_n_MT_drought=alln,controls=controls)
(P/'JOINT_RECORD_DROUGHT_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
