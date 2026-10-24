from pathlib import Path
from collections import deque,Counter
import json,time,sys
start=time.time();path=Path('recurrent_spaced_words150.recurrent.txt');marks=('LLLLRLRRRRLR','RRRLLRLLRRRR');lookup={int(w.replace('L','0').replace('R','1'),2):w for w in marks};mask=(1<<149)-1
ws=[int(w.strip().replace('L','0').replace('R','1'),2)for w in path.open()];vs=sorted({w>>1 for w in ws}|{w&mask for w in ws});ids={w:i for i,w in enumerate(vs)};A=[[]for _ in vs]
for w in ws:A[ids[w>>1]].append(ids[w&mask])
ports={u:lookup[v&4095]for u,v in enumerate(vs)if(v&4095)in lookup};deg=[0]*len(vs)
for u in range(len(vs)):
 if u in ports:continue
 for v in A[u]:
  if v not in ports:deg[v]+=1
q=deque(u for u in range(len(vs))if u not in ports and deg[u]==0);top=[]
while q:
 u=q.popleft();top.append(u)
 for v in A[u]:
  if v not in ports:
   deg[v]-=1
   if deg[v]==0:q.append(v)
assert len(top)+len(ports)==len(vs)
height=[0]*len(vs)
for u in reversed(top):height[u]=1+max((height[v]for v in A[u]),default=0)
print('vertices',len(vs),'ports',len(ports),'max nonport height',max(height),'seconds',time.time()-start,flush=True)
macros=Counter();returned=[];paths=0;maxgap=0
for u,mark in ports.items():
 stack=[(v,'R'if vs[v]&1 else'L')for v in A[u]]
 while stack:
  v,w=stack.pop()
  if v in ports:
   before=(mark+w)[:-12];macros[(mark,ports[v],before)]+=1;returned.append((u,v,(mark,ports[v],before)));paths+=1;maxgap=max(maxgap,len(w))
   if paths>10000000:raise RuntimeError('return-path cap: incomplete')
  else:
   for z in A[v]:stack.append((z,w+('R'if vs[z]&1 else'L')))
print('return paths',paths,'maxgap',maxgap,'macro types',len(macros),'seconds',time.time()-start,flush=True)
out={'source':str(path),'vertices':len(vs),'ports':len(ports),'max_nonport_height':max(height),'paths':paths,'maxgap':maxgap,'macros':[{'start_marker':a,'end_marker':b,'word':w,'multiplicity':n}for(a,b,w),n in sorted(macros.items(),key=lambda z:(len(z[0][2]),z[0][2]))]}
keys=[(z['start_marker'],z['end_marker'],z['word'])for z in out['macros']];ki={k:i for i,k in enumerate(keys)};ps=sorted(ports);pi={u:i for i,u in enumerate(ps)};E=[(pi[u],ki[k],pi[v])for u,v,k in returned];PA=[[]for _ in ps]
for u,a,v in E:PA[u].append((a,v))
classes=[0]*len(ps);rounds=0
while True:
 signatures=[tuple(sorted((a,classes[v])for a,v in adj))for adj in PA];uniq={s:i for i,s in enumerate(sorted(set(signatures)))};nc=[uniq[s]for s in signatures];print('partition round',rounds,'classes',len(uniq),flush=True)
 if len(set(classes))==len(uniq):classes=nc;break
 classes=nc;rounds+=1
quotient=sorted({(classes[u],a,classes[v])for u,a,v in E});assert all(len(adj)==len({a for a,v in adj})for adj in PA)
PO={'ports':len(ps),'edges':len(E),'classes':len(uniq),'rounds':rounds,'quotient_edges':quotient,'macro_words':out['macros']};Path('spaced_two_marker_port_quotient.json').write_text(json.dumps(PO,indent=2));Path('spaced_two_marker_actual_ports.json').write_text(json.dumps({'port_histories':[format(vs[u],'0149b').replace('0','L').replace('1','R')for u in ps],'edges':E,'classes':classes}))
for i,z in enumerate(out['macros']):print(i,len(z['word']),z['start_marker']==marks[0],z['end_marker']==marks[0],z['word'],z['multiplicity'])
