"""Enumerate self-consistent k^2 prefixes for pure position-only inflation.
No heading preservation, no initial-color or mass restriction.
A node cap is explicitly UNKNOWN and cannot certify exhaustiveness.
"""
import collections,itertools,json,pathlib,sys,time
from search_position_only_inflations import D,mul,rotate,trace,seed
HERE=pathlib.Path(__file__).resolve().parent

def enumerate_prefixes(k,a,nodecap=10000000):
 by=collections.defaultdict(list)
 for letters in itertools.product('RL',repeat=k):
  w=''.join(letters)
  if seed(w) is not None: by[trace(w)[1][:2]].append(w)
 poses=[(0,0,0)];letters=[];last={};choices=[];nodes=0;conflicts=0;results=[];capped=False
 def dfs(n):
  nonlocal nodes,conflicts,capped
  nodes+=1
  if nodes>nodecap: capped=True;return
  if n==k:
   results.append(dict(choices=choices.copy(),word=''.join(letters)));return
  for c in ('RL' if n==0 else letters[n]):
   x,y,h=poses[n];H=poses[-1][2]
   dx,dy=D[(h+(1 if c=='R' else -1))%4]
   target=mul(a,(dx,dy));local=rotate(*target,(-H)%4)
   for w in by.get(local,[]):
    if n==0 and w[0]!=c: continue
    undo=[];l0=len(letters);p0=len(poses);okay=True
    for ch in w:
     X,Y,H=poses[-1];q=X,Y;old=last.get(q)
     if old==ch: conflicts+=1;okay=False;break
     undo.append((q,old));last[q]=ch;letters.append(ch)
     H=(H+(1 if ch=='R' else -1))%4;dx,dy=D[H];poses.append((X+dx,Y+dy,H))
    if okay:
     assert poses[-1][:2]==mul(a,poses[n+1][:2])
     choices.append(w);dfs(n+1);choices.pop()
    for q,old in reversed(undo):
     if old is None:del last[q]
     else:last[q]=old
    del letters[l0:];del poses[p0:]
    if capped:return
 dfs(0)
 return dict(k=k,scale=a,status='NODE_CAP' if capped else 'COMPLETE',nodes=nodes,conflicts=conflicts,prefix_count=len(results),prefixes=results)
if __name__=='__main__':
 k=int(sys.argv[1]);a=tuple(map(int,sys.argv[2].split(',')));start=time.time()
 r=enumerate_prefixes(k,a);r['seconds']=time.time()-start
 p=HERE/f'position_only_prefixes_k{k}_a{a[0]}_{a[1]}.json';p.write_text(json.dumps(r,indent=2))
 print(json.dumps({key:value for key,value in r.items() if key!='prefixes'},indent=2))
