import json,time,heapq
from certify_active_C_entry_exit_forests import active_C
from check_extremal_read_coupling import D
z=json.load(open('middle_short_return_dictionary_certificate.json'))['arbitrary_suffix_prefix_cover']['unique_32_read_prepared_survivor_before_E1'];basevisited=frozenset(tuple(e['p'])for e in z['events']);baseB=frozenset(map(tuple,z['full_final_black']));root=(-8,0);target=(-7,1);start=time.monotonic()
# State p,h,B,visited,targetseen,word,added
beam=[(root,2,baseB,basevisited,False,'',frozenset())];ans=None;tested=0
for depth in range(160):
 candidates=[];seen=set()
 for p,h,B,V,paid,w,added in beam:
  tested+=1;cc=active_C(p,h)
  if 3*cc[1]-cc[0]<7 or p in[(-7,0),(-6,0)]:continue
  new=p not in V;opts=[False,True]if new else[p in B]
  if p==target:
   if paid or h!=2:continue
   opts=[False]if p not in B else[]
  for b in opts:
   # choose unknown initial bit b; resulting bit is !b
   BB=(B|{p})if not b else(B-{p});VV=V|{p};ww=w+('L'if b else'R');hh=(h+(-1 if b else 1))%4;pp=p[0]+D[hh][0],p[1]+D[hh][1];pd=paid or p==target;aa=(added|{p})if new and b else added
   if pp==root:
    if hh==2 and pd:ans={'word':ww,'added_initial_black':sorted(aa),'length':len(ww)};break
    continue
   key=(pp,hh,BB,VV,pd)
   if key in seen:continue
   seen.add(key)
   goal=root if pd else target;dist=abs(pp[0]-goal[0])+abs(pp[1]-goal[1]);score=dist*8+len(aa)*0.1+(0 if pd else 20)
   candidates.append((score,len(candidates),(pp,hh,BB,VV,pd,ww,aa)))
  if ans:break
 if ans:break
 if not candidates:break
 # retain varied headings/positions as well as best scored paths
 beam=[x[2]for x in heapq.nsmallest(500,candidates)]
print('depth',depth,'tested',tested,'seconds',time.monotonic()-start,'answer',ans)
if ans:open('/tmp/owned_core_return_answer.json','w').write(json.dumps(ans,indent=2))
