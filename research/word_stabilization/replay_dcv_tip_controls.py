import json
from pathlib import Path
W={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR'};dirs=(1j,1,-1j,-1);M='LLLLRLRRRRL'
def replay(s):
 p=0j;h=0;last={};seed=[];reads=[];bound=[];fuel=[]
 for a in s:
  bound.append((len(reads),p,h));f=len(seed)
  for c in W[a]:
   if last.get(p)==c:return None
   if p not in last and c=='L':seed.append((int(p.real),int(p.imag)))
   last[p]=c;reads.append((p,c));h=(h+(1 if c=='R'else-1))%4;p+=dirs[h]
  fuel.append(len(seed)-f)
 q=bound[-1][1]+complex(1,2)*(-1j)**bound[-1][2];r=[(t,c)for t,(z,c)in enumerate(reads)if z==q];end=[int(p.real),int(p.imag),h];rawseed=list(seed)
 for c in M:
  if last.get(p)==c:return None
  if p not in last and c=='L':seed.append((int(p.real),int(p.imag)))
  last[p]=c;h=(h+(1 if c=='R'else-1))%4;p+=dirs[h]
 return {'macros':s,'raw_word':''.join(W[a]for a in s),'actual_right_marker':M,'seed':seed,'raw_seed':rawseed,'entry_mass_with_marker':len(seed),'raw_macro_fuel':fuel,'raw_endpoint':end,'target_tip':[int(q.real),int(q.imag)],'target_tip_reads':r}
controls=[]
for s in ['DCCCV','DDCDCDCDV','DCVCCVV']:
 a=replay(s);assert a and len(a['target_tip_reads'])>=3;a['one_macro_extensions']={b:replay(s+b) is not None for b in W};controls.append(a)
Path('dcv_vtip_reuse_controls.json').write_text(json.dumps({'scope':'Exact finite marked factors, not an infinite counterexample; the second avoids a DCCC packet.','controls':controls},indent=2));print([(a['macros'],a['entry_mass_with_marker'],a['raw_macro_fuel'],a['target_tip_reads'],a['one_macro_extensions'])for a in controls])
