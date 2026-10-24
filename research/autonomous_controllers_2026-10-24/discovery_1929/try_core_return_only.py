import json,time
from certify_active_C_entry_exit_forests import active_C
from check_extremal_read_coupling import D
z=json.load(open('middle_short_return_dictionary_certificate.json'))['arbitrary_suffix_prefix_cover']['unique_32_read_prepared_survivor_before_E1']
known={tuple(e['p']):False for e in z['events']};B0=set(map(tuple,z['full_final_black']));known={p:p in B0 for p in known};root=(-8,0);target=(-7,1);beg=time.monotonic();calls=0;answer=None;trail=[];added=set();path=[]
def dfs(p,h,k,limit,targetseen):
 global calls,answer
 calls+=1
 if calls%10000==0 and time.monotonic()-beg>2:raise TimeoutError
 if k and p==root:
  if h==2:
   answer={'word':''.join(trail),'added_initial_black':sorted(added),'events':path.copy(),'length':k};return True
  return False
 if k==limit or abs(p[0]-root[0])+abs(p[1]-root[1])>limit-k:return False
 c=active_C(p,h)
 if 3*c[1]-c[0]<7 or p in[(-7,0),(-6,0)]:return False
 new=p not in known
 options=[False,True]if new else[known[p]]
 if False:
  if targetseen or h!=2:return False
  options=[False]if new else([False]if not known[p]else[])
 for b in options:
  if new and b:added.add(p)
  known[p]=not b;turn='L'if b else'R';trail.append(turn);path.append([p,h,turn]);hh=(h+(-1 if b else 1))%4;pp=p[0]+D[hh][0],p[1]+D[hh][1]
  if dfs(pp,hh,k+1,limit,targetseen or p==target):return True
  trail.pop();path.pop()
  if new:del known[p]
  else:known[p]=b
  if new and b:added.remove(p)
 return False
try:
 for lim in range(4,53,4):
  if dfs(root,2,0,lim,False):break
except TimeoutError:pass
print('calls',calls,'seconds',time.monotonic()-beg,'answer',answer)
if answer:open('/tmp/owned_core_return_answer.json','w').write(json.dumps(answer,indent=2))
