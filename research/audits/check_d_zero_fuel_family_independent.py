"""No-import literal proof ingredients for UCCV D^n, n>=1."""
import hashlib,json,pathlib
ROOT=pathlib.Path('/workspace/shared/langton')
D='LLLLRLRRRR';C='LLLLRLRRRRLRRRR';V='LLLLRLRRRRLRRLRRRR';U='LLLLRLRRRRLRLLLLRRRRLRRLRRRR';P=U+C+C+V

def walk(word,start=(0,0,0)):
 x,y,h=start;out=[]
 for t,c in enumerate(word):
  out.append(((x,y),c,t));h=(h+(1 if c=='R' else -1))%4
  dx,dy=((0,1),(1,0),(0,-1),(-1,0))[h];x+=dx;y+=dy
 return out,(x,y,h)
def feasible(word):
 trace,pose=walk(word);last={};seed=set();fuel=[]
 for p,c,t in trace:
  assert p not in last or last[p][0]!=c,(p,c,t,last.get(p))
  if p not in last and c=='L':seed.add(p);fuel.append(t)
  last[p]=(c,t)
 return seed,pose,fuel
pre,entry=walk(P);one,end=walk(D,entry)
assert len(P)==76 and entry==(-2,2,2) and end==(-3,1,2)
# The displacement is (-1,-1). Equality of two copy reads has a unique
# nonnegative index gap iff both coordinate differences agree.
def copy_index(p,q):
 dx=p[0]-q[0];dy=p[1]-q[1]
 return -dx if dx==dy and dx<=0 else None
seps={copy_index(p,q) for p,_,_ in one for q,_,_ in one}-{None}
hits={copy_index(p,q) for p,_,_ in pre for q,_,_ in one}-{None}
assert max(seps)==2 and max(hits)==1
feasible(D*4);feasible(P+D*6)
seed0,_,_=feasible(P);assert len(seed0)==11
for n in range(1,41):
 seed,pose,fuel=feasible(P+D*n)
 expected=seed0|{(-1-j,2-j) for j in range(1,n)}
 assert seed==expected and len(seed)==n+10
 assert pose==(-2-n,2-n,2)
 assert [t for t in fuel if t>=76]==[76+10*j+1 for j in range(1,n)]
# All predecessors of a read in copy j are confined to j,j-1,j-2.
# For j>=2 prefix reads are absent, so the j=2 phase result is stationary.
source=ROOT/'word_stabilization/d_zero_fuel_family_certificate.json'
j=json.loads(source.read_text());assert j['D']==D and j['P']==P
assert {tuple(p) for p in j['shortest_seed']}==seed0
assert j['max_D_copy_overlap']==2 and j['max_prefix_D_copy_overlap']==1
out={'status':'literal finite ingredients and all-parameter predecessor cover verified','copy_separations':sorted(seps),'prefix_copy_indices':sorted(hits),'prefix_entry_mass':len(seed0),'seed_formula':'seed(UCCV) union {(-1-j,2-j):1<=j<n}','mass_formula':'n+10 for n>=1','pose_formula':'(-2-n,2-n,S)','literal_controls':40,'certificate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'scope':'all finite powers, not a common finite seed for infinite D'}
(ROOT/'audits/check_d_zero_fuel_family_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
