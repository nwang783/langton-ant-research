from check_three_positive_passes import *
from collections import Counter
z=json.loads((OUT/'THREE_POSITIVE_PASSES_CHECKED.json').read_text())
for c in z['cases']:
 q=c['q'];B=set(map(tuple,c['full_final_field']));p,h=tuple(c['final_pose'][0]),c['final_pose'][1];origin={tuple(x):(o,b)for x,o,b in c['full_final_lifetime_labels']};G=Graph(B,0);A3={x for x,v in origin.items()if v[0]=='third_positive_ordinary'};stages=[];T=0;r=0
 for phase in range(3):
  name='exception'if phase%2==0 else'ordinary';word='';deaths=Counter();m=len(B);entry=[p,h];n=0
  while True:
   ch='L'if p in B else'R';cyc=ch=='L'and G.connected(p,True);ex=ch=='L'and(r>=3 or cyc)
   if name=='ordinary'and ex:break
   word+=ch
   if ch=='R':r+=1;origin[p]=('followup',T);B.add(p);G.insert(p);h=(h+1)%4
   else:
    o,b=origin.pop(p);deaths[o]+=1;B.remove(p);G.erase(p);h=(h-1)%4;r=0
   p=(p[0]+D[h][0],p[1]+D[h][1]);T+=1;n+=1
   if name=='exception'and ch=='L':break
   assert n<=3*m+10
  # Roll R prefix into next exception, rather than declaring it ordinary output.
  stages.append(dict(name=name,word=word,T=len(word),gain=len(B)-m,deaths=dict(deaths),entry=entry,exit=[p,h],unfinished_R=r))
 print('q',q,[(s['name'],s['T'],s['gain'],s['deaths'],s['unfinished_R'])for s in stages],'A3remain',len(A3&B),flush=True)
