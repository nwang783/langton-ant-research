"""Complete cap-four outer-reader transfer after the unique RRLL even band.
All ten unique-S-arrival G and ten unique-N-departure F words, not a scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
b = Path(__file__).parent
L = {'__file__':str(b/'explore_one_use_RRLL_transfer_graph.py')}
exec((b/'explore_one_use_RRLL_transfer_graph.py').read_text().split('states = []')[0], L)
check, words = L['check'], L['words']
def out(h, r):
    H = 'NESW'
    return H[(H.index(h[r]) + (1 if r % 2 == 0 else -1)) % 4]
Gs = [h for h in words('NS') if h.count('S') == 1]
Fs = [h for h in words('EW') if sum(out(h,r) == 'N' for r in range(len(h))) == 1]
assert len(Gs) == len(Fs) == 10

def patch(state, x=0):
    g,f = state
    return {(x,1):'E',(x+1,1):'N',(x,0):'NNSN',(x+1,0):'WWEW',
            (x,-1):'WWWE',(x+1,-1):'SSSN',(x,-2):g,(x+1,-2):f}

states=[];nc=Counter()
for state in product(Gs,Fs):
    result=check(patch(state));nc[result]+=1
    if result=='open':states.append(state)
print('node',nc,'states',len(states),states,flush=True)
edges=[];ec=Counter()
for i,a in enumerate(states):
    for j,c in enumerate(states):
        result=check(patch(a)|patch(c,2));ec[result]+=1
        if result=='open':edges.append((i,j))
adj={i:[]for i in range(len(states))}
for i,j in edges:adj[i].append(j)
index={};low={};stack=[];active=set();scc=[]
def visit(v):
    index[v]=low[v]=len(index);stack.append(v);active.add(v)
    for w in adj[v]:
        if w not in index:visit(w);low[v]=min(low[v],low[w])
        elif w in active:low[v]=min(low[v],index[w])
    if low[v]==index[v]:
        part=[]
        while True:
            w=stack.pop();active.remove(w);part.append(w)
            if w==v:break
        scc.append(part)
for i in adj:
    if i not in index:visit(i)
cyclic = [z for z in scc if len(z) > 1 or (z[0], z[0]) in edges]
print('edge',ec,len(edges),'cyclic',cyclic,flush=True)
for z in cyclic:print([(i,states[i])for i in z],flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,G_domain=Gs,F_domain=Fs,node_counts=dict(nc),states=states,edge_counts=dict(ec),edges=edges,cyclic_components=cyclic,warning='Necessary finite interface graph only; cycles do not certify exterior readers or a full cursor.'),indent=2)+'\n')
