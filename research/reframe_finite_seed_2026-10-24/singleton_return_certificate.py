"""Exact component-fuel and bounded-stride certificates, no floating arithmetic."""
import json
from pathlib import Path
from collections import Counter
OUT=Path(__file__).parent
j=json.loads((OUT/'kernel_M5_scc.json').read_text());rs=j['first_return_cycles'];records=[];zero=[]
for i,r in enumerate(rs):
 consume=Counter();emit=Counter();single_in=single_out=0
 for t in r['transitions']:
  if t['consume']is not None:
   consume[t['consume']]+=1;single_in+=len(t['imported_component'])==1
  if t['emit']is not None:
   emit[t['emit']]+=1;single_out+=len(t['emitted_component'])==1
 drop=single_in-single_out;assert drop>=0
 if drop==0:zero.append(i)
 records.append({'index':i,'word':r['word'],'consumed_types':dict(sorted(consume.items())),'emitted_types':dict(sorted(emit.items())),'singletons_consumed':single_in,'singletons_emitted':single_out,'singleton_drop':drop})
assert zero==[0,11]
# Graph-theoretic relaxation: allow crossings at old interior stride-two vertices,
# but never enter an earlier START vertex. Every physical zero-drop run obeys it.
dirs=((1,0),(0,1),(-1,0),(0,-1));front=[((0,0),frozenset({(0,0)}),'')];levels=[]
for depth in range(9):
 nxt=[];dx,dy=dirs[depth%4]
 for p,seen,word in front:
  for stride in (1,2):
   pts=[(p[0]+k*dx,p[1]+k*dy)for k in range(1,stride+1)]
   if not any(q in seen for q in pts):nxt.append((pts[-1],seen|{pts[-1]},word+str(stride)))
 levels.append({'length':depth+1,'survivor_count':len(nxt),'stride_words':[w for p,s,w in nxt]});front=nxt
assert not front
out={'status':'EXACT_INTEGER_CERTIFICATES_AUTHOR_PENDING_AUDIT','zero_drop_first_return_indices':zero,'positive_drop_count':sum(r['singleton_drop']>0 for r in records),'component_counts':records,'geometric_survivors':levels,'scope':'Graph/count identities. Physical star-persistence and cursor-segment implication are proved separately in the companion note.'}
(OUT/'singleton_return_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('zero',zero,'strict',out['positive_drop_count'],'counts',[r['survivor_count']for r in levels])
