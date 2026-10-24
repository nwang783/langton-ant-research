from pathlib import Path
from collections import defaultdict,Counter
import json

def scc(adj,rev):
    n=len(adj);seen=bytearray(n);order=[]
    for root in range(n):
        if seen[root]:continue
        seen[root]=1;stack=[(root,0)]
        while stack:
            v,i=stack[-1]
            if i==len(adj[v]):order.append(v);stack.pop();continue
            w=adj[v][i];stack[-1]=(v,i+1)
            if not seen[w]:seen[w]=1;stack.append((w,0))
    component=[-1]*n;cs=[]
    for root in reversed(order):
        if component[root]>=0:continue
        ci=len(cs);group=[];stack=[root];component[root]=ci
        while stack:
            v=stack.pop();group.append(v)
            for w in rev[v]:
                if component[w]<0:component[w]=ci;stack.append(w)
        cs.append(group)
    return component,cs

def main():
    p=Path(__file__).with_name('no_pair_words150.txt')
    ws=[int(w.strip().replace('L','0').replace('R','1'),2) for w in p.open()]
    mask=(1<<149)-1
    vs=sorted(set(w>>1 for w in ws)|set(w&mask for w in ws));ids={v:i for i,v in enumerate(vs)}
    adj=[[]for v in vs];rev=[[]for v in vs]
    for w in ws:
        a,b=ids[w>>1],ids[w&mask];adj[a].append(b);rev[b].append(a)
    c,cs=scc(adj,rev)
    cyc=[]
    for i,g in enumerate(cs):
        inner=sum(c[v]==i for u in g for v in adj[u])
        if inner:
            info={'size':len(g),'edges':inner,'branches':sum(sum(c[v]==i for v in adj[u])>1 for u in g)}
            if inner==len(g):
                start=g[0];v=start;word=[]
                while True:
                    v=next(w for w in adj[v] if c[w]==i)
                    word.append('R' if vs[v]&1 else 'L')
                    if v==start:break
                info['word']=''.join(word)
            cyc.append(info)
    print('words',len(ws),'vertices',len(vs),'cyclic',cyc,flush=True)
    big=max(cs,key=len);inside=set(big)
    outset={u:{vs[v]&1:v for v in adj[u] if v in inside} for u in big}
    Path(__file__).with_name('no_pair_large_scc.txt').write_text(''.join(format(vs[u],'0149b').replace('0','L').replace('1','R')+' '+''.join('R'if b else'L'for b in sorted(outset[u]))+'\n'for u in sorted(big)))
    group={u:0 for u in big}
    oldn=1
    for iteration in range(500):
        sig={u:tuple(group[outset[u][b]] if b in outset[u] else -1 for b in (0,1))for u in big}
        uniq={s:i for i,s in enumerate(sorted(set(sig.values())))}
        newgroup={u:uniq[sig[u]]for u in big}
        ng=len(uniq)
        if ng==oldn:
            group=newgroup;break
        group=newgroup;oldn=ng
    q={}
    for u in big:
        out={('R'if b else'L'):group[v]for b,v in outset[u].items()}
        if group[u] in q:assert q[group[u]]==out
        q[group[u]]=out
    marker='LLLLRLRRRRLR'
    mb=int(marker.replace('L','0').replace('R','1'),2)
    actual_ports={u for u in big if (vs[u]&4095)==mb}
    nonports=set(big)-actual_ports
    indeg={u:0 for u in nonports}
    for u in nonports:
        for v in outset[u].values():
            if v in nonports:indeg[v]+=1
    queue=[u for u in nonports if indeg[u]==0];topo=[]
    while queue:
        u=queue.pop();topo.append(u)
        for v in outset[u].values():
            if v in nonports:
                indeg[v]-=1
                if indeg[v]==0:queue.append(v)
    assert len(topo)==len(nonports),('cycle avoids marker',len(nonports)-len(topo))
    length={}
    for u in reversed(topo):length[u]=1+max((length[v] for v in outset[u].values()if v in nonports),default=0)
    marker_gap=max(length.values())+1
    tails=defaultdict(set)
    for u in big:tails[group[u]].add(format(vs[u]&((1<<len(marker))-1),'012b').replace('0','L').replace('1','R'))
    ports=[u for u,t in tails.items()if marker in t]
    port_mixed=[u for u in ports if len(tails[u])>1]
    from analyze_language import highway_word,cyclic_factors
    fs=cyclic_factors(highway_word(),10)
    badflags=defaultdict(set)
    for u in big:
        for b,v in outset[u].items():
            f=format(((vs[u]&511)<<1)+b,'010b').replace('0','L').replace('1','R')
            badflags[group[u],('R'if b else'L'),group[v]].add(f not in fs)
    badedges=[list(e) for e,flags in badflags.items()if True in flags]
    incoming=Counter(v for out in q.values()for v in out.values())
    junction={u for u,out in q.items() if len(out)!=1 or incoming[u]!=1}
    macros=[]
    for u in sorted(junction):
        for ch,v in q[u].items():
            w=ch
            while v not in junction:
                ch,v=next(iter(q[v].items()));w+=ch
            macros.append((u,v,w))
    print('quotient states',len(q),'rounds',iteration,'junctions',len(junction),'macros',macros,flush=True)
    Path(__file__).with_name('no_pair_quotient.json').write_text(json.dumps({'states':len(q),'rounds':iteration,'quotient':q,'macros':macros,'bad_edges':badedges,'mixed_flags':sum(len(a)>1 for a in badflags.values()),'marker':marker,'ports':ports,'port_mixed':port_mixed,'actual_port_count':len(actual_ports),'maximum_marker_gap':marker_gap},indent=2))
    Path(__file__).with_name('no_pair_graph_result.json').write_text(json.dumps({'words':len(ws),'vertices':len(vs),'cyclic':cyc},indent=2))

if __name__=='__main__':main()
