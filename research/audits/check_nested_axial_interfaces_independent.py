from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();R=P.parent.parent/'causal_reduction/unit_scale'
U='RRLRRRRL';V='LLRLLRLL';W=U+'R'+V;mirror=str.maketrans('RL','LR');D=(1j,1,-1j,-1)
def trace(w,h=0):
 z=0j;out=[]
 for t,c in enumerate(w):out.append((z,h,c));h=(h+(1 if c=='R'else-1))%4;z+=D[h]
 return out,(z,h)
rows,end=trace(W);assert end==(1,1)
slots=[i for i,(_,h,_)in enumerate(rows)if h%2];assert slots==list(range(1,16,2))
for c in 'RL':
 for h in range(4):
  word=W if c=='R'else W.translate(mirror)
  assert trace(word,h)[1]==trace(c,h)[1]
author=json.loads((R/'nested_axial_subsets.json').read_text());assert author['slots']==slots
checks=[]
for mask in range(256):
 selected={j for i,j in enumerate(slots)if mask>>i&1}
 word=''.join(W if j==8 else(W if c=='R'else W.translate(mirror))if j in selected else c for j,(_,_,c)in enumerate(rows))
 assert len(word)==33+16*len(selected)and trace(word)[1]==(1,1)
 last={};conflict=None
 for t,(z,h,c)in enumerate(trace(word)[0]):
  if z in last and last[z][1]==c:conflict=(z,last[z][0],t,c);break
  last[z]=(t,c)
 if mask==0:assert conflict is None and word==U*2+'R'+V*2;continue
 assert conflict is not None
 a=author['cases'][mask-1];b=a['tests'];assert a['mask']==mask and a['slots']==sorted(selected)and len(b)==1 and b[0]['depth']==2 and b[0]['length']==len(word)
 z,t0,t1,c=conflict;v=b[0]['conflict'];assert tuple(v['cell'])==(int(z.real),int(z.imag))and v['previous'][:2]==[t0,int(c=='L')]and v['current'][:2]==[t1,int(c=='L')]
 checks.append(dict(mask=mask,cell=[int(z.real),int(z.imag)],previous=t0,current=t1,turn=c))
# Reflection/complement field delta, on finite complete read support only.
field_cases=0
for n in range(1,34):
 for mirrored in(False,True):
  word=U*n+'R'+V*n
  if mirrored:word=word.translate(mirror)
  for h in range(4):
   rr,_=trace(word,h);need={};state=set()
   for z,hh,c in rr:
    if z not in need:need[z]=(c=='L');state.add(z)if c=='L'else None
    assert(z in state)==(c=='L');state.symmetric_difference_update({z})
   before={z for z,b in need.items()if b};delta={z:int(z in state)-int(z in before)for z in state^before}
   rot=(-1j)**h;sign=-1 if mirrored else 1
   # Every stable axial interior column has exactly the reflected/complemented transfer.
   for x in range(2,2*n):
    changes={z:v for z,v in delta.items()if (z/rot).real==sign*x}
    expect={complex(sign*x,-2)*rot:(-1 if mirrored else 1),complex(sign*x,2)*rot:(1 if mirrored else-1)}
    assert changes==expect
   field_cases+=1
out=dict(status='PASS independent fixed eight-slot depth-two conflicts and dihedral complete-field controls',subsets=255,empty_subset_positive=True,conflicts=checks,field_cases=field_cases,scope='Every nonempty fixed subset of supplied perpendicular same-physical-type axial children fails by literal chronology at depth2, with simultaneous choices retained. Proper rotations and local reflected/complemented variants have the same clockwise signed bulk transfer along their ray, hence fixed-center remote-column proof extends. No arbitrary hierarchy, other bodies, moving-emitter theorem or global finite-support complementation symmetry.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='conflicts'})
