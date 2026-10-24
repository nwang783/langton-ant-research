from synthesize_third_return import *
import json
q=3;z=json.loads((OUT/'third_return_synthesis_v5_q3.json').read_text());B,p,h,data=final(q);origA={tuple(x)for x,s in data['labels']if s=='second'};B=set(map(tuple,data['initial']))|set(map(tuple,z['extra']));p,h=tuple(data['entry'][0]),data['entry'][1];r=0;events=[];t=0
for name,w in [('first',data['words'][0]),('return1',data['words'][1]),('second',data['words'][2]),('return2',z['return_word'])]:
 count=0
 for j,c in enumerate(w):
  assert c==('L'if p in B else'R')
  if c=='L':
   bridge=not connected(B-{p},0,*endpoints(p,0));ex=r>=3 or notbridge if False else r>=3 or not bridge
   if ex:events.append((name,j,r,bridge));count+=1
   r=0
  else:r+=1
  p,h=step(B,p,h);t+=1
 print(name,len(w),'exceptions',count,'mass',len(B),'pose',p,h)
print('events',events)
A=set(origA);startmass=len(B);cons=[];third='';r=0;last=False
for j in range(1000):
 c='L'if p in B else'R'
 if c=='L':
  ex=r>=3 or connected(B-{p},0,*endpoints(p,0))
  if ex:print('stop at exception',j,'r',r,'cell',p);break
  cons.append((p,p in A));A.discard(p);r=0
 else:r+=1
 third+=c;p,h=step(B,p,h)
print('THIRD','T',len(third),'gain',len(B)-startmass,'R',third.count('R'),'L',third.count('L'),'Acons',len(origA)-len(A),'Atotal',len(origA),'remaining',A,'Rtail',r,'pose',p,h)
