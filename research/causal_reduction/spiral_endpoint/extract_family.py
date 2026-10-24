from probe_continuation import sim,initial,D
from pathlib import Path
import json
w,poses,_=sim(100,12000)
parts={'P':w[:1540],'V':w[1540:1550],'C':w[2450:2472],'W':w[2472:2482],'D':w[3472:5021],'H':w[5021:5125]}
assert [len(parts[k])for k in parts]==[1540,10,22,10,1549,104]
def test(n,extra=10):
 word='RL'*n+parts['P']+parts['V']*(n-9)+parts['C']+parts['W']*n+parts['D']+parts['H']*extra
 B=initial(n);x=y=h=0
 for t,c in enumerate(word):
  if ((x,y)in B)!=(c=='L'):return dict(n=n,valid=False,time=t,pose=(x,y,h))
  B.symmetric_difference_update({(x,y)});h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 return dict(n=n,valid=True,end=(x,y,h),mass=len(B))
results=[test(n)for n in range(9,201)]
assert all(r['valid']for r in results if r['n']>=11)
P=Path(__file__).resolve().parent
(P/'family_words.json').write_text(json.dumps(parts,indent=2));(P/'family_controls.json').write_text(json.dumps(results,indent=2))
print('exceptions:',[r for r in results if not r['valid']]);print('sample',results[-1])
