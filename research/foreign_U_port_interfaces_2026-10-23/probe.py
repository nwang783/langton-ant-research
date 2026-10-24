from pathlib import Path
import json
from collections import Counter
P=Path('/workspace/shared/langton/word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json');J=json.loads(P.read_text());G=J['macro_words'];M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)};Z={(1,0),(1,1),(2,0),(2,1)};V=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def place(q,p,h):return add(p,rot(q,h))
def derive(w):
 p=(0,0);h=0;par=set();req={};reads={}
 for t,ch in enumerate(w):
  need=(ch=='L')^(p in par);assert p not in req or req[p]==need;req[p]=need;reads.setdefault(p,[]).append((t,ch));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,V[h])
 return req,par,p,h,reads
for held,name,target in((L,'L',L),(L|Z,'LZ',Z)):
 rows=[];cases={}
 for a in(4,5,6):
  w=G[a]['word'];req,_,_,_,reads=derive(w+M);I={q for q,b in req.items()if b}-K;white={q for q,b in req.items()if not b}
  for z in sorted(target):
   for q in sorted(I):
    for h in range(4):
     p=sub(z,rot(q,h));core={place(x,p,h)for x in K};W={place(x,p,h)for x in white};II={place(x,p,h)for x in I};ctx={place(x,p,h)for x in req};raw={place(x,p,h)for x,t in reads.items()if t[0][0]<len(w)}
     why='sector'if(sum(p)+h)%2 else'held_core'if held&core else'held_before_white'if held&W else'candidate'
     row=dict(a=a,pose=[*p,h],z=z,q=q,why=why)
     rows.append(row)
     if why=='candidate':
      key=(a,*p,h);tags=II&held;cases[key]=dict(a=a,name='DCVUFQB'[a],pose=[*p,h],targets=sorted(tags&target),held_inputs=sorted(tags),raw_first_L=sorted(tags&raw),marker_only_L=sorted(tags-raw),held_untouched_raw=sorted(held-raw),held_context_hits=sorted(held&ctx))
 print(name,len(rows),Counter(r['why']for r in rows),'unique',len(cases))
 print(Counter((c['name'],len(c['targets']),len(c['raw_first_L']),len(c['marker_only_L']))for c in cases.values()))
 Path('/workspace/shared/langton/foreign_U_port_interfaces_2026-10-23/'+name+'_probe.json').write_text(json.dumps(dict(rows=rows,cases=list(cases.values())),indent=2))
