"""Discovery in the exact core-frame infinite-age reference; no transfer claim."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];OLD=HERE.parent/'blank_return_cap'
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'));from ant_exact import W,plan,PHASES
sys.path.insert(0,str(HERE.parent/'transverse'));from crossing import Field,tail

def reference(k):
 T=json.loads((OLD/'r28_complete_template.json').read_text());points={(-19,8),(-2*k-26,-2*k-5)};rays=[];p=(200,200);h=0
 for i,s in enumerate(T['segments']):
  word=s['word'];reads,_,end,eh=plan(word,(0,0),h);odd=set()
  for q in reads:odd.symmetric_difference_update([q])
  if s['type']=='finite':
   if i not in [0,6]:points.symmetric_difference_update((p[0]+x,p[1]+y) for x,y in odd)
   p=(p[0]+end[0],p[1]+end[1])
  else:
   a,b,c=s['count_mk'];count=100*a+k*b+c;d=end
   for x,y in odd:
    base=(p[0]+x,p[1]+y)
    if i in [1,7]:base=(base[0]+(count-1)*d[0],base[1]+(count-1)*d[1]);rays.append((base,(-d[0],-d[1]),0,None))
    elif i==5:rays.append((base,d,0,None))
    else:assert i==3;rays.append((base,d,0,count-1))
   p=(p[0]+count*d[0],p[1]+count*d[1])
  h=eh
 assert p==(45,-26) and h==3
 return Field(rays,points),p,h

def main(k):
 F,p,h=reference(k);q=(2*k+27,-2*k-5);assert not F.color(q);F.flip(q);word=[];reads=[];first=None
 for t in range(1200000):
  reads.append(p)
  if p==q and first is None:first=t
  p,h,c=F.step(p,h);word.append(c)
  if first is not None and t>first+50000 and (t+1)%104==0:
   tw=''.join(word[-104:])
   if tw in PHASES and ''.join(word[-312:])==tw*3:
    cert=tail(F,p,h,tw)
    if cert:
     name=f'parent_k{k}.txt.gz'
     with gzip.open(HERE/name,'wt') as f:f.write(''.join(word))
     out=dict(status='infinite-reference discovery only',k=k,marker=q,first_contact=first,capture=t+1,pose=[p,h],tail=cert,bounds_u_z=[min(x-y for x,y in reads),max(x-y for x,y in reads),min(map(sum,reads)),max(map(sum,reads))],word_file=name);break
 else:out=dict(status='limit',k=k,time=len(word),pose=[p,h],first_contact=first)
 (HERE/f'parent_k{k}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main(int(sys.argv[1]))
