"""Exact role-potential and initial-edge audit on independently rebuilt graph."""
from pathlib import Path
import hashlib,json
import check_genealogy_saturation_roles_independent as G
F=G.ROOT/'core_periodicity_new/genealogy_role_speed_frozen_20261023_0840'
M=json.loads((F/'manifest.json').read_text())
for f in M['files']:
 assert hashlib.sha256((F/f['file']).read_bytes()).hexdigest()==f['sha256']
assert hashlib.sha256((G.F/'manifest.json').read_bytes()).hexdigest()==hashlib.sha256((F/'role_graph_manifest.json').read_bytes()).hexdigest()
R=json.loads((F/'optimal_speed_root_potential.json').read_text());P=R['P']
assert len(P)==len(G.roles) and all(type(v)is int for v in P)
assert min(P)==0 and max(P)==5 and R['K']==13
# This is G's independently rebuilt set, not the author's serialized edge list.
margin=[2*n+P[u]-P[v]-3*d for u,v,n,d in G.fundamental]
assert min(margin)>=0
first=[]
for i,(a,o,h) in enumerate(G.roles):
 d=int(G.rotation(o-G.anchors[a],h).imag)
 first.append(3*d+P[i])
assert max(first)==13
# A rotated potential is obtained simply by rotating both absolute headings.
for turn in range(4):
 for u,v,n,d in G.fundamental:
  a,z,h=G.roles[u];b,o,hh=G.roles[v]
  ur=G.index[a,z,(h-turn)%4];vr=G.index[b,o,(hh-turn)%4]
  rotated_d=int(G.rotation(o-G.anchors[b],hh-turn).imag)
  assert 3*rotated_d<=2*n+P[ur]-P[vr]
# Construct the attaining cycle from literal roles, not supplied edge IDs.
cycle=[G.index[6,0j,2],G.index[0,2+0j,3],G.index[5,2+5j,0]]
actual=[]
for u,v in zip(cycle,cycle[1:]+cycle[:1]):
 es=[e for e in G.fundamental if e[:2]==(u,v)]
 assert len(es)==1;actual.append(es[0])
assert sum(e[2] for e in actual)==12 and sum(e[3]for e in actual)==8
psi=[3*G.phi[h]+G.longest[i]for i,(a,o,h)in enumerate(G.roles)]
assert all(12*d+1<=9*n+psi[u]-psi[v]for u,v,n,d in G.fundamental)
# Exact algebra: j=3q+t has 2R+2=4q+w[t]. Sum complete blocks.
w=[2*((2*t+13)//3)+2 for t in range(3)];assert w==[10,12,12]
assert sum(w)==34
# Radius dominance reduces to twelve residues; its difference gains one/12 steps.
assert all((2*t+13)//3 <= (3*t+18)//4 for t in range(12))
for j in range(300):
 assert 2*((2*j+13)//3)+2==4*(j//3)+w[j%3]
 k=j;s=sum(2*((2*t+13)//3)+2 for t in range(k+1));q,r=divmod(k+1,3)
 assert s==6*q*q+28*q+4*q*r+[0,10,22][r]
 assert 3*s<=2*(k+1)*(k+16)
out={'status':'PASS exact integer potential, four rotated frames, initial edges, cycle and symbolic residue sum','role_graph_manifest_sha256':hashlib.sha256((G.F/'manifest.json').read_bytes()).hexdigest(),'manifest_sha256':hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest(),'roles':len(P),'fundamental_edges':len(margin),'minimum_margin':min(margin),'first_role_max':max(first),'attaining_cycle':actual,'cycle_C':12,'cycle_dy':8,'radius':'floor((2k+13)/3)','duration':'28(m-5)[6q^2+28q+4qs+[0,10,22][s]]+15k, k+1=3q+s','scope':'Produced-parent ancestry speed and finite-C duration only; no realization of the abstract cycle, total-C bound or confinement.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
