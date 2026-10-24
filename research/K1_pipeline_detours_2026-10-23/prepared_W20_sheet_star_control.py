"""Project the existing prescribed W20 profiles, no ant or front search.
Prepared singleton-L inputs stay explicit and violate the WHITE premise.
"""
from pathlib import Path
import json
p=Path(__file__).resolve().parent
src=json.loads((p/'bent_pipeline_W20_controls.json').read_text());W=src['word'];reports=[]
for pr in src['profiles']:
 P=pr['full_period'];dy=pr['full_drift'][1]
 H={tuple(z['face']):z['height']for z in pr['stream']['faces']};hist=pr['histories']
 q=1+0j;heading=1j;outs={};labels={};events={}
 for hh in hist:
  for r,t in enumerate(hh['times']):events[t%P]=dict(cell=hh['cell'],rank=r,turn=hh['turns'][r],input=hh['input'])
 for t,c in enumerate(W*(P//20)):
  k=int(q.imag)//dy;z=q-1j*k*dy;ct=t-k*P
  hh=next(x for x in hist if x['cell']==[int(z.real),int(z.imag)])
  es=list(zip(hh['times'],hh['incoming'],hh['turns']));r=hh['times'].index(ct)
  out=heading*(-1j if c=='R'else 1j)
  rank=sum(complex(*inc)*(-1j if turn=='R'else 1j)==out for tm,inc,turn in es[:r+1])
  center=q+out/2-out*1j/2;cf=(int(round(center.real-.5)),int(round(center.imag-.5))%dy)
  labels[t]=H[cf]-rank+1;outs[t]=out;q+=out;heading=out
 tau=list(range(P));exchanges=[]
 for hh in hist:
  if hh['turns']=='RLRL':
   x,y=[t%P for t in hh['times'][1:3]]
   tau[x],tau[y]=tau[y],tau[x]
   assert hh['times'][2]-hh['times'][1]==4
   exchanges.append((hh['cell'],x,y))
 sigma=[tau[(t+1)%P]for t in range(P)];seen=set();cycles=[];node={}
 for t in range(P):
  if t in seen:continue
  c=[];u=t
  while u not in seen:seen.add(u);node[u]=len(cycles);c.append(u);u=sigma[u]
  assert u==t and len({labels[u]for u in c})==1
  d=sum(outs[u]for u in c);assert d.real==0 and int(d.imag)%dy==0
  cycles.append(dict(level=labels[t],length=len(c),winding=int(d.imag)//dy,black_input_reads=sum(events[u]['input']=='black'for u in c),events=[events[u]for u in c]))
 edges=[dict(cell=cell,L1_node=node[x],R2_node=node[y])for cell,x,y in exchanges]
 a=P//20;root=next(i for i,c in enumerate(cycles)if c['level']==0)
 assert len(cycles)==4*a+1 and len(edges)==4*a
 assert cycles[root]['winding']==1 and cycles[root]['length']==4*a
 assert all(e['R2_node']==root for e in edges)
 assert sorted(e['L1_node']for e in edges)==[i for i in range(len(cycles))if i!=root]
 low=[c for c in cycles if c['level']==-1];top=[c for c in cycles if c['level']==1]
 assert len(low)==len(top)==2*a and all(c['length']==4 and c['winding']==0 for c in low+top)
 assert sum(c['black_input_reads']==2 for c in low)==a and sum(c['black_input_reads']==0 for c in low)==a
 reports.append(dict(full_period=P,full_drift=[0,dy],N2=len(edges),C=len(cycles),cycle_excess=len(edges)-len(cycles)+1,cycles=cycles,edges=edges))
out=dict(scope=__doc__,source='bent_pipeline_W20_controls.json',reports=reports)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS existing prepared profiles:',[(r['full_period'],r['N2'],r['C'],r['cycle_excess'])for r in reports])
