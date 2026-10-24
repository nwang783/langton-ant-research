"""Independent enumeration: binary masks, current colors, base-k digit access.
No discovery geometry, conflict or substitution-stream routine is imported.
Finite survivors are discharged by an exact infinite first-L sublattice lemma.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json,time,hashlib
ROOT=Path('/workspace/shared/langton');SOURCE=ROOT/'causal_reduction/morphic_candidates';start=time.time()
def image(bits):
 p=0j;heading=1j;colors={}
 for b in bits: # 0 means R / white; 1 means L / black
  if p in colors and colors[p]!=b:return
  colors[p]=1-b;heading*=1j if b else -1j;p+=heading
 return heading,p
summary=[];remaining=[];total=Counter()
for n in range(3,18,2):
 groups=defaultdict(list)
 for mask in range(1<<n):
  bits=tuple((mask>>j)&1 for j in range(n-1,-1,-1));g=image(bits)
  if g and g[0] in (1,-1) and abs(g[1])**2>1:groups[g].append(bits)
 outcomes=Counter();latest=-1;count=0;digits=[]
 for t in range(5000):
  z=t;d=[]
  while z:d.append(z%n);z//=n
  digits.append(tuple(reversed(d)))
 for (heading,a),us in groups.items():
  if heading!=1:continue
  norm=int(a.real)**2+int(a.imag)**2
  for u in us:
   for v in groups.get((-1,-a),[]):
    modes=[]
    if v[0]==1:modes.append(('L',1,1))
    if u[0]==1 and v[0]==0:modes.append(('two_cycle',0,2))
    for mode,root,period in modes:
     count+=1;eu=sum(1-2*b for b in u);ev=sum(1-2*b for b in v);bias=(eu+ev)//2
     analytic=bias<0 or (bias!=0 and n>norm) or (bias==0 and (mode=='L' or eu*eu<=norm or abs(eu)>norm))
     if analytic:outcomes['analytic_filter']+=1;continue
     depth=period
     while n**depth<5000:depth+=period
     p=0j;h=1j;colors={};maps=(u,v)
     for t,ds in enumerate(digits):
      b=root
      for _ in range(depth-len(ds)):b=maps[b][0]
      for d in ds:b=maps[b][d]
      if p in colors and colors[p]!=b:
       outcomes['chronology_conflict']+=1;latest=max(latest,t);break
      colors[p]=1-b;h*=1j if b else -1j;p+=h
     else:
      outcomes['finite_survivor']+=1
      remaining.append(dict(n=n,u=''.join('L'if b else'R'for b in u),v=''.join('L'if b else'R'for b in v),mode=mode,root=root,a=[int(a.real),int(a.imag)]))
 total.update(outcomes);row=dict(n=n,internally_valid_images=sum(map(len,groups.values())),rooted_cases=count,outcomes=dict(outcomes),latest_conflict=latest);summary.append(row);print(json.dumps(row),flush=True)
old=json.loads((SOURCE/'complementary_roots_l17.json').read_text())
for new,original in zip(summary,old['results']):
 expected=original['totals'].copy()
 if 'prefix_survivor'in expected:expected['finite_survivor']=expected.pop('prefix_survivor')
 assert new['outcomes']==expected and new['internally_valid_images']==original['internally_valid_images']
assert total=={'analytic_filter':1000661,'chronology_conflict':240394,'finite_survivor':2}
assert sum(x['rooted_cases']for x in summary)==1241057 and max(x['latest_conflict']for x in summary)==3466
for r in remaining:
 u,v=r['u'],r['v'];a=complex(*r['a']);A=a*a;X,Y=int(A.real),int(A.imag);norm=X*X+Y*Y
 squared={c:''.join(u if z=='R'else v for z in w)for c,w in [('R',u),('L',v)]}
 assert squared['R'][:2]=='RL' and squared['L'][:3]=='LRL'
 for c,w in squared.items():
  assert len(w)==289 and w[0]==c
  p=0j;h=1j
  for j,z in enumerate(w):
   x,y=int(p.real),int(p.imag)
   if j:assert (X*x+Y*y)%norm or (X*y-Y*x)%norm
   h*= -1j if z=='R'else 1j;p+=h
  assert (p,h)==((A,1)if c=='R'else(-A,-1))
 r.update(squared_scale=[X,Y],isolated_internal_offsets=576,first_L_R=[1,[1,0]],first_L_L=[2,[-1,1]])
out=dict(status='Independent exhaustive complementary-root exclusions passed',rooted_cases=1241057,totals=dict(total),maximum_conflict_time=3466,rows=summary,sublattice_discharged_survivors=remaining,seconds=time.time()-start,scope='Only uniform internally feasible two-letter opposite-displacement geometric images of odd lengths3 through17, with L-prolongable or alternating first-letter roots. The two finite survivors are excluded by infinite first-L scaling, not the5000-step cutoff.')
Path(__file__).with_name('complementary_roots_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
