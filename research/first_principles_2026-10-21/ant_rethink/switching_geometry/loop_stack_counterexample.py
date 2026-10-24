"""Find exact failure of LIFO reattachment of discarded frozen loops."""
import json
from pathlib import Path
from active_loops import step,loop

p=(0,0);h=3;black=set();stack=[];events=[];first=None
for t in range(2000):
    states,area=loop(p,h,black)
    other=(p,(h+2)%4)
    if other in states:
        i=states.index(other)
        assert i>0
        discarded=frozenset(states[i+1:]+states[:1])
        stack.append((t,discarded))
        events.append({'t':t,'operation':'split','active_length':i,
                       'discarded_length':len(discarded),'position':p,'heading':h})
    else:
        ostates,oarea=loop(p,(h+2)%4,black)
        target=frozenset(ostates)
        found=[j for j,(born,c) in enumerate(stack) if c==target]
        if found:
            assert len(found)==1
            j=found[0]
            event={'t':t,'operation':'reattach','born':stack[j][0],
                   'loop_length':len(target),'newer_still_discarded':[a for a,c in stack[j+1:]],
                   'position':p,'heading':h}
            events.append(event)
            if j!=len(stack)-1 and first is None:
                first=event|{'all_events':events.copy(),'black':sorted(black)}
                break
            stack.pop(j)
    p,h=step(p,h,black,True)
assert first is not None
Path(__file__).with_name('loop_stack_counterexample.json').write_text(json.dumps(first,indent=2))
print(json.dumps(first,indent=2))
