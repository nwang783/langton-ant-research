"""Freeze the supplied12-turn inverse tail and all-orbit negative controls.
Its full initial field is the signed launch output with the unique15-cell
launch-only return-memory patch, not a finite fresh cap.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib
from probe4352_repaired_launch_past import build
from probe4352_return_end_limit import first_bad,trace,V
P=Path(__file__).resolve().parent
J=json.loads((P/'prepared4352_memory_patch_past_tail.json').read_text())
b=build()
for q in J['patch']:b.toggle(tuple(q))
initial=b.manifest();p=(-1,3);h=1
for i,c in enumerate(J['prefix']):
 assert b.color(p)==(c=='L'),(i,p,h)
 b.toggle(p);h=(h+(1 if c=='R'else-1))%4;p=p[0]+V[h][0],p[1]+V[h][1]
assert len(J['prefix'])==2313 and(p,h)==((27,-2),0)
w='RLRRRRLLLLRL';assert J['word']==w
bad,d=first_bad(b,p,h,w);assert bad is None and d==(2,2)
g=defaultdict(list)
for i,q,hh,c in list(trace(w,p,h))[:-1]:g[q[0]-q[1],q[0]%2].append((i-12*(q[0]//2),q[0]//2,c))
records=[]
for (t,a),rows in sorted(g.items()):
 rows.sort();assert all(x[2]!=y[2]for x,y in zip(rows,rows[1:]))
 k=max(r[1]for r in rows)+1000000;q=(a+2*k,a+2*k-t)
 b.toggle(q);fail,dd=first_bad(b,p,h,w);assert fail is not None;b.toggle(q)
 records.append({'class':[t,a],'history':''.join(r[2]for r in rows),'initial_black':rows[0][2]=='L','final_black':(rows[0][2]=='L')^(len(rows)%2),'far_flip_first_mismatch':fail})
out={'scope':__doc__,'status':'EXACT_PREPARED_PERIOD12_PAST','prefix_length':len(J['prefix']),'prefix':J['prefix'],'pose':[p,h],'word':w,'drift':d,'initial_field':initial,'tail_entry_finite_xor':sorted(b.F),'patch':J['patch'],'class_records':records,'far_flip_rejections':len(records),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'patch_sha256':hashlib.sha256((P/'prepared4352_launch_memory_patch.json').read_bytes()).hexdigest()}
(P/'prepared4352_memory_patch_past_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items()if k not in('prefix','initial_field','tail_entry_finite_xor','patch')})
