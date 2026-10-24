from collections import defaultdict,Counter
B=set(); p=(0,0); h=0; D=((0,1),(1,0),(0,-1),(-1,0)); turns=[]; poses=[]
for t in range(12000):
    poses.append((*p,h))
    black=p in B
    turns.append('L' if black else 'R'); h=(h+(-1 if black else 1))%4
    if black:B.remove(p)
    else:B.add(p)
    p=(p[0]+D[h][0],p[1]+D[h][1])
H=''.join(turns[11000:11104])
assert all(turns[t]==turns[t+104] for t in range(11000,11896))
print('H',H)
open('/workspace/shared/langton/word_stabilization/standard_word.txt','w').write(H+'\n')
for k in range(1,30):
    word=H*2
    factors={word[i:i+k] for i in range(104)}
    succ=defaultdict(set); pred=defaultdict(set)
    for f in factors:succ[f[:-1]].add(f[1:]);pred[f[1:]].add(f[:-1])
    branches={v: len(ns) for v,ns in succ.items() if len(ns)>1}
    print(k,'factors',len(factors),'verts',len(succ),'branches',len(branches), 'branch locations', [H.find(b) for b in branches])
