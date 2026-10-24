"""Complete shortest connectors for the derived H/LR/Q diagonal pipeline.
Not a length-bound search: every shortest geometrically possible connector
between the three frozen endpoint poses is enumerated exactly.
"""
from pathlib import Path
import itertools,collections,json,hashlib
import certify_short_refinement_rup as core
P=Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))
H=json.loads((P/'short_refinement_scaffold_inputs.json').read_text())['H']
Q=json.loads((P/'forward108_prepared_control.json').read_text())['word']
def turns(ds,h):
 w=''
 for d in ds:
  z=(d-h)%4;assert z in(1,3);w+='R' if z==1 else 'L';h=d
 return w

def palettes():
 c1=[]
 for e in range(3):
  hs=[1 if i==e else 3 for i in range(3)]
  ds=[2,hs[0],2,hs[1],2,hs[2],2]
  c1.append(turns(ds,1))
 c2=[]
 for ee in itertools.combinations(range(7),2):
  hs=[1 if i in ee or i==7 else 3 for i in range(8)]
  ds=[d for i,h in enumerate(hs) for d in ([h,2] if i<7 else [h])]
  c2.append(turns(ds,2))
 c3=[]
 for ee in itertools.combinations(range(9),4):
  hs=[1 if i in ee or i==9 else 3 for i in range(10)]
  c3.append(turns([d for h in hs for d in (0,h)],1))
 for cs,st,en in zip((c1,c2,c3),((2,12,1),(2,7,2),(2,2,1)),((1,8,2),(0,0,1),(2,12,1))):
  for w in cs:
   rr,p,h=core.trace(w,st[:2],st[2]);assert (*p,h)==en
 return c1,c2,c3

def inspect(w):
 rr,p,h=core.trace(w,(0,10),1);assert p==(2,12) and h==1 and len(w)==256
 by=collections.defaultdict(list)
 for t,(q,hh,c) in enumerate(rr):
  by[(q[0]-q[1],q[0]%2)].append((t-len(w)*(q[0]//2),t,q,hh,c))
 bad=[]
 for a,es in sorted(by.items()):
  es.sort()
  if es[0][-1]!='R':bad.append(dict(kind='first_black',orbit=a,events=[es[0]]))
  for u,v in zip(es,es[1:]):
   if u[-1]==v[-1]:bad.append(dict(kind='repeat_turn',orbit=a,events=[u,v]))
 return bad,by

def main():
 ps=palettes();records=[];passing=[];hist=collections.Counter();minimum=999
 for ids in itertools.product(*(range(len(p)) for p in ps)):
  a,b,c=(ps[j][i] for j,i in enumerate(ids));w=H+a+'LR'+b+Q+c
  bad,by=inspect(w);minimum=min(minimum,len(bad))
  if not bad:passing.append(dict(ids=ids,word=w,histories=[dict(orbit=a,events=es) for a,es in sorted(by.items())]))
  else:
   records.append(dict(ids=ids,bad_count=len(bad),witness=bad[0]));hist[(bad[0]['kind'],tuple(bad[0]['orbit']))]+=1
 out=dict(scope=__doc__,palette_sizes=list(map(len,ps)),palettes=ps,total=len(records)+len(passing),minimum_bad_histories=minimum,passing=passing,first_witness_counts=[dict(kind=k[0],orbit=k[1],count=v) for k,v in sorted(hist.items())],records=records,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 (P/'pipeline_shortest_connectors.json').write_text(json.dumps(out,indent=2)+'\n')
 print({k:v for k,v in out.items() if k not in ['records','palettes','passing']});print('PASSING',len(passing))
if __name__=='__main__':main()
