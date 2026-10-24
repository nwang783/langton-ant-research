"""Exact two large epochs: second consumes ALL first R output, no extra input branch."""
from check_collector import component
from check_spiral import *

def check(r):
 B={(x,0)for x in range(2*r+1)};p=(0,0);h=1;label={c:('initial',None)for c in B};M=len(B);segments=[];clock=0;pairs=[]
 pre=B|{(-1,0)};pp,hh=step(pre,(-1,0),2);assert(pre,pp,hh)==(B,p,h)
 for name,word,ordinary in [('first_ordinary',('LRRL'*r)+'L',True),('R4_reset','RRRRL',False),('second_ordinary','LRRL'*r,True)]:
  m0=len(B);act0=len(component(B,wwhich(p,h),cursors(p,h)[1]));rprefix=0;birth=[0,0];erase=[0,0];consumed={'initial':0,'first_R':0,'reset_R':0,'second_R':0};L=R=0
  for t,c in enumerate(word):
   clock+=1;assert('L'if p in B else'R')==c,('read',r,name,t,p,h,c)
   k=wwhich(p,h)
   for kk in(0,1):
    yes=connected(B-{p}if c=='L'else B,kk,*endpoints(p,kk));(erase if c=='L'else birth)[kk]+=yes
   if c=='R':
    R+=1;rprefix+=1;label[p]=({'first_ordinary':'first_R','R4_reset':'reset_R','second_ordinary':'second_R'}[name],clock)
   else:
    L+=1;life,born=label.pop(p);consumed[life]+=1
    if life=='first_R':pairs.append({'cell':p,'birth':born,'death':clock,'age':clock-born})
    assert not ordinary or(rprefix<=2 and not connected(B-{p},k,*endpoints(p,k)))
    rprefix=0
   p,h=step(B,p,h)
  segments.append({'name':name,'T':len(word),'entry_mass':m0,'exit_mass':len(B),'gain':len(B)-m0,'entry_active':act0,'exit_active':len(component(B,k,cursors(p,h)[1])),'L':L,'R':R,'births':birth,'erasures':erase,'consumed_lifetimes':consumed,'position':p,'heading_NESW':h,'ranks':[rank(B,kk)for kk in(0,1)]})
  if name=='first_ordinary':assert B=={(x,1)for x in range(2*r)} and(p,h)==((2*r,1),0)
  if name=='R4_reset':assert(p,h)==((2*r-1,1),3)
 assert segments[2]['consumed_lifetimes']['first_R']==2*r
 assert segments[2]['consumed_lifetimes']['initial']==segments[2]['consumed_lifetimes']['reset_R']==0
 assert B=={(x,0)for x in range(2*r)}|{(2*r+1,1),(2*r+1,0),(2*r,0)}
 assert (p,h)==((-1,1),3)
 assert [z['cell']for z in pairs]==[(x,1)for x in range(2*r-1,-1,-1)]
 for j in range(r):
  assert pairs[2*j]['age']==8*j+8 and pairs[2*j+1]['age']==8*j+12
 return {'r':r,'initial_mass':M,'total_T':clock,'first_R_recycled':2*r,'segments':segments,'first_R_birth_death_pairing':pairs}

if __name__=='__main__':
 out=[check(r)for r in(1,2,3,10,30,100)]
 Path(__file__).with_name('odd_rod_recycling_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out[-1],indent=2))
