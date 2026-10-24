#!/usr/bin/env python3
"""Heuristic context separation for a five-macro local-energy LP.

No success of the heuristic is an exhaustive verification. Infeasibility of
the accumulated LP would be a genuine obstruction to this precise ansatz.
"""
from pathlib import Path
import json
import random
import time
import numpy as np
from scipy.optimize import linprog
from local_energy_search import DATA, prepare_macro, changes, pattern_orbits

BASE=Path(__file__).resolve().parent


class Macro:
    def __init__(self,name,k,idx,n):
        self.name=name;self.k=k;self.idx=idx;self.n=n
        self.initial,self.toggled,self.origins,self.unknown=prepare_macro(name,k)
        self.p0=np.array([sum(((x+dx,y+dy) in self.initial)<<(dx+k*dy)
                             for dy in range(k) for dx in range(k))
                          for x,y in self.origins]+[0],dtype=np.int32)
        self.toggle=np.array([sum(((x+dx,y+dy) in self.toggled)<<(dx+k*dy)
                                 for dy in range(k) for dx in range(k))
                              for x,y in self.origins]+[0],dtype=np.int32)
        uindex={p:i for i,p in enumerate(self.unknown)}
        affect=[[] for _ in self.unknown]
        for j,(x,y) in enumerate(self.origins):
            for dy in range(k):
                for dx in range(k):
                    if (x+dx,y+dy) in uindex:
                        affect[uindex[x+dx,y+dy]].append((j,1<<(dx+k*dy)))
        self.ai=np.full((len(affect),k*k),len(self.origins),dtype=np.int32)
        self.ab=np.zeros(self.ai.shape,dtype=np.int32)
        for i,a in enumerate(affect):
            for j,(factor,bit) in enumerate(a):
                self.ai[i,j]=factor;self.ab[i,j]=bit

    def row(self,bits):
        outside={p for p,b in zip(self.unknown,bits) if b}
        return changes(self.initial,self.toggled,self.origins,outside,self.k,self.idx,self.n)

    def optimize(self,weights,rng,restarts=25):
        allweights=np.r_[0.,weights][np.array(self.idx)+1]
        states=np.arange(1<<(self.k*self.k))
        f=allweights[states[None,:]^self.toggle[:,None]]-allweights[states][None,:]
        witnesses=[];best=(-float('inf'),None)
        for r in range(restarts):
            prob=(0 if r==0 else 1 if r==1 else rng.random())
            bits=np.array([rng.random()<prob for _ in self.unknown],dtype=bool)
            p=self.p0.copy()
            for i,b in enumerate(bits):
                if b:
                    # Padded dummy-factor bit masks are zero.
                    p[self.ai[i]]^=self.ab[i]
            for _ in range(500):
                values=p[self.ai]
                delta=(f[self.ai,values^self.ab]-f[self.ai,values]).sum(axis=1)
                j=int(np.argmax(delta))
                if delta[j]<1e-8:break
                bits[j]=not bits[j]
                p[self.ai[j]]^=self.ab[j]
            val=float(f[np.arange(len(p)),p].sum())
            if val>best[0]:best=(val,bits.copy())
            if val>-1+1e-7:witnesses.append(bits.copy())
        return best,witnesses


def main(k=3,rounds=100,restarts=25):
    idx,classes=pattern_orbits(k)
    macros=[Macro(n,k,idx,len(classes)) for n in DATA]
    rng=random.Random(773849)
    rows=[];seen=set();contexts=[]
    def add(m,bits):
        key=(m.name,tuple(bool(x) for x in bits))
        if key in seen:return False
        seen.add(key)
        rows.append(m.row(bits))
        contexts.append([m.name,[list(p) for p,b in zip(m.unknown,bits) if b]])
        return True
    for m in macros:
        for prob in [0.,1.]+[rng.random() for _ in range(200)]:
            add(m,[rng.random()<prob for _ in m.unknown])
    output={'k':k,'status':'unfinished','rounds':[]}
    start=time.monotonic()
    for it in range(rounds):
        res=linprog(np.ones(len(classes)),A_ub=np.array(rows,dtype=float),b_ub=-np.ones(len(rows)),
                    bounds=(0,None),method='highs')
        if not res.success:
            output['status']='sample LP infeasible';output['message']=res.message
            print('INFEASIBLE',it,len(rows),res.message,flush=True);break
        maximum=-float('inf');added=0;maxima={}
        for m in macros:
            best,witnesses=m.optimize(res.x,rng,restarts)
            maximum=max(maximum,best[0]);maxima[m.name]=round(best[0],6)
            for bits in witnesses:added+=add(m,bits)
        rec={'iteration':it,'rows':len(rows),'weights':float(res.fun),'maxima':maxima,'added':added}
        output['rounds'].append(rec)
        print(rec,'seconds',round(time.monotonic()-start,1),flush=True)
        output['energy']={str(c):float(w) for c,w in zip(classes,res.x) if w>1e-8}
        if added==0:
            output['status']='no heuristic violations; NOT exhaustively certified';break
    output['constraints']=contexts
    (BASE/f'energy_cegis_{k}.json').write_text(json.dumps(output,indent=2))
    np.savez_compressed(BASE/f'energy_cegis_{k}_matrix.npz',matrix=np.array(rows),classes=np.array(classes))


if __name__=='__main__':
    import sys
    main(*(list(map(int,sys.argv[1:]))))
