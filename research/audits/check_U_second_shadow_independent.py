from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();B=ROOT/'core_periodicity_new/U_second_shadow_frozen_20261023_1754';M=json.loads((B/'manifest.json').read_text())
assert hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest()=='4f9baf189966b0f97deb5deb357c77eeef0ad6b7b59e91f5cceb8428f50138bc'
for r in M['files']:assert hashlib.sha256((B/r['frozen']).read_bytes()).hexdigest()==r['sha256']
K={q for q,b in walk(mark)[2].items()if b};P={-1+1j,-1+2j,2j,3j};ALL=P|{-1+4j};r=1+1j;s=1+2j;G={}
for a in(0,1,4,5,6,7,8,9):
 e,h,_,flip=walk(raws[a]);req=walk(raws[a]+mark)[2];black={q for q,b in req.items()if b};G[a]=dict(I=black-K,O=(black^flip)-{e+rotation(q,h)for q in K},C=set(req)|K,req=req,end=e,dh=h)
 if a in(7,8,9):assert G[a]['I']==ALL and req[r]is False and req[s]is False

def aligned(q):
 rows=[];surv=[]
 for a,g in G.items():
  for inp in g['I']:
   for h in range(4):
    p=q-rotation(inp,h);hit=P&{p+rotation(x,h)for x in g['C']};reason='sector'if(sum(xy(p))+h)%2 else'protected'if hit else'candidate';row=[a,(*xy(p),h),xy(inp),reason];rows.append(row)
    if reason=='candidate':surv.append((a,p,h))
 return rows,surv
one,H=aligned(r);two,C=aligned(s);assert Counter(x[3]for x in one)==dict(sector=46,protected=43,candidate=3);assert Counter(x[3]for x in two)==dict(sector=46,protected=37,candidate=9)
assert set(H)=={(a,2+0j,0)for a in(7,8,9)}
expected={(a,p,0)for aa,p in[((0,1),1+1j),((4,5),1-1j),((7,8),2-2j),((7,8,9),2+0j)]for a in aa};assert set(C)==expected
cross=lambda a,b:int(a.real*b.imag-a.imag*b.real)
def chord(a,p,h):
 base=0 if a in(0,1)else 4 if a in(4,5,6)else 7;beg=2*p+rotation(-1-1j,h);return beg,beg+2*rotation(G[base]['end'],h)
contacts=[]
for a,p,h in H:
 assert s in{p+rotation(q,h)for q in G[a]['I']}and s in{p+rotation(q,h)for q in G[a]['O']}
 end=(p+rotation(G[a]['end'],h),(h+G[a]['dh'])%4);x,y=chord(a,p,h);assert(x,y)==(3-1j,3+7j)
 for b,q,k in C:
  assert end!=(q,k);z,w=chord(b,q,k);u=y-x;v=w-z;den=cross(u,v)
  if den:
   aa=F(cross(z-x,v),den);bb=F(cross(z-x,u),den);assert 0<=aa<=1 and 0<=bb<=1;params=[str(aa),str(bb)];kind='closed contact'
  else:
   assert cross(z-x,u)==0;aa=F(int((z-x).imag),int(u.imag));bb=F(int((w-x).imag),int(u.imag));lo=max(F(0),min(aa,bb));hi=min(F(1),max(aa,bb));assert lo<hi;params=[str(lo),str(hi)];kind='positive overlap'
  contacts.append(dict(helper=a,clearer=b,clearer_pose=(*xy(q),k),intersection=kind,parameters=params,full_exit_matches=False))
assert len(contacts)==27
for a in(7,8,9):
 p=-1+1j;outs={p+q for q in G[a]['O']};ins={p+q for q in G[a]['I']};assert outs&ALL==P and r in outs and-1+4j in ins and-1+4j not in outs
out=dict(status='PASS universal two-generation U retirement shadow and final three four-cohort exclusions',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),first_counts=dict(Counter(x[3]for x in one)),second_counts=dict(Counter(x[3]for x in two)),first_rows=one,second_rows=two,all27_contacts=contacts,scope='Four protected final identities; forced U helper creates its own valid simple U-entry suffix. Fresh replacement s, not old root identity, must retire. No age/kernel premise, no component-merger or U-count theorem. Universal no-four-from-one-producer assembly remains separate.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(out['first_counts'],out['second_counts'])
