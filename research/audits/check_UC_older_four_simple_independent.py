from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();B=ROOT/'core_periodicity_new/UC_older_four_simple_frozen_20261023_1733';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
K={q for q,b in walk(mark)[2].items()if b};P={-1+1j,-1+2j,-1+4j,2j,3j};w=4j;G={}
for s in(0,1,4,5,6,7,8,9):
 e,h,_,flip=walk(raws[s]);req=walk(raws[s]+mark)[2];black={q for q,b in req.items()if b};G[s]=(black-K,(black^flip)-{e+rotation(q,h)for q in K},set(req)|K)
 if s in(7,8,9):assert req[w]is False and black-K==P
assert not(P&set(walk(mark)[2]))
A=3+11j;Bend=3+3j;u=Bend-A
cross=lambda z,v:int(z.real*v.imag-z.imag*v.real);rows=[]
for s,(I,O,C)in G.items():
 for i in I:
  for h in range(4):
   p=w-rotation(i,h);hit={p+rotation(q,h)for q in C}&P
   if(sum(xy(p))+h)%2:reason='sector';st=None
   elif hit:reason='protected';st=None
   else:
    base=0 if s in(0,1)else 4 if s in(4,5,6)else 7
    e=walk(raws[base])[0];q=2*p+rotation(-1-1j,h);v=2*rotation(e,h);den=cross(u,v)
    assert den;aa=Fraction(cross(q-A,v),den);bb=Fraction(cross(q-A,u),den)
    assert 0<aa<1 and 0<=bb<=1;st=[str(aa),str(bb)];reason='old_source_base_contact'
   rows.append(dict(packet=s,pose=(*xy(p),h),reason=reason,parameters=st))
assert Counter(q['reason']for q in rows)==dict(sector=46,protected=40,old_source_base_contact=6)
actual={(q['packet'],tuple(q['pose']),tuple(q['parameters']))for q in rows if q['parameters']}
assert actual=={(s,p,st)for ss,p,st in[((0,1),(1,4,3),('1/2','0')),((4,5),(3,4,3),('1/3','2/3')),((7,8),(4,5,3),('1/4','3/4'))]for s in ss}
for s in(8,9):
 O={1+5j+rotation(q,2)for q in G[s][1]};assert {w,* (P-{-1+2j})}<=O and-1+2j not in O
old=json.loads((ROOT/'audits/check_U_white_shadow_independent.json').read_text())['remaining_static_templates']
assert {tuple(r['source_and_pose'])for r in old}-{(8,1,5,2),(9,1,5,2)}=={(s,1,-1,0)for s in(7,8,9)}
out=dict(status='PASS independent compulsory-sibling/simple-center exclusion of two older-q four-cohorts',manifest_sha256=hashlib.sha256((SELF.parents[1]/'core_periodicity_new/UC_older_four_simple_frozen_20261023_1733/manifest.json').read_bytes()).hexdigest(),counts=dict(Counter(q['reason']for q in rows)),cases=rows,scope='Same simple retained complete-eight factor, exact four old source identities and older q. No age kernel, root-merger or all-U conclusion; three same-heading four-cohorts still open.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
