from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/common_output_4C_frozen_20261023_1333';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_common_output_four_C_barrier.json').read_text());q=2+0j;age2=[];endpoints=[]
assert q not in K
for a in ids:
 assert q in G[a][4]and q not in G[a][3]and G[a][2][q]is False
 assert len(raws[a])%2==counts[a]%2
 # Independently locate first raw+marker read of that cell.
 p=0j;h=0
 for t,c in enumerate(raws[a]+mark):
  if p==q:assert t==8 and c=='R';break
  h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 for inp in G[a][3]:
  assert oldages[a,inp]>=2
  if oldages[a,inp]==2:
   pos=q-rotation(inp,2);assert(a,inp)in((4,3j),(5,3j))and(pos,2)==(2+3j,2)
   assert(int(pos.real+pos.imag)+2)%2==1;age2.append((a,xy(inp),(*xy(pos),2)))
for h in(0,1):
 for a in(0,4,7):
  step=rotation(G[a][0],h);assert step.real>=0
  for inp in G[a][3]:
   pos=q-rotation(inp,h);e=pos+step;assert e.real>=2
   endpoints.append((4-h,h,a,xy(inp),xy(pos),xy(e),h,int(e.real)+h))
AA={(r['age'],r['heading'],r['consumer_base'],tuple(r['input']),tuple(r['base_start']),tuple(r['base_end']),r['remaining_C_to4'],r['minimum_four_C_final_x'])for r in J['all16_after_consumer_endpoints']};assert set(endpoints)==AA and len(endpoints)==16
assert walk(C)[:2]==(1j,3)and rotation(1j,1)==1
out=dict(status='PASS independent common-output maturity and unconditional complete-boundary4C nonreturn',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),common_fresh_outputs=8,common_marker_whites=8,age2_sector_cases=age2,endpoints=endpoints,scope='ANY complete8 source including factor-first freshly outputs entryrelative(2,0). JO plus sector excludes ages0..2. Actual endpoint cones keep it current before any3C E or4C N marked targetX<=1. Exact4C same-pose target demands this cell initiallywhite, contradiction. No predecessor, funding, new counted clause, atomic-cut extension or higher-C recurrence exclusion.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='endpoints'})
