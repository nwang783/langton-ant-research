"""Finite boundary-current lemma and whole-field permanent-pinning controls."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,future
from certified_comparison_perturbation import geometry
P=Path(__file__).parent

def boundary_check(B,p,h,box,limit=100):
 x0,x1,y0,y1=box;inside=lambda q:x0<=q[0]<=x1 and y0<=q[1]<=y1;inner=lambda q:x0<q[0]<x1 and y0<q[1]<y1
 C=set(B);positions=[p];turns=[];states=[set(C)];heads=[h]
 while len(turns)<limit and inside(p):
  ch='L'if p in C else'R';C.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1]);turns.append(ch);positions.append(p);states.append(set(C));heads.append(h)
 assert not inside(p)
 end=max(t for t,q in enumerate(positions)if inner(q));assert inner(positions[0]);sigma=(-1)**sum(positions[0])*(1 if heads[0]%2==0 else-1)
 sides=[[(x,y1)for x in range(x0+1,x1)],[(x1,y)for y in range(y1-1,y0,-1)],[(x,y0)for x in range(x1-1,x0,-1)],[(x0,y)for y in range(y0+1,y1)]]
 corners={(x0,y0),(x0,y1),(x1,y0),(x1,y1)};corner_seen=set();dom=[0]*4;cornerchanges=[0]*4;phi=lambda a,side,C:sum((j+1)*(int(q in C)if ((-1)**sum(q)==(sigma if a%2==0 else-sigma))else int(q not in C))for j,q in enumerate(side))
 # Side order top/right/bottom/left; normal-arrival axis vertical on even side indices.
 initial=[]
 for a,side in enumerate(sides):initial.append(phi(a,side,states[0]))
 t=0;episodes=[]
 while t<end:
  if inner(positions[t]):t+=1;continue
  b=t
  while t<end and not inner(positions[t]):t+=1
  cells=positions[b:t];word=''.join(turns[b:t]);cs=[q for q in cells if q in corners]
  assert len(cells)in(2,3)and word in('RR','LL','RRR','LLL')and len(cs)==len(cells)-2
  if cs:assert cs[0]not in corner_seen;corner_seen.add(cs[0])
  for a,side in enumerate(sides):
   hits=sum(q in side for q in cells);change=phi(a,side,states[t])-phi(a,side,states[b])
   if not cs and hits:assert hits==2 and change==-1;dom[a]+=1
   elif cs and hits:assert hits==1 and abs(change)<=len(side);cornerchanges[a]+=change
   else:assert change==0
  episodes.append((b,t,word));
 for a,side in enumerate(sides):
  assert dom[a]==initial[a]-phi(a,side,states[end])+cornerchanges[a]
  assert dom[a]<=len(side)*(len(side)+1)//2+2*len(side)
 reads=sum(b-a for a,b,w in episodes);W=x1-x0+1;H=y1-y0+1;bound=2*W*W+2*H*H+2*W+2*H-12;assert reads<=bound
 return dict(exit=len(turns),interior_end=end,boundary_reads=reads,corner_reads=len(corner_seen),dominos=dom,bound=bound)

small=[];cells=[(x,y)for x in range(3)for y in range(3)]
for mask in range(512):
 B={q for i,q in enumerate(cells)if mask>>i&1}
 for h in range(4):small.append(boundary_check(B,(1,1),h,(0,2,0,2),50))
assert len(small)==2048
A=json.loads((P/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());R=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());J=json.loads((P/'JOINT_RECORD_DROUGHT_CHECKED.json').read_text())
TP,TH,te,th=geometry((0,0),0,A['T_recovery']);SQ,SH,_,_=geometry(te,th,A['T_tail_word']);post,_,pe,ph=geometry((207,229),1,A['postcollision_word']);NW=A['controls'][0]['complete_future_certificate']['tail_word'];NQ,_,_,_=geometry(pe,ph,NW)
assert TP[6452]==(20,8)and TP[8494]==(1,33)and A['T_recovery'][6452]==A['T_recovery'][8494]=='R'
assert max(i for i,q in enumerate(TP)if q==(20,8))==6452 and max(i for i,q in enumerate(TP)if q==(1,33))==8494
assert max(x for x,y in SQ)<20 and max(y for x,y in SQ)<33 and max(x for x,y in post+NQ)<=240 and min(y for x,y in post+NQ)>0
# Complete first standard period removes the entire negative-x fringe and leaves genuine R20 at origin.
B={tuple(q):-i-1 for i,q in enumerate(R['canonical_source'])};p=(0,0);h=1
for t,c in enumerate(R['W']):
 old=B.pop(p,None);assert(c=='L')==(old is not None)
 if old is None:B[p]=t;h=(h+1)%4
 else:h=(h-1)%4
 p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
assert B[(0,0)]==20 and min(x for x,y in B)==min(y for x,y in B)==0
WQ,_,_,_=geometry((0,0),1,R['W']);assert min(x for x,y in WQ)>=-1 and min(y for x,y in WQ)>=0
preQ,_,mp,mh=geometry((0,0),1,R['W']*100+R['W'][:13]+R['modes']['M']['recovery_word']);assert min(x for x,y in preQ[104:])>=0 and min(y for x,y in preQ[104:])>=0
_,_,localT,_=future({tuple(q):i for i,q in enumerate(A['T_output_black'])},te,th);assert len(localT)==21 and max(localT.values())<104*100-628
# Strict interior affine extrema for the whole SW flight, including the actual collision.
affine=[]
def strict(ax,bx,ay,by,label):
 for aa,bb in[(ax,bx-1),(2-ax,249-bx),(ay,by-1),(2-ay,261-by)]:
  assert aa>=0 and 100*aa+bb>=0,(label,aa,bb);affine.append((label,aa,bb))
for i,(x,y)in enumerate(SQ):strict(2,230+x,2,229+y,f'first{i}');strict(0,246+x,0,245+y,f'last{i}')
for i,(x,y)in enumerate(SQ[:101]):strict(0,244+x,0,243+y,f'partial{i}')
for i,(x,y)in enumerate(post):strict(0,x,0,y,f'post{i}')
controls=[]
for c in J['controls']:
 if not c['name'].startswith('MT_'):continue
 n=int(c['name'][3:]);s=29671+104*n;start=32433+104*n;end=80270+208*n;snap=c['named_full_snapshots'][str(s)];B={tuple(q):i for q,i in snap['full_field']};p=tuple(snap['pose'][0]);h=snap['pose'][1];death={};Bstart=None;pins={(0,0):20,(2*n+250,2*n+237):27653+104*n,(2*n+231,2*n+262):29695+104*n}
 for t in range(s,end):
  if t==start:
   Bstart=dict(B);pose_start=[p,h]
   assert all(B[q]==i for q,i in pins.items())
   assert(min(x for x,y in B),max(x for x,y in B),min(y for x,y in B),max(y for x,y in B))==(0,2*n+250,0,2*n+262)
  if t>=start:assert 0<p[0]<2*n+250 and 0<p[1]<2*n+262 and all(B[q]==i for q,i in pins.items())
  old=B.pop(p,None)
  if old is None:B[p]=t;h=(h+1)%4
  else:death[old]=t;h=(h-1)%4
  p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 w,d,tail,tests=future(B,p,h);death.update({i:end+tt for i,tt in tail.items()});assert w==NW
 assert all(i not in death and B[q]==i for q,i in pins.items());relevant={q for q,i in Bstart.items()if i in death};assert len(relevant)==807
 controls.append(dict(n=n,start=start,end=end,duration=end-start,pose_start=pose_start,pose_end=[p,h],constant_BLACK_hull=[0,2*n+250,0,2*n+262],permanent_R_pins=[dict(cell=q,birth=i)for q,i in pins.items()],whole_start_black=[[q,i]for q,i in sorted(Bstart.items())],whole_end_black=[[q,i]for q,i in sorted(B.items())],whole_start_relevant=sorted(relevant),tail_word=w,tail_drift=d,infinite_parity_tests=tests,physical_updates=end-s))
 print(n,'constant hull duration',end-start,'relevant',len(relevant),'permanent pins',len(pins),flush=True)
files=['JOINT_RECORD_DROUGHT_MANIFEST.json','../audits/check_joint_record_drought_independent.json','SOUTHWEST_ARCHIVE_IMPORT_MANIFEST.json','../audits/check_southwest_archive_import_independent.json','../first_principles_new/recurrent_boundary_current.md']
for f in files:assert(P/f).exists(),f
out=dict(status='AUTHOR boundary peeling/pinning interface; independent audit pending',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files},three_by_three_complete_exhaustion=dict(states=len(small),max_exit=max(x['exit']for x in small),max_boundary_reads=max(x['boundary_reads']for x in small),max_corner_reads=max(x['corner_reads']for x in small),results_sha256=hashlib.sha256(json.dumps(small,separators=(',',':')).encode()).hexdigest()),all_n_pinning=dict(domain='integer n>=100',interval='[32433+104n,80270+208n]',duration='47837+104n',BLACK_hull='[0,2n+250] x [0,2n+262]',whole_entry_relevant=807,affine_inequalities=len(affine),affine_sha256=hashlib.sha256(json.dumps(affine,separators=(',',':')).encode()).hexdigest()),controls=controls,scope='Universal finite boundary-read budget and nested HEAD-region subintervals; full BLACK hull can remain exactly pinned. No unbounded number of distinct completed global droughts or autonomous renewal.' )
(P/'DROUGHT_BOUNDARY_PINNING_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
