"""Independent integer-vector ownership check for eventual affine cone equality."""
import itertools,json,pathlib
ROOT=pathlib.Path('/workspace/shared/langton');D=((0,1),(1,0),(0,-1),(-1,0))
def walk(word,h):
 p=(0,0);history={};first={}
 for c in word:
  if history.get(p)==c:return None
  history[p]=c;first.setdefault(p,c);h=(h+(1 if c=='R' else -1))%4;p=p[0]+D[h][0],p[1]+D[h][1]
 return p,first
records=[]
for k,a,theta in [(4,2,0),(7,3,1)]:
 inv=[]
 for hc,c,hf in itertools.product(range(4),'RL',range(4)):
  if (hf-k*hc-theta)%2:continue
  target=tuple(a*z for z in D[(hc+(1 if c=='R' else -1))%4])
  for letters in itertools.product('RL',repeat=k):
   w=''.join(letters);z=walk(w,hf)
   if z is not None and z[0]==target:inv.append((hc,c,hf,w,z[1]))
 targets=[]
 for hc,c,hf,w,first in inv:
  if hc!=0 or c!='R':continue
  witnesses=[]
  for (x,y),letter in first.items():
   if letter!='L':continue
   poses=set()
   for h,_,_,_,foot in inv:
    for u,v in foot:
     dx,dy=x-u,y-v
     if dx%a or dy%a:continue
     q=dx//a,dy//a
     if (sum(q)+h)%2==0:poses.add((*q,h))
   if poses and min(q[1] for q in poses)>=0:
    witnesses.append(dict(cell=[x,y],owners=sorted({q[:2] for q in poses})))
  assert witnesses
  targets.append(dict(word=w,fine_heading=hf,forward_witnesses=witnesses))
 records.append(dict(k=k,scale=a,theta=theta,oriented_records=len(inv),target_count=len(targets),targets=targets,status='PASS all target images have forward first-L witness'))
source=json.loads((ROOT/'computability/check_affine_small_owners_independent.json').read_text())
assert json.loads(json.dumps(records))==source
out=dict(status='all records and full owner sets independently matched',counts=[(r['k'],r['oriented_records'],r['target_count']) for r in records],scope='eventual affine equality k=3A-2 cases (4,2),(7,3), with correct fine-heading phases')
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
