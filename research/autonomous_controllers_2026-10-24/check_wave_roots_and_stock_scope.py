#!/usr/bin/env python3
"""Supplied-wave causal roots, COMPLETE prepared fields, and stock counterchecks."""
import json,sys,hashlib
from pathlib import Path
from collections import defaultdict
from check_extremal_read_coupling import ROOT,event_word,quotient,cycles,D
from check_all_cut_wave_interfaces import WORDS,literal_pair
sys.path.insert(0,str(ROOT/'computability'))
from check_rigid_reachability import State,forward,transform,rot_point
from periodic_tail_checker import first_mismatch
G=ROOT/'nonlinear_global_budget_2026-10-23';OUT=Path(__file__).resolve().parent

def mask(q):return q[0]%2==0 and sum(q)%28==20

def graph(w):
 ev,d,h=event_word(w);H=defaultdict(list)
 for e in ev:
  r,k=quotient(e['p'],d);H[r].append(dict(e,clock=e['t']-len(w)*k))
 for es in H.values():es.sort(key=lambda e:e['clock']);assert all(a['c']!=b['c']for a,b in zip(es,es[1:]))
 F={};L={};I=[];O=[]
 for r,es in H.items():
  a,z=es[0],es[-1]
  if a['c']=='R':F[r]=quotient((r[0]+D[a['ho']][0],r[1]+D[a['ho']][1]),d)
  else:I.append(r)
  if z['c']=='L':L[r]=quotient((r[0]-D[z['hi']][0],r[1]-D[z['hi']][1]),d)
  else:O.append(r)
 de=sum((1 if e['c']=='R'else-1)for e in ev if mask(e['p']))
 return {'period':len(w),'drift':d,'read_classes':len(H),'first_black_roots':len(I),'last_black_roots':len(O),'first_R_cycles':cycles(F),'reverse_last_L_cycles':cycles(L),'selected_first_black':sum(map(mask,I)),'selected_last_black':sum(map(mask,O)),'selected_stock_delta':de}

def prepared(nf,word,bkey):
 N=json.loads((G/nf).read_text());start=tuple(N['pose'][0]);h0=N['pose'][1];stride=N['drift'][0];bulk=set(map(tuple,N[bkey]));cap=set(map(tuple,N['finite_XOR_cap']));w=WORDS[word];p=start;h=h0;F=set(cap);hist=defaultdict(list)
 for t,c in enumerate(w*3):
  bit=((p[0]-p[1],p[0]%2) in bulk)^(p in F);assert ('L'if bit else'R')==c
  if t<len(w):x,y=p;hist[(x-y,x%stride)].append((t-len(w)*((x-x%stride)//stride),c))
  F.symmetric_difference_update((p,));h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 assert p==(start[0]+3*stride,start[1]+3*stride)and h==h0
 for es in hist.values():es.sort();assert all(a[1]!=b[1]for a,b in zip(es,es[1:]))
 B={(t,a)for t,b in bulk for a in range(b,stride,2)};need={r for r,es in hist.items()if es[0][1]=='L'};assert need==B&hist.keys()
 O=B^{r for r,es in hist.items()if len(es)%2};U=B-hist.keys()
 def selected(r):
  t,a=r;q=(a-start[0],a-t-start[1]);return mask(rot_point(q,(-h0)%4))
 return {'normal_form':nf,'normal_form_sha256':hashlib.sha256((G/nf).read_bytes()).hexdigest(),'full_bulk_black_classes':len(B),'full_output_black_classes':len(O),'untouched_black_classes':len(U),'selected_full_input':sum(map(selected,B)),'selected_full_output':sum(map(selected,O)),'selected_untouched':sum(map(selected,U)),'retained_finite_XOR_cap_count':len(cap),'literal_replay_periods':3,'final_full_XOR_count':len(F),'final_full_XOR_sha256':hashlib.sha256(json.dumps(sorted(F),separators=(',',':')).encode()).hexdigest()}

def main():
 graphs={n:graph(w)for n,w in WORDS.items()};complete=[prepared('prepared_wave_five_band_normal_form.json','P1564','full_black_orbit_profiles'),prepared('three_standard_band_wave_normal_form.json','Q4352','full_black_profiles')]
 interfaces=json.loads((OUT/'all_cut_wave_interfaces.json').read_text())
 for report in interfaces['reports']:
  f=report['witness'];s=State(frozenset(map(tuple,f['minimum_black'])),(0,0),0);a=WORDS[report['source']];b=WORDS[report['target']];i,j=report['witness_phases'];w=a[i:]+a[:i]+b[j:]+b[:j]
  for c in w:
   assert ('L'if s.p in s.black else'R')==c;s=forward(s)
  assert sorted(s.black)==list(map(tuple,f['final_black']))and list(s.p)==f['final_position']and s.h==0
 standard=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());s=State(frozenset(map(tuple,standard['seed'])),(0,0),standard['heading'])
 for _ in range(14):s=forward(s)
 r=(-s.h)%4;sp=rot_point(s.p,r);s=transform(s,r,(-sp[0],-sp[1]));w=WORDS['S104'][14:]+WORDS['S104'][:14];assert first_mismatch(s,w)is None
 original=s;counts=[]
 for n in range(4):
  counts.append(sum(mask(q)for q in s.black))
  for c in w:assert ('L'if s.p in s.black else'R')==c;s=forward(s)
 assert counts==list(range(counts[0],counts[0]+4))
 counter={'phase':14,'initial_black':sorted(original.black),'initial_position':original.p,'initial_heading':original.h,'exact_periodic_tail_certified':True,'complete_stock_counts_at_four_boundaries':counts,'drift':[-2,2],'meaning':'An actual finite-seed standard highway replenishes this proposed fuel by1 each period. Therefore it is not a phase-independent resource.'}
 out={'scope':__doc__,'graphs':graphs,'complete_prepared_fields':complete,'stock_mask':'x even and x+y=20 mod28, in common boundary-heading-N coordinates','canonical_phase_stock_deltas':[0,-3,-6],'all_six_canonical_cross_pairs_illegal':all(not r['canonical_cut_pair']['legal']for r in interfaces['reports']),'phase14_countercontrol':counter,'all_six_finite_mixed_witnesses_literally_replayed':True}
 (OUT/'wave_roots_and_stock_scope.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ('graphs','phase14_countercontrol')},indent=2))
if __name__=='__main__':main()
