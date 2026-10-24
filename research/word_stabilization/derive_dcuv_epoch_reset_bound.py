from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];P=R/'core_periodicity_new/chronology_dcuv';G=json.loads((P/'literal_residual_geometry.json').read_text())['geometry'];v=json.loads((R/'word_stabilization/dcv_free_direction_family102.json').read_text())['values'];rot=lambda z,h:[z,(z[1],-z[0]),(-z[0],-z[1]),(-z[1],z[0])][h%4];L=lambda z:z[0]+3*z[1];a=[L(rot((-1,1),h))+v[f'c{h}']for h in range(4)];terms=[];prefix=[]
for i in [7,8,9]:
 g=G[i]
 for h in range(4):
  e=g['endpoint'];terms.append([2*L(rot(e[:2],h))+a[(h+e[2])%4]-a[h],i,h,'core'])
  for z in g['outputs']:terms.append([2*L(rot(z,h))+60-a[h],i,h,z])
 p=(0,0);d=0;dirs=[(0,1),(1,0),(0,-1),(-1,0)]
 for t,c in enumerate(g['word']):
  for h in range(4):prefix.append([2*L(rot(p,h))-a[h],i,t,h,p])
  d=(d+(1 if c=='R'else-1))%4;q=dirs[d];p=p[0]+q[0],p[1]+q[1]
assert max(z[0]for z in terms)==100 and max(z[0]for z in prefix)==40
files=['word_stabilization/dcv_free_direction_family102.json','word_stabilization/dcv_producer_closed_family.tsv','core_periodicity_new/chronology_dcuv/literal_residual_geometry.json','audits/check_dcuv_boundary_pruning_independent.json']
out={'status':'Exact arithmetic controls; epoch-reset proof pending independent review','core_offsets':a,'baseline_weight':60,'minimum_typed_weight':-60,'reset_cost':120,'U_core_output_cost':100,'U_prefix_maximum':40,'DCV_prefix_maximum':36,'initial_activation_cost':76,'U_cost_attainers':[z for z in terms if z[0]==100],'prefix_attainers':[z for z in prefix if z[0]==40],'B':'57+38(m-5)+60u','R':'ceil(2B/5)','t':'floor((2R+1)^2/3)','duration':'20R(t+1)+28t','hashes':{s:hashlib.sha256((R/s).read_bytes()).hexdigest()for s in files}}
Path(__file__).with_name('dcuv_epoch_reset_bound.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
