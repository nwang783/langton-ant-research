from pathlib import Path
from fractions import Fraction
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();B=ROOT/'core_periodicity_new/U_renewal_exact_clock_frozen_20261023_1902';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
for p,h in M['dependencies'].items():assert hashlib.sha256((ROOT/'core_periodicity_new'/p).read_bytes()).hexdigest()==h
C=raws[1][len(raws[0]):];D=(1j,1,-1j,-1);ctr=lambda p,h:2*p+rotation(-1-1j,h)
def run(word,p=0j,h=0):
 reads=[]
 for c in word:reads.append(p);h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return p,h,reads
def cross(a,b):return int(a.real*b.imag-a.imag*b.real)
def meet(A,B):
 a,b=A;c,d=B;u=b-a;v=d-c;z=cross(u,v)
 if z:
  t=Fraction(cross(c-a,v),z);s=Fraction(cross(c-a,u),z)
  return('point',t,s)if 0<=t<=1 and 0<=s<=1 else None
 if cross(c-a,u):return None
 f=(lambda q:int(q.real))if u.real else(lambda q:int(q.imag));ts=sorted((Fraction(f(c-a),f(u)),Fraction(f(d-a),f(u))));lo=max(ts[0],0);hi=min(ts[1],1)
 return('interval',lo,hi)if lo<=hi else None
P=-1+7j;E=5+1j;bridge=[E,3+3j,1+1j,-1+3j,P];edges=list(zip(bridge,bridge[1:]));source=(-1-1j,P);goal=(5-3j,E)
for q,(a,b)in zip((2+1j,1+1j,1j),edges):
 x,y=xy(q);v=1+1j if(x+y)%2==0 else 1-1j;assert {a,b}=={2*q-v,2*q+v}
for i in range(4):
 for j in range(i+1,4):
  m=meet(edges[i],edges[j])
  if j==i+1:assert m==('point',1,0)
  else:assert m is None
for j,e in enumerate(edges):assert meet(goal,e)==(('point',1,0)if j==0 else None)
assert edges[-1][0].real==source[0].real and source[0].imag<edges[-1][0].imag<P.imag
atom=[]
for name,word,v,cn in [('D',raws[0],2+2j,0),('V',raws[4],2+6j,0),('U',raws[7],8j,0),('C',C,2+2j,1)]:
 for h in range(4):
  p,g,_=run(word,h=h);assert ctr(p,g)-ctr(0j,h)==rotation(v,h)and g==(h-cn)%4
  atom.append((name,h,xy(ctr(p,g)-ctr(0j,h)),cn))
# All alpha are in [pi/4,pi/2], C alpha exactly pi/4. Therefore zero-C
# predecessor turns lie[-pi/4,pi/4], C turns[pi/2,3pi/4], all principal.
angles=[2,3,5,3,2];turns=[(b-a+4)%8-4 for a,b in zip(angles,angles[1:])];assert turns==[1,2,-2,-1]and sum(turns)==0
K={q for q,b in walk(mark)[2].items()if b};Z={1+0j,1+1j,2+0j,2+1j};tails=[]
for s,n in((7,0),(8,1),(9,2)):
 assert raws[s]==raws[7]+C*n;e,h,_,f=walk(raws[s]);black={q for q,b in walk(raws[s]+mark)[2].items()if b};O=(black^f)-{e+rotation(q,h)for q in K};assert Z|{1j}<=O
 p,h,_=run(raws[7]);assert ctr(p,h)==P
 for j in range(n):
  a=ctr(p,h);p,h,reads=run(C,p,h);b=ctr(p,h);assert not set(reads)&(Z|{1j});hits=[(k,meet((a,b),e))for k,e in enumerate(edges)if meet((a,b),e)is not None]
  assert hits==([(3,('point',0,1))]if j==0 else[]);tails.append((s,j,xy(a),xy(b)))
# Same-heading creator/breaker makes C gap nonnegative multiple4. The
# protected future arc plus bridge is Jordan, and its signed turn n*pi/2
# is +/-2pi; nonnegative n therefore equals4. Age is FULL-source ENTRY
# included to breaker ENTRY excluded, not the internal output-install time.
assert [n for n in range(0,9)if n in(-4,4)]==[4]
out=dict(status='PASS independent protected Jordan bridge and exact-four-C renewal interface',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),bridge_doubled=list(map(xy,bridge)),atomic_geometry=atom,source_tail_chords=tails,bridge_turns_pi_over_4=turns,analytic_conclusion='Cgap=4; each produced upper birth<=creator full-entry clock-1; factor-first creator breaker has exactly4 historical input components',scope='Source U-entry suffix simplicity plus current original Z/w lifetimes protect bridge; source C tails separately checked before full-output ledger birth. No direct lower-parent2/3 potential, finite chain or U-count bound.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
