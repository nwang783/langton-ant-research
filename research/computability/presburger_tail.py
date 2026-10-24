#!/usr/bin/env python3
"""Exact random-access space-time from a certified infinite periodic tail.

The generated SMT-LIB definitions use only Presburger arithmetic. This module
checks the word certificate first; no SMT solver or bounded-repeat assumption
is used. It does not decide arbitrary unknown ant orbits.
"""
from periodic_tail_checker import plan,first_mismatch,multiplier
from check_rigid_reachability import State,D,forward
from pathlib import Path
import json

class Tail:
    def __init__(self,state,word):
        if first_mismatch(state,word) is not None:
            raise ValueError('Not an exact periodic tail.')
        self.state=state;self.word=word;self.q,self.d=plan(state,word)
        h=state.h;self.hs=[]
        for ch in word:
            self.hs.append(h);h=(h+(1 if ch=='R' else -1))%4
    def pose(self,t):
        if t<0:raise ValueError('Forward times only.')
        k,j=divmod(t,len(self.word));q=self.q[j]
        return (q[0]+k*self.d[0],q[1]+k*self.d[1]),self.hs[j]
    def black(self,t,point):
        if t<0:raise ValueError('Forward times only.')
        ans=point in self.state.black
        for j,q in enumerate(self.q):
            k=multiplier((point[0]-q[0],point[1]-q[1]),self.d)
            if k is not None and k>=0 and len(self.word)*k+j<t:ans=not ans
        return ans
    def smt(self):
        def integer(n):return str(n) if n>=0 else f'(- {-n})'
        def disjoin(xs):return '(or '+' '.join(xs)+')' if xs else 'false'
        def eqpoint(q,drift):
            return f'(= x (+ {integer(q[0])} (* k {integer(drift[0])}))) (= y (+ {integer(q[1])} (* k {integer(drift[1])})))'
        P=len(self.word)
        heads=[f'(exists ((k Int)) (and (>= k 0) (= t (+ (* {P} k) {j})) {eqpoint(q,self.d)} (= h {h})))' for j,(q,h) in enumerate(zip(self.q,self.hs))]
        pieces=[disjoin([f'(and (= x {integer(x)}) (= y {integer(y)}))' for x,y in sorted(self.state.black)])]
        pieces += [f'(exists ((k Int)) (and (>= k 0) {eqpoint(q,self.d)} (< (+ (* {P} k) {j}) t)))' for j,q in enumerate(self.q)]
        color=pieces[0]
        for piece in pieces[1:]:color=f'(xor {color} {piece})'
        return '; Forward times t>=0; tail capture state is at t=0.\n' + f'(define-fun Head ((t Int) (x Int) (y Int) (h Int)) Bool (and (>= t 0) {disjoin(heads)}))\n' + f'(define-fun Black ((t Int) (x Int) (y Int)) Bool (and (>= t 0) {color}))\n'

def main():
    root=Path(__file__).resolve().parents[1]
    data=json.loads((root/'recovered_bundle/ant_global/root/standard.json').read_text())
    seed=State(frozenset(map(tuple,data['seed'])),(0,0),data['heading'])
    tail=Tail(seed,data['word']);s=seed;count=0
    times={0,1,2,17,103,104,105,208,417,999,1500}
    for t in range(max(times)+1):
        if t in times:
            assert tail.pose(t)==(s.p,s.h)
            points=set(s.black)|{(s.p[0]+dx,s.p[1]+dy) for dx in range(-10,11) for dy in range(-10,11)}
            for q in points:assert tail.black(t,q)==(q in s.black);count+=1
        s=forward(s)
    far=[]
    for t in [10**30,10**30+103,104*10**60+7]:
        p,h=tail.pose(t);bit=tail.black(t,p)
        nh=(h+(-1 if bit else 1))%4;np=(p[0]+D[nh][0],p[1]+D[nh][1])
        assert tail.pose(t+1)==(np,nh)
        for dx,dy in [(0,0),(1,0),(0,1),(-1,0),(0,-1),(100,-100)]:
            q=p[0]+dx,p[1]+dy
            assert tail.black(t+1,q)==(tail.black(t,q)^(q==p))
        far.append({'time':t,'pose':[p,h],'black_under_head':bit})
    (Path(__file__).resolve().parent/'standard_tail.smt2').write_text(tail.smt())
    out={'status':'PASS','literal_cell_comparisons':count,'literal_pose_comparisons':len(times),'huge_time_local_controls':far,'scope':'Exact certified periodic tail only. SMT definitions emitted but no external SMT solver was run.'}
    (Path(__file__).resolve().parent/'presburger_tail_controls.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
