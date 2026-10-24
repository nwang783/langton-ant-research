"""First positive sqrt-gain epoch followed by substantial first-R recycling.
No second branch is seeded: append an odd rod to the original spiral input.
"""
from check_collector import component
from check_spiral import *
DIR=((0,1),(1,0),(0,-1),(-1,0))

def check(q):
 P,p,h,vs,cells,spiralword=setup(q,4);n=len(P);r=n
 tmp=set(P);rp,rh=p,h
 for c in spiralword:rp,rh=step(tmp,rp,rh)
 dx,dy=DIR[rh];rod={(rp[0]+j*dx,rp[1]+j*dy)for j in range(2*r+1)}
 assert P.isdisjoint(rod)
 B=P|rod;M=len(B);initial=set(B);labels={c:('initial',0)for c in B};first=spiralword+'LRRL'*r+'L';k=wwhich(p,h)
 assert rank(B,k)==0 and len(component(B,k,cursors(p,h)[1]))==M
 rprefix=0;birth=[0,0];erase=[0,0];clock=0;firstR=0;firstL=0
 for t,c in enumerate(first):
  clock+=1;assert('L'if p in B else'R')==c,('first read',q,t,p,h,c)
  for kk in(0,1):
   yes=connected(B-{p}if c=='L'else B,kk,*endpoints(p,kk));(erase if c=='L'else birth)[kk]+=yes
  if c=='R':rprefix+=1;firstR+=1;labels[p]=('rod_R'if t>=len(spiralword)else'spiral_R',clock)
  else:
   firstL+=1;assert rprefix<=2 and not connected(B-{p},k,*endpoints(p,k));rprefix=0;assert labels.pop(p)[0]=='initial'
  p,h=step(B,p,h)
 assert len(B)-M==q-3 and firstL==M
 firstdata={'T':len(first),'gain':len(B)-M,'L':firstL,'R':firstR,'births':birth,'erasures':erase,'exit_mass':len(B),'exit_active':len(component(B,k,cursors(p,h)[1]))}
 assert firstdata['exit_active']==0
 rb=[0,0];re=[0,0]
 for c in 'RRRRL':
  assert('L'if p in B else'R')==c
  for kk in(0,1):
   yes=connected(B-{p}if c=='L'else B,kk,*endpoints(p,kk));(re if c=='L'else rb)[kk]+=yes
  clock+=1
  if c=='R':labels[p]=('reset_R',clock)
  else:assert labels.pop(p)[0]=='reset_R'
  p,h=step(B,p,h)
 entry=len(B);active=len(component(B,k,cursors(p,h)[1]));rprefix=0;blockreads=[];word='';ordinary=[];deleted=[];eb=[0,0];ee=[0,0]
 # Exact first-exception stopping condition, with signed zipper theorem bound.
 for t in range(3*entry+5):
  c='L'if p in B else'R';clock+=1;word+=c;blockreads.append((p,c))
  for kk in(0,1):
   yes=connected(B-{p}if c=='L'else B,kk,*endpoints(p,kk));(ee if c=='L'else eb)[kk]+=yes
  if c=='R':rprefix+=1;labels[p]=('second_R',clock)
  else:
   ex=rprefix>=3 or connected(B-{p},k,*endpoints(p,k));life=labels.pop(p);deleted.append((p,life[0],ex))
  p,h=step(B,p,h)
  if c=='L':
   if ex:
    finalexception={'r':rprefix,'deleted':deleted[-1]};break
   ordinary.append({'r':rprefix,'life':life[0]});rprefix=0;blockreads=[]
 else:raise AssertionError('violated first-exception finite-fuel bound')
 consumed={z:sum(b['life']==z for b in ordinary)for z in('initial','spiral_R','rod_R','reset_R','second_R')}
 assert consumed['initial']==consumed['second_R']==0
 assert consumed['rod_R']>=2*r-2
 return {'q':q,'spiral_input_edges':n,'odd_rod_input_edges':2*r+1,'M':M,'initial_ranks':[rank(initial,kk)for kk in(0,1)],'first':firstdata,'reset':{'births':rb,'erasures':re,'entry_second_mass':entry,'entry_second_active':active},'second_ordinary':{'blocks':len(ordinary),'R':sum(b['r']for b in ordinary),'gain':sum(b['r']-1 for b in ordinary),'consumed_lifetimes':consumed,'first_R_fraction':(consumed['spiral_R']+consumed['rod_R'])/max(1,len(ordinary))},'second_following_exception':finalexception,'second_prefix_word_sha256':hashlib.sha256(word.encode()).hexdigest(),'second_including_final_exception_births':eb,'second_including_final_exception_erasures':ee}

if __name__=='__main__':
 out=[check(q)for q in(1,2,3,4,8,16)]
 Path(__file__).with_name('positive_spiral_rod_recycling_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
