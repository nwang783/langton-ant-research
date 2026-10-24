#!/usr/bin/env python3
"""Exact countercheck: balanced internal-lifetime cycles are not deletable modules.
All31 nonempty subsets of the supplied standard104 internal components fail
literal stable read alternation after phase deletion. No other surgery excluded.
"""
from pathlib import Path
from collections import defaultdict
import hashlib,json
from lifetime_boundary_graph import analyze
from check_all_cut_wave_interfaces import WORDS
from check_extremal_read_coupling import event_word,quotient,front
R=Path(__file__).resolve().parent

def main():
 W=WORDS['S104'];F=analyze(W);components=[set(c['events'])for c in F['internal_cycles']];assert sorted(map(len,components))==[2,2,2,2,14]
 assert not any(a&b for i,a in enumerate(components)for b in components[i+1:])
 for C in components:assert sum(1 if W[i]=='R'else-1 for i in C)==0
 rows=[]
 for mask in range(1,32):
  cut=set().union(*(C for i,C in enumerate(components)if mask>>i&1));w=''.join(c for i,c in enumerate(W)if i not in cut);E,d,h=event_word(w);P=len(w)
  assert h==0 and d!=(0,0)and w.count('R')-w.count('L')==12
  H=defaultdict(list)
  for e in E:
   q,k=quotient(e['p'],d);H[q].append({'phase':e['t'],'full_lift':k,'stable_clock':e['t']-P*k,'position':e['p'],'turn':e['c']})
  fail=None
  for q,es in H.items():
   es.sort(key=lambda e:e['stable_clock'])
   for a,b in zip(es,es[1:]):
    if a['turn']==b['turn']:
     fail={'full_class_representative':q,'complete_stable_class_history':es,'earlier':a,'later':b};break
   if fail:break
  assert fail is not None
  assert not front(w)['complete_white']
  rows.append({'selected_component_indices':[i for i in range(5)if mask>>i&1],'deleted_event_phases':sorted(cut),'remaining_word':w,'period':P,'full_drift':d,'heading_restored':True,'turn_excess':12,'literal_non_alternation_witness':fail})
 assert len({r['remaining_word']for r in rows})==31
 out={'scope':__doc__,'standard_word_sha256':hashlib.sha256(W.encode()).hexdigest(),'five_complete_internal_components':[sorted(C)for C in components],'all31_cases':rows,'scope_warning':'Only deleting entire selected internal component event sets and keeping the remaining cyclic order is covered. This does not exclude another reconnection, chronological rearrangement or controller. The original alpha/beta compression is not a physical splice.','dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['lifetime_boundary_graph.py','CHRONOLOGICAL_LIFETIME_BOUNDARY_GRAPH.md','check_extremal_read_coupling.py']}}
 (R/'standard_lifetime_cycle_deletion_certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print('PASS all31 distinct balanced deletions restore heading and excess12 but fail stable alternation on every initial board')
if __name__=='__main__':main()
