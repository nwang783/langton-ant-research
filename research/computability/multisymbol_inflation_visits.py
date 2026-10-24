#!/usr/bin/env python3
"""Exact inverse certificate adapter for finite-control geometric inflation.
The production alphabet may contain many symbols with the same R/L output.
No finite prefix is treated as a positive all-time ant certificate.
"""
from expanding_recurrence_visits import Recurrence
from automatic_radix import Rel,reverse_msb
from selfsimilar_visit_relations import D,add,rot,inverse_tests
import json

def model(productions,colors,root):
    if root not in productions:raise ValueError('Missing root production')
    alphabet=[];seen={root};todo=[root]
    while todo:
        s=todo.pop(0);alphabet.append(s)
        if s not in colors or colors[s] not in ['R','L']:raise ValueError('Every accessible symbol needs a turn')
        for t in productions[s]:
            if t not in productions:raise ValueError('Production alphabet is not closed')
            if t not in seen:seen.add(t);todo.append(t)
    k=len(productions[root])
    if k<=1 or any(len(productions[s])!=k for s in alphabet):raise ValueError('Uniform length k>1 required')
    if productions[root][0]!=root:raise ValueError('Root must be prolongable; take a power for a root cycle')
    paths={};a=None
    for s in alphabet:
        p=(0,0);h=0;points=[];heads=[]
        for t in productions[s]:
            points.append(p);heads.append(h)
            h=(h+(1 if colors[t]=='R' else -1))%4;p=add(p,D[h])
        sign=1 if colors[s]=='R' else -1
        if h!=sign%4:raise ValueError('A production does not restore its coarse turn heading')
        scale=(sign*p[0],sign*p[1])
        if a is None:a=scale
        if a!=scale:raise ValueError('No common geometric scalar')
        paths[s]=(points,heads)
    if a[0]**2+a[1]**2<=1:raise ValueError('Expansion required')
    states=[(h,s) for h in range(4) for s in alphabet];ix={s:i for i,s in enumerate(states)}
    nxt=[];off=[]
    for h,s in states:
        points,heads=paths[s]
        nxt.append([ix[((h+heads[j])%4,t)] for j,t in enumerate(productions[s])])
        off.append([rot(p,h) for p in points])
    rec=Recurrence(k,a,nxt,off,start=ix[0,root]);rec.validate()
    letters={s:i for i,s in enumerate(alphabet)}
    left=reverse_msb(Rel(('t',),[[letters[t] for t in productions[s]] for s in alphabet],
                         {letters[s] for s in alphabet if colors[s]=='L'},k,start=letters[root]))
    return rec,left,{'accessible_symbols':alphabet,'projected_images':{s:''.join(colors[t] for t in productions[s]) for s in alphabet}}

def exact(productions,colors,root):
    rec,left,meta=model(productions,colors,root);rs,carry=rec.difference_machine(0);eq=rs((0,0))
    return {**meta,'scale':rec.scale,'radix':rec.base,**carry,**inverse_tests(eq,left)}

def controls():
    examples=[({'R':'RRL','L':'LRL'},{'R':'R','L':'L'},'R'),
              ({'A':'ABC','B':'BAC','C':'CAC'},{'A':'R','B':'R','C':'L'},'A'),
              ({'A':'ABC','B':'BAC','C':'CAC'},{'A':'R','B':'R','C':'L'},'C')]
    out=[]
    for rules,colors,root in examples:
        rec,left,meta=model(rules,colors,root);rs,carry=rec.difference_machine(0);eq=rs((0,0))
        symbolic=[root]
        while len(symbolic)<160:symbolic=[t for s in symbolic for t in rules[s]]
        word=''.join(colors[s] for s in symbolic[:160]);p=(0,0);h=0;points=[]
        for t,c in enumerate(word):
            points.append(p);assert rec.point(t)==p;assert left.eval(t=t)==(c=='L')
            h=(h+(1 if c=='R' else -1))%4;p=add(p,D[h])
        for s in range(160):
            for t in range(160):assert eq.eval(s=s,t=t)==(points[s]==points[t])
        out.append({'root':root,**meta,**carry,**inverse_tests(eq,left),'literal_points':160,'literal_pair_checks':25600})
    return out

if __name__=='__main__':
    result={'status':'finite independent-path controls passed; all three examples need infinite initial support','cases':controls()}
    open(__file__.replace('.py','_controls.json'),'w').write(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
