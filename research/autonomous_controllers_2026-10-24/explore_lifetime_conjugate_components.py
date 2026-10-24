#!/usr/bin/env python3
"""Discovery: complete physical lifetime matching and its event-cycle conjugate.
Prepared input and permanent output holes are retained explicitly.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json
from check_all_cut_wave_interfaces import WORDS
from check_extremal_read_coupling import event_word,quotient
R=Path(__file__).resolve().parent

def analyze(w):
 E,d,h=event_word(w);P=len(w);H=defaultdict(list);lift={};A={};I=[];O=[]
 for e in E:
  q,k=quotient(e['p'],d);H[q].append((e['t']-P*k,e));lift[e['t']]=k
 for q,es in H.items():
  es.sort(key=lambda z:z[0]);assert all(a[1]['c']!=b[1]['c']for a,b in zip(es,es[1:]))
  if es[0][1]['c']=='L':I.append(es[0][1]['t'])
  if es[-1][1]['c']=='R':O.append(es[-1][1]['t'])
  for (_,a),(_,b)in zip(es,es[1:]):
   if a['c']=='R':
    i,j=a['t'],b['t'];v=lift[i]-lift[j];A[i]=(j,v);A[j]=(i,-v)
 B={}
 for i,(j,v)in A.items():
  a,b=(i+1)%P,(j+1)%P;B[a]=(b,v+int(j==P-1)-int(i==P-1))
 unseen=set(range(P));components=[]
 while unseen:
  seed=min(unseen);stack=[seed];verts=set();lv={seed:0};wind=[]
  while stack:
   i=stack.pop();verts.add(i);unseen.discard(i)
   for color,M in [('A',A),('B',B)]:
    if i not in M:continue
    j,v=M[i]
    if j in lv:
     if lv[j]!=lv[i]+v:wind.append(lv[i]+v-lv[j])
    else:lv[j]=lv[i]+v;stack.append(j)
  endpoints=[i for i in verts if i not in A or i not in B];closed=not endpoints
  points=[(E[i]['p'][0]+lv[i]*d[0],E[i]['p'][1]+lv[i]*d[1])for i in verts]
  times=[i+P*lv[i]for i in verts]
  components.append({'vertices':sorted(verts),'closed':closed,'endpoints':endpoints,'input_holes':[i for i in verts if i in I],'output_holes':[i for i in verts if i in O],'shifted_input_holes':[i for i in verts if(i-1)%P in I],'shifted_output_holes':[i for i in verts if(i-1)%P in O],'voltages':wind,'collinear_x':len({x for x,y in points})==1,'collinear_y':len({y for x,y in points})==1,'time_span':max(times)-min(times)})
 return{'period':P,'drift':d,'I':len(I),'O':len(O),'components':components,'summary':dict(Counter(('cycle'if c['closed']else'path')for c in components)),'cycle_lengths':dict(Counter(len(c['vertices'])for c in components if c['closed']))}
J={name:analyze(w)for name,w in WORDS.items()}
for n,j in J.items():print(n,{k:v for k,v in j.items()if k!='components'},flush=True)
(R/'lifetime_conjugate_components_discovery.json').write_text(json.dumps(J))
