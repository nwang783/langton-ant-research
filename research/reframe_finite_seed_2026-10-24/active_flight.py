"""Exact capped active-w flight planner. No complete field is discarded.
The isolated component is only a motion predictor; the full frozen archive,
including every emitted component, is checked before an actual R import.
Coordinates of graph vertices are doubled; physical cell coordinates are not.
"""
from dataclasses import dataclass
from typing import Optional

DIR=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
    x,y=q
    for _ in range(h): x,y=y,-x
    return x,y
def cursor(p,h):
    x,y=rot((1,-1),h)
    return 2*p[0]+x,2*p[1]+y
def ends(q,k):
    x,y=q;s=1 if (x+y)%2==k else -1
    return ((2*x-1,2*y-s),(2*x+1,2*y+s))
def sector(p,h):
    w=cursor(p,h)
    return next(k for k in (0,1) if w in ends(p,k))
def vertices(B,k): return {v for q in B for v in ends(q,k)}
def comp(B,k,w):
    g={}
    for q in B:
        a,b=ends(q,k);g.setdefault(a,[]).append((b,q));g.setdefault(b,[]).append((a,q))
    todo=[w];seen={w};C=set()
    for a in todo:
        for b,q in g.get(a,()):
            C.add(q)
            if b not in seen:seen.add(b);todo.append(b)
    return C
def step(B,p,h):
    if p in B:B.remove(p);h=(h-1)%4
    else:B.add(p);h=(h+1)%4
    return (p[0]+DIR[h][0],p[1]+DIR[h][1]),h

def ray_epoch(v,q,d):
    """Integer n such that v=q+n*d, or None; d is nonzero."""
    n=None
    for a,b,c in zip(v,q,d):
        if c:
            if (a-b)%c:return None
            x=(a-b)//c
            if n is not None and n!=x:return None
            n=x
        elif a!=b:return None
    assert n is not None
    return n

def shape(C,p,h):return h,tuple(sorted((x-p[0],y-p[1])for x,y in C))

@dataclass
class Phase:
    p:tuple
    h:int
    C:frozenset
    turn:str
    query:Optional[tuple] # nonactive endpoint of an R, else None
    emitted:frozenset    # complete lost edge components, after this update

@dataclass
class Plan:
    status:str # 'import', 'cap', 'translator'
    event:int  # zero-based update for import, first pre-update cut for cap
    cap:int
    preperiod:int
    period:int
    drift:tuple
    phases:list
    initial_archive:frozenset
    k:int
    witness:Optional[dict]=None

    def state_at(self,t,limit=1_000_000):
        """Materialize exact complete state at any cut up to event.
        The scalable alternative is archive_terms(), which never expands k.
        """
        assert t>=0 and (self.status=='translator' or t<=self.event)
        ph,terms=self.archive_terms(t)
        B=set(ph.C)
        for base,d,count in terms:
            if len(base)*count>limit:raise ValueError('Use archive_terms for this exact large finite field')
            for n in range(count):B.update((x+n*d[0],y+n*d[1])for x,y in base)
        return B,ph.p,ph.h

    def archive_terms(self,t):
        """Exact complete field is active.C UNION all finite translated terms.
        Each term is (finite edge set, physical drift, number of copies).
        Repeated archive terms are never erased or XOR-cancelled.
        """
        assert t>=0 and (self.status=='translator' or t<=self.event)
        terms=[(self.initial_archive,(0,0),1)]
        if self.period==0 or t<self.preperiod:
            for ph in self.phases[:t]:
                if ph.emitted:terms.append((ph.emitted,(0,0),1))
            ph=self.phases[t]
            return ph,terms
        a=self.preperiod;P=self.period;k,i=divmod(t-a,P)
        for ph in self.phases[:a]:
            if ph.emitted:terms.append((ph.emitted,(0,0),1))
        for ph in self.phases[a:a+P]:
            if ph.emitted and k:terms.append((ph.emitted,self.drift,k))
        for ph in self.phases[a:a+i]:
            if ph.emitted:terms.append((frozenset((x+k*self.drift[0],y+k*self.drift[1])for x,y in ph.emitted),(0,0),1))
        ph=self.phases[a+i]
        C=frozenset((x+k*self.drift[0],y+k*self.drift[1])for x,y in ph.C)
        p=(ph.p[0]+k*self.drift[0],ph.p[1]+k*self.drift[1])
        return Phase(p,ph.h,C,ph.turn,None,frozenset()),terms

def prefix_collision(initial,phases,k):
    AV=vertices(initial,k)
    for t,ph in enumerate(phases):
        if ph.query is not None and ph.query in AV:
            return t,{'kind':'finite_prefix','vertex':ph.query}
        AV.update(vertices(ph.emitted,k))
    return None

def plan(B0,p0=(0,0),h0=0,M=50):
    """Total mathematical algorithm for finite B0 and finite M.
    Stop before first nonempty dormant import, at first cap failure, or
    certify an infinite nonzero translating no-import future.
    If import and post-R cap failure coincide, import has priority.
    """
    assert M>=0
    B0=set(B0);p=p0;h=h0;k=sector(p,h);C=comp(B0,k,cursor(p,h))
    initial=frozenset(B0-C)
    phases=[];seen={}
    while True:
        t=len(phases)
        if len(C)>M:
            phases.append(Phase(p,h,frozenset(C),'?',None,frozenset()))
            hit=prefix_collision(initial,phases[:t],k)
            if hit is not None:
                when,wit=hit
                return Plan('import',when,M,t,0,(0,0),phases,initial,k,wit)
            return Plan('cap',t,M,t,0,(0,0),phases,initial,k)
        key=shape(C,p,h)
        if key in seen:
            a=seen[key];P=t-a;d=(p[0]-phases[a].p[0],p[1]-phases[a].p[1]);D=(2*d[0],2*d[1])
            assert (d[0]+d[1])%2==0
            # A_static contains initial and preperiod archives ONLY.
            static=set(initial)
            for ph in phases[:a]:static.update(ph.emitted)
            SV=vertices(static,k);hit=prefix_collision(initial,phases[:a],k)
            best,wit=(None,None)if hit is None else hit
            for i,ph in enumerate(phases[a:]):
                q=ph.query
                if q is None:continue
                # Static old/preperiod archive.
                for v in SV:
                    if D==(0,0):n=0 if q==v else None
                    else:n=ray_epoch(v,q,D)
                    if n is not None and n>=0:
                        z=a+n*P+i
                        if best is None or z<best:best=z;wit={'kind':'static','phase':i,'epoch':n,'vertex':v}
                # All emitted components of ALL earlier copies, not only rays
                # meeting the active read cells.
                for j,dh in enumerate(phases[a:]):
                    for v in vertices(dh.emitted,k):
                        if D==(0,0):n=(0 if j<i else 1) if q==v else None
                        else:n=ray_epoch(v,q,D)
                        if n is None or n<0 or (n==0 and j>=i):continue
                        z=a+n*P+i
                        if best is None or z<best:best=z;wit={'kind':'periodic_emission','query_phase':i,'dump_phase':j,'epoch_gap':n,'vertex':v}
            # The prediction may already have diverged. Only the EARLIEST
            # causal query/archive collision is reported; all later phases are
            # hypothetical and do not assert actual execution.
            if best is not None:
                return Plan('import',best,M,a,P,d,phases,initial,k,wit)
            assert d!=(0,0),'A zero-drift archive-free cycle contradicts no bounded ant orbit'
            return Plan('translator',-1,M,a,P,d,phases,initial,k)
        seen[key]=t
        w=cursor(p,h);q=None;turn='L'if p in C else'R'
        if turn=='R':
            u,v=ends(p,k);assert w in(u,v);other=v if u==w else u
            if other not in vertices(C,k)|{w}:
                q=other
        old=frozenset(C);new=set(C);pn,hn=step(new,p,h)
        Cn=comp(new,k,cursor(pn,hn));emitted=frozenset(new-Cn)
        if turn=='R':assert not emitted
        # Emissions after the first collision are hypothetical. Their precise
        # birth phase is retained; no overlapping emissions are XOR-cancelled.
        phases.append(Phase(p,h,old,turn,q,emitted));C=Cn;p=pn;h=hn
