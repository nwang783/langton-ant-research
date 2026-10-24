import json
from pathlib import Path
P=Path(__file__).parent
c=json.loads((P/'TERMINAL_TRAP_CERTIFICATE.json').read_text()); B=set(map(tuple,c['eleven_cell_source']));C=c['fixed_continuation'];H=c['period'];D=((0,1),(1,0),(0,-1),(-1,0));p=(0,0);h=2
states=[];reads=[]
for i,a in enumerate(C+H*3):
 states.append((set(B),p,h));reads.append(p);assert (p in B)==(a=='L');B^={p};h=(h+(1 if a=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
mins=[min(y for x,y in states[0][0])]
for i,(B,p,h) in enumerate(states[:len(C)+len(H)]):
 if p[1]<mins[-1]:
  mins.append(p[1]);G={r for r in reads[i:] if r[1]>p[1]};bb=G&B
  print(i,p,h,'guard',len(G),'black',len(bb),'miny',min(y for x,y in B))
