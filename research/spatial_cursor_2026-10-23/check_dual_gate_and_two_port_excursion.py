from pathlib import Path
from collections import Counter
import json,hashlib
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent;U=ROOT/'causal_reduction/unit_scale'
manifest=json.loads((U/'prepared4352_capture_manifest.json').read_text());stages=manifest['stages']
W=next(s['word'] for s in stages if s['kind']=='wave');T=next(s['word'] for s in stages if s['kind']=='source-transition');P=next(s['word'] for s in stages if s['kind']=='return-wave');FULLZ=next(s['word'] for s in stages if s['kind']=='launch-end-response');Z=FULLZ[:17395];H=stages[0]['word']
F={(H*2)[i:i+10] for i in range(104)}
D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 x,y=p;return ((x,y),(y,-x),(-x,-y),(-y,x))[h]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def z2(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def w2(p,h):return add((2*p[0],2*p[1]),rot((1,-1),h))
def move(p,h,c):
 g=(h+(1 if c=='R' else -1))%4
 return add(p,D[g]),g
local=0
for x in range(-3,4):
 for y in range(-3,4):
  for h in range(4):
   for c in 'RL':
    p=(x,y);q,g=move(p,h,c);a,b=z2(p,h),w2(p,h);aa,bb=z2(q,g),w2(q,g)
    assert (b[0]-a[0],b[1]-a[1])==rot((2,0),h)
    if c=='R':assert aa==add(a,rot((2,2),h)) and bb==b
    else:assert aa==a and bb==add(b,rot((-2,2),h))
    assert add(a,add(a,rot((2,2),h)))==(4*x,4*y)
    assert add(b,add(b,rot((-2,2),h)))==(4*x,4*y)
    local+=1
# Trace one explicit word at its supplied pose; no board model assumed here.
def trace(w,p,h):
 out=[]
 for c in w:
  out.append((p,h,c));p,h=move(p,h,c)
 return out,(p,h)
wr,_=trace(W,(-2,3),3);tr,_=trace(T,(102,107),3);pr,_=trace(P,(117,111),0);zr,end=trace(Z,(117,111),0)
assert min(sum(q) for q,h,c in wr)==1
assert min(sum(q) for q,h,c in tr)==182
assert min(sum(q) for q,h,c in pr)==26 # adding156M then taking last SW copy gives182
assert zr[-1]==((10,-10),2,'R') and min(sum(q) for q,h,c in zr[:-1])>=1
assert end==((9,-10),3)
small={(-1,2),(-1,3)}
assert all(q not in small for q,h,c in wr+zr)
# Exact stationary-history counting for every positive number of copies.
def cost(word,history=''):
 last=history[-10:];n=0
 for c in word:
  v=last+c
  if len(v)>=11 and v[-11:-1] not in F and v[-10:] not in F:n+=1
  last=v[-10:]
 return n,last
cw,_=cost(W,'RLL');sw,_=cost(W,W[-10:]);ct,_=cost(T,W[-10:]);cp,_=cost(P,T[-10:]);sp,_=cost(P,P[-10:]);cz,_=cost(Z,P[-10:])
assert (cw,sw,ct,cp,sp,cz)==(1973,1972,75515,7358,7353,8418)
assert cw+3*sw+ct+cp-sp+cz==91827 and 3*sw+sp==13269
# Direct full continuous physical controls on newly initialized finite boards.
controls=[]
for M in (1,2):
 body=W*(3*M+4)+T+P*M+Z;rows,body_end=trace(body,(-2,3),3)
 first={};bits={}
 for q,h,c in rows:
  b=c=='L'
  if q not in first:first[q]=b;bits[q]=b
  assert bits[q]==b,(M,q,c)
  bits[q]=not b
 A={q for q,b in first.items() if b};assert not A&small and all(sum(q)>=1 for q in A)
 B=A|small;initial=set(B);p=(-2,2);h=0;boundary=[];Rcut=Lcut=0;inside_reads=0;full='RLL'+body
 for tick,c in enumerate(full):
  before=(p in B);assert before==(c=='L'),(M,tick,p,h,c)
  if sum(p)==0:
   boundary.append([tick,list(p),h,c]);Rcut+=c=='R';Lcut+=c=='L'
  # Sector-zero active cut is z_sum=-1 / +1. All pre-exit nonboundary reads inside.
  if tick>0 and tick<len(full)-1:assert sum(z2(p,h))>=2
  B.symmetric_difference_update({p});p,h=move(p,h,c)
 assert (p,h)==((9,-10),3)
 assert boundary==[[0,[-2,2],0,'R'],[len(full)-1,[10,-10],2,'R']]
 exterior={q for q in B if sum(q)<=0};assert exterior=={(-2,2),(10,-10)}
 assert not {q for q in initial if sum(q)<=0}
 assert len(full)==192957+28380*M
 kc,_=cost(full);assert kc==91827+13269*M
 assert Rcut==2 and Lcut==0 and len(exterior)==2
 controls.append({'M':M,'initial_mass':len(initial),'duration':len(full),'K_internal':kc,
  'boundary_events':boundary,'returned_exterior_black':sorted(exterior),'exit_pose':[list(p),h]})
result={'status':'all exact controls passed','local_dual_coupling_cases':local,'stationary_K_costs':[cw,sw,ct,cp,sp,cz],
 'direct_two_port_controls':controls,'scope':'Global dual-cursor gate algebra plus actual fixed-empty-exterior finite excursions; no fixed-mass claim.',
 'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [U/'prepared4352_capture_manifest.json',U/'prepared4352_two_phase_manifest.json']}}
(OUT/'dual_gate_two_port_controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
