"""Choose supplied two-corner words for the seven specifically required lanes.
No new corner palette or cap radius. Each candidate is checked with full 30-period
incoming and outgoing histories; this is not yet their mutual composition.
"""
from pathlib import Path
import json
from check_prepared1564_router_geometry import H,trace,infer,corner
P=Path(__file__).resolve().parent
V=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,k):
 x,y=p
 for _ in range(k%4):x,y=y,-x
 return x,y
C=json.loads((P/'single_turn_corner_selected.json').read_text())['cases'];uniq={}
for c in C:
 w=corner(c['in_phase'],c['cap'],c['out_phase']);e=list(trace(w))[-1]
 uniq.setdefault(w,dict(word=w,q=e[1],h=e[2],sig=[c['in_phase'],c['cap'],c['out_phase']],extra=c['extra_count']))
C=list(uniq.values())
LANES=[(-37,1,3),(-65,0,1),(-25,1,3),(49,0,1),(-13,0,3),(21,0,1),(1,1,3)]
res=[]
for i,(src,dst) in enumerate(zip(LANES,LANES[1:])):
 ts,ps,hs=src;td,pd,hd=dst;rr=(hs-1)%4;want=(td-ts)*(-1 if rr==2 else 1);par=(pd-ps)%2;cand=[]
 for a in C:
  for b in C:
   if a['h']!=b['h']:continue
   rb=rot(b['q'],a['h']-1);q0=a['q'][0]+rb[0],a['q'][1]+rb[1];step=rot((2,2),a['h']-1);delta=want-(q0[0]-q0[1]);coef=step[0]-step[1]
   if delta%coef:continue
   k=delta//coef
   if k<0:continue
   q=q0[0]+k*step[0],q0[1]+k*step[1]
   if q[0]%2!=par:continue
   w=a['word']+H*k+b['word'];cand.append((a['extra']+b['extra'],len(w),k,a,b,q,w))
 cand.sort(key=lambda z:(z[0],z[1],z[2],z[3]['sig'],z[4]['sig']))
 tried=0;chosen=None
 for score,ln,k,a,b,q,w in cand:
  tried+=1;z=infer(H*30+w+H*30)
  if z['bad']:continue
  base=infer(H*30)['input'];extra=z['input']-base
  # Convert from normalized 30-period launch to the actual source heading.
  extra=sorted(rot((x-60,y-60),rr)for x,y in extra);actualq=rot(q,rr)
  events=list(trace(w,(0,0),hs));assert events[-1][1]==actualq and events[-1][2]==hd
  poses=[z[1]for z in events[:-1]]
  chosen={'index':i+1,'source_lane':src,'target_lane':dst,'first_corner':a['sig'],'middle_periods':k,'second_corner':b['sig'],'word':w,'endpoint':[actualq,hd],
   'extra_black_relative_input':extra,'extra_mass':len(extra),'local_control_reads':z['reads'],'local_candidates_before_success':tried,
   'read_u_bounds':[min(x+y for x,y in poses),max(x+y for x,y in poses)],'read_t_bounds':[min(x-y for x,y in poses),max(x-y for x,y in poses)]}
  break
 assert chosen,('no local router',i,len(cand));res.append(chosen)
 print({k:v for k,v in chosen.items()if k not in('word','extra_black_relative_input')})
out={'scope':__doc__,'lanes':LANES,'routers':res}
(P/'prepared1564_noncrossing_router_plan.json').write_text(json.dumps(out,indent=2)+'\n')
