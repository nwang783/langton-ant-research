from pathlib import Path
from fractions import Fraction
import hashlib,json,math
P=Path(__file__).resolve();S=P.with_name('check_atomic_crossing_contexts_independent.py');exec(compile(S.read_text().split('rows=[];start=')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/two_C_first_contact_frozen_20261023_1436';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_two_C_first_center_contact.json').read_text());order={'D':2,'C':2,'V':1,'U':0};start=-1-1j;geoms=[]
for an,(_,_,out,da)in atoms.items():
 for bn,(need,I,_,db)in atoms.items():
  if order[an]<=order[bn]:continue
  h=2;dbh=rotation(db,h);offset=rotation(start,h);den=det(da,dbh);assert den
  corners=[start-offset+s*da-t*dbh for s in(0,1)for t in(0,1)]
  for x in range(math.ceil(min(z.real for z in corners)/2),math.floor(max(z.real for z in corners)/2)+1):
   for y in range(math.ceil(min(z.imag for z in corners)/2),math.floor(max(z.imag for z in corners)/2)+1):
    if(x+y+h)%2:continue
    pos=complex(x,y);delta=2*pos+offset-start;s=Fraction(det(delta,dbh),den);t=Fraction(det(delta,da),den)
    if not(0<=s<1 and 0<t<=1):continue
    hits=[q for q in I if pos+rotation(q,h)in K and oldages[(4 if bn=='V'else 7),q]>2]
    # Derive eligible forced core inputs, then choose the source's canonical true slot.
    assert hits and s==0
    slot=1+2j if bn=='V'else(2j if y==1 else-1+4j);assert slot in hits
    z=pos+rotation(slot,h);geoms.append((an,bn,(x,y,h),s,t,slot,z))
assert len(geoms)==8
roles=[]
for src in ids:
 roles.append((('D'if base[src]==0 else'V'if base[src]==4 else'U'),src,0j,0,0,counts[src]))
 p=G[base[src]][0];h=0
 for shift in range(counts[src]):
  roles.append(('C',src,p,h,shift,counts[src]-shift));p+=rotation(1j,h);h=(h-1)%4
assert len(roles)==15
cases=[]
for an,bn,pos,s,t,slot,z in geoms:
 for atom,src,p,h,shift,remaining in roles:
  if atom!=an:continue
  fullcell=p+rotation(z,h);assert fullcell not in G[src][4]
  for dst in ((4,5,6)if bn=='V'else(7,8,9)):
   assert slot in G[dst][3];minimum=oldages[dst,slot];assert minimum>2
   cases.append((an,bn,pos,src,xy(p),h,shift,xy(fullcell),dst,xy(slot),minimum,2-remaining))
auth=J['all_99_source_role_target_tail_core_age_cases'];assert len(cases)==len(auth)==99
A={ (r['earlier_atom'],r['later_atom'],tuple(r['later_pose'])):r for r in J['all_eight_canonical_two_C_contact_geometries']}
for an,bn,pos,s,t,slot,z in geoms:
 r=A[an,bn,pos];assert Fraction(r['earlier_chord_parameter'])==s and Fraction(r['later_chord_parameter'])==t and tuple(r['chosen_later_input'])==xy(slot)and tuple(r['input_cell_in_earlier_atomic_core'])==xy(z)
expected=[]
for r in auth:
 g=J['all_eight_canonical_two_C_contact_geometries'][r['geometry_index']];role=J['all_15_actual_atomic_source_roles'][r['actual_source_role_index']];p=role['atomic_entry_in_full_source_frame']
 expected.append((g['earlier_atom'],g['later_atom'],tuple(g['later_pose']),r['full_source'],tuple(p[:2]),p[2],role['atomic_entry_clock_shift'],tuple(r['same_cell_in_full_source_frame']),r['target_full_packet'],tuple(r['target_input_slot']),r['signed_produced_age_minimum'],r['later_producer_age_upper_bound']))
assert sorted(cases)==sorted(expected)
out=dict(status='PASS independent exact two-C canonical contact geometry and ordered core-to-residual age obstruction',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),geometries=[(a,b,p,str(s),str(t),xy(slot),xy(z))for a,b,p,s,t,slot,z in geoms],source_roles=len(roles),cases=cases,scope='First center contact inside actual complete-eight factors cannot have atomic-entry C gap two, including canonical endpoint contacts. Earlier core excludes entry residual identity; same full-source output absence blocks internal-tail birth loophole; every later producer is age<=2. No higher-gap, word-length, global capture or unrestricted atomic-language exclusion.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(cases))
