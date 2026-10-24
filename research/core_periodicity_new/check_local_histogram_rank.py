"""One physical rail traversal preserves every fixed-radius pattern histogram."""
import contextlib, io, json
from pathlib import Path
from collections import Counter
with contextlib.redirect_stdout(io.StringIO()):
    from check_reversal_rank_obstruction import step, event, F

def patch(B,p,R):
    return tuple((x-p[0],y-p[1]) for x,y in sorted(B)
                 if abs(x-p[0])<=R and abs(y-p[1])<=R)
def histogram(B,R):
    # Count each nonempty translated square patch exactly once.
    centers={(x+dx,y+dy) for x,y in B for dx in range(-R,R+1) for dy in range(-R,R+1)}
    return Counter(patch(B,p,R) for p in centers)
def components(B):
    unseen=set(B);out=[]
    while unseen:
        p=unseen.pop();todo=[p];C={p}
        while todo:
            x,y=todo.pop()
            for q in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if q in unseen:unseen.remove(q);C.add(q);todo.append(q)
        x0=min(x for x,y in C);y0=min(y for x,y in C)
        out.append(tuple(sorted((x-x0,y-y0) for x,y in C)))
    return Counter(out)
def test(R,n):
    M=max(12,4*R+2)
    B0=frozenset({(0,y) for y in range(-M,0)}|{(1,y) for y in range(0,2*n+M)})
    X=(B0,(0,0),0);s=X;windows=set();word=''
    for _ in range(4*n):
        e=event(s);assert e['left_J'] and e['right_J'];windows.add(e['eleven'])
        s,a=step(s);word+=a
    B1=frozenset({(0,y) for y in range(-M,2*n)}|{(1,y) for y in range(2*n,2*n+M)})
    assert s==(B1,(0,2*n),0) and word=='RLLR'*n
    H0=histogram(B0,R);H1=histogram(B1,R)
    assert H0==H1
    assert patch(B0,X[1],R)==patch(B1,s[1],R)
    assert components(B0)==components(B1)
    assert {(1-x,2*n-1-y) for x,y in B0}==set(B1)
    return {'radius':R,'n':n,'padding':M,'mass':len(B0),'steps':4*n,
            'nonempty_pattern_types':len(H0),'patch_centers':sum(H0.values()),
            'K11_windows':sorted(windows),'components':[M,2*n+M]}
assert all(('RLLR'*4)[i:i+10] not in F for i in range(4))
out={'cases':[test(R,n) for R in range(7) for n in (1,2,5,13,30)]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
