from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/four_C_bud_nonreturn_frozen_20261023_1324';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_four_C_bud_nonreturn.json').read_text());rows=[]
for h in(0,1):
 for a in(0,4,7):
  step=rotation(G[a][0],h);assert step.real>=0
  for inp in G[a][3]:
   p=1-1j-rotation(inp,h);end=p+step;assert end.real>=1
   rows.append((4-h,h,a,xy(inp),xy(p),xy(end),h,int(end.real)+h))
# The independent raw walker uses a zero-N default; literal C has displacement i and turn-1.
assert walk(C)[:2]==(1j,3)and rotation(walk(C)[0],1)==1
AA={(q['first_retirement_postexit_C'],q['heading'],q['consumer'],tuple(q['input']),tuple(q['base_start']),tuple(q['base_end']),q['remaining_C'],q['final_marked_min_x'])for q in J['all16_endpoints']};assert set(rows)==AA and len(rows)==16
for p in ids:
 e,h=G[p][:2];assert e+rotation(1-1j,h)in G[p][4]
out=dict(status='PASS independent four-C persistence endpoint and fresh-output collision reduction',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),endpoints=rows,C_E_to_N=[1,0,0],scope='Uses signed typed exit-bud no-retirement atpostexitdelta0..2. Strict retirement atdelta3 leaves one E-to-N C and ends finalX>=2; delta4 zero-C N endsX>=1. Hence oldbudcurrent before any4C markedN boundaryX<=0. An exact noninitial pose repeat would install a different fresh predecessor output at the same still-current cell, contradicting ordered residual freshness. Factor-first exception retained; no larger-C/general recurrence exclusion.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='endpoints'})
