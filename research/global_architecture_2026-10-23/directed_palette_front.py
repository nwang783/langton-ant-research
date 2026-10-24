#!/usr/bin/env python3
"""Exact colored fronts for ONE supplied common-nonzero-drift finite palette.

No ant-word, period, cap, or architecture synthesis. Full graph decisions are
explicitly UNKNOWN above a caller-supplied state budget. Literal transitions
and supplied finite-cap prefix reachability are exact independently of that
budget. A prepared periodic background may have infinitely many black cells.
"""
from __future__ import annotations
import collections

DIRECTIONS=((0,1),(1,0),(0,-1),(-1,0))

def literal_trace(word, heading):
    if not isinstance(word,str) or not word or not set(word)<=set('LR'):
        raise ValueError('each supplied word must be a nonempty literal R/L word')
    if type(heading) is not int or not 0<=heading<4:
        raise ValueError('heading must be an integer0..3')
    x=y=0; h=heading; rows=[]
    for c in word:
        rows.append(((x,y),c=='L'))
        h=(h+(1 if c=='R' else -1))%4
        dx,dy=DIRECTIONS[h]; x+=dx; y+=dy
    return rows,(x,y),h

def multiple(p,d):
    axis=0 if d[0] else 1
    if p[axis]%d[axis]: return None
    k=p[axis]//d[axis]
    return k if p==(k*d[0],k*d[1]) else None

class FrontArchitecture:
    def __init__(self, words, heading=0):
        self.words=tuple(words)
        if not self.words: raise ValueError('a finite nonempty palette is required')
        traced=[literal_trace(w,heading) for w in self.words]
        self.heading=heading; self.drift=traced[0][1]
        if self.drift==(0,0): raise ValueError('common drift must be nonzero')
        if any(d!=self.drift or h!=heading for _,d,h in traced):
            raise ValueError('every supplied word must restore the same heading and drift')
        self.representatives=[]; self.levels=[]; self.rows=[]
        for raw,_,_ in traced:
            rows=[]
            for (x,y),black in raw:
                a,k=self.locate((x,y))
                if a is None:
                    a=len(self.representatives); k=0
                    self.representatives.append((x,y)); self.levels.append(set())
                self.levels[a].add(k); rows.append((a,k,black))
            self.rows.append(rows)
        self.lower=[min(k) for k in self.levels]
        self.upper=[max(k) for k in self.levels]
        self.front=tuple((a,z) for a in range(len(self.levels))
                         for z in range(self.lower[a],self.upper[a]))
        self.front_index={az:i for i,az in enumerate(self.front)}
        self.front_bits=len(self.front)

    def locate(self,cell):
        for a,rep in enumerate(self.representatives):
            k=multiple((cell[0]-rep[0],cell[1]-rep[1]),self.drift)
            if k is not None:return a,k
        return None,None

    def physical(self,a,k):
        r=self.representatives[a];d=self.drift
        return r[0]+k*d[0],r[1]+k*d[1]

    def geometry(self):
        return dict(words=list(self.words),heading=self.heading,drift=self.drift,
                    front_bits=self.front_bits,front=list(self.front),
                    orbits=[dict(representative=r,levels=sorted(k),lower=l,upper=u)
                            for r,k,l,u in zip(self.representatives,self.levels,
                                              self.lower,self.upper)])

class PeriodicFront:
    def __init__(self,architecture,profiles):
        self.architecture=architecture
        self.profiles=tuple(tuple(row) for row in profiles)
        if len(self.profiles)!=len(architecture.levels) or not self.profiles:
            raise ValueError('one periodic input row per full-drift orbit is required')
        self.period=len(self.profiles[0])
        if not self.period or any(len(row)!=self.period or any(b not in (0,1) for b in row)
                                  for row in self.profiles):
            raise ValueError('input rows must have one common positive period and binary bits')
        self.state_count=self.period*(1<<architecture.front_bits)

    def background(self,a,k):return self.profiles[a][k%self.period]

    def edges(self,state, fresh_flips=frozenset()):
        """Edges for (input phase, packed front); fresh_flips contains orbit IDs.

        Only each orbit's single top cell is fresh at one frame boundary.
        The same finite override is used for every alternative block choice.
        """
        phase,bits=state;a=self.architecture
        if not 0<=phase<self.period or not 0<=bits<(1<<a.front_bits):
            raise ValueError('front state out of range')
        initial={az:(bits>>i)&1 for i,az in enumerate(a.front)}
        for orbit,u in enumerate(a.upper):
            initial[orbit,u]=self.background(orbit,phase+u)^(orbit in fresh_flips)
        result=[]
        for label,rows in enumerate(a.rows):
            colors=initial.copy()
            for orbit,k,required in rows:
                if colors[orbit,k]!=required:break
                colors[orbit,k]^=1
            else:
                newbits=sum(colors[orbit,z+1]<<i for i,(orbit,z) in enumerate(a.front))
                result.append((((phase+1)%self.period,newbits),label))
        return result

    def initial_state(self,cap=()):
        cap=set(map(tuple,cap));a=self.architecture
        bits=sum((self.background(orbit,z)^(a.physical(orbit,z) in cap))<<i
                 for i,(orbit,z) in enumerate(a.front))
        return 0,bits

    def cap_prefix(self,cap=(), max_prefix=100000):
        """Exact all-choice reachability through the last exceptional fresh input.

        Caps are XOR flips relative to the prepared background. Cells initially
        in the front are handled by initial_state; cells behind it never read.
        This method never truncates a nonempty prefix and calls it impossible.
        """
        cap=set(map(tuple,cap));a=self.architecture;events={}
        for cell in cap:
            orbit,k=a.locate(cell)
            if orbit is not None and k>=a.upper[orbit]:
                n=k-a.upper[orbit];events.setdefault(n,set()).add(orbit)
        stop=max(events,default=-1)+1
        if stop>max_prefix:
            return dict(status='UNKNOWN_PREFIX_BUDGET',prefix_blocks=stop,
                        budget=max_prefix)
        states={self.initial_state(cap)}
        for n in range(stop):
            states={v for state in states for v,_ in self.edges(state,events.get(n,()))}
            if not states:
                return dict(status='FINITE_PREFIX_IMPOSSIBLE',prefix_blocks=n+1,states=[])
        return dict(status='EXACT_PREFIX',prefix_blocks=stop,states=sorted(states))

    def decide(self,cap=None,max_states=100000,max_prefix=100000):
        """Cycle decision. cap=None means SOME finite cap, not the empty cap.

        A positive result includes exact labeled cycle and finite-cap witness
        (unknown-cap mode), or a finite exceptional-prefix reachable set and a
        reachable cycle (specified-cap mode). No huge graph is silently pruned.
        """
        a=self.architecture
        if self.state_count>max_states:
            return dict(status='UNKNOWN_STATE_BUDGET',state_count=self.state_count,
                        budget=max_states,scope='No negative feasibility claim.')
        if cap is None:
            starts=[(0,b) for b in range(1<<a.front_bits)]
            prefix=None
        else:
            prefix=self.cap_prefix(cap,max_prefix)
            if prefix['status']!='EXACT_PREFIX':return prefix
            starts=prefix['states']
        # Iterative depth-first search. State colors are exact graph states;
        # completed subgraphs need not be explored again from another start.
        color={};predecessor={};depth={};finish=[]
        cycle=None
        for root in starts:
            if color.get(root):continue
            color[root]=1;depth[root]=0;predecessor[root]=None
            stack=[(root,iter(self.edges(root)))]
            while stack:
                v,iterator=stack[-1]
                edge=next(iterator,None)
                if edge is None:
                    color[v]=2;finish.append(v);stack.pop();continue
                w,label=edge
                if not color.get(w):
                    color[w]=1;depth[w]=depth[v]+1;predecessor[w]=(v,label)
                    stack.append((w,iter(self.edges(w))))
                elif color[w]==1:
                    # Recover the cycle w -> ... -> v -> w.
                    reverse=[];u=v
                    while u!=w:
                        old,oldlabel=predecessor[u]
                        reverse.append((old,oldlabel,u));u=old
                    cycle=list(reversed(reverse))+[(v,label,w)]
                    break
            if cycle is not None:break
        base=dict(state_count=self.state_count,states_explored=len(color),
                  front_bits=a.front_bits,input_period=self.period,
                  mode='some_finite_extra_cap' if cap is None else 'specified_finite_extra_cap')
        if prefix is not None:base['prefix_blocks']=prefix['prefix_blocks']
        if cycle is None:
            # finish order has targets before sources; all explored vertices
            # are acyclic, so this is an exact path-length certificate.
            longest={}
            for v in finish:
                longest[v]=max((1+longest[w] for w,_ in self.edges(v)),default=0)
            return dict(**base,status='NO_INFINITE_SCHEDULE',
                        max_remaining_blocks=max((longest[s] for s in starts),default=0))
        # Rotate unknown-cap cycle to a phase-zero vertex. A cycle's clock
        # length is divisible by the input period, so phase zero occurs.
        if cap is None:
            cut=next(i for i,e in enumerate(cycle) if e[0][0]==0)
            cycle=cycle[cut:]+cycle[:cut]
        result=dict(**base,status='INFINITE_SCHEDULE',cycle=[dict(source=s,label=i,target=t)
                                                          for s,i,t in cycle],
                    cycle_word=''.join(a.words[i] for _,i,_ in cycle))
        if cap is None:
            bits=cycle[0][0][1]
            result['witness_cap']=[a.physical(orbit,z) for i,(orbit,z) in enumerate(a.front)
                                  if ((bits>>i)&1)!=self.background(orbit,z)]
        else:
            # Recover a periodic-graph entry path from the explored prefix root.
            u=cycle[0][0];entry=[]
            while predecessor[u] is not None:
                v,label=predecessor[u];entry.append(dict(source=v,label=label,target=u));u=v
            result['graph_entry_path']=list(reversed(entry))
            result['graph_entry_state']=u
        return result
