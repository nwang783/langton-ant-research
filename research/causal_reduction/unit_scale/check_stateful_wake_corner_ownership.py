from pathlib import Path
import json,hashlib
from probe_perpendicular_highway_wake import H,step
from certify_highway_wake_reflector import trace
P=Path(__file__).resolve().parent
a=json.loads((P/'stateful_wake_corner_second_hit.json').read_text());b=json.loads((P/'stateful_wake_corner_third_hit.json').read_text())
expected=H*6+a['word'];actual=b['word'];i=next(i for i,(x,y)in enumerate(zip(expected,actual))if x!=y)
rr,p,h=trace(actual[:i],(327,-300),0);assert(i,p,h,expected[i],actual[i])==(12016,(91,-66),0,'R','L')
assert p in set(map(tuple,a['first_output_black'])) and p in set(map(tuple,b['initial_black']))
Q=(a['word']+H[a['phase']:])[110*104:];r,end,head=trace(Q,(95,-80),0)
assert(len(Q),end,head,len({q for q,_,_ in r}))==(1895,(83,-59),1,707)
q=(80,-73);one=[(j,c)for j,(x,_,c)in enumerate(r)if x==q];two=[(j,c)for j,(x,_,c)in enumerate(r)if(x[0],x[1]+12)==q]
assert one[-1]==(614,'R') and two[0]==(222,'R')
r1,_,_=trace(H,(83,-59),1);r2,_,_=trace(H,(327,-300),0)
b1=[min(x-y for(x,y),_,_ in r1),max(x-y for(x,y),_,_ in r1)];b2=[min(x+y for(x,y),_,_ in r2),max(x+y for(x,y),_,_ in r2)]
assert b1==[135,145] and b2==[20,30] and not b1[0]<=q[0]-q[1]<=b1[1] and not b2[0]<=sum(q)<=b2[1]
B=set(map(tuple,b['output_black']));p=tuple(b['pose'][0]);h=b['pose'][1]
for c in H[b['phase']:]:p,h,t=step(B,p,h);assert t==c
assert(p,h)==((57,41),1)
z=dict(first_difference=dict(time=i,cell=[91,-66],expected='R',actual='L'),Q_length=len(Q),Q_end=end,Q_read_cells=707,repeat_cell=q,first_Q_history=one,shifted_Q_history=two,outgoing_normal_bounds=b1,incoming_sum_bounds=b2,third_canonical_time=b['time']+104-b['phase'],third_canonical_pose=[p,h],inputs={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in['stateful_wake_corner_second_hit.json','stateful_wake_corner_third_hit.json']},source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'stateful_wake_corner_ownership.json').write_text(json.dumps(z,indent=2)+'\n');print(z)
