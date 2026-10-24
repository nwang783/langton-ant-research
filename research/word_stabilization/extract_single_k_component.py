from pathlib import Path
import json,sys,importlib.util
prefix=sys.argv[1];p=Path(prefix+'_words150.txt');lines=p.read_text().splitlines();n=len(lines[0]);mask=(1<<(n-1))-1
spec=importlib.util.spec_from_file_location('graph','../continuation_2026-10-22/ant_continuation/factor_language/no_pair_graph.py');g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
ws=[int(w.replace('L','0').replace('R','1'),2)for w in lines];vs=sorted({w>>1 for w in ws}|{w&mask for w in ws});ids={w:i for i,w in enumerate(vs)};A=[[]for _ in vs];R=[[]for _ in vs]
for w in ws:a,b=ids[w>>1],ids[w&mask];A[a].append(b);R[b].append(a)
c,cs=g.scc(A,R);pattern=sys.argv[2];bad={c[ids[w>>1]]for w,s in zip(ws,lines)if pattern in s and c[ids[w>>1]]==c[ids[w&mask]]};assert len(bad)==1,bad
j=next(iter(bad));keep=[s for w,s in zip(ws,lines)if c[ids[w>>1]]==j and c[ids[w&mask]]==j];Path(prefix+'_bad_component.txt').write_text('\n'.join(keep)+'\n');print('bad component',len(cs[j]),len(keep),flush=True)
