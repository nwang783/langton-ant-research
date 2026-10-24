from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];S=ROOT/'spatial_cursor_2026-10-23';D=(1j,1,-1j,-1);p=0j;h=0;B=set();states=[];reads=[]
xy=lambda z:(int(z.real),int(z.imag))
for tick in range(18):
 states.append((set(B),p,h))
 if tick==17:break
 c='L'if p in B else'R';reads.append((p,c));B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=D[h]
assert states[9][1:]==states[17][1:]==(-1+0j,3)
assert ''.join(c for q,c in reads[9:17])=='LRRRRLLL'
E=states[9][0]^states[17][0];L={-2-1j,-2+0j};R={-1j,0j};assert E==L|R
f=lambda n:3**abs(n)-1
J=lambda n,e:f(n)//2 if n*e>=0 else -3*f(n)//2
def edges(q):
 x,y=xy(q);v=1+1j if(x+y)%2==0 else 1-1j;return{2*q-v,2*q+v}
assert not set.union(*(edges(q)for q in L))&set.union(*(edges(q)for q in R))
rest={q for q,c in reads[9:17]}-E;assert rest=={-1-1j,-1+0j}
verts=set();active=states[9][1]+(-1-1j)/2*((-1j)**states[9][2]);verts.add(2*active)
for q,c in reads[9:17]:
 ed=edges(q);assert ed&verts;verts|=ed
for sign in(1,-1):
 z=lambda q:int(q.real+sign*q.imag)
 norm=lambda cells:min(sum(f(z(q)-c)for q in cells)for c in range(min(map(z,cells)),max(map(z,cells))+1))
 assert norm(L)==norm(R)==2 and norm(E)==12
centers={q:-2 for q in L|rest}|{q:-1 for q in R};debt=[]
for tick in range(9,17):
 field,p,h=states[tick];nfield,np,nh=states[tick+1];c=centers[p];j0=J(int(p.real+p.imag)-c,1 if h in(0,1)else-1);j1=J(int(np.real+np.imag)-c,1 if nh in(0,1)else-1);debt.append(j1-j0)
assert debt==[3,1,-1,1,-1,1,1,-1]and sum(debt)==4
for h in range(4):
 for turn in(-1,1):
  nh=(h+turn)%4
  for sign in(1,-1):
   arg=int(D[nh].real+sign*D[nh].imag);e=(1 if nh in((0,1)if sign==1 else(1,2))else-1);assert J(arg,e)==1
out=dict(status='PASS exact actual eight-read component countercontrol and cursor port accounting',actual_interval=[9,17],same_pose=[-1,0,3],word='LRRRRLLL',component_norm_sum=4,complete_XOR_norm=12,duration=8,port_debt=debt,total_port_debt=4,singleton_center_head_increment=1,bindings={n:hashlib.sha256((S/n).read_bytes()).hexdigest()for n in ['causal_component_decomposition_countercontrol.md','continuous_cursor_port_debt_lemma.md']},scope='General read-edge connectedness and variable-center telescoping reviewed analytically. No amortized port-debt bound or historical component budget.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
