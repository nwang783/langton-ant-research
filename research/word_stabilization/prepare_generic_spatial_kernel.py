import json,sys
from pathlib import Path
from collections import defaultdict
mode=sys.argv[1];M=json.load(open('spaced_two_marker_macros.json'))['macros'];dirs=((0,1),(1,0),(0,-1),(-1,0))
def trace(w):
 p=(0,0);h=0;first={};last={}
 for t,c in enumerate(w):
  if last.get(p)==c:return None
  first.setdefault(p,(c,t));last[p]=c;h=(h+(1 if c=='R'else-1))%4;p=(p[0]+dirs[h][0],p[1]+dirs[h][1])
 return first,last,p,h
if mode=='n':
 ids=[0,3,8,10,45,71];E={8,10,45,71};g2={(a,b)for a in ids for b in ids};g3={(a,c,b)for a in ids for c in ids for b in ids if not(a in E and c==3 and b in E)}
elif mode=='single57':
 g=json.load(open('single_bad57_scc_grammar.json'));ids=g['alphabet'];g2={tuple(x)for x in g['pairs']};g3={tuple(x)for x in g['triples']}
elif mode=='full':
 q=json.load(open('spaced_two_marker_port_quotient.json'));ids=list(range(len(M)));A=defaultdict(list)
 for u,a,v in q['quotient_edges']:A[u].append((a,v))
 g2=set();g3=set()
 for u,a,v in q['quotient_edges']:
  for b,w in A[v]:
   g2.add((a,b))
   for c,z in A[w]:g3.add((a,b,c))
else:raise ValueError(mode)
def feasible(w):return trace(''.join(M[a]['word']for a in w)+M[w[-1]]['end_marker'])is not None
g2={w for w in g2 if feasible(w)};g3={w for w in g3 if feasible(w)};idx={a:i for i,a in enumerate(ids)};lines=[str(len(ids))]
for a in ids:
 raw=trace(M[a]['word']);tar=trace(M[a]['word']+M[a]['end_marker']);lines.append(f'{raw[2][0]} {raw[2][1]} {raw[3]} {len(raw[1])}')
 lines += [f'{p[0]} {p[1]} {int(c=="L")}'for p,c in raw[1].items()];lines.append(str(len(tar[0])));lines += [f'{p[0]} {p[1]} {int(c=="L")} {t}'for p,(c,t)in tar[0].items()]
lines.append(str(len(g2)));lines += [' '.join(str(idx[a])for a in w)for w in sorted(g2)];lines.append(str(len(g3)));lines += [' '.join(str(idx[a])for a in w)for w in sorted(g3)]
base='generic_'+mode;Path(base+'.input').write_text('\n'.join(lines)+'\n');Path(base+'.metadata.json').write_text(json.dumps({'ids':ids,'pairs':sorted(g2),'triples':sorted(g3)},indent=2));print(mode,'macros',len(ids),'pairs',len(g2),'triples',len(g3))
