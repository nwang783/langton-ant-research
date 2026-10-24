"""Independent literal constants for the U-epoch reset potential bound."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];W=ROOT/'word_stabilization';v=json.loads((W/'dcv_free_direction_family102.json').read_text())['values'];expected=json.loads((W/'dcuv_epoch_reset_bound.json').read_text())
words={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR','U':'LLLLRLRRRRLRLLLLRRRRLRRLRRRR'};M='LLLLRLRRRRL';names=['D','DC','V','VC','VCC','U','UC','UCC']
def trace(w):
 p=0j;h=1j;required={};current={};odd=set();prefix=[]
 for c in w:
  prefix.append(p);needed=c=='L'
  if p in current:assert current[p]==needed
  else:required[p]=needed
  current[p]=not needed;odd.symmetric_difference_update({p});h*=(-1j if c=='R'else 1j);p+=h
 prefix.append(p);return p,h,{p for p,b in required.items()if b},odd,prefix
L=lambda p:int(p.real+3*p.imag);rotate=lambda p,h:p*(-1j)**h
core=trace(M)[2];a=[L(rotate(-1+1j,h))+v[f'c{h}']for h in range(4)];minw=min(z for k,z in v.items()if k.startswith('w_'));maxw=max(z for k,z in v.items()if k.startswith('w_'));I=max(z for k,z in v.items()if k.startswith('u_'))
assert(a,minw,maxw,I)==([2,52,54,-8],-60,60,60)
u_cost=[];u_prefix=[];dcv_prefix=[];activation=[];checks=[]
for name in names:
 raw=''.join(words[c]for c in name);p,h,_,odd,prefix=trace(raw);B=trace(raw+M)[2];endcore={p+h/1j*z for z in core};ins=B-core;outs=(B^odd)-endcore;dh=(1j,1,-1j,-1).index(h)
 for heading in range(4):
  if name.startswith('U'):
   u_cost.append(2*L(rotate(p,heading))+a[(heading+dh)%4]-a[heading])
   u_cost.extend(2*L(rotate(q,heading))+I-a[heading]for q in outs)
   u_prefix.extend(2*L(rotate(q,heading))-a[heading]for q in prefix)
  else:
   dcv_prefix.extend(2*L(rotate(q,heading))-a[heading]for q in prefix)
   activation.extend(2*L(rotate(q,heading))+I-a[heading]for q in ins)
 checks.append({'packet':name,'length':len(raw),'black_increment':len(B^odd)-len(B)})
assert(max(u_cost),max(u_prefix),max(dcv_prefix),max(activation),I-minw)==(100,40,36,76,120)
for field,value in [('core_offsets',a),('baseline_weight',I),('minimum_typed_weight',minw),('reset_cost',I-minw),('U_core_output_cost',max(u_cost)),('U_prefix_maximum',max(u_prefix)),('DCV_prefix_maximum',max(dcv_prefix)),('initial_activation_cost',max(activation))]:assert expected[field]==value
for p,h in expected['hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
out=dict(status='PASS epoch-reset constants and analytic O((m+u)^3) recurrent-factor bound',core_offsets=a,reset_cost=120,U_core_output_cost=100,U_prefix_maximum=40,DCV_prefix_maximum=36,initial_activation_cost=76,packets=checks,produced_strip='57+38(m-5)+60u',radius='ceil(2B/5)',duration='20R(t+1)+28t, t=floor((2R+1)^2/3)',scope='Complete recurrent-eight factors only. Does not bound u or exclude an infinite DCUV tail.',sha256=hashlib.sha256((W/'dcuv_epoch_reset_bound.md').read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
