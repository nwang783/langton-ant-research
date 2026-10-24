"""Occurrence-dependent identity/nine self-embedding, starting at first insertion.
No fixed controller or heading-state choice is imposed. Finite branching tree
only: EXHAUSTED proves the scoped absence; caps/prefixes are inconclusive.
"""
from search_heading_transport import inventories,D
import pathlib,json,time,hashlib,sys
sys.setrecursionlimit(10000)
CAP=2000;NODECAP=1000000

def search(root,dom):
 P=[root];board={};trail=[];macro=[];nodes=0;latest=0;maxread=0;maxmac=0;leaves=[];best=[];found=None;capped=False
 def go(i,t,x,y,h):
  nonlocal nodes,latest,maxread,maxmac,best,found,capped
  if nodes>=NODECAP:capped=True;return
  nodes+=1
  if t>maxread:maxread=t;maxmac=i;best=macro.copy()
  if t>=CAP:
   found=dict(macros=macro.copy(),reads=t,coarse_reads=i,pose=(x,y,h));return
  assert i<len(P);s=P[i];assert s//2==h
  choices=dom[s%2]
  if i==0:choices=[w for w in choices if len(w)>1 and w[0]=='RL'[root%2]]
  for w in choices:
   save=(len(P),len(trail));tt=t;xx=x;yy=y;hh=h;conf=None
   for c in w:
    actual=2*hh+(c=='L')
    if tt<len(P):
     if P[tt]!=actual:conf=dict(kind='state',read=tt);break
    else:P.append(actual)
    q=(xx,yy);old=board.get(q)
    if old==c:conf=dict(kind='color',read=tt,cell=q,turn=c);break
    trail.append((q,old));board[q]=c;hh=(hh+(1 if c=='R' else -1))%4;xx+=D[hh][0];yy+=D[hh][1];tt+=1
   macro.append(w)
   if conf is None:go(i+1,tt,xx,yy,hh)
   else:
    latest=max(latest,conf['read']);leaves.append(dict(macros=macro.copy(),**conf))
   macro.pop()
   while len(trail)>save[1]:
    q,old=trail.pop()
    if old is None:del board[q]
    else:board[q]=old
   del P[save[0]:]
   if found is not None or capped:return
 go(0,0,0,0,0)
 return dict(root=root,status='PREFIX SURVIVOR' if found else 'NODE CAP' if capped else 'EXHAUSTED',nodes=nodes,latest_conflict=latest,max_read_boundary=maxread,max_coarse_boundary=maxmac,conflict_leaves=len(leaves),survivor=found,best_macros=best),leaves

def main():
 st=time.monotonic();dom=inventories();results=[];records=[]
 for root in [0,1]:
  a,b=search(root,dom);results.append(a);records.extend(dict(root=root,**z) for z in b)
 p=pathlib.Path(__file__);raw=(json.dumps(records,sort_keys=True,separators=(',',':'))+'\n').encode();p.with_suffix('.records.json').write_bytes(raw)
 ans=dict(scope='arbitrary occurrence choices identity or legal charge-preserving unit9, normalized at first nonidentity insertion, equal poses at coarse/fine checkpoints',prefix_cap=CAP,node_cap=NODECAP,results=results,seconds=time.monotonic()-st,records_sha256=hashlib.sha256(raw).hexdigest())
 p.with_suffix('.json').write_text(json.dumps(ans,indent=2)+'\n');print(json.dumps(ans))
if __name__=='__main__':main()
