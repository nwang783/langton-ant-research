from pathlib import Path
from fractions import Fraction as F
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';data=json.loads((D/'foreign_kinked_barrier_and_turn.json').read_text());J=json.loads((R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json').read_text());W={a:r['word']for a,r in zip('DCVUFQB',J['macro_words'])};M='LLLLRLRRRRL';dirs=(1j,1,-1j,-1)
def walk(w,check=True):
 p=0j;h=0;odd=set();req={};reads=[];first={}
 for i,a in enumerate(w):
  c=(a=='L')^(p in odd)
  if p in req and req[p]!=c:return dict(feasible=False,i=i,q=p,first=first[p])
  req[p]=c;first.setdefault(p,i);reads.append((p,h,a));odd.symmetric_difference_update({p});h=(h+(1 if a=='R'else-1))%4;p+=dirs[h]
 return dict(feasible=True,p=p,h=h,odd=odd,req=req,reads=reads)
def center(p,h):return 2*p+(-1-1j)*(-1j)**h
def xy(q):return(int(q.real),int(q.imag))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def minus(a,b):return(a[0]-b[0],a[1]-b[1])
def within(a,b,q):return cross(minus(q,a),minus(b,a))==0 and all(min(a[i],b[i])<=q[i]<=max(a[i],b[i])for i in(0,1))
def meet(a,b,c,d):
 u=minus(b,a);v=minus(d,c);r=minus(c,a);den=cross(u,v)
 if den:
  s=F(cross(r,v),den);t=F(cross(r,u),den)
  if 0<=s<=1 and 0<=t<=1:return(s,t,tuple(F(a[i])+s*u[i]for i in(0,1)))
  return None
 inter={q for q in(a,b,c,d)if within(a,b,q)and within(c,d,q)}
 return tuple(sorted(inter))if inter else None
def inventory(a,b):
 lo=[-((1-min(a[i],b[i]))//2)for i in(0,1)];hi=[(max(a[i],b[i])+1)//2 for i in(0,1)];out={}
 for x in range(lo[0],hi[0]+1):
  for y in range(lo[1],hi[1]+1):
   z=1 if(x+y)%2==0 else-1;c=(2*x-1,2*y-z);d=(2*x+1,2*y+z);m=meet(a,b,c,d)
   if m is not None:out[x,y]=m
 return out
geometries=[]
for ref in data['barriers']:
 a=ref['name'];raw=walk(W[a]);full=walk(W[a]+M);assert raw['feasible']and full['feasible'];ctx={xy(q)for q in full['req']};end=xy(center(raw['p'],raw['h']));whole=inventory((-1,-1),end)
 assert set(whole)=={tuple(x['cell'])for x in ref['whole_chord']['contacts']}
 missing=set(whole)-ctx;assert missing=={tuple(x['cell'])for x in ref['whole_chord']['missing']}
 pts=[(-1,-1),(-7,-3)]+([]if a=='F'else[end]);pcs=[]
 for b,c,rp in zip(pts,pts[1:],ref['pieces']):
  hit=inventory(b,c);assert set(hit)<=ctx;assert set(hit)=={tuple(x['cell'])for x in rp['contacts']};pcs.append(len(hit))
 geometries.append(dict(name=a,whole=len(whole),missing=sorted(missing),pieces=pcs))
for ref in data['physical_straight_chord_controls']:
 a=ref['name'];q=complex(*ref['persistent_cell']);full=walk(W[a]+M);seed={p for p,c in full['req'].items()if c}|{q};assert q not in full['req'];assert sorted(map(xy,seed))==list(map(tuple,ref['seed']))
 board=set(seed);p=0j;h=0
 for i,ch in enumerate(W[a]+M):
  if i==len(W[a]):assert sorted(map(xy,board))==list(map(tuple,ref['raw_exit_black']))
  assert(p in board)==(ch=='L');assert p!=q;board.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
 assert q in board
assert inventory((-1,-1),(-5,-9))[-1,-2]==(F(1,3),F(1,3),(F(-7,3),F(-11,3)))
assert inventory((-1,-1),(-7,-7))[-2,-2]==((-5,-5),(-3,-3))
# All direction coefficients are derived from the actual word endpoint centers.
assert W['Q'][:56]==W['B'][:56]==W['F'];tails={'TQ':W['Q'][56:],'TB':W['B'][56:]};assert tails=={'TQ':'LRRLRRRR','TB':'LRLLLLRRRRLRRLRRRR'}
words={a:W[a]for a in'DCVUF'}|tails
vec={'D':2+2j,'C':2+2j,'V':2+6j,'U':8j,'F':-6-2j,'TQ':4j,'TB':-2+6j}
alpha={'D':(1,0),'C':(1,0),'V':(2,-1),'U':(2,0),'F':(4,1),'TQ':(2,0),'TB':(2,1)};omega={'D':0,'C':2,'V':0,'U':0,'F':4,'TQ':0,'TB':0}
for a,w in words.items():
 tr=walk(w);assert tr['feasible'];assert center(tr['p'],tr['h'])-(-1-1j)==vec[a];assert omega[a]%8==(-2*tr['h'])%8
expand={a:[a]for a in'DCVUF'}|{'Q':['F','TQ'],'B':['F','TB']};angles=[]
for a,aa in expand.items():
 for b,bb in expand.items():
  x=aa[-1];y=bb[0];c=omega[x]+alpha[y][0]-alpha[x][0];d=alpha[y][1]-alpha[x][1];wrap=int(x=='C'and y=='F');c-=8*wrap
  if x==y=='F':assert(c,d)==(4,0)
  else:assert min(c,c+d)>=-4 and max(c,c+d)<=4 and not(d==0 and abs(c)==4)
  angles.append((a,b,c,d,wrap))
assert set(angles)=={(r['before_macro'],r['after_macro'],r['turn_pi_over_4_coefficient'],r['turn_beta_coefficient'],r['subtract_full_turn'])for r in data['boundary_turn_rows']}
for t in tails:
 c=4+alpha[t][0]-alpha['F'][0];d=alpha[t][1]-alpha['F'][1];assert -4<min(c,c+d)and max(c,c+d)<4
cf=walk(W['C']+W['F']+M);ff=walk(W['F']*2);assert cf['feasible'];seed={q for q,c in cf['req'].items()if c};assert len(seed)==19
assert not ff['feasible']and(ff['i'],ff['q'],ff['first'])==(107,-1j,3)
board=set(seed);p=0j;h=0
for ch in W['C']+W['F']+M:assert(p in board)==(ch=='L');board.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
for f,h in data['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
note=D/'foreign_kinked_barrier_and_turn.md';assert hashlib.sha256(note.read_bytes()).hexdigest()=='3117f55712758edf66c9f658078052ebdaa21f69457dcc80965e9fbd2c62fb78'
out=dict(status='PASS literal kinked survivor-edge barrier and exact seven-word tangent lift',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),geometry=geometries,boundary_pairs=len(angles),CF_mass=19,FF_conflict={'read':107,'cell':[0,-1],'first_read':3},analytic='A surviving original residual ID avoids the entire foreign before-context: core/white/input exhaust it. Every edge meeting the actual F-prefix and tail chords lies in that full context, without an internal marker assumption. Formal C-to-F turns wrap by -2pi, FF-prefix joins are physically infeasible, and the remaining exact turns telescope to pi/2*(C-lastC+2*(foreign-lastF)-4*CF)+alpha_last-alpha_first.',scope='Local survivor-edge proxy only. No global injectivity, Jordan hypothesis, positive foreign C clock, lifetime extension, ancestry permanence or global capture.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(geometries)
