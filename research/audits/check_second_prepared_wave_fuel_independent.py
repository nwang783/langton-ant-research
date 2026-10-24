from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];J=json.loads((ROOT/'nonlinear_global_budget_2026-10-23/second_prepared_wave_probe.json').read_text());w=J['word'];P=len(w);p=68+73j;h=3;v=(1j,1,-1j,-1);g=defaultdict(list)
for i,c in enumerate(w):
 x,y=int(p.real),int(p.imag);g[x-y,x%26].append(((x-x%26)//26,i,c));h=(h+(1 if c=='R'else-1))%4;p+=v[h]
assert p==94+99j and h==3
slope=constant=0;boundary=[];spans=Counter()
for cl,a in g.items():
 lo=min(z[0]for z in a);hi=max(z[0]for z in a);span=hi-lo;spans[span]+=1;assert span in(0,1)
 first=lambda b:min((i-P*k,c)for k,i,c in b)[1]=='L'
 full=first(a);slope+=full
 if span:
  l=first([z for z in a if z[0]==lo]);r=first([z for z in a if z[0]==hi]);constant+=l+r-full;boundary.append(dict(orbit=cl,first_left=l,first_full=full,first_right=r,contribution='(N-1)*full+left+right'))
assert slope==406 and constant==57 and spans=={0:1058,1:104}
# Exact algebra: span0 contributes N*full; span1 contributes (N-1)*full+left+right for every integer N>=1.
assert all(w!=w[:n]*(len(w)//n)for n in range(1,len(w))if len(w)%n==0)
net=w.count('R')-w.count('L');assert net==184
for n in(1,2,3,7):
 initial=set();last={};p=68+73j;h=3
 for c in w*n:
  if p not in last:
   if c=='L':initial.add(p)
  else:assert last[p]!=c
  last[p]=c;h=(h+(1 if c=='R'else-1))%4;p+=v[h]
 assert len(initial)==slope*n+constant
out=dict(status='PASS exact all-N first-L fiber count',word_sha256=hashlib.sha256(w.encode()).hexdigest(),orbits=len(g),spans=dict(spans),slope=slope,constant=constant,boundary_orbits=boundary,minimal_input_black='406*N+57 for every integer N>=1',minimal_output_black='590*N+57',net_black_change_per_period=net,scope='This exact repeated word requires unbounded initial black supply at its entry and cannot persist forever on any finite board. Does not bound earlier finite-seed preparation or exclude arbitrarily long wave prefixes from a fixed-mass family.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
