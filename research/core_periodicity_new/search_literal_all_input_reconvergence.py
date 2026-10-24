"""Exact finite literal word search for an all-input incidence cycle.
Unknown required-black residual inputs are initial roots, never free production.
"""
from pathlib import Path
import json,sys,time
W=Path(__file__).resolve().parent;G0=json.loads((W/'chronology_dcuv/literal_residual_geometry.json').read_text());G=G0['geometry'];K={tuple(p)for p in G0['core']};IDS=(0,1,4,5,6,7,8,9)
def rot(p,h):x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def find(P,a):
 while P[a]!=a:a=P[a]
 return a
# state: head,h,colors,residual identities,DSU,entry roots,C,history
INIT=((0,0),0,{p:True for p in K},{},[],[],0,[])
def advance(S,a,cap):
 head,h,color,tokens,PP,roots,C,hist=S
 color=color.copy();tokens=tokens.copy();P=PP.copy();roots=roots.copy();new=[]
 core={add(head,rot(p,h))for p in K};I=[add(head,rot(p,h))for p in G[a]['inputs']]
 for x,y,b,*_ in G[a]['requirements']:
  p=add(head,rot((x,y),h))
  if p in color:
   if color[p]!=b:return None
  else:color[p]=b
 for p in I:
  if p not in tokens:
   # Only a previously unrepresented initial black can enter here.
   # All produced residuals were installed at their birth.
   if p in core:return None
   k=len(roots)
   if k>=cap:return None
   roots.append(p);P.append(k);tokens[p]=['root',k,k];new.append([list(p),k])
 assert not any(p in tokens for p in core)
 inp=[[list(p),tokens[p]]for p in I]; comps={find(P,tokens[p][-1])for p in I};inc=len(I)-len(comps)
 z=min(comps)
 for k in comps:P[k]=z
 for p in I:del tokens[p]
 out=[]
 for si,q in enumerate(G[a]['outputs']):
  p=add(head,rot(q,h));assert p not in tokens,(hist,a,'outputcollision',p)
  tag=[len(hist),si,z];tokens[p]=tag;out.append([list(p),tag])
 for q in G[a]['raw_odd']:
  p=add(head,rot(q,h));assert p in color;color[p]=not color[p]
 dx,dy,dh=G[a]['endpoint'];nh=add(head,rot((dx,dy),h));hh=(h+dh)%4
 nc={add(nh,rot(p,hh))for p in K}
 assert not any(p in tokens for p in nc)
 assert {p for p,b in color.items()if b}==nc|set(tokens),('ledger',hist,a)
 rec=dict(packet=a,name=G[a]['name'],pose=[*head,h],C_before=C,new_initial_roots=new,inputs=inp,input_components=sorted(comps),outputs=out,beta_increment=inc)
 return(nh,hh,color,tokens,P,roots,C+({0:0,1:1,4:0,5:1,6:2,7:0,8:1,9:2}[a]),hist+[rec])
if __name__=='__main__':
 cap=int(sys.argv[1]);depth=int(sys.argv[2]);limit=int(sys.argv[3])if len(sys.argv)>3 else 10000000
 goal=int(sys.argv[4])if len(sys.argv)>4 else 1
 stats=dict(nodes=0,legal_by_depth=[0]*(depth+1),cap=cap,depth=depth,limit=limit);start=time.time();hit=None
 stack=[INIT]
 while stack:
  s=stack.pop();d=len(s[-1]);stats['nodes']+=1;stats['legal_by_depth'][d]+=1
  if sum(r['beta_increment']for r in s[-1])>=goal:hit=s;break
  if d==depth:continue
  if stats['nodes']>=limit:stats['capped']=True;break
  for a in reversed(IDS):
   t=advance(s,a,cap)
   if t is not None:stack.append(t)
 stats['seconds']=time.time()-start
 if hit:
  head,h,col,tok,P,roots,C,hist=hit
  O=dict(status='FINITE_PHYSICAL_LITERAL_WITNESS',stats=stats,word=[x['packet']for x in hist],names=[x['name']for x in hist],entry_residual_root_count=len(roots),entry_residual_roots=roots,entry_total_mass=5+len(roots),beta=sum(x['beta_increment']for x in hist),C=C,final_pose=[*head,h],initial_black_cells=sorted(K|set(roots)),history=hist)
 else:O=dict(status='NO_HIT_WITHIN_STATED_FINITE_SEARCH_NOT_A_THEOREM',stats=stats)
 P=W/'all_input_literal_probe'/f'r{cap}_depth{depth}_beta{goal}.json';P.write_text(json.dumps(O,indent=2)+'\n');print(json.dumps({k:v for k,v in O.items()if k!='history'},indent=2));print(P)
