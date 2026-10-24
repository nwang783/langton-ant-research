#!/usr/bin/env python3
"""Infer all-future finite XOR needed to join1564 from each matching B H phase."""
from pathlib import Path
from collections import defaultdict
from bisect import bisect_left
import json,runpy
ROOT=Path(__file__).parent;E=runpy.run_path(str(ROOT/'endpoint_catalog.py'));J=json.loads((ROOT/'prepared_travelling_wave_certificate.json').read_text());N=json.loads((ROOT/'prepared_wave_five_band_normal_form.json').read_text());BULK={tuple(j)for j in N['full_black_orbit_profiles']};FWD={j for j in E['PORB']if -28<=j[0]<=-18};LAST={(t+26,a)for t,a in FWD};OTHER=BULK-LAST;assert len(OTHER)==48;p0=tuple(J['wave_pose'][0]);h0=J['wave_pose'][1];trans=(0,-26);G=defaultdict(list);p=p0;h=h0
for i,ch in enumerate(J['word']):
 x,y=p;t=x-y;a=x%14;k=(x-a)//14;G[t,a].append((k,i,ch,(a,a-t)));h=(h+(-1 if ch=='L'else 1))%4;v=E['V'][h];p=(p[0]+v[0],p[1]+v[1])
for g in G.values():g.sort(key=lambda z:(-z[0],z[1]))
results=[]
for phase,q in enumerate(E['PH']):
 q=(q[0]+trans[0],q[1]+trans[1]);copy=E['along'](p0,q,E['d'])
 if copy is None or E['HD'][phase]!=h0:continue
 tau=104*copy+phase;rows=defaultdict(set);past_max={}
 for i,q in enumerate(E['PH']):
  q=(q[0]+trans[0],q[1]+trans[1]);j,k=E['old_orbit'](q);th=k+(tau-i-1)//104
  if th in rows[j]:rows[j].remove(th)
  else:rows[j].add(th)
  past_max[j]=max(past_max.get(j,-10**9),th)
 rows={j:sorted(r)for j,r in rows.items()if r}
 def color(q):return (E['old_orbit'](q)[0]in OTHER)^E['row_color'](q,rows)
 mismatch=set();black_erase=[];past=[];tested=0
 for j,g in G.items():
  mn=min(x[0]for x in g);mx=max(x[0]for x in g);c=g[0][3];oj,kc=E['old_orbit'](c);hi=mx+2
  for th in rows.get(oj,[]):hi=max(hi,(th-kc)//-7+3)
  for n in range(mn,hi+1):
   elig=[x for x in g if x[0]<=n]
   if not elig:continue
   q=(c[0]+14*n,c[1]+14*n);want=elig[0][2]=='L';tested+=1
   if color(q)!=want:mismatch.add(q)
  q=(c[0]+14*(hi+100),c[1]+14*(hi+100));assert color(q)==(g[0][2]=='L')
 for q in mismatch:
  if color(q):black_erase.append(q)
  j,k=E['old_orbit'](q)
  if j in past_max and k<=past_max[j]:past.append(q)
 results.append({'H_phase':phase,'H_copy':copy,'tau':tau,'mismatch_cells':sorted(mismatch),'mass':len(mismatch),'erasures':sorted(black_erase),'strict_past_overlap':sorted(past),'tested_required_cells':tested,'additions_only_and_fresh':not black_erase and not past})
out={'scope':'Exact causal-front join inference on four pre-existing full standard bands; full physical rail preparation still separate.','last_writer':'SW[-2,8]a0','wave_pose':[list(p0),h0],'phase_results':results};(ROOT/'wave_join_from_last_writer.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
