"""Rational protected-bridge geometry for exact four-C U-cycle renewal.
The universal Jordan-turn step is analytic; this checker binds every literal
atomic chord, source prefix, bridge edge, and endpoint used by that proof.
"""
from pathlib import Path
from fractions import Fraction
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];C=G[1]['word'][len(G[0]['word']):];assert C=='LLLLRLRRRRLRRRR'
K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def cross(p,q):return p[0]*q[1]-p[1]*q[0]
def on(p,A,B):return cross(sub(p,A),sub(B,A))==0 and sum((p[i]-A[i])*(p[i]-B[i])for i in range(2))<=0
def contact(A,B,C,D):
 u=sub(B,A);v=sub(D,C);r=sub(C,A);det=cross(u,v)
 if det:
  s=Fraction(cross(r,v),det);t=Fraction(cross(r,u),det)
  return [[str(Fraction(A[i])+s*u[i])for i in range(2)]]if 0<=s<=1 and 0<=t<=1 else[]
 return [list(p)for p in sorted({A,B,C,D})if on(p,A,B)and on(p,C,D)]
def edge(p):
 x,y=p;return((2*x-1,2*y-1),(2*x+1,2*y+1))if(x+y)%2==0 else((2*x-1,2*y+1),(2*x+1,2*y-1))
def center(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def run(word,p=(0,0),h=0):
 for ch in word:
  h=(h+(-1 if ch=='L'else 1))%4;p=add(p,rot((0,1),h))
 return p,h
atom_rows=[]
for name,word,expected,Cn in [('D',G[0]['word'],(2,2),0),('V',G[4]['word'],(2,6),0),('U',G[7]['word'],(0,8),0),('C',C,(2,2),1)]:
 for h in range(4):
  p2,h2=run(word,h=h);v=sub(center(p2,h2),center((0,0),h));assert v==rot(expected,h);assert h2==(h-Cn)%4
  atom_rows.append(dict(atom=name,entry_heading=h,center_displacement_doubled=v,C_increment=Cn,exit_head=[*p2,h2]))
P=(-1,7);M=(5,1);bridge=[M,(3,3),(1,1),(-1,3),P]
for A,B,cell in zip(bridge[:3],bridge[1:4],[(2,1),(1,1),(0,1)]):assert set(edge(cell))=={A,B}
assert bridge[-2][0]==bridge[-1][0]==-1 and -1<bridge[-2][1]<bridge[-1][1]==7
# Bridge has no self-contact except permitted adjacent common endpoints.
for i in range(4):
 for j in range(i+1,4):
  hit=contact(bridge[i],bridge[i+1],bridge[j],bridge[j+1])
  if j==i+1:assert len(hit)==1
  else:assert not hit
# Its exact principal turns, measured in units pi/4, include incoming N
# from the final half-U at M and outgoing N along the source U at P.
directions=[2,3,5,3,2];turns=[(b-a+4)%8-4 for a,b in zip(directions,directions[1:])];assert turns==[1,2,-2,-1]and sum(turns)==0
# Right-breaker half-base meets bridge only at its last point M.
B0=center((3,-1),0);B1=center((3,3),0);assert B0==(5,-3)and B1==(5,5)
for A,B in zip(bridge,bridge[1:]):
 hit=contact(B0,M,A,B);assert hit==[['5','1']]if A==M else not hit
source_rows=[]
for a in[7,8,9]:
 assert G[a]['word']==G[7]['word']+C*G[a]['name'].count('C')
 assert {(1,0),(1,1),(2,0),(2,1),(0,1)}<=set(map(tuple,G[a]['outputs']))
 p,h=run(G[7]['word']);assert center(p,h)==P
 cs=[]
 for k in range(G[a]['name'].count('C')):
  A=center(p,h);p,h=run(C,p,h);B=center(p,h)
  hits=[]
  for j,(u,v)in enumerate(zip(bridge,bridge[1:])):
   hit=contact(A,B,u,v)
   if hit:hits.append(dict(bridge_edge=j,intersection=hit))
  if k==0:assert hits==[dict(bridge_edge=3,intersection=[['-1','7']])]
  else:assert not hits
  cs.append(dict(index=k,chord=[A,B],bridge_contacts=hits))
 assert (p,h)==(tuple(G[a]['endpoint'][:2]),G[a]['endpoint'][2])
 source_rows.append(dict(source=a,C_tail_chords=cs,full_exit=[*p,h]))
# The analytic turn lift only uses alpha_D=alpha_C=pi/4,
# pi/4<alpha_V=atan(3)<pi/2, alpha_U=pi/2.
# For a non-C predecessor the increment lies[-pi/4,pi/4];
# for C, whose alpha is pi/4, it lies[pi/2,3pi/4].
# Hence every telescoping lift is the actual principal turn, never a
# hidden extra winding. Source/target U alpha agree.
D=[GP,W/'causal_cycle_renewal_20261023_1841/manifest.json',W/'current_residual_barrier_frozen_20261023_1822/manifest.json',W/'U_entry_simplicity_frozen_20261023_1616/manifest.json',Path(__file__).resolve()]
R=dict(status='AUTHOR_EXACT_FOUR_C_RENEWAL_PENDING_INDEPENDENT_AUDIT',scope='Actual complete recurrent-eight U-cycle creator/first-breaker relation. Source-start-inclusive, consumer-entry-exclusive C gap equals4. Fixed protected Jordan bridge and exact principal-turn lift; no guessed path bound. The three breaker uppers predate the creator by at least one full C clock when produced. If creator is factor-first, they are distinct entry identities and the first breaker merges exactly four reset incidence components. No later-chain budget, U1 closure or confinement.',atomic_chords=atom_rows,bridge_doubled=bridge,bridge_cells=[(2,1),(1,1),(0,1)],bridge_turns_in_pi_over_4=turns,right_breaker_entry_doubled=B0,right_breaker_exit_doubled=B1,right_breaker_midpoint_doubled=M,source_C_tail_bridge_checks=source_rows,turn_lift=dict(atom_alphas=['pi/4','atan(3)','pi/2','pi/4'],non_C_predecessor_turn_bounds=['-pi/4','pi/4'],C_predecessor_turn_bounds=['pi/2','3pi/4'],future_arc_plus_bridge_total_turn='n*pi/2',Jordan_turn='plus_or_minus_2*pi',nonnegative_C_conclusion=4),support_clock_corollary=dict(full_source_start_C_gap=4,produced_upper_minimum_age=5,upper_birth_at_most_creator_start_minus=1,initial_upper_birth='minus_infinity',factor_first_creator_upper_ids='all_three_entry_and_distinct_singletons',factor_first_breaker_components='exactly4'),dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U_renewal_exact_clock.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(dict(bridge=bridge,bridge_turns=turns,source_tail_rows=source_rows,conclusion='Cgap4;uppersstrictlyolder'),indent=2))
