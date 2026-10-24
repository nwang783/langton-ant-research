"""Exact constants for a conditional finite D/C/V factor bound.
The proof requires the producer-family exclusion, whose independent signoff is separate.
"""
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent
weight=P/'dcv_free_direction_family102.json';resource=P/'dcv_residual_core_resources.json';wordfile=P/'seven_sub_dcv_port_quotient.json'
v=json.loads(weight.read_text())['values'];res=json.loads(resource.read_text());words=json.loads(wordfile.read_text())['macro_words'];keep=res['kept_packet_types'];K=res['core']
def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def L(p):return p[0]+3*p[1]
a=[L(rot((-1,1),h))+v[f'c{h}']for h in range(4)]
I=max(x for k,x in v.items()if k.startswith('u_'));M=max(I,*a);wmin=min(I,*[x for k,x in v.items()if k.startswith('w_')])
core_term=max(2*L(rot(k,h))-a[h]for h in range(4)for k in K)
best=(-10**9,None)
for i in keep:
 p=(0,0);h=0;coords=[p]
 for c in words[i]['word']:
  h=(h+(1 if c=='R'else-1))%4;d=((0,1),(1,0),(0,-1),(-1,0))[h];p=(p[0]+d[0],p[1]+d[1]);coords.append(p)
 for h in range(4):
  for t,z in enumerate(coords):
   value=2*L(rot(z,h))-a[h]
   if value>best[0]:best=(value,{'packet':i,'heading':h,'prefix_length':t,'relative_cell':z})
assert a==[2,52,54,-8] and I==60 and M==60 and wmin==-60 and core_term==14 and best[0]==36
out={'status':'Exact arithmetic checked; theorem application needs independent producer-family signoff','core_offsets':a,'initial_token_weight':I,'initial_potential_extra':M,'minimum_stored_weight':wmin,'core_black_strip_margin':(M+core_term)//2,'residual_black_strip_margin':(M-wmin)//2,'intermediate_head_strip_margin':(M+best[0])//2,'head_max_attainer':best[1],'all_black_strip_margin':60,'bounding_rectangle':{'x_margin':'24+ceil(3H/10)','y_margin':'24+ceil(3W/10)','width_X':'W+48+2ceil(3H/10)','width_Y':'H+48+2ceil(3W/10)'},'factor_bound':{'A':'(X+1)(Y+1)','d':'min(X,Y)','m':'floor((A-N0)/3)','macro_count':'(m+1)d+m','fine_step_count':'10(m+1)d+18m'},'sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in[weight,resource,wordfile]}}
(P/'dcv_directional_factor_bound.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
