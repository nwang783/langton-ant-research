import itertools,json
from collections import Counter
from pathlib import Path
from verify_uv_interior_crossing import window
words=list(map(''.join,itertools.product('UV',repeat=5)));north={w:window(w,0)for w in words};south={w:window(w,2)for w in words};miss=[];groups=Counter()
for x in words:
 af,al,as_,ae=north[x]
 for y in words:
  bf,bl,bs,be=south[y]
  good=[q for q in al.keys()&bf.keys()if al[q][3]==bf[q][3] and as_[1]<q[1]<ae[1]-1 and be[1]+1<q[1]<bs[1] and q[1]<ae[1]-5]
  if not good:miss.append({'north':x,'south':y});groups[x[1:3],y[1:3]]+=1
print('cases',len(words)**2,'unexcluded',len(miss),'by incoming/outgoing',dict(groups))
Path(__file__).with_name('uv_center_scattering.json').write_text(json.dumps({'unexcluded':miss,'groups':[(a,b,n)for(a,b),n in groups.items()]},indent=2))
