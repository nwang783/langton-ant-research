"""Exact finite-word obstruction for a whole flat flow-two F segment.
No period, drift, width, multiplicity or front scan.
"""
from pathlib import Path
from itertools import product
import json
H='NESW';v={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def ids(h,dr,kind):return[r for r,x in enumerate(h)if(x if kind=='in'else out(h,r))==dr]
base={(0,-1):'WWEE',(0,0):'NSSN',(1,0):'WWEE',(1,1):'NSSN',(2,1):'WWEE'}
D=[]
for n in range(1,5):
 for hs in product('NS',repeat=n):
  h=''.join(hs)
  if len(ids(h,'S','in'))==len(ids(h,'W','out'))==2:
   a=ids(h,'W','out')[0];b=ids(h,'S','in')[1]
   # Literal first-W-to-second-S return has four steps and no intervening D.
   D.append(dict(headings=h,first_W_rank=a,second_S_rank=b,can_return_in_four=b==a+1))
assert {r['headings']for r in D}=={'NNSS','NSSN','SNNS','SSNN'}
assert[r['headings']for r in D if r['can_return_in_four']]==['SSNN']
full=base|{(1,-1):'SSNN',(2,0):'SSNN'}
edges={};openports=[];incomingopen=[]
for p,h in full.items():
 for r in range(len(h)):
  dr=out(h,r);q=(p[0]+v[dr][0],p[1]+v[dr][1]);sr=ids(h,dr,'out');ord=sr.index(r)
  if q not in full:
   openports.append(dict(source=p,rank=r,heading=dr,target=q,outgoing_ordinal=ord+1));continue
  tr=ids(full[q],dr,'in');assert len(sr)==len(tr)
  edges[(p,r)]=(q,tr[ord])
for p,h in full.items():
 for r,dr in enumerate(h):
  q=(p[0]-v[dr][0],p[1]-v[dr][1])
  if q not in full:incomingopen.append(dict(target=p,rank=r,heading=dr,source=q,incoming_ordinal=ids(h,dr,'in').index(r)+1))
# Add unknown E=(2,-1) only as its fixed ordinal boundary ports.
E=(2,-1)
chains=[]
for k in(0,1):
 d=(k+1,k-1);path=[(d,0)];cur=path[0]
 for _ in range(4):cur=edges[cur];path.append(cur)
 assert path[-1]==(d,1)
 chains.append(dict(kind='D firstW to secondS',steps=4,path=[dict(cell=p,rank=r)for p,r in path]))
# E's second N goes to D1's third N arrival, rank3. Follow exactly seven
# named successor events, then its first E arrival is forced by D0.L1.
path=[dict(cell=E,port='second outgoing N')];cur=((2,0),3);path.append(dict(cell=cur[0],rank=cur[1]))
for _ in range(6):
 cur=edges[cur];path.append(dict(cell=cur[0],rank=cur[1]))
assert cur==((1,-1),1)
assert out(full[cur[0]],cur[1])=='E'and len(ids(full[cur[0]],'E','out'))==2 and ids(full[cur[0]],'E','out')[0]==1
path.append(dict(cell=E,port='first incoming E'));assert len(path)==9
assert len(ids(full[(1,-1)],'E','out'))==len(ids(full[(2,0)],'N','in'))==2
chains.append(dict(kind='E secondN to firstE',steps=8,path=path))
obj=dict(scope=__doc__,given_complete_histories=[dict(cell=p,headings=h)for p,h in base.items()],D_candidates=D,forced_D_histories=[dict(cell=p,headings=h)for p,h in full.items()if p not in base],forced_return_chains=chains,all_named_internal_edges=[dict(source=p,source_rank=r,target=q,target_rank=s)for(p,r),(q,s)in edges.items()],all_named_outgoing_open_ports=openports,all_named_incoming_open_ports=incomingopen,unknown_E_port_counts=dict(incoming_E=2,outgoing_N=2),ordinal_collision='First E immediately after second N: source cannot be L(E), so it is R(W); the next read is L(E), producing a third N departure, contradicting count2.',scope_warning='Only this five-corner constant flow2 staircase word is excluded. Other flat states, odd LEFT corners, changing flows, turns, all exterior histories and the general one-use theorem remain open.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS three literal return chains, with open exterior ports retained')
