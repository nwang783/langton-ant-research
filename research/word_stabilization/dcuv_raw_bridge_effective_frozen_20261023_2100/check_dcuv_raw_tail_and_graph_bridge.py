"""Fixed literal/graph checks, not a trajectory-prefix search.

The mass-budget enumeration below is a reference effective definition.  It is
NOT called by this script. Its totality is a consequence of the separately
proved raw-language exclusion and the analytic Konig argument.
"""
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[1]
G=json.loads((ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
D,V,U=(G[i]['word'] for i in (0,4,7))
C=G[1]['word'][len(D):]
M='LLLLRLRRRRL'
ALPHABET=(D,C,V,U)
DIRS=((0,1),(1,0),(0,-1),(-1,0))
def fresh_trace(word):
    p=(0,0);h=0;last={};firstL=[]
    for i,c in enumerate(word):
        if last.get(p)==c:
            return {'feasible':False,'conflict_read':i,'cell':list(p),'turn':c}
        if p not in last and c=='L':firstL.append(p)
        last[p]=c;h=(h+(1 if c=='R' else -1))%4
        a,b=DIRS[h];p=(p[0]+a,p[1]+b)
    return {'feasible':True,'endpoint':[*p,h],'first_L_count':len(firstL)}

def mass_only_lifetime(m):
    """Total by the raw-tail theorem + Konig; intentionally never run here.

    Returns the maximum raw length of any physically consistent concatenation
    of D,C,V,U requiring at most m initially black cells. The stack represents
    the complete four-ary prefix tree, without a depth/node cap.
    """
    if not isinstance(m,int) or m<0:raise ValueError('m must be a nonnegative integer')
    maximum=0
    stack=[('',0)]
    while stack:
        word,length=stack.pop()
        maximum=max(maximum,length)
        for atom in ALPHABET:
            child=word+atom
            r=fresh_trace(child)
            if r['feasible'] and r['first_L_count']<=m:
                stack.append((child,length+len(atom)))
    return maximum

def cyclic_components(n,edges):
    a=[[]for _ in range(n)];rev=[[]for _ in range(n)]
    for x,t,y in edges:a[x].append(y);rev[y].append(x)
    seen=set();order=[]
    def dfs(x):
        seen.add(x)
        for y in a[x]:
            if y not in seen:dfs(y)
        order.append(x)
    for x in range(n):
        if x not in seen:dfs(x)
    seen=set();comps=[]
    def back(x,c):
        seen.add(x);c.append(x)
        for y in rev[x]:
            if y not in seen:back(y,c)
    for x in order[::-1]:
        if x not in seen:
            c=[];back(x,c);s=set(c)
            es=[e for e in edges if e[0]in s and e[2]in s]
            if len(c)>1 or any(x==y for x,t,y in es):
                comps.append({'vertices':len(c),'edges':len(es),'labels':sorted({t for x,t,y in es})})
    return sorted(comps,key=lambda r:-r['vertices'])

def main():
    assert [len(w)for w in ALPHABET]==[10,15,18,28]
    for i,(a,k)in enumerate(((D,0),(D,1),(D,2),(D,3),(V,0),(V,1),(V,2),(U,0),(U,1),(U,2))):
        assert a+C*k==G[i]['word']
    fixed={name:fresh_trace(word)for name,word in {
        'C5_raw':C*5,'C4_marker':C*4+M,'DC4_marker':D+C*4+M,
        'VC3_marker':V+C*3+M,'UC3_marker':U+C*3+M}.items()}
    assert all(not r['feasible']for r in fixed.values())
    ten={g['name']:g['word']for g in G}
    boundary={}
    for n,w in ten.items():
        boundary['DCC_successor_'+n]=fresh_trace(ten['DCC']+w+M)
        boundary['DCCC_predecessor_'+n]=fresh_trace(w+ten['DCCC']+M)
    assert len(boundary)==20 and all(not r['feasible']for r in boundary.values())
    path=ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
    graph=json.loads(path.read_text());es=graph['quotient_edges'];n=graph['classes']
    assert [g['word']for g in graph['macro_words'][:4]]==list(ALPHABET)
    scc={k:cyclic_components(n,ee)for k,ee in {
        'all':es,'DCUV_edges':[e for e in es if e[1]<4],'FQB_edges':[e for e in es if e[1]>=4]}.items()}
    assert scc=={'all':[{'vertices':214,'edges':993,'labels':list(range(7))}],
                 'DCUV_edges':[{'vertices':93,'edges':417,'labels':list(range(4))}],
                 'FQB_edges':[]}
    out={'status':'PASS fixed literal raw-tail boundary and exact existing-graph diagnostic; no mass-budget tree evaluated',
         'alphabet_lengths':[len(w)for w in ALPHABET],'fixed_long_C_conflicts':fixed,
         'twenty_boundary_conflicts':boundary,'source_graph_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
         'cyclic_components':scc,
         'not_claimed':'No new global K-language coverage, SCC deletion, finite foreign count, or universal capture.'}
    (Path(__file__).with_suffix('.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'SCCs':scc}))
if __name__=='__main__':main()
