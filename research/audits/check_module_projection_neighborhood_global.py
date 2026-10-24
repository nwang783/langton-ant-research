"""Exact finite geometry/group check for the autonomous no-ABA interface.
No trajectory truncation: Q_R/Q_L are all-parameter packet overapproximations.
The return grammar/forced completion are separate analytic prerequisites.
"""
import json
from pathlib import Path
D=[(0,1),(1,0),(0,-1),(-1,0)]
def pose(w):
 x=y=h=0
 for a in w:
  h=(h+(1 if a=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
 return x,y,h

def rot(p,h):
 x,y=p
 for _ in range(h%4):x,y=y,-x
 return x,y

def reduce(w):
 st=[]
 for a in w:
  if st and st[-1][0]==a:
   if st[-1][1]==3:st.pop()
   else:st[-1]=(a,st[-1][1]+1)
  else:st.append((a,1))
 return tuple(st)

def inverse(w):return ''.join(a*3 for a in reversed(w))
def same_coset(a,b):
 # For this finite table the exact difference has at most 24 letters.
 # Nonzero powers of RL^3 have reduced syllable length 2|k|, so |k|<=24
 # is exhaustive, not a heuristic search in H.
 d=reduce(inverse(a)+b)
 for k in range(-24,25):
  if d==reduce(('RLLL'*k) if k>=0 else ('LRRR'*(-k))):return True
 return False

def packet_contains(root,a,p):
 x,y,h=pose(root);u,v=rot((p[0]-x,p[1]-y),-h)
 if a=='L':u=-u
 return (u>=0 and v in (-1,0)) or (u in (0,1) and v>=0)

target_words=['','RRR','R','RR','L','LL']
targets={pose(w)[:2]:w for w in target_words}
assert len(targets)==6
faces=[];grandchildren=[]
for a,b in [('R','L'),('L','R')]:
 faces.append(('',a))
 for i in (1,2):
  child=a*i;faces.append((child,b))
  for j in (1,2):grandchildren.append((child+b*j,a))

face_checks=0
for root,a in faces:
 for j in range(4):
  w=root+a*j;q=pose(w)[:2]
  if q in targets:
   assert same_coset(targets[q],w),(root,a,j,q,w,targets[q]);face_checks+=1

rows=[]
for root,a in grandchildren:
 p=pose(root+a*3)[:2];hits=[]
 for q,w in targets.items():
  if packet_contains(root,a,q):
   assert q==p,(root,a,q,p)
   assert same_coset(w,root+a*3),(root,a,q,w)
   hits.append({'physical_cell':q,'boundary_group_word':root+a*3,'tracked_representative':w})
 rows.append({'root_word':root,'sign':a,'pose':pose(root),'possible_tracked_hits':hits})

rebases=[]
for a in ('R','L'):
 for k in range(1,5):
  # At the first turn change after a^k, the original group state is a^-k.
  w=a*((4-k)%4);q=pose(w)[:2]
  assert q in targets and same_coset(w,targets[q])
  # No revisit of the initial physical cell during the preceding same-turn
  # prefix except the fourth-turn endpoint, which is the identical state.
  for j in range(1,k):assert pose(a*j)[:2]!=(0,0)
  rebases.append({'first_letter':a,'same_turn_count':k,'initial_cell_in_rebased_frame':q,'tracked_representative':targets[q]})

out={'status':'PASS','explicit_faces':len(faces),'explicit_target_representative_checks':face_checks,'grandchildren':rows,'rebasing_cases':rebases,'scope':'Exact finite geometry and free-product coset table. Depends analytically on module trapping, return grammar, packet support bounds, and interval completion.'}
print(json.dumps(out,indent=2));Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
