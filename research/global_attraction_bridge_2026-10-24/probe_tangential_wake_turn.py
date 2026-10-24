import json
from pathlib import Path
from blank_collision_operator import D
from blank_collision_absorber import certify_word
P=Path(__file__).parent
S={(0,1),(0,2),(0,3),(2,4),(3,2),(3,3)}
rows=[]
for K in (0,1,2,3,5,11,32,128):
 B=S|{(5+2*K,-4-2*K)};p=(1,1);h=2;word=[];newrecords=[];best=2;low=2;high=2
 target=279+104*K;capture=None
 for t in range(target+20001):
  z=sum(p);low=min(low,z);high=max(high,z)
  if z<best:
   best=z
   if all(sum(q)>z for q in B):newrecords.append([t,p,h,z,len(B)])
  if t>=target+208 and t%104==target%104 and word[-104:]==word[-208:-104]:
   w=''.join(word[-104:]);c=certify_word([(q,(0,0),1)for q in B],p,h,w)
   if c is not None:
    capture={'time':t,'relative_to_interrupt':t-target,'pose':[p,h],'mass':len(B),'drift':c['drift'],'word':w,'full_black':sorted(B)};break
  a='L'if p in B else'R';word.append(a);B^={p};h=(h+(1 if a=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 rows.append(dict(K=K,first_interrupt=target,min_normal_sum=low,max_normal_sum=high,pristine_SW_records=newrecords,capture=capture,
                  post_interrupt_word=''.join(word[target:]),last_time=t))
 print(K,'capture',None if capture is None else capture['relative_to_interrupt'],'span',(low,high),'records',len(newrecords),flush=True)
(P/'TANGENTIAL_WAKE_TURN_DISCOVERY.json').write_text(json.dumps(rows,indent=2)+'\n')
