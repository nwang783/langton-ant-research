import json
from pathlib import Path
from check_fresh_record_trap_bridge import geometry,multiple,verify_tail,replay,D
P=Path(__file__).parent
A=json.loads((P/'TERMINAL_TRAP_CERTIFICATE.json').read_text());H=A['period'];Q,pe,he=geometry((0,0),2,H);d=pe
heads=[];h=2
for a in H:heads.append(h);h=(h+(1 if a=='R'else-1))%4
for n in [(1,0),(0,-1),(1,-1)]:
 f=lambda x:sum(a*b for a,b in zip(n,x));delta=f(d);past=max(map(f,Q))-delta;records=[]
 for i,q in enumerate(Q):
  if f(q)>past:
   W=H[i:]+H[:i];V,vp,vh=geometry((0,0),heads[i],W);assert vp==d
   G=set()
   for v in V:
    for k in range(max(0,(-1-f(v))//delta+1)):G.add(tuple(v[j]+k*d[j]for j in range(2)))
   first={};
   for k in range(10):
    for j,v in enumerate(V):
     x=tuple(v[u]+k*d[u]for u in range(2))
     if x in G and x not in first:first[x]=[k*104+j,W[j]]
   assert set(first)==G
   J={x for x,(t,a)in first.items()if a=='L'}
   verify_tail(J,(0,0),heads[i],W)
   records.append(dict(phase=i,pose=[q,heads[i]],guard_size=len(G),black_size=len(J),black=sorted(J),guard=sorted(G),max_first_read=max(t for t,a in first.values()),cycle_word=W))
  past=max(past,f(q))
 print(n,[(x['phase'],x['pose'],x['guard_size'],x['black_size'],x['max_first_read'])for x in records])
 (P/('STANDARD_RECORD_PROBE_'+str(n[0])+'_'+str(n[1])+'.json')).write_text(json.dumps(records,indent=2)+'\n')
