import json
from pathlib import Path
from active_loops import step

def edge(z):
    x,y=z
    if (x+y)%2==0:return (x,y-1),(x-1,y)
    return (x-1,y-1),(x,y)

def components(B):
    d={}
    def find(a):
        if a not in d:d[a]=a
        while d[a]!=a:d[a]=d[d[a]];a=d[a]
        return a
    for z in B:
        u,v=edge(z);d[find(u)]=find(v)
    out={}
    for z in B:
        u,v=edge(z);r=find(u)
        out.setdefault(r,{'cells':set(),'vertices':set()})
        out[r]['cells'].add(z);out[r]['vertices'].update((u,v))
    return list(out.values())

OFFSETS=((-1,-1),(-1,0),(0,0),(0,-1))
def run():
    p=(0,0);h=3;B=set();stats=[];snapshots={}
    for t in range(11209):
        cs=components(B)
        v=(p[0]+OFFSETS[h][0],p[1]+OFFSETS[h][1])
        active=next((c for c in cs if v in c['vertices']),{'cells':set(),'vertices':{v}})
        stats.append({'t':t,'active_edges':len(active['cells']),
                      'active_vertices':len(active['vertices']),
                      'active_beta':len(active['cells'])-len(active['vertices'])+1})
        if t in (11000,11104):snapshots[t]=cs
        p,h=step(p,h,B,True)
    old={frozenset(c['cells']) for c in snapshots[11000]}
    new=[c for c in snapshots[11104] if frozenset(c['cells']) not in old]
    changes=[{'cells':sorted(c['cells']),'vertices':sorted(c['vertices']),
              'beta':len(c['cells'])-len(c['vertices'])+1} for c in new]
    here=Path(__file__).resolve().parent
    (here/'component_stats_blank.json').write_text(json.dumps(stats))
    (here/'standard_component_changes.json').write_text(json.dumps(changes,indent=2))
    print(json.dumps({'max_active_edges':max(r['active_edges'] for r in stats),
      'max_active_beta':max(r['active_beta'] for r in stats),
      'standard_beta':[r['active_beta'] for r in stats[11000:11104]],
      'new_components':changes},indent=2))

if __name__=='__main__':run()
