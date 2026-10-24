#!/usr/bin/env python3
"""Automatic cell-equality relation for a uniformly self-similar turtle walk."""
from automatic_radix import Rel,linear,reverse_msb
from math import isqrt
from collections import deque
import json,time
D=((0,1),(1,0),(0,-1),(-1,0))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def rot(p,h):
    for _ in range(h%4):p=p[1],-p[0]
    return p

def macros(u,v):
    if len(u)<=1 or len(u)!=len(v) or set(u+v)-set('RL') or u[0]!='R':raise ValueError('R/L words, uniform length k>1, and prolongable on R required')
    ws=[u,v];ps=[];hs=[]
    for w in ws:
        p=(0,0);h=0;pp=[];hh=[]
        for c in w:
            pp.append(p);hh.append(h);h=(h+(1 if c=='R'else -1))%4;p=add(p,D[h])
        ps.append(pp);hs.append(hh)
        if len(ps)==1:a=p;assert h==1
        else:assert p==(-a[0],-a[1])and h==3
    assert a[0]**2+a[1]**2>1
    return ws,ps,hs,a

def state_tables(u,v):
    ws,ps,hs,a=macros(u,v);states=[(h,c)for h in range(4)for c in range(2)]
    ix={s:i for i,s in enumerate(states)};nxt=[];off=[]
    for h,c in states:
        nxt.append([ix[((h+hs[c][j])%4,int(ws[c][j]=='L'))]for j in range(len(u))])
        off.append([rot(ps[c][j],h)for j in range(len(u))])
    return nxt,off,a

def equality(u,v):
    b=len(u);nxt,off,a=state_tables(u,v);norm=a[0]**2+a[1]**2
    maxq=max(x*x+y*y for row in off for x,y in row);m=isqrt(maxq)
    if m*m<maxq:m+=1
    delta=2*m;R=0
    while norm*R*R<(R+delta)**2:R+=1
    # State: two prefix (heading,letter) states and their exact position difference.
    st=[(0,0,(0,0))];ix={st[0]:0};tr=[];ac=set()
    for i,state in enumerate(st):
        if state is not None and state[2]==(0,0):ac.add(i)
        row=[]
        for code in range(b*b):
            j=code%b;l=code//b;ns=None
            if state is not None:
                q,r,d=state;nd=add(mul(a,d),sub(off[q][j],off[r][l]))
                if nd[0]**2+nd[1]**2<=R*R:ns=(nxt[q][j],nxt[r][l],nd)
            if ns not in ix:ix[ns]=len(st);st.append(ns)
            row.append(ix[ns])
        tr.append(row)
    msb=Rel(('s','t'),tr,ac,b).minimal();lsb=reverse_msb(msb)
    return lsb,{'scale':a,'carry_radius':R,'raw_msb_states':len(st),'min_msb_states':len(msb.tr),'lsb_states':len(lsb.tr)}

def left_relation(u,v):
    return reverse_msb(Rel(('t',),[[int(c=='L')for c in u],[int(c=='L')for c in v]],{1},len(u)))

def point(t,u,v):
    b=len(u);nxt,off,a=state_tables(u,v);ds=[]
    while t:ds.append(t%b);t//=b
    p=(0,0);q=0
    for d in reversed(ds):p=add(mul(a,p),off[q][d]);q=nxt[q][d]
    return p

def inverse_tests(eq,left):
    b=eq.base
    earlier=linear(b,{'t':1,'s':-1},1,'>=')
    first=left&~(eq&earlier).exists('s')
    # eq(s,t); compare t,u with no intermediate s at that cell.
    etu=eq.rename(s='t',t='u')
    between=eq&linear(b,{'s':1,'t':-1},1,'>=')&linear(b,{'u':1,'s':-1},1,'>=')
    bad=etu&linear(b,{'u':1,'t':-1},1,'>=')&~between.exists('s')&left.iff(left.rename(t='u'))
    return {'first_left_times_finite':first.bounded(),'first_left_dfa_states':len(first.tr),'bad_alternation_witness':bad.witness(),'bad_alternation_dfa_states':len(bad.tr),'repeated_cell_witness':(eq&~linear(b,{'s':1,'t':-1},0)).witness()}

def main():
    out=[]
    for u,v in [('RRL','LRL'),('RLR','LLR'),('RRRLL','LRRLL'),('RLRLLLLRL','LRLRRRRLR')]:
        start=time.monotonic();eq,meta=equality(u,v);left=left_relation(u,v)
        checks=0
        ps=[point(i,u,v)for i in range(100)]
        for s in range(100):
            for t in range(100):assert eq.eval(s=s,t=t)==(ps[s]==ps[t]);checks+=1
        tests=inverse_tests(eq,left)
        out.append({'R':u,'L':v,**meta,'finite_point_controls':checks,**tests,'elapsed_seconds':time.monotonic()-start})
    from pathlib import Path
    (Path(__file__).resolve().parent/'selfsimilar_visit_controls.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
