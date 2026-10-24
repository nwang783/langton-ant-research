"""Targeted positive spiral output made a backbone by charged corner stitches."""
from check_collector import cells_of,component
from check_spiral import *
Dxy=((0,1),(1,0),(0,-1),(-1,0))

def setup_stair(q):
 coarse=vertices(q,4);fine=[(0,0)]
 for u,v in zip(coarse,coarse[1:]):
  x,y=fine[-1];dx=v[0]-u[0];dy=v[1]-u[1];a=dx-dy;b=dx+dy
  fine.extend([(x+a,y),(x+a,y+b)])
 assert len(fine)==len(set(fine))
 es=[(v[0]-u[0],v[1]-u[1])for u,v in zip(fine,fine[1:])]
 turn=[es[i-1][0]*es[i][1]-es[i-1][1]*es[i][0]for i in range(1,len(es))]
 stitches=set()
 for i in range(1,len(fine)-2):
  if turn[i-1]==turn[i]==1:
   x,y=fine[i];dx,dy=es[i-1];u=(x+dx,y+dy);v=(fine[i+1][0]+dx,fine[i+1][1]+dy);stitches|=cells_of([u,v])
 assert len(stitches)==q-1
 # Odd endpoint hook: right turn, no R arm, reset lands on the output end.
 x,y=fine[-1];dx,dy=es[-1];fine.append((x+dy,y-dx));es.append((dy,-dx))
 assert len(fine)==len(set(fine))
 P=cells_of(fine);assert not P&stitches
 B=P|stitches
 dvs=list(map(xy,fine));p=next(iter(cells_of(fine[:2])));h=next(h for h in range(4)if cursors(p,h)[1]==dvs[0])
 word='L'
 for a,b in zip(es,es[1:]):
  t=a[0]*b[1]-a[1]*b[0];assert t in(-1,1);word+='R'*(1+t)+'L'
 return B,p,h,word,P,stitches

def check(q):
 B,p,h,word,P,C=setup_stair(q);M=len(B);initial=set(B);labels={c:'seed'for c in B};k=wwhich(p,h);R=L=0;birth=[0,0];erase=[0,0];r=0
 for t,c in enumerate(word):
  assert('L'if p in B else'R')==c,('first',q,t,p,h,c)
  for kk in(0,1):
   yes=connected(B-{p}if c=='L'else B,kk,*endpoints(p,kk));(erase if c=='L'else birth)[kk]+=yes
  if c=='R':R+=1;r+=1;labels[p]='first_R'
  else:
   L+=1;assert r<=2 and not connected(B-{p},k,*endpoints(p,k)),('ordinary bridge',q,t,p,r);r=0;assert labels.pop(p)=='seed'
  p,h=step(B,p,h)
 G=R-L
 assert len(B)-M==G
 assert birth==erase==[0,0],('first paired events',q,birth,erase)
 g={}
 for e in B:
  u,v=endpoints(e,k);g.setdefault(u,[]).append(v);g.setdefault(v,[]).append(u)
 assert all(len(ns)<=2 for ns in g.values()) and rank(B,k)==0
 assert len(component(B,k,next(iter(g))))==len(B)
 first={'L':L,'R':R,'gain':G,'T':len(word),'births':birth,'erasures':erase,'output_mass':len(B),'output_is_one_path':True,'R_output_edges':sum(x=='first_R'for x in labels.values()),'old_stitch_edges':sum(x=='seed'for x in labels.values())}
 reset=''
 for _ in range(5):
  c='L'if p in B else'R';reset+=c
  if c=='R':labels[p]='reset_R'
  else:labels.pop(p)
  p,h=step(B,p,h)
 assert reset=='RRRRL'
 entry=len(B);oldR=first['R_output_edges'];rp=0;secondbirth=[0,0];seconderase=[0,0];secondlabels=[];cons={'first_R':0,'seed':0,'reset_R':0,'second_R':0};secondR=secondL=0;body='';blocks=[]
 for t in range(3*entry+5):
  c='L'if p in B else'R';body+=c
  ev=[connected(B-{p}if c=='L'else B,kk,*endpoints(p,kk)) for kk in(0,1)]
  if c=='R':rp+=1;labels[p]='second_R';secondlabels.append(('R',ev))
  else:
   ex=rp>=3 or connected(B-{p},k,*endpoints(p,k));life=labels.pop(p);secondlabels.append(('L',ev))
  p,h=step(B,p,h)
  if c=='L':
   if ex:break
   cons[life]+=1;secondL+=1;secondR+=rp;blocks.append(rp);rp=0
 else:raise AssertionError('bound')
 ordinary_word=body[:-rp-1]
 ordinary_events=secondlabels[:len(ordinary_word)]
 assert all(not any(ev) for _,ev in ordinary_events),('second ordinary paired event',q)
 assert ordinary_word==('LRRL'*(2*q+1)+'L' if q>=3 else 'LRRL'*4)
 assert first['gain']==q-2 and M==2*(len(P)-1)//2+q
 return {'q':q,'initial_mass':M,'input_path_edges':len(P),'charged_stitches':len(C),'initial_ranks':[rank(initial,kk)for kk in(0,1)],'first':first,'reset':reset,'second':{'L':secondL,'R':secondR,'gain':secondR-secondL,'consumed':cons,'fraction_first_R_recycled':cons['first_R']/oldR,'ordinary_word':ordinary_word,'terminal_exception_r':rp,'terminal_exception_word':body[len(ordinary_word):],'terminal_events':secondlabels[len(ordinary_word):]}}

if __name__=='__main__':
 out=[check(q)for q in(1,3,5,7,9,15,25)]
 Path(__file__).with_name('staircase_backbone_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
