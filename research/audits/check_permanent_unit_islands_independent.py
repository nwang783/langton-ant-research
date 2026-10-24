from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];U=ROOT/'causal_reduction/unit_scale';S=ROOT/'spatial_cursor_2026-10-23'
mp=U/'prepared1564_uniform_support_manifest.json';cp=U/'prepared1564_source_endpoint_family.json'
assert hashlib.sha256(mp.read_bytes()).hexdigest()=='90fcf1a66046418c38d07f7e935ea80cf873751aefae69a4b07af89ba3bd8399'
m=json.loads(mp.read_text());c=json.loads(cp.read_text());w=m['stages'][15]['word'];assert len(w)==1564 and m['seed_mass']==184
D=(1j,1,-1j,-1)
def trace(w,p,h):
 out=[]
 for i,b in enumerate(w):out.append((i,p,h,b));h=(h+(1 if b=='R'else-1))%4;p+=D[h]
 return out,p,h
def xy(p):return int(p.real),int(p.imag)
rs,p,h=trace(w,-6-6j,0);assert p==8+8j and h==0
Q=[1+18j,1+19j,2+18j,2+19j];profiles=[]
for q in Q:
 hits=[]
 for i,z,h,b in rs:
  dx,dy=xy(q-z)
  if dx==dy and dx%14==0:hits.append((dx//14,i,b))
 assert hits and{a for a,i,b in hits}=={0}and hits[-1][2]=='R';profiles.append((xy(q),hits))
assert profiles==[((1,18),[(0,1497,'R')]),((1,19),[(0,1490,'L'),(0,1498,'R')]),((2,18),[(0,1492,'L'),(0,1496,'R'),(0,1500,'L'),(0,1504,'R')]),((2,19),[(0,1491,'R'),(0,1495,'L'),(0,1499,'R')])]
_,p,h=trace(w[:1505],-6-6j,0);assert p==3+18j and h==1
opp2=2*p+(1-1j)*((-1j)**h);assert opp2==5+35j
cont,p,h=trace(c['after_checkpoint_word'],-6-6j,0);assert len(cont)==56504 and c['threshold_N']==4
umin=min(int(z.real+z.imag)for _,z,_,_ in cont);assert umin==-137 and(p,h)==(-104-24j,0)
tail,e,g=trace(c['capture_word'],p,h);assert len(tail)==104 and e-p==-2-2j and g==h
normals={int(z.real-z.imag)for _,z,_,_ in tail};assert(min(normals),max(normals))==(-86,-76)
assert normals.isdisjoint(int(q.real-q.imag)for q in Q)
# For j<=N-6, max u(Q_j)<=21+28(N-6)=28N-147<28N-137.
assert max(int(q.real+q.imag)for q in Q)-28*6 < umin
# Literal standard odd orbit profile at the supplied translated canonical cut.
b=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());tr,_,_=trace(b['word'],1+38j,b['heading']);counts=Counter((int(q.real-q.imag),int(q.real)%2)for _,q,_,_ in tr);P={k for k,v in counts.items()if v%2}
assert len(P)==12 and min(t for t,a in P)==-40 and max(t for t,a in P)==-30
# Exact quotient graph under U->U+2; no finite crop is used.
def edge(t,a):
 x,y=a,a-t
 if t%2==0:return((x+y-2)//2,(x-y)//2+20),((x+y)//2,(x-y)//2+20)
 return((x+y-1)//2,(x-y-1)//2+20),((x+y-1)//2,(x-y+1)//2+20)
def norm(e):
 e=sorted(e);q=e[0][0]//2;return tuple((u-2*q,v)for u,v in e)
actual={norm(edge(t,a))for t,a in P}
expected={norm(((u,v),(u+1,v)))for u in(0,1)for v in(0,5)}
path=[(1,0),(1,1),(1,2),(2,2),(2,3),(1,3)]
expected|={norm(e)for e in zip(path,path[1:])};expected.add(norm(((1,1),(2,1))))
path=[(1,5),(1,4),(2,4)];expected|={norm(e)for e in zip(path,path[1:])}
assert actual==expected and len(actual)==12
# Unit-square primal edges form one 4-cycle; different j have disjoint edges.
vertices=[]
for q in Q:
 x,y=xy(q);v=1+1j if(x+y)%2==0 else 1-1j;vertices.append((2*q-v,2*q+v))
ct=Counter(v for e in vertices for v in e);assert len(ct)==4 and set(ct.values())=={2}
note=S/'permanent_unit_islands_fixed_mass_countercontrol.md';assert hashlib.sha256(note.read_bytes()).hexdigest()=='d0f8b7cd8f86387b2e30f2aa790a103ad8a4f1dc42a04edf3b1c2aed0458c0ee'
out=dict(status='PASS independent permanent physical islands in original184 family',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),wave_copy_alignments=profiles,continuation_min_u=umin,tail_normal_hull=[min(normals),max(normals)],standard_profile=sorted(P),exact_standard_quotient_edges=sorted(actual),conclusion='N>=6 leaves at leastN-5 pairwise disjoint permanently occupied primal unit cycles and isolated opposite-white-dual vertices. Full standard bulk itself is two toothed bi-infinite trees.',scope='Actual whole future of signed finite184 family, including all56504 scattering reads and infinite tail. Physical islands are NOT certified genuine full-producer U output cycles in a retained-eight factor; no contradiction to renewal-chain theorem or capture.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
