"""Constructive ALL-LENGTH local RR(LLRR)* flat-strip chronology.
The four selected k values below are unit controls for a symbolic construction,
not a bounded search. Exterior connectors remain OPEN; no board factor/front.
"""
from pathlib import Path
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def phase(p):return (2*(p[0]%2)+(1 if sum(p)%2 else 0))%4 if sum(p)%2==0 else (3-2*(p[0]%2))%4
def make(k):
 assert k>=1
 a=lambda j:(2*j,0);b=lambda j:(2*j+1,0);u=lambda j:(2*j,-1);v=lambda j:(2*j+1,-1)
 L=(-1,-1);W=(-1,0);S=(2*k,-1);Z=(2*k,0)
 hs={L:'NNN',W:'WEW',S:'EWE',Z:'SSS'}
 for j in range(k):hs.update({a(j):'NSSN',b(j):'EWWE',u(j):'WWEE',v(j):'NNSS'})
 blocks=[]
 def add(name,*events):blocks.append(dict(name=name,events=list(events)))
 add('right D', (v(k-1),0),(S,0))
 for j in reversed(range(k)):
  add(f'A{j}',(v(j),1),(u(j),0),(a(j),0),(b(j),0),(v(j),2),(u(j),1))
  if j:add(f'D{j-1}',(v(j-1),0),(u(j),2))
 add('left D',(L,0),(u(0),2));add('left middle',(L,1));add('right middle',(S,1))
 add('right C',(Z,0),(b(k-1),1),(v(k-1),3),(S,2));add('Z middle',(Z,1));add('Z final',(Z,2),(b(k-1),2))
 add(f'P{k-1}',(a(k-1),1),(b(k-1),3))
 for j in reversed(range(k-1)):
  add(f'C{j}',(a(j+1),2),(b(j),1),(v(j),3),(u(j+1),3),(a(j+1),3),(b(j),2))
  add(f'P{j}',(a(j),1),(b(j),3))
 add('left first top',(a(0),2),(W,0));add('W middle',(W,1));add('left final',(L,2),(u(0),3),(a(0),3),(W,2))
 ev={(p,r)for p,h in hs.items()for r in range(len(h))}
 flat=[e for bl in blocks for e in bl['events']]
 assert len(flat)==len(set(flat))==len(ev)==16*k+12 and set(flat)==ev
 succ={};pred={};ports=[]
 for p,h in hs.items():
  for dr,d in V.items():
   q=p[0]+d[0],p[1]+d[1]
   sr=[r for r in range(len(h))if out(h,r)==dr]
   if q not in hs:
    ports.extend(dict(cell=p,rank=r,outgoing=dr,target=q)for r in sr);continue
   tr=[r for r,a0 in enumerate(hs[q])if a0==dr];assert len(sr)==len(tr)
   for r,s in zip(sr,tr):succ[p,r]=q,s;pred[q,s]=p,r
 selected={(x,y)for bl in blocks for x,y in zip(bl['events'],bl['events'][1:])}
 assert selected==set(succ.items())
 for bl in blocks:
  assert bl['events'][0]not in pred and bl['events'][-1]not in succ
 # Separate literal blocks by an arbitrary large delay, keeping the exact
 # checker/axis mod-four time phase. No geometric connector is asserted.
 times={};end=-4*k-40;gap=4*k+20
 for bl in blocks:
  p=bl['events'][0][0];st=end+gap;st+=(phase(p)-st)%4
  for z,e in enumerate(bl['events']):times[e]=st+z
  end=st+len(bl['events'])-1;bl['start_time']=st
 assert len(set(times.values()))==len(times)
 for e,f in succ.items():assert times[f]==times[e]+1
 for p,h in hs.items():
  for r in range(len(h)):
   assert times[p,r]%4==phase(p)
   if r:assert times[p,r]-times[p,r-1]>=4
 return dict(k=k,histories={str(p):h for p,h in hs.items()},blocks=blocks,events=16*k+12,flat_contacts=2*k,formal_odd_end_cells=[L,W,S,Z],cluster_R_minus_L=2,open_outgoing_ports=ports,rank_clock_injective=True,mod4_phase_respected=True)
rows=[make(k)for k in[1,2,3,7]]
obj=dict(scope=__doc__,symbolic_k_domain='all integers k>=1; proof is the displayed block-index formula and rank inequalities, not the finite controls',unit_controls=rows,warning='Every internal physical ordinal and every complete cell history is retained, with an injective mod-four rank schedule. The gaps are unfilled exterior connector demands. No actual ant word, board factor, full event orbit, critical side-current completion or WHITE translating front is claimed.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS symbolic strip construction; unit controls',[(r['k'],r['events'],len(r['blocks']))for r in rows])
