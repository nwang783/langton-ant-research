"""History-conditioned after-marker physical transitions and energy contexts.

Every actual orbit in H obeys one of these transitions.  Some graph transitions
are discarded because their full 149+macro word already has a contradictory
cell read.  For retained transitions, arbitrary unknown surrounding colours
give a superset of possible complete fields, suitable for rigorous energy
inequalities.
"""
from collections import Counter
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
DIRECTIONS=((0,1),(1,0),(0,-1),(-1,0))
NAMES={15:'C',18:'V',28:'U',64:'Q',74:'B'}

def trace(word):
    x=y=h=0;first={};last={};odd=set()
    for c in word:
        p=x,y
        assert last.get(p)!=c,('inconsistent word',word,p,c)
        first.setdefault(p,c);last[p]=c
        odd.symmetric_difference_update({p})
        h=(h+(1 if c=='R' else -1))%4
        dx,dy=DIRECTIONS[h];x+=dx;y+=dy
    return first,last,odd,(x,y,h)

def endpoint_colours(history):
    first,last,odd,(x,y,h)=trace(history)
    vx,vy=DIRECTIONS[h]
    def normalize(p):
        dx,dy=p[0]-x,p[1]-y
        return dx*vy-dy*vx,dx*vx+dy*vy
    return {normalize(p):(c=='R') for p,c in last.items()}

def main():
    raw=json.loads((HERE/'five_macro_actual_ports.json').read_text())
    ports=sorted({s for s,t,w in raw['edges']}|{t for s,t,w in raw['edges']})
    ids={s:i for i,s in enumerate(ports)}
    known=[endpoint_colours(s) for s in ports]
    words={w:trace(w) for s,t,w in raw['edges']}
    contexts=[];context_ids={};edges=[];discarded=[]
    for s,t,w in raw['edges']:
        sid,tid=ids[s],ids[t]
        fixed=known[sid].copy()
        first,last,toggled,end=words[w]
        conflict=[p for p,c in first.items() if p in fixed and fixed[p]!=(c=='L')]
        if conflict:
            discarded.append({'source':sid,'target':tid,'macro':NAMES[len(w)],'conflict':sorted(conflict)})
            continue
        fixed.update({p:c=='L' for p,c in first.items()})
        origins={(x-dx,y-dy) for x,y in toggled for dx in range(3) for dy in range(3)}
        relevant={(x+dx,y+dy) for x,y in origins for dx in range(3) for dy in range(3)}
        black=tuple(sorted(p for p,b in fixed.items() if p in relevant and b))
        white=tuple(sorted(p for p,b in fixed.items() if p in relevant and not b))
        key=(tuple(sorted(toggled)),black,white)
        if key not in context_ids:
            cid=len(contexts);context_ids[key]=cid
            contexts.append({'id':cid,'macro':NAMES[len(w)],'initial_black':black,'initial_white':white,'toggled':sorted(toggled),'end_pose':end})
        edges.append({'source':sid,'target':tid,'context':context_ids[key],'macro':NAMES[len(w)]})
    out={'convention':'Immediately after marker; normalized head at (0,0), heading north.',
         'marker':raw['marker'],'ports':ports,'contexts':contexts,'edges':edges,'discarded':discarded}
    (HERE/'conditioned_macro_contexts.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
    print({'ports':len(ports),'edges':len(edges),'discarded':len(discarded),'contexts':len(contexts),
           'contexts_by_macro':dict(Counter(c['macro'] for c in contexts)),
           'edges_by_macro':dict(Counter(e['macro'] for e in edges))})

if __name__=='__main__':main()
