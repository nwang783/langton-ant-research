"""Exhaustive local-energy separation by binary variable elimination.

For each fixed physical macro, all cells it reads have fixed initial colours.
Only cells outside that read footprint are free. Every changed 3x3 patch is a
factor in these free bits. Min-fill variable elimination computes the exact
maximum of E(after)-E(before) over all 2^n assignments, rather than sampling.

For these five macros the largest combined factor has only twelve bits.
Floating weights give a floating computation of the exact finite optimization
problem. Integer weights make all arithmetic exact (provided int64 does not
overflow); rational discovery weights should be scaled to integers before a
proof claim is made.
"""
from pathlib import Path
import argparse
import json
import numpy as np

HERE=Path(__file__).resolve().parent
DATA=json.loads((HERE/'five_macro_footprints.json').read_text())

def rotate(p):
    return sum(((p>>(x+3*y))&1)<<((2-y)+3*x) for y in range(3) for x in range(3))

def canonical(p):
    out=p
    for _ in range(3):p=rotate(p);out=min(out,p)
    return out

CANON=[canonical(p) for p in range(512)]

def canonical_sector(phase,p):
    """phase 0 is +; phase 1 is -. A quarter rotation flips the phase."""
    out=(phase<<9)|p
    for _ in range(3):
        phase^=1;p=rotate(p)
        out=min(out,(phase<<9)|p)
    return out

SECTOR_CANON=[canonical_sector(phase,p) for phase in (0,1) for p in range(512)]

class MacroProblem:
    def __init__(self,name,initial_black=None,initial_white=None,toggled=None,extra_cells=()):
        self.name=name
        self.sector_covariant=False
        if initial_black is None:
            d=DATA[name]
            initial_black=d['first_L'];initial_white=d['first_R'];toggled=d['odd_visits']
        self.initial=set(map(tuple,initial_black))
        white=set(map(tuple,initial_white))
        assert not (self.initial&white)
        visited=self.initial|white
        self.toggled=set(map(tuple,toggled))
        assert self.toggled<=visited
        self.origins=sorted({(x-dx,y-dy) for x,y in self.toggled for dy in range(3) for dx in range(3)})
        self.unknown=sorted(({(x+dx,y+dy) for x,y in self.origins for dy in range(3) for dx in range(3)}|set(extra_cells))-visited)
        uid={p:i for i,p in enumerate(self.unknown)}
        self.factors=[]
        for x,y in self.origins:
            cells=[(x+dx,y+dy) for dy in range(3) for dx in range(3)]
            scope=tuple(sorted(uid[p] for p in cells if p in uid))
            indices={v:i for i,v in enumerate(scope)}
            fixed=sum((p in self.initial)<<bit for bit,p in enumerate(cells))
            change=sum((p in self.toggled)<<bit for bit,p in enumerate(cells))
            before=np.empty((2,)*len(scope),dtype=np.int16)
            for assignment in np.ndindex(before.shape):
                p=fixed
                for bit,cell in enumerate(cells):
                    if cell in uid:p|=assignment[indices[uid[cell]]]<<bit
                before[assignment]=p
            self.factors.append((scope,before,before^change))
        adj={v:set() for v in range(len(self.unknown))}
        for scope,_,_ in self.factors:
            for v in scope:adj[v].update(set(scope)-{v})
        self.order=[];self.width=0
        while adj:
            def cost(v):
                ns=adj[v]
                return sum(b not in adj[a] for a in ns for b in ns if a<b),len(ns),v
            v=min(adj,key=cost);ns=adj.pop(v)
            self.order.append(v);self.width=max(self.width,len(ns))
            for a in ns:adj[a].discard(v);adj[a].update(ns-{a})

    def maximize(self,weights,unary=None,constant=0):
        # Keys are canonical 3x3 pattern integers. Missing weights are zero.
        unary=unary or {}
        integral=all(isinstance(w,(int,np.integer)) for w in list(weights.values())+list(unary.values())+[constant])
        dtype=np.int64 if integral else np.float64
        if self.sector_covariant:
            full=np.array([weights.get(c,0) for c in SECTOR_CANON],dtype=dtype).reshape(2,512)
        else:
            full=np.array([[weights.get(CANON[p],0) for p in range(512)]]*2,dtype=dtype)
        if integral:
            assert int(np.max(np.abs(full),initial=0))*len(self.origins)+sum(abs(w) for w in unary.values())+abs(constant)<2**62
        factors=[(scope,full[(x+y)&1,after]-full[(x+y)&1,before])
                 for (x,y),(scope,before,after) in zip(self.origins,self.factors)]
        uindex={p:i for i,p in enumerate(self.unknown)}
        fixed=constant
        for p,a in unary.items():
            if p in uindex:factors.append(((uindex[p],),np.array([0,a],dtype=dtype)))
            elif p in self.initial:fixed+=a
        factors.append(((),np.array(fixed,dtype=dtype)))
        decisions=[]
        for v in self.order:
            active=[f for f in factors if v in f[0]]
            factors=[f for f in factors if v not in f[0]]
            if not active:
                decisions.append((v,(),np.array(0)))
                continue
            scope=tuple(sorted({u for s,_ in active for u in s}))
            combined=np.zeros((2,)*len(scope),dtype=dtype)
            for s,table in active:
                combined+=table.reshape(tuple(2 if u in s else 1 for u in scope))
            axis=scope.index(v);remaining=scope[:axis]+scope[axis+1:]
            decisions.append((v,remaining,np.argmax(combined,axis=axis)))
            factors.append((remaining,np.max(combined,axis=axis)))
        value=sum(table.item() for scope,table in factors)
        assert all(not scope for scope,_ in factors)
        assignment={}
        for v,scope,choices in reversed(decisions):
            assignment[v]=int(choices[tuple(assignment[u] for u in scope)])
        outside={p for i,p in enumerate(self.unknown) if assignment[i]}
        before=self.initial|outside;after=before^self.toggled
        direct=constant+sum(a for p,a in unary.items() if p in before)
        for x,y in self.origins:
            p=sum(((x+dx,y+dy) in before)<<(dx+3*dy) for dy in range(3) for dx in range(3))
            q=sum(((x+dx,y+dy) in after)<<(dx+3*dy) for dy in range(3) for dx in range(3))
            direct+=full[(x+y)&1,q].item()-full[(x+y)&1,p].item()
        assert abs(direct-value)<1e-7*(1+abs(value)),(self.name,value,direct)
        return {'macro':self.name,'unknown_cells':len(self.unknown),
                'affected_patches':len(self.origins),'elimination_width':self.width,
                'arithmetic':'int64' if integral else 'float64',
                'maximum_energy_change':value,'outside_black':sorted(outside)}

class ContextProblem(MacroProblem):
    def __init__(self,context):
        super().__init__(str(context['id']),context['initial_black'],
                         context['initial_white'],context['toggled'])

class SectorContextProblem(ContextProblem):
    def __init__(self,context):
        super().__init__(context)
        self.sector_covariant=True

def rotate_point(p,h):
    x,y=p
    return ((x,y),(y,-x),(-x,-y),(-y,x))[h]

class HeadContextProblem(MacroProblem):
    """Pattern energy plus a bounded signed potential around the ant's head.

    head_weights maps relative local coordinates to coefficients. Its change
    adds only unary factors. Unknown extra cells outside the former context
    remain arbitrary, which safely enlarges the set of physical contexts.
    """
    def __init__(self,context,radius=4,sector=True):
        self.head_sites=[(x,y) for x in range(-radius,radius+1) for y in range(-radius,radius+1)]
        self.end_pose=tuple(context['end_pose'])
        x,y,h=self.end_pose
        self.after_sites={p:(x+rotate_point(p,h)[0],y+rotate_point(p,h)[1]) for p in self.head_sites}
        extra=set(self.head_sites)|set(self.after_sites.values())
        super().__init__(str(context['id']),context['initial_black'],context['initial_white'],context['toggled'],extra)
        self.sector_covariant=sector

    def head_row(self,outside):
        before=self.initial|set(map(tuple,outside));after=before^self.toggled
        return {p:int(self.after_sites[p] in after)-int(p in before) for p in self.head_sites}

    def maximize(self,weights,head_weights=None):
        unary={};constant=0
        for p,a in (head_weights or {}).items():
            assert p in self.after_sites
            unary[p]=unary.get(p,0)-a
            q=self.after_sites[p]
            if q in self.toggled:
                constant+=a;unary[q]=unary.get(q,0)-a
            else:unary[q]=unary.get(q,0)+a
        return super().maximize(weights,unary,constant)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('weights',type=Path)
    p.add_argument('--output',type=Path,default=HERE/'exact_local_energy_result.json')
    args=p.parse_args()
    raw=json.loads(args.weights.read_text())
    weights={int(k):v for k,v in raw['energy'].items()}
    assert weights.get(0,0)==0 and all(v>=0 for v in weights.values())
    results=[MacroProblem(k).maximize(weights) for k in DATA]
    args.output.write_text(json.dumps({'weights_file':str(args.weights),'results':results,
                                     'maximum':max(r['maximum_energy_change'] for r in results)},indent=2)+'\n')
    for r in results:print({k:v for k,v in r.items() if k!='outside_black'})

if __name__=='__main__':main()
