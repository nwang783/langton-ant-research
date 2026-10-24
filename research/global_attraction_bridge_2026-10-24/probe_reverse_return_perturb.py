import json
from pathlib import Path
from blank_collision_operator import D
from blank_collision_absorber import certify_word
P=Path(__file__).parent
rows=[]
for N in(0,16,64,256):
 q=(-47-2*N,-28-2*N);x=(18,-22);B={q,x};p=(0,0);h=0;word=[];hit=64200+208*N;target=hit+12;capture=None;lo=0;hi=0;states={}
 for t in range(target+50001):
  normal=p[0]-p[1];lo=min(lo,normal);hi=max(hi,normal)
  if t in(hit,target):states[t]=dict(black=sorted(B),pose=[p,h])
  if t==hit:assert p==(20,-22)and h==0
  if t==target:assert p==x and p in B
  if t>=target+208 and t%104==target%104 and word[-104:]==word[-208:-104]:
   w=''.join(word[-104:]);c=certify_word([(z,(0,0),1)for z in B],p,h,w)
   if c is not None:
    capture=dict(time=t,post_extra_read=t-target,pose=[p,h],mass=len(B),drift=c['drift'],word=w,black=sorted(B));break
  a='L'if p in B else'R';word.append(a);B^={p};h=(h+(1 if a=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 row=dict(N=N,initial_black=[q,x],historical_hit_time=hit,extra_first_read=target,normal_range=[lo,hi],states=states,post_extra_word=''.join(word[target:]),capture=capture,last_time=t)
 rows.append(row)
 print(N,'capture',None if capture is None else capture['post_extra_read'],'normalrange',(lo,hi),'tail',None if capture is None else capture['drift'],flush=True)
(P/'REVERSE_RETURN_PERTURB_DISCOVERY.json').write_text(json.dumps(rows,indent=2)+'\n')
