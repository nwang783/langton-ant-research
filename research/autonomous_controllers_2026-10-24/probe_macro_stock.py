import json
from pathlib import Path
from collections import Counter
from check_extremal_read_coupling import ROOT,event_word
G=ROOT/'nonlinear_global_budget_2026-10-23'
ws={'S104':json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'],'P1564':json.loads((G/'prepared_travelling_wave_certificate.json').read_text())['word'],'Q4352':json.loads((G/'second_prepared_wave_certificate.json').read_text())['word']}
Ds={};deltas={}
for n,w in ws.items():
 ev,d,h=event_word(w,0);Ds[n]=d;delta=Counter()
 for e in ev:delta[(sum(e['p'])%28,e['p'][0]%2)]+=1 if e['c']=='R' else -1
 deltas[n]=delta
 print(n,d,'nonzero',sorted((k,v) for k,v in delta.items() if v))
A=deltas['S104'];B=deltas['P1564'];C=deltas['Q4352'];print('eligible',[(k,B[k],C[k]) for k in [(z,x)for z in range(28)for x in range(2)] if A[k]==0 and (B[k]<0 or C[k]<0)])
