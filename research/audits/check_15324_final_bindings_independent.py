from pathlib import Path
from collections import Counter
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];U=ROOT/'causal_reduction/unit_scale';R=ROOT/'nonlinear_global_budget_2026-10-23'
old=json.loads((U/'prepared4352_uniform_support_manifest.json').read_text());new=json.loads((U/'prepared4352_two_phase_manifest.json').read_text());A=json.loads((U/'prepared4352_output_return_wave.json').read_text());nf=json.loads((R/'three_standard_band_wave_normal_form.json').read_text());W=old['stages'][-1]['word'];D=(1j,1,-1j,-1)
seed=[[[3*x[0],4*x[0]+x[1]],[3*y[0],4*y[0]+y[1]]]for x,y in old['seed_families']];assert seed==new['seed_families']and len(seed)==394
for a,b in zip(old['stages'],new['stages']):
 assert a['word']==b['word']and a['heading']==b['heading']
 for key in('count_N_constant','start_x_N_constant','start_y_N_constant','start_time_N_constant'):
  x,y=a[key];assert b[key]==[3*x,4*x+y]
assert len(new['stages'])==14
assert new['stages'][-2]['word']==W*3+W[:2331]+A['prefix_word']and new['stages'][-1]['word']==A['word']
assert new['stages'][-2]['count_N_constant']==[0,1]and new['stages'][-1]['count_N_constant']==[1,0]
assert new['end_time_M_constant']==[129780,455161]and new['end_mass_M_constant']==[12660,37419]and new['actual_K_M_constant']==[13269,86411]and new['end_pose']==[[117,111],0]
# Exact bulk input of return, including untouched standard classes, not merely
# the last colors on4352's read support.
base={(t,a)for t,r in nf['full_black_profiles']for a in range(r,26,2)};p=-2+3j;h=3;odd=set()
for c in W:
 x,y=int(p.real),int(p.imag);odd.symmetric_difference_update({(x-y,x%26)});h=(h+(1 if c=='R'else-1))%4;p+=D[h]
output=base^odd;assert len(output)==652
field=A['complete_initial_ray_field'];full=set(map(tuple,field['full']));rayodd={tuple(k)for k,ts in field['upper_rays']if len(ts)%2};bulk=full^rayodd
returnclasses=set();p=13+7j;h=0
for c in A['word']:
 x,y=int(p.real),int(p.imag);returnclasses.add((x-y,x%26));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
assert all((q in output)==(q in bulk)for q in returnclasses)
# Exterior mature helpers do not change any class of the entire return strip.
assert {q for q in bulk if -28<=q[0]<=46}=={q for q in output if -28<=q[0]<=46}
files=['prepared15324_output_consumer.md','prepared4352_two_phase_finite_family.md','prepared4352_two_phase_manifest.json','prepared4352_output_return_wave.json']
out={'status':'PASS final exact proof/manifest bindings and complete mature output equality','bindings':{name:hashlib.sha256((U/name).read_bytes()).hexdigest()for name in files},'complete4352_output_black_classes':len(output),'checked_return_26_classes':len(returnclasses),'whole_return_normal_strip':[-28,46],'scope':'Whole original394-cell affine chronology signed separately; return consumes complete mature4352 output. Exterior helpers retained in complete field and absent on this strip. No third phase or renewal.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
