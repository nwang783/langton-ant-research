#!/usr/bin/env python3
from collections import defaultdict,Counter
from pathlib import Path
import json,time
from probe_axis4_fast_zone import rows
from axis4_first_return_window import bad_window
cap=5;ss=rows(1,cap,4);ix=defaultdict(list)
for row in ss:ix[tuple(row[c]['ins'][0] if c%2==0 else row[c]['outs'][2] for c in range(4))].append(row)
profiles=[(m,)*4 for m in range(1,6)]+[(0,0,1,1),(2,2,3,3),(4,4,5,5),(1,2,2,1),(3,4,4,3)];out=[]
for ns in profiles:
 bottom=[tuple((3 if j%2==0 else 1) if c%2==0 else 2 for j in range(m)) for c,m in enumerate(ns)];good=[];reject=Counter()
 for row in ix[ns]:
  hs=[r['h'] for r in row];bad=bad_window([bottom,hs])
  if bad:reject[bad]+=1
  else:good.append(hs)
 item=dict(bottom=ns,raw_upper_rows=len(ix[ns]),passed_literal_window=len(good),rejected=dict(reject),examples=good[:6]);out.append(item);print(json.dumps(item),flush=True)
r=dict(cap=cap,scope='NECESSARY_COMPLETE_LOWER_TWO_ROW_WINDOW_NOT_FULL_FRONTS',cases=out);Path(__file__).with_name('axis4_bottom_cap5_first_return_catalog.json').write_text(json.dumps(r,indent=2)+'\n')
