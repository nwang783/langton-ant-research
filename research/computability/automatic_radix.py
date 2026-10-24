#!/usr/bin/env python3
"""Exact synchronous automatic relations in an arbitrary fixed integer radix.
LSB-first, zero-padding saturated. Research implementation, stdlib only.
"""
from collections import deque
from dataclasses import dataclass
from itertools import product

@dataclass
class Rel:
    vs: tuple
    tr: list
    ac: set
    base: int
    start: int=0
    def eval(self,**vals):
        ns=[vals[v] for v in self.vs]
        if any(n<0 for n in ns):raise ValueError('Naturals only')
        q=self.start
        while any(ns):
            q=self.tr[q][sum((n%self.base)*self.base**i for i,n in enumerate(ns))]
            ns=[n//self.base for n in ns]
        return q in self.ac
    def minimal(self):
        blk=[int(i in self.ac) for i in range(len(self.tr))]
        while True:
            keys={};new=[]
            for i,row in enumerate(self.tr):
                key=(i in self.ac,tuple(blk[j] for j in row))
                if key not in keys:keys[key]=len(keys)
                new.append(keys[key])
            if new==blk:break
            blk=new
        reps={}
        for i,b in enumerate(blk):reps.setdefault(b,i)
        return Rel(self.vs,[[blk[j] for j in self.tr[reps[b]]] for b in range(len(reps))],{blk[i] for i in self.ac},self.base,blk[self.start])
    def lift(self,vs):
        vs=tuple(vs)
        if vs==self.vs:return self
        ids=[vs.index(v) for v in self.vs];b=self.base
        mp=[sum(((a//b**j)%b)*b**i for i,j in enumerate(ids)) for a in range(b**len(vs))]
        return Rel(vs,[[r[a] for a in mp]for r in self.tr],set(self.ac),b,self.start)
    def rename(self,**names):
        vs=tuple(names.get(v,v) for v in self.vs)
        if len(set(vs))!=len(vs):raise ValueError('Cannot identify variables')
        return Rel(vs,self.tr,self.ac,self.base,self.start)
    def both(self,o,op):
        if self.base!=o.base:raise ValueError('Radices must match')
        vs=tuple(sorted(set(self.vs)|set(o.vs)));a=self.lift(vs);b=o.lift(vs)
        st=[(a.start,b.start)];ix={st[0]:0};tr=[];ac=set()
        for i,(q,r) in enumerate(st):
            if op(q in a.ac,r in b.ac):ac.add(i)
            row=[]
            for d in range(self.base**len(vs)):
                ns=(a.tr[q][d],b.tr[r][d])
                if ns not in ix:ix[ns]=len(st);st.append(ns)
                row.append(ix[ns])
            tr.append(row)
        return Rel(vs,tr,ac,self.base).minimal()
    def __and__(self,o):return self.both(o,lambda a,b:a and b)
    def __or__(self,o):return self.both(o,lambda a,b:a or b)
    def __invert__(self):return Rel(self.vs,self.tr,set(range(len(self.tr)))-self.ac,self.base,self.start)
    def implies(self,o):return ~self|o
    def iff(self,o):return (self&o)|(~self&~o)
    def exists(self,*names):
        ans=self;b=self.base
        for name in names:
            if name not in ans.vs:continue
            at=ans.vs.index(name);power=b**at;vs=ans.vs[:at]+ans.vs[at+1:]
            def insert(a,d):return a%power+d*power+(a//power)*power*b
            back=[[]for _ in ans.tr]
            for q,row in enumerate(ans.tr):
                for d in range(b):back[row[insert(0,d)]].append(q)
            good=set(ans.ac);todo=list(good)
            for q in todo:
                for prev in back[q]:
                    if prev not in good:good.add(prev);todo.append(prev)
            st=[frozenset([ans.start])];ix={st[0]:0};tr=[];ac=set()
            for i,qs in enumerate(st):
                if qs&good:ac.add(i)
                row=[]
                for a in range(b**len(vs)):
                    ns=frozenset(ans.tr[q][insert(a,d)]for q in qs for d in range(b))
                    if ns not in ix:ix[ns]=len(st);st.append(ns)
                    row.append(ix[ns])
                tr.append(row)
            ans=Rel(vs,tr,ac,b).minimal()
        return ans
    def forall(self,*names):return ~(~self).exists(*names)
    def witness(self):
        todo=deque([self.start]);prev={self.start:None};b=self.base
        while todo:
            q=todo.popleft()
            if q in self.ac:
                ds=[]
                while prev[q] is not None:q,d=prev[q];ds.append(d)
                ds.reverse()
                return {v:sum(((d//b**i)%b)*b**j for j,d in enumerate(ds))for i,v in enumerate(self.vs)}
            for d,r in enumerate(self.tr[q]):
                if r not in prev:prev[r]=(q,d);todo.append(r)
        return None
    def truth(self):
        if self.vs:raise ValueError('Not a sentence')
        return self.witness() is not None
    def bounded(self):
        bound=truth(self.base)
        for v in self.vs:bound=bound&linear(self.base,{'_bound':1,v:-1},0,'>=')
        return self.implies(bound).forall(*self.vs).exists('_bound').truth()

def truth(base):return Rel((),[[0]],{0},base)
def linear(base,coeff,c=0,op='='):
    if op not in['=','>=']:raise ValueError(op)
    vs=tuple(sorted(coeff));cs=[coeff[v]for v in vs];st=[-c];ix={-c:0};tr=[];ac=set()
    for i,carry in enumerate(st):
        if carry is not None and (carry==0 if op=='=' else carry>=0):ac.add(i)
        row=[]
        for a in range(base**len(vs)):
            z=None if carry is None else carry+sum(v*((a//base**j)%base)for j,v in enumerate(cs))
            ns=None if z is None or(op=='='and z%base)else z//base
            if ns not in ix:ix[ns]=len(st);st.append(ns)
            row.append(ix[ns])
        tr.append(row)
    return Rel(vs,tr,ac,base).minimal()

def reverse_msb(rel):
    """Reverse an MSB-first DFA language; numeric leading padding becomes trailing."""
    alpha=rel.base**len(rel.vs);back=[[set()for _ in rel.tr]for _ in range(alpha)]
    for q,row in enumerate(rel.tr):
        for a,r in enumerate(row):back[a][r].add(q)
    st=[frozenset(rel.ac)];ix={st[0]:0};tr=[];ac=set()
    for i,qs in enumerate(st):
        if rel.start in qs:ac.add(i)
        row=[]
        for a in range(alpha):
            ns=frozenset(q for r in qs for q in back[a][r])
            if ns not in ix:ix[ns]=len(st);st.append(ns)
            row.append(ix[ns])
        tr.append(row)
    return Rel(rel.vs,tr,ac,rel.base).minimal()

if __name__=='__main__':
    count=0
    for b in [2,3,5,7]:
        for a in[-2,0,3]:
            for c in[-4,0,9]:
                for op in ['=','>=']:
                    r=linear(b,{'x':a,'y':-1},c,op)
                    for x in range(20):
                        for y in range(20):
                            assert r.eval(x=x,y=y)==(a*x-y==c if op=='='else a*x-y>=c);count+=1
        assert linear(b,{'y':1},b**10).exists('y').truth()
        assert linear(b,{'y':1,'x':-1},1,'>=').exists('y').forall('x').truth()
    print({'status':'PASS','arithmetic_controls':count,'radices':[2,3,5,7]})
