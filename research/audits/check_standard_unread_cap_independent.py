from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];p=SELF.parent/'check_serial_bridge_archive_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('# Fixed local masks')[0],ns)
ends,graph,component,connected,step,wvertex=[ns[k]for k in('ends','graph','component','connected','step','wvertex')]
D=ROOT/'standard_unread_cap_2026-10-23';J=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());H=J['word'];I={complex(*q)for q in J['seed']};dr=-2-2j;assert len(I)==13 and J['heading']==3 and J['drift']==[-2,-2]
F={-2+1j,-1+1j,1j,1+1j,1,1-1j,2-2j,2-3j,1-4j,1-5j,1-6j}
P={-4-1j,-3-1j,-3,-2-1j};Q={-1-8j,-1-7j,-1-6j,-7j};R={-1-2j,-3j,-2j};S={0j};U={-3-1j,-3,-2};V={-2-4j,-2-3j,-1-5j,-1-3j,-1-2j,-6j,-5j,-4j,-3j,1-3j,1-2j,1,2-1j,2}
shift=lambda X,n:{q+n*dr for q in X}
B=set(I);p=0j;h=3;trace=[];A18=None
for i,ch in enumerate(H):
 if i==18:A18=set(B);assert(p,h,ch,H[17])==(-1-1j,1,'L','L')
 assert('L'if p in B else'R')==ch;trace.append((p,h,ch));p,h,ch2=step(B,p,h);assert ch2==ch
assert(p,h)==(dr,3)and shift(I,1)<=B
out=B-shift(I,1);assert out==P|Q|R|S and len(out)==12 and not I&F
# Complete infinite geometric occurrences of one fixed physical cell.
def occ(q):
 ans=[]
 for i,(p,h,ch)in enumerate(trace):
  z=(q-p)/dr
  if z.imag==0 and z.real==int(z.real):ans.append((int(z.real),i,ch))
 return ans
assert all(not any(k>=1 for k,i,ch in occ(q))for q in out)
assert all(not any(k>=0 for k,i,ch in occ(q))for q in F)
assert A18-{-1-1j}==U|(V-shift(R,-1))and shift(R,-1)<=V
# Author z parity1 corresponds to doubled-vertex-sum lattice0; w parity0 ->2.
zlat,wlat=0,2
verts=lambda X:set(graph(X,zlat))
def isconn(X):return component(X,zlat,next(iter(verts(X))))[1]==X
for X in(P,Q,U,V):assert isconn(X)
patch=shift(P,1)|R|shift(S,1);remaining=set(patch);patchparts=[]
while remaining:
 e=next(iter(remaining));vs,es=component(patch,zlat,ends(e,zlat)[0]);remaining-=es;assert vs&verts(P);patchparts.append(len(es))
assert verts(Q)&verts(shift(Q,1))and verts(shift(U,1))&verts(P)and verts(shift(V,1))&verts(Q)
q=-1-1j;ep=ends(q,zlat);assert any(a in verts(U)and b in verts(V)for a,b in(ep,ep[::-1]))
bases=dict(P=P,Q=Q,R=R,S=S,U=U,V=V)
CU=[('P',(0,0),(1,-1)),('R',(0,0),(1,-2)),('S',(0,1),(1,-1)),('U',(1,0),(1,0))];CV=[('Q',(0,0),(1,-1)),('V',(1,0),(1,0))];ISO=[('S',(0,0),(0,0))]
def minus(a,b):return(a[0]-b[0],a[1]-b[1])
def ge(dom,a):
 if dom is None:return None
 lo,hi=dom;A,B=a
 if A==0:return dom if B>=0 else None
 if A>0:lo=max(lo,-(B//A))
 else:hi=B//(-A)if hi is None else min(hi,B//(-A))
 return None if hi is not None and lo>hi else(lo,hi)
collisions=[]
for AA,BB in((CU,CV),(CU,ISO),(CV,ISO)):
 for a,al,ah in AA:
  for b,bl,bh in BB:
   offsets=set()
   for x in verts(bases[a]):
    for y in verts(bases[b]):
     f=(x-y)/(2*dr)
     if f.imag==0 and f.real==int(f.real):offsets.add(int(f.real))
   for s in offsets:
    dom=(1,None)
    for ine in(minus(ah,al),minus(bh,bl),minus((bh[0],bh[1]-s),al),minus(ah,(bl[0],bl[1]-s))):dom=ge(dom,ine)
    assert dom is None;collisions.append((a,b,s))
assert isconn(F)and -5+1j in verts(F)&verts(P)and 1-13j in verts(F)&verts(Q)
fg=graph(F,zlat);assert len(fg)==12 and sorted(len(es)for es in fg.values())==[1,1]+[2]*10
ports={-1-1j,-1,-1j,0};leaf=-1-1j;assert all(leaf in ends(q,wlat)for q in ports)
last={}
for q in ports:
 os=[(104*k+i,k,i,ch)for k,i,ch in occ(q)if 104*k+i<18];a=max(os);assert a[1]==0;last[q]=a
assert last[-1-1j][2:]==(10,'R')and{last[q][2:]for q in ports-{-1-1j}}=={(11,'L'),(9,'L'),(0,'L')}
# Distinct all-n edge counts are additionally checked at fixed n; analytic exhaustion is above.
for n in(1,2,3,7,19):
 cu=set().union(*(shift(P,j)for j in range(n)),*(shift(R,j)for j in range(n-1)),*(shift(S,j)for j in range(1,n)),shift(U,n));cv=set().union(*(shift(Q,j)for j in range(n)),shift(V,n))
 full=shift(A18,n)|set().union(*(shift(out,j)for j in range(n)))
 assert full-{q+n*dr for q in[-1-1j]}==cu|cv|S and len(cu)==8*n-1 and len(cv)==4*n+14
 assert isconn(cu)and isconn(cv)and not verts(cu)&verts(cv)and not(verts(cu)|verts(cv))&verts(S)
# Complete24-cell trajectory, including every passive cap and old output, twelve periods.
B=I|F;p=0j;h=3;birth={q:-1 for q in B};tests=[]
for t in range(104*12):
 n,i=divmod(t,104);ch=H[i];assert('L'if p in B else'R')==ch
 if i==18 and n>=1:
  assert(p,h)==(-1-1j+n*dr,1)and birth[p]==104*n+10
  a,b=ends(p,zlat);assert connected(B-{p},zlat,a,b)and not connected(B-F-{p},zlat,a,b)
  assert not connected(B-{p},wlat,*ends(p,wlat))and len(graph(B,wlat)[leaf+2*n*dr])==1
  assert all(birth[q]==-1 for q in F);tests.append({'n':n,'time':t,'age':8,'support_age':t+1,'mass':len(B)})
 if ch=='L':del birth[p]
 else:birth[p]=t
 p,h,ch2=step(B,p,h);assert ch2==ch
sha=hashlib.sha256((D/'PROOF.md').read_bytes()).hexdigest();assert sha=='3337fa1adc69e63c2394ac1b704363fde65e755aeff140d7fa5d07ca93b940b3'
o={'status':'PASS fixed24-cell standard orbit with recurrent indispensable original z-cycle support','note_sha256':sha,'initial_mass':24,'permanent_output_cells':12,'unread_cap_cells':11,'all_parameter_cross_component_collision_exclusions':len(collisions),'growth_patch_component_sizes':patchparts,'full_board_control_reads':1248,'controls':tests,'analytic':['One complete104 replay leaves exactly translated13-cell input plus12-cell output. Every output has no future-period geometric read, and every cap cell has no read at any nonnegative period. These exact104-slot integer equations prove full-board H forever by induction, including all permanent output and all11 cap cells.','At phase18, subtracting the current edge gives the exact algebraic partition into two growing rails plus isolated S0. Local growth patches prove both rails connected. Every possible cross-family vertex-collision offset is solved against its full affine index intervals; all integer n>=1 domains are empty. Thus the components are complete and no remote younger bypass is omitted.','The unread original11-edge cap is a simple z path joining P0 and Q0, so it connects the two rails after deleting q. Removing all cap edges disconnects them. Therefore every z cycle through q contains an original cap lifetime, and all lifetimes have birth>=-1; the intrinsic maximin support birth is exactly-1, not merely bounded by an unnecessary old witness.','The four w ports at the designated endpoint have exact current-period last reads R10,L11,L9,L0. Hence q is a full-graph w leaf/bridge, its token age is8, and phase17 L makes phase18 a proper r0 ordinary block. These are z-only erasures, not w-exceptional renewals.','For every n>=1 in ONE fixed24-cell seed, the support age is104n+19 while the token age stays8 and the trajectory is standard from time0. This refutes a necessary bounded-age support condition for all dual erasures lumped together, not the oriented w-renewal theorem or standard capture.'],'scope':'Exact standard104 phase18 z-only mechanism with one fixed unread cap. No classification of arbitrary standard phases, w-exceptional self-feeding or arbitrary seeds.'}
SELF.with_suffix('.json').write_text(json.dumps(o,indent=2)+'\n');print(o['status']);print('collision checks',len(collisions))
