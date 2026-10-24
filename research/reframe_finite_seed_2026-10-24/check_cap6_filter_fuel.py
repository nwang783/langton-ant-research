"""Exact cap-six certificate replay; no optimization or floating-point library.
Uses compact kernel paths; author certificate checker, not independent audit.
"""
from active_flight import *
from filter_cap6_physical_returns import lift
from pathlib import Path
from collections import Counter
import json,hashlib
OUT=Path(__file__).parent
OPEN={'RRRRLRL','RRRRLRLL','RRRRLRRLL','RRRRLRLRL','RRRRLRRLRL'}
def weight(D):
 D=set(map(tuple,D))
 if len(D)==1:return 1
 if len(D)!=2:return 0
 aa,bb=[set(ends(q,1))for q in D];mid=aa&bb;assert len(mid)==1
 v=next(iter(mid));u=next(iter(aa-{v}));w=next(iter(bb-{v}))
 return 2 if(u[0]+w[0],u[1]+w[1])==(2*v[0],2*v[1])else 1

def field_weight(B):
 todo=set(B);s=0
 while todo:
  q=next(iter(todo));D=comp(B,1,ends(q,1)[0]);s+=weight(D);todo-=D
 return s

def trap(B,p,h):
 w=cursor(p,h);d=rot((-2,2),h);u=(w[0]+d[0],w[1]+d[1]);U=set()
 for i in range(4):
  d=rot((-2,2),(h+i)%4);U|=comp(B,1,(w[0]+d[0],w[1]+d[1]))
 return len(U)>=3 or len(U)==2 and u not in vertices(U,1)

if __name__=='__main__':
 K=json.loads((OUT/'component_kernel_M6.json').read_text());T=K['transitions'];J=json.loads((OUT/'kernel_M6_compact_returns.json').read_text());R=J['returns'];n=K['summary']['active_states'];order=J['nonempty_topological_order'];assert sorted(order)==list(range(1,n));pos={v:i for i,v in enumerate(order)}
 assert all(not t['source']or not t['target']or pos[t['source']]<pos[t['target']]for t in T)
 # Independent in-script enumeration of every first return, with exact path binding.
 adj=[[]for _ in range(n)]
 for i,t in enumerate(T):adj[t['source']].append(i)
 reaches=[False]*n
 for u in reversed(order):reaches[u]=any(T[z]['target']==0 or reaches[T[z]['target']]for z in adj[u])
 paths=[]
 def walk(u,path):
  for z in adj[u]:
   v=T[z]['target']
   if not v:paths.append(path+[z])
   elif reaches[v]:walk(v,path+[z])
 walk(0,[]);paths.sort(key=lambda a:(len(a),a));assert paths==[r['indices']for r in R]
 assert all(r['word']==''.join(T[z]['turn']for z in r['indices'])for r in R)
 physical=[];survive=[];zero=[];drops=[];byword=Counter()
 for i,r in enumerate(R):
  if r['word']not in OPEN:continue
  rr={**r,'transitions':[T[z]for z in r['indices']]};seed=lift(rr);byword[r['word']]+=1
  if seed is None:continue
  physical.append(i);B=set(seed);p=(0,0);h=0
  for c in r['word']:p,h=step(B,p,h)
  if trap(B,p,h):continue
  survive.append(i);drop=sum(weight(t['imported_component'])-weight(t['emitted_component'])for t in rr['transitions']);assert drop>=0
  assert drop==field_weight(seed)-field_weight(B)
  drops.append({'index':i,'drop':drop})
  if not drop:zero.append(i)
 assert len(R)==43527 and len(physical)==4657 and len(survive)==93
 assert zero==[78,4554,4555,4866,4895,5169,33389]
 assert physical==json.loads((OUT/'cap6_physical_return_filter.json').read_text())['feasible_indices']
 assert survive==json.loads((OUT/'cap6_profile_budget_filter.json').read_text())['surviving_indices']
 report={'status':'EXACT_AUTHOR_CERTIFICATE_CHECKED_PENDING_INDEPENDENT_AUDIT','kernel_states':n,'kernel_edges':len(T),'first_returns':len(R),'word_counts':dict(Counter(r['word']for r in R)),'after_word_trap_filter':sum(byword.values()),'physically_realizable':len(physical),'after_profile_budget_filter':len(survive),'zero_drop_indices':zero,'strict_drop_profiles':sum(x['drop']>0 for x in drops),'drops':drops,'scope':'Necessary reduction for sustained cap-six tails, not yet termination or cross-profile composability.'}
 (OUT/'cap6_filter_fuel_certificate.json').write_text(json.dumps(report,indent=2)+'\n');print({k:v for k,v in report.items()if k not in('word_counts','drops')})
