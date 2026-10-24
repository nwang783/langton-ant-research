#!/usr/bin/env python3
"""Finite controls for the explicitly nonliteral U-archive relaxation."""
import json
from pathlib import Path
N=2048
parent=list(range(8)); adj=[set() for _ in range(8)]; cc=8; edges=0
positions={r:(0,10*r) for r in range(8)}; board={p:r for r,p in positions.items()}
born={r:None for r in range(8)}; root={r:r for r in range(8)}
main=list(range(8)); spares=[None]*8; archive=[None]*8; gen=[0]*8
v=u=d=0; agechecks=0; maxedge=0; packets=0; snapshots=[]
def find(a):
    while a!=parent[a]: parent[a]=parent[parent[a]]; a=parent[a]
    return a
def vertex():
    global cc
    a=len(parent); parent.append(a); adj.append(set()); cc+=1; return a
def link(a,b):
    global cc,edges
    assert b not in adj[a]; adj[a].add(b); adj[b].add(a); edges+=1
    a,b=find(a),find(b)
    if a!=b: parent[b]=a; cc-=1

def update(inputs,coords,k,r):
    global agechecks,maxedge,packets
    oldbeta=edges-len(parent)+cc
    groups=len({find(i) for i in inputs})
    assert groups==1
    for i in inputs:
        assert root[i]==r and board.pop(positions[i])==i
        if born[i] is not None:
            assert k-born[i]==8; agechecks+=1
            assert ((-k)-(-born[i]))%4==0
    assert len(set(coords))==len(coords) and not(set(coords)&set(board))
    for i in inputs:
        for q in coords:
            p=positions[i]; dist=max(abs(p[0]-q[0]),abs(p[1]-q[1]))
            assert dist<=4; maxedge=max(maxedge,dist)
    packet=vertex()
    for i in inputs: link(i,packet)
    outputs=[]
    for q in coords:
        i=vertex(); outputs.append(i); link(packet,i)
        positions[i]=q; root[i]=r; born[i]=k; board[q]=i
    assert edges-len(parent)+cc-oldbeta==len(inputs)-1
    packets+=1
    return outputs

for k in range(N):
    r=k%8; n=gen[r]; x=4*n; y=10*r
    if n:
        bx=x-4; a,b,c=spares[r]
        if n==1:
            out=update([a,b],[(bx,y+2),(bx+1,y+2),(bx+2,y+2),
                              (bx+3,y+2),(bx,y+3),(bx+3,y+3)],k,r)
            archive[r]=[out[3],out[5]]; v+=1
            update([c],[(bx+2,y+3)],k,r); d+=1
        else:
            assert [positions[i] for i in archive[r]]==[(bx-1,y+2),(bx-1,y+3)]
            out=update([a,b,c]+archive[r],
                       [(bx+i,y+2) for i in range(4)]+
                       [(bx+i,y+3) for i in range(4)]+[(bx,y+4)],k,r)
            archive[r]=[out[3],out[7]]; u+=1
        assert all((bx+i,y+1) not in board for i in range(3))
    out=update([main[r]],[(x+4,y),(x,y+1),(x+1,y+1),(x+2,y+1)],k,r)
    main[r]=out[0]; spares[r]=out[1:]; gen[r]+=1
    K=k+1
    assert v==min(max(K-8,0),8) and u==max(K-16,0) and d==v
    mass=len(board); beta=edges-len(parent)+cc
    assert mass==8+3*K+4*(v+u) and beta==v+4*u and cc==8
    rad=max(max(abs(p[0]),abs(p[1]-10*root[i])) for p,i in board.items())
    assert rad<=K/2+4 and rad<=(2*K+13)//3
    if K in (1,8,9,16,17,32,128,512,2048):
        snapshots.append(dict(K=K,mass=mass,v=v,u=u,beta=beta,radius=rad))
# Independent component reconstruction from every retained historical vertex.
seen=set(); components=0
for i in range(len(adj)):
    if i in seen: continue
    seen.add(i); todo=[i]; components+=1
    while todo:
        a=todo.pop()
        for b in adj[a]:
            if b not in seen: seen.add(b); todo.append(b)
assert components==8
result=dict(scope='Abstract counts/ages/topology only, not literal masks or ant',
            main_updates=N,packet_updates=packets,V=v,U=u,D=d,beta=beta,
            all_produced_input_ages=8,produced_inputs_checked=agechecks,
            maximum_all_input_edge=maxedge,historical_vertices=len(adj),
            historical_edges=edges,components=components,snapshots=snapshots)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
