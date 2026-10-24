"""Exact downward sweep of X F Y, X,Y over U,V and F Q/B.
Research enumerator: a separation cap is an explicit frontier, not a proof.
Flags: bit0 old/prepend active; bit1 new/append active.
Field bits: first L, last L, any-X, any-F, any-Y, any-marked-first-L-input.
"""
from collections import deque,Counter
from pathlib import Path
import json,sys,time
from verify_macro_word import D,check,rot
ROOT=Path(__file__).parent
X,F,Y,TIP=4,8,16,32
MARKS={"U":[(-1,0),(-1,1),(-1,2),(0,2),(0,3)],"V":[(-1,0),(1,2)]}

def encode(dx,dy,flags,field):return(dx,dy,flags,tuple(sorted((x,y,v)for(x,y),v in field.items())))
def prune(dx,dy,flags,field):
 ceiling=max(([0]if flags&1 else[])+([dy+1]if flags&2 else[]))
 field={p:v for p,v in field.items()if p[1]<=ceiling}
 if flags==1 and not any(v&TIP for v in field.values()):return None
 if flags==2 and not any(v&(X|F)for v in field.values()):return None
 return encode(dx,dy,flags,field)

def initialize(f):
 field={}
 for z in D[f]['trace']:
  p=tuple(z['p']);c=z['c']=='L';v=field.get(p)
  if v is not None:assert bool(v&2)!=c;field[p]=(v&~2)|(2*c)|F
  else:field[p]=int(c)*3|F
 dx,dy,h=D[f]['end_pose'];assert h==2
 return prune(dx,dy,3,field)

def steps(state):
 dx,dy,flags,items=state;field={(x,y):v for x,y,v in items}
 if flags==3:
  for nf in(1,2):
   q=prune(dx,dy,nf,field)
   if q is not None:yield('stop'+str(nf),q,False)
 side=1 if flags==1 or flags==3 and 0>=dy+1 else 2
 for a in'UV':
  fx,fy,_=D[a]['end_pose'];nf=dict(field);hit=False
  if side==1:
   # New old-head is (-fx,-fy); traverse this prepended macro backwards.
   for z in reversed(D[a]['trace']):
    x,y=z['p'];p=x-fx,y-fy;c=z['c']=='L';v=nf.get(p)
    if v is not None:
     if bool(v&1)==c:break
     hit|=bool(v&TIP);nf[p]=(v&~1)|int(c)|X
    else:nf[p]=int(c)*3|X
   else:
    nf={(x+fx,y+fy):v for(x,y),v in nf.items()};q=prune(dx+fx,dy+fy,flags,nf)
    if q is not None or hit:yield('X'+a,q,hit)
  else:
   tips=[(dx-x,dy-y)for x,y in MARKS[a]]
   if any(tip in nf for tip in tips):hit=True
   for z in D[a]['trace']:
    x,y=z['p'];p=dx-x,dy-y;c=z['c']=='L';v=nf.get(p)
    if v is not None:
     if bool(v&2)==c:break
     nf[p]=(v&~2)|(2*c)|Y
    else:nf[p]=int(c)*3|Y
   else:
    for tip in tips:nf[tip]|=TIP
    q=prune(dx-fx,dy-fy,flags,nf)
    if q is not None or hit:yield('Y'+a,q,hit)

def replay(parent,node,act):
 acts=[act]
 while parent[node][0] is not None:
  node,aa=parent[node];acts.append(aa)
 f=parent[node][1];x='';y=''
 for aa in reversed(acts):
  if aa.startswith('X'):x=aa[1]+x
  elif aa.startswith('Y'):y+=aa[1]
 w=x+f+y;r=check(w)
 seen=set();reuses=[];seam={(0,0),(-1,-1),(0,-1),(1,0)}
 for bi,b in enumerate(r['blocks']):
  first={}
  for z in D[b['macro']]['trace']:first.setdefault(tuple(z['p']),z['c'])
  bx,by,bh=b['pose']
  for local,c in first.items():
   if c!='L' or local in seam:continue
   xx,yy=rot(local,bh);q=(bx+xx,by+yy)
   if q in seen:reuses.append({'block':bi,'local':local,'cell':q})
  for z in D[b['macro']]['trace']:
   xx,yy=rot(z['p'],bh);seen.add((bx+xx,by+yy))
 assert reuses
 r['marked_reuses']=reuses
 return r

def main():
 cap=int(sys.argv[1])if len(sys.argv)>1 else 8;limit=int(sys.argv[2])if len(sys.argv)>2 else 500000
 todo=deque();parent={};front=[];counts=Counter();start=time.time();high=[0,0]
 for f in'QB':
  s=initialize(f);parent[s]=(None,f);todo.append(s)
 while todo:
  s=todo.popleft();counts[s[2]]+=1;high=[max(high[0],abs(s[1])),max(high[1],len(s[3]))]
  for a,t,hit in steps(s):
   if hit:
    r=replay(parent,s,a);(ROOT/'one_fold_sweep_counterexample.json').write_text(json.dumps(r,indent=2));print('PHYSICAL COUNTEREXAMPLE',r['word'],flush=True);return
   if abs(t[0])>cap:front.append((s,a,t));continue
   if t not in parent:parent[t]=(s,a);todo.append(t)
  if len(parent)>=limit:print('STATE CAP',len(parent),'queue',len(todo),flush=True);break
  if sum(counts.values())%10000==0:print('PROGRESS',sum(counts.values()),len(parent),len(todo),'front',len(front),'elapsed',round(time.time()-start,2),flush=True)
 else:print('EXHAUSTED INSIDE SEPARATION CAP',cap,'states',len(parent),'frontier',len(front),flush=True)
 print('COUNTS',dict(counts),'max_abs_dy_and_cells',high,'elapsed',time.time()-start,flush=True)
 out={'separation_cap':cap,'states':len(parent),'frontier':len(front),'queue':len(todo),'counts':dict(counts),'max_abs_dy_and_cells':high}
 (ROOT/f'one_fold_sweep_{cap}.json').write_text(json.dumps(out,indent=2))
 # Raw states saved for exact far-shape analysis, not a proof when frontier exists.
 (ROOT/f'one_fold_sweep_states_{cap}.json').write_text(json.dumps({'states':list(parent),'frontier':[(a,t)for s,a,t in front]}))
if __name__=='__main__':main()
