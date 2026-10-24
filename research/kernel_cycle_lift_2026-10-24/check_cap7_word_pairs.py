"""Exact529 turn-word pair existence tests, NOT fixed-profile composition.
All initial bits are shared. Extra initial black cells are unread by the whole
word and cannot reduce an active component or repair a nonempty seam.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import sys,json,hashlib
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'reframe_finite_seed_2026-10-24'))
from active_flight import DIR,cursor,ends,vertices,comp,step
SRC=OUT/'cap7_word_budget_filters_certificate.json';SOURCE=json.loads(SRC.read_text());WORDS=SOURCE['remaining_words'];assert len(WORDS)==23

def sequence(words):
 W=''.join(words);seams=[0];s=0
 for x in words:s+=len(x);seams.append(s)
 last={};seed=set();p=(0,0);h=0;poses=[]
 for t,c in enumerate(W):
  poses.append((p,h))
  if p in last and last[p][1]==c:return dict(status='NO_WORD_COLOR',words=words,cell=p,earlier=last[p],next=[t,c])
  if p not in last and c=='L':seed.add(p)
  last[p]=(t,c);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1])
 B=set(seed);p=(0,0);h=0;birth={q:None for q in B};events=[];trace=[];maxC=0
 for t in range(len(W)+1):
  C=comp(B,1,cursor(p,h));maxC=max(maxC,len(C));trace.append(dict(cut=t,pose=[p,h],full_black=sorted(B),active_w=sorted(C)))
  if len(C)>7:return dict(status='NO_CAP7',words=words,initial_black=sorted(seed),cut=t,mandatory_component=sorted(C))
  if t in seams and C:return dict(status='NO_EMPTY_SEAM',words=words,initial_black=sorted(seed),cut=t,mandatory_component=sorted(C))
  if t not in seams:assert C,'Individual local minimum first-return witnesses rule out this lower-bound failure'
  if t==len(W):break
  c=W[t];assert c==('L'if p in B else'R');q=p;m=next(i for i in range(len(words))if seams[i]<=t<seams[i+1])
  if c=='R':
   w=cursor(p,h);u,v=ends(q,1);o=v if u==w else u;D=comp(B,1,o)if o not in vertices(C,1)|{w}else set()
   if D:events.append(dict(kind='import',update=t,macro=m,component=sorted(D),births=[dict(cell=e,birth=birth[e],birth_macro=None if birth[e]is None else next(i for i in range(len(words))if seams[i]<=birth[e]<seams[i+1]))for e in sorted(D)]))
   birth[q]=t
  else:
   events.append(dict(kind='consume',update=t,macro=m,cell=q,birth=birth[q]));birth.pop(q)
  p,h=step(B,p,h)
 r=cursor(p,h);U=set()
 for dx,dy in product((-2,2),repeat=2):U|=comp(B,1,(r[0]+dx,r[1]+dy))
 a,b=ends(p,1);u=b if a==r else a
 trap=len(U)>3 or(len(U)==3 and u not in vertices(U,1))
 return dict(status='ACTUAL_WORD_SEQUENCE',words=words,initial_black=sorted(seed),initial_mass=len(seed),word=W,seams=seams,maximum_complete_active_mass=maxC,final_pose=[p,h],final_black=sorted(B),events=events,trace=trace,future_budget_trap=dict(trapped=trap,mandatory_imported_edges=sorted(U),mass=len(U),first_tip_incident=u in vertices(U,1)))

single=[sequence([w])for w in WORDS];assert all(a['status']=='ACTUAL_WORD_SEQUENCE'for a in single)
pairs=[sequence([a,b])for a,b in product(WORDS,repeat=2)]
E=[(WORDS.index(a['words'][0]),WORDS.index(a['words'][1]))for a in pairs if a['status']=='ACTUAL_WORD_SEQUENCE']
T=[(WORDS.index(a['words'][0]),WORDS.index(a['words'][1]))for a in pairs if a['status']=='ACTUAL_WORD_SEQUENCE'and not a['future_budget_trap']['trapped']]
def scc(edges):
 n=len(WORDS);adj={v:[]for v in range(n)};rev={v:[]for v in range(n)}
 for a,b in edges:adj[a].append(b);rev[b].append(a)
 order=[];seen=set()
 def dfs(v):
  seen.add(v)
  for u in adj[v]:
   if u not in seen:dfs(u)
  order.append(v)
 for v in range(n):
  if v not in seen:dfs(v)
 seen=set();cc=[]
 def collect(v,Q):
  seen.add(v);Q.append(v)
  for u in rev[v]:
   if u not in seen:collect(u,Q)
 for v in reversed(order):
  if v not in seen:
   Q=[];collect(v,Q)
   if len(Q)>1 or(v,v)in edges:cc.append(sorted(Q))
 return cc
out=dict(status='AUTHOR exact cap7 word-pair existence graph and separate future-trap graph',source_sha256={str(SRC.relative_to(ROOT)):hashlib.sha256(SRC.read_bytes()).hexdigest()},words=WORDS,single_witnesses=single,all_529_pairs=pairs,existence_edges=E,future_untrapped_edges=T,existence_recurrent_sccs=scc(E),future_untrapped_recurrent_sccs=scc(T),scope='Every positive edge is one actual complete finite seed with both first returns and cap7, not an imposed profile. Negatives exclude arbitrary unread extras by monotonicity. Future-trap removal is a separate sustained-tail necessity, not a failed finite pair. A compatible graph cycle is NOT automatically physically composable indefinitely.')
(OUT/'cap7_word_pairs_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'counts':dict(Counter(a['status']for a in pairs)),'existence_edges':len(E),'future_untrapped_edges':len(T),'existence_sccs':[[WORDS[i]for i in Q]for Q in out['existence_recurrent_sccs']],'tail_sccs':[[WORDS[i]for i in Q]for Q in out['future_untrapped_recurrent_sccs']]},indent=2))
