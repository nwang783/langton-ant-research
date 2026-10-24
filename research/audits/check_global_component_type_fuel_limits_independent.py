from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'kernel_cycle_lift_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ns={'__file__':str(S.with_name('check_cycle_birth_finite_fuel_independent.py'))};exec(Path(ns['__file__']).read_text().split('cells=')[0],ns)
ends,component,step,wvertex=[ns[x]for x in ['ends','component','step','wvertex']]
xy=lambda q:(int(q.real),int(q.imag));G={-1j,1+1j,2+2j,1+3j};B=set(G);p=0j;h=1;rd=[]
for t in range(173):rd.append((p,h,'L'if p in B else'R'));p,h,ch=step(B,p,h)
L=set(B);assert(len(L),p,h)==(35,4+1j,0)
assert [t for t,(q,h,c)in enumerate(rd)if q==2j]==[60] and rd[60][2]=='R'
assert tuple(f(q.real if ax==0 else q.imag for q,h,c in rd)for ax in [0,1]for f in [min,max])==(0,7,-2,7)
sector=int(wvertex(p,h).real+wvertex(p,h).imag)%4;assert sector==2
A=component(L,sector,wvertex(p,h))[1];mark=component(L,sector,ends(2j,sector)[0])[1];assert len(A)==6 and len(mark)==15 and not(A&mark)
def profile(B):
 todo=set(B);out=[];sizes=[]
 while todo:
  q=min(todo,key=xy);vs,es=component(B,sector,ends(q,sector)[0]);todo-=es;sizes.append(len(es));base=min(vs,key=xy)
  out.append(tuple(sorted(tuple(sorted(xy(v-base)for v in ends(e,sector)))for e in es)))
 return sorted(out),sorted(sizes)
# Exact affine fields (coefficient*n+offset), not fitted from finite observations.
ports=[(1+1j,-1+0j,0),(-1+3j,-4j,3),(-5-1j,5+0j,2),(-3-3j,8j,1)]
groups=[('local',0j,L)]+[(str(i),a,{b+q*(-1j)**((hh-1)%4)for q in G})for i,(a,b,hh)in enumerate(ports)]
order=[3,4,2,0,1];ivs=[]
for ix in order:
 name,a,qs=groups[ix];assert len(qs)==(35 if ix==0 else 4)
 ivs.append((name,int(a.real),min(int(q.real)for q in qs),max(int(q.real)for q in qs)))
gaps=[]
for u,v in zip(ivs,ivs[1:]):
 aa=v[1]-u[1];bb=v[2]-u[3];assert aa>=0 and 20*aa+bb>=9;gaps.append((aa,bb,20*aa+bb))
assert [z[2]for z in gaps]==[32,36,20,9]
# Translation by every admissible parameter difference preserves the FIXED lattice.
assert all(int((2*a).real+(2*a).imag)%2==0 for _,a,_ in groups)
base_profile=None;controls=[]
for n in [20,22,40,80,1000000]:
 initial=set(G)
 for a,b,hh in ports:initial|={a*n+b+q*(-1j)**((hh-1)%4)for q in G}
 assert len(initial)==20
 B=set(initial);pp=0j;hh=1
 for t,(q,h0,c)in enumerate(rd):
  assert(pp,hh,'L'if pp in B else'R')==(q,h0,c);pp,hh,_=step(B,pp,hh)
 expected=set().union(*[{a*n+q for q in qs}for _,a,qs in groups]);assert B==expected
 typ,sizes=profile(B)
 assert len(B)==51 and sizes==[1]*10+[2]*5+[6,10,15] and component(B,sector,wvertex(pp,hh))[1]==A and component(B,sector,ends(2j,sector)[0])[1]==mark
 if base_profile is None:base_profile=typ
 assert typ==base_profile;controls.append({'n':n,'mass':len(B),'sizes':sizes})
ref=json.loads((D/'twenty_cell_type_profile_certificate.json').read_text());assert sorted(map(xy,L))==list(map(tuple,ref['local_field_173'])) and sorted(map(xy,A))==list(map(tuple,ref['active_component']))
assert ref['named_controls'][0]['component_types']==json.loads(json.dumps(base_profile))
notes={'GLOBAL_COMPONENT_TYPE_FUEL_LIMITS.md':'fab336f3de6843cfcab406fb875507532599dd0ffaa30cadaed59db410231dec','check_twenty_cell_type_profile.py':'d1e821d5cc257ebd507e8af06982c5494115e6016aa244ce1a9c10dc407e464f','twenty_cell_type_profile_certificate.json':'635adda34e08c3041faa92084f4d9d4aa4ee5f48b6af9bfc088a49d5d93b1d10'}
for p,h in notes.items():assert sha(D/p)==h
out={'status':'PASS exact global component-type potential scope limits and all-even-n fixed full profile','author_hashes':notes,'controls':controls,'affine_intervals':ivs,'affine_gaps':gaps,'marked_R60_cell':xy(2j),'marked_archive':sorted(map(xy,mark)),'active_component':sorted(map(xy,A)),'source_dependencies':{p:sha(R/p)for p in ['causal_reduction/unit_scale/prepared1564_original_bistandard_family.md','standard_unread_cap_2026-10-23/W_FRONTIER.md','active_w_archive_itinerary_2026-10-23/TWENTY_CELL_SUSTAINED_CAP.md','reframe_finite_seed_2026-10-24/PARAMETER_FREE_SATURATION_AND_FUEL_SCHEMA.md']},'analytic_review':[
'For complete finite mass m, connected embedded graph types up to translation and rooted active types are finite, with at most m passive components. Finite nonnegative type weights therefore give a placement-independent uniform initial upper bound. With a GLOBAL lower bound and global nonincrease INCLUDING preparation, arbitrarily many actual1564 copies from fixed184 defeat any fixed strictly positive per-copy charge. This does not exclude conditional ranks, spatial/ancestral types, or preparation gains.',
'The signed cleared standard whole-field decomposition has identical translated active/frontier types and one extra COMPLETE disjoint12-edge tree per period; other legacy components remain unchanged. Thus the potential increment is exactly W(T12), forcing W(T12)=0 under global nonincrease and nonnegative W. This is not a claim of future usefulness of these trees.',
'For the twenty-cell family, every read through172 lies in the exact local box, disjoint from the other four affine port groups for every n>=20. Therefore the complete field at173 is precisely local35 plus those16 unread initial cells. Its affine x gaps32/36/20/9 at20 are nondecreasing, so different groups cannot share any diagonal vertex; no hidden attachment or extra component is omitted.',
'Every admissible even parameter shift preserves the fixed diagonal lattice and translates each old port without rotating it. Thus the entire18-component TYPE MULTISET is exactly constant, with sizes ten1/five2/6/10/15. Active geometry/head and the unchanged actualR60 lifetime in the15-edge archive are identical too. Named replays are controls; separation and translation are the all-parameter proof.',
'The prior signed all-time501229 cap and wait624n-1778 are used as dependencies, not re-inferred from these finite replays. The type summary cannot provide a uniform waiting deadline across this family, although each member captures. No one-orbit noncapture, impossibility of every potential, or new attraction theorem follows.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
