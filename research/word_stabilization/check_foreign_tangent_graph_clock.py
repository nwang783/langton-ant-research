"""Exact finite GRAPH-ONLY cycle-sign certificate, no physical prefix search."""
from pathlib import Path
from collections import deque,defaultdict,Counter
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
def potential(n,es,cost):
 d=[0]*n
 for round in range(n):
  changed=False
  for u,v,w,t,i in es:
   c=cost(w,t)
   if d[v]>d[u]+c:d[v]=d[u]+c;changed=True
  if not changed:return d
 raise AssertionError('negative directed cycle')
def scc(n,es):
 a=[[]for _ in range(n)];b=[[]for _ in range(n)]
 for u,v,*_ in es:a[u].append(v);b[v].append(u)
 order=[];seen=set()
 def go(u):
  seen.add(u)
  for v in a[u]:
   if v not in seen:go(v)
  order.append(u)
 for u in range(n):
  if u not in seen:go(u)
 cs=[];cl=[-1]*n
 def back(u,k):
  cl[u]=k;cs[k].append(u)
  for v in b[u]:
   if cl[v]<0:back(v,k)
 for u in reversed(order):
  if cl[u]<0:cs.append([]);back(u,len(cs)-1)
 return cl,cs

def main():
 g=json.loads(SRC.read_text());E=g['quotient_edges'];n=2*g['classes'];es=[]
 for i,(u,a,v)in enumerate(E):
  for b in(0,1):
   w=int(a==1)+2*int(a>=4)-4*b*int(a>=4)
   es.append((2*u+b,2*v+int(a==1),w,int(a>=4),i))
 d=potential(n,es,lambda w,t:w)
 assert all(w+d[u]-d[v]>=0 for u,v,w,t,i in es)
 tight=[e for e in es if e[2]+d[e[0]]-d[e[1]]==0]
 cl,cs=scc(n,tight)
 assert all(not t or cl[u]!=cl[v]for u,v,w,t,i in tight)
 rate=potential(n,es,lambda w,t:n*w-t)
 assert all(n*w-t+rate[u]-rate[v]>=0 for u,v,w,t,i in es)
 # A concrete positive GRAPH walk, repeated for restored actual heading.
 ids=[21,232,866]*2;q=9;b=0;h=0;states=[[q,b,h]];W=T=0;word=[]
 for i in ids:
  u,a,v=E[i];assert q==u
  w=int(a==1)+2*int(a>=4)-4*b*int(a>=4)
  W+=w;T+=int(a>=4);word.append(a);b=int(a==1);q=v
  h=(h+(3 if a==1 else 2 if a>=4 else 0))%4;states.append([q,b,h])
 assert states[0]==states[-1] and W==4 and T==2
 out={'status':'AUTHOR_GRAPH_ONLY_NO_NEGATIVE_OR_FOREIGN_ZERO_CYCLE_PENDING_INDEPENDENT_REPLAY',
      'source_graph_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
      'states':n,'lifted_edges':es,'clock_potential':d,'clock_potential_histogram':dict(Counter(d)),
      'zero_reduced_edge_count':len(tight),'zero_reduced_SCC_class':cl,'zero_reduced_SCC_sizes':sorted(map(len,cs),reverse=True),
      'foreign_zero_cyclic_edges':0,'foreign_rate_multiplier':n,'foreign_rate_potential':rate,
      'foreign_rate_potential_oscillation':max(rate)-min(rate),
      'path_inequality':f'T_foreign <= {n} W + rate_potential(start)-rate_potential(end)',
      'restored_heading_positive_graph_cycle':{'original_edge_ids':ids,'label_word':word,'states_q_prevC_heading':states,'clock':W,'foreign_count':T},
      'scope':'Exact inherited214-state quotient only; no assertion of physical realization, global graph coverage or simple foreign-piece path.'}
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k]for k in['states','clock_potential_histogram','zero_reduced_edge_count','foreign_zero_cyclic_edges','foreign_rate_potential_oscillation']}))
if __name__=='__main__':main()
