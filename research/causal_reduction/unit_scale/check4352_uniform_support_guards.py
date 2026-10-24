"""Exact affine support guards for R=200+52N, N>=1.
This checks the finite component-gluing inequalities, not a sampled horizon.
"""
from pathlib import Path
import json,hashlib
from check4352_noncrossing_producer import setup,H,W,J,L
from check_prepared1564_router_geometry import trace,infer
P=Path(__file__).resolve().parent

def box(pts):return[min(x+y for x,y in pts),max(x+y for x,y in pts),min(x-y for x,y in pts),max(x-y for x,y in pts)]
def affine(a,b):return[b-a,a] # coefficient of N, constant

def as_box(b0,b1):return[affine(a,b)for a,b in zip(b0,b1)]
def value(a,n):return a[0]*n+a[1]
def less(a,b): # a(N)<b(N) for every N>=1
 d=a[0]-b[0],a[1]-b[1];return d[0]<=0 and sum(d)<0

def disjoint(a,b):
 for index,name in[(0,'u'),(2,'t')]:
  if less(a[index+1],b[index]):return name+' first-before-second'
  if less(b[index+1],a[index]):return name+' second-before-first'
 return None

def data(n):
 R=200+52*n;start,B,ss,caps=setup(R,n);flights=[];routers=[];seed0=infer(H*30,start,3)['input'];stageword=[];tt=0
 for s in ss:
  p,h=s['start']
  if s['kind'] in('H','wave'):
   w=H if s['kind']=='H'else W;count=s['count'];rows=list(trace(w,p,h));end=rows[-1][1];d=end[0]-p[0],end[1]-p[1]
   pts=[z[1]for z in rows[:-1]]
   if count:pts +=[(x+(count-1)*d[0],y+(count-1)*d[1])for x,y in pts[:]]
   bb=box(pts)
   if s['kind']=='H':flights.append({'box':bb,'start':p,'end':(p[0]+count*d[0],p[1]+count*d[1]),'count':count})
   stageword.append({'kind':s['kind'],'count':count,'word':w,'start':p,'heading':h,'time':tt});tt+=len(w)*count
  else:
   rows=list(trace(s['word'],p,h));pts=[z[1]for z in rows[:-1]]
   if s['kind']=='router':pts +=[tuple(q)for q in caps[s['index']-1]];routers.append(box(pts))
   stageword.append({'kind':s['kind'],'count':1,'word':s['word'],'start':p,'heading':h,'time':tt});tt+=len(s['word'])
 # The launch contract and finite wave share this entire central u window.
 central=[-61,52*n+19,-50,78]
 return start,seed0,flights,routers,stageword,central,B
D0=data(0);D1=data(1);FB=[as_box(a['box'],b['box'])for a,b in zip(D0[2],D1[2])];RB=[as_box(a,b)for a,b in zip(D0[3],D1[3])];SB=as_box(box(D0[1]),box(D1[1]));CB=as_box(D0[5],D1[5]);guards=[]
for j,r in enumerate(RB):
 for i,f in enumerate(FB):
  if i in(j,j+1):continue
  why=disjoint(r,f);assert why,('foreign router/flight',j,i,r,f);guards.append(['router-flight',j+1,i+1,why])
 for k in range(j):
  why=disjoint(r,RB[k]);assert why,('router pair',j,k);guards.append(['router-router',j+1,k+1,why])
 why=disjoint(r,SB);assert why;guards.append(['router-initial-seed',j+1,why])
 why=disjoint(r,CB);assert why;guards.append(['router-central-window',j+1,why])
for i in range(5):
 for j in range(i):
  why=disjoint(FB[i],FB[j]);assert why;guards.append(['flight-flight',i+1,j+1,why])
 if i:
  why=disjoint(FB[i],SB);assert why;guards.append(['flight-initial-seed',i+1,why])
why=disjoint(SB,CB);assert why;guards.append(['initial-seed-central-window',why])
# Two completed useful flights contain the whole central window with32 guard.
mature=[]
for i in[0,2]:
 a,b=D0[2][i],D1[2][i]
 starts=affine(sum(a['start']),sum(b['start']));ends=affine(sum(a['end']),sum(b['end']))
 if i==5:lo=[starts[0],starts[1]+32];hi=[ends[0],ends[1]-32]
 else:lo=[ends[0],ends[1]+32];hi=[starts[0],starts[1]-32]
 assert less(lo,CB[0]) and less(CB[1],hi),(i,lo,hi,CB)
 mature.append({'flight':i+1,'guarded_u_interval':[lo,hi]})
for i in[1,3]:assert disjoint(FB[i],CB).startswith('t')
# Last writer begins far NE of the entire launch/wave window; its preceding
# router/fringe and every missing infinite-past cell are beyond that window.
a,b=D0[2][4],D1[2][4];startu=affine(sum(a['start']),sum(b['start']));limit=[startu[0],startu[1]-32];assert less(CB[1],limit)
assert all(value(affine(a['count'],b['count']),1)>=60 for a,b in zip(D0[2],D1[2]))
# Reconstruct the full mature black profiles in the common physical gauge.
from collections import Counter
actual_profiles=set()
for i in [0,2]:
    flight=D1[2][i];head=3 if i in (0,2,4) else 1
    counts=Counter((q[0]-q[1],q[0]%2)for _,q,hh,c in list(trace(H,flight['start'],head))[:-1])
    actual_profiles|={j for j,k in counts.items()if k%2}
assert actual_profiles=={tuple(j)for j in L['other_full_black_profiles']}
# Bind every affine stage, including literal words and global time.
stages=[]
for a,b in zip(D0[4],D1[4]):
 assert a['word']==b['word']and a['heading']==b['heading']and a['kind']==b['kind']
 stages.append({'kind':a['kind'],'word':a['word'],'count_N_constant':affine(a['count'],b['count']),
 'start_x_N_constant':affine(a['start'][0],b['start'][0]),'start_y_N_constant':affine(a['start'][1],b['start'][1]),
 'heading':a['heading'],'start_time_N_constant':affine(a['time'],b['time'])})
# Semantic seed families, rather than assuming a sorted global correspondence.
seedfam=[]
for n0,n1 in [(sorted(D0[1]),sorted(D1[1]))]:
 for a,b in zip(n0,n1):seedfam.append([affine(a[0],b[0]),affine(a[1],b[1])])
for r0,r1,r in zip(D0[4],D1[4],stages):pass
for j,router in enumerate(J['routers']):
 source0=[s for s in D0[4]if s['kind']=='router'][j]['start'];source1=[s for s in D1[4]if s['kind']=='router'][j]['start']
 for x,y in router['extra_black_relative_input']:
  seedfam.append([affine(source0[0]+x,source1[0]+x),affine(source0[1]+y,source1[1]+y)])
for x,y in L['fresh_cap']:seedfam.append([[0,x],[0,y]])
assert len(seedfam)==394
for n,d in[(0,D0),(1,D1)]:assert{(value(a,n),value(b,n))for a,b in seedfam}==d[6]
# Distinctness for all N: two affine coordinates can coincide only at one rational
# N (or identically); explicitly rule out every integer solution >=1.
for i,(ax,ay)in enumerate(seedfam):
 for bx,by in seedfam[:i]:
  cand=None;possible=True
  for a,b in[(ax,bx),(ay,by)]:
   slope=a[0]-b[0];constant=b[1]-a[1]
   if slope==0:
    if constant:possible=False;break
   elif constant%slope:possible=False;break
   else:
    v=constant//slope
    if cand is not None and cand!=v:possible=False;break
    cand=v
  assert not(possible and(cand is None or cand>=1)),(i,cand)
out={'scope':__doc__,'status':'PASS exact affine support guards','domain':'N>=1, R=200+52N','seed_mass':394,'seed_families':seedfam,
 'initial_pose':{'x_N_constant':affine(D0[0][0],D1[0][0]),'y_N_constant':affine(D0[0][1],D1[0][1]),'heading':3},
 'stages':stages,'router_read_and_cap_boxes':RB,'flight_read_boxes':FB,'initial_seed_box':SB,'central_window':CB,
 'mature_black_profiles':sorted(actual_profiles),'guards':guards,'mature_completed_writer_intervals':mature,'last_writer_NE_guard':limit,
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared4352_uniform_support_manifest.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(guards),'guards;',len(stages),'stages;',len(seedfam),'distinct affine seed cells')
