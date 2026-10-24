import json,sys
from pathlib import Path
from collections import defaultdict
prefix=sys.argv[1];q=json.load(open(prefix+'_port_quotient.json'));M=q['macro_words'];dirs=((0,1),(1,0),(0,-1),(-1,0))
def trace(w):
 p=(0,0);h=0;first={};last={}
 for t,c in enumerate(w):
  if last.get(p)==c:return None
  first.setdefault(p,(c,t));last[p]=c;h=(h+(1 if c=='R'else-1))%4;p=(p[0]+dirs[h][0],p[1]+dirs[h][1])
 return first,last,p,h
A=defaultdict(list)
for u,a,v in q['quotient_edges']:A[u].append((a,v))
g2=set();g3=set()
for u,a,v in q['quotient_edges']:
 for b,w in A[v]:
  g2.add((a,b))
  for c,z in A[w]:g3.add((a,b,c))
def feasible(w):return trace(''.join(M[a]['word']for a in w)+M[w[-1]]['end_marker'])is not None
g2={w for w in g2 if feasible(w)};g3={w for w in g3 if feasible(w)};g3 &= {tuple(z) for z in q.get('allowed_context_triples',g3)};lines=[str(len(M))]
for a in range(len(M)):
 raw=trace(M[a]['word']);tar=trace(M[a]['word']+M[a]['end_marker']);assert raw and tar
 lines.append(f'{raw[2][0]} {raw[2][1]} {raw[3]} {len(raw[1])}');lines += [f'{p[0]} {p[1]} {int(c=="L")}'for p,c in raw[1].items()];lines.append(str(len(tar[0])));lines += [f'{p[0]} {p[1]} {int(c=="L")} {t}'for p,(c,t)in tar[0].items()]
lines.append(str(len(g2)));lines += [' '.join(map(str,w))for w in sorted(g2)];lines.append(str(len(g3)));lines += [' '.join(map(str,w))for w in sorted(g3)]
Path(prefix+'_kernel.input').write_text('\n'.join(lines)+'\n');Path(prefix+'_grammar.json').write_text(json.dumps({'pairs':sorted(g2),'triples':sorted(g3),'macros':M},indent=2));print('macros',len(M),'pairs',len(g2),'triples',len(g3),flush=True)
