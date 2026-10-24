"""One fixed24-cell board: H forever, unbounded OLD z-cycle support.
All-period proof: exact permanent-output induction plus affine component partitions.
No finite replay supplies the infinite quantifier.
"""
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction
from collections import deque
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'renewal_input_placement_2026-10-23'))
from build_forced_input_cycles import deterministic_trace,occurrences,endpoints,graph,component,vertices,step
SOURCE=ROOT/'recovered_bundle/ant_global/root/standard.json'
J=json.loads(SOURCE.read_text());H=J['word'];I={tuple(z)for z in J['seed']};d=tuple(J['drift'])
F={(-2,1),(-1,1),(0,1),(1,1),(1,0),(1,-1),(2,-2),(2,-3),(1,-4),(1,-5),(1,-6)}
P={(-4,-1),(-3,-1),(-3,0),(-2,-1)}
Q={(-1,-8),(-1,-7),(-1,-6),(0,-7)}
R={(-1,-2),(0,-3),(0,-2)}
S={(0,0)}
U={(-3,-1),(-3,0),(-2,0)}
V={(-2,-4),(-2,-3),(-1,-5),(-1,-3),(-1,-2),(0,-6),(0,-5),(0,-4),(0,-3),(1,-3),(1,-2),(1,0),(2,-1),(2,0)}
BASES=dict(P=P,Q=Q,R=R,S=S,U=U,V=V)
def sh(E,j):return{(x+d[0]*j,y+d[1]*j)for x,y in E}
def affine(a,n):return a[0]*n+a[1]
def diff(a,b):return[a[0]-b[0],a[1]-b[1]]
def impose(domain,a):
 lo,hi=domain;A,B=a
 if A==0:return None if B<0 else domain
 x=Fraction(-B,A)
 if A>0:lo=max(lo,-((-x.numerator)//x.denominator))
 else:hi=x.numerator//x.denominator if hi is None else min(hi,x.numerator//x.denominator)
 return None if hi is not None and lo>hi else(lo,hi)
def collision_offsets(X,Y,k=1):
 ans=set();dd=(2*d[0],2*d[1])
 for u in vertices(X,k):
  for v in vertices(Y,k):
   z=(u[0]-v[0],u[1]-v[1])
   if z[0]*dd[1]!=z[1]*dd[0]or z[0]%dd[0]:continue
   ans.add(z[0]//dd[0])
 return sorted(ans)
def family(base,lo,hi):return{'base':base,'lo':lo,'hi':hi}
CU=[family('P',[0,0],[1,-1]),family('R',[0,0],[1,-2]),family('S',[0,1],[1,-1]),family('U',[1,0],[1,0])]
CV=[family('Q',[0,0],[1,-1]),family('V',[1,0],[1,0])]
ISO=[family('S',[0,0],[0,0])]
def collision_domain(f,g,offset):
 # j_g-j_f=offset. Both index intervals must be nonempty and overlap after translation.
 dom=(1,None)
 inequalities=[diff(f['hi'],f['lo']),diff(g['hi'],g['lo']),diff([g['hi'][0],g['hi'][1]-offset],f['lo']),diff(f['hi'],[g['lo'][0],g['lo'][1]-offset])]
 for a in inequalities:
  dom=impose(dom,a)
  if dom is None:break
 return dom

def all_connected(E,k=1):return component(E,k,next(iter(vertices(E,k))))==E

def main():
 assert len(H)==104 and len(I)==13 and len(F)==11 and not I&F and d==(-2,-2)and J['heading']==3
 tr,end,eh=deterministic_trace(H,(0,0),3);assert end==d and eh==3
 B=set(I);p=(0,0);h=3;A18=None
 for i,c in enumerate(H):
  assert c==('L'if p in B else'R')
  if i==18:A18=set(B);assert p==(-1,-1)and h==1 and c==H[i-1]=='L'
  p,h=step(B,p,h)
 assert sh(I,1)<=B
 D=B-sh(I,1);assert D==P|Q|R|S and sum(map(len,(P,Q,R,S)))==12
 # Permanent-output induction: D is never read in any FUTURE period.
 permanent=[]
 for q in sorted(D):
  occ=occurrences(q,tr,d);assert not any(z['copy_offset']>=1 for z in occ)
  permanent.append({'cell':q,'complete_occurrences':occ})
 unread=[]
 for q in sorted(F):
  occ=occurrences(q,tr,d);assert not any(z['copy_offset']>=0 for z in occ)
  unread.append({'cell':q,'complete_occurrences':occ})
 # Exact symbolic partition B_n,18-q_n = CU(n) disjoint CV(n) disjoint S0.
 q=(-1,-1);assert A18-{q}==U|(V-sh(R,-1))
 assert sh(R,-1)<=V and not U&V and not U&sh(R,-1)
 partitions=[]
 for left,right in[(CU,CV),(CU,ISO),(CV,ISO)]:
  for f in left:
   for g in right:
    offsets=collision_offsets(BASES[f['base']],BASES[g['base']]);checks=[]
    for a in offsets:
     dom=collision_domain(f,g,a);assert dom is None,(f,g,a,dom)
     checks.append({'index_offset':a,'collision_N_domain':None})
    partitions.append({'left':f,'right':g,'all_possible_vertex_index_offsets':offsets,'checks':checks})
 # Connectivity of the two exact components, by finite gluing valid for every n>=1.
 assert all_connected(P)and all_connected(Q)and all_connected(U)and all_connected(V)
 patch=sh(P,1)|R|sh(S,1);G=graph(patch,1);seen=set();patch_components=[]
 for v in G:
  if v in seen:continue
  C=component(patch,1,v);vs=vertices(C,1);seen|=vs;touch=vs&vertices(P,1);assert touch
  patch_components.append({'edges':sorted(C),'touches_previous_P_vertices':sorted(touch)})
 assert vertices(Q,1)&vertices(sh(Q,1),1)
 assert vertices(sh(U,1),1)&vertices(P,1)
 assert vertices(sh(V,1),1)&vertices(Q,1)
 u,v=endpoints(q,1);assert u in vertices(U,1)and v in vertices(V,1)
 # F gives an unread, all-original connection between P0 and Q0.
 fs=(-5,1);ft=(1,-13);assert fs in vertices(P,1)and ft in vertices(Q,1)
 assert F==component(F,1,fs)and ft in vertices(F,1)
 # q is w-leaf at this phase: all other ports have just been read L.
 leaf=(-1,-1);ports={(-1,-1),(-1,0),(0,-1),(0,0)}
 assert {z for z in ports if leaf in endpoints(z,0)}==ports
 port_reads=[]
 for z in sorted(ports):
  occ=occurrences(z,tr,d);prev=max([o for o in occ if o['relative_time']<18],key=lambda o:o['relative_time'])
  assert prev['copy_offset']==0
  if z==q:assert prev['turn']=='R'and prev['slot']==10
  else:assert prev['turn']=='L'
  port_reads.append({'cell':z,'last_before18':prev,'complete_occurrences':occ})
 # Small literal full-field controls are separate from the infinite certificate.
 controls=[];B=I|F;p=(0,0);h=3;birth={q:-1 for q in B};t=0
 from check_young_token_old_cycle_support import widest_cycle_path
 for n in range(8):
  for i,c in enumerate(H):
   assert c==('L'if p in B else'R')
   if i==18 and n>=1:
    E=component(B-{p}-F,1,endpoints(p,1)[0]);assert endpoints(p,1)[1]not in vertices(E,1)
    beta,path=widest_cycle_path(B,p,1,birth,t);assert beta==-1 and birth[p]==104*n+10
    assert len(graph(B,0)[(-1-4*n,-1-4*n)])==1
    controls.append({'period':n,'global_time':t,'consumed_age':t-birth[p],'cycle_bottleneck_birth':beta,'indispensable_support_age':t-beta,'cycle_length':len(path)+1,'full_mass':len(B)})
   if c=='R':birth[p]=t
   else:del birth[p]
   p,h=step(B,p,h);t+=1
 out={'status':'PASS all-period infinite-standard legality, exact two-rail component separation and original z-support necessity','source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'initial_seed':sorted(I|F),'original_mass':24,'standard_word':H,'heading':3,'drift':d,'target_period_domain':'all integers n>=1','target_phase':18,'target_pose':[[-2,-1],[-2,-1],1],'target_global_time':[104,18],'target_R_birth':[104,10],'consumed_lifetime_age':8,'intrinsic_z_cycle_bottleneck_birth':-1,'indispensable_z_support_age':[104,19],'w_bridge_reason':'one endpoint is an exact degree-one leaf at every target; proper r0 L','minimal_source_seed':sorted(I),'unread_cap':sorted(F),'permanent_output':sorted(D),'permanent_read_certificates':permanent,'unread_cap_certificates':unread,'component_bases':{k:sorted(v)for k,v in BASES.items()},'CU_families':CU,'CV_families':CV,'isolated_families':ISO,'cross_component_collision_certificates':partitions,'A_growth_patch_components':patch_components,'w_leaf_read_certificates':port_reads,'finite_full_board_controls':controls}
 (OUT/'standard_unread_cap_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if k in('status','original_mass','target_period_domain','target_phase','target_global_time','target_R_birth','consumed_lifetime_age','intrinsic_z_cycle_bottleneck_birth','indispensable_z_support_age','finite_full_board_controls')},indent=2))
if __name__=='__main__':main()
