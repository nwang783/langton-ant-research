#!/usr/bin/env python3
"""Transparent OPEN event-interface control, not a trajectory or controller."""
import json
from pathlib import Path
from collections import defaultdict
from check_extremal_read_coupling import D,quotient,cycles
P=124;d=(2,-2)
DATA=[((0,-1),(3,),(0,)),((1,-2),(3,),(94,)),
 ((0,0),(2,2,0),(-31,-3,1)),((1,-1),(2,2,0),(-1,91,95)),
 ((0,1),(1,1,3,3,3),(-32,-28,-16,-4,28)),((1,0),(1,1,3,3),(-2,2,14,90))]

def main():
 H={p:[{'rank':j,'h':h,'out':(h+(1 if j%2==0 else-1))%4,'turn':'R'if j%2==0 else'L','clock':t}for j,(h,t)in enumerate(zip(hs,ts))]for p,hs,ts in DATA};events=[(p,e)for p,es in H.items()for e in es]
 assert len({e['clock']%P for p,e in events})==len(events)==17
 for p,es in H.items():
  assert all((e['clock']-(2*p[0]-sum(p)%2+1))%4==0 for e in es)
  assert all(b['clock']-a['clock']>=4 for a,b in zip(es,es[1:]))
 edges=[];openout=[];openin=[]
 for p,es in H.items():
  for h in range(4):
   src=[e for e in es if e['out']==h]
   if not src:continue
   q,k=quotient((p[0]+D[h][0],p[1]+D[h][1]),d)
   if q not in H:
    openout +=[{'cell':p,'rank':e['rank'],'target_class':q,'voltage':k,'clock':e['clock']}for e in src];continue
   dst=[e for e in H[q]if e['h']==h];assert len(src)==len(dst)
   for u,v in zip(src,dst):
    assert u['clock']+1==v['clock']+k*P
    edges.append({'source':p,'source_rank':u['rank'],'target':q,'target_rank':v['rank'],'voltage':k})
 for p,es in H.items():
  for e in es:
   q,k=quotient((p[0]-D[e['h']][0],p[1]-D[e['h']][1]),d)
   if q not in H:openin.append({'cell':p,'rank':e['rank'],'source_class':q,'voltage':k,'clock':e['clock']})
 E={tuple(e['source']):(tuple(e['target']),e['voltage'])for e in edges if e['source_rank']==0 and e['target_rank']==len(H[tuple(e['target'])])-1}
 F={tuple(e['source']):(tuple(e['target']),e['voltage'])for e in edges if e['source_rank']==0}
 assert len(E)==4 and len(cycles(E))==1 and cycles(E)[0]['winding']==-1
 assert len(cycles(F))==1 and cycles(F)[0]['winding']==-1
 ages=[es[-1]['clock']-es[0]['clock']for p,es in H.items()if p in E and len(es)>1];assert ages==[32,96] and sum(ages)==P+4
 # A full g8 wake compatible with parity screens, not asserted compatible
 # with unspecified higher-row history or count equations.
 O={(0,-1),(1,-2),(0,0),(1,-1),(0,1),(1,2),(0,5),(1,10)}
 for ax in (0,1):
  for r in (0,1):assert sum(1 if sum(p)%2==0 else-1 for p in O if p[ax]%2==r)%4==2
 Q=[p for p in O if sum(p)%2==0];C=[p for p in O if sum(p)%2]
 J=sum(sum(q)<sum(c)for q in Q for c in C);assert len(Q)==2 and J==8 and(J+len(Q)//2)%2==1
 # Exact geometric outside completions for each gap between known phases.
 # Their turn strings need not be mutually colour-compatible.
 phases=sorted((e['clock']%P,(p[0]-(e['clock']//P)*d[0],p[1]-(e['clock']//P)*d[1]),e)for p,e in events)
 bridges=[]
 for z,(t,p,e)in enumerate(phases):
  tn,pn,en=phases[(z+1)%len(phases)]
  if z==len(phases)-1:tn+=P;pn=(pn[0]+d[0],pn[1]+d[1])
  gap=tn-t;start=(p[0]+D[e['out']][0],p[1]+D[e['out']][1],e['out']);states={start:''}
  for dt in range(1,gap):
   nxt={}
   for (x,y,h),w in states.items():
    if quotient((x,y),d)[0]in H:continue
    for c,turn in [('R',1),('L',-1)]:
     hh=(h+turn)%4;xx=x+D[hh][0];yy=y+D[hh][1]
     if abs(xx-pn[0])+abs(yy-pn[1])>gap-dt-1:continue
     if not -1<=xx+yy<=11:continue
     nxt.setdefault((xx,yy,hh),w+c)
   states=nxt
  target=(pn[0],pn[1],en['h']);assert target in states,(t,tn,p,pn,gap)
  if gap>1:bridges.append({'start_phase':t,'next_phase':tn,'unknown_turns':states[target],'scope':'Geometric bridge only; no shared field or colour compatibility assertion.'})
 result={'scope':__doc__,'period_parameter':P,'full_drift':d,'complete_histories_on_six_named_classes':[{'cell':p,'events':es}for p,es in H.items()],'internal_matched_edges':edges,'open_incoming_ports':openin,'open_outgoing_ports':openout,'E_cycles':cycles(E),'first_cycles_in_patch':cycles(F),'triple_ages':ages,'odd_class_screen_only':{'O':sorted(O),'width':12,'V':len(Q),'J':J},'geometric_bridges':bridges,'limitations':['Higher-row field and histories unspecified, not discarded.','No complete one-event orbit or finite BLACK seed supplied.','Geometric gap words are individually paths only, not asserted jointly colour-legal.','The whole proposed wake is only a necessary-screen completion, not an actual emitted field.']}
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'events':len(events),'internal_edges':len(edges),'open_inputs':len(openin),'open_outputs':len(openout),'geometric_bridges':len(bridges),'scope':__doc__}))
if __name__=='__main__':main()
