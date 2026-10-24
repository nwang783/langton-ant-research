from pathlib import Path
import importlib.util,json,sys
spec=importlib.util.spec_from_file_location('graph','../continuation_2026-10-22/ant_continuation/factor_language/no_pair_graph.py');g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
path=Path(sys.argv[1])if len(sys.argv)>1 else Path('spaced_pair_words100.txt');lines=path.read_text().splitlines();n=len(lines[0]);M='LLLLRLRRRRLR';mb=int(M.replace('L','0').replace('R','1'),2);mm=(1<<len(M))-1;mask=(1<<(n-1))-1
ws=[int(w.replace('L','0').replace('R','1'),2)for w in lines];vs=sorted({w>>1 for w in ws}|{w&mask for w in ws});ids={w:i for i,w in enumerate(vs)};adj=[[]for _ in vs];rev=[[]for _ in vs]
for w in ws:
 a,b=ids[w>>1],ids[w&mask]
 if vs[a]&mm!=mb and vs[b]&mm!=mb:adj[a].append(b);rev[b].append(a)
c,cs=g.scc(adj,rev);s=max(cs,key=len);i=c[s[0]];S=set(s);aa={u:[v for v in adj[u]if v in S]for u in S};rr={u:[v for v in rev[u]if v in S]for u in S};ports={u for u in S if len(aa[u])!=1 or len(rr[u])!=1};edges=[]
for u in ports:
 for v in aa[u]:
  word='R'if vs[v]&1 else'L';z=v
  while z not in ports:z=aa[z][0];word+='R'if vs[z]&1 else'L'
  edges.append((u,z,word))
out={'vertices':len(S),'ports':len(ports),'edges':edges,'histories':{str(u):format(vs[u],'0'+str(n-1)+'b').replace('0','L').replace('1','R')for u in S},'adjacency':aa};path.with_suffix('.nonmarker_core.json').write_text(json.dumps(out,indent=2));print('vertices',len(S),'ports',len(ports),'edges',len(edges));print('edge lengths',sorted({len(w)for u,v,w in edges}));print('unique words',len(set(w for u,v,w in edges)))
for u,v,w in edges:print(u,v,w)
