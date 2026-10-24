"""Eight literal paired-Hilbert embedding controls, not a finite-seed theorem."""
import json,pathlib
HERE=pathlib.Path(__file__).resolve().parent

def hilbert(n,bits=8):
 x=y=0;s=1;t=n
 while s<(1<<bits):
  rx=1&(t//2);ry=1&(t^rx)
  if not ry:
   if rx:x,y=s-1-x,s-1-y
   x,y=y,x
  x+=s*rx;y+=s*ry;t//=4;s*=2
 return x,y
results=[]
for swap in [0,1]:
 for sx in [-1,1]:
  for sy in [-1,1]:
   last={};old=(0,0);dy_old=1;word='';conflict=None;firstL=[]
   for n in range(1000):
    u,v=hilbert(n+1)
    if swap:u,v=v,u
    u*=sx;v*=sy;new=(u+v,u-v);dx,dy=new[0]-old[0],new[1]-old[1]
    assert abs(dx)==abs(dy)==1
    reads=[(old,'R' if dx==dy_old else 'L'),((old[0]+dx,old[1]),'R' if dy==-dx else 'L')]
    for j,(p,c) in enumerate(reads):
     t=2*n+j;word+=c
     if p in last and last[p][1]==c:
      conflict=dict(time=t,cell=p,letter=c,previous=last[p][0]);break
     if p not in last and c=='L':firstL.append(p)
     last[p]=(t,c)
    if conflict:break
    old=new;dy_old=dy
   assert conflict and conflict['time'] in [5,17]
   results.append(dict(swap=swap,sx=sx,sy=sy,word=word,conflict=conflict,firstL=firstL))
(HERE/'paired_hilbert_controls.json').write_text(json.dumps(results,indent=2))
print('PASS: all8 embeddings fail literal alternation at5 or17')
