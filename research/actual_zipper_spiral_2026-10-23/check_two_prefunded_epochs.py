"""Targeted exact two-epoch construction; second input is fully pre-funded."""
from check_detoured_collector import detoured
from check_collector import cells_of,component
from check_spiral import *

def forced_word(vs):
 word='L'
 for u,v,w in zip(vs,vs[1:],vs[2:]):
  a=(v[0]-u[0],v[1]-u[1]);b=(w[0]-v[0],w[1]-v[1]);cr=a[0]*b[1]-a[1]*b[0]
  turn=1 if cr>0 else -1 if cr<0 else 0 # ab CCW is physical CW
  word+='R'*(1+turn)+'L'
 return word

def make(q1,q2,scale=8):
 assert q1%4==q2%4==2
 P,p,h,dvs,cells,w=setup(q1,scale);pv=vertices(q1,scale);A,B=pv[-1]
 u=(A,B);v=(A+1,B);b=(A,B-1);a=(A+1,B-1)
 hook=cells_of([u,v]);Kvs=detoured(q1,scale);assert Kvs[-1]==v and Kvs[-2]==a
 K=cells_of(Kvs[:-1]);connector=cells_of([(0,0),(-1,0),(-1,-1),(0,-1)])
 branch=[b,(A-1,B-1),(A-2,B-1)]
 for j in range(1,17):branch.append((A-2,B-1+j))
 cw=[(0,0)]
 for j in range(1,q2+1):
  dx,dy=D[-(j-1)%4]
  for _ in range(scale*((j+1)//2)):
   x,y=cw[-1];cw.append((x+dx,y+dy))
 cw=cw[::-1];sx,sy=cw[0];ex,ey=branch[-1]
 second=[(x-sx+ex,y-sy+ey)for x,y in cw]
 assert second[1][0]==second[0][0] and second[1][1]==second[0][1]+1
 branch+=second[1:];assert len(branch)==len(set(branch))
 branchcells=cells_of(branch)
 assert P.isdisjoint(hook|K|connector|branchcells)
 assert not(hook&(K|connector|branchcells)) and not(K&(connector|branchcells))and not(connector&branchcells)
 board=P|hook|K|connector|branchcells
 assert rank(board,0)==0 and len(component(board,0,cursors(p,h)[1]))==len(board)
 w1=w+'L';v2=[a]+branch;w2=forced_word(v2)
 assert w2[:2]=='LR'
 return board,p,h,w1,w2,{'q1':q1,'q2':q2,'M':len(board),'first_path_edges':len(P)+1,'collector_edges':len(K),'connector_edges':len(connector),'prefunded_branch_edges':len(branchcells),'second_path_edges':len(v2)-1,'first_gain':q1-3,'second_gain':q2-3}

def check(q1,q2):
 B,p,h,w1,w2,data=make(q1,q2);initial=set(B);allblocks=[];segments=[]
 assert (0,1)not in B
 pre=B|{(0,1)};pp,hh=step(pre,(0,1),2);assert(pre,pp,hh)==(B,p,h)
 for name,word,ordinary in [('first_ordinary_epoch',w1,True),('R4_reset','RRRRL',False),('second_ordinary_epoch',w2,True)]:
  m0=len(B);act0=len(component(B,0,cursors(p,h)[1]));r=0;birth=[0,0];erase=[0,0];blockct=0
  for t,c in enumerate(word):
   assert ('L'if p in B else'R')==c,('read',q1,q2,name,t,p,h,c)
   for kk in(0,1):
    yes=connected(B-{p}if c=='L'else B,kk,*endpoints(p,kk));(erase if c=='L'else birth)[kk]+=yes
   if c=='R':r+=1
   else:
    wb=connected(B-{p},0,*endpoints(p,0));assert not ordinary or(r<=2 and not wb),(name,t,r,wb)
   p,h=step(B,p,h)
   if c=='L':blockct+=1;allblocks.append({'segment':name,'r':r,'active_after':len(component(B,0,cursors(p,h)[1]))});r=0
  segments.append({'name':name,'T':len(word),'entry_mass':m0,'exit_mass':len(B),'gain':len(B)-m0,'entry_active_mass':act0,'exit_active_mass':len(component(B,0,cursors(p,h)[1])),'blocks':blockct,'births':birth,'erasures':erase,'ranks':[rank(B,kk)for kk in(0,1)]})
 assert segments[0]['gain']==data['first_gain'] and segments[2]['gain']==data['second_gain']
 assert segments[0]['blocks']==data['first_path_edges'] and segments[2]['blocks']==data['second_path_edges']
 assert segments[0]['exit_active_mass']==segments[2]['exit_active_mass']==0
 data.update(segments=segments,first_following_ordinary_blocks=[d for d in allblocks if d['segment']=='second_ordinary_epoch'][:6],initial_ranks=[rank(initial,kk)for kk in(0,1)])
 return data

if __name__=='__main__':
 out=[check(q,q)for q in(2,6,10,14)]
 Path(__file__).with_name('two_prefunded_epochs_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
