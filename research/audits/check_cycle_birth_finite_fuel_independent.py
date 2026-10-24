from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'global_cycle_birth_2026-10-23';dirs=(1j,1,-1j,-1);stats=Counter();maxwait=0

def wvertex(p,h):return 2*p+(1-1j)*(-1j)**h

def ends(q,lattice):
 for e in(1+1j,1-1j):
  a,b=2*q-e,2*q+e
  if int(a.real+a.imag)%4==lattice:return a,b
 raise AssertionError

def graph(B,lattice):
 g={}
 for q in B:
  a,b=ends(q,lattice);g.setdefault(a,[]).append((b,q));g.setdefault(b,[]).append((a,q))
 return g

def component(B,lattice,v):
 g=graph(B,lattice);seen={v};todo=[v];edges=set()
 while todo:
  v=todo.pop()
  for u,q in g.get(v,()):
   edges.add(q)
   if u not in seen:seen.add(u);todo.append(u)
 return seen,edges

def rank(B,lattice):
 g=graph(B,lattice);todo=set(g);nc=0
 while todo:
  nc+=1;start=next(iter(todo));seen,_=component(B,lattice,start);todo-=seen
 return len(B)-len(g)+nc

def connected(B,lattice,a,b):return b in component(B,lattice,a)[0]

def isbirth(B,p,lattice=None):
 assert p not in B
 return any(connected(B,k,*ends(p,k))for k in((0,2)if lattice is None else(lattice,)))

def step(B,p,h):
 ch='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;return p+dirs[h],h,ch

def check(B0,p0,h0,weaker=False):
 global maxwait
 B=set(B0);p=p0;h=h0;lattice=int(wvertex(p,h).real+wvertex(p,h).imag)%4;m=len(B);beta=rank(B,lattice);bound=2*(m+1)*(3**(beta+1)-1);r=0;C=component(B,lattice,wvertex(p,h))[1];blockmass=m;epochmass=m;epochbridges=0;nonbridge=0;blocks=0;t=0
 while True:
  assert int(wvertex(p,h).real+wvertex(p,h).imag)%4==lattice
  if p not in B and((r==3 or isbirth(B,p,lattice))if weaker else isbirth(B,p)):
   stats['weak_cases'if weaker else'cases']+=1;maxwait=max(maxwait,t+1);assert t+1<=bound and nonbridge<=beta
   assert t<=4*blocks+3 and blocks<=(m+1)*(3**(nonbridge+1)-1)//2-1
   return t+1
  assert t<10000,'fixed control unexpectedly exceeds safety limit, not a proof'
  if p not in B:
   beforew=wvertex(p,h);assert not isbirth(B,p,lattice);p,h,ch=step(B,p,h);r+=1;assert r<=3 and wvertex(p,h)==beforew
  else:
   q=p;oldw=wvertex(p,h);isnon=connected(B-{q},lattice,*ends(q,lattice));p,h,ch=step(B,p,h);blocks+=1;assert q in C and len(B)-blockmass==r-1
   assert{oldw,wvertex(p,h)}==set(ends(q,lattice))
   if not isnon:
    actual=component(B,lattice,wvertex(p,h))[1];expected=component(C-{q},lattice,wvertex(p,h))[1];assert actual==expected and len(actual)<=len(C)-1;epochbridges+=1;assert epochbridges<=epochmass;stats['exact_bridge_inheritance']+=1
   else:
    nonbridge+=1;assert len(B)<=3*epochmass+2;epochmass=len(B);epochbridges=0;stats['nonbridge_renewals']+=1
   C=component(B,lattice,wvertex(p,h))[1];blockmass=len(B);r=0
  assert rank(B,lattice)==beta-nonbridge;t+=1
cells=[complex(x,y)for x in range(-1,2)for y in range(-1,2)]
for bits in range(512):
 B={q for i,q in enumerate(cells)if bits>>i&1}
 for h in range(4):check(B,0j,h);check(B,0j,h,True)
 # Every 16th mask retains a distant cyclic passive component in GLOBAL beta.
 if bits%16==0:
  B|={100+100j,101+100j,100+101j,101+101j}
  for h in range(4):check(B,0j,h)
rods=[]
for r in(1,2,3,7,16,31,64):
 B={complex(x,0)for x in range(2*r)};p=0j;h=1
 for t in range(4*r):
  assert rank(B,0)==rank(B,2)==0
  assert('L'if p in B else'R')=='LRRL'[t%4]
  if p not in B:assert not isbirth(B,p)
  p,h,ch=step(B,p,h);stats['rod_fine_steps']+=1
 assert(B,p,h)==({complex(x,1)for x in range(2*r)},2*r,1)
 assert rank(B,0)==rank(B,2)==0
 assert check({complex(x,0)for x in range(2*r)},0j,1)==4*r+4;rods.append(r)
# Four literal R turns on arbitrary pose close the same z vertex after the
# fourth edge, while all four addressed w ports are distinct.
p=0j;h=0;z=lambda p,h:2*p+(-1-1j)*(-1j)**h;Z=[z(p,h)];ports=[]
for t in range(4):
 ports.append(p);h=(h+1)%4;p+=dirs[h];Z.append(z(p,h))
assert len(set(ports))==4 and len(set(Z[:-1]))==4 and Z[-1]==Z[0]
std=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];tens={(std*2)[i:i+10]for i in range(104)};bad=[('LRRL'*4)[i:i+10]for i in range(4)];assert all(w not in tens for w in bad)
note=D/'cycle_birth_or_finite_fuel.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='7bd38a60ed9d0f104d44503a4ac1de09ab5d6afd89069f3203483da1393f8c42'
out={'status':'PASS global cycle-birth-or-finite-fuel theorem and exact active-edge inheritance','note_sha256':sha,'counts':dict(stats),'maximum_control_wait':maxwait,'rods':rods,'all_four_transport_ten_words_bad':bad,'analytic':['Four consecutive R insert four distinct edges around a z unit cycle, so an interval with no birth in either graph has R runs of length<=3. During a shorter R prefix w is fixed and addresses distinct ports; the departing L edge is an old block-entry edge.','Each no-birth R attaches a different formerly disconnected w component through a bridge. Those additions cannot alter the old L-edge bridge status. If L is a bridge, its far active edge set is EXACTLY the far component of the original entry component minus that edge; all newly attached components remain at the departed w.','A nonbridge L may retain/import those passive components but lowers TOTAL w-cycle rank by1. This global rank includes initially passive cycles, so at most beta renewals occur and no archive is discarded.','For bridge epoch j, n_j<=M_j by strict active-edge loss. Complete mass change per block<=2 gives M_(j+1)<=3M_j+2 and M_j<=(m+1)3^j-1. Thus blocks<=((m+1)(3^(h+1)-1))/2-1. With <=3 terminal R, T<=2(m+1)(3^(beta+1)-1)-1. Empty beta0/m0 yields T<=3, with first birth at fourth update.','Apply the finite waiting bound after any proposed last birth to force infinitely many births. The signed hull theorem places every birth inside an existing rectangle hull; neither frequency nor birth count is bounded by original mass.','The same proof needs only no wholly-contained RRRR and no w-black birth; arbitrary non-RRRR z births do not affect the active w accounting. This is an analytic strengthening, not silently edited into the frozen author note.','At every rod fine cut, two zigzag row paths meet in at most one vertex in either lattice because the written and unwritten intervals satisfy a<=b. Both graphs are forests, all cuts bi-exterior, and LRRL transport remains nonstandard for arbitrary r supplied by2r initial blacks.'],'scope':'Arbitrary actual finite-support intervals. A global reconnection recurrence theorem, not standard capture, mass-only total complexity, an original-fuel rank or a finite-summary map.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(stats,maxwait)
