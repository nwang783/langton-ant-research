from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/exit_bud_halfplane_frozen_20261023_1309';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_exit_bud_maturation_halfplane.json').read_text());C5={tuple(map(int,l.split()[:8]))for l in(B/'04_01_closure.tsv').read_text().splitlines()};mp={a:i for i,a in enumerate(ids)}
queries=[];wrong=[];buds=[];endpoints=[];effects=[];r=1-1j
for p in ids:
 e,h=G[p][:2];o=e+rotation(r,h);assert o in G[p][4]
 assert r not in G[p][2] and r not in G[p][3]|G[p][4]
 rows=[]
 for delta in range(3):
  age=counts[p]+delta;ch=(-age)%4;assert 0<=age<=4
  for a in ids:
   for inp in G[a][3]:
    pos=o-rotation(inp,ch)
    row=(p,delta,age,a,xy(inp),(*xy(pos),ch),xy(o))
    if(int(pos.real+pos.imag)+ch)%2:wrong.append(row);continue
    key=(mp[p],mp[a],*xy(pos),ch,*xy(o),age);assert key in C5
    queries.append((row,key));rows.append(key)
 assert len(rows)==29;buds.append((p,(*xy(e),h),xy(o)))
for a in(0,4,7):
 step=rotation(G[a][0],1);assert step.real>0
 for inp in G[a][3]:
  pos=r-rotation(inp,1);end=pos+step
  assert pos.real<=0 and end.real>=1
  endpoints.append((a,xy(inp),xy(pos),xy(end)))
assert all(z.imag<1 for z in K)
for a in ids:
 for z,bit in G[a][2].items():
  if z.imag>=1:
   pos=1-z.imag+(z.real-1)*1j;assert pos.real<=0 and rotation(r-pos,-1)==z
   if bit:assert z in G[a][3]
   effects.append((a,xy(z),bit,(*xy(pos),1)))
AQ={(q['source'],q['postexit_C_age'],q['source_included_C_age'],q['consumer'],tuple(q['input']),tuple(q['consumer_pose']),tuple(q['exit_bud_output'])):tuple(q['exact_counted_query']) for q in J['all_exact_exclusion_queries']}
assert dict(queries)==AQ and len(queries)==232
AW={(q['source'],q['postexit_C_age'],q['source_included_C_age'],q['consumer'],tuple(q['input']),tuple(q['consumer_pose']),tuple(q['exit_bud_output'])) for q in J['sector_impossible_options']};assert set(wrong)==AW and len(wrong)==320
AE={(q['consumer'],tuple(q['input']),tuple(q['consumer_head']),tuple(q['raw_end'])) for q in J['zero_C_E_consumer_endpoints']};assert set(endpoints)==AE and len(endpoints)==8
AF={(q['target'],tuple(q['local_cell']),bit,tuple(q['relative_B_pose'])) for bit,field in((False,'halfplane_target_white_avoidances'),(True,'halfplane_target_black_origins'))for q in J[field]};assert set(effects)==AF
assert sum(not q[2]for q in effects)==115 and sum(q[2]for q in effects)==23
result=dict(status='PASS independent literal bud, all exact counted queries and halfplane endpoints',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),buds=buds,exact_queries=[dict(row=q,query=k)for q,k in queries],wrong_sector_count=len(wrong),endpoints=endpoints,white_avoidances=115,black_origins=23,scope='Only fresh universal producer exit bud. Cannot retire within 0/1/2 postexit Cs by signed exact ages0..4. At3 postexit Cs before a marked E boundary X<=0, any first strict retirement must be a zero-C E packet; it ends X>=1 and all remaining E zero-C steps increase X, contradiction. No Y restriction. Positive-C consumers at the same input clock are not globally forbidden but cannot finish before that boundary. Initial-factor boundary exception retained; no V1/U1 closure or capture.')
P.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items()if k!='exact_queries'})
