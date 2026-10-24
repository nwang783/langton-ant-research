#!/usr/bin/env python3
"""Discovery control for stronger fresh bands. Counts are scoped finite inventories."""
from check_position_k9_record_independent import trace,extend,words
from pathlib import Path
from collections import Counter
import json
out=[]
for k,a in ((9,3),(13,5),(17,7)):
 W=words(k);tr={w:trace(w)for w in W}
 oriented=[];top_non=-999;top_all=-999
 for hc in(1j,1,-1j,-1):
  for c in'RL':
   target=a*hc*(-1j if c=='R'else 1j)
   for hf in(hc,-hc):
    for w,(ev,p,h)in tr.items():
     rot=hf/1j
     if rot*p!=target:continue
     top=max((rot*q).imag for q,ch in ev);top_all=max(top_all,top)
     if target.imag!=a:top_non=max(top_non,top)
 # Earlier macro reads have y<=-gap in record-normalized coordinates.
 gap=int(min(a-top_non,2*a-top_all));data=[]
 for threshold in(0,1-gap):
  pairs=[]
  for hf in(1,-1):
   prev=[w for w,(ev,p,h)in tr.items()if hf/1j*p==a*1j]
   for u in prev:
    ev,p,h=trace(u,hf,-a*1j)
    for v,(vv,vp,vh)in tr.items():
     if h/1j*vp!=a:continue
     ev2,p2,h2=trace(v,h)
     d={};ok=True
     for q,c in ev+ev2:
      if q in d and d[q]==c:ok=False;break
      if q not in d and q.imag>=threshold and c=='L':ok=False;break
      d[q]=c
     if ok:pairs.append((u,v,int(h.real),int(h.imag),int(max(q.imag for q,c in ev))))
  data.append(dict(white_threshold=threshold,pairs=len(pairs),record_words=sorted(set(z[1]for z in pairs)),all_aligned=all(z[2:4]==(0,1)and z[4]<0 for z in pairs),pair_data=pairs))
 rec=dict(k=k,a=a,words=len(W),top_all=top_all,top_non_north=top_non,gap=gap,tests=data);out.append(rec)
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({key:value for key,value in rec.items()if key!='tests'}),[(x['white_threshold'],x['pairs'],len(x['record_words']),x['all_aligned'])for x in data],flush=True)
