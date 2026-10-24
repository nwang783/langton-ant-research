#!/usr/bin/env python3
from pathlib import Path
import runpy,json,time,hashlib
ROOT=Path(__file__).parent;C=runpy.run_path(str(ROOT/'certify_prepared_travelling_wave.py'));E=C['E'];data=json.loads((ROOT/'endpoint_return_closure_results.json').read_text());node=next(s for s in data['states']if s['state_sha256'].startswith('5110a44e'));rows0={tuple(j):[0]for j in node['profiles']};cap={tuple(q)for q in node['cap']};rows,F,p,h,tau,phi=E['incoming'](rows0,cap,(20,1));V=E['V'];color=E['initial_color'];toggle=E['toggle'];out=[];start=time.time()
for i in range(300000):
 ch='L'if color(p,rows,F)else'R';out.append(ch);toggle(F,p);h=(h+(-1 if ch=='L'else 1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
word=''.join(out);tail=word[-100000:];pi=[0]*len(tail)
for i in range(1,len(tail)):
 j=pi[i-1]
 while j and tail[i]!=tail[j]:j=pi[j-1]
 if tail[i]==tail[j]:j+=1
 pi[i]=j
period=len(tail)-pi[-1];report={'scope':'Second exact prepared72-profile endpoint only, no finite seed itinerary.','node':node['state_sha256'],'channel':[20,1],'sampled_prefix':300000,'suffix_period':period}
if period<20000:
 j=len(word)-1
 while j>=period and word[j]==word[j-period]:j-=1
 begin=j-period+1;report['wave_entry']=begin
 rows,F,p,h,tau,phi=E['incoming'](rows0,cap,(20,1));p,h,Q=E['advance'](rows,F,p,h,begin);w=word[begin:begin+period];report['word']=w;report['pose']=[list(p),h]
 try:cert=C['cert_parallel'](rows,F,p,h,w)
 except AssertionError:cert=None
 report['certificate']=cert
 if cert:
  bad=[''.join(w[(i-9+j)%len(w)]for j in range(10))not in E['FACTORS']for i in range(len(w))];report['K_per_period']=sum(bad[i]and bad[(i-1)%len(w)]for i in range(len(w)));report['bad10_per_period']=sum(bad);report['word_sha256']=hashlib.sha256(w.encode()).hexdigest()
report['elapsed_seconds']=time.time()-start;(ROOT/'second_prepared_wave_probe.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if k!='word'},indent=2))
