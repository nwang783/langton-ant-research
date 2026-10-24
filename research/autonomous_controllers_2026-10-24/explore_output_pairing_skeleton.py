#!/usr/bin/env python3
"""Discovery: root skeleton induced by lifetime matching and its conjugate.
This retains input/output endpoint labels; no internal-cycle deletion is physical.
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
 unseen=set(range(P));paths=[];cycles=[]
 while unseen:
  seed=min(unseen);stack=[seed];verts=set();lv={seed:0};vol=[]
  while stack:
   i=stack.pop();verts.add(i);unseen.discard(i)
   for color,M in [('A',A),('B',B)]:
    if i not in M:continue
    j,v=M[i]
    if j in lv:
     if lv[j]!=lv[i]+v:vol.append(lv[i]+v-lv[j])
    else:lv[j]=lv[i]+v;stack.append(j)
  ends=[]
  for i in verts:
   if i not in A:ends.append({'event':i,'type':'I'if i in I else'O','side':'A','lift':lv[i]})
   if i not in B:
    j=(i-1)%P;ends.append({'event':j,'type':'I'if j in I else'O','side':'B','lift':lv[i]-int(j==P-1)})
  assert len(ends)in(0,2)
  if not ends:cycles.append({'events':sorted(verts),'voltages':vol});continue
  e,f=ends;v=f['lift']-e['lift'];p=E[e['event']]['p'];q=E[f['event']]['p'];dx=q[0]+v*d[0]-p[0];dy=q[1]+v*d[1]-p[1]
  assert dx==0 or dy==0
  # The fibre is the arrival axis of every component event.
  axis='V'if E[seed]['hi']%2==0 else'H';assert(dx==0 if axis=='V'else dy==0)
  paths.append({'ends':ends,'edge_voltage':v,'axis':axis,'ray_displacement':[dx,dy],'interior_events':sorted(verts)})
 adj=defaultdict(list)
 for k,p in enumerate(paths):
  a,b=[e['event']for e in p['ends']];v=p['edge_voltage'];adj[a].append((b,v,k));adj[b].append((a,-v,k))
 assert set(adj)==set(I+O)and all(len(v)==2 for v in adj.values())
 assert all(set(paths[k]['axis']for j,v,k in es)=={'H','V'}for i,es in adj.items())
 unseen=set(adj);rootcycles=[]
 while unseen:
  st=min(unseen);at=st;prev=None;vol=0;seq=[]
  while True:
   unseen.discard(at);seq.append(at);nxt=next(x for x in adj[at]if x[2]!=prev);at,dv,prev=nxt;vol+=dv
   if at==st:break
  rootcycles.append({'roots':seq,'length':len(seq),'input_count':sum(i in I for i in seq),'output_count':sum(i in O for i in seq),'winding':vol})
 return{'P':P,'d':d,'input_events':I,'output_events':O,'internal_cycles':cycles,'root_pairing_edges':paths,'root_skeleton_cycles':rootcycles}
J={n:analyze(w)for n,w in WORDS.items()}
for n,j in J.items():print(n,'internal',len(j['internal_cycles']),'root cycles',Counter((c['length'],c['winding'],c['input_count'])for c in j['root_skeleton_cycles']),flush=True)
(R/'output_pairing_skeleton_discovery.json').write_text(json.dumps(J))
