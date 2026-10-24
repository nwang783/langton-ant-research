from collections import defaultdict
from certify_active_C_entry_exit_forests import active_C
D=[(0,1),(1,0),(0,-1),(-1,0)]
B=set();p=(0,0);h=0;C=defaultdict(list);H=defaultdict(list);E=[];states={}
for t in range(20001):
 if t in [9977,20000]:states[t]=(set(B),p,h)
 if t==20000:break
 c='L'if p in B else'R';e=dict(t=t,p=p,h=h,c=c,C=active_C(p,h));E.append(e);C[e['C']].append(e);H[p].append(e)
 B.symmetric_difference_update({p});h=(h+(1 if c=='R' else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
# Standard tail at9977, drift computed from its104 events. A face is certified
# retired if no geometric translate of the104 active-C templates hits it later.
s0=9977;pd=(E[s0+104]['p'][0]-E[s0]['p'][0],E[s0+104]['p'][1]-E[s0]['p'][1]);print('d',pd)
def futurehit(q):
 for i in range(104):
  r=E[s0+i]['C'];nums=[]
  for a,b,d in zip(q,r,pd):
   if d==0:
    if a!=b:break
   elif (a-b)%d:break
   else:nums.append((a-b)//d)
  else:
   if nums and len(set(nums))==1 and s0+i+104*nums[0]>=20000:return True
 return False
out=[]
for q,es in C.items():
 if len(es)!=6 or ''.join(e['c']for e in es)!='RRRRLL' or es[-1]['t']-es[0]['t']!=12:continue
 if futurehit(q):continue
 out.append((q,[(e['t'],e['p'],e['h'],e['c'])for e in es]))
print('controls',len(out),out[:10])
