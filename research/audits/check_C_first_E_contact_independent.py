from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/C_first_E_crossing_frozen_20261023_1428';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_C_first_E_crossing.json').read_text());C5={tuple(map(int,l.split()[:8]))for l in(B/'04_01_closure.tsv').read_text().splitlines()};mp={a:i for i,a in enumerate(ids)};rows=[]
for src in ids:
 pp=G[base[src]][0];hh=0
 for shift in range(counts[src]):
  out=pp+rotation(2+0j,hh);assert out in G[src][4]
  for dst in(4,5,6):
   pos=pp+rotation(-1+0j,hh);h=(hh+1)%4;assert pos+rotation(3j,h)==out
   query=(mp[src],mp[dst],*xy(pos),h,*xy(out),3+shift);excluded=query in C5
   if not excluded:assert src==1 and shift==0 and dst in(4,5)and pos==1j and h==1 and out==3+1j
   rows.append(dict(source=src,shift=shift,target=dst,query=query,excluded=excluded))
  pp+=rotation(1j,hh);hh=(hh-1)%4
assert len(rows)==21 and sum(r['excluded']for r in rows)==19
assert {tuple(r['query'])for r in rows}=={tuple(r['counted_query'])for r in J['all_21_role_tail_cases']}
# Old atomic output cannot be retired and replaced before target: earliest age3,
# zero-C E consumer is the only timing-compatible strict retirement.
ends=[]
for a in(0,4,7):
 for z in G[a][3]:
  pos=2-rotation(z,1);end=pos+rotation(G[a][0],1);assert end.real>=2;ends.append((a,xy(z),xy(end)))
assert all(rotation(G[a][0],1).real>=0 for a in(0,4,7))
out=dict(status='PASS independent old-identity survival and complete21 C-role/tail queries',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),queries=rows,strict_retiring_endpoints=ends,scope='Exact actualC0N to Vbase(-1,0,E), atomic-entryC3: source is firstC of factor-FIRST fullDC and target fullV/VC. No first-contact premise needed. Not no-crossing, arbitrary atomic language, or a higher-C/global result.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
