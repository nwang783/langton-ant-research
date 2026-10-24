import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'computability'))
from periodic_tail_checker import multiplier
D=((0,1),(1,0),(0,-1),(-1,0))
a=json.loads((Path(__file__).resolve().parents[1]/'recovered_bundle/ant_global/root/standard.json').read_text());w=a['word'];h=a['heading'];p=(0,0);ev=[]
for i,c in enumerate(w):
 old=h;h=(h+(1 if c=='R' else -1))%4
 ev.append((p,old,h,c,i));p=(p[0]+D[h][0],p[1]+D[h][1])
d=p;P=len(w)
def key(q):
 # simple full-vector fundamental rep
 if d[0]: k=q[0]//abs(d[0]); k=k if d[0]>0 else -k
 else:k=q[1]//abs(d[1]);k=k if d[1]>0 else -k
 return (q[0]-k*d[0],q[1]-k*d[1]),k
hist={}
for q,hin,hout,c,i in ev:
 r,k=key(q);hist.setdefault(r,[]).append((i-k*P,hin,hout,c,i,k))
for r in hist:hist[r].sort()
f={};l={}
for r,ls in hist.items():
 e=ls[0];n=(r[0]+D[e[2]][0],r[1]+D[e[2]][1]);f[r]=key(n)
 e=ls[-1]
 if e[3]=='L':n=(r[0]-D[e[1]][0],r[1]-D[e[1]][1]);l[r]=key(n)
def cycles(graph):
 out=[];seen=set()
 for s in graph:
  path=[];at=s;idx={}
  while at in graph and at not in idx and at not in seen:idx[at]=len(path);path.append(at);at=graph[at][0]
  if at in idx:
   cyc=path[idx[at]:];out.append((cyc,sum(graph[x][1] for x in cyc)))
  seen.update(path)
 return out
print('d',d,'first',cycles(f),'lastLreverse',cycles(l))
for r,ls in sorted(hist.items()):print(r,''.join(e[3] for e in ls),f[r],l.get(r))
ft={};ftl={}
for r,ls in hist.items():
 e=ls[0];nr,k=f[r];target=hist[nr][-1];lasttime=target[0]+k*P
 if e[0]+1==lasttime:
  ft[r]=(nr,k)
  if target[3]=='L':ftl[r]=(nr,k)
print('first-last',ft,'cycles',cycles(ft));print('first-lastL',ftl)
