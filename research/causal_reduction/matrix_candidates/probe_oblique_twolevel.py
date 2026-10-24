"""Exact local two-level record relaxation; positive finite fragments are not models."""
import json,pathlib,sys,time,hashlib
P=pathlib.Path(__file__).parent
D=((0,1),(1,0),(0,-1),(-1,0)); A=((3,2),(2,7)); K=13
INV=json.loads((P/'mixed_k13_3_2_2_7_inventory.json').read_text())['domains']

def test(depth,cap=1000000):
 coarse={};fine={};stack=[];nodes=0;levels=[0]*(depth+1);capped=False
 def dfs(n,x,y,h,fx,fy,fh):
  nonlocal nodes,capped
  if n==depth:return list(stack)
  q=(x,y);old=coarse.get(q);choices=(4-old,) if old is not None else (1,) if y>=0 else (1,3)
  for turn in choices:
   z=(h+turn)%4;coarse[q]=turn
   for word in INV[z]:
    nodes+=1;levels[n]+=1
    if nodes>cap:capped=True;break
    xx,yy,hh=fx,fy,fh;undo=[];ok=True
    for d in word:
     c=(d-hh)%4;v=(xx,yy);prev=fine.get(v)
     if c not in (1,3) or prev==c or (prev is None and -2*xx+3*yy>=0 and c!=1):ok=False;break
     undo.append((v,prev));fine[v]=c;xx+=D[d][0];yy+=D[d][1];hh=d
    if ok:
     stack.append(dict(coarse_turn=turn,coarse_direction=z,image=''.join(map(str,word))))
     ans=dfs(n+1,x+D[z][0],y+D[z][1],z,xx,yy,hh)
     if ans is not None:return ans
     stack.pop()
    for v,prev in reversed(undo):
     if prev is None:del fine[v]
     else:fine[v]=prev
    if capped:break
   if old is None:del coarse[q]
   else:coarse[q]=old
   if capped:break
  return None
 st=time.monotonic();ans=dfs(0,0,0,0,0,0,0)
 return dict(k=K,matrix=A,depth=depth,cap=cap,nodes=nodes,levels=levels,status='LOCAL SURVIVOR, NOT A MODEL' if ans is not None else 'UNKNOWN' if capped else 'UNSAT',witness=ans,seconds=time.monotonic()-st)
if __name__=='__main__':
 d=int(sys.argv[1]) if len(sys.argv)>1 else 4;cap=int(sys.argv[2]) if len(sys.argv)>2 else 1000000;r=test(d,cap);out=P/f'oblique_twolevel_n{d}.json';out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
