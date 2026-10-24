"""Exact inverse104 completion at cuts of ONE supplied inverse prefix.
All additional initial changes must miss the whole forward4352 READ set,
the prescribed17511-read return prefix, and every already executed inverse
read. No prefix branching or enlargement is performed.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
from probe4352_repaired_launch_past import build
from probe4352_return_end_limit import trace,V,A
import inverse4352_tail_completion as T
P=Path(__file__).resolve().parent
J=json.loads((P/'prepared4352_memory_patch_past_certificate.json').read_text())
goal=json.loads((P/'prepared4352_launch_memory_patch.json').read_text())
protected={q for _,q,hh,c in list(trace((A['word']*2)[:goal['prescribed_legal_prefix_length']],(117,111),0))[:-1]}
b=build()
for q in J['patch']:b.toggle(tuple(q))
seen=set();p=(-1,3);h=1;records=[];found=None
def complete(word):
 groups=defaultdict(list)
 for i,q,hh,c in list(trace(word,p,h))[:-1]:groups[q[0]-q[1],q[0]%2].append((i-104*(q[0]//2),q[0]//2,c))
 extra=set()
 for(t,a),rows in sorted(groups.items()):
  rows.sort();assert all(x[2]!=y[2]for x,y in zip(rows,rows[1:]))
  lo=min(v[1]for v in rows);end=max(v[1]for v in rows)
  for (tt,aa),cuts in b.rays.items():
   if tt==t and aa%2==a and cuts:end=max(end,(aa+78*max(cuts)-a)//2)
  for x,y in b.F:
   if x-y==t and x%2==a:end=max(end,x//2)
  for n in range(lo,end+40):
   q=(a+2*n,a+2*n-t);wanted=next(v[2]=='L'for v in rows if v[1]<=n)
   if b.color(q)==wanted:continue
   reason='infinite stable mismatch'if n>end else'earlier inverse read'if q in seen else'forward wave read'if T.future_read(q)else'protected return read'if q in protected else None
   if reason:return None,{'cell':q,'reason':reason,'wanted':wanted,'current':bool(b.color(q))}
   extra.add(q)
 return extra,None
for cut in range(len(J['prefix'])+1):
 for phase,word,_,_ in T.TARGETS.get((p[0]-p[1],p[0]%2,h),()):
  extra,bad=complete(word);record={'cut':cut,'pose':[p,h],'phase':phase,'rejection':bad};records.append(record)
  if extra is not None:
   found={'cut':cut,'pose':[p,h],'phase':phase,'inverse_prefix':J['prefix'][:cut],'inverse_tail_word':word,'additional_entry_XOR':sorted(extra),'protected_return_prefix_length':goal['prescribed_legal_prefix_length']};break
 if found is not None:break
 if cut<len(J['prefix']):
  c=J['prefix'][cut];assert b.color(p)==(c=='L');seen.add(p);b.toggle(p);h=(h+(1 if c=='R'else-1))%4;p=p[0]+V[h][0],p[1]+V[h][1]
out={'scope':__doc__,'status':'COMPATIBLE SUPPLIED CUT'if found else'NO COMPLETION ON THIS SUPPLIED PREFIX','found':found,'tested_candidates':len(records),'rejection_reasons':dict(Counter(r['rejection']['reason']for r in records if r['rejection'])),'records':records,'protected_return_cells':len(protected),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared4352_memory_patch_tail_completion.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='records'})
