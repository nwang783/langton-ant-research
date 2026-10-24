#!/usr/bin/env python3
from pathlib import Path
import re,ast,json,hashlib
root=Path('/workspace/shared/langton/sources/kehao95-core/one_black/lean/OneBlack')
text=(root/'EntryData.lean').read_text()
rows=ast.literal_eval(re.search(r'def pristineLaneTimes.*?:=\s*(\[[\s\S]*?\])\s*def actualLaneTimes',text)[1])
D=((0,1),(1,0),(0,-1),(-1,0))
def step(B,p,h):
 b=p in B;B.symmetric_difference_update({p});h=(h+(-1 if b else 1))%4;d=D[h];return(p[0]+d[0],p[1]+d[1]),h,'L' if b else 'R'
B=set();p=(0,0);h=0
for _ in range(9977):p,h,_=step(B,p,h)
entry=p;eh=h
S=[];tmp=set(B);p=entry;h=eh
for _ in range(104):
 if p not in S:S.append(p)
 p,h,_=step(tmp,p,h)
d=(p[0]-entry[0],p[1]-entry[1]);base=B&set(S);heads=[s for s in S if(s[0]+d[0],s[1]+d[1])not in S]
assert len(heads)==len(rows)==22
def rot(p,k):
 for _ in range(k%4):p=(p[1],-p[0])
 return p
canonical_word='';bb=set(base);pp=entry;hh=eh
for _ in range(104):pp,hh,ch=step(bb,pp,hh);canonical_word+=ch
relS=[(x-entry[0],y-entry[1])for x,y in S]
relB={(x-entry[0],y-entry[1])for x,y in base}
def terminal_check(board,position,heading):
 k=(heading-eh)%4
 ss={rot(s,k)for s in relS};pat={rot(s,k)for s in relB};ee=rot(d,k)
 for z in ss:
  if ((position[0]+z[0],position[1]+z[1])in board)!=(z in pat):return False
 for point in board:
  z=(point[0]-position[0],point[1]-position[1])
  if z in ss:continue
  for a in ss:
   diff=(z[0]-a[0],z[1]-a[1]);ns=[]
   for v,w in zip(diff,ee):
    if w==0:
     if v:break
    elif v%w:break
    else:ns.append(v//w)
   else:
    if ns and len(set(ns))==1 and ns[0]>=1:return False
 return True
out=[]
for head,row in zip(heads,rows):
 n=len(row);t=row[-1];obs=(head[0]+n*d[0],head[1]+n*d[1]);bb=base|{obs};pp=entry;hh=eh
 for _ in range(t):pp,hh,_=step(bb,pp,hh)
 assert terminal_check(bb,pp,hh)
 start=pp;word=''
 for _ in range(104):pp,hh,ch=step(bb,pp,hh);word+=ch
 assert word==canonical_word
 e=(pp[0]-start[0],pp[1]-start[1]);out.append({'head_relative':[head[0]-entry[0],head[1]-entry[1]],'depth':n,'anchor':t,'outgoing_drift':e})
result={'status':'PASS','incoming_drift':d,'rows':out,'entry_data_sha256':hashlib.sha256((root/'EntryData.lean').read_bytes()).hexdigest(),'scope':'All22 supplied stable-anchor replays, complete-board standard terminal guards, and exact outgoing directions. Global pristine induction remains retained source.'}
rev=[r for r in out if tuple(r['outgoing_drift'])==tuple(-x for x in d)]
assert len(rev)==1 and rev[0]['head_relative']==[-2,-8]
result['unique_reversing_head_relative']=rev[0]['head_relative']
print(json.dumps(result,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
