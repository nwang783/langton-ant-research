#!/usr/bin/env python3
"""Automatic grid presentation in complex base -1+i, with binary digit tracks.

A digit word for a cell is stored as its ordinary binary numeral CODE; decode
maps that code to the actual Gaussian coordinate. Grid addition is not code
addition. Automata and Boolean/projection operations act on the digit strings.
"""
from automatic_relations import Rel
from collections import deque
import json

UNITS=((1,0),(0,1),(-1,0),(0,-1))
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def times(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def divbeta(z):
    x,y=z
    if (x+y)%2:return None
    return (-x+y)//2,(-x-y)//2

def encode(z):
    code=0;place=0
    while z!=(0,0):
        a=(z[0]+z[1])%2;code|=a<<place;place+=1
        z=divbeta((z[0]-a,z[1]));assert z is not None
    return code

def decode(code):
    z=(0,0);p=(1,0)
    while code:
        if code&1:z=plus(z,p)
        p=times(p,(-1,1));code>>=1
    return z

def neighbor(delta):
    states=[(-delta[0],-delta[1])];idx={states[0]:0};tr=[];ac=set()
    for i,c in enumerate(states):
        if c==(0,0):ac.add(i)
        row=[]
        for letter in range(4):
            a=letter&1;b=(letter>>1)&1
            nxt=None if c is None else divbeta((c[0]+b-a,c[1]))
            if nxt not in idx:idx[nxt]=len(states);states.append(nxt)
            row.append(idx[nxt])
        tr.append(row)
    return Rel(('z','w'),tr,ac).minimal()

def dragon_graph():
    # p(2n)=(1+i)p(n), p(2n+1)=(1+i)p(n)+i^(n mod2)d(n),
    # d(n)=i^popcount(n xor(n>>1)). A state means remaining cell z=r*p(n)+c,
    # with prescribed d(n) and the next time digit. r is a fourth root of unity.
    roots=[(0,(0,0),g,-1) for g in range(4)]
    states=list(roots);idx={s:i for i,s in enumerate(states)};tr=[];ac=set()
    for i,(r,c,g,expected) in enumerate(states):
        if c==(0,0) and g==0 and expected in (-1,0):ac.add(i)
        row=[]
        for letter in range(4):
            bit=letter&1;a=(letter>>1)&1;dest=set()
            if expected in (-1,bit):
                for e in [0,1]:
                    ng=(g-(e if bit==0 else 1-e))%4
                    u=UNITS[(r+e+ng)%4] if bit else (0,0)
                    nc=divbeta((c[0]+u[0]-a,c[1]+u[1]))
                    if nc is None:continue
                    assert nc[0]*nc[0]+nc[1]*nc[1]<=25
                    ns=((r-1)%4,nc,ng,e)
                    if ns not in idx:idx[ns]=len(states);states.append(ns)
                    dest.add(idx[ns])
            row.append(dest)
        tr.append(row)
    ss=[frozenset(range(4))];si={ss[0]:0};dt=[];da=set()
    for i,qset in enumerate(ss):
        if qset&ac:da.add(i)
        row=[]
        for a in range(4):
            ns=frozenset(j for q in qset for j in tr[q][a])
            if ns not in si:si[ns]=len(ss);ss.append(ns)
            row.append(si[ns])
        dt.append(row)
    return Rel(('t','z'),dt,da).minimal(),len(states),len(ss)

def dragon_left():
    # For n>0 the paperfolding turn is L iff its odd part is 1 modulo4.
    # State0: before first1; 1: first1 seen; 2: next digit0; 3: next digit1.
    return Rel(('t',),[[0,1],[2,3],[2,2],[3,3]],{1,2})

def controls():
    n=0
    for x in range(-30,31):
        for y in range(-30,31):assert decode(encode((x,y)))==(x,y);n+=1
    small=[]
    for x in range(-2,3):
        for y in range(-2,3):
            if x*x+y*y<=5:small.append({'point':[x,y],'code':encode((x,y))})
    grids=[]
    for delta in UNITS:
        r=neighbor(delta);checks=0
        for x in range(-12,13):
            for y in range(-12,13):
                z=(x,y);w=plus(z,delta)
                assert r.eval(z=encode(z),w=encode(w))
                assert not r.eval(z=encode(z),w=encode(z));checks+=2
        grids.append({'delta':delta,'states':len(r.tr),'checks':checks})
    graph,ns,ds=dragon_graph();left=dragon_left();p=(0,0);old={};bad=None
    for t in range(2048):
        code=encode(p);assert graph.eval(t=t,z=code)
        assert not graph.eval(t=t,z=encode(plus(p,(1,0))))
        turn='L' if left.eval(t=t) else 'R'
        if bad is None and p in old and old[p][1]==turn:bad={'time':t,'point':p,'turn':turn,'previous':old[p]}
        old[p]=(t,turn)
        d=UNITS[(t^(t>>1)).bit_count()%4];p=plus(p,d)
    assert bad=={'time':11,'point':(-2,1),'turn':'R','previous':(7,'R')}
    return {'status':'PASS','gaussian_encode_decode_controls':n,'small_norm_termination_codes':small,'unit_neighbor_automata':grids,'dragon_graph':{'nfa_states':ns,'unminimized_dfa_states':ds,'minimal_dfa_states':len(graph.tr),'point_and_nonpoint_controls':4096},'dragon_first_alternation_failure':bad,'scope':'Exact automatic geometric model; the dragon path is NOT an ant trajectory on any coloring.'}
if __name__=='__main__':print(json.dumps(controls(),indent=2))
