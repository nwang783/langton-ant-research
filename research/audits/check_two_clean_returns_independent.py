from pathlib import Path
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'kernel_cycle_lift_2026-10-24';K=R/'reframe_finite_seed_2026-10-24/kernel_M5_scc.json'
p=SELF.with_name('check_cycle_birth_finite_fuel_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('cells=')[0],ns)
ends,component,step,wvertex=[ns[x]for x in('ends','component','step','wvertex')]
def xy(q):return int(q.real),int(q.imag)
def ck(C):return sorted(map(xy,C))
def transform(C,p,h):return{p+complex(*q)*(-1j)**h for q in C}
J=json.loads(K.read_text());mac={k:J['first_return_cycles'][i]for k,i in [('A',0),('C',11)]}
def plan(word):
 p=0j;h=0;rows=[]
 for a in word:
  for z in mac[a]['transitions']:
   rows.append((p,h,transform(z['input_component'],p,h),z['turn']))
   pn=p+complex(*z['output_pose'][0])*(-1j)**h;hn=(h+z['output_pose'][1])%4
   p,h=pn,hn
 rows.append((p,h,set(),None));return rows

def test(word):
 plan0=plan(word);seen={};flips={}
 for t,(p,h,C,ch)in enumerate(plan0):
  V={wvertex(p,h)}|{v for q in C for v in ends(q,0)}
  ports={(v+d)/2 for v in V for d in(1+1j,1-1j,-1+1j,-1-1j)}
  for q in sorted(ports,key=xy):
   required=(q in C)^bool(flips.get(q,0))
   if q in seen and seen[q][0]!=required:return{'word':word,'conflict':xy(q),'first':seen[q],'second':(required,t,q in C,flips.get(q,0))}
   seen.setdefault(q,(required,t,q in C,flips.get(q,0)))
  if ch:flips[p]=flips.get(p,0)^1
 B={q for q,z in seen.items()if z[0]};seed=set(B);p=0j;h=0
 for t,(pp,hh,C,ch)in enumerate(plan0):
  assert (p,h)==(pp,hh)and component(B,0,wvertex(p,h))[1]==C
  if ch:
   p,h,c=step(B,p,h);assert c==ch
 return{'word':word,'seed':ck(seed),'final':ck(B),'pose':[xy(p),h]}
ones=[test(a)for a in 'AC'];pairs=[test(a+b)for a,b in product('AC',repeat=2)]
assert ones[0]['seed']==[]and ones[1]['seed']==[(-1,1)]
assert all('conflict'in z for z in pairs)
assert [z['conflict']for z in pairs]==[(0,-1),(0,-1),(-1,0),(-1,0)]
cont=[]
for z in ones:
 B={complex(*q)for q in z['final']};p=complex(*z['pose'][0]);h=z['pose'][1];events=[]
 for t in range(4):
  w=wvertex(p,h);_,C=component(B,0,w);a,b=ends(p,0);v=b if a==w else a;_,I=component(B,0,v)
  if I==C:I=set()
  p,h,ch=step(B,p,h);assert ch=='R';events.append((len(I),len(component(B,0,wvertex(p,h))[1])))
 cont.append(events)
assert cont==[[(0,1),(0,2),(0,3),(3,7)],[(0,1),(0,2),(0,3),(1,5)]]
files=['TWO_CLEAN_RETURNS_OBSTRUCTION.md','check_two_clean_returns.py','two_clean_returns_certificate.json'];hashes={f:hashlib.sha256((D/f).read_bytes()).hexdigest()for f in files}
out={'status':'PASS exact two-clean-return complete-field obstruction','author_hashes':hashes,'kernel_sha256':hashlib.sha256(K.read_bytes()).hexdigest(),'single_macro_controls':ones,'all_four_profile_conflicts':pairs,'four_R_continuations':cont,'analytic':['The supplied component at each cut is COMPLETE iff every edge incident to its vertices or the isolated active cursor has exactly its stated bit. Any exterior attachment must cross one of these tested ports. Pulling each constraint through exact earlier read parity therefore is a necessary and sufficient finite-board test for the entire prescribed component history, with arbitrary unread exterior retained.','The two allowed single macros independently reconstruct seeds empty and{(-1,1)} and their complete outputs. A leaves a3star; C leaves that star plus a fresh singleton at(-1,0). No remote extension changes these complete emitted components without already violating the profile.','After A the next fourthR must import that3star, yielding mass7. After C the next fourthR must import the new singleton, yielding mass5 but at the wrong port: pathC only imports at its firstR and A never imports. Earlier other imports already violate the clean paths. No L occurs before the compulsory contact, so neither retained output can disappear.','Independent finite port/read-parity constraints exclude AA,AC at(0,-1), CA,CC at(-1,0), while singleA/C pass complete-board replay. This is stronger than the signed conservative9-return geometry but does not invalidate or alter that proof.'],'scope':'No two consecutive exact zero-singleton-drop paths can compose physically. Turn words alone can survive with different active components. With signed110-path singleton ledger this sharpens the finite-support cap5 exit argument; it is not standard capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
