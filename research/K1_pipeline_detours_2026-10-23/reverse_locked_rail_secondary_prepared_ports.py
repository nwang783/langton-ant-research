"""Secondary ports of a root-free plateau's reverse locked rail.
Reverse WHITE-even and BLACK-odd histories only, lambda=0,L floor=-3.
No whole-front or period search; all immediate physical port profiles.
"""
from itertools import product
from collections import Counter
from pathlib import Path
import json
H='NESW';O=[];E=[]
def local(h,black,base):
 R=[x for i,x in enumerate(h)if(i%2==1)==black];L=[x for i,x in enumerate(h)if(i%2==0)==black];rs=Counter(R);ls=Counter(L)
 out=[H[(H.index(x)+(-1 if(i%2==0)==black else 1))%4]for i,x in enumerate(h)]
 if h[0]in'EW':
  a=-2-rs['W'];cs=dict(NE=-2,SW=a+rs['E']);l=dict(NW=a-ls['E'],SE=a-ls['W']);other=cs['SW']
 else:
  a=-2-rs['N'];cs=dict(SE=-2,NW=a+rs['S']);l=dict(NE=a-ls['S'],SW=a-ls['N']);other=cs['NW']
 if min(l.values()) < -3:return
 return dict(headings=h,initial='BLACK'if black else'WHITE',turns=''.join('L'if(i%2==0)==black else'R'for i in range(len(h))),outgoing=''.join(out),C=cs,L=l,other=other)
for n in range(1,5):
 black=n%2==1
 for h in product('EW',repeat=n):
  h=''.join(h)
  if h.count('W')!=1:continue
  r=local(h,black,'O')
  if r:O.append(r)
 for h in product('NS',repeat=n):
  h=''.join(h);r=local(h,black,'E')
  if r and r['outgoing'].count('E')==1:E.append(r)
assert len(O)==len(E)==6
pairs=[]
for o,e in product(O,E):
 if o['other']!=e['other']:continue
 a=[i for i,x in enumerate(o['outgoing'])if x=='S'];b=[i for i,x in enumerate(e['headings'])if x=='S']
 if len(a)!=len(b):continue
 ns=[('O',i)for i in range(len(o['headings']))]+[('E',i)for i in range(len(e['headings']))];edges=[]
 for v,h in [('O',o['headings']),('E',e['headings'])]:
  for i in range(len(h)-1):edges.append(((v,i),(v,i+1),4))
 for i,j in zip(a,b):edges.extend([(('O',i),('E',j),1),(('E',j),('O',i),-1)])
 si=o['headings'].index('W');fi=e['outgoing'].index('E');edges.append((('O',si),('E',fi),1));d={x:0 for x in ns}
 for _ in ns:
  change=False
  for x,y,k in edges:
   if d[y]<d[x]+k:d[y]=d[x]+k;change=True
  if not change:break
 else:continue
 off=d['O',si];t={v:[d[v,i]-off for i in range(len(h))]for v,h in [('O',o['headings']),('E',e['headings'])]}
 pairs.append(dict(O=o,E=e,W_input_rank=si,E_output_rank=fi,minimum_clocks=t,next_N_outputs=o['outgoing'].count('N'),previous_N_inputs=e['headings'].count('N')))
assert len(pairs)==11
out=dict(scope=__doc__,O=O,E=E,pairs=pairs)
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(O),'O profiles,',len(E),'E profiles,',len(pairs),'same-level chronological pairs')
