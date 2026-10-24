#!/usr/bin/env python3
"""No search: test only the dictated34->50->66 translation of known widening branch."""
from pathlib import Path
import json,runpy,hashlib
G=Path('/workspace/shared/langton/nonlinear_global_budget_2026-10-23');O=Path(__file__).parent
E=runpy.run_path(str(G/'changed_endpoint_catalog.py'))
A=json.loads((G/'endpoint_catalog_results.json').read_text())['results'];B=json.loads((G/'changed_endpoint_catalog_results.json').read_text())['cap_results']
s=next(r for r in A if r['channel']==[34,1]);rows,cap,meta=E['normalized_endcap'](s);P=set(rows)
b=next(r for r in B if r['normalization']['source_channel']==[34,1]);r=next(r for r in b['results']if r['channel']==[50,0]);assert r['drift']==[2,2]
rr,F,p,h,tau,phi=E['incoming'](rows,cap,[50,0]);p,h,read=E['advance'](rr,F,p,h,r['entry']);assert[list(p),h]==r['pose'];assert E['certify'](rr,F,p,h,r['tail_word'])
rx={j:set(v)for j,v in rr.items()};pp=p;hh=h
for c in r['tail_word']:
 j,k=E['old_orbit'](pp);E['add_threshold'](rx,j,k);hh=(hh+(-1 if c=='L'else 1))%4;v=E['V'][hh];pp=pp[0]+v[0],pp[1]+v[1]
final={j for j,v in rx.items()if len(v)%2};assert len(final)==72
# Translation making34,1 into50,0 has delta(t)=16 and odd x parity.
# Applying precisely that same displacement again dictates66,1.
nextchannel=(66,1);readclasses={(t+66,(a+1)%2)for t,a in E['RORB']};hits=readclasses&final
initialP=E['E']['PORB'];oldhits=readclasses&initialP;assert hits and oldhits
report={'status':'EXACT OBSTRUCTION to this translated continuation only','source_channel':[34,1],'second_channel':[50,0],'dictated_next_channel':nextchannel,'settled_profile_counts':[24,48,72],'next_read_black_classes':sorted(hits),'already_original_black_classes':sorted(oldhits),'first_black_witness':sorted(oldhits)[0],'reason':'The next clean104 arrival crosses an entire original settled-black orbit ray; no finite cap or longitudinal shift repairs it. No new reaction was simulated.','scope':__doc__,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(O/'widening_branch_translation_closure.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
