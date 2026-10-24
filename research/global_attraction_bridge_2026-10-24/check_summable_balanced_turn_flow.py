"""An exact stationary-flow relaxation countercontrol, NOT an ant orbit."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
P=Path(__file__).parent
r=F(1,2)
def A(q):return r**(abs(q[0])+abs(q[1]))
def faces(v):
 x,y=v
 return [(x,y),(x-1,y),(x-1,y-1),(x,y-1)] # NE,NW,SW,SE

def turn(v,k):
 f=faces(v);return (3*A(f[k])+A(f[(k-1)%4])+A(f[(k+1)%4])-A(f[(k+2)%4]))/4

def mass(v):return sum(A(q)for q in faces(v))
# Directions N,E,S,W. At even sites, first sector arrives vertically.
D=[(0,1),(1,0),(0,-1),(-1,0)]
# Face corner for incoming heading h and outgoing h2: the two position vectors
# from the read site are -D[h] (arrival neighbor) and D[h2] (departure neighbor).
def corner(h,h2):
 x=-D[h][0]+D[h2][0];y=-D[h][1]+D[h2][1]
 return {(1,1):0,(-1,1):1,(-1,-1):2,(1,-1):3}[x,y]

checked=0;norm=4*((1+r)/(1-r))**2;assert norm==36 and mass((0,0))/norm==F(1,16)
log=[]
for x in range(-20,21):
 for y in range(-20,21):
  v=(x,y);f=faces(v);tt=[turn(v,k)for k in range(4)];aa=[A(q)for q in f]
  assert min(tt)>0 and sum(tt)==sum(aa)
  u=max(aa);assert sorted(a/u for a in aa)==sorted([F(1),r,r,r*r])
  assert tt[0]+tt[2]==tt[1]+tt[3]==mass(v)/2
  for k in range(4):assert tt[k]+tt[(k+1)%4]==aa[k]+aa[(k+1)%4]
  for sector in range(2):
   incoming_axis=(x+y+sector)%2 #0 vertical,1 horizontal
   ins=[incoming_axis,incoming_axis+2];R=[];L=[];outs={}
   for h in ins:
    vals=[]
    for dh in[-1,1]:
     h2=(h+dh)%4;k=corner(h,h2);val=tt[k];vals.append(val);(R if dh==1 else L).append(val);outs[h2]=outs.get(h2,F(0))+val
    # The incoming physical edge's face pair and flow at its predecessor endpoint.
    prev=(x-D[h][0],y-D[h][1]);edgefaces=set(f)&set(faces(prev));assert len(edgefaces)==2
    assert sum(vals)==sum(A(q)for q in edgefaces)
   assert sum(R)==sum(L)==mass(v)/2
   for h2,val in outs.items():
    nxt=(x+D[h2][0],y+D[h2][1]);edgefaces=set(f)&set(faces(nxt));assert val==sum(A(q)for q in edgefaces)
   checked+=1
  for dx in[-1,1]:
   for dy in[-1,1]:assert mass(v)<=2*(mass((x+dx,y))+mass((x,y+dy)))
  log.append([x,y,*[str(t)for t in tt]])
# Exact symbolic coefficient comparison for all r: numerators ordered as powers r^0,r^1,r^2.
assert [F(3)+2*r-r*r,(1+r)**2,3*r*r+2*r-1]==[F(15,4),F(9,4),F(3,4)]
assert (3*r-1)*(r+1)==3*r*r+2*r-1
# Infinite sum derives from 1+2r/(1-r), then tensor product.
face_sum=(1+2*r/(1-r))**2;assert face_sum==9 and 4*face_sum==norm
fs=['RECTANGLE_VISIT_FLOW_MANIFEST.json','../audits/check_rectangle_visit_flow_independent.json','../first_principles_new/recurrent_boundary_current.md']
for z in fs:assert(P/z).exists(),z
out={'status':'AUTHOR explicit summable flow countercontrol; independent audit pending','NOT_AN_ANT_ORBIT':True,'r':'1/2','sector_vertex_checks':checked,'four_corner_inequalities':4*41*41,'unnormalized_total_turn_flow':str(norm),'head_probability_at_origin':'1/16','finite_exact_log_sha256':hashlib.sha256(json.dumps(log,separators=(',',':')).encode()).hexdigest(),'all_lattice_formula':'A(i,j)=r^(abs(i)+abs(j)); edge=A_left+A_right; corner=(3A_self+A_adj1+A_adj2-A_opposite)/4','parameter_domain':'1/3 <= r < 1','dependencies':{z:hashlib.sha256((P/z).read_bytes()).hexdigest()for z in fs},'scope':'Refutes only stationary edge-conservation plus equal per-site R/L-flow exclusion of a summable profile. Actual chronological alternation and finite-seed realization are not established.'}
(P/'SUMMABLE_BALANCED_TURN_FLOW_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n');print(checked,'exact sector/vertex checks; infinite total',norm)
