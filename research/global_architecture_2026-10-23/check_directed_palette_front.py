#!/usr/bin/env python3
"""Author controls, not an independent audit or general architecture scan."""
import hashlib,itertools,json,pathlib
from directed_palette_front import FrontArchitecture,PeriodicFront,DIRECTIONS
HERE=pathlib.Path(__file__).resolve().parent

def direct(p,state,word,flips=()):
    """Separate physical-coordinate board replay for one frame transition."""
    a=p.architecture;phase,bits=state;n=phase
    board={a.physical(orbit,n+z):(bits>>i)&1
           for i,(orbit,z) in enumerate(a.front)}
    for orbit,u in enumerate(a.upper):
        board[a.physical(orbit,n+u)]=p.background(orbit,n+u)^(orbit in flips)
    x=n*a.drift[0];y=n*a.drift[1];h=a.heading
    for c in word:
        orbit,k=a.locate((x,y));assert orbit is not None
        got=board.get((x,y),p.background(orbit,k))
        if got!=(c=='L'):return None
        board[x,y]=got^1
        h=(h+(1 if c=='R' else -1))%4
        dx,dy=DIRECTIONS[h];x+=dx;y+=dy
    assert (x,y)==((n+1)*a.drift[0],(n+1)*a.drift[1]) and h==a.heading
    out=0
    for i,(orbit,z) in enumerate(a.front):
        pos=a.physical(orbit,n+1+z)
        out|=board.get(pos,p.background(orbit,n+1+z))<<i
    return ((phase+1)%p.period,out)

def brute_cycle(p,starts):
    """Independent transitive-closure oracle on tiny explicit graphs."""
    states=[(phase,b) for phase in range(p.period)
            for b in range(1<<p.architecture.front_bits)]
    index={s:i for i,s in enumerate(states)}
    reach=[0 for _ in states]
    for s in states:
        for t,_ in p.edges(s):reach[index[s]]|=1<<index[t]
    for k in range(len(states)):
        for i in range(len(states)):
            if reach[i]>>k&1:reach[i]|=reach[k]
    cyclic=[i for i in range(len(states)) if reach[i]>>i&1]
    return any(index[s]==i or (reach[index[s]]>>i&1) for s in starts for i in cyclic)

def replay_cycle(p,result,repetitions=8):
    assert result['status']=='INFINITE_SCHEDULE'
    state=result['cycle'][0]['source'];state=tuple(state)
    for _ in range(repetitions):
        for e in result['cycle']:
            assert state==tuple(e['source'])
            expected=tuple(e['target'])
            assert direct(p,state,p.architecture.words[e['label']])==expected
            state=expected
    if result['mode']=='some_finite_extra_cap':
        assert p.initial_state(result['witness_cap'])==tuple(result['cycle'][0]['source'])

summary=dict(scope='Author controls for supplied finite palettes; no general ant reduction.',
             physical_transition_equalities=0,cycle_oracle_comparisons=0,
             infinite_witness_replays=0,cases=[])
# Every color profile for these small explicitly supplied literal palettes.
for words in [('RL',),('RL','RLRRRR'),('LR','LRLLLL'),('RLLR','RLLRRRRR')]:
 for heading in range(4):
  a=FrontArchitecture(words,heading)
  for period in (1,2):
   for pattern in itertools.product((0,1),repeat=len(a.levels)*period):
    profiles=[pattern[j*period:(j+1)*period] for j in range(len(a.levels))]
    p=PeriodicFront(a,profiles)
    for phase in range(period):
     for bits in range(1<<a.front_bits):
      state=(phase,bits);edges=dict((label,t) for t,label in p.edges(state))
      for label,w in enumerate(words):
       assert direct(p,state,w)==edges.get(label)
       summary['physical_transition_equalities']+=1
    result=p.decide(max_states=64)
    expected=brute_cycle(p,[(0,b) for b in range(1<<a.front_bits)])
    assert (result['status']=='INFINITE_SCHEDULE')==expected
    summary['cycle_oracle_comparisons']+=1
    if expected:
     replay_cycle(p,result);summary['infinite_witness_replays']+=1
# Actual finite-cap effects, including a remote failure after a valid prefix.
a=FrontArchitecture(['RL'])
p=PeriodicFront(a,[[0,0],[1,1]])
for cap,want in [((),True),([a.physical(0,50)],False),
                 ([a.physical(1,37)],False),([a.physical(0,-5)],True)]:
 result=p.decide(cap=cap,max_states=64)
 assert (result['status']=='INFINITE_SCHEDULE')==want
 if want:replay_cycle(p,result)
 summary['cases'].append(dict(name='specified_cap',cap=cap,result=result))
assert p.decide(cap=[a.physical(0,50)],max_prefix=10)['status']=='UNKNOWN_PREFIX_BUDGET'
assert p.decide(max_states=1)['status']=='UNKNOWN_STATE_BUDGET'
# Nontrivial retained standard flight:18-bit front, known finite seed.
standard=json.loads((HERE.parent/'recovered_bundle/ant_global/root/standard.json').read_text())
H=standard['word'];a=FrontArchitecture([H],standard['heading'])
p=PeriodicFront(a,[[0] for _ in a.levels])
r=p.decide(cap=standard['seed'],max_states=1<<19)
assert r['status']=='INFINITE_SCHEDULE';replay_cycle(p,r)
summary['cases'].append(dict(name='retained_standard_white_input',front_bits=a.front_bits,result=r))
# Signed prepared108 control: the background has11 infinite black orbits.
rev=''.join('L' if c=='R' else 'R' for c in H[::-1])
P=rev[:31]+'LRRRR'+rev[32:]
a=FrontArchitecture([P],3);profiles=[];bits=0
for orbit in range(len(a.levels)):
 events=sorted((i-len(P)*k,i,k,b) for i,(o,k,b) in enumerate(a.rows[0]) if o==orbit)
 assert all(x[3]!=y[3] for x,y in zip(events,events[1:]))
 profiles.append([int(events[0][3])])
 for z in range(a.lower[orbit],a.upper[orbit]):
  bit=int(events[0][3])^(sum(i+len(P)*(z-k)<0 for _,i,k,_ in events)%2)
  bits|=bit<<a.front_index[orbit,z]
p=PeriodicFront(a,profiles)
cap=[a.physical(o,z) for i,(o,z) in enumerate(a.front)
     if ((bits>>i)&1)!=p.background(o,z)]
r=p.decide(cap=cap,max_states=1<<20)
assert r['status']=='INFINITE_SCHEDULE' and sum(row[0] for row in profiles)==11
assert a.front_bits==19 and len(cap)==13
replay_cycle(p,r)
summary['cases'].append(dict(name='retained_prepared108_infinite_black_input',
                             front_bits=a.front_bits,black_input_orbits=11,
                             extra_finite_color_flips=cap,result=r))
# Unsupported architectures fail explicitly, never as a negative graph answer.
for words in [[],['RRRR'],['RL','LR'],['R'],['']]:
 try:FrontArchitecture(words)
 except ValueError:pass
 else:raise AssertionError(('accepted invalid architecture',words))
summary['source_sha256']=hashlib.sha256((HERE/'directed_palette_front.py').read_bytes()).hexdigest()
(HERE/'directed_palette_front_controls.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='cases'},indent=2))
