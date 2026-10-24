from pathlib import Path
import hashlib,json
from fractions import Fraction as F
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
D=ROOT/'core_periodicity_new'
def freeze(name):
 b=D/name;m=json.loads((b/'manifest.json').read_text())
 for row in m['files']:assert hashlib.sha256((b/row['frozen']).read_bytes()).hexdigest()==row['sha256']
 return b,hashlib.sha256((b/'manifest.json').read_bytes()).hexdigest()
b,controlhash=freeze('center_crossing_control_frozen_20261023_1407');j=json.loads((b/'02_center_crossing_beta_zero_control.json').read_text())
seq=[1,1,1,0,4];assert j['word']==seq
seed={complex(x,y)for x,y in j['seed']};assert len(seed)==10
word=''.join(raws[a]for a in seq);assert len(word)==103
assert seed=={z for z,c in walk(word+mark)[2].items()if c}
# Actual full-state, current identity, and undirected incidence components.
parent={};defids={};nextid=0
for z in seed-K:parent[nextid]=nextid;defids[z]=(nextid,None);nextid+=1
def root(a):
 while parent[a]!=a:a=parent[a]
 return a
board=set(seed);p=0j;h=0;clock=0;rows=[];centers=[];atomic=[]
for ix,a in enumerate(seq):
 assert board=={p+rotation(z,h)for z in K}|set(defids)
 end,dh,need,I,O=G[a];ins={p+rotation(z,h):z for z in I};assert set(ins)<=set(defids)
 comps={root(defids[z][0])for z in ins};delta=len(ins)-len(comps);assert delta==0
 origin=[(xy(z),defids[z][1])for z in ins]
 if ix==4:assert set(origin)=={((2,0),0),((1,-1),None)}and len(comps)==2
 pid=nextid;nextid+=1;parent[pid]=pid
 for rt in comps:parent[rt]=pid
 for z in ins:del defids[z]
 for z in O:
  q=p+rotation(z,h);assert q not in defids;oid=nextid;nextid+=1;parent[oid]=pid;defids[q]=(oid,ix)
 # Atomic center chords reconstructed from literal word, not author center data.
 bas=a-counts[a];atoms=[(bas,raws[bas])]+[(2,raws[1][len(raws[0]):])]*counts[a]
 pp=p;hh=h
 for typ,ww in atoms:
  c0=2*pp+rotation(-1-1j,hh);ee,dd,*_=walk(ww);pp+=rotation(ee,hh);hh=(hh+dd)%4;c1=2*pp+rotation(-1-1j,hh)
  centers.append((c0,c1));atomic.append((typ,clock))
  if typ==2:clock+=1
 bb=set(board);q=p;qh=h
 for ti,c in enumerate(raws[a]+mark):
  assert(q in bb)==(c=='L');bb.symmetric_difference_update({q});qh=(qh+(1 if c=='R'else-1))%4;q+=(1j,1,-1j,-1)[qh]
  if ti+1==len(raws[a]):saved=(set(bb),q,qh)
 board,p,h=saved;assert(pp,hh)==(p,h)
 assert board=={p+rotation(z,h)for z in K}|set(defids)
 rows.append(dict(packet=a,inputs=origin,beta=delta,mergers=len(comps)-1))
assert(p,h)==(2-1j,1)and clock==3
assert centers[0]==(-1-1j,1+1j)and centers[-1]==(-3+1j,3-1j)
def cross(z,w):return int(z.real*w.imag-z.imag*w.real)
a,v=centers[0][0],centers[0][1]-centers[0][0];b,w=centers[-1][0],centers[-1][1]-centers[-1][0];det=cross(v,w)
t=F(cross(b-a,w),det);u=F(cross(b-a,v),det);assert t==u==F(1,2)and a+float(t)*v==0
assert sum(row['mergers']for row in rows)==1
# All allowed exact angle cases depend only on ordering 0<atan(1/3)<pi/4.
b,horhash=freeze('first_center_contact_frozen_20261023_1412');alpha={'D':2,'C':2,'V':1,'U':0};cases=[]
for n in range(8):
 for a,aa in alpha.items():
  for b,ab in alpha.items():
   ok=(n in (3,4,5))or(n==2 and aa>ab)or(n==6 and aa<ab)
   if ok:cases.append((n,a,b))
assert len(cases)==58
out=dict(status='PASS independent actual crossing/zero-beta and exact angle reconstruction',control_manifest=controlhash,horizon_manifest=horhash,seed_mass=len(seed),raw_length=len(word),raw_endpoint=(*xy(p),h),incidence_rows=rows,twice_center_segments=[(xy(a),xy(b))for a,b in centers],crossing_parameters=[str(t),str(u)],exact_angle_cases=cases,scope='Actual ten-cell center crossing is compatible with zero incidence-rank increase. Analytically, earliest repeated point gives an injective simple closed subarc; its closing cusp cannot reverse without earlier overlap. Principal-turn lift forces entry-C gap2..6. No finite word/box bound, loop deletion, microscopic conflict, unfunded record, or global capture claim.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in ('exact_angle_cases','twice_center_segments','incidence_rows')})
