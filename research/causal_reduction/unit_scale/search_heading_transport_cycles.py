"""The first-state two-cycle residue of independent identity/nine transport.
Source palettes are shared with the author fixed-root generator, not claimed
as independent audit. The pending-state stack expands phi^2 lazily.
"""
from search_heading_transport import inventories,D,CAP
import itertools,pathlib,json,hashlib,time

def children(s,w):
 h=s//2;out=[]
 for c in w:
  out.append(2*h+(c=='L'));h=(h+(1 if c=='R' else -1))%4
 return out

def search(root,initial,dom):
 ass=initial.copy();P=[root];board={};trail=[];records=[];survivors=[];nodes=covered=latest=maxi=0
 def go(i,t,x,y,h,pending):
  nonlocal nodes,covered,latest,maxi
  nodes+=1;save=(len(P),len(trail));conf=None
  while t<CAP:
   if not pending:
    assert i<len(P);pending=[(P[i],2)];i+=1;maxi=max(maxi,i)
   s,depth=pending[-1]
   if depth:
    if ass[s] is None:
     for w in dom[s%2]:
      ass[s]=w;go(i,t,x,y,h,pending.copy())
     ass[s]=None;break
    pending.pop();pending.extend((c,depth-1) for c in reversed(children(s,ass[s])));continue
   pending.pop()
   if s//2!=h:conf=dict(kind='heading',read=t);break
   if t<len(P):
    if P[t]!=s:conf=dict(kind='state',read=t);break
   else:P.append(s)
   c='RL'[s%2];q=(x,y);old=board.get(q)
   if old==c:conf=dict(kind='color',read=t,cell=q,turn=c);break
   trail.append((q,old));board[q]=c;h=(h+(1 if c=='R' else -1))%4;x+=D[h][0];y+=D[h][1];t+=1
  if conf is not None:
   latest=max(latest,conf['read']);n=sum(w is None for w in ass);weight=7**n;covered+=weight
   records.append(dict(assignment=ass.copy(),unassigned=n,completion_weight=weight,**conf))
  elif t==CAP:survivors.append(dict(assignment=ass.copy(),reads=t,pose=(x,y,h),coarse_reads=i))
  while len(trail)>save[1]:
   q,old=trail.pop()
   if old is None:del board[q]
   else:board[q]=old
  del P[save[0]:]
 go(0,0,0,0,0,[])
 return dict(root=root,root_R=initial[0],root_L=initial[1],nodes=nodes,latest_conflict=latest,max_coarse_reads=maxi,covered_rooted_controllers=covered,expected_rooted_controllers=7**6,conflict_branches=len(records),survivors=survivors),records

def main():
 st=time.monotonic();dom=inventories();out=[];records=[]
 for u in dom[0]:
  if u[0]!='L':continue
  for v in dom[1]:
   if v[0]!='R':continue
   for root in [0,1]:
    a,b=search(root,[u,v]+[None]*6,dom);out.append(a);records.extend(dict(root=root,**z) for z in b)
 p=pathlib.Path(__file__);raw=(json.dumps(records,sort_keys=True,separators=(',',':'))+'\n').encode();p.with_suffix('.records.json').write_bytes(raw)
 ans=dict(scope='eight independent heading-turn images, identity or legal charge-preserving unit length9; first-state two-cycle roots only',domains=dom,prefix_cap=CAP,results=out,seconds=time.monotonic()-st,records_sha256=hashlib.sha256(raw).hexdigest())
 p.with_suffix('.json').write_text(json.dumps(ans,indent=2)+'\n');print(json.dumps(ans))
if __name__=='__main__':main()
