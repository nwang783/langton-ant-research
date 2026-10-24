"""Exact mature-profile interface between two frozen forward108 copies.
This does not give finite bootstrap, endpoint routing, or debris cleanup.
"""
import json,collections,hashlib
from pathlib import Path
import certify_short_refinement_rup as core
P=Path(__file__).resolve().parent;Q=json.loads((P/'forward108_prepared_control.json').read_text())['word']
def prof(h):
 rr,e,g=core.trace(Q,(0,0),h);sgn=e[0]//2;by=collections.defaultdict(list)
 for t,(p,hh,c)in enumerate(rr):by[p[0]-p[1],p[0]%2].append((t-sgn*len(Q)*(p[0]//2),c))
 I=set();O=set()
 for a,v in by.items():
  v.sort();assert all(x[1]!=y[1]for x,y in zip(v,v[1:]));
  if v[0][1]=='L':I.add(a)
  if v[-1][1]=='R':O.add(a)
 return set(by),I,O
R,I,O=prof(1);records=[];hits=[]
for h in(1,3):
 r,i,o=prof(h)
 # At least one output black must coincide with an input black. Any exact
 # input match must be among this finite anchored displacement inventory.
 shifts=sorted({(a-c,b^d)for a,b in O for c,d in i if(a-c)%2==0})
 for dn,xp in shifts:
  sh=lambda S:{(a+dn,b^xp)for a,b in S}
  rr,ii=sh(r),sh(i);missing=ii-O;pollution=(O&rr)-ii
  z=dict(incoming_heading=h,normal_shift=dn,x_parity=xp,missing=sorted(missing),pollution=sorted(pollution),input=sorted(ii),read=sorted(rr))
  records.append(z)
  if not missing and not pollution:hits.append(z)
out=dict(scope=__doc__,source_input=sorted(I),source_output=sorted(O),cases=len(records),hits=hits,records=records,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'forward108_self_interfaces.json').write_text(json.dumps(out,indent=2)+'\n');print('cases',len(records),'hits',hits);print('closest',sorted([(len(z['missing'])+len(z['pollution']),z['incoming_heading'],z['normal_shift'],z['x_parity'],z['missing'],z['pollution'])for z in records])[:6])
