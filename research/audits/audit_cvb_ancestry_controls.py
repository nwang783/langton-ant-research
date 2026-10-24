"""Independent literal token accounting controls, not an unbounded-word proof."""
from itertools import product
from pathlib import Path
import json
ROOT=Path('/workspace/shared/langton')
DATA=json.loads((ROOT/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json').read_text())
WORDS={k:DATA[k]['word'] for k in 'CVB'}
DIR=((0,1),(1,0),(0,-1),(-1,0))

def genealogy(macros):
    colors={};tokens={};parents=[None];depth=[0];writes=[0];meta=[('entry',0)]
    p=(0,0);h=0;node=0;initial_black=set()
    for m in macros:
        for phase,letter in enumerate(WORDS[m]):
            black=letter=='L'
            if p not in colors:
                colors[p]=black
                if black:initial_black.add(p)
            if colors[p]!=black:return None
            colors[p]=not black
            if black:
                owner=tokens.pop(p,None)
                node=len(depth);parents.append(owner)
                depth.append(0 if owner is None else depth[owner]+1)
                writes.append(0);meta.append((m,phase+1))
            else:
                assert p not in tokens
                tokens[p]=node;writes[node]+=1
            h=(h+(1 if letter=='R' else -1))%4
            p=(p[0]+DIR[h][0],p[1]+DIR[h][1])
    maxnode=max(depth);maxpositive=max((d for d,r in zip(depth,writes) if r),default=0)
    maxbud=max((depth[v]+1 for v in tokens.values()),default=0)
    deepest=depth.index(maxnode);chain=[]
    while deepest is not None:
        chain.append((meta[deepest],depth[deepest]));deepest=parents[deepest]
    return dict(max_node=maxnode,max_positive=maxpositive,max_boundary_bud=maxbud,
                deepest_chain=list(reversed(chain)),entry_black_mass=len(initial_black))

feasible=0;maxima=[0,0,0]
for length in range(9):
    for word in product('CVB',repeat=length):
        f=genealogy(word)
        if f is None:continue
        feasible+=1
        values=[f[k] for k in ('max_node','max_positive','max_boundary_bud')]
        assert values[0]<=8 and values[1]<=7 and values[2]<=8,(word,f)
        maxima=[max(a,b) for a,b in zip(maxima,values)]
witness=genealogy('CCCVV');assert witness and witness['max_node']==8
assert genealogy('B')['max_positive']==3 and genealogy('CB')['max_positive']==4
out=dict(status='PASS: independent literal cut-forest controls',
         maximum_tested_macro_length=8,feasible_words=feasible,
         max_node_positive_bud=maxima,sharp_witness=witness,
         scope='Finite controls only; unbounded theorem uses the audited local closures and analytic type argument.')
(ROOT/'audits/cvb_ancestry_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
