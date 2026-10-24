"""ALL-r literal certificate by a finite arrangement of delta/epsilon intervals.
No empirical r cutoff: atom membership is constant on each integer rectangle.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry']
D=((0,1),(1,0),(0,-1),(-1,0));K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def read(word,p=(0,0),h=0):
 rows=[]
 for t,ch in enumerate(word):
  rows.append((t,p,ch));h=(h+(-1 if ch=='L'else 1))%4;dx,dy=D[h];p=p[0]+dx,p[1]+dy
 return rows,(p,h)
assert G[4]['endpoint']==[1,3,0]and G[6]['endpoint']==[0,4,2]
# p_n=(1,2)+n*(-3,1); q_n=p_n+(-4,0). Incoming indices run r..-1.
A=defaultdict(list)
def install(kind,rows):
 for t,(x,y),ch in rows:
  dx,dy=x-1,y-2;ell=dx+3*dy
  A[ell].append(dict(kind=kind,dy=dy,t=t,turn=ch))
install('DC',read(G[1]['word'])[0])
install('O',read(G[4]['word'],(1,2),3)[0])
install('F',read(G[6]['word'],(1,2),3)[0])
install('I',read(G[4]['word'],(-3,2),1)[0])
install('M',read(G[4]['marker'],(3,0),1)[0])
def partition(C):
 z=sorted(C);ans=[(None,z[0]-1)]
 for j,c in enumerate(z):
  ans.append((c,c))
  if j+1<len(z)and c+1<=z[j+1]-1:ans.append((c+1,z[j+1]-1))
 ans.append((z[-1]+1,None));return ans
def sample(B):a,b=B;return a if a is not None else b
def contains(B,x):a,b=B;return(a is None or a<=x)and(b is None or x<=b)
def feasible(B,C):return B[1]is None or C[0]is None or B[1]>=C[0]
def active(z,delta,eps):
 k,y=z['kind'],z['dy']
 return delta==y if k in('DC','M')else delta>=y and eps<=y-1 if k=='O'else eps==y if k=='F'else delta>=y-1 and eps<=y
order={'DC':0,'O':1,'F':2,'I':3,'M':4}
def key(z):return(order[z['kind']],-z['dy']if z['kind']=='O'else z['dy']if z['kind']=='I'else 0,z['t'])
regions=[];black=[];checked=0
for ell,atoms in sorted(A.items()):
 dc={z['dy']for z in atoms if z['kind']in('DC','M','O')}|{z['dy']-1 for z in atoms if z['kind']=='I'}
 ec={z['dy']-1 for z in atoms if z['kind']=='O'}|{z['dy']for z in atoms if z['kind']in('I','F')}
 # An unused axis can be split anywhere, without changing completeness.
 X=partition(dc or{0});Y=partition(ec or{0})
 for B in X:
  for C in Y:
   if not feasible(B,C):continue
   delta,eps=sample(B),sample(C)
   visit=sorted([z for z in atoms if active(z,delta,eps)],key=key)
   turns=''.join(z['turn']for z in visit)
   assert all(x!=y for x,y in zip(turns,turns[1:])),(ell,B,C,turns,visit)
   row=dict(ell=ell,delta=list(B),epsilon=list(C),turns=turns)
   regions.append(row);checked+=len(visit)
   if turns.startswith('L'):black.append(row)
# Verify canonical entry core for every r>=0 using the same complete partition.
for x,y in K:
 ell=x+3*y-7;delta=y-2
 applicable=[z for z in regions if z['ell']==ell and contains(z['delta'],delta)and(z['epsilon'][0]is None or z['epsilon'][0]<=delta)]
 assert applicable and all(z['turns'].startswith('L')for z in applicable),(x,y,applicable)
def mass(r):
 n=0
 for z in black:
  a,b=z['delta'];c,d=z['epsilon']
  lows=[v for v in(a,None if c is None else c+r)if v is not None]
  ups=[v for v in(b,None if d is None else d+r)if v is not None]
  assert lows and ups # finite word gives finite mass on each fixed-r diagonal
  n+=max(0,min(ups)-max(lows)+1)
 return n
# All min/max branch changes and count-zero crossings are at differences of
# finite interval endpoints. Beyond their largest nonnegative value, every
# summand is affine. Testing both endpoints of that final affine ray is exact.
breaks={0}
for z in black:
 for x in z['delta']:
  for y in z['epsilon']:
   if x is not None and y is not None and x-y>=0:breaks.add(x-y)
B=max(breaks);masschecks=[mass(r)for r in range(B+3)]
assert masschecks==[3*r+9 for r in range(B+3)]
# Small direct board+ledger controls independently sanity-check the parameter
# encoding, but are NOT the proof of the universal parameter claim.
def replay(r):
 ids=[1]+[4]*r+[6]+[4]*(r+2);word=''.join(G[a]['word']for a in ids)+G[4]['marker'];reads,end=read(word);need={};par={}
 for t,p,ch in reads:
  b=(ch=='L')^par.get(p,False);assert p not in need or need[p]==b
  need[p]=b;par[p]=not par.get(p,False)
 seed={p for p,b in need.items()if b};assert len(seed)==3*r+9 and K<=seed
 Board=set(seed);T={p:('entry',None)for p in seed-K};p=(0,0);h=0;clock=0;raw=0;inputs=[]
 for j,a in enumerate(ids):
  core={(p[0]+rot(k,h)[0],p[1]+rot(k,h)[1])for k in K};assert core.isdisjoint(T)and Board==core|set(T)
  I=[(p[0]+rot(k,h)[0],p[1]+rot(k,h)[1])for k in G[a]['inputs']]
  if j==len(ids)-1:assert [T[q][0]for q in I]==[0,0]and[clock-T[q][1]for q in I]==[3,3]and p==(0,1)and h==1
  inputs.append([j,a,[*p,h],clock,[T[q]for q in I]])
  for q in I:del T[q]
  for k in G[a]['outputs']:
   q=p[0]+rot(k,h)[0],p[1]+rot(k,h)[1];assert q not in T;T[q]=(j,clock)
  for ch in G[a]['word']:
   assert(ch=='L')==(p in Board)
   if p in Board:Board.remove(p)
   else:Board.add(p)
   h=(h+(-1 if ch=='L'else 1))%4;dx,dy=D[h];p=p[0]+dx,p[1]+dy;raw+=1
  clock+=G[a]['name'].count('C')
 assert raw==109+36*r and clock==3 and len(Board)==11*r+30 and(p,h)==((3,0),1)
 return dict(r=r,mass=len(seed),seed=sorted(seed),packet_inputs=inputs,raw_reads=raw,final_mass=len(Board))
controls=[replay(r)for r in(0,1,2,5)]
J=dict(status='AUTHOR_ALL_R_FINITE_RECTANGLE_LITERAL_FAMILY_PASS',family='DC V^r VCC V^(r+2), integer r>=0',scope='Actual supported finite words; not a renewal, infinite trajectory, or unfunded record witness. Seed mass grows with r.',coordinates='p_n=(1,2)+n*(-3,1), q_n=p_n+(-4,0); cell=(1+ell-3delta,2+delta), epsilon=delta-r',atom_conditions={'DC/M':'delta=dy','O':'delta>=dy and epsilon<=dy-1','F':'epsilon=dy','I':'delta>=dy-1 and epsilon<=dy'},ordering='DC; O sorted by decreasing dy then t; F by t; I increasing dy then t; M. Exact because outgoing n increases and incoming n decreases.',feasibility='delta>=epsilon (r>=0)',atom_inventory={str(k):v for k,v in A.items()},rectangle_count=len(regions),visit_obligations=checked,regions=regions,black_regions=black,mass_piecewise_certificate=dict(breakpoints=sorted(breaks),last_breakpoint=B,values=masschecks,formula='3r+9',reason='Each summand max(0,min(b,r+d)-max(a,r+c)+1); all branch changes and zero crossings are finite endpoint differences. Tail affine, checked at B+1 and B+2.'),formulae=dict(initial_mass='3r+9',raw_duration='36r+109',duration_with_final_marker='36r+120',C_count=3,final_mass_after_raw='11r+30',final_raw_pose=[3,0,1],protected_DC_outputs_consumed_by_goal=[[3,1],[2,0]],goal_C_ages=[3,3]),direct_controls=controls,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,Path(__file__).resolve()]})
(R/'chronology_dcuv/dc_V_return_family.json').write_text(json.dumps(J,indent=2)+'\n')
print(dict(rectangles=len(regions),visits=checked,black_rectangles=len(black),last_mass_breakpoint=B,mass_formula='3r+9',direct_controls=[(x['r'],x['mass'])for x in controls]))
