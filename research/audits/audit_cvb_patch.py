"""Independent C/V/B audit, using last-read letters rather than current colors."""
import json
from pathlib import Path
from collections import deque

ROOT=Path('/workspace/shared/langton')
WORDS={'C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR',
       'B':'LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRR'}
source=json.loads((ROOT/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json').read_text())
assert all(source[k]['word']==w for k,w in WORDS.items())
D=((0,1),(1,0),(0,-1),(-1,0))
PATCH=tuple((x,y) for x in range(-1,4) for y in range(0,5))
INDEX={p:i for i,p in enumerate(PATCH)}
NOSE=(1,2);QBIT=1<<INDEX[NOSE];OUT=None

def trace(p,h,w):
    out=[]
    for c in w:
        assert c in 'RL'
        out.append((p,c=='L'))
        h=(h+(1 if c=='R' else -1))%4
        p=(p[0]+D[h][0],p[1]+D[h][1])
    return out,(p,h)

def pose(a,b,h):
    f,r=D[h],D[(h+1)%4]
    x,y=-1+2*a-6*b-f[0]+r[0],1+6*a+2*b-f[1]+r[1]
    assert x%2==y%2==0
    return (x//2,y//2),h

def inverse(p,h):
    f,r=D[h],D[(h+1)%4]
    X,Y=2*p[0]+f[0]-r[0]+1,2*p[1]+f[1]-r[1]-1
    a,b=X+3*Y,-3*X+Y
    if a%20 or b%20:return None
    return a//20,b//20,h

centers=set()
for q in PATCH:
    for h in range(4):
        for w in WORDS.values():
            relative,_=trace((0,0),h,w)
            for d,_ in relative:
                state=inverse((q[0]-d[0],q[1]-d[1]),h)
                if state is not None:centers.add(state[:2])
heads={(a,b,h) for a,b in centers for h in range(4)}
trans={};initial=set();sources=[];macro_moves={}
for name,w in WORDS.items():
    for h in range(4):
        _,(p,eh)=trace(*pose(0,0,h),w)
        end=inverse(p,eh);assert end is not None
        da,db=((1,0),(0,-1),(-1,0),(0,1))[h]
        expected={'C':(0,0,(h-1)%4),'V':(da,db,h),'B':(-2*da,-2*db,(h+2)%4)}[name]
        assert end==expected
        macro_moves[name,h]=end

for head in heads:
    for name,w in WORDS.items():
        visits,(end,eh)=trace(*pose(*head),w)
        dest=inverse(end,eh);assert dest is not None
        da,db,eh_expected=macro_moves[name,head[2]]
        assert dest==(head[0]+da,head[1]+db,eh_expected)
        dest=dest if dest in heads else OUT
        local=[(1<<INDEX[q],isL) for q,isL in visits if q in INDEX]
        trans[head,name]=dest,local
        qreads=[isL for q,isL in visits if q==NOSE]
        if qreads and not qreads[-1]:
            known=lastL=0
            for bit,isL in local:
                known|=bit
                if isL:lastL|=bit
                else:lastL&=~bit
            initial.add((dest,known,lastL));sources.append((head,name))

# Derive every possible reentry from the literal endpoint transformations.
boundary=set()
for a,b,h in heads:
    for (name,oldh),(da,db,newh) in macro_moves.items():
        if newh==h and (a-da,b-db) not in centers:boundary.add((a,b,h))

def successors(state):
    head,known,lastL=state
    assert known&QBIT and not lastL&QBIT and lastL&~known==0
    if head is OUT:return {(h,known,lastL) for h in boundary}
    out=set()
    for name in WORDS:
        dest,local=trans[head,name]
        target=head==(0,0,0) and name=='V'
        if not target and any(bit==QBIT for bit,_ in local):continue
        nk,nl=known,lastL
        for bit,isL in local:
            if nk&bit and bool(nl&bit)==isL:break
            nk|=bit
            if isL:nl|=bit
            else:nl&=~bit
        else:
            assert not target,('ABSTRACT REUSE',state)
            out.add((dest,nk,nl))
    return out

closure=set(initial);queue=deque(initial)
while queue:
    state=queue.popleft()
    for nxt in successors(state):
        if nxt not in closure:closure.add(nxt);queue.append(nxt)
# Recheck the final set as a closed inductive certificate.
assert initial<=closure
for state in closure:assert successors(state)<=closure

def conflict(word):
    visits,_=trace((0,0),0,word);last={}
    for t,(q,isL) in enumerate(visits):
        if q in last and last[q][1]==isL:return (q,last[q][0],t,'L' if isL else 'R')
        last[q]=(t,isL)
    return None

short_conflicts={}
for following,w in WORDS.items():
    bad=conflict(WORDS['C']*4+w)
    assert bad==((2,1),7,67,'R')
    short_conflicts['CCCC'+following]=bad
for k in range(4):
    bad=conflict(WORDS['B']+WORDS['C']*k+WORDS['B'])
    assert bad is not None
    short_conflicts['B'+'C'*k+'B']=bad

out=dict(status='PASS: V nose is unread earlier in any feasible C/V/B concatenation',
         patch=PATCH,sensitive_centers=sorted(centers),head_states=len(heads)+1,
         source_macros=sorted(sources),initial_states=len(initial),
         reachable_states=len(closure),outside_states=sum(h is OUT for h,k,l in closure),
         short_conflicts=short_conflicts,finite_support_macro_bound='8*m+8')
(ROOT/'audits/cvb_patch_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
