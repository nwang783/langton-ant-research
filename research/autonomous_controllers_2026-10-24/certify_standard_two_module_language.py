#!/usr/bin/env python3
"""All-length A10/B94 classification via two exact physical ownership guards."""
from pathlib import Path
from collections import defaultdict
import json,hashlib,sys
from check_extremal_read_coupling import event_word,quotient
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parent/'computability'))
from periodic_tail_checker import first_mismatch
from check_rigid_reachability import State
DELTA=(-1,1)

def minimal_factor(w,h=3):
 E,d,endh=event_word(w,h=h);B=set();seen={};seed=set()
 for e in E:
  p=e['p'];c=e['c']
  if p not in seen:
   if c=='L':seed.add(p);B.add(p)
  else:assert ('L'if p in B else'R')==c
  B.symmetric_difference_update({p});seen[p]=c
 return {'word':w,'initial_black':sorted(seed),'final_black':sorted(B),'head':d,'heading':endh,'all_events':E}

def main():
 src=json.loads((R/'C_cycle_excursion_normal_form_certificate.json').read_text());ww=src['standard_module_words'];words={'A':ww['A10'],'B':ww['B94']};H={};events={};classes=set()
 for a,w in words.items():
  E,d,h=event_word(w,h=3);assert d==DELTA and h==3;events[a]=E;H[a]=defaultdict(list)
  for e in E:
   q,k=quotient(e['p'],DELTA);H[a][q].append({'relative_module_index':-k,'local_phase':e['t'],'turn':e['c'],'heading':e['hi'],'local_position':e['p']});classes.add(q)
  for rows in H[a].values():rows.sort(key=lambda z:(z['relative_module_index'],z['local_phase']))
 qfuel=(0,-1);qcollision=(0,-3)
 hf={a:[(z['relative_module_index'],z['local_phase'],z['turn'])for z in H[a].get(qfuel,[])]for a in 'AB'}
 hc={a:[(z['relative_module_index'],z['local_phase'],z['turn'])for z in H[a].get(qcollision,[])]for a in 'AB'}
 assert hf['A']==[(0,5,'L')]
 assert hf['B']==[(-1,7,'R'),(0,5,'R'),(0,9,'L'),(0,13,'R'),(1,23,'R'),(1,31,'L'),(1,39,'R'),(2,25,'L'),(2,29,'R'),(2,41,'L'),(3,43,'L')]
 assert hc['A']==[]
 assert hc['B']==[(-2,17,'R'),(-1,15,'R'),(-1,19,'L'),(-1,35,'R'),(0,21,'L'),(0,33,'R'),(0,37,'L')]
 # AA at modules j-1,j: A_j L5 has no earlier read at qfuel+j*delta.
 assert all(k>=0 or(k==-1 and t==7 and c=='R')for k,t,c in hf['B'])
 # BB at modules j,j+1: choose anchor j+2, hence the first two listed reads.
 EB,d,h=event_word(words['B']*2,h=3);cell=EB[17]['p'];assert cell==EB[94+15]['p']
 visits=[e for e in EB if e['p']==cell];assert [e['t']for e in visits][:2]==[17,109]and visits[0]['c']==visits[1]['c']=='R'
 assert cell==(-2,-1)
 aa=minimal_factor(words['A']*2);assert aa['initial_black']==[(-1,0),(0,-1),(1,-1)]and len(aa['final_black'])==3
 # Positive complete WHITE case: AB is exactly the signed standard phase45.
 standard=json.loads((R.parent/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
 assert words['A']+words['B']==standard[45:]+standard[:45]
 bf=src['full_blank_realization'];st=next(x for x in bf['states']if x['time']==bf['A10_start'])
 assert len(st['full_black_field'])==758
 assert first_mismatch(State(frozenset(map(tuple,st['full_black_field'])),tuple(st['head']),st['heading']),words['A']+words['B'])is None
 # Reconstruct all n full-drift WHITE classes for representative standard powers.
 powers=[]
 for n in[1,2,3,5]:
  w=(words['A']+words['B'])*n;E,d,h=event_word(w,h=3);hist=defaultdict(list)
  for e in E:q,k=quotient(e['p'],d);hist[q].append((e['t']-k*len(w),e['c']))
  for hh in hist.values():hh.sort();assert hh[0][1]=='R'and all(a[1]!=b[1]for a,b in zip(hh,hh[1:]))
  powers.append({'module_count':2*n,'period':len(w),'full_drift':d,'complete_read_classes':len(hist)})
 out={'status':'AUTHOR all-length exact two-module language classification; independent audit pending',
  'scope':'Only concatenations of the two literal supplied modules, with one fixed orientation and anchor. No claim arbitrary ant trajectories enter this language.',
  'module_words':words,'common_initial_and_final_heading':3,'common_module_displacement':DELTA,
  'all104_local_events':events,'complete_cell_source_tables':[{'representative':q,'A_sources':H['A'].get(q,[]),'B_sources':H['B'].get(q,[])}for q in sorted(classes)],
  'AA_guard':{'cell_anchor':qfuel,'A_complete_sources':hf['A'],'B_complete_sources':hf['B'],'conclusion':'With A at j-1 and j, physical cell (0,-1)+j*delta is read first by A_j L5. It requires a distinct initial BLACK bit in a one-sided module tail.'},
  'BB_guard':{'cell_anchor':qcollision,'A_complete_sources':hc['A'],'B_complete_sources':hc['B'],'first_B_phase':17,'second_B_phase':15,'consecutive_same_physical_R_reads':visits[:2],'conclusion':'Literal BB fails on every board, independent of earlier or unread colors.'},
  'genuine_prepared_AA_full_factor':aa,'genuine_standard_AB_full_field':st,'standard_AB_exact_all_future_check':None,'standard_full_drift_power_controls':powers,
  'theorems':['Every complete WHITE bi-infinite module sequence is alternating AB or BA, so every complete WHITE periodic module word is a standard104 power/phase.','Any infinite actual trajectory from a finite field that follows only these modules has no BB and at most one AA per distinct initially BLACK witness cell; hence only finitely many AA and eventual standard alternation. The finite field is at module-tail entry, not necessarily the original seed.'],
  'dependencies':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in[R/'C_cycle_excursion_normal_form_certificate.json',R.parent/'recovered_bundle/ant_global/root/standard.json',R.parent/'computability/periodic_tail_checker.py',R.parent/'computability/check_rigid_reachability.py']}}
 dest=R/'standard_two_module_language_certificate.json';dest.write_text(json.dumps(out,indent=2)+'\n');print('PASS all-period A10/B94 language: WHITE iff alternating; finite-field infinite module tail eventually alternating');print(hashlib.sha256(dest.read_bytes()).hexdigest())
if __name__=='__main__':main()
