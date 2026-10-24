"""Bounded controls for explicit finite record-clock forcing. No huge F-window is run."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,future
PTH=Path(__file__).parent
norm=lambda q:(q[1],q[0],-q[1],-q[0])
# Return the NEXT physical turn, opposite the most recent same-cell turn.
def predict(h,history):
 q=(0,0);hh=h
 for c in reversed(history):
  q=(q[0]-DXY[hh][0],q[1]-DXY[hh][1])
  if q==(0,0):return 'L'if c=='R'else'R'
  hh=(hh-(1 if c=='R'else-1))%4
 return 'R'

def trial(c):
 n=c['name'].split('_')[1];cut=88368+208*int(n);snap=c['named_full_snapshots'][str(cut)];B={tuple(q)for q,i in snap['full_field']};p=tuple(snap['pose'][0]);h=snap['pose'][1];ext=list(snap['hull']);hist=[]
 # Complete physical208-read preparation, no archive truncation.
 for t in range(208):
  v=norm(p);ext=[max(a,b)for a,b in zip(ext,v)];ch='L'if p in B else'R';hist.append(ch);B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 ext=[max(a,b)for a,b in zip(ext,norm(p))];B0=set(B);p0=p;h0=h;M0=list(ext);mem=(h,tuple(hist[-208:]));P=104;H=104;K=2*P+H+2;word=[];Q=[];records=[];last=0;d=None;predicted=0
 for t in range(P*K):
  v=norm(p)
  for a in range(4):
   if v[a]>ext[a]:assert v[a]==ext[a]+1;ext[a]=v[a];records.append((t,a));last=t
  assert t-last<H
  ch='L'if p in B else'R'
  if t<3*P:assert predict(h,hist[-208:])==ch;predicted+=1
  if t<P:Q.append(p);word.append(ch)
  else:assert ch==word[t%P]
  B.symmetric_difference_update({p});hist.append(ch);h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
  if t+1==P:
   assert(h,tuple(hist[-208:]))==mem;d=(p[0]-p0[0],p[1]-p0[1]);assert h==h0 and d!= (0,0)
 r,a=next((t,a)for t,a in records if P<t<=P+H);delta=norm(d)[a];assert delta>0 and M0[a]<=norm(p0)[a]+P+H
 axis=0 if d[0]else 1
 def mult(v):
  if v[axis]%d[axis]:return None
  k=v[axis]//d[axis]
  return k if v==(k*d[0],k*d[1])else None
 allcrit=[];maxhit=-1;maxoverlap=0
 for i,q in enumerate(Q):
  hits=[];overlap=[];crit={0}
  for z in B0:
   k=mult((z[0]-q[0],z[1]-q[1]))
   if k is not None and k>=0:hits.append(k);crit|={k,k+1};maxhit=max(maxhit,k);assert k<=2*P+H
  for j,z in enumerate(Q):
   m=mult((z[0]-q[0],z[1]-q[1]))
   if m is not None and(m>0 or(m==0 and j<i)):overlap.append(m);crit.add(m);maxoverlap=max(maxoverlap,m);assert m<=P
  assert max(crit)<=K-1
  for k in crit:assert(sum(j==k for j in hits)+sum(m<=k for m in overlap))%2==(word[i]=='L')
  allcrit.append(sorted(crit))
 fw,dr,_,tests=future({q:i for i,q in enumerate(B)},p,h);assert fw==''.join(word) and dr==d
 sha=lambda A:hashlib.sha256(json.dumps(sorted(A),separators=(',',':')).encode()).hexdigest()
 return dict(n=int(n),source_cut=cut,loop_start=cut+208,initial_full_mass=len(B0),initial_full_sha256=sha(B0),loop_pose=[p0,h0],old_full_hull=M0,memory_regression_length=208,memory_state_repeat_period=P,memory_predictions_checked=predicted,clock_H=H,observed_copies=K,physical_reads=208+P*K,word=''.join(word),drift=d,positive_record=[r,a],initial_ray_hit_max=maxhit,self_overlap_max=maxoverlap,all_critical_indices=allcrit,terminal_full_mass=len(B),terminal_full_sha256=sha(B),all_future_parity_tests=tests)

j=json.loads((PTH/'JOINT_RECORD_DROUGHT_CHECKED.json').read_text());controls=[trial(c)for c in j['controls']if c['name'].startswith('MT_')]
# Exercise truncated color prediction on four tiny full histories. A discrepancy can only be an old BLACK input.
reg=[]
for seed in[set(),{(0,0)},{(0,-1),(1,1),(1,3),(2,2)},{(-2,-1),(1,-2),(0,0)}]:
 B={q:-1 for q in seed};p=(0,0);h=0;hist=[];counts={a:0 for a in(1,4,16,64)}
 for t in range(1200):
  old=B.get(p);ch='L'if old is not None else'R'
  for a in counts:
   if t>=a and predict(h,hist[-a:])!=ch:
    assert ch=='L'and(old==-1 or old<t-a);counts[a]+=1
  if old is None:B[p]=t;h=(h+1)%4
  else:del B[p];h=(h-1)%4
  hist.append(ch);p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 reg.append(dict(seed=sorted(seed),reads=1200,only_old_BLACK_prediction_failures=counts))
small=[]
for H in(1,2):
 G=H*(H+1)**4;S=4*(2**G);F=G+1+2*S*S+(H+3)*S;small.append(dict(H=H,G=G,S=str(S),F_star=str(F)))
files=['FINITE_RECORD_CLOCK_MANIFEST.json','../audits/check_finite_record_clock_independent.json','JOINT_RECORD_DROUGHT_MANIFEST.json','../audits/check_joint_record_drought_independent.json','JOINT_RECORD_DROUGHT_CHECKED.json']
for f in files:assert(PTH/f).exists(),f
out=dict(status='AUTHOR explicit finite record-clock bound; independent audit pending',source_hashes={f:hashlib.sha256((PTH/f).read_bytes()).hexdigest()for f in files},formula='G=H(H+1)^4; S=4*2^G; F*=G+1+2*S^2+(H+3)*S',small_formula_regressions=small,truncated_prediction_regressions=reg,full_repeat_certificate_controls=controls,scope='No F*-length global search; controls test local proof interfaces on actual full canonical tails. Universal explicit bound is analytic.')
(PTH/'EXPLICIT_RECORD_CLOCK_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n');print('full controls',len(controls),'reads',sum(c['physical_reads']for c in controls),'prediction regressions4800; explicit formula only H1/2 evaluated')
