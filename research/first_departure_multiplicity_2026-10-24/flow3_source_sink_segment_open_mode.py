"""One symbolic maximal flow-three source-to-sink mode with its exterior supply.
Complete named WHITE histories, exact physical ordinals and integer clocks.
No exterior board, front, event period or global completion is asserted.
"""
from pathlib import Path
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
h={(0,1):'EWE',(0,0):'NSSS',(1,0):'EEE',(1,1):'NSS'}
t={(0,1):[0,12,16],(0,0):[-3,1,13,17],(1,0):[-2,2,18],(1,1):[3,7,11]}
def out(w,r):return H[(H.index(w[r])+(1 if r%2==0 else-1))%4]
edges=[];op=[];ip=[]
for p,w in h.items():
 assert all(t[p][r+1]-t[p][r]>=4 for r in range(len(w)-1))
 for dr in H:
  sr=[r for r in range(len(w))if out(w,r)==dr];q=(p[0]+V[dr][0],p[1]+V[dr][1])
  if q in h:
   tr=[r for r,x in enumerate(h[q])if x==dr];assert len(sr)==len(tr)
   for j,(a,b)in enumerate(zip(sr,tr)):
    assert t[q][b]==t[p][a]+1
    edges.append(dict(source=p,source_rank=a,target=q,target_rank=b,ordinal=j+1))
  else:
   for j,a in enumerate(sr):op.append(dict(source=p,rank=a,target=q,heading=dr,ordinal=j+1,departure_time=t[p][a]))
 for dr in H:
  tr=[r for r,x in enumerate(w)if x==dr];q=(p[0]-V[dr][0],p[1]-V[dr][1])
  if q not in h:
   for j,b in enumerate(tr):ip.append(dict(source=q,target=p,rank=b,heading=dr,ordinal=j+1,arrival_time=t[p][b]))
assert len({x for v in t.values()for x in v})==sum(map(len,h.values()))==13
obj=dict(scope=__doc__,named_histories=[dict(cell=p,history=w,clocks=t[p])for p,w in h.items()],all_internal_edges=edges,all_outgoing_open_ports=op,all_incoming_open_ports=ip,symbolic_obligation='For source first-read alpha and L1 gap a, helper N first occurs at alpha+3 and its W departure at alpha+a-1. WHITE requires helper NSS or NSSS and a>=12.',depth_obligation='Right C level is c on the G3 source/left-gate/sink path. Helper has both C=c-2 and opposite L=c-4 (NSS) or c-5 (NSSS), so the path low-L component is not locally minimal.',limitations='A finite exact partial rank/port/time network only. It is NOT a physical seed factor, shared global board, full WHITE front, closed departure cycle or proof that this open mode has an exterior completion.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS 13 distinct named physical events and all internal ordinal clocks')
