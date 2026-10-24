"""Author-side exact arithmetic control; independent audit remains separate.
Checks the finite fundamental C-gap cases. Gaps larger by4 add16 to margin.
"""
from pathlib import Path
from fractions import Fraction
import json,hashlib,itertools
root=Path(__file__).resolve().parent
Gpath=root/'chronology_dcuv/literal_residual_geometry.json';Apath=root/'chronology_dcuv/counted_input_age_rules_complete.json'
G=json.loads(Gpath.read_text())['geometry'];A={(a,x,y):v for a,x,y,v in json.loads(Apath.read_text())}
chosen={0:(0,1),1:(0,1),4:(1,2),5:(1,2),6:(0,3),7:(0,3),8:(0,3),9:(0,3)};phi=(0,5,6,3)
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
checks=0;tight=[];zero=[];edges=[]
for parenth,childh in itertools.product(range(4),repeat=2):
 for b,q in chosen.items():
  age=A[b,*q];n=age+(parenth-childh-age)%4
  assert n>=age and n%4==(parenth-childh)%4
  assert G[b]['endpoint'][2]%4==(-G[b]['name'].count('C'))%4
  for r0 in G[b]['outputs']:
   r=tuple(r0);delta=rot((r[0]-q[0],r[1]-q[1]),childh)
   for frame in range(4):
    dy=rot(delta,frame)[1];margin=4*(n-dy)+phi[(parenth+frame)%4]-phi[(childh+frame)%4]-3*(b!=9)
    assert margin>=0,(parenth,childh,b,r,n,dy,margin);checks+=1
   dy=delta[1];margin=4*(n-dy)+phi[parenth]-phi[childh]-3*(b!=9)
   if margin==0:tight.append([parenth,childh,b,list(r),n,dy])
   if n==dy:zero.append([parenth,childh,b,list(r),n,dy])
   edges.append((parenth,childh,int(b!=9),n-dy,b,r))
# Independently enumerate all simple cycles of the four heading states. This
# proves the coefficient4/3 is optimal for THIS age+heading+slot relaxation only.
minimum={}
for p,h,e,s,b,r in edges:
 key=p,h,e
 if key not in minimum or s<minimum[key][0]:minimum[key]=(s,b,r)
best=Fraction(0);cycle=None
for nstates in range(1,5):
 for states in itertools.permutations(range(4),nstates):
  if states[0]!=min(states):continue
  for flags in itertools.product(range(2),repeat=nstates):
   cycle_edges=list(zip(states,states[1:]+states[:1],flags));slack=sum(minimum[e][0]for e in cycle_edges);count=sum(flags)
   assert slack or not count
   if slack and Fraction(count,slack)>best:best=Fraction(count,slack);cycle=[[list(e),list(minimum[e][:2]),list(minimum[e][2])]for e in cycle_edges]
assert best==Fraction(4,3)
# Zero slack graph exact form. Its only recurrent component is UCC0->0.
assert set((p,h,b)for p,h,b,r,n,dy in zero)=={(2,3,1),(3,0,5),(0,0,9)}
R={'status':'AUTHOR_EXACT_ARITHMETIC_PASS','scope':'Auxiliary residual genealogy, JO ages plus exact packet heading and output coordinates. No physical realizability of abstract equality cycles is claimed.','inputs':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()for p in [Gpath,Apath]},'fundamental_output_facet_checks':checks,'potential_plus_y':phi,'inequality':'3*non_UCC <= 4*(C_birth_gap - dy) + Phi(parent_heading)-Phi(child_heading)','zero_spatial_slack_edges':zero,'potential_equality_edges':tight,'optimal_relaxed_non_UCC_to_slack_ratio':str(best),'relaxed_optimality_cycle':cycle}
(root/'chronology_dcuv/genealogy_coordinate_slack.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(R,indent=2))
