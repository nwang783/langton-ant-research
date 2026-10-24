"""Literal arithmetic for the signed deferred-activation D/C/V factor bound.
No author geometry or bound code is imported.
"""
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parents[1];S=P/'word_stabilization'
words={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR'}
marker='LLLLRLRRRRL';names=['D','DC','V','VC','VCC'];ids=[0,1,4,5,6]
def walk(w):
 p=0j;h=1j;required={};color={};flip=set();prefix=[p]
 for c in w:
  b=c=='L'
  if p in color:assert color[p]==b
  else:required[p]=b
  color[p]=not b;flip.symmetric_difference_update({p});h*=(-1j if c=='R'else 1j);p+=h;prefix.append(p)
 return p,h,{q for q,b in required.items()if b},flip,prefix
core=walk(marker)[2];assert len(core)==5
v=json.loads((S/'dcv_free_direction_family102.json').read_text())['values']
L=lambda z:int(z.real+3*z.imag)
rot=lambda z,h:z*(-1j)**h
A=[L(rot(-1+1j,h))+v[f'c{h}']for h in range(4)]
I=max(n for k,n in v.items()if k.startswith('u_'));wm=min(n for k,n in v.items()if k.startswith('w_'))
activation=[];heads=[];cores=[];mass=[]
for i,name in zip(ids,names):
 w=''.join(words[c]for c in name);end,h,_,flip,prefix=walk(w);entry=walk(w+marker)[2]
 newcore={end+h/1j*z for z in core};ins=entry-core;outs=(entry^flip)-newcore
 for g in range(4):
  activation.extend((2*L(rot(z,g))+I-A[g],i,g,[int(z.real),int(z.imag)])for z in ins)
  heads.extend((2*L(rot(z,g))-A[g],i,g,j)for j,z in enumerate(prefix))
  cores.extend((2*L(rot(z,g))-A[g],g,[int(z.real),int(z.imag)])for z in core)
 mass.append({'packet':name,'length':len(w),'mass_change':len(entry^flip)-len(entry),'inputs':len(ins),'outputs':len(outs)})
assert A==[2,52,54,-8] and I==60 and wm==-60
K=max(r[0]for r in activation);hp=max(r[0]for r in heads);cp=max(r[0]for r in cores)
assert(K,hp,cp)==(76,36,14)
assert[(max(A)-wm)//2,(max(A)+hp)//2,(max(A)+cp)//2]==[57,45,34]
# Exact inverse of the two independent strips: x=(u-3v)/10,
# y=(3u+v)/10 for u=x+3y and v=-3x+y.
for B in range(58):
 for x in range(-B,B+1):
  for y in range(-B,B+1):
   if abs(x+3*y)<=B and abs(-3*x+y)<=B:assert 5*max(abs(x),abs(y))<=2*B
source=json.loads((S/'dcv_mass_only_bound.json').read_text())
assert source['activation_bound']==K
assert sorted(source['activation_attainers'])==sorted([list(r[1:])for r in activation if r[0]==K])
for f,h in source['hashes'].items():assert hashlib.sha256((S/f).read_bytes()).hexdigest()==h
out={'status':'PASS literal activation and active-box constants; analytic scope is context-complete recurrent packet factors',
 'core_cells':len(core),'core_offsets':A,'input_weight':I,'minimum_output_weight':wm,'activation_bound':K,
 'activation_attainers':[list(r[1:])for r in activation if r[0]==K],
 'prefix_maximum':hp,'prefix_attainers':[r[1:]for r in heads if r[0]==hp],
 'core_maximum':cp,'packet_checks':mass,
 'produced_strip':'57+38(m-5)','head_strip':'45+38(m-5)','core_strip':'34+38(m-5)',
 'radius':'ceil((114+76(m-5))/5)','area':'(2R+1)^2','non_D_macro_bound':'floor(A/3)',
 'fine_step_bound':'20R(t+1)+18t','note_sha256':hashlib.sha256((S/'dcv_mass_only_cubic_bound.md').read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
