"""Tiny independent geometric controls, not a front or large-polygon search."""
from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];R=ROOT/'K1_pipeline_detours_2026-10-23';V=(1j,1,-1j,-1);records=[]
for n in (4,8):
 for turns in product((1,-1),repeat=n):
  p=0j;h=0;vertices=[];edges=[]
  for t in turns:
   vertices.append(p);h=(h+t)%4;q=p+V[h];edges.append(frozenset((p,q)));p=q
  if p!=0 or h!=0 or len(set(edges))!=n:continue
  repeats=[z for z,k in Counter(vertices).items()if k==2]
  if n==4:assert len(set(vertices))==4 and abs(sum(turns))==4
  else:
   assert len(set(vertices))==7 and len(repeats)==1 and abs(sum(turns))==4
   if sum(turns)==-4:assert {vertices[i]for i,t in enumerate(turns)if t==1}==set(repeats)
  records.append(dict(length=n,turns=''.join('R'if t==1 else'L'for t in turns),distinct_vertices=len(set(vertices)),turn_sum=sum(turns)))
assert Counter(r['length']for r in records)=={4:2,8:8}
# Independently reconstructed signed local ordinal rows, not author's table.
rows=json.loads(SELF.with_name('check_stream_sheet_exchange_independent.json').read_text())['rows'];checks=0
for row in rows:
 M=max(row['face_heights'][c]for c in ('NW','SE'));arcs=row['levels'].get(str(M-1),[])
 assert not(len(arcs)==2 and all(t==1 for h,o,t in arcs));checks+=1
out=dict(status='PASS independent short edge-simple polygon and penultimate local junction controls',note_sha256=hashlib.sha256((R/'max_turn_middle_stock_hole_length.md').read_bytes()).hexdigest(),orientation_note_sha256=hashlib.sha256((R/'penultimate_max_adjacent_contour_orientation.md').read_bytes()).hexdigest(),short_closed_walks=records,local_rows_checked=checks,analytic_result='Every contractible penultimate canonical cycle with a RIGHT turn around a global max face has at least12 edges.',scope='Counterclockwise orientation comes from signed high-region connectivity. Counts apply per distinct canonical node, not per renewal.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
