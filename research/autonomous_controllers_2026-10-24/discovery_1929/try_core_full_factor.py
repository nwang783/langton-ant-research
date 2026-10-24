import json,time
from certify_active_C_entry_exit_forests import active_C
from check_extremal_read_coupling import D,event_word
from certify_middle_short_return_dictionary import literal,K
pre='RRRRLRRRRLLLLRLLRRRRLLRLLRRRRLLR'+'RRRLLRLRRLRRLRRLRLLR'+'LLLL'
z=literal(pre);assert z['legal'];print('pre',len(pre),len(z['full_minimal_initial_black']),z['full_minimal_initial_black']);known={tuple(e['p']):False for e in z['events']};B0=set(map(tuple,z['full_final_black']));known={p:p in B0 for p in known};root=(-8,0);beg=time.monotonic();calls=0;answer=None;trail=[];added=set();path=[]
def dfs(p,h,k,limit,g):
 global calls,answer
 calls+=1
 if calls%10000==0 and time.monotonic()-beg>5:raise TimeoutError
 if k and p==root:
  if h==2 and g==0:
   zz=literal(pre+''.join(trail)+K)
   if zz['legal']:
    answer={'E2':''.join(trail),'whole_word':zz['word'],'added_initial_black':sorted(added),'length':k,'whole_factor':zz};return True
  return False
 if k==limit or max(abs(p[0]-root[0])+abs(p[1]-root[1]),abs(g))>limit-k:return False
 c=active_C(p,h)
 if 3*c[1]-c[0]<7 or p in[(-7,0),(-6,0)]:return False
 new=p not in known;options=[False,True]if new else[known[p]]
 for b in options:
  if new and b:added.add(p)
  known[p]=not b;turn='L'if b else'R';trail.append(turn);path.append([p,h,turn]);hh=(h+(-1 if b else 1))%4;pp=p[0]+D[hh][0],p[1]+D[hh][1]
  if dfs(pp,hh,k+1,limit,g+(-1 if b else 1)):return True
  trail.pop();path.pop()
  if new:del known[p]
  else:known[p]=b
  if new and b:added.remove(p)
 return False
try:
 for lim in range(4,81,4):
  if dfs(root,2,0,lim,0):break
except TimeoutError:pass
print('limit',lim,'calls',calls,'seconds',time.monotonic()-beg,'answer',None if answer is None else {k:v for k,v in answer.items()if k!='whole_factor'})
if answer:open('/tmp/core_full_factor_answer.json','w').write(json.dumps(answer,indent=2))
