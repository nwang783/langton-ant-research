"""Exact cut-token controls for completed ladder and two-finger modules."""
import json,sys
from pathlib import Path
DIR=((0,1),(1,0),(0,-1),(-1,0))
def G(a,n):
 if not n:return a*4
 b='L' if a=='R' else 'R';return a*2+G(b,n-1)+a*2
def B(a,n,m=None):
 b='L' if a=='R' else 'R'
 return a+G(b,n)+(a*3 if m is None else a+G(b,m)+a*2)
def analyze(w,detail=False):
 x=y=h=0;last={};tokens={};parent=[None];root=[0];depth=[0];r=[0];active=0;initial=[];nodes=[(0,(0,0),0)]
 for t,c in enumerate(w):
  q=(x,y)
  assert last.get(q)!=c,(t,q,c)
  last[q]=c
  if c=='R':tokens[q]=active;r[active]+=1
  else:
   p=tokens.pop(q,None)
   if p is None:initial.append(q)
   active=len(parent);parent.append(p);root.append(active if p is None else root[p]);depth.append(0 if p is None else depth[p]+1);r.append(0);nodes.append((t+1,q,h))
  h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy
 sizes={};positive={}
 for i,rt in enumerate(root):sizes[rt]=sizes.get(rt,0)+1;positive[rt]=positive.get(rt,0)+(r[i]>0)
 for p in tokens.values():sizes[root[p]]+=1
 out=dict(max_component=max(sizes.values()),max_depth=max(depth+[depth[p]+1 for p in tokens.values()]),max_positive=max(positive.values()),input_black=len(initial),output_black=len(tokens),components=len(sizes),pose=[x,y,h],final_root=root[-1])
 if detail:out.update(word=w,parent=parent,root=root,depth=depth,r=r,nodes=nodes,initial=initial,buds=[(q,p) for q,p in tokens.items()],sizes=sizes)
 return out
if __name__=='__main__':
 N=int(sys.argv[1]) if len(sys.argv)>1 else 30;out={};best={}
 for a in 'RL':
  for typ in ('G','B1','B2'):
   records=[]
   pairs=((n,None) for n in range(N+1)) if typ!='B2' else ((n,m) for n in range(N+1) for m in range(N+1))
   for n,m in pairs:
    w=G(a,n) if typ=='G' else B(a,n,m);z=analyze(w);z.update(n=n,m=m);records.append(z)
   key=typ+a;out[key]=records;best[key]={s:max(records,key=lambda z:z[s]) for s in ('max_component','max_depth','max_positive')}
 print(json.dumps(best,indent=2));Path(__file__).with_name('completed_module_forest_controls.json').write_text(json.dumps(dict(limit=N,best=best,records=out),indent=2))
