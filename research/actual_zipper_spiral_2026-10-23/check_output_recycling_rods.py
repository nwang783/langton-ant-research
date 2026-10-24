"""Fixed full-board rod output recycling; initial/R lifetime labels retained."""
from check_collector import component
from check_spiral import *

def check(r):
 B={(x,0)for x in range(2*r)};p=(0,0);h=1;label={c:('initial',None)for c in B};first='LRRL'*r
 for t,c in enumerate(first):
  assert('L'if p in B else'R')==c
  if c=='R':label[p]=('first_R',t)
  else:del label[p]
  p,h=step(B,p,h)
 assert B=={(x,1)for x in range(2*r)}
 # Run through the next exceptional block and following ordinary epoch.
 phases=[];rprefix=0;phase={'blocks':0,'L':0,'R':0,'first_R_consumed':0,'initial_consumed':0,'entry_mass':len(B),'entry_active':len(component(B,wwhich(p,h),cursors(p,h)[1]))};seen_exception=0;word=''
 for t in range(1,12*len(B)+30):
  c='L'if p in B else'R';word+=c;k=wwhich(p,h);ex=False
  if c=='R':rprefix+=1;phase['R']+=1;label[p]=('later_R',t)
  else:
   ex=rprefix>=3 or connected(B-{p},k,*endpoints(p,k));phase['L']+=1;phase['blocks']+=1
   age=label.pop(p);phase['first_R_consumed']+=(age[0]=='first_R');phase['initial_consumed']+=(age[0]=='initial')
  p,h=step(B,p,h)
  if c=='L':
   rprefix=0
   if ex:
    phase.update(end_exception=True,exit_mass=len(B),exit_active=len(component(B,k,cursors(p,h)[1])));phases.append(phase)
    seen_exception+=1
    if seen_exception==3:break
    phase={'blocks':0,'L':0,'R':0,'first_R_consumed':0,'initial_consumed':0,'entry_mass':len(B),'entry_active':len(component(B,k,cursors(p,h)[1]))}
 return {'r':r,'first_epoch_R_outputs':2*r,'following_word':word,'phases_ending_at_exception':phases}

if __name__=='__main__':
 out=[check(r)for r in(1,2,3,10,30,100)]
 Path(__file__).with_name('output_recycling_rods_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
