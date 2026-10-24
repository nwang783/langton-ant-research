#!/usr/bin/env python3
"""One explicit two-layer moving-endpoint frame candidate, no cap/parameter scan.
First prove outer-frame ownership for all r,k, then one r=k10 natural orbit.
"""
from pathlib import Path
import sys,json,hashlib,time
P=Path('/workspace/shared/langton');O=Path(__file__).parent
sys.path.insert(0,str(P/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from isl_exact import Object,_FUN
C=Context(max_operations=5000000)
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def rotv(p,n):
 x,y=p
 for _ in range(n):x,y=y,neg(x)
 return x,y

def expr(v):return '('+'+'.join(f'{z}*{a}'for z,a in zip(v,('r','k','s','1')))+')'
def sets(shift):
 v=((2,1,0,shift),(0,-1,0,-shift-1));start=((0,0,0,0),(0,0,0,0));I=C.set('[r,k]->{[x,y]:false}');R=C.set('[r,k]->{[x,y]:false}')
 base=[('L',((0,0,1,0),(0,0,0,0)),'0<=s<2r'),('R',((0,0,1,0),(0,0,0,1)),'0<=s<2r'),('L',((2,0,1,0),(0,0,-1,-1)),f'0<=s<k+{shift}'),('R',((2,0,1,0),(0,0,-1,0)),f'0<=s<=k+{shift}')]
 for j in range(4):
  for turn,p,bound in base:
   q=rotv(p,j);q=tuple(plus(q[t],start[t])for t in(0,1));z=C.set('[r,k]->{[x,y]:r>=0 and k>=0 and exists(s:'+bound+f' and x={expr(q[0])} and y={expr(q[1])}' +')}')
   if turn=='L':I=I.union(z)
   else:R=R.union(z)
  d=rotv(v,j);start=tuple(plus(start[t],d[t])for t in(0,1))
 T=C.map(f'[r,k]->{{[x,y]->[X,Y]:X=x and Y=y+{shift}}}')
 I=Object(C,'map',_FUN['map','intersect_domain'](T._copy(),I._copy())).range()
 R=Object(C,'map',_FUN['map','intersect_domain'](T._copy(),R._copy())).range()
 return I.coalesce(),R.coalesce()
I0,R0=sets(0);I2,R2=sets(2);I4,R4=sets(4)
assert I2.intersect(I0.union(R0)).is_empty()
assert I0.intersect(I2).is_empty()and I2.intersect(I4).is_empty()
pre={'status':'EXACT all-r,k complete outer ownership PASS','domain':'r>=0,k>=0','initial':'K=I(r,k) UNION (I(r,k+2)+(0,2))','target':'K(r,k+2)+(0,2)','initial_mass':'16r+8k+8','target_mass':'16r+8k+24','first_word':'((LRRL)^r (RL)^k R)^4','first_complete_output':'I(r,k+1)+(0,1) UNION I(r,k+2)+(0,2)','outer_disjoint_entire_first_read_set':True,'initial_sector':1,'target_sector':1,'target_pose':[[0,2],1],'scope':__doc__}
(O/'two_layer_gap_frame_geometry.json').write_text(json.dumps(pre,indent=2)+'\n')
print(json.dumps(pre,indent=2),flush=True)
# Literal construction used only after the exact all-parameter ownership check.
D=((0,1),(1,0),(0,-1),(-1,0))
def minimal(r,k):
 w=('LRRL'*r+'RL'*k+'R')*4;p=(0,0);h=1;B=set();read=set()
 for c in w:
  assert p not in read;read.add(p)
  if c=='L':B.add(p)
  h=(h+(-1 if c=='L'else 1))%4;v=D[h];p=p[0]+v[0],p[1]+v[1]
 assert(p,h)==((0,0),1)
 return B,w,read
r=k=10;inner,w,read=minimal(r,k);outer,_,_=minimal(r,k+2);outer={(x,y+2)for x,y in outer};B=inner|outer;initial=set(B);targetinner,_,_=minimal(r,k+2);targetouter,_,_=minimal(r,k+4);target={(x,y+2)for x,y in targetinner}|{(x,y+4)for x,y in targetouter};assert len(B)==248 and len(target)==264 and not outer&read
sys.path.insert(0,str(P/'computability'));from periodic_tail_checker import first_mismatch,State,plan
H=json.loads((P/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];rotations={H[i:]+H[:i]for i in range(104)}
p=(0,0);h=1;t=0;recent='';turns=[];attempts=[];start=time.time();outcome=None
while outcome is None:
 if p==(0,2)and h==1 and B==target:
  outcome={'status':'EXACT TARGET HIT at this ONE parameter; no all-k renewal yet','time':t,'pose':[p,h],'mass':len(B)};break
 if t>=208 and t%104==0 and recent[:104]==recent[104:]and recent[104:]in rotations:
  word=recent[104:];state=State(frozenset(B),p,h);bad=first_mismatch(state,word);attempts.append({'time':t,'pose':[p,h],'mass':len(B),'first_mismatch':bad})
  if bad is None:outcome={'status':'AUTHOR EXACT permanent104 capture of this ONE candidate','time':t,'pose':[p,h],'mass':len(B),'tail_word':word,'drift':plan(state,word)[1]};break
 c='L'if p in B else'R';
 if t<len(w):assert c==w[t]
 B.symmetric_difference_update({p});h=(h+(-1 if c=='L'else 1))%4;v=D[h];p=p[0]+v[0],p[1]+v[1];t+=1;recent=(recent+c)[-208:];turns.append(c)
 if t==len(w):assert B==(read-inner)|outer and(p,h)==((0,0),1)
 if t%1000000==0:print('RUNNING',t,p,h,len(B),flush=True)
report={'r':r,'k':k,'initial_mass':len(initial),'target_mass':len(target),'outcome':outcome,'exact_tail_attempts':attempts,'elapsed':time.time()-start,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'One unchanged248cell two-concentric-gapframe seed. No cap/parameter/horizon scan or all-family inference.'}
(O/'two_layer_gap_frame_r10_k10.json').write_text(json.dumps(report,indent=2)+'\n');(O/'two_layer_gap_frame_r10_k10.word.txt').write_text(''.join(turns));(O/'two_layer_gap_frame_r10_k10.final.json').write_text(json.dumps({'black':sorted(B),'pose':[p,h]}));print(json.dumps(report,indent=2))
