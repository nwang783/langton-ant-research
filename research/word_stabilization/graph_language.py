from collections import defaultdict
from pathlib import Path
H=Path(__file__).with_name('standard_word.txt').read_text().strip(); W=H*2
F={W[i:i+10] for i in range(104)};succ=defaultdict(list);pred=defaultdict(list)
for f in sorted(F):succ[f[:-1]].append((f[1:],f[-1]));pred[f[1:]].append(f[:-1])
nodes={v for v in succ if len(succ[v])!=1 or len(pred[v])!=1}; ids={v:i for i,v in enumerate(sorted(nodes))}
for v in sorted(nodes):
    print('NODE',ids[v],v,'at',[i for i in range(104) if W[i:i+9]==v])
    for to,label in succ[v]:
        while to not in nodes:
            to,c=succ[to][0];label+=c
        print(' EDGE',ids[to],len(label),label)
# Branch paths return to one selected central vertex.
print('edges',len(F))
