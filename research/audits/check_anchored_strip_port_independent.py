"""Exact fixed-anchor switch identity and literal periodic debt controls."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];U=ROOT/'causal_reduction/unit_scale';V=((0,1),(1,0),(0,-1),(-1,0));f=lambda n:3**abs(n)-1
M=json.loads((U/'prepared1564_uniform_support_manifest.json').read_text());Q=json.loads((U/'prepared4352_two_phase_manifest.json').read_text())
def J(p,h,c,s):
 z=p[0]+s*p[1]-c;e=V[h][0]+s*V[h][1];return f(z)//2 if z*e>=0 else-3*f(z)//2
def calc(word,p,h,k=0,a=1,b=0,s=-1):
 cA=k-a;cB=k+b;initial=(p,h);debt=nc=0
 for turn in word:
  side=p[0]+s*p[1]>=k;c=cB if side else cA;hh=(h+(1 if turn=='R'else-1))%4;q=tuple(p[j]+V[hh][j]for j in(0,1));debt+=J(q,hh,c,s)-J(p,h,c,s);nc+=(q[0]+s*q[1]>=k)!=side;p,h=q,hh
 piece=lambda p,h:J(p,h,cB if p[0]+s*p[1]>=k else cA,s)
 delta=piece(p,h)-piece(*initial);kap=(3**a+3**(b+1)-4)//2;assert debt==delta+kap*nc
 return dict(debt=debt,crossings=nc,delta=delta,end=(p,h),kappa=kap)
checks=0
for s in(-1,1):
 for h in range(4):
  for t in'LR':
   for k in(-2,0,3):
    for a in range(1,5):
     for b in range(4):
      for z in range(-6,7):calc(t,(z,0),h,k,a,b,s);checks+=1
H=M['stages'][0]['word'];W=M['stages'][-1]['word'];G=next(s['word']for s in Q['stages']if s['kind']=='wave');R=Q['stages'][-1]['word']
periods=[calc(H,(0,0),3),calc(W,(-6,-6),0),calc(G,(-2,3),3),calc(R,(117,111),0)]
assert [(r['debt'],r['crossings'],r['delta'])for r in periods]==[(8,8,0),(4,4,0),(66,66,0),(326,326,0)]
seed={(-2,-4),(-2,-3),(-2,0),(-1,-5),(-1,-2),(-1,-1),(-1,0),(0,-6),(0,-5),(0,-4),(0,0),(1,-3),(1,-2)}
s=SELF.with_name('check_prepared1564_connected_capture_independent.py').read_text();exec(compile(s[s.index('def periodic('):s.index('reports=[]')],str(SELF),'exec'))
fail,d,groups,n=periodic(seed,(0,0),3,H);assert fail is None and d==(-2,-2)
for a in groups:assert periodic(seed^{(a[0]+1000000*d[0],a[1]+1000000*d[1])},(0,0),3,H)[0]is not None
assert J((0,0),0,-37,-1)-J((-37,0),3,-37,-1)==-3*f(37)//2
assert J((6,0),0,25,-1)-J((25,0),3,25,-1)==f(19)//2
assert J((30,0),0,25,-1)-J((25,0),3,25,-1)==-3*f(5)//2
affine=[]
for name,manifest,expected in [('184',M,((144,559),(4,69))),('394two',Q,((1148,3498),(524,1786))),('394capture',json.loads((U/'prepared4352_capture_manifest.json').read_text()),((1148,3944),(524,2232)))]:
 total=[0,0];ordinary=[0,0]
 for st in manifest['stages']:
  x,y=st['start_x_N_constant'],st['start_y_N_constant'];assert x[0]==y[0]
  q=(x[1],y[1]);r=calc(st['word'],q,st['heading']);a,b=st['count_N_constant']
  if a or b>1:assert r['end'][0][0]-r['end'][0][1]==q[0]-q[1]and r['end'][1]==st['heading']
  for j,n0 in enumerate((a,b)):
   total[j]+=n0*r['crossings']
   if st['kind']in('H','H-prefix','SW-standard','SW-partial'):ordinary[j]+=n0*r['crossings']
 residual=[total[j]-ordinary[j]for j in(0,1)];assert(tuple(total),tuple(residual))==expected
 affine.append(dict(family=name,total=total,supplied_standard=ordinary,residual=residual))
out=dict(status='PASS exact fixed-anchor crossing identity and actual periodic controls',one_step_cases=checks,periods=periods,full_affine_crossings=affine,note_sha256=hashlib.sha256((ROOT/'spatial_cursor_2026-10-23/anchored_strip_crossing_port_identity.md').read_bytes()).hexdigest(),standard_seed_mass=13,standard_tail_orbits=len(groups),standard_tail_critical_tests=n,far_flip_rejections=len(groups),scope='Exact positive separator flux, not a global resource bound. Arbitrary-region streak bound must retain endpoint DeltaH unless it cancels or endpoint ports are bounded. Prepared bodies transfer to finite original seeds only through the previously signed family contracts.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],checks)
