#!/usr/bin/env python3
from pathlib import Path
import runpy,json,time
ROOT=Path(__file__).parent;E=runpy.run_path(str(ROOT/'changed_endpoint_catalog.py'));data=json.loads((ROOT/'endpoint_return_closure_results.json').read_text());node=next(s for s in data['states']if s['state_sha256'].startswith('425bd79f'));rows={tuple(j):[0]for j in node['profiles']};cap={tuple(q)for q in node['cap']};rows,F,p,h,tau,phi=E['incoming'](rows,cap,(12,1));V=E['V'];color=E['initial_color'];toggle=E['toggle'];out=[];samples=[];start=time.time()
for i in range(300000):
 if i%10000==0:samples.append([i,list(p),h,len(F)])
 ch='L'if color(p,rows,F)else'R';out.append(ch);toggle(F,p);h=(h+(-1 if ch=='L'else 1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
word=''.join(out);tail=word[-100000:];pi=[0]*len(tail)
for i in range(1,len(tail)):
 j=pi[i-1]
 while j and tail[i]!=tail[j]:j=pi[j-1]
 if tail[i]==tail[j]:j+=1
 pi[i]=j
period=len(tail)-pi[-1];last=word[-period:];print('PERIOD',period,'tail repeat whole',tail==''.join(tail[i%period]for i in range(len(tail))),flush=True)
report={'scope':'Prepared72-profile exact field only; no finite seed itinerary claimed.','node':node['state_sha256'],'channel':[12,1],'prefix':300000,'samples':samples,'terminal_pose':[list(p),h],'suffix_period':period,'period_word':last,'elapsed':time.time()-start}
if period<20000:
 pp=p;hh=h
 for ch in last:
  hh=(hh+(-1 if ch=='L'else 1))%4;v=V[hh];pp=(pp[0]+v[0],pp[1]+v[1])
 report['word_displacement']=[pp[0]-p[0],pp[1]-p[1]];report['heading_return']=hh==h;report['standard_checker']=E['certify'](rows,F,p,h,last)
 # Find start of exact word periodicity by comparing backward.
 j=len(word)-1
 while j>=period and word[j]==word[j-period]:j-=1
 report['periodic_suffix_start']=j-period+1
(ROOT/'prepared_nonstandard_tail_probe.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2),flush=True)
