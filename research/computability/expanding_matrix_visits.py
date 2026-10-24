#!/usr/bin/env python3
"""Exact automatic visit relations for common expansive integer 2x2 recurrences.
Uses a rational discrete-Lyapunov norm, not a Euclidean expansion assumption.
The local automata library remains a research implementation, not formally verified.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
from automatic_radix import Rel, reverse_msb
import json, time


def matvec(A,v):
    return (A[0][0]*v[0]+A[0][1]*v[1],A[1][0]*v[0]+A[1][1]*v[1])

def add(u,v):return (u[0]+v[0],u[1]+v[1])
def sub(u,v):return (u[0]-v[0],u[1]-v[1])
def qform(P,v):return P[0]*v[0]**2+2*P[1]*v[0]*v[1]+P[2]*v[1]**2

def solve_rational(A,b):
    A=[[F(v)for v in row]+[F(y)]for row,y in zip(A,b)]
    n=len(A)
    for j in range(n):
        i=next((i for i in range(j,n)if A[i][j]),None)
        if i is None:raise ValueError('Singular Lyapunov equation; matrix is not expansive')
        A[i],A[j]=A[j],A[i];v=A[j][j];A[j]=[x/v for x in A[j]]
        for i in range(n):
            if i!=j:
                v=A[i][j];A[i]=[x-v*y for x,y in zip(A[i],A[j])]
    return tuple(row[-1]for row in A)

def ceil_fraction(x):return -((-x.numerator)//x.denominator)
def ceil_sqrt_fraction(x):
    assert x>=0
    r=isqrt(x.numerator//x.denominator)
    return r+(r*r*x.denominator<x.numerator)

def expanding_norm(A):
    """Return P=(P11,P12,P22)>0 and rational q<1 with ||A^-1||_P<=q.
    P - A^-T P A^-1 = I is solved and checked with exact fractions.
    Positive definiteness is itself an exact expansiveness test.
    """
    aa,bb=A[0];cc,dd=A[1];det=aa*dd-bb*cc
    if not det:raise ValueError('Singular matrix is not expansive')
    a,b,c,d=F(dd,det),F(-bb,det),F(-cc,det),F(aa,det)
    P=solve_rational(((1-a*a,-2*a*c,-c*c),(-a*b,1-a*d-b*c,-c*d),(-b*b,-2*b*d,1-d*d)),(1,0,1))
    x,y,z=P
    if x<=0 or x*z-y*y<=0:raise ValueError('Matrix is not expansive')
    assert x-a*a*x-2*a*c*y-c*c*z==1
    assert y-a*b*x-(a*d+b*c)*y-c*d*z==0
    assert z-b*b*x-2*b*d*y-d*d*z==1
    # Positivity of the Lyapunov solution proves inverse spectral radius<1,
    # hence P=sum (A^-i)^T A^-i >= I. q^2 >= 1-1/trace(P).
    tr=x+z;assert tr>=2
    q=1-F(1,2*tr)
    assert 0<q<1 and q*q>=1-1/tr
    # Optional exact tightening: Gershgorin upper-bounds lambda_max(P).
    U=max(x+abs(y),z+abs(y));q2=1-1/U
    den=4096
    while True:
        sharp=F(ceil_sqrt_fraction(q2*den*den),den)
        if sharp<1:break
        den*=2
    q=min(q,sharp)
    a0=1-(1-q*q)*x;c0=1-(1-q*q)*z;b0=-(1-q*q)*y
    assert 0<q<1 and a0>=0 and c0>=0 and a0*c0-b0*b0>=0
    return P,q

@dataclass
class MatrixRecurrence:
    base:int
    matrix:tuple
    nxt:list
    off:list
    start:int=0
    def validate(self):
        assert self.base>1 and len(self.nxt)==len(self.off)>0
        assert len(self.matrix)==2 and all(len(row)==2 for row in self.matrix)
        assert all(isinstance(x,int)for row in self.matrix for x in row)
        assert all(len(r)==self.base for r in self.nxt+self.off)
        assert all(0<=s<len(self.nxt)for row in self.nxt for s in row)
        assert all(len(v)==2 and all(isinstance(x,int)for x in v)for row in self.off for v in row)
        assert self.nxt[self.start][0]==self.start and self.off[self.start][0]==(0,0)
        return expanding_norm(self.matrix)
    def point(self,n):
        assert n>=0
        ds=[]
        while n:ds.append(n%self.base);n//=self.base
        p=(0,0);s=self.start
        for d in reversed(ds):p=add(matvec(self.matrix,p),self.off[s][d]);s=self.nxt[s][d]
        return p
    def difference_machine(self,max_target_linf=1):
        P,q=self.validate();b=self.base
        offsets=[v for row in self.off for v in row]
        M=ceil_sqrt_fraction(max(qform(P,sub(v,w))for v in offsets for w in offsets))
        target_radius=ceil_sqrt_fraction(max(qform(P,(x,y))for x in (-max_target_linf,max_target_linf)for y in (-max_target_linf,max_target_linf)))
        R=max(target_radius,ceil_fraction(q*M/(1-q)))
        states=[(self.start,self.start,(0,0))];idx={states[0]:0};tr=[];labels=[]
        for st in states:
            labels.append(None if st is None else st[2]);row=[]
            for code in range(b*b):
                j=code%b;l=code//b;ns=None
                if st is not None:
                    s,t,D=st;D2=add(matvec(self.matrix,D),sub(self.off[s][j],self.off[t][l]))
                    if qform(P,D2)<=R*R:ns=(self.nxt[s][j],self.nxt[t][l],D2)
                if ns not in idx:idx[ns]=len(states);states.append(ns)
                row.append(idx[ns])
            tr.append(row)
        cache={}
        def relation(target=(0,0)):
            target=tuple(target);assert max(map(abs,target))<=max_target_linf
            if target not in cache:
                cache[target]=reverse_msb(Rel(('s','t'),tr,{i for i,d in enumerate(labels)if d==target},b).minimal())
            return cache[target]
        return relation,{'raw_difference_states':len(states),'lyapunov_P':[str(v)for v in P], 'inverse_contraction_upper':str(q),'offset_difference_norm_ceiling':M,'carry_radius':R}

def direction_substitution(matrix,images,root='E'):
    """Convert four absolute-move images into the exact common-matrix recurrence.
    Letter ordering E,N,W,S; all images have one common length and net A*d.
    This adapter does not assume rotation covariance or ant legality.
    """
    letters='ENWS';vectors=((1,0),(0,1),(-1,0),(0,-1));lookup=dict(zip(letters,vectors))
    assert set(images)==set(letters) and root in letters
    k=len(images[root]);assert k>=2 and all(len(images[c])==k for c in letters)
    assert images[root][0]==root
    nxt=[];off=[]
    for c,v in zip(letters,vectors):
        p=(0,0);row=[]
        for d in images[c]:
            assert d in letters;row.append(p);p=add(p,lookup[d])
        assert p==matvec(matrix,v),(c,p,matvec(matrix,v))
        off.append(row);nxt.append([letters.index(d)for d in images[c]])
    model=MatrixRecurrence(k,tuple(tuple(row)for row in matrix),nxt,off,letters.index(root))
    model.validate();return model

def pair_context_substitution(matrix,images,root=('N','E')):
    """Eight incoming/outgoing pair images with shared last letter per output.
    This is a context-sensitive construction class, not an ordinary four-letter
    substitution. Shared last letters make the zero-digit transition finite.
    """
    letters='ENWS';vectors=((1,0),(0,1),(-1,0),(0,-1));lookup=dict(zip(letters,vectors))
    pairs=[(e,d)for e in letters for d in letters if (letters.index(e)-letters.index(d))%2]
    assert set(images)==set(pairs) and root in pairs
    k=len(images[root]);assert k>=2 and all(len(w)==k for w in images.values())
    last={}
    for (e,d),w in images.items():
        assert all(c in letters for c in w)
        if d in last:assert last[d]==w[-1]
        else:last[d]=w[-1]
        assert all((letters.index(w[j-1])-letters.index(w[j]))%2 for j in range(1,k))
    assert last[root[0]]==root[0] and images[root][0]==root[1]
    nxt=[];off=[]
    for e,d in pairs:
        w=images[e,d];p=(0,0);rr=[];nn=[]
        for j,c in enumerate(w):
            prev=last[e] if j==0 else w[j-1]
            assert (prev,c)in pairs
            nn.append(pairs.index((prev,c)));rr.append(p);p=add(p,lookup[c])
        assert p==matvec(matrix,lookup[d]),((e,d),p,matvec(matrix,lookup[d]))
        nxt.append(nn);off.append(rr)
    model=MatrixRecurrence(k,tuple(tuple(row)for row in matrix),nxt,off,pairs.index(root))
    model.validate();return model

def controls():
    start=time.monotonic()
    cases=[MatrixRecurrence(2,((2,0),(0,3)),[[0,0]],[[(0,0),(1,1)]]),
           MatrixRecurrence(2,((2,3),(0,2)),[[0,0]],[[(0,0),(0,1)]]),
           MatrixRecurrence(2,((0,-2),(3,0)),[[0,1],[1,0]],[[(0,0),(1,0)],[(0,1),(1,-1)]])]
    out=[];targets=[(0,0),(1,0),(-1,0),(0,1),(0,-1),(1,1)]
    for i,m in enumerate(cases):
        rs,meta=m.difference_machine();ps=[m.point(n)for n in range(128)];checks=0
        for v in targets:
            rel=rs(v)
            for s in range(128):
                for t in range(128):
                    assert rel.eval(s=s,t=t)==(sub(ps[s],ps[t])==v),(i,v,s,t)
                    checks+=1
        out.append({'case':i,'matrix':m.matrix,**meta,'comparison_controls':checks})
    # Same physical dragon control as the established scalar implementation.
    from expanding_recurrence_visits import dragon,derive_ant_geometry
    from selfsimilar_visit_relations import inverse_tests
    d=dragon();m=MatrixRecurrence(d.base,((1,-1),(1,1)),d.nxt,d.off,d.start)
    rs,meta=m.difference_machine();left,g=derive_ant_geometry(m,rs)
    assert all(v is None for k,v in g.items()if k.startswith('bad_'))
    inverse=inverse_tests(rs((0,0)),left)
    assert inverse['bad_alternation_witness'] is not None and not inverse['first_left_times_finite']
    rejects=[]
    for A in [((1,0),(0,2)),((0,0),(0,2)),((1,1),(1,2)),((0,-1),(1,0))]:
        try:expanding_norm(A)
        except ValueError:rejects.append(A)
        else:raise AssertionError(('Expected nonexpansive rejection',A))
    return {'status':'PASS finite implementation controls; no finite-seed example found','cases':out,'dragon':{**meta,'geometry':g,**inverse},'nonexpansive_rejections':rejects,'elapsed_seconds':time.monotonic()-start}

if __name__=='__main__':
    from pathlib import Path
    out=controls();Path(__file__).with_name('expanding_matrix_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
