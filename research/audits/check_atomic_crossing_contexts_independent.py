from pathlib import Path
from fractions import Fraction
import json,hashlib,math
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/atomic_crossing_contexts_frozen_20261023_1414';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_atomic_center_crossing_contexts.json').read_text());atoms={}
for n,ww in {'D':raws[0],'V':raws[4],'U':raws[7],'C':C}.items():
 e,dh,_,flip=walk(ww);need=walk(ww+mark)[2];init={z for z,c in need.items()if c};assert K<=init
 O=(init^flip)-{e+rotation(z,dh)for z in K};step=2*e+rotation(-1-1j,dh)+1+1j
 atoms[n]=(need,init-K,O,step)
def det(a,b):return int(a.real*b.imag-a.imag*b.real)
rows=[];start=-1-1j
for an,(_,_,out,da)in atoms.items():
 for bn,(need,I,_,db)in atoms.items():
  for h in range(4):
   dbh=rotation(db,h);offset=rotation(start,h);den=det(da,dbh)
   if not den:continue
   # Coordinate-projection overlap bounds give a proven finite candidate domain.
   alo=complex(min(start.real,(start+da).real),min(start.imag,(start+da).imag));ahi=complex(max(start.real,(start+da).real),max(start.imag,(start+da).imag))
   blo=complex(min(offset.real,(offset+dbh).real),min(offset.imag,(offset+dbh).imag));bhi=complex(max(offset.real,(offset+dbh).real),max(offset.imag,(offset+dbh).imag))
   for x in range(math.ceil((alo.real-bhi.real)/2),math.floor((ahi.real-blo.real)/2)+1):
    for y in range(math.ceil((alo.imag-bhi.imag)/2),math.floor((ahi.imag-blo.imag)/2)+1):
     if(x+y+h)%2:continue
     pos=complex(x,y);delta=2*pos+offset-start;t=Fraction(det(delta,dbh),den);u=Fraction(det(delta,da),den)
     if not(0<t<1 and 0<u<1):continue
     contacts=[]
     for q in out:
      z=rotation(q-pos,-h)
      if z in need:contacts.append((xy(q),'INPUT'if z in I else'WHITE'if not need[z]else'CORE'))
     assert contacts
     strict=sorted(z for z,typ in contacts if typ!='INPUT');row=(an,bn,(x,y,h),str(t),str(u),strict,any(z==(2,0)for z,_ in contacts));rows.append(row)
auth={ (r['first_atom'],r['later_atom'],tuple(r['later_pose'])):r for r in J['crossings']}
assert len(rows)==len(auth)==42
for a,b,pos,t,u,strict,common in rows:
 r=auth[a,b,pos];assert t==str(Fraction(*r['first_parameter']))and u==str(Fraction(*r['later_parameter']))
 assert strict==sorted(map(tuple,r['strict_prior_retirement_outputs']))and common==(r['common_output_contact']is not None)
assert sum(bool(r[5])for r in rows)==40 and sum(not r[6]for r in rows)==20
assert {(a,b,pos)for a,b,pos,t,u,s,c in rows if not s}=={('D','V',(-1,0,1)),('C','V',(-1,0,1))}
out=dict(status='PASS independent exact complete static atomic proper-crossing catalogue',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),crossings=rows,scope='All proper interior transverse sector-compatible atom chord contacts only;40 require old output-identity retirement strictly before later atom,2 allow input consumption there. No chronological feasibility, entry-C horizon, fresh roots, beta, fuel or capture conclusion.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
