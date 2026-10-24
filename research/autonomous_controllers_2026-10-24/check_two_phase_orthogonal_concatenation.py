#!/usr/bin/env python3
"""Exact bounded two-standard-block translating-controller candidate family."""
import json,hashlib,time
from pathlib import Path
from collections import Counter,defaultdict
from check_extremal_read_coupling import ROOT,event_word,quotient

def check(word):
 ev,d,h=event_word(word);assert h==0 and d!=(0,0)
 H=defaultdict(list);P=len(ev)
 for e in ev:
  r,k=quotient(e['p'],d);H[r].append((e['t']-k*P,e['t'],k,e['c']))
 for r,g in H.items():g.sort()
 for r,g in H.items():
  for a,b in zip(g,g[1:]):
   if a[3]==b[3]:return 'nonalternating_complete_class',{'cell':r,'consecutive_stable_reads':[a,b]},d
 for r,g in H.items():
  if g[0][3]!='R':return 'BLACK_first_complete_class',{'cell':r,'first_stable_read':g[0]},d
 return 'complete_WHITE',{'classes':len(H)},d

def main():
 W=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];assert len(W)==104
 rotations=[W[i:]+W[:i]for i in range(len(W))];assert len(set(rotations))==104
 for F in rotations:
  for copies in (1,2):assert check(F*copies)[0]=='complete_WHITE'
 stats=Counter();drifts=Counter();reject=[];surv=[];start=time.time()
 for connector in ('RL','LR'):
  for a,F in enumerate(rotations):
   for b,G in enumerate(rotations):
    word=F+connector[0]+G+connector[1];kind,wit,d=check(word);assert len(word)==210 and word.count('R')-word.count('L')==24 and all(abs(x)%2==1 for x in d)
    stats[kind]+=1;drifts[d]+=1
    if kind=='complete_WHITE':surv.append({'connector':connector,'phases':[a,b],'word':word,'drift':d,'witness':wit})
    else:reject.append({'connector':connector,'phases':[a,b],'drift':d,'reason':kind,'witness':wit})
 result={'scope':__doc__,'standard_word_sha256':hashlib.sha256(W.encode()).hexdigest(),'candidate_count':sum(stats.values()),'positive_standard_controls':208,'period':210,'formal_turn_growth':24,'outcomes':dict(stats),'drift_distribution':{str(k):v for k,v in sorted(drifts.items())},'survivors':surv,'seconds':time.time()-start,'limitations':'Only the exact two104-block family with one R and one L connector is covered. No longer connector, arbitrary standard-piece length, prepared input, or global controller exclusion.'}
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');Path(__file__).with_name('two_phase_orthogonal_rejection_certificate.json').write_text(json.dumps(reject,separators=(',',':'))+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
