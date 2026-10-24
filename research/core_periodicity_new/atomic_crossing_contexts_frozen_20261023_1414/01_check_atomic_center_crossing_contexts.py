"""Complete exact finite geometry of proper atomic corrected-center crossings.
Literal contexts only; no chronological realizability or first-contact bound.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';AP=W/'atomic_exit_bud_frozen_20261023_1325/02_atomic_exit_bud_maturation.json'
J=json.loads(GP.read_text());G=J['geometry'];K=set(map(tuple,J['core']));AT=json.loads(AP.read_text());marker=G[0]['marker']
def rot(z,h):x,y=z;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def frac(x):return[x.numerator,x.denominator]
def reconstruct(word):
 p=(0,0);h=0;need={};par=set();raw=None
 for i,ch in enumerate(word+marker):
  b=ch=='L';v=b^(p in par);assert p not in need or need[p]==v;need[p]=v
  par.symmetric_difference_update({p});h=(h+(-1 if b else 1))%4;p=add(p,rot((0,1),h))
  if i+1==len(word):raw=(p,h,set(par))
 p,h,odd=raw;B=K|{q for q,b in need.items()if b};I={q for q,b in need.items()if b}-K;after=B^odd;core={add(p,rot(q,h))for q in K};assert core<=after
 O=after-core;D2=sub(add((2*p[0],2*p[1]),rot((-1,-1),h)),(-1,-1))
 return dict(word=word,endpoint=[*p,h],requirements=[[x,y,bool(b)]for(x,y),b in sorted(need.items())],inputs=sorted(I),outputs=sorted(O),center_step_twice=D2)
atoms={name:reconstruct(G[a]['word'])for name,a in [('D',0),('V',4),('U',7)]};atoms['C']=reconstruct(AT['C_word'])
for name,a in [('D',0),('V',4),('U',7)]:
 assert atoms[name]['inputs']==sorted(map(tuple,G[a]['inputs']))and atoms[name]['outputs']==sorted(map(tuple,G[a]['outputs']))
assert atoms['C']['inputs']==[]and atoms['C']['outputs']==sorted(map(tuple,AT['C_residual_outputs']))
assert{n:tuple(a['center_step_twice'])for n,a in atoms.items()}==dict(D=(2,2),V=(2,6),U=(0,8),C=(2,2))
assert all((2,0)in a['outputs']for a in atoms.values())
rows=[];boxes=[];C0=(-1,-1)
for sa,S in atoms.items():
 d=tuple(S['center_step_twice'])
 for ta,T in atoms.items():
  for h in range(4):
   e=rot(T['center_step_twice'],h);den=det(d,e)
   if den==0:continue
   # At a crossing, 2p=C0-R_h(C0)+t*d-u*e with0<t,u<1.
   shift=sub(C0,rot(C0,h));corners=[add(shift,sub((t*d[0],t*d[1]),(u*e[0],u*e[1])))for t in[0,1]for u in[0,1]]
   lo=[min(q[k]for q in corners)for k in[0,1]];hi=[max(q[k]for q in corners)for k in[0,1]]
   bounds=[[-((-lo[k])//2),hi[k]//2]for k in[0,1]]
   boxes.append(dict(first_atom=sa,later_atom=ta,later_heading=h,pose_integer_bounds=bounds,parallelogram_corners_twice=corners))
   for x in range(bounds[0][0],bounds[0][1]+1):
    for y in range(bounds[1][0],bounds[1][1]+1):
     if(x+y+h)%2:continue
     z=sub(add((2*x,2*y),rot(C0,h)),C0);t=Fraction(det(z,e),den);u=Fraction(det(z,d),den)
     if not(0<t<1 and 0<u<1):continue
     req={tuple(r[:2]):bool(r[2])for r in T['requirements']};I=set(map(tuple,T['inputs']));contacts=[]
     for o in S['outputs']:
      q=rot(sub(o,(x,y)),-h)
      if q not in req:continue
      typ='INPUT'if q in I else'CORE'if req[q]else'WHITE'
      if typ=='CORE':assert q in K
      contacts.append(dict(source_output=o,later_local_cell=q,later_role=typ))
     assert contacts
     pre=[c for c in contacts if c['later_role']!='INPUT'];common=next((c for c in contacts if tuple(c['source_output'])==(2,0)),None)
     rows.append(dict(first_atom=sa,later_atom=ta,later_pose=[x,y,h],first_parameter=frac(t),later_parameter=frac(u),crossing_point_twice=[frac(Fraction(C0[k])+t*d[k])for k in[0,1]],common_output_contact=common,all_source_output_contacts=contacts,strict_prior_retirement_outputs=[c['source_output']for c in pre],strict_prior_retirement_required=bool(pre)))
assert len(rows)==42
assert Counter(r['later_pose'][2]for r in rows)=={1:21,3:21}
assert Counter(r['first_atom']for r in rows)==dict(D=2,V=20,U=18,C=2)
assert sum(r['common_output_contact']is None for r in rows)==20
assert sum(r['strict_prior_retirement_required']for r in rows)==40
exceptions=[r for r in rows if not r['strict_prior_retirement_required']]
assert[(r['first_atom'],r['later_atom'],r['later_pose'])for r in exceptions]==[('D','V',[-1,0,1]),('C','V',[-1,0,1])]
assert all(len(r['all_source_output_contacts'])==1 and r['all_source_output_contacts'][0]['source_output']==(2,0)and r['all_source_output_contacts'][0]['later_role']=='INPUT'for r in exceptions)
small=[r for r in rows if r['first_atom']=='V'and r['later_atom']=='D'and r['later_pose']==[0,1,1]];assert len(small)==1 and small[0]['common_output_contact']is None
O=dict(status='AUTHOR_COMPLETE_PROPER_ATOMIC_CENTER_CROSSING_CONTEXT_CATALOGUE_PASS',scope='Complete static corrected-center proper-transverse crossing geometry in the conserved sector. All42 crossings contact some source output;40 force at least one STRICT prior source-identity retirement, two may retire common2,0 at crossing. No chronological feasibility, first-contact C bound, fresh-root import, beta cost, global fuel or capture inference.',center_offset_twice=C0,atoms=atoms,complete_bounding_boxes=boxes,crossings=rows,counts=dict(crossings=42,common_output_avoided=20,strict_prior_retirement=40,input_only_exceptions=2),minimal_common_output_counterpair=small[0],dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,AP,Path(__file__).resolve()]})
OUT=W/'chronology_dcuv/atomic_center_crossing_contexts.json';OUT.write_text(json.dumps(O,indent=2)+'\n');print(O['counts']);print('exceptions',[(r['first_atom'],r['later_pose'])for r in exceptions])
