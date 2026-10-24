from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files={'RRLL_flat_strip_is_one_exact_temporal_archive_interval.md':'a8422e3e30c8e5a3bad234f3817385f5805a32513387ca5eed0900ee1a423324','check_RRLL_strip_temporal_relay.py':'9a7629526811bc8ae08b3561fb752eeb22efd2439dbb53c768a4a939f828c81a','check_RRLL_strip_temporal_relay.json':'8ce9bb6f84b203bd715a2ea7db6b12a56d15fc38d997451de6cd0aebb382989a'}
for f,h in files.items():assert sha(D/f)==h
signed=R/'audits/check_open_flat_strip_independent.json';assert sha(signed)=='c60807ab27a7fa005bb0b547849f7e6653b5999e47613d025ed7caee42d81abc'
J=json.loads((D/'check_RRLL_strip_temporal_relay.json').read_text());C=json.loads((D/'check_open_flat_RRLL_strip_family.json').read_text());rows=[]
for row in J['rows']:
 k=row['k'];z=next(x for x in C['unit_controls']if x['k']==k);T={(tuple(p),r):b['start_time']+i for b in z['blocks']for i,(p,r)in enumerate(b['events'])};a=lambda j:(2*j,0);b=lambda j:(2*j+1,0);u=lambda j:(2*j,-1);v=lambda j:(2*j+1,-1)
 intervals=[];selected=[]
 for j in range(k):
  for p in(a(j),b(j)):assert all(T[p,r+1]-T[p,r]>=4 for r in range(3));intervals.append((T[p,1],T[p,3]))
  assert T[b(j),3]==T[a(j),1]+1;selected.append((T[a(j),1],T[b(j),3]))
  if j:
   seq=[(a(j),2),(b(j-1),1),(v(j-1),3),(u(j),3),(a(j),3),(b(j-1),2)];ts=[T[x]for x in seq];assert ts==list(range(ts[0],ts[0]+6));selected.extend(zip(ts[1:4],ts[2:5]))
 ordered=[(T[p,1],T[p,3])for j in range(k-1,-1,-1)for p in(b(j),a(j))]
 assert all(x<xx and y<yy for(x,y),(xx,yy)in zip(ordered,ordered[1:]));overlaps=[y-xx for(x,y),(xx,yy)in zip(ordered,ordered[1:])];assert overlaps==[1 if i%2==0 else 3 for i in range(2*k-1)];assert all(ordered[i+2][0]-ordered[i][1]>=4 for i in range(len(ordered)-2))
 U=(ordered[0][0],ordered[-1][1]);assert list(U)==row['effective_interval']and list(map(list,intervals))==row['flat_intervals']and list(map(list,selected))==row['selected_internal_edges']and len(selected)==4*k-3
 # Exact integer endpoint jump identity proves equality at every real regular time.
 jumps=Counter()
 for x,y in intervals:jumps[x]+=1;jumps[y]-=1
 for x,y in[U]+selected:jumps[x]-=1;jumps[y]+=1
 assert all(v==0 for v in jumps.values())
 for P in(19,38):
  for t in range(P):
   count=lambda arr:sum((2*t+1-2*x)//(2*P)-(2*t+1-2*y)//(2*P)for x,y in arr)
   assert count(intervals)==count([U])+count(selected)
 rows.append(dict(k=k,flat_intervals=2*k,selected_internal_edges=len(selected),effective_length=U[1]-U[0],integrated_age=sum(y-x for x,y in intervals)))
out=dict(status='PASS all-index all-Y temporal relay; not physical strip deletion',files=files,script=sha(S),dependency=sha(signed),controls=rows,analytic_review=['For every index the signed complete ordinal table gives a_j.L1 -> b_j.L3 and the full six-event LL chain a_(j+1).R2,b_j.L1,v_j.L3,u_(j+1).L3,a_(j+1).L3,b_j.R2. These formulas include every internal bridge; k=1 has only the RR edge.','Rank gaps>=4 imply strict reverse-spatial start/end order. Adjacent overlaps alternate1 and3; two-apart gaps are>=4. Specifically end(b_j)=start(a_j)+1 and start(b_(j-1))=T2(a_j)+1>=start(a_j)+5. Also end(a_j)=start(b_(j-1))+3, while start(a_(j-1))>=start(b_(j-1))+7. This proves absence of third overlap for ALL k, not sample extrapolation.','The consecutive union is exactly U, and double coverage is exactly the4k-3 selected actual boundary edge intervals. Thus the pointwise identity and integrated age identity hold for ANY clocks satisfying the complete ordinal/rank constraints, not only the supplied open schedule. Summing all P-translates preserves equality and every old copy.','Cancellation against signed5671 is a temporal-cochain substitution only, conditional on a proper full boundary embedding with distinct quotient event classes. Spatial displacement2k-1, curvature+2, every exterior connector, full voltages and physical read constraints remain. No ant splice, fresh output payment, bounded age, complete front or period inference follows. End-X changes are explicitly outside the positive relay theorem.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
