"""Discovery of affine rail-fringe transitions, not an all-n certificate.
Canonical states retain both finite fringes and a long period-two column run.
Identifying different run lengths is a conjectural abstraction until replayed
at other lengths and certified by complete event histories.
"""
import sys,json,time,collections,pathlib
HERE=pathlib.Path(__file__).resolve().parent
LO=int(sys.argv[1]) if len(sys.argv)>1 else -3
HI=int(sys.argv[2]) if len(sys.argv)>2 else 8
H=HI-LO+1; N=int(sys.argv[5]) if len(sys.argv)>5 else 64;FRINGE=12;MAXSTATES=int(sys.argv[3]) if len(sys.argv)>3 else 30000
SEEDROWS=tuple(map(int,sys.argv[4].split(','))) if len(sys.argv)>4 else (-1,)
FULL=(1<<H)-1; PORTS=[y-LO for y in range(LO,HI+1) if y%2==0]
def visit(mask,y):
 x=0;dx=1;t=0;mx=0
 while x>=0:
  i=x*H+y;a=1-2*((mask>>i)&1);mask^=1<<i;z=y-dx*a;t+=1
  if not 0<=z<H:return 'VERTICAL',mask,z,t,mx
  j=x*H+z;b=1-2*((mask>>j)&1);mask^=1<<j;dx=-dx*a*b;y=z;x+=dx;t+=1;mx=max(mx,x)
  if x>=512 or t>=200000:return 'UNKNOWN',mask,y,t,mx
 return 'LEFT',mask,y,t,mx

def canon(B):
 cols=[]
 while B:cols.append(B&FULL);B>>=H
 if len(cols)<24:return None
 runs=[];i=0
 while i+1<len(cols):
  j=i+2
  while j<len(cols) and cols[j]==cols[j-2]:j+=1
  z=(j-i)//2*2
  if z>=24 and i<=FRINGE and len(cols)-(i+z)<=FRINGE:runs.append((z,-i,i))
  i=max(i+1,j-2)
 if not runs:return None
 length,_,i=max(runs);key=(tuple(cols[:i]),tuple(cols[i:i+2]),tuple(cols[i+length:]))
 return key,length//2
B=sum(1<<(x*H+(y-LO)) for x in range(N) for y in SEEDROWS);k,n=canon(B)
keys={k:0};states=[(B,k,n,-1,None)];q=collections.deque([0]);edges=[];outcomes=collections.Counter();cand=[];st=time.time()
while q and len(states)<MAXSTATES:
 v=q.popleft();B,k,n,par,port=states[v]
 for y in PORTS:
  status,C,z,t,mx=visit(B,y);outcomes[status]+=1
  if status!='LEFT':continue
  cr=canon(C)
  if cr is None:outcomes['UNREPRESENTED']+=1;continue
  key,m=cr;w=keys.get(key)
  if w is None:
   w=len(states);keys[key]=w;states.append((C,key,m,v,y+LO));q.append(w)
  edges.append((v,w,y+LO,z+LO,m-n,t,mx))
  # Check real root-tree ancestors only; this preserves a literal candidate.
  a=v;controls=[y+LO]
  while a>=0:
   if states[a][1]==key:
    delta=m-states[a][2]
    if delta>=0:
     assert delta>0,('literal bounded field cycle',a,v,controls)
     rec=dict(ancestor=a,from_vertex=v,delta_pairs=delta,ports=list(reversed(controls)),initial_hex=hex(states[a][0]),final_hex=hex(C),initial_pairs=states[a][2],final_pairs=m)
     cand.append(rec);print('CANDIDATE',rec,flush=True)
    break
   _,_,_,pa,pp=states[a]
   if pa>=0:controls.append(pp)
   a=pa
 if len(states)%1000<5:print('progress',len(states),len(q),len(edges),dict(outcomes),flush=True)
out=dict(lo=LO,hi=HI,seed_rows=SEEDROWS,initial_rail=N,fringe_bound=FRINGE,states=len(states),edges=len(edges),frontier=len(q),outcomes=dict(outcomes),candidates=cand,seconds=time.time()-st,graph_edges=edges,state_records=[dict(key=k,pairs=n,parent=p,port=port,board_hex=hex(B)) for B,k,n,p,port in states])
(HERE/(f'rail_transducer_{LO}_{HI}_n{N}_'+('_'.join(map(str,SEEDROWS)))+'.json')).write_text(json.dumps(out));print('DONE',{k:v for k,v in out.items() if k not in ('state_records','graph_edges','candidates')},'candidates',len(cand),flush=True)
