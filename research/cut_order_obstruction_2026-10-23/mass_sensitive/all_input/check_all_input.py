#!/usr/bin/env python3
"""Finite controls only; all-time proofs are in the accompanying notes."""
import json, random
from pathlib import Path

class History:
    def __init__(self, roots):
        self.parent=list(range(roots)); self.size=[1]*roots
        self.adj=[set() for _ in range(roots)]
        self.live=set(range(roots)); self.c=roots; self.edges=0
        self.r0=roots; self.v=0; self.u=0; self.beta=0; self.packet_count=0
    def new(self):
        x=len(self.parent); self.parent.append(x); self.size.append(1)
        self.adj.append(set()); self.c+=1; return x
    def find(self,x):
        while self.parent[x]!=x:
            self.parent[x]=self.parent[self.parent[x]]; x=self.parent[x]
        return x
    def link(self,a,b):
        assert b not in self.adj[a]
        self.adj[a].add(b); self.adj[b].add(a); self.edges+=1
        a=self.find(a); b=self.find(b)
        if a!=b:
            if self.size[a]<self.size[b]: a,b=b,a
            self.parent[b]=a; self.size[a]+=self.size[b]; self.c-=1
    def packet(self, inputs, outputs):
        assert len(set(inputs))==len(inputs) and set(inputs)<=self.live
        a=len(inputs); assert a in (1,2,5)
        g=len({self.find(i) for i in inputs}); old=self.beta
        p=self.new()
        for i in inputs: self.link(i,p); self.live.remove(i)
        out=[]
        for _ in range(outputs):
            i=self.new(); self.link(p,i); self.live.add(i); out.append(i)
        self.packet_count+=1; self.v+=a==2; self.u+=a==5
        self.beta=self.edges-len(self.parent)+self.c
        assert self.beta-old==a-g
        assert self.beta==self.v+4*self.u-self.r0+self.c
        assert self.beta>=old
        return out,p
    def independent_components(self):
        seen=set(); c=0
        for i in range(len(self.adj)):
            if i in seen: continue
            c+=1; seen.add(i); todo=[i]
            while todo:
                x=todo.pop()
                for y in self.adj[x]:
                    if y not in seen: seen.add(y); todo.append(y)
        assert c==self.c
        return c

random_updates=0
for seed in range(96):
    rng=random.Random(seed); H=History(1+seed%12)
    for step in range(128):
        choices=[a for a in (1,2,5) if a<=len(H.live)]
        a=rng.choice(choices); b={1:rng.choice((1,4)),2:6,5:9}[a]
        H.packet(rng.sample(sorted(H.live),a),b); random_updates+=1
    H.independent_components()

H=History(8)
positions={r:(0,10*r) for r in range(8)}
birth={r:None for r in range(8)}
owners={r:r for r in range(8)}
board={p:i for i,p in positions.items()}
mains=list(range(8)); spares=[None]*8; gens=[0]*8
consumed_ages=[]; max_edge=0; source_packets=[]; cycle_pairs=[]
KMAX=2048

def install(inputs, coords, k, r):
    global max_edge
    oldpos=[positions[i] for i in inputs]
    for i in inputs:
        assert owners[i]==r
        assert board.pop(positions[i])==i
        if birth[i] is not None:
            age=k-birth[i]; assert age==8; consumed_ages.append(age)
            assert ((-k)-(-birth[i]))%4==0
    assert len(set(coords))==len(coords)
    assert not(set(coords)&set(board))
    for p in oldpos:
        for q in coords:
            edge=max(abs(p[0]-q[0]),abs(p[1]-q[1])); assert edge<=4
            max_edge=max(max_edge,edge)
    out,p=H.packet(inputs,len(coords))
    for i,q in zip(out,coords):
        positions[i]=q; birth[i]=k; owners[i]=r; board[q]=i
    assert len(board)==len(H.live)
    return out,p

snapshots=[]
for k in range(KMAX):
    r=k%8; n=gens[r]; x=4*n; y=10*r
    if n:
        ox=x-4; a,b,c=spares[r]
        vout,vp=install([a,b],[(ox,y),(ox+1,y),(ox+2,y),(ox+3,y),
                               (ox,y+2),(ox+1,y+2)],k,r)
        cycle_pairs.append((source_packets[-8],a,vp,b))
        install([c],[(ox+2,y+2)],k,r)
        assert all((ox+j,y+1) not in board for j in range(3))
    out,p=install([mains[r]],[(x+4,y),(x,y+1),(x+1,y+1),(x+2,y+1)],k,r)
    source_packets.append(p)
    mains[r]=out[0]; spares[r]=out[1:]; gens[r]+=1
    K=k+1; helpers=max(K-8,0)
    assert len(board)==8+3*K+4*helpers
    assert H.beta==helpers and H.c==8
    # Current-cell bound at each finite completed main tick.
    radius=max(max(abs(q[0]),abs(q[1]-10*owners[i])) for q,i in board.items())
    assert radius<=K/2+4 and radius<=(2*K+13)//3
    if K in (1,8,9,32,128,512,2048):
        snapshots.append(dict(K=K,mass=len(board),beta=H.beta,radius=radius))
H.independent_components()
# Every non-tree block is exactly one distinct four-cycle; deleting one
# source-to-spare edge per helper leaves E=V-c and a connected forest per root.
assert len(cycle_pairs)==H.beta
for p,a,v,b in cycle_pairs:
    assert a in H.adj[p] and v in H.adj[a] and b in H.adj[v] and p in H.adj[b]
    H.adj[p].remove(a); H.adj[a].remove(p)
E2=sum(map(len,H.adj))//2
assert E2==len(H.adj)-8
H.independent_components()

out=dict(scope='Finite controls of abstract resource graph only; not literal masks or ant',
         random_histories=96,random_packet_updates=random_updates,
         aged_main_updates=KMAX,aged_packet_updates=H.packet_count,
         produced_inputs_checked=len(consumed_ages),all_produced_input_ages=8,
         maximum_all_input_edge=max_edge,cactus_four_cycles=len(cycle_pairs),
         snapshots=snapshots)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
