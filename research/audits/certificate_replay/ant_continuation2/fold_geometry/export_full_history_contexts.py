"""Keep all 149-history colors for global max-plus domination checks.

The earlier additive-energy export intentionally dropped unchanged distant
colors.  Such dropping remains a sound relaxation for max-plus, but can lose
the unchanged pattern that dominates a newly created local pattern.  This
export retains every known history cell, while still leaving all other cells
arbitrary.
"""
from pathlib import Path
import json
import sys
from collections import Counter

ROOT=Path(__file__).resolve().parents[2]
PRIOR=ROOT/'ant_continuation/factor_language'
sys.path.insert(0,str(PRIOR))
from conditioned_macro_contexts import trace,endpoint_colours,NAMES


def main():
    raw=json.loads((PRIOR/'five_macro_actual_ports.json').read_text())
    ports=sorted({s for s,t,w in raw['edges']}|{t for s,t,w in raw['edges']})
    ids={s:i for i,s in enumerate(ports)}
    known={s:endpoint_colours(s) for s in ports}
    words={w:trace(w) for s,t,w in raw['edges']}
    contexts=[];lookup={};edges=[];discarded=[]
    for s,t,w in raw['edges']:
        first,last,odd,end=words[w]
        fixed=known[s].copy()
        conflict=[p for p,c in first.items() if p in fixed and fixed[p]!=(c=='L')]
        if conflict:
            discarded.append({'source':ids[s],'target':ids[t],'macro':NAMES[len(w)],'conflict':sorted(conflict)})
            continue
        fixed.update({p:c=='L' for p,c in first.items()})
        black=tuple(sorted(p for p,b in fixed.items() if b))
        white=tuple(sorted(p for p,b in fixed.items() if not b))
        key=(NAMES[len(w)],black,white)
        if key not in lookup:
            cid=len(contexts);lookup[key]=cid
            contexts.append({'id':cid,'macro':NAMES[len(w)],'initial_black':black,'initial_white':white,
                             'toggled':sorted(odd),'end_pose':end})
        edges.append({'source':ids[s],'target':ids[t],'context':lookup[key],'macro':NAMES[len(w)]})
    out={'convention':'Immediately after marker; full normalized 149-history colors retained.',
         'marker':raw['marker'],'ports':ports,'contexts':contexts,'edges':edges,'discarded':discarded}
    path=Path(__file__).with_name('full_history_macro_contexts.json')
    path.write_text(json.dumps(out,separators=(',',':'))+'\n')
    print({'ports':len(ports),'contexts':len(contexts),'edges':len(edges),'discarded':len(discarded),
           'contexts_by_macro':dict(Counter(c['macro'] for c in contexts))})


if __name__=='__main__':main()
