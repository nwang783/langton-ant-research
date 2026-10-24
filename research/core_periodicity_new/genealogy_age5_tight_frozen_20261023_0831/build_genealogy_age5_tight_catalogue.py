"""Author exact tight-edge catalogue with physical output parity and age4 holes."""
from pathlib import Path
import json
W=Path(__file__).resolve().parent;G=json.loads((W/'chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];A={0:3,1:3,4:3,5:3,6:5,7:5,8:5,9:5};P={0:(0,1),1:(0,1),4:(1,2),5:(1,2),6:(0,3),7:(0,3),8:(0,3),9:(0,3)};phi=[0,5,6,3];edges=[]
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
for h in range(4):
 for parity in range(2):
  for hh in range(4):
   if(parity-1+h-hh)%2:continue
   for a in A:
    n=A[a]+((h-hh-A[a])%4)
    if a in[0,1,4,5]and n==4:n+=4
    for o in G[a]['outputs']:
     dx,dy=rot((o[0]-P[a][0],o[1]-P[a][1]),hh);margin=3*n+phi[h]-phi[hh]-4*dy;assert margin>=0
     if margin==0:edges.append(dict(source=[h,parity],target=[hh,sum(o)%2],packet=a,name=G[a]['name'],output=o,gap=n,displacement=[dx,dy]))
# Independent eight-vertex transitive closure identifies edges on cycles.
R=[[i==j for j in range(8)]for i in range(8)]
for e in edges:R[2*e['source'][0]+e['source'][1]][2*e['target'][0]+e['target'][1]]=True
for k in range(8):
 for i in range(8):
  for j in range(8):R[i][j]|=R[i][k]and R[k][j]
cyclic=[e for e in edges if R[2*e['target'][0]+e['target'][1]][2*e['source'][0]+e['source'][1]]]
assert len(cyclic)==18 and {tuple(e['source'])for e in cyclic}=={(0,1),(2,0),(3,0)}
cycles=[]
for a in[6,7,8,9]:
 for o in[[0,0],[2,0]]:
  cycles.append(dict(middle_packet=a,middle_name=G[a]['name'],middle_output=o,net_C_gap=12,net_displacement=[1-o[0],9],transfers=[dict(source_packet=5,target_packet=a,target_pose=[2,8,2],protected_output=[2,5],exact_C_gap=6),dict(source_packet=a,target_packet=1,target_pose=[o[0]-1,0,1],protected_output=o,exact_C_gap=3),dict(source_packet=1,target_packet=5,target_pose=[1,2,1],protected_output=[3,1],exact_C_gap=3)]))
two=[]
for a in[6,7,8,9]:
 for o in[[0,0],[2,0]]:
  two.append(dict(middle_packet=a,middle_name=G[a]['name'],middle_output=o,net_C_gap=8,net_displacement=[-o[0],6],transfers=[dict(source_packet=1,target_packet=a,target_pose=[6,1,3],protected_output=[3,1],exact_C_gap=5),dict(source_packet=a,target_packet=1,target_pose=[o[0]-1,0,1],protected_output=o,exact_C_gap=3)]))
O=dict(status='AUTHOR_TIGHT_CATALOGUE_NOT_PHYSICAL_REALIZABILITY',scope='All zero-margin edges of the age5+selected age4-hole+physical output parity relaxation. No complete HB, count6 proof, shared word or live ledger is asserted.',state_semantics='[birth_heading, parity of producer output local x+y]',potential=phi,total_tight_edges=len(edges),cyclic_edges=cyclic,transient_tight_edges=[e for e in edges if e not in cyclic],eight_three_generation_cycle_variants=cycles,eight_two_generation_cycle_variants=two)
p=W/'chronology_dcuv/genealogy_age5_tight_catalogue.json';p.write_text(json.dumps(O,indent=2)+'\n');print(dict(file=str(p),tight_edges=len(edges),cyclic_edges=len(cyclic),cycles=len(cycles)))
