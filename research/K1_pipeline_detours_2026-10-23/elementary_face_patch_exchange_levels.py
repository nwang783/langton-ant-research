"""All 24 two-R local exchanges: top-C and bottom-L endpoint directions.
Necessary local geometry only, not a complete front or an assumed splice.
"""
from itertools import product
from collections import Counter
from pathlib import Path
import json
H='NESW';rows=[]
for n in (3,4):
 for z in product('EW',repeat=n):
  h=''.join(z);rs=Counter(h[::2]);ls=Counter(h[1::2]);a=-max(rs['E'],rs['W']);C=dict(NE=a+rs['W'],SW=a+rs['E']);L=dict(NW=a-ls['E'],SE=a-ls['W']);rc={'E':C['SW'],'W':C['NE'],'N':C['NE'],'S':C['SW']}
  ic=Counter();oc=Counter();ev=[]
  for i,x in enumerate(h):
   y=H[(H.index(x)+(1 if i%2==0 else -1))%4];ic[x]+=1;oc[y]+=1
   ev.append(dict(rank=i,x=x,y=y,il=rc[x]-ic[x]+1,ol=rc[y]-oc[y]+1))
  pairs=[]
  for i in(1,2):
   s=3-i;x=ev[i]['x'];y=ev[s]['y'];j=ev[i]['il'];assert j==ev[s]['ol']
   turn='R'if(H.index(y)-H.index(x))%4==1 else'L'
   c=C['SW'if x=='E'else'NE'] if turn=='R'else None
   l=L['NW'if x=='E'else'SE'] if turn=='L'else None
   top=c==j if c is not None else False
   bottom=l==j-1 if l is not None else False
   if top:assert turn=='R'and j==a+1 and rs['E']==rs['W']==1
   if bottom:assert turn=='L'and j==a
   pairs.append(dict(in_rank=i,out_rank=s,j=j,turn=turn,selected_C=c,selected_L=l,top_C_possible=top,bottom_L_possible=bottom))
  assert sorted(p['j']for p in pairs)==[a,a+1]
  rows.append(dict(headings=h,center=a,C=C,L=L,pairs=pairs,elementary_pair_possible=any(p['top_C_possible']for p in pairs)and any(p['bottom_L_possible']for p in pairs)))
assert len(rows)==24 and sum(r['elementary_pair_possible']for r in rows)==8
out=dict(scope=__doc__,exchange_rows=len(rows),elementary_pair_rows=8,rows=rows)
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n');print('PASS all24 exchange rows, eight possible C-top/L-bottom joint rows')
