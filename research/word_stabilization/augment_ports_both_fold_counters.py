"""Add the proved at-most-two-U-separated-folds rule to the H-port DFA."""
import json,collections
base='/workspace/shared/langton/word_stabilization/'
d=json.load(open(base+'minimized_actual_ports.json'));alpha=d['alphabet'];old={(a,k):b for a,k,b in d['transitions']}
starts={(s,0,0) for s in d['states']};states=set(starts);queue=collections.deque(starts);T={}
while queue:
 s,c,e=queue.popleft()
 for k in alpha:
  t=old.get((s,k))
  if t is None:continue
  nc=0 if k in 'CV' else (c+1 if k in 'BQ' else c)
  ne=0 if k in 'CU' else (e+1 if k in 'BQ' else e)
  if nc>2 or ne>2:continue
  dest=(t,nc,ne);T[(s,c,e),k]=dest
  if dest not in states:states.add(dest);queue.append(dest)
states=sorted(states);cl={s:0 for s in states};rounds=[]
while True:
 sigs={};nc={}
 for s in states:
  sig=tuple(cl.get(T.get((s,k)),-1) for k in alpha)
  if sig not in sigs:sigs[sig]=len(sigs)
  nc[s]=sigs[sig]
 rounds.append(len(sigs))
 if all(nc[s]==cl[s] for s in states):break
 cl=nc
trans={(cl[s],k):cl[t] for (s,k),t in T.items()}
ports=[]
for word,oldclass in d['port_classes']:
 for s in states:
  if s[0]==oldclass:ports.append([word,cl[s]])
ports=sorted(set((w,c) for w,c in ports))
result={'alphabet':alpha,'states':sorted(set(cl.values())),'transitions':[[a,k,b] for (a,k),b in sorted(trans.items())],'source_contexts':{k:sorted({cl[t] for (s,j),t in T.items() if j==k}) for k in alpha},'port_classes':ports,'product_states':len(states),'rounds':rounds,'proof':['triple_u_fold_lemma.md','triple_v_fold_lemma.md'],'product_class_mapping':[[*s,cl[s]] for s in states]}
json.dump(result,open(base+'minimized_ports_both_fold_counters.json','w'),indent=2)
print('PRODUCT',len(states),'MINIMIZED',len(result['states']),'EDGES',len(trans),'ROUNDS',rounds)
