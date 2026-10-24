from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
Pth=Path(__file__).resolve();ROOT=Pth.parents[1];A=json.loads((ROOT/'causal_reduction/unit_scale/prepared4352_output_return_wave.json').read_text());w=A['word'];P=len(w);D=(1j,1,-1j,-1);p=13+7j;h=0;g=defaultdict(list);where=[]
for i,c in enumerate(w):
 x,y=int(p.real),int(p.imag);a=x%78;k=-(x-a)//78;cl=(x-y,a);r=[k,i,c];g[cl].append(r);where.append((cl,r));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
assert(p,h)==(-65-71j,0)
for gs in g.values():gs.sort(key=lambda z:z[1]-P*z[0])
def info(gs):
 lo=min(x[0]for x in gs);hi=max(x[0]for x in gs);a=gs[0][2]=='L'
 b=sum(next(c for k,i,c in gs if k<=n)=='L'for n in range(lo,hi))+sum(next(c for k,i,c in gs if k>=n)=='L'for n in range(lo+1,hi+1))-int(a)*(hi-lo)
 return hi-lo,int(a),b
stats={cl:info(gs)for cl,gs in g.items()};sl=sum(v[1]for v in stats.values());b=sum(v[2]for v in stats.values());assert(sl,b)==(1439,101)
spanhist=Counter(v[0]for v in stats.values());rows=[]
for phase in range(P):
 rows.append([phase,b,max(spanhist)])
 cl,r=where[phase];old=stats[cl];spanhist[old[0]]-=1
 if spanhist[old[0]]==0:del spanhist[old[0]]
 r[0]+=1;new=info(g[cl]);assert new[1]==old[1];stats[cl]=new;b+=new[2]-old[2];spanhist[new[0]]+=1
assert b==101 and max(spanhist)==1
out=dict(status='PASS all15324 cyclic entry phases exact first-L affine count',word_sha256=hashlib.sha256(w.encode()).hexdigest(),fuel_slope=sl,canonical_constant=101,constant_range=[min(x[1]for x in rows),max(x[1]for x in rows)],maximum_copy_span=max(x[2]for x in rows),constant_histogram=dict(sorted(Counter(x[1]for x in rows).items())),span_histogram=dict(Counter(x[2]for x in rows)),phase_rows=rows,scope='For phase s, exact minimum entry black mass1439*N+b_s once N>=max(1,copyspan_s). Head/heading are actual rotated-cut pose, not a stationary endcap reset. No finite-original or cross-wave renewal inference.')
Pth.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in('phase_rows','constant_histogram')},indent=2))
