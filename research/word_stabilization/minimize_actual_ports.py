import json,collections
from verify_macro_word import D
base='/workspace/shared/langton/continuation_2026-10-22/ant_continuation/factor_language/'
d=json.load(open(base+'five_macro_actual_ports.json'));M=d['marker'];labels={v['word'][len(M):]+M:k for k,v in D.items()}
def feasible(w):
 x=y=h=0;last={};dirs=((0,1),(1,0),(0,-1),(-1,0))
 for c in w:
  if last.get((x,y))==c:return False
  last[x,y]=c;h=(h+(1 if c=='R' else -1))%4;dx,dy=dirs[h];x+=dx;y+=dy
 return True
edges=[];bad=0
for a,b,w in d['edges']:
 assert (a+w)[-len(b):]==b
 if feasible(a+w):edges.append((a,b,labels[w]))
 else:bad+=1
states=sorted({v for a,b,k in edges for v in (a,b)});T={(a,k):b for a,b,k in edges};assert len(T)==len(edges)
ALPHA='CUVQB';cl={s:0 for s in states};rounds=[]
while True:
 sigs={};nc={}
 for s in states:
  sig=tuple(cl.get(T.get((s,k)),-1) for k in ALPHA)
  if sig not in sigs:sigs[sig]=len(sigs)
  nc[s]=sigs[sig]
 rounds.append(len(sigs))
 if all(nc[s]==cl[s] for s in states):break
 cl=nc
trans={(cl[s],k):cl[to] for (s,k),to in T.items()};classes=sorted(set(cl.values()))
print('PORTS',len(states),'EDGES',len(edges),'BAD',bad,'CLASSES',len(classes),'ROUNDS',rounds)
result={'alphabet':ALPHA,'states':classes,'transitions':[[c,k,to] for (c,k),to in sorted(trans.items())],'source_contexts':{k:sorted({cl[b] for a,b,j in edges if j==k}) for k in ALPHA},'class_sizes':dict(collections.Counter(cl.values())),'original_states':len(states),'original_edges':len(edges),'discarded_edges':bad,'rounds':rounds,'port_classes':[[s,cl[s]] for s in states]}
json.dump(result,open('/workspace/shared/langton/word_stabilization/minimized_actual_ports.json','w'),indent=2)
