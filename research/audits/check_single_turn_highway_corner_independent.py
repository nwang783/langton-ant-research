"""Independent all-m literal/full-field and all-future corner reconstruction."""
from pathlib import Path
import json,sys,hashlib,time
R=Path('/workspace/shared/langton');D=R/'causal_reduction/unit_scale';P=D/'single_turn_highway_corner_certificate.json';J=json.loads(P.read_text());S0=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text());H=S0['word'];assert S0['heading']==3 and len(H)==104
sys.path.insert(0,str(R/'sources/kehao95-core/defect_synthesis/verification/presburger_defects'));from isl_exact import Context
C=Context(max_operations=100000000);started=time.monotonic()
def xy(z):return int(z.real),int(z.imag)
def trace(w,p,h):
 ans=[]
 for t,c in enumerate(w):ans.append((p,c,t));h*=(-1j if c=='R'else 1j);p+=h
 return ans,p,h
def execute(B,p,h,w):
 for c in w:
  assert(p in B)==(c=='L');B.symmetric_difference_update([p]);h*=(-1j if c=='R'else 1j);p+=h
 return p,h
base={complex(x,y)*1j for x,y in S0['seed']};head,heading=execute(base,0j,-1j,H[:68]);base={z-head for z in base};assert heading==1j and len(base)==23
assert sorted(map(xy,base))==list(map(tuple,J['base_seed']))
F=H[68:]+H[:68];assert F==J['input_word'];slots,end,h=trace(F,0j,1j);assert(end,h)==(2-2j,1j)
K={complex(x,y)for x,y in((1,4),(1,5),(1,6),(2,0),(2,1),(2,2),(2,5),(3,0),(3,3),(3,4))};assert K=={complex(x,y)for x,y in J['corner_relative_black']}
def S(c):return C.set('[m]->{[x,y]:m>=3 and ('+c+')}')
def T(c):return C.set('[m]->{[t]:m>=3 and ('+c+')}')
def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
def pts(points):return S(' or '.join(f'(x={x} and y={y})'for x,y in map(xy,points))or'false')
markers=S(' or '.join(f'(x=2*m+{x} and y=-2*m+{y})'for x,y in map(xy,K)))
read=S('false');parity=S('false')
for z,c,t in slots:
 x,y=xy(z);family=S(f'exists(i:0<=i<m and x={x}+2*i and y={y}-2*i)');read=read.union(family);parity=xor(parity,family)
assert markers.intersect(read.union(pts(base))).is_empty()
initial=pts(base).union(markers);before=xor(initial,parity);cap=S('x=2*m and y=-2*m');assert before.intersect(cap).is_empty();after=xor(before,cap)
assert initial.is_equal(C.set(J['initial_relation'])) and before.is_equal(C.set(J['entry_before_R_relation'])) and after.is_equal(C.set(J['output_relation']))
# Signed standard104 supplies the approach; independently check the phase family too.
def allfuture(start_board,word,p,h,ox,oy):
 slots,end,hh=trace(word,p,h);assert hh==h;dx,dy=xy(end-p);n=0;nonempty=0
 for z,c,j in slots:
  C.reset_operations();x,y=xy(z);selector=C.map(f'[m]->{{[x,y]->[t]:m>=3 and t>=0 and x=({ox})+{x}+{dx}*t and y=({oy})+{y}+{dy}*t}}')
  color=selector.binary('intersect_domain',start_board).range()
  for v,cv,l in slots:
   vx,vy=xy(v);old=T(f't>=0 and exists(u:u>=0 and {x}+{dx}*t={vx}+{dx}*u and {y}+{dy}*t={vy}+{dy}*u and 104*u+{l}<104*t+{j})');n+=1
   if not old.is_empty():nonempty+=1;color=xor(color,old)
  assert (T('t>=0').subtract(color)if c=='L'else color).is_empty(),j
 return n,nonempty,slots
approach_pairs,approach_rel,_=allfuture(pts(base),F,0j,1j,'0','0')
pairs,relations,outslots=allfuture(after,H,1+0j,1+0j,'2*m','-2*m')
assert pairs==10816 and relations==262
odd=set()
for z,c,j in outslots:odd.symmetric_difference_update([z])
assert sorted(map(xy,odd))==list(map(tuple,J['complete_outgoing_first_block_xor_relative_cap']))
histories={}
for k in sorted(K,key=xy):
 visits=[]
 for z,c,j in outslots:
  d=k-z
  if d.real==d.imag and d.real%2==0 and d.real>=0:visits.append((int(d.real/2)*104+j,c))
 visits.sort();assert visits and all(c==('L'if n%2==0 else'R')for n,(t,c)in enumerate(visits));histories[str(xy(k))]=visits
assert sum(len(v)%2 for v in histories.values())==8
controls=[]
for m in(3,4,50):
 board=base|{z+complex(2*m,-2*m)for z in K};assert len(board)==33
 p,h=execute(board,0j,1j,F*m+'R');assert(p,h)==(complex(2*m+1,-2*m),1+0j);execute(board,p,h,H*100);controls.append(m)
out={'status':'PASS exact all-m>=3 full-board one-shot corner and every future read','candidate_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'initial_mass':33,'turn_time':'104*m+1','turn_pose':['2*m+1','-2*m','E'],'outgoing_drift':[2,2],'approach_ordered_pairs':approach_pairs,'approach_nonempty_prior_relations':approach_rel,'outgoing_ordered_pairs':pairs,'outgoing_nonempty_prior_relations':relations,'complete_corner_histories':histories,'corner_cells_erased_after_last_use':8,'literal_m_controls':controls,'seconds':time.monotonic()-started,'scope':'Finite prepared one-shot SE-to-NE corner. All ten cells read; eight consumed. No restoration, renewable corner, compound construction or noncapture model.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
