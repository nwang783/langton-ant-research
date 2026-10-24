#!/usr/bin/env python3
"""Exact visit equality and inverse ant checks for common-expanding recurrences.
The input specifies p(kn+j)=a*p(n)+off[state(n)][j], with finite state update.
No canonical numeral system for grid positions is needed.
"""
from dataclasses import dataclass
from math import isqrt
from automatic_radix import Rel,linear,reverse_msb,truth
from selfsimilar_visit_relations import mul,add,sub,inverse_tests
import json,time

UNITS=((1,0),(0,1),(-1,0),(0,-1))
@dataclass
class Recurrence:
    base:int
    scale:tuple
    nxt:list
    off:list
    start:int=0
    def validate(self):
        assert self.base>1 and self.scale[0]**2+self.scale[1]**2>1
        assert len(self.nxt)==len(self.off)>0
        assert all(len(r)==self.base for r in self.nxt+self.off)
        assert all(0<=s<len(self.nxt)for row in self.nxt for s in row)
        assert self.nxt[self.start][0]==self.start and self.off[self.start][0]==(0,0)
    def point(self,n):
        ds=[]
        while n:ds.append(n%self.base);n//=self.base
        p=(0,0);s=self.start
        for d in reversed(ds):p=add(mul(self.scale,p),self.off[s][d]);s=self.nxt[s][d]
        return p
    def difference_machine(self,max_target_norm=1):
        self.validate();b=self.base;norm=sum(x*x for x in self.scale)
        n=max(x*x+y*y for row in self.off for x,y in row);m=isqrt(n)+(isqrt(n)**2<n);delta=2*m
        radius=max_target_norm
        while norm*radius*radius<(radius+delta)**2:radius+=1
        states=[(self.start,self.start,(0,0))];idx={states[0]:0};tr=[];labels=[]
        for state in states:
            labels.append(None if state is None else state[2]);row=[]
            for code in range(b*b):
                d=code%b;e=code//b;ns=None
                if state is not None:
                    s,t,D=state;nd=add(mul(self.scale,D),sub(self.off[s][d],self.off[t][e]))
                    if nd[0]**2+nd[1]**2<=radius*radius:ns=(self.nxt[s][d],self.nxt[t][e],nd)
                if ns not in idx:idx[ns]=len(states);states.append(ns)
                row.append(idx[ns])
            tr.append(row)
        def relation(target):
            assert target[0]**2+target[1]**2<=max_target_norm**2
            return reverse_msb(Rel(('s','t'),tr,{i for i,d in enumerate(labels)if d==target},b).minimal())
        return relation,{'raw_difference_states':len(states),'carry_radius':radius}

def derive_ant_geometry(model,relations):
    b=model.base;succ=linear(b,{'t':1,'s':-1},1);dirs=[]
    for dx,dy in UNITS:
        dirs.append((relations((-dx,-dy))&succ).exists('t').rename(s='t'))
    allmoves=~truth(b)
    for d in dirs:allmoves=allmoves|d
    badunit=(~allmoves).witness()
    badturn=~truth(b)
    for old in range(4):
        for new in [old,(old+2)%4]:
            badturn=badturn|(dirs[old].rename(t='s')&dirs[new]&succ)
    badinitial=((dirs[1]|dirs[3])&linear(b,{'t':1},0)).witness()
    # Initial heading N. First W is L; all later L turns increase CCW direction.
    left=dirs[2]&linear(b,{'t':1},0)
    for old in range(4):left=left|((dirs[old].rename(t='s')&dirs[(old+1)%4]&succ).exists('s'))
    return left,{'bad_unit_step':badunit,'bad_quarter_turn':badturn.witness(),'bad_initial_turn':badinitial,'direction_dfa_states':[len(d.tr)for d in dirs]}

def dragon():
    states=[(p,g)for p in range(2)for g in range(4)];idx={s:i for i,s in enumerate(states)}
    nxt=[];off=[]
    for p,g in states:
        nxt.append([idx[(0,(g+p)%4)],idx[(1,(g+1-p)%4)]])
        off.append([(0,0),UNITS[(p+g)%4]])
    return Recurrence(2,(1,1),nxt,off)

def main():
    start=time.monotonic();m=dragon();rs,meta=m.difference_machine();left,geometry=derive_ant_geometry(m,rs)
    assert all(v is None for k,v in geometry.items()if k.startswith('bad_'))
    eq=rs((0,0));tests=inverse_tests(eq,left);assert tests['bad_alternation_witness'] is not None and not tests['first_left_times_finite']
    checks=0;ps=[m.point(i)for i in range(200)]
    for s in range(200):
        for t in range(200):assert eq.eval(s=s,t=t)==(ps[s]==ps[t]);checks+=1
    out={'status':'PASS: exact negative control','model':'ordinary dragon; binary clock, expanding scalar1+i, eight affine states',**meta,'equal_cell_dfa_states':len(eq.tr),'geometry':geometry,**tests,'point_pair_controls':checks,'elapsed_seconds':time.monotonic()-start,'scope':'No positional numeral system or full automatic pose graph assumed. This path is not an ant on any initial coloring.'}
    from pathlib import Path
    (Path(__file__).resolve().parent/'expanding_recurrence_controls.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
