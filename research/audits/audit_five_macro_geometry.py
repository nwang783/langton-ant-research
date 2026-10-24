"""Independent direct doubled-center geometry and literal source bindings."""
import ast,json
from pathlib import Path
R=Path('/workspace/shared/langton')
P=R/'audits/five_macro_snapshot/certify_five_macro_phase6.py'
# Bind the copied literals without importing/running the closure implementation.
t=ast.parse(P.read_text()); words={}
for st in t.body:
 if isinstance(st,ast.Assign) and len(st.targets)==1:
  v=st.targets[0]
  if isinstance(v,ast.Name) and v.id=='WORDS':words.update(ast.literal_eval(st.value))
  if isinstance(v,ast.Subscript) and isinstance(v.value,ast.Name) and v.value.id=='WORDS':words[ast.literal_eval(v.slice)]=ast.literal_eval(st.value)
source=json.loads((R/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json').read_text())
assert all(w==source[k]['word'] for k,w in words.items())
D=((0,1),(1,0),(0,-1),(-1,0))
def center(p,h):
 f=D[h];r=D[(h+1)%4]
 return (2*p[0]+f[0]-r[0],2*p[1]+f[1]-r[1])
def trace(p,h,w):
 tr=[]
 for c in w:
  tr.append((p,h,c));h=(h+(1 if c=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return tr,p,h
ends={}; sensitive=set(); patch={(x,y) for x in range(3) for y in range(-1,2)}
for h in range(4):
 # Exact common doubled center (-1,1), computed without checker pose formula.
 f=D[h];r=D[(h+1)%4]
 nums=(-1-f[0]+r[0],1-f[1]+r[1]);assert all(z%2==0 for z in nums)
 p=tuple(z//2 for z in nums)
 for m,w in words.items():
  tr,ep,eh=trace(p,h,w);ec=center(ep,eh);dc=(ec[0]+1,ec[1]-1)
  assert dc[0]%2==dc[1]%2==0
  shift=tuple(z//2 for z in dc)
  assert (shift[0]+shift[1])%2==0
  ends[h,m]=[shift,eh]
  for (x,y),_,_ in tr:
   for px,py in patch:
    tx,ty=px-x,py-y
    if (tx+ty)%2==0:sensitive.add((tx,ty))
assert len(sensitive)==80
# Phase-5 is the first read of q and the final producer stars have four Rs.
checks={}
for m,w in words.items():
 tr,p,h=trace((0,0),0,w)
 hits=[i for i,(p,_,_) in enumerate(tr) if p==(1,0)]
 assert hits[0]==5 and w[5]=='L' and w[6:10]=='RRRR'
 owner={'C':11,'V':14,'U':24,'Q':60,'B':70}[m]
 assert w[owner-1]=='L' and w[owner:owner+4]=='RRRR'
 if m!='C':assert owner+4==len(w)
 checks[m]=dict(length=len(w),phase5_hits=hits,allowed_producer=owner)
out=dict(status='PASS',bound_literal_source=str(source is not None),sensitive_centers=len(sensitive),heads=4*len(sensitive)+1,macros=checks,scope='Exact finite geometry plus algebraic center-lattice invariance; not a sampled-path theorem.')
(R/'audits/five_macro_geometry.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
