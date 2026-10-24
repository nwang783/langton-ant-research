from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23'
# Reuse only independently written literal walk and rational segment primitives.
old=R/'audits/check_foreign_kinked_barrier_turn_independent.py';ns={'__file__':str(old)};exec(old.read_text().split('geometries=[]')[0],ns)
W,M,walk,center,xy,meet=(ns[k] for k in ('W','M','walk','center','xy','meet'))
a=json.loads((D/'foreign_first_contact_interface.json').read_text());K={-1-1j,-1,-1j,0,1};L={0,1j,1,1+1j}
vec={};rows=[]
for name in 'DCVU':
 t=walk(W[name]);assert t['feasible'];vec[name]=center(t['p'],t['h'])-center(0,0)
assert vec=={'D':2+2j,'C':2+2j,'V':2+6j,'U':8j}
f=walk(W['F']);assert f['feasible'];fv=center(f['p'],f['h'])-center(0,0);assert fv==-6-2j
for h in range(4):
 turn=(-1j)**h;age=(-h)%4 or 4
 for name,v in vec.items():
  c=-1-1j;end=c+v;d=fv*turn;off=(-1-1j)*turn
  corners=[c+s*v-off-t*d for s in (0,1) for t in(0,1)]
  lo=[-((-int(min(getattr(q,z)for q in corners)))//2)for z in('real','imag')]
  hi=[int(max(getattr(q,z)for q in corners))//2 for z in('real','imag')]
  for x in range(lo[0],hi[0]+1):
   for y in range(lo[1],hi[1]+1):
    if(x+y+h)%2:continue
    p=complex(x,y);z=2*p+off;hit=meet(xy(c),xy(end),xy(z),xy(z+d))
    if hit is None:continue
    assert len(hit)==3 and isinstance(hit[0],F), 'All chord directions are nonparallel.'
    s,t,_=hit
    if not(0<=s<1 and 0<t<=1):continue
    rows.append((name,x,y,h,s,t,age,age+4))
def canon(r):return(r['source_atom'],*r['foreign_pose'],F(r['source_parameter']),F(r['foreign_parameter']),*r['permitted_C_ages'])
assert set(rows)=={canon(r)for r in a['rows']};assert len(rows)==42
assert Counter(r[6]for r in rows)=={1:9,2:12,3:9,4:12};assert Counter(r[0]for r in rows)=={'D':6,'C':6,'V':14,'U':16}
# Exact symbolic principal-turn check. beta/(pi/4) lies strictly between0 and1.
# Delta = dc + db*beta in quarter-pi units. For n=4q+r the closing
# principal turn is8 ceil(n/4)-2n-Delta; increasing n by4 preserves it.
angle=[]
for name,(dc,db) in {'D':(3,1),'C':(3,1),'V':(2,2),'U':(2,1)}.items():
 for n in range(4):
  k=(n+3)//4;cc=8*k-2*n-dc;cd=-db
  assert min(cc,cc+cd)>=-4 and max(cc,cc+cd)<=4
  assert not(cd==0 and abs(cc)==4)
  angle.append((name,n,cc,cd))
branches=[]
for b in(0,1):
 for n in range(13):
  if b and n==0:continue
  turn=8*((n+3)//4-b)
  if abs(turn)==8:branches.append((b,n,turn))
assert branches==[(0,n,8)for n in range(1,5)]+[(1,n,8)for n in range(5,9)]
filters={}
for name in 'FQB':
 ctx=walk(W[name]+M);assert ctx['feasible'];out=[]
 for r in rows:
  if r[0]!='U':continue
  _,x,y,h,*_=r;p=complex(x,y);turn=(-1j)**h
  core={p+z*turn for z in K};white={p+z*turn for z,b in ctx['req'].items()if not b};inputs={p+z*turn for z,b in ctx['req'].items()if b}-core
  reason='held_star_in_core'if L&core else'held_star_before_white'if L&white else'unexcluded_necessary_interface'
  out.append((x,y,h,reason,tuple(sorted(map(xy,L&inputs)))))
 expected={(tuple(q['foreign_pose'])+(q['reason'],tuple(map(tuple,q['star_input_hits']))))for q in a['U_source_star_filters'][name]};assert set(out)==expected
 filters[name]={'counts':dict(Counter(r[3]for r in out)),'necessary_poses':[list(r[:3])for r in out if r[3]=='unexcluded_necessary_interface']}
# Actual suffix ownership, without assuming a U-to-foreign connector exists.
assert (walk(W['U'])['p'],walk(W['U'])['h'])==(4j,0)
p=-3-3j;h=2;assert(p+f['p']*(-1j)**h,(h+f['h'])%4)==(1-1j,0)
assert not L&{p+z*(-1j)**h for z in walk(W['F']+M)['req']}
d=walk(W['D']);assert not L&{1-1j+q for q,hd,ch in d['reads']};assert 1-1j+d['p']==2
c=walk(W['C']);assert(c['reads'][1][0]+2,c['reads'][1][2])==(1,'L')
closure=[-5-5j,1-3j,3-1j,1+1j,-1-1j]
assert closure[1]-closure[0]==6+2j and closure[2]-closure[1]==2+2j
# Boundary edges have midpoints (1,0),(0,0), respectively.
assert[(closure[i]+closure[i+1])/4 for i in(2,3)]==[1,0]
assert sum((2,2,-3))==1
conditional=[(n,b)for b in(0,1)for n in range(2,15,4)if abs(2*(n+2-4*b))==8];assert conditional==[(2,0),(6,1)]
# Source/suffix literal positions for preceding-C branch.
cp=-2-3j;ch=3;assert(cp+c['p']*(-1j)**ch,(ch+c['h'])%4)==(p,h)
manifest=D/'foreign_first_contact_manifest.json';note=D/'foreign_first_contact_interface.md'
assert hashlib.sha256(manifest.read_bytes()).hexdigest()=='8c922bd6545d543d6939aa200fb6ee70d9a4424079131925502f8738fbcaa35a'
out={'status':'PASS exact first foreign contact catalogue and qualified Jordan obligations','manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest(),'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'geometry_count':42,'clock_labels':84,'full_word_filters':filters,'symbolic_principal_turn_cases':angle,'first_contact_age_ranges':{'preceded_not_C':[1,4],'preceded_C':[5,8]},'prepared_return_conditional_Jordan_branches':conditional,'analytic_review':'The first chronological contact closes a simple prior atomic subarc using the nonparallel F-prefix. The C-to-F -2pi principal wrap is retained. The separate two-held-edge return closure is only conditional on Jordan simplicity; no older ghost-path avoidance is assumed. Full Q/B contexts, not an internal F marker, are used.','scope':'Necessary interfaces only; no attained ancestry, first-contact exclusion, Q/B-tail catalogue, global seven-word simplicity or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(filters)
