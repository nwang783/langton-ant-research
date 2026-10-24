#!/usr/bin/env python3
"""General-root extension of the exact visit-equality certificate.
Default R-root exhaustive results remain separately scoped. A first-letter
2-cycle is handled by explicitly composing the substitution with itself.
"""
from expanding_recurrence_visits import Recurrence
from automatic_radix import Rel,reverse_msb
from selfsimilar_visit_relations import D,add,rot,inverse_tests
import json

def rooted_model(u,v,root='R'):
    if root not in 'RL' or len(root)!=1 or len(u)<=1 or len(u)!=len(v) or set(u+v)-set('RL'):
        raise ValueError('Uniform R/L substitution and root R or L required')
    ws=[u,v];ri=int(root=='L')
    if ws[ri][0]!=root:raise ValueError('Chosen root must be prolongable')
    ps=[];hs=[];ends=[]
    for w in ws:
        p=(0,0);h=0;pp=[];hh=[]
        for c in w:
            pp.append(p);hh.append(h);h=(h+(1 if c=='R' else -1))%4;p=add(p,D[h])
        ps.append(pp);hs.append(hh);ends.append((p,h))
    a=ends[0][0]
    if ends[0][1]!=1 or ends[1]!=((-a[0],-a[1]),3) or a[0]**2+a[1]**2<=1:
        raise ValueError('Opposite expanding displacement and coarse quarter-turn endpoints required')
    states=[(h,c) for h in range(4) for c in range(2)];ix={s:i for i,s in enumerate(states)}
    nxt=[];off=[]
    for h,c in states:
        nxt.append([ix[((h+hs[c][j])%4,int(ws[c][j]=='L'))] for j in range(len(u))])
        off.append([rot(ps[c][j],h) for j in range(len(u))])
    model=Recurrence(len(u),a,nxt,off,start=ix[0,ri]);model.validate()
    left=reverse_msb(Rel(('t',),[[int(c=='L') for c in u],[int(c=='L') for c in v]],{1},len(u),start=ri))
    return model,left

def compose(u,v):
    return tuple(''.join(u if c=='R' else v for c in w) for w in [u,v])

def exact(u,v,root='R'):
    model,left=rooted_model(u,v,root);rs,meta=model.difference_machine(0);eq=rs((0,0))
    return {'root':root,'R':u,'L':v,**meta,**inverse_tests(eq,left)}

def controls():
    out=[]
    for u,v,root in [('RRL','LRL','R'),('RRL','LRL','L'),('RRRLL','LRRLL','L')]:
        model,left=rooted_model(u,v,root);rs,meta=model.difference_machine(0);eq=rs((0,0))
        w=root
        while len(w)<150:w=''.join(u if c=='R' else v for c in w)
        p=(0,0);h=0;points=[]
        for t,c in enumerate(w[:150]):
            points.append(p);assert model.point(t)==p;assert left.eval(t=t)==(c=='L')
            h=(h+(1 if c=='R' else -1))%4;p=add(p,D[h])
        for s in range(150):
            for t in range(150):assert eq.eval(s=s,t=t)==(points[s]==points[t])
        out.append({'root':root,'R':u,'L':v,**meta,**inverse_tests(eq,left),'literal_points':150,'literal_cell_pairs':22500})
    return out
if __name__=='__main__':
    result={'status':'finite controls passed; no positive ant model','cases':controls()}
    open(__file__.replace('.py','_controls.json'),'w').write(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
