"""Independent physical ant simulator with exact edge-token ancestry.
N,E,S,W headings. Parity sector (0,0),N. No recovered simulator import.
"""
from dataclasses import dataclass
from collections import Counter
import json
from pathlib import Path
DIR=((0,1),(1,0),(0,-1),(-1,0))
OFF=((0,-1),(-1,-1),(-1,0),(0,0))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def edge(q):
    x,y=q
    return ((x,y-1),(x-1,y)) if (x+y)%2==0 else ((x-1,y-1),(x,y))
def simulate(n,initial=(),p=(0,0),h=0):
    B=set(initial); initial=tuple(sorted(B)); tokens={q:-(i+1) for i,q in enumerate(initial)}
    # The initial cursor node is a root distinct from seed-edge roots.
    nodes=[dict(id=0,time=0,pos=add(p,OFF[h]),parent=None,incoming=None,r=0,children=[])]
    reads=[]; node=0
    for t in range(n):
        v=add(p,OFF[h]); c=p in B; oldp=p
        assert v==nodes[node]['pos']
        if c:
            B.remove(p); parent=tokens.pop(p); h=(h-1)%4
        else:
            B.add(p);tokens[p]=node; nodes[node]['r']+=1;h=(h+1)%4
        p=add(p,DIR[h]);w=add(p,OFF[h])
        reads.append((oldp,c,node))
        if c:
            assert v!=w and set((v,w))==set(edge(oldp))
            new=len(nodes);nodes.append(dict(id=new,time=t+1,pos=w,parent=parent,incoming=oldp,r=0,children=[]))
            if parent>=0:
                nodes[parent]['children'].append(new)
                assert w==nodes[parent]['pos'] or w in edge(oldp)
                assert nodes[parent]['pos'] in edge(oldp)
            node=new
        else:assert v==w
    return dict(nodes=nodes,reads=reads,black=B,tokens=tokens,initial=initial,p=p,h=h)

def main():
    d=simulate(25000); nodes=d['nodes']; reads=d['reads']
    # Find reliable interior standard window using exact turnword period, not a capture assertion.
    w=''.join('L' if c else 'R' for p,c,node in reads)
    assert w[12000:24896]==w[12104:25000]
    lo=15000;hi=24000; phases={}; phase_nodes={}
    for a in nodes:
        if lo<=a['time']<hi:
            parent=nodes[a['parent']]; phase=a['time']%104
            record=(parent['time']%104,a['time']-parent['time'],a['r'], tuple(a['pos'][i]-parent['pos'][i] for i in (0,1)))
            assert phase not in phases or phases[phase]==record
            phases[phase]=record;phase_nodes[phase]=a['id']
    assert len(phases)==46
    cycles=[];done=set()
    for start in sorted(phases):
        if start in done:continue
        path=[];seen={};s=start
        while s not in done and s not in seen:
            seen[s]=len(path);path.append(s);s=phases[s][0]
        if s in seen:
            cyc=path[seen[s]:]; cycles.append(dict(phases=cyc,period_winding=sum(phases[q][1] for q in cyc)//104, total_delay=sum(phases[q][1] for q in cyc)))
        done.update(path)
    stats=dict(nodes=len(nodes),r_counts=dict(Counter(a['r'] for a in nodes[:-1])),max_consumed_token_age=max(t-nodes[reads[t][2]]['time'] for t in [] ) if False else None,
        standard_node_phases=len(phases),standard_parent_cycles=cycles,standard_phase_table=phases)
    Path(__file__).with_name('blank_ancestry.json').write_text(json.dumps(stats,indent=2))
    print(json.dumps({k:v for k,v in stats.items() if k!='standard_phase_table'},indent=2))
if __name__=='__main__':main()
