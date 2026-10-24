"""Separate author finite cube-union proof replay; graph construction audited separately."""
from pathlib import Path
import json,collections,hashlib
D=Path('chronology_dcuv/vcc_d_vc_joint_box_patch');J=json.loads((D/'model.json').read_text());rows=(D/'basis.txt').read_text().splitlines();m,np,nb,nlab=map(int,rows[0].split());assert m==0 and np==J['goal']+1 and nb==len(J['points'])and nlab==len(rows)-1
by=collections.defaultdict(list)
for line in rows[1:]:
 p,k,v=map(int,line.split());assert v&~k==0;by[p].append((k,v))
def covers(p,k,v):return any(a&k==a and(v^b)&a==0 for a,b in by[p])
assert covers(J['goal'],0,0)
p,k,v=J['start'];assert not any(v&a==b for a,b in by[p])
checks=0;nonempty=0
for fr,to,a,op,K,V,F,C,R in J['edges']:
 assert C==R==op==0
 for k,v in by[to]:
  checks+=1;w=(v^F)&k
  if(w^V)&k&K:continue
  kk=k|K;vv=(w|V)&kk
  assert covers(fr,kk,vv),(fr,to,a,kk,vv)
  nonempty+=1
S={'status':'PASS complete unrestricted cube predecessor closure','controls':np,'color_bits':nb,'basis_cubes':nlab,'edges':len(J['edges']),'target_cube_edge_cases':checks,'nonempty_preimage_cases':nonempty,'goal_included':True,'unique_initial_color_excluded':True,'scope':'Finite graph no-hit certificate only. The physical mapping and no-zero-C-reentry lemma require independent reconstruction.','hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in[D/'model.json',D/'model.dat',D/'basis.txt']}}
(D/'basis_check.json').write_text(json.dumps(S,indent=2)+'\n');print(S)
