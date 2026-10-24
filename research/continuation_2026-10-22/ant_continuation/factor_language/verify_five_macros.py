"""Exact marker-return coverage on the unquotiented 149-history SCC.

Run no_adjacent_defects.cpp and no_pair_graph.py first.  This check avoids
the mixed-history quotient port and does not depend on quotient minimization.
Histories end immediately AFTER a complete marker.  An edge word appended to
one such history therefore has the form rest+marker.  Physical footprint
blocks instead begin BEFORE the marker and are marker+rest.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
MARKER='LLLLRLRRRRLR'
NAMES={15:'C',18:'V',28:'U',64:'Q',74:'B'}

def main():
    lines=(HERE/'no_pair_large_scc.txt').read_text().splitlines()
    outgoing={w:cs for w,cs in map(str.split,lines)}
    assert len(outgoing)==34712
    adj={w:[(c,w[1:]+c) for c in cs] for w,cs in outgoing.items()}
    assert all(v in adj for edges in adj.values() for _,v in edges)
    ports={w for w in adj if w.endswith(MARKER)}
    assert len(ports)==995
    nonports=set(adj)-ports
    indeg={w:0 for w in nonports}
    for w in nonports:
        for _,v in adj[w]:
            if v in nonports:indeg[v]+=1
    queue=[w for w,d in indeg.items() if not d]
    topo=[]
    while queue:
        w=queue.pop();topo.append(w)
        for _,v in adj[w]:
            if v in nonports:
                indeg[v]-=1
                if not indeg[v]:queue.append(v)
    assert len(topo)==len(nonports),'A cycle avoids the marker'
    suffixes={}
    for w in reversed(topo):
        out=[]
        for c,v in adj[w]:
            if v in ports:out.append((v,c))
            else:out.extend((z,c+s) for z,s in suffixes[v])
        suffixes[w]=out
    edges=[]
    for w in sorted(ports):
        for c,v in adj[w]:
            if v in ports:edges.append((w,v,c))
            else:edges.extend((w,z,c+s) for z,s in suffixes[v])
    words=sorted({s for _,_,s in edges},key=lambda s:(len(s),s))
    assert len(words)==5
    assert [len(s) for s in words]==[15,18,28,64,74]
    assert all(s.endswith(MARKER) for s in words)
    assert max(map(len,suffixes.values()),default=0)>0
    footprints=json.loads((HERE/'five_macro_footprints.json').read_text())
    blocks={NAMES[len(s)]:MARKER+s[:-len(MARKER)] for s in words}
    assert blocks=={k:v['word'] for k,v in footprints.items()}
    prior=json.loads((HERE/'no_pair_port_words.json').read_text())
    assert set(prior['words'])==set(words)
    report={
        'history_length':149,'vertices':len(adj),'internal_edges':sum(map(len,adj.values())),
        'actual_marker_ports':len(ports),'nonport_vertices':len(nonports),
        'nonport_graph_is_acyclic':True,'actual_port_edges':len(edges),
        'maximum_marker_return_length':max(map(len,words)),
        'return_word_counts':dict(Counter(NAMES[len(s)] for _,_,s in edges)),
        'after_marker_words':{NAMES[len(s)]:s for s in words},
        'before_marker_words':blocks,
        'source_scc_sha256':hashlib.sha256((HERE/'no_pair_large_scc.txt').read_bytes()).hexdigest(),
        'status':'Exact finite graph reduction; does not exclude infinite folded physical paths.'
    }
    (HERE/'five_macro_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    (HERE/'five_macro_actual_ports.json').write_text(json.dumps({'marker':MARKER,'edges':edges},separators=(',',':'))+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
