"""Literal role offsets and source-entry C clock for the analytic simple-path bound."""
from pathlib import Path
from collections import Counter
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();B=ROOT/'core_periodicity_new/simple_center_C_lifetime_frozen_20261023_1719';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
K={p for p,b in walk(mark)[2].items()if b};G={}
ids=(0,1,4,5,6,7,8,9);cs={0:0,1:1,4:0,5:1,6:2,7:0,8:1,9:2}
for s in ids:
 e,h,_,flip=walk(raws[s]);before={p for p,b in walk(raws[s]+mark)[2].items()if b};G[s]=(before-K,(before^flip)-{e+rotation(q,h)for q in K});assert h==(-cs[s])%4
assert sum(len(v[0])for v in G.values())==23 and sum(len(v[1])for v in G.values())==68
c=-.5-.5j;rows=[];hist=Counter();raw=0
for s in ids:
 for o in G[s][1]:
  for t in ids:
   for i in G[t][0]:
    for h in range(4):
     raw+=1;p=o-rotation(i,h)
     if (sum(xy(p))+h)%2:continue
     d=p+rotation(c,h)-c;dx,dy=map(abs,xy(d));N=(dx+11)*(dy+11)
     rows.append((s,xy(o),t,xy(i),h,xy(p),xy(d),N));hist[N]+=1
assert raw==6256 and len(rows)==3128 and max(hist)==289
assert (9,(-2,6),7,(-1,4),1,(-6,5),(-6,6),289)in rows
expected=json.loads((B/'02_simple_center_C_lifetime_bound.json').read_text())['all_sector_compatible_role_alignments']
assert set(rows)=={(r['source'],tuple(r['output']),r['target'],tuple(r['input']),r['relative_heading'],tuple(r['consumer_head']),tuple(r['center_delta']),r['rectangle_sites'])for r in expected}
assert all(r['necessary_age_residue_mod4']==(-r['relative_heading'])%4 and r['source_C_tails']==cs[r['source']]for r in expected)
# Full-entry-to-entry includes source C tails and excludes target C tails.
# Corrected atom steps use precisely the same center correction.
steps={}
for s in (0,4,7):
 e,h,*_=walk(raws[s]);steps[s]=xy(e+rotation(c,h)-c)
e0=walk(raws[0])[0];e1,h1,*_=walk(raws[1]);steps['C']=xy(e1+rotation(c,h1)-(e0+c))
assert steps=={0:(1,1),4:(1,3),7:(0,4),'C':(1,1)}
out=dict(status='PASS independent literal lifetime-role reconstruction and analytic clock interface',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),raw_alignments=raw,sector_valid=len(rows),rectangle_maximum=max(hist),C_age_bound=8*max(hist)+11,maximum_rows=[r for r in rows if r[-1]==max(hist)],rectangle_histogram=dict(sorted(hist.items())),scope='Finite injective corrected-center subarc. Sources and consumers are full-packet entries inside the same simple complete-eight factor; full-source C tails included. Entry roots and later history outside that factor exempt. No bound on archive number, total C, U, or duration.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
