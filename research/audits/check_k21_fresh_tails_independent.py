from pathlib import Path
from collections import deque
import json,hashlib
P=Path(__file__).resolve().parents[1];dirs=[1j,1,-1j,-1]
def opts(p,b):return[b[p]]if p in b else([False]if p.imag>=0 else[False,True])
def step(p,h,b,bit):
 q=b.copy();q[p]=not bit;g=h*(1j if bit else-1j);return p+g,g,q
report=json.loads((P/'computability/check_k21_fresh_tails.json').read_text());results=[]
for rec in report['tails']:
 p=0j;h=1j;b={}
 for c in rec['tail']:
  bit=c=='L';assert bit in opts(p,b);p,h,b=step(p,h,b,bit)
 assert p==-1+1j and h==1j
 if rec['tail']=='RRRRLR':
  q,g,c=p,h,b.copy();post=[]
  for _ in range(4):
   v=opts(q,c);assert len(v)==1;q,g,c=step(q,g,c,v[0]);post.append(dirs.index(g))
  assert post==[1,2,3,2]
 todo=deque([(p,h,b,'',(0,0,0,0))]);nodes={};target=(5,7,5,4)
 while todo:
  p,h,b,w,c=todo.popleft();assert len(w)<21;options=opts(p,b);pruned=[]
  for bit in options:
   q,g,v=step(p,h,b,bit);d=dirs.index(g)
   if c[d]==target[d]:pruned.append(d);continue
   cc=list(c);cc[d]+=1;todo.append((q,g,v,w+('L'if bit else'R'),tuple(cc)))
  nodes[w]={'word':w,'pose':[int(p.real),int(p.imag),dirs.index(h)],'counts':list(c),'options':list(map(int,options)),'pruned':pruned}
 assert nodes=={x['word']:x for x in rec['tree']}
 results.append({'tail':rec['tail'],'nodes':len(nodes),'max_extension':max(map(len,nodes))})
out={'status':'PASS independent complete k21 tail continuations and post-F obstruction','tails':results,'certificate_sha256':hashlib.sha256((P/'computability/check_k21_fresh_tails.json').read_bytes()).hexdigest(),'note_sha256':hashlib.sha256((P/'computability/rectangular_k21_record_exclusion.md').read_bytes()).hexdigest()}
(P/'audits/k21_fresh_tails_independent.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
