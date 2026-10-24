#!/usr/bin/env python3
"""One exact genuine standard control against spatial-planarity shortcuts."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
from check_all_cut_wave_interfaces import WORDS
from check_extremal_read_coupling import event_word,quotient
from lifetime_boundary_graph import analyze
R=Path(__file__).resolve().parent

def main():
 w=WORDS['S104']; E,d,_=event_word(w); P=len(w); F=analyze(w)
 histories=defaultdict(list); lift={}; A={}
 for e in E:
  q,k=quotient(e['p'],d); histories[q].append((e['t']-P*k,e));lift[e['t']]=k
 for es in histories.values():
  es.sort(key=lambda z:z[0]); assert es[0][1]['c']=='R'
  for (_,a),(_,b) in zip(es,es[1:]):
   assert a['c']!=b['c']
   if a['c']=='R':
    i,j=a['t'],b['t'];v=lift[i]-lift[j];A[i]=(j,v);A[j]=(i,-v)
 B={(i+1)%P:((j+1)%P,v+int(j==P-1)-int(i==P-1))for i,(j,v)in A.items()}
 def path(k):
  p=F['root_pairing_edges'][k]; st=min(p['interior_events']);lv={st:0};todo=[st]
  while todo:
   i=todo.pop()
   for M in [A,B]:
    if i not in M:continue
    j,v=M[i]
    if j in lv:assert lv[j]==lv[i]+v
    else:lv[j]=lv[i]+v;todo.append(j)
  assert set(lv)==set(p['interior_events'])
  first=p['ends'][0];i=first['event'];g=lv[i]if first['side']=='A'else lv[(i+1)%P]-int(i==P-1)
  ends=[]
  for ee in p['ends']:
   z=ee['lift']-p['ends'][0]['lift'];q=E[ee['event']]['p'];ends.append([q[a]+z*d[a]for a in range(2)])
  lives={}
  for i in lv:
   if i in A and E[i]['c']=='R':
    j,v=A[i];z=lv[i]-g;lives[i,z]=(j,v,'A')
   pi=(i-1)%P
   if i in B and E[pi]['c']=='R':
    j,v=A[pi];z=lv[i]-int(pi==P-1)-g;lives[pi,z]=(j,v,'B')
  rows=[]
  for (i,z),(j,v,color)in sorted(lives.items()):
   pos=[E[i]['p'][a]+z*d[a]for a in range(2)];birth=i+z*P;end=j+(z+v)*P
   assert birth<end and pos==[E[j]['p'][a]+(z+v)*d[a]for a in range(2)]
   rows.append({'birth_phase':i,'birth_lift':z,'position':pos,'birth_time':birth,'consumption_time':end,'matching_color':color})
  return {'component_index':k,'axis':p['axis'],'output_root_events':[ee['event']for ee in p['ends']],'endpoints':ends,'complete_event_lifts':sorted((i,z-g)for i,z in lv.items()),'complete_black_lifetimes':rows}
 H=path(6);V=path(1);p=[-1,0]
 assert H['axis']=='H'and V['axis']=='V'
 assert H['endpoints']==[[-2,0],[0,0]] and V['endpoints']==[[-1,2],[-1,-2]]
 HL=[r for r in H['complete_black_lifetimes']if r['position']==p]
 VL=[r for r in V['complete_black_lifetimes']if r['position']==p]
 assert [(r['birth_time'],r['consumption_time'])for r in HL]==[(21,101)]
 assert sorted((r['birth_time'],r['consumption_time'])for r in VL)==[(-151,-71),(-67,-63),(1,9)]
 assert not{(r['birth_phase'],r['birth_lift'])for r in HL}&{(r['birth_phase'],r['birth_lift'])for r in VL}
 out={'status':'AUTHOR CHECK PASS; independent audit pending','scope':'One standard104 proper projected H/V crossing with disjoint actual BLACK lifetime sets at the crossing. Not a classification or a new controller.','word':w,'word_sha256':hashlib.sha256(w.encode()).hexdigest(),'P':P,'full_drift':d,'horizontal_path':H,'vertical_path':V,'proper_crossing':p,'horizontal_lifetimes_at_crossing':HL,'vertical_lifetimes_at_crossing':VL,'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['lifetime_boundary_graph.py','check_extremal_read_coupling.py','check_all_cut_wave_interfaces.py']}}
 (R/'lifetime_projection_crossing_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS: exact projected crossing with distinct lifetime epochs')
if __name__=='__main__':main()
