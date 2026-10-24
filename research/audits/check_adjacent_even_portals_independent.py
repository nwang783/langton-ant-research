from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__);D=S.parents[1]/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files={'even_one_use_LL_portals_cannot_be_adjacent.md':'a0095ea6','check_adjacent_even_one_use_portals.py':'b91c0536','check_adjacent_even_one_use_portals.json':'fb0d686e'}
for f,h in files.items():assert sha(D/f).startswith(h)
J=json.loads((D/'check_adjacent_even_one_use_portals.json').read_text());H='NESW';V=[1j,1,-1j,-1];rows=[]
for upper,lower in product(['EWW','EWWE'],repeat=2):
 hs={}
 for i,y in enumerate([upper,lower]):
  s=-2j*i;hs.update({1+1j+s:'SN',1j+s:y,0j+s:'NNSS',1+0j+s:'EE'})
 succ={};bad=[]
 for p,w in hs.items():
  for d,v in enumerate(V):
   q=p+v
   if q not in hs:continue
   sr=[r for r,c in enumerate(w)if(H.index(c)+(1 if r%2==0 else-1))%4==d];tr=[r for r,c in enumerate(hs[q])if H.index(c)==d]
   if len(sr)!=len(tr):bad.append((p,q,d,sr,tr))
   else:succ.update({(p,r):(q,s)for r,s in zip(sr,tr)})
 au=next(z for z in J['rows']if z['upper_root']==upper and z['lower_root']==lower)
 if lower=='EWW':
  assert bad and any(p==-1j and q==0j and d==0 and len(sr)==1 and len(tr)==2 for p,q,d,sr,tr in bad);assert au['result']=='port'
  rows.append(dict(upper=upper,lower=lower,reason='one north output versus two arrivals'))
 else:
  assert not bad;path=[(1-1j,0),(-1j,1),(-2j,3),(1-2j,1),(1-1j,1),(-1j,2),(0j,0),(1+0j,0),(1-1j,0)]
  assert all(succ[e]==f for e,f in zip(path,path[1:]))and path[0]==path[-1]
  serial=[[[int(p.real),int(p.imag)],r]for p,r in path];assert au['result']=='actual_event_cycle'and au['certificate']==serial
  rows.append(dict(upper=upper,lower=lower,actual_same_event_cycle=serial))
O=dict(status='PASS exact adjacent even one-use portal obstruction',files={f:sha(D/f)for f in files},script=sha(S),rows=rows,scope='Exactly two displayed complete physical portals with immediate one-use Aupper→Blower. LowerO fails counts; lowerU closes an8-step ACTUAL successor cycle at the SAME physicalR0. No temporal voltage/exterior stock can repair that exact cycle. Single preparedF48/F49 and altered/spaced joins remain allowed; no global/critical or exterior cap premise needed after histories are fixed.')
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(sha(S.with_suffix('.json')))
