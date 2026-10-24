from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];p=SELF.with_name('check_cap6_full_fuel_and_composition_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('# Rebuild word-only')[0],ns)
lift,trap,paths,words,T,expected,key=[ns[k]for k in('lift','trap','paths','words','T','expected','key')];D=R/'reframe_finite_seed_2026-10-24';G=R/'kernel_cycle_lift_2026-10-24';src=D/'physical_cap6_resource_obstructions.json';j=json.loads(src.read_text());profiles={a['index']:a for o in j['obstructions']for a in o['cycles']};assert set(profiles)=={2818,33389,33390};singles=[];pairs=[]
for i,r in sorted(profiles.items()):
 assert [expected(t)for t in r['transitions']]==[T[z]for z in paths[i]]
 result,err=lift(paths[i]);assert err is None;seed,B,p,h,tr=result;assert key(seed)==tuple(map(tuple,r['minimal_seed']));bad,detail=trap(B,p,h);assert bad==(i!=33389);singles.append({'index':i,'seed':key(seed),'output':key(B),'pose':[(int(p.real),int(p.imag)),h],'mandatory_budget':detail,'budget_trapped':bad})
 for k in sorted(profiles):
  result,err=lift(paths[i]+paths[k]);assert result is None
  pp=0j;hh=0;parity=set();witness=[];target=-1+0j if i==2818 else 2j
  for tick,z in enumerate(paths[i]+paths[k]+[None]):
   C=set()if z is None else{pp+complex(*q)*(-1j)**hh for q in T[z][3]}
   V=ns['edgevertices'](C)|{ns['wvertex'](pp,hh)}
   if any(v in V for v in ns['ends'](target,0)):witness.append((tick,int((target in C)^(target in parity))))
   if z is not None:parity.symmetric_difference_update({pp});hh=(hh+(1 if T[z][2]=='R'else-1))%4;pp+=1j*(-1j)**hh
  assert(1,0)in witness and((11 if i==2818 else 14),1)in witness
  pairs.append({'first':i,'second':k,**err,'author_specific_cell':(int(target.real),int(target.imag)),'author_specific_bit_obligations':witness})
files=[G/'THREE_PHYSICAL_CAP6_PROFILES_DO_NOT_COMPOSE.md',G/'three_cap6_profiles_certificate.json',G/'finite_component_profile_lift.py',src,SELF.with_name('check_cap6_full_fuel_and_composition_independent.json')]
out={'status':'PASS three actual resource profiles and all9 immediate complete-field pair obstructions','single_controls':singles,'all9_pair_conflicts':pairs,'dependencies':{str(f.relative_to(R)):hashlib.sha256(f.read_bytes()).hexdigest()for f in files},'scope':'Each single profile is a real finite-board prefix. All nine exact immediate ordered profile pairs fail with arbitrary unread exterior; this does not say the word alone is impossible. P/T are additionally trapped by mandatory old surviving full-profile members; Q is not trapped by that local budget test, although the separately signed complete cap6 theorem now excludes every eventual sustained cap6 orbit. No resource compiler, infinite regeneration, or capture follows.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
