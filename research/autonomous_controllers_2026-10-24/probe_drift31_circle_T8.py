import json,time
from collections import Counter
from partial_drift31_graph import graph
from certify_drift31_read_minimum import words,returns_to,depart
from probe_drift31_circle_middle_returns import budget
z=json.load(open('drift31_circle_middle_returns_discovery.json'));S=Counter();out=[];start=time.time()
for c in z['cases']:
 for s in c['survivors']:
  H=[(2,),(3,),(2,),(1,1,3,1),(2,2,0,2),c['circle_T5'],c['T6'],s['T7_history']];k,G=graph(H,list(range(8)));assert k=='open';rs,paths=returns_to(H,G,8);I=len(depart(H[5],0));J=H[7].count(1);ds=words(0,2*(I+J)+1,0,I,1,J,rs);cc=Counter();kept=[]
  for v8 in ds:
   HH=H+[v8]
   if not budget(HH):kind='g8_residue_budget'
   else:kind,w=graph(HH,list(range(9)))
   cc[kind]+=1
   if kind=='open':kept.append(v8)
  S.update(cc);out.append({'histories':H,'T8_counts':[I,J],'T8_domain_size':len(ds),'outcomes':dict(cc),'survivors':kept});print('mode',len(H[5]),''.join('NESW'[h]for h in H[6]),''.join('NESW'[h]for h in H[7]),'domain',len(ds),dict(cc),'open',[''.join('NESW'[h]for h in x)for x in kept],flush=True)
json.dump({'scope':'Discovery only exact local T8 completion','aggregate':dict(S),'cases':out},open('drift31_circle_T8_discovery.json','w'),indent=2);print('TOTAL',dict(S),'seconds',time.time()-start)
