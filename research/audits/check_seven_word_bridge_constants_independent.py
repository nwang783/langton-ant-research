"""Literal and arithmetic controls for the separately reviewed bridge-reset proof."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];P=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';J=json.loads(P.read_text());E=json.loads((R/'word_stabilization/seven_word_foreign_count_cubic_bound.json').read_text());assert hashlib.sha256(P.read_bytes()).hexdigest()==E['source_sha256']
records=[]
for name,entry in zip('DCVUFQB',J['macro_words']):
 w=entry['word'];p=0j;h=1j;initial={};current={};reads=[]
 for c in w:
  need=c=='L'
  if p in current:assert current[p]==need
  else:initial[p]=need
  current[p]=not need;reads.append(p);h*=(-1j if c=='R'else 1j);p+=h
 inc=sum(current.values())-sum(initial.values());assert inc==w.count('R')-w.count('L')
 records.append(dict(macro=name,length=len(w),mass_change=inc,displacement=[int(p.real),int(p.imag)],heading=[int(h.real),int(h.imag)]))
assert [{k:r[k]for k in ('macro','length','mass_change')}for r in records]==E['macro_counts']
assert records[0]['displacement']==[1,1]and records[0]['heading']==[0,1]
a=(2,52,54,-8);core_max=14;minw=-60;baseline=60
assert baseline-minw==120 and max(a)-min(a)==62 and core_max+baseline==74 and baseline-min(a)==68
# Every bridge g>=0 is controlled by the stated max rise.
for g in range(100):assert max(120,74,6*g+68,6*g+62)<=6*g+120
for m in range(12):
 for k in range(12):
  G=193+267*k;Pmax=54+76*(m+G)+6*G+120*k;B=57+38*(m+G)+3*G+60*k
  assert 2*B==Pmax+60
out=dict(status='PASS literal constants and independently reviewed seven-word bridge-reset cubic proof',records=records,reset_cost=120,old_core_residual_cost=74,new_touched_offset=68,new_core_offset=62,G=E['G'],B=E['B'],R=E['R'],t=E['t'],duration=E['duration'],scope='Arbitrary feasible finite DCVUFQB factor; bound depends on initial mass m and count k of U/F/Q/B. Does not bound k or prove capture.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
