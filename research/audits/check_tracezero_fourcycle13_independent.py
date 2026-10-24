"""Independent inventories, additive spectral coefficients and cone records.
Uses complex geometry, a fixed proven forcing period, and opposite-source pairs.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
from collections import defaultdict,Counter
from math import lcm,prod
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];FOLDER=ROOT/'computability/tracezero_fourcycle13'
J=json.loads((FOLDER/'inventory.json').read_text());records=json.loads((FOLDER/'cone_only.records.json').read_text())
D=(1j,1,-1j,-1);CYCLE=(3,0,1,2);domains=[];rawcounts=[]
def legal(word,heading):
 p=0j;colors={}
 for out in word:
  ratio=out/heading;assert ratio in (1j,-1j)
  needed=int(ratio==1j)
  if p in colors and colors[p]!=needed:return False
  colors[p]=1-needed;p+=out;heading=out
 return True
for source in range(4):
 words={};raw=0
 for signs in product((-1,1),repeat=12):
  word=[D[CYCLE[source]]]
  for j,s in enumerate(signs,1):word.append(s*(1j if (j+source)%2 else 1))
  if sum(word)!=3j*D[source]:continue
  raw+=1;heads=tuple(h for h in D if h/word[0] in (1j,-1j)and legal(word,h))
  if heads:words[tuple(word)]=set(heads)
 assert raw==300 and len(words)==56;rawcounts.append(raw)
 author={tuple(D[x]for x in r['word']):set(D[x]for x in r['heads'])for r in J['domains'][source]}
 assert words==author
 domains.append([tuple(D[x]for x in r['word'])for r in J['domains'][source]])
assert all(set(w)==set(D)for opts in domains for w in opts)
records_by_key={tuple(r['indices']):r for r in records};assert len(records_by_key)==len(records)

def rotated(x,y,n):
 for _ in range(n%4):x,y=-y,x
 return x,y

def contribution(source,word,G):
 # Actual seam map powers, with no imported general periodicity routine.
 gp=list(range(4));fp=list(range(4));bs=[]
 for r in range(1,11):
  total=0
  for u,v in zip(word,word[1:]):
   ratio=D[fp[D.index(v)]]/D[gp[D.index(u)]]
   assert ratio in (1j,-1j);total+=1 if ratio==-1j else -1
  bs.append(total);gp=[G[x]for x in gp];fp=[CYCLE[x]for x in fp]
 assert bs[2:6]==bs[6:10]
 charge=Q(0);ex=Q(0);ey=Q(0)
 for r,b in enumerate(bs[:6],1):
  cyc=r>=3;charge+=Q(b,4*13**r)/(1-Q(1,13**4)if cyc else 1)
  # Coordinate coefficient of a forcing concentrated at source d.
  x=Q(b*int(D[source].real),2);y=Q(b*int(D[source].imag),2)
  x,y=rotated(x,y,r);weight=Q(1,3**r)/(1-Q(1,81)if cyc else 1)
  ex+=x*weight;ey+=y*weight
 return charge,ex,ey

summaries=[];checked=set();hist=Counter();controller_total=0;zero_total=0
for G in product(*[(CYCLE[d],(CYCLE[d]+2)%4)for d in range(4)]):
 opts=[]
 for d in range(4):opts.append([(i,contribution(d,w,G))for i,w in enumerate(domains[d])if D.index(w[-1])==G[d]])
 scale=lcm(*(x.denominator for opt in opts for i,v in opt for x in v))
 ints=[[(i,*(int(x*scale)for x in v))for i,v in opt]for opt in opts]
 maps=[]
 for a,b in ((0,2),(1,3)):
  mp=defaultdict(list)
  for i,c,x,y in ints[a]:
   for j,e,u,v in ints[b]:mp[c+e].append((i,j,x+u,y+v))
  maps.append(mp)
 count=prod(map(len,opts));zero=0;surv=0
 for c,left in maps[0].items():
  right=maps[1].get(-c,());zero+=len(left)*len(right)
  for i,l,x,y in left:
   for j,m,u,v in right:
    if y+v<2*scale:continue
    ids=(i,j,l,m);assert ids not in checked;checked.add(ids);surv+=1
    r=records_by_key[ids];ex=Q(x+u,scale);ey=Q(y+v,scale)
    assert [str(ex),str(ey)]==r['ell']and list(G)==r['last_map']
    images=[domains[d][ids[d]]for d in range(4)]
    # Four-digit random-access expansion is geometric only, no ant simulator.
    p=0j;first=None
    for n in range(13**4):
     if ex*int(p.real)+ey*int(p.imag)<2*max(abs(int(p.real)),abs(int(p.imag))):first=n;break
     z=n;ds=[]
     for _ in range(4):ds.append(z%13);z//=13
     a=0
     for digit in reversed(ds):a=D.index(images[a][digit])
     p+=D[a]
    assert first is not None and first==r['read']and[int(p.real),int(p.imag)]==r['cell']
    hist[first]+=1
 summaries.append(dict(last_map=G,controllers=count,zero_C=zero,root_cone_survivors=surv));controller_total+=count;zero_total+=zero
 print(json.dumps(summaries[-1]),flush=True)
assert checked==set(records_by_key)
assert(controller_total,zero_total,len(checked),max(hist))==(9834496,1224564,20475,489)
expected=json.loads((FOLDER/'cone_only.json').read_text());assert {str(k):v for k,v in hist.items()}==expected['histogram']
out=dict(status='PASS all root cycles for k13 A=3J independent four-direction images',raw_domains=rawcounts,legal_domains=list(map(len,domains)),controllers=controller_total,zero_C=zero_total,root_cone_survivors=len(checked),last_first_cone_violation=max(hist),histogram=dict(sorted(hist.items())),last_maps=summaries,analytic_branches=['Two-cycles excluded by signed HA applied to A squared.','F=-J four-cycle has opposite prefixes d and -3d, violating the exact scalar-power cone.'],sha256={f:hashlib.sha256((FOLDER/f).read_bytes()).hexdigest()for f in ['inventory.json','exclusion.md','cone_only.records.json']},scope='Finite support only; ordinary four independent absolute-direction images; no hidden alphabet, variable directive schedule, or other trace-zero parameters.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['histogram','last_maps']},indent=2))
