"""Author exact integer certificate replay; no solver premise."""
from pathlib import Path
import json,sys,hashlib
W=Path(__file__).resolve().parent;src=W/'genealogy_saturation_roles_frozen_20261023_0833/01_graph.json';J=json.loads(src.read_text());Q=json.loads((W/'chronology_dcuv/genealogy_saturation_roles/optimal_speed.json').read_text());R=json.loads((W/'chronology_dcuv/genealogy_saturation_roles/optimal_speed_root_potential.json').read_text());roles=J['roles'];E=J['all_fundamental_edges'];P=R['P'];K=R['K'];assert K==13 and len(P)==len(roles)and min(P)==0
assert Q['rho_numerator']==2 and Q['rho_denominator']==3 and Q['source_sha256']==hashlib.sha256(src.read_bytes()).hexdigest()
assert all(3*d<=2*n+P[u]-P[v]for u,v,n,d in E)
cy=Q['attaining_cycle_edge_ids'];assert cy
for i,j in zip(cy,cy[1:]+cy[:1]):assert E[i][1]==E[j][0]
assert sum(E[i][3]for i in cy)*3==sum(E[i][2]for i in cy)*2
anchors={int(a):v[0]for a,v in J['selected_anchors'].items()}
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
first=[]
for i,(a,o,h)in enumerate(roles):
 p=anchors[a];d=rot((o[0]-p[0],o[1]-p[1]),h)[1];v=3*d+P[i];assert v<=K;first.append(v)
# The independent rank-style per-generation penalty is also purely integer.
rank=J['topological_rank'];phi=J['potential_plus_y'];psi=[3*phi[h]+rank[i]for i,(a,o,h)in enumerate(roles)]
assert all(12*d+1<=9*n+psi[u]-psi[v]for u,v,n,d in E)
s=0
for k in range(10001):
 r=(2*k+13)//3;assert r<=(3*k+18)//4
 s+=2*r+2;q,t=divmod(k+1,3);formula=6*q*q+28*q+4*q*t+[0,10,22][t];assert formula==s
O=dict(status='AUTHOR_EXACT_ALL_EDGE_AND_ATTAINING_CYCLE_PASS_NOT_INDEPENDENT',source_file=str(src),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),roles=len(roles),edges=len(E),speed=[2,3],root_constant=K,root_potential_min=min(P),root_potential_max=max(P),first_role_max=max(first),integer_all_edge_min_margin=min(2*n+P[u]-P[v]-3*d for u,v,n,d in E),critical_cycle=cy,critical_cycle_C=sum(E[i][2]for i in cy),critical_cycle_dy=sum(E[i][3]for i in cy),root_radius='floor((2*k+13)/3)',duration_exact='28*(m-5)*(6*q^2+28*q+4*q*s+[0,10,22][s])+15*k; q=floor((k+1)/3),s=(k+1)mod3',duration_coarse='(56/3)*(m-5)*(k+1)*(k+16)+15*k',rank_penalty='12*DeltaY+N <=9*DeltaC+Psi(start)-Psi(end)',checked_k=10001)
(W/'chronology_dcuv/genealogy_saturation_roles/optimal_speed.check.json').write_text(json.dumps(O,indent=2)+'\n');print(json.dumps(O,indent=2))
