from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry']
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h]
assert G[0]['inputs']==[[0,1]] and G[1]['name']=='DC'
# Affine-in-g positions are represented as coefficient and constant pairs.
# Last pre-D head (2-g,1+g), W; first post-D head (-g,1+g), E.
w=rot((0,1),3);e=rot((0,1),1)
assert w==(-1,0)and e==(1,0)
assert[(2+w[0],-1),(1+w[1],1)]==[(0+e[0],-1),(1+e[1],1)]==[(1,-1),(1,1)]
J=dict(status='AUTHOR_AFFINE_ORDERED_AGE_CROSSING_PASS',scope='Signed1112 younger-critical source branch only; g>=1 impossible for V or VCC.',cell_affine=[[1,-1],[1,1]],pre_C_minus_tau=1,post_C_minus_tau=3,max_replacement_age=2,D_produced_minimum_age=3,conclusion='g=0; no trailing D; source V or VCC directly follows DC',dependencies={str(GP.relative_to(R)):hashlib.sha256(GP.read_bytes()).hexdigest()})
(R/'chronology_dcuv/v1_D_crossing_age.json').write_text(json.dumps(J,indent=2)+'\n');print(J)
