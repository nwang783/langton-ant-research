from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];J=json.loads((ROOT/'nonlinear_global_budget_2026-10-23/prepared_travelling_wave_certificate.json').read_text());w=J['word'];P=len(w);p=-6-6j;h=0;v=(1j,1,-1j,-1);g=defaultdict(list)
for i,c in enumerate(w):
 x,y=int(p.real),int(p.imag);g[x-y,x%14].append(((x-x%14)//14,i,c));h=(h+(1 if c=='R'else-1))%4;p+=v[h]
assert p==8+8j and h==0
slope=constant=0;boundary=[];spans=Counter()
for cl,a in g.items():
 lo=min(z[0]for z in a);hi=max(z[0]for z in a);span=hi-lo;spans[span]+=1;assert span in(0,1)
 first=lambda b:min((i-P*k,c)for k,i,c in b)[1]=='L'
 full=first(a);slope+=full
 if span:
  l=first([z for z in a if z[0]==lo]);r=first([z for z in a if z[0]==hi]);constant+=l+r-full;boundary.append(dict(orbit=cl,first_left=l,first_full=full,first_right=r,contribution='(N-1)*full+left+right'))
assert slope==197 and constant==1 and spans=={0:555,1:2}
# Exact algebra: span0 contributes N*full; span1 contributes (N-1)*full+left+right for every integer N>=1.
net=w.count('R')-w.count('L');assert net==104
for n in(1,2,3,7):
 initial=set();last={};p=-6-6j;h=0
 for c in w*n:
  if p not in last:
   if c=='L':initial.add(p)
  else:assert last[p]!=c
  last[p]=c;h=(h+(1 if c=='R'else-1))%4;p+=v[h]
 assert len(initial)==slope*n+constant
out=dict(status='PASS exact all-N first-L fiber count',word_sha256=hashlib.sha256(w.encode()).hexdigest(),orbits=len(g),spans=dict(spans),slope=slope,constant=constant,boundary_orbits=boundary,minimal_input_black='197*N+1 for every integer N>=1',minimal_output_black='301*N+1',net_black_change_per_period=net,scope='This exact repeated word requires unbounded initial black supply at its entry and cannot persist forever on any finite board. Does not bound earlier finite-seed preparation or exclude arbitrarily long wave prefixes from a fixed-mass family.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
