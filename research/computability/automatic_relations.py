#!/usr/bin/env python3
"""Small exact automatic-relation engine over nonnegative integers, base 2.

Words are synchronised least-significant-bit first, with arbitrary zero padding.
Existential projection includes arbitrarily longer hidden-variable encodings.
Research implementation, not a verified library. No third-party dependencies.
"""
from collections import deque
from dataclasses import dataclass

@dataclass
class Rel:
    vs: tuple
    tr: list
    ac: set
    start: int=0
    def eval(self,**vals):
        nums=[vals[v] for v in self.vs]
        if any(n<0 for n in nums):raise ValueError('Natural-number coordinates only.')
        q=self.start
        for j in range(max([n.bit_length() for n in nums]+[0])):
            a=sum(((n>>j)&1)<<i for i,n in enumerate(nums));q=self.tr[q][a]
        return q in self.ac
    def minimal(self):
        n=len(self.tr);blk=[int(i in self.ac) for i in range(n)]
        while True:
            keys={};new=[]
            for i in range(n):
                key=(i in self.ac,tuple(blk[j] for j in self.tr[i]))
                if key not in keys:keys[key]=len(keys)
                new.append(keys[key])
            if new==blk:break
            blk=new
        reps={}
        for i,b in enumerate(blk):reps.setdefault(b,i)
        trs=[None]*len(reps)
        for b,i in reps.items():trs[b]=[blk[j] for j in self.tr[i]]
        return Rel(self.vs,trs,{blk[i] for i in self.ac},blk[self.start])
    def lift(self,vs):
        vs=tuple(vs)
        if self.vs==vs:return self
        ids=[vs.index(v) for v in self.vs]
        mp=[sum(((a>>j)&1)<<i for i,j in enumerate(ids)) for a in range(1<<len(vs))]
        return Rel(vs,[[row[a] for a in mp] for row in self.tr],set(self.ac),self.start)
    def rename(self,**rename):
        vs=tuple(rename.get(v,v) for v in self.vs)
        if len(set(vs))!=len(vs):raise ValueError('Rename must not identify variables.')
        return Rel(vs,self.tr,self.ac,self.start)
    def both(self,other,op):
        vs=tuple(sorted(set(self.vs)|set(other.vs)));a=self.lift(vs);b=other.lift(vs)
        states=[(a.start,b.start)];idx={states[0]:0};tr=[];ac=set()
        for i,(q,r) in enumerate(states):
            if op(q in a.ac,r in b.ac):ac.add(i)
            row=[]
            for d in range(1<<len(vs)):
                st=(a.tr[q][d],b.tr[r][d])
                if st not in idx:idx[st]=len(states);states.append(st)
                row.append(idx[st])
            tr.append(row)
        return Rel(vs,tr,ac).minimal()
    def __and__(self,o):return self.both(o,lambda a,b:a and b)
    def __or__(self,o):return self.both(o,lambda a,b:a or b)
    def __invert__(self):return Rel(self.vs,self.tr,set(range(len(self.tr)))-self.ac,self.start)
    def implies(self,o):return ~self|o
    def iff(self,o):return (self&o)|(~self&~o)
    def exists(self,*names):
        ans=self
        for name in names:
            if name not in ans.vs:continue
            at=ans.vs.index(name);vs=ans.vs[:at]+ans.vs[at+1:]
            def insert(a,b):return (a&((1<<at)-1))|(b<<at)|((a>>at)<<(at+1))
            # Hidden witnesses may require arbitrarily many extra digits after
            # all free variables have ended. Close accepting states backwards
            # along those zero-free-variable transitions before projection.
            back=[[] for _ in ans.tr]
            for q,row in enumerate(ans.tr):
                for bit in [0,1]:back[row[insert(0,bit)]].append(q)
            good=set(ans.ac);todo=list(good)
            for q in todo:
                for prev in back[q]:
                    if prev not in good:good.add(prev);todo.append(prev)
            states=[frozenset([ans.start])];idx={states[0]:0};tr=[];ac=set()
            for i,qs in enumerate(states):
                if qs&good:ac.add(i)
                row=[]
                for d in range(1<<len(vs)):
                    ns=frozenset(ans.tr[q][insert(d,b)] for q in qs for b in [0,1])
                    if ns not in idx:idx[ns]=len(states);states.append(ns)
                    row.append(idx[ns])
                tr.append(row)
            ans=Rel(vs,tr,ac).minimal()
        return ans
    def forall(self,*names):return ~(~self).exists(*names)
    def witness(self):
        todo=deque([self.start]);prev={self.start:None}
        while todo:
            q=todo.popleft()
            if q in self.ac:
                ds=[]
                while prev[q] is not None:
                    q,d=prev[q];ds.append(d)
                ds.reverse()
                return {v:sum(((d>>i)&1)<<j for j,d in enumerate(ds)) for i,v in enumerate(self.vs)}
            for d,r in enumerate(self.tr[q]):
                if r not in prev:prev[r]=(q,d);todo.append(r)
        return None
    def truth(self):
        if self.vs:raise ValueError('Not a sentence.')
        return self.witness() is not None
    def bounded(self):
        m='_bound'
        if m in self.vs:raise ValueError('Reserved variable.')
        bound=TRUE
        for v in self.vs:bound=bound&linear({m:1,v:-1},0,'>=')
        return self.implies(bound).forall(*self.vs).exists(m).truth()

TRUE=Rel((),[[0]],{0});FALSE=~TRUE

def linear(coeff,c=0,op='='):
    """sum(coeff[v]*v) op c, with all variables nonnegative."""
    vs=tuple(sorted(coeff));cs=[coeff[v] for v in vs];states=[-c];idx={-c:0};tr=[];ac=set()
    for i,carry in enumerate(states):
        if carry is not None and (carry==0 if op=='=' else carry>=0):ac.add(i)
        row=[]
        for d in range(1<<len(vs)):
            z=None if carry is None else carry+sum(a*((d>>j)&1) for j,a in enumerate(cs))
            nxt=None if z is None or (op=='=' and z%2) else z//2
            if nxt not in idx:idx[nxt]=len(states);states.append(nxt)
            row.append(idx[nxt])
        tr.append(row)
    if op not in ('=','>='):raise ValueError(op)
    return Rel(vs,tr,ac).minimal()

def congruent(v,residue,modulus):
    # Remainder and place value; works for arbitrary positive moduli.
    if modulus<=0:raise ValueError(modulus)
    st=[(0,1%modulus)];idx={st[0]:0};tr=[];ac=set()
    for i,(r,p) in enumerate(st):
        if r==residue%modulus:ac.add(i)
        row=[]
        for bit in [0,1]:
            ns=((r+bit*p)%modulus,(2*p)%modulus)
            if ns not in idx:idx[ns]=len(st);st.append(ns)
            row.append(idx[ns])
        tr.append(row)
    return Rel((v,),tr,ac).minimal()

def first_visit(head):
    old=head.rename(t='s')&linear({'t':1,'s':-1},1,'>=')
    return head&~old.exists('s')

def initial_left_cells(head,left):return (first_visit(head)&left).exists('t')

def bad_alternation(head,left):
    between=(head.rename(t='s')&linear({'s':1,'t':-1},1,'>=')&linear({'u':1,'s':-1},1,'>='))
    adjacent=head&head.rename(t='u')&linear({'u':1,'t':-1},1,'>=')&~between.exists('s')
    return adjacent&left.iff(left.rename(t='u'))

def controls():
    count=0
    for a in [-3,-1,0,1,2,5]:
        for b in [-2,0,1,3]:
            for c in [-7,0,4]:
                for op in ['=','>=']:
                    r=linear({'x':a,'y':b},c,op)
                    for x in range(16):
                        for y in range(16):
                            want=a*x+b*y==c if op=='=' else a*x+b*y>=c
                            assert r.eval(x=x,y=y)==want;count+=1
    more=linear({'y':1,'x':-1},1,'>=')
    assert more.exists('y').forall('x').truth()
    # Explicitly tests longer hidden encodings: y may be 1024 with free x=0.
    assert linear({'y':1},1024).exists('y').truth()
    assert not linear({'x':2},1).exists('x').truth()
    assert congruent('x',1,3).eval(x=100)
    # Infinite staircase: RL repeated, all L reads occur at fresh cells.
    north=linear({'t':1,'x':-2},0)&linear({'x':1,'y':-1},0)
    east=linear({'t':1,'y':-2},1)&linear({'x':1,'y':-1},1)
    head=north|east;left=congruent('t',1,2)
    firstblack=initial_left_cells(head,left)
    assert not firstblack.bounded()
    assert bad_alternation(head,left).witness() is None
    for x in range(8):
        for y in range(8):assert firstblack.eval(x=x,y=y)==(x==y+1)
    # Geometric clockwise square, R forever: finite initial demand, but fails
    # the mandatory alternate-read condition at its first return.
    square=FALSE
    for j,(x,y) in enumerate([(0,1),(1,1),(1,0),(0,0)]):
        square=square|(congruent('t',j,4)&linear({'x':1},x)&linear({'y':1},y))
    assert initial_left_cells(square,FALSE).bounded()
    bad=bad_alternation(square,FALSE);witness=bad.witness()
    assert witness is not None
    return {'status':'PASS','arithmetic_point_controls':count,'long_hidden_witness_projection':'PASS','staircase':'alternation passes; finite seed fails exactly','clockwise_square_alternation_witness':witness,'scope':'Natural-number coordinate automatic relations; no ant counterexample found.'}
if __name__=='__main__':
    import json
    print(json.dumps(controls(),indent=2))
