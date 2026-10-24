from collections import Counter
from pathlib import Path
import json,hashlib
ROOT=Path('/workspace/shared/langton');N=20;columns=[]
for q in range(N):
 p=q if q%2 else q+2
 for c in range(p+1,N+1):
  exits=[(1j if r==p else -1j)*(-1j if r%2==0 else 1j)for r in range(c)]
  for d in range(q+1,N+1):
   enters=[(-1j if r==q else 1j)/( -1j if r%2==0 else 1j)for r in range(d)]
   if exits.count(1)!=enters.count(1):continue
   columns.append((q,p,c,d,exits.count(-1),enters.count(-1)))
checks=0;caps=set();mixed=0
for x in columns:
 for y in columns:
  if x[4]!=y[5]or y[4]!=x[5]:continue
  q,p,c,d,_,_=x;qq,pp,cc,dd,_,_=y
  small=(c-2*(-1)**q,d-2*(-1)**q,cc-2*(-1)**qq,dd-2*(-1)**qq);lo=min(small);hi=max(small)
  assert lo>=0 and hi-lo<=1 and small[0]>0 and small[2]>0
  if hi>lo:
   highs=[i for i,z in enumerate(small)if z==hi];assert len(highs)==2 and (highs[1]-highs[0])%4 in(1,3)
  if q%2!=qq%2:
   even,odd=(x,y)if q%2==0 else(y,x);assert even[2]>=odd[2]+3 and even[3]>=odd[3]+3;mixed+=1
  if q!=qq and max(c,d,cc,dd)<=4:
   assert sorted((q,qq))==[1,3]
   z=(x,y)if q==1 else(y,x);profile=(z[0][2],z[0][3],z[1][2],z[1][3]);assert profile in((3,3,4,4),(4,4,4,4));caps.add(profile)
  checks+=1
assert caps=={(3,3,4,4),(4,4,4,4)}
J={'status':'PASS direct compass-port controls for the analytically reviewed shifted profile','maximum_read_count_control':N,'local_column_states':len(columns),'matched_pair_controls':checks,'mixed_parity_controls':mixed,'cap4_profiles':sorted(caps),'scope':'Conditional on all four lowest-row classes singleton, actual full drift(-4,0). No all-cap front exclusion.','hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in(Path(__file__),ROOT/'periodic_classification_new/axis_singleton_shifted_count_profile.md')}}
Path(__file__).with_suffix('.json').write_text(json.dumps(J,indent=2)+'\n');print(json.dumps(J))
