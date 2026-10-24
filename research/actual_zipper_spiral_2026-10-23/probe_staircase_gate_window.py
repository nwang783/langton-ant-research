"""Exact finite spatial-window exit, not a chosen time-depth scan."""
from check_staircase_backbone import *

def probe(q,pad=2):
 B,p,h,word,P,C=setup_stair(q);k=wwhich(p,h);labels={c:('seed',c)for c in B};born={};t=0
 for c in word:
  t+=1
  if c=='R':labels[p]=('first_R',p);born[p]=t
  else:assert labels.pop(p)[0]=='seed'
  p,h=step(B,p,h)
 final=set(B);arm_to_gate={};gates=[]
 for stitch in sorted(C):
  es=endpoints(stitch,k);arms=[]
  for v in es:
   a=[e for e in B if e!=stitch and v in endpoints(e,k)]
   assert len(a)==1 and labels[a[0]][0]=='first_R';arms+=a
  i=len(gates);gates.append({'stitch':stitch,'arms':arms,'deaths':[]})
  for a in arms:assert a not in arm_to_gate;arm_to_gate[a]=i
 lo=(min(x for x,y in B)-pad,min(y for x,y in B)-pad);hi=(max(x for x,y in B)+pad,max(y for x,y in B)+pad)
 entry=t;seen=set();r=0;E=0;events=[];allR=sum(lab[0]=='first_R'for lab in labels.values());deathsR=0;body=''
 while lo[0]<=p[0]<=hi[0] and lo[1]<=p[1]<=hi[1]:
  key=(p,h,frozenset(B))
  if key in seen:reason='literal full-state repeat inside window';break
  seen.add(key);c='L'if p in B else'R';body+=c;t+=1
  if c=='R':r+=1;labels[p]=('later_R',t)
  else:
   cyc=connected(B-{p},k,*endpoints(p,k));ex=r>=3 or cyc;life=labels.pop(p)
   if ex:E+=1
   if life[0]=='first_R':
    deathsR+=1
    if life[1]in arm_to_gate:gates[arm_to_gate[life[1]]]['deaths'].append({'time_after_first':t-entry,'E_so_far':E,'w_exceptional':ex,'r':r,'cell':p})
   if ex:events.append({'time_after_first':t-entry,'r':r,'nonbridge':cyc,'cell':p,'pose_heading':h,'life_class':life[0]})
   r=0
  p,h=step(B,p,h)
 else:reason='first spatial-window exit'
 return {'q':q,'window':[lo,hi],'stop':reason,'post_first_updates':t-entry,'w_exceptional_blocks':E,'total_first_R':allR,'first_R_consumed':deathsR,'gate_arms_consumed':sum(len(g['deaths'])for g in gates),'total_gate_arms':2*len(gates),'gates':gates,'exception_events':events,'word':body,'exit_pose':[p,h],'final_mass':len(B)}

if __name__=='__main__':
 out=[probe(q)for q in(3,5,7,9)]
 Path(__file__).with_name('staircase_gate_window_probe.json').write_text(json.dumps(out,indent=2)+'\n')
 for x in out:print({k:v for k,v in x.items()if k not in('gates','exception_events','word')})
