#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict,Counter
import json,runpy,hashlib
ROOT=Path(__file__).parent;E=runpy.run_path(str(ROOT/'changed_endpoint_catalog.py'));D=json.loads((ROOT/'endpoint_return_closure_results.json').read_text());node=next(s for s in D['states']if s['state_sha256'].startswith('5110a44e'));J=json.loads((ROOT/'second_prepared_wave_probe.json').read_text());rows0={tuple(j):[0]for j in node['profiles']};cap={tuple(q)for q in node['cap']};rows,F,p,h,tau,phi=E['incoming'](rows0,cap,(20,1));p,h,Q=E['advance'](rows,F,p,h,J['wave_entry']);G=defaultdict(list);pp=p;hh=h;s=J['certificate']['drift'][0];word=J['word']
for i,ch in enumerate(word):
 x,y=pp;t=x-y;a=x%s;k=(x-a)//s;G[t,a].append((k,i,ch,(a,a-t)));hh=(hh+(-1 if ch=='L'else 1))%4;v=E['V'][hh];pp=(pp[0]+v[0],pp[1]+v[1])
B={j for j,r in rows.items()if len(r)%2 and -16<=j[0]<=40};assert len(B)==36;edge=set();spans=Counter()
for j,g in G.items():
 g.sort(key=lambda x:(-x[0],x[1]));lo=min(x[0]for x in g);hi=max(x[0]for x in g);spans[hi-lo]+=1;c=g[0][3];assert ((c[0]-c[1],c[0]%2)in B)==(g[0][2]=='L')
 for n in range(lo,hi):
  first=next(x for x in g if x[0]<=n);q=(c[0]+s*n,c[1]+s*n)
  if ((q[0]-q[1],q[0]%2)in B)!=(first[2]=='L'):edge.add(q)
# necessary/sufficient starting black count for N copies, from exactfirstvisitcolors
sup=[]
for N in range(1,12):
 count=0
 for g in G.values():
  lo=min(x[0]for x in g);hi=max(x[0]for x in g)
  for n in range(lo,hi+N):
   candidates=[x for x in g if n-N+1<=x[0]<=n]
   if candidates:count+=candidates[0][2]=='L'
 sup.append(count)
# Two periods literal check on simplified fullbulk+finitecap, proof is orbitargument.
pp=p;hh=h;ff=set(edge)
for i in range(2*len(word)):
 ch='L'if (((pp[0]-pp[1],pp[0]%2)in B)^(pp in ff))else'R';assert ch==word[i%len(word)];E['toggle'](ff,pp);hh=(hh+(-1 if ch=='L'else 1))%4;v=E['V'][hh];pp=(pp[0]+v[0],pp[1]+v[1])
report={'scope':'Exact three-full-standard-band prepared normal form, not finite-original reachability.','source_node':node['state_sha256'],'pose':[list(p),h],'period':len(word),'drift':[s,s],'full_black_profiles':sorted(B),'finite_XOR_cap':sorted(edge),'cap_mass':len(edge),'additions':sum((q[0]-q[1],q[0]%2)not in B for q in edge),'erasures':sum((q[0]-q[1],q[0]%2)in B for q in edge),'read_class_spans':dict(spans),'input_black_classes':sum(g[0][2]=='L'for g in G.values()),'output_black_classes':sum(g[-1][2]=='R'for g in G.values()),'odd_write_classes':sum(len(g)%2 for g in G.values()),'net_black_change_per_period':word.count('R')-word.count('L'),'minimum_initial_mass_N1_through11':sup,'K_per_period':J['K_per_period'],'word_sha256':J['word_sha256'],'word_primitive':all(word!=word[:m]*(len(word)//m)for m in range(1,len(word))if len(word)%m==0)}
(ROOT/'three_standard_band_wave_normal_form.json').write_text(json.dumps(report,indent=2)+'\n');(ROOT/'second_prepared_wave_input.json').write_text(json.dumps({k:node[k]for k in ['profiles','cap','state_sha256','profile_count','cap_mass','cap_t_hull']},indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if k not in ['full_black_profiles','finite_XOR_cap']},indent=2))
