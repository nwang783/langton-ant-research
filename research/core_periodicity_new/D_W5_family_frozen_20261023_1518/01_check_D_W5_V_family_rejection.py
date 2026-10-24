"""All-w age rejection of one proposed D/W5 literal family, not a depth scan."""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';JP=W/'chronology_dcuv/counted_input_age_rules_complete.json';G=json.loads(GP.read_text())['geometry'];mins={(a,x,y):m for a,x,y,m in json.loads(JP.read_text())}
def rot(z,h):x,y=z;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def scale(k,a):return k*a[0],k*a[1]
# Each coordinate is an exact pair (coefficient ofw,constant).
p=((0,0),(0,0));h=0;clock=0
for a in[1,0,5,5]:
 e=rot(G[a]['endpoint'][:2],h);p=tuple(plus(p[k],(0,e[k]))for k in[0,1]);h=(h+G[a]['endpoint'][2])%4;clock+=G[a]['name'].count('C')
assert p==((0,-5),(0,0))and h==1 and clock==3
prefix_end=[p,h,clock];vE=rot(G[4]['endpoint'][:2],h);assert vE==(3,-1)
third_preV=(p[0][1]+2*vE[0],p[1][1]+2*vE[1]);assert third_preV==(1,-2)
# w+2 E-oriented Vs.
p=tuple(plus(p[k],scale(vE[k],(1,2)))for k in[0,1]);assert p==((3,1),(-1,-2))
farVCCpose=p;e=rot(G[6]['endpoint'][:2],h);p=tuple(plus(p[k],(0,e[k]))for k in[0,1]);h=(h+G[6]['endpoint'][2])%4;clock+=2
assert p==((3,5),(-1,-2))and h==3 and clock==5
vW=rot(G[4]['endpoint'][:2],h);assert vW==(-3,1)
p=tuple(plus(p[k],scale(vW[k],(1,0)))for k in[0,1]);assert p==((0,5),(0,-2))
lateDpose=(5,-2,3);z=rot(G[0]['inputs'][0],3);lateDinput=(5+z[0],-2+z[1]);assert lateDinput==(4,-2)
early_input=rot((0,3),1);assert(1+early_input[0],-2+early_input[1])==lateDinput
assert all([0,3]in G[a]['inputs']and[0,3]not in G[a]['outputs']for a in[4,6])
assert mins[0,0,1]==3
rawconst=sum(len(G[a]['word'])for a in[1,0,5,5,6,0,4,4])+2*len(G[4]['word']);assert rawconst==231
O=dict(status='AUTHOR_ALL_W_PROPOSED_D_W5_V_FAMILY_EXCLUDED',scope='ONLY family DC,D,VC,VC,V^(w+2),VCC,V^w,D,V,V for every integerw>=0. Orderedidentity retirement atclock3 forces any laterq replacement age<=2 atclock5 D, contradicting signedDmin3. Not exclusion of generalD/W5 gate.',family_prefix=[1,0,5,5],parameter='integerw>=0',affine_coordinate_encoding='(w_coefficient,constant)',prefix_end=prefix_end,third_preV_pose_for_w_ge1=[1,-2,1],farVCC_pose_affine=farVCCpose,farVCC_pose_w0=[1,-2,1],earlier_consumer_clock=3,earlier_consumer_input=[0,3],earlier_consumer_does_not_output_same_cell=True,late_D_pose=lateDpose,late_D_input=lateDinput,late_D_clock=5,maximum_replacement_age=2,required_D_minimum=3,raw_length_affine=[36,231],dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,JP,Path(__file__).resolve()]})
OUT=W/'chronology_dcuv/D_W5_V_family_rejection.json';OUT.write_text(json.dumps(O,indent=2)+'\n');print(dict(all_w='excluded',cell=lateDinput,earlierC=3,laterC=5,replacement_age_bound=2,D_min=3))
