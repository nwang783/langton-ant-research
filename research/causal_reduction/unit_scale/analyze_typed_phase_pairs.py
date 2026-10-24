"""Exact composition of two heading-dependent elementary transport phases.
Inventory reduction uses legal primitive outer refinements, not legality of
any intermediate infinite phase word. Finite conflict means arbitrary-board
exclusion for that chosen composite root only.
"""
import json,pathlib,itertools,collections,time,hashlib
from search_heading_transport import inventories,D
BASE=pathlib.Path(__file__).parent

def rotate(a,j):return tuple(a[(s-2*j)%8] for s in range(8))
def expand(w,h,a):
 out=[]
 for c in w:
  out.append(a[2*h+(c=='L')]);h=(h+(1 if c=='R' else -1))%4
 return ''.join(out)
def typed(w,h):
 out=[]
 for c in w:
  out.append(2*h+(c=='L'));h=(h+(1 if c=='R' else -1))%4
 return out

def conflict(w,h=0):
 x=y=0;last={}
 for t,c in enumerate(w):
  if last.get((x,y))==c:return t
  last[x,y]=c;h=(h+(1 if c=='R' else -1))%4;x+=D[h][0];y+=D[h][1]
 return None

def main():
 st=time.monotonic();dom=inventories();surv=json.load(open(BASE/'probe_typed_transport_composition.survivors.json'))
 fs=sorted({rotate(q['assignment'],j) for q in surv for j in range(4) if q['length']>9})
 controllers={};domain_hist=collections.Counter();pair_count=0
 for f in fs:
  gd=[];cd=[]
  for s in range(8):
   opts=[(w,expand(w,s//2,f)) for w in dom[s%2]]
   opts=[z for z in opts if conflict(z[1],s//2) is None]
   gd.append([x[0] for x in opts]);cd.append([x[1] for x in opts])
  domain_hist[tuple(len(x) for x in gd)]+=1
  for inds in itertools.product(*(range(len(x)) for x in gd)):
   if not any(len(gd[s][inds[s]])>1 for s in range(8)):continue
   g=tuple(gd[s][inds[s]] for s in range(8));c=tuple(cd[s][inds[s]] for s in range(8));pair_count+=1
   controllers.setdefault(c,dict(outer=f,inner=g))
 print('outer_maps',len(fs),'phase_pairs',pair_count,'distinct_composites',len(controllers),flush=True)
 inv=[dict(composite=c,**phases) for c,phases in sorted(controllers.items())]
 pathlib.Path(__file__).with_suffix('.inventory.json').write_text(json.dumps(inv,separators=(',',':'))+'\n')
 records=[];survivors=[];rootcounts=collections.Counter();latest=0
 for c,phases in sorted(controllers.items()):
  words=[typed(c[s],s//2) for s in range(8)];F=[z[0] for z in words]
  for root in range(8):
   if len(c[root])==1:continue
   q=root;cycle=[]
   while q not in cycle:cycle.append(q);q=F[q]
   if q!=root:continue
   m=len(cycle);assert m in (1,2)
   rootcounts[m]+=1;v=[root];found=None
   for level in range(1,9):
    v=[z for s in v for z in words[s]]
    if level%m:continue
    turnword=''.join('RL'[s%2] for s in v)
    found=conflict(turnword,root//2)
    if found is not None:
     latest=max(latest,found);records.append(dict(composite=c,root=root,cycle=m,level=level,read=found,**phases));break
    if len(v)>100000:break
   if found is None:survivors.append(dict(composite=c,root=root,cycle=m,level=level,length=len(v),**phases))
 p=pathlib.Path(__file__);raw=(json.dumps(records,sort_keys=True,separators=(',',':'))+'\n').encode();p.with_suffix('.records.json').write_bytes(raw);p.with_suffix('.survivors.json').write_text(json.dumps(survivors,indent=2)+'\n')
 ans=dict(scope='two distinct independent eight-state identity/nine phases; all internally legal composite images; genuine growing root cycles',outer_maps=len(fs),phase_pairs=pair_count,distinct_composites=len(controllers),root_cases=dict(rootcounts),rejected=len(records),survivors=len(survivors),latest_conflict=latest,maximum_composite_image=max(len(w) for c in controllers for w in c),seconds=time.monotonic()-st,records_sha256=hashlib.sha256(raw).hexdigest())
 p.with_suffix('.json').write_text(json.dumps(ans,indent=2)+'\n');print(json.dumps(ans),flush=True)
if __name__=='__main__':main()
