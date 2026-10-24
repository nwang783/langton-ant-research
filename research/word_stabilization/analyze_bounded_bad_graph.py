from pathlib import Path
import sys,json,importlib.util
p=Path(sys.argv[1]);lines=p.read_text().splitlines();n=len(lines[0]);assert all(len(w)==n for w in lines)
spec=importlib.util.spec_from_file_location('graph','../continuation_2026-10-22/ant_continuation/factor_language/no_pair_graph.py');g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
ws=[int(w.replace('L','0').replace('R','1'),2)for w in lines];mask=(1<<(n-1))-1
vs=sorted({w>>1 for w in ws}|{w&mask for w in ws});ids={w:i for i,w in enumerate(vs)};adj=[[]for _ in vs];rev=[[]for _ in vs]
for w in ws:a,b=ids[w>>1],ids[w&mask];adj[a].append(b);rev[b].append(a)
c,cs=g.scc(adj,rev);big=max(range(len(cs)),key=lambda i:len(cs[i]));p.with_suffix('.recurrent.txt').write_text(''.join(w+'\n'for w in lines if c[ids[int(w[:-1].replace('L','0').replace('R','1'),2)]]==big and c[ids[int(w[1:].replace('L','0').replace('R','1'),2)]]==big));out=[];M='LLLLRLRRRRLR';mb=int(M.replace('L','0').replace('R','1'),2);mm=(1<<len(M))-1
for i,s in enumerate(cs):
 e=sum(c[v]==i for u in s for v in adj[u])
 if not e:continue
 ports={u for u in s if vs[u]&mm==mb};non=set(s)-ports;deg={u:0 for u in non}
 for u in non:
  for v in adj[u]:
   if v in non:deg[v]+=1
 stack=[u for u in non if deg[u]==0];count=0
 while stack:
  u=stack.pop();count+=1
  for v in adj[u]:
   if v in non:
    deg[v]-=1
    if deg[v]==0:stack.append(v)
 z={'vertices':len(s),'edges':e,'ports':len(ports),'unremoved_nonport_vertices':len(non)-count}
 ns=sorted(non);ni={u:j for j,u in enumerate(ns)};na=[[ni[v]for v in adj[u]if v in non]for u in ns];nr=[[]for _ in ns]
 for u in range(len(ns)):
  for v in na[u]:nr[v].append(u)
 nc,ncs=g.scc(na,nr);nz=[]
 for j,ss in enumerate(ncs):
  ee=sum(nc[v]==j for u in ss for v in na[u])
  if not ee:continue
  zz={'vertices':len(ss),'edges':ee}
  if ee==len(ss):
   u=ss[0];v=u;ww=''
   while True:
    v=next(k for k in na[v]if nc[k]==j);ww+='R'if vs[ns[v]]&1 else'L'
    if v==u:break
   zz['word']=ww
  nz.append(zz)
 z['nonmarker_cyclic_components']=nz
 if e==len(s):
  u=s[0];v=u;w=''
  while True:
   v=next(k for k in adj[v]if c[k]==i);w+='R'if vs[v]&1 else'L'
   if v==u:break
  z['word']=w
 out.append(z)
r={'horizon':n,'words':len(ws),'vertices':len(vs),'cyclic_components':out};print(json.dumps(r,indent=2));p.with_suffix('.graph.json').write_text(json.dumps(r,indent=2))
