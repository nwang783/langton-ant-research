"""Independent exact local/algebra checks for recovered recurrence prerequisites.
Not the general proof and not a highway search. Uses no recovered implementation.
"""
from fractions import Fraction as Q
import json
D=((0,1),(1,0),(0,-1),(-1,0))
def chi(p): return 1 if (p[0]+p[1])%2==0 else -1
def pow3(n): return Q(3**n) if n>=0 else Q(1,3**(-n))
def sig(p,h): return chi(p)*(1 if h%2==0 else -1)
def step(B,p,h):
    c=p in B
    g=(h+(-1 if c else 1))%4
    C=B^{p}; d=D[g]
    return C,(p[0]+d[0],p[1]+d[1]),g
EZ=(1,1,-1,-1); EU=(-1,1,1,-1)
def clocks(B,p,h):
    sigma=sig(p,h); ans=[]
    for f,es,sgn in ((lambda p:p[0]+p[1],EZ,-sigma),(lambda p:p[0]-p[1],EU,sigma)):
      for orient in (1,-1):
        field=sum((sgn*chi(q)*pow3(orient*f(q)) for q in B),Q(0))
        a=Q(1,2) if orient*es[h]==1 else Q(-3,2)
        ans.append(field+a*pow3(orient*f(p)))
    return ans

def G(p,h,r,sigma):
    if p[1]<r:return 0
    if p[1]>r:return 2
    kap=sigma*(-1 if r%2 else 1)
    return (0,kap,2,-kap)[h]
def F(p,h,c,sigma):
    if p[0]<c:return 0
    if p[0]>c:return 2
    kap=sigma*(-1 if c%2 else 1)
    return (kap,0,-kap,2)[h]

tests=0
for x in range(-3,4):
 for y in range(-3,4):
  p=(x,y)
  for h in range(4):
   for bit in (0,1):
    B={p} if bit else set(); C,q,g=step(B,p,h)
    assert sig(q,g)==sig(p,h)
    a,b=clocks(B,p,h),clocks(C,q,g)
    expect=[]
    for f,es in ((lambda p:p[0]+p[1],EZ),(lambda p:p[0]-p[1],EU)):
      expect.extend((4*pow3(f(p)) if es[h]==-1 and es[g]==1 else 0,4*pow3(-f(p)) if es[h]==1 and es[g]==-1 else 0))
    assert [b[i]-a[i] for i in range(4)]==expect
    assert sum(v>0 for v in expect)==1
    for r in range(-5,6):
      sb=sum((-1)**u for u,v in B if v==r); sc=sum((-1)**u for u,v in C if v==r)
      assert (sc-sb-G(q,g,r,sig(p,h))+G(p,h,r,sig(p,h)))%4==0
    for c in range(-5,6):
      tb=sum((-1)**v for u,v in B if u==c);tc=sum((-1)**v for u,v in C if u==c)
      assert (tc-tb-F(q,g,c,sig(p,h))+F(p,h,c,sig(p,h)))%4==0
    tests+=1

# Explore every legal color choice while avoiding one clock increment.
# The non-forbidden direction-sign word is positive then negative, so this tree
# has only polynomially many nodes at these depths. Stop at maximum black budget.
def avoid(K,h0,kind):
    es=(EZ,EU)[kind//2]; oldsign,newsign=((-1,1),(1,-1))[kind%2]
    best=0; nodes=0; repeated_reads=0
    stack=[((0,0),h0,{},0,0,set())]
    while stack:
      p,h,current,black,depth,read=stack.pop();nodes+=1;best=max(best,depth)
      if depth>2*K+3: raise AssertionError((K,h0,kind,depth))
      colors=(current[p],) if p in current else (0,1)
      for color in colors:
        bc=black+(color if p not in current else 0)
        if bc>K:continue
        g=(h+(-1 if color else 1))%4
        if es[h]==oldsign and es[g]==newsign:continue
        assert p not in read, ('Repeated read in forbidden-increment-free segment',p,h,depth)
        nxt=dict(current);nxt[p]=1-color;dx,dy=D[g]
        stack.append(((p[0]+dx,p[1]+dy),g,nxt,bc,depth+1,read|{p}))
    return best,nodes
res=[]
for K in range(21):
 for kind in range(4):
  out=[avoid(K,h,kind) for h in range(4)]
  assert max(a for a,b in out)==2*K+3
  res.append({'K':K,'type':kind,'max_length':max(a for a,b in out),'nodes':sum(b for a,b in out)})
result={'local_exact_cases':tests,'symbolic_forbidden_increment_cases':len(res),'max_K':20,'total_symbolic_nodes':sum(r['nodes'] for r in res),'all_pass':True,'results':res}
print(json.dumps({k:v for k,v in result.items() if k!='results'},indent=2))
open('/workspace/shared/langton/audits/global_constraints_independent.json','w').write(json.dumps(result,indent=2)+'\n')
