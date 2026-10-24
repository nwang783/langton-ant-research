"""Discovery only: next adjacent corner after the fixed actual cap75."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'));from ant_exact import W,PHASES,plan,step,certify_period
sys.path.insert(0,str(HERE.parent/'blank_return_cap'));from discover import initial
sys.path.insert(0,str(HERE.parent/'transverse'));from crossing import tail

def main(n,cycle=False):
 field,p,h=initial(75);model=json.loads((HERE.parent/'blank_return_cap/fixed_caps.json').read_text());model=next(x for x in model['rows'] if x['phase']==75)
 with gzip.open(HERE.parent/'blank_return_cap'/'word_r75.txt.gz','rt') as f:old=f.read()
 for c in old:
  p,h,d=field.step(p,h);assert c==d
 q=(2*n+24,-2*n-12);assert not field.color(q);field.changes.symmetric_difference_update([q])
 
 if cycle:
  extra=[(-2*n-35,2*n+109),(2*n+24,2*n+109)]
  for e in extra:assert not field.color(e);field.flip(e)
 B=set(field.changes)
 for base,d,lo,hi in field.rays:
  for k in range(lo,lo+300):
   v=(base[0]+k*d[0],base[1]+k*d[1]);B.symmetric_difference_update([v])
 w=[];reads=[];hit=None;other_hits={}
 for t in range(1000000):
  reads.append(p)
  if cycle:
   for j,e in enumerate(extra):
    if p==e and j not in other_hits:other_hits[j]=t
  if p==q and hit is None:hit=t
  p,h,c=step(B,p,h);w.append(c)
  if hit is not None and (not cycle or 0 in other_hits) and t>=hit+1000 and (t+1)%104==0:
   tw=''.join(w[-104:])
   if tw in PHASES and ''.join(w[-312:])==tw*3:
    cert=certify_period(B,p,h,tw)
    if cert:
     for x in reads:field.changes.symmetric_difference_update([x])
     infinite=tail(field,p,h,tw)
     omitted_hits=[]
     for v in set(reads):
      for base,d,lo,hi in field.rays:
       delta=(v[0]-base[0],v[1]-base[1]);
       if delta[0]%d[0]==0 and delta[1]%d[1]==0 and delta[0]//d[0]==delta[1]//d[1]>=lo+300:omitted_hits.append(v)
     fn=f'r75_{"cycle_" if cycle else ""}n{n}.txt.gz'
     with gzip.open(HERE/fn,'wt') as f:f.write(''.join(w))
     out=dict(status='infinite-model discovery' if infinite and not omitted_hits else 'finite-only',n=n,marker=q,first_hit=hit,other_hits=other_hits,capture=t+1,pose=[p,h],tail=cert,infinite_tail=infinite,omitted_hits=omitted_hits[:10],bounds_u_z=[min(x-y for x,y in reads),max(x-y for x,y in reads),min(x+y for x,y in reads),max(x+y for x,y in reads)],word_file=fn);break
 else:out=dict(status='limit',n=n,marker=q,pose=[p,h])
 (HERE/f'r75_{"cycle_" if cycle else ""}n{n}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main(int(sys.argv[1]),'cycle' in sys.argv)
