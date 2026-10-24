from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'kernel_cycle_lift_2026-10-24';F=R/'reframe_finite_seed_2026-10-24';p=SELF.with_name('check_cycle_birth_finite_fuel_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('cells=')[0],ns);component,ends,step,wvertex=[ns[k]for k in('component','ends','step','wvertex')];xy=lambda z:(int(z.real),int(z.imag));ser=lambda B:sorted(map(xy,B))
def comps(B,k):
 left=set(B);out=[]
 while left:
  q=next(iter(left));C=component(B,k,ends(q,k)[0])[1];out.append(C);left-=C
 return out
def small(B,k=0,cap=2):return sum(len(C)<=cap for C in comps(B,k))
seed={-1,-2j,-1j,2+1j};B=set(seed);p=-1-1j;h=0;word='RL'+'RRRRLLLLRLRL';born={q:None for q in B};rows=[];A=json.loads((D/'one_branch_fuel_limit_certificate.json').read_text())
for t in range(len(word)+1):
 w=wvertex(p,h);z=2*p+(-1-1j)*(-1j)**h;cw=component(B,0,w)[1];cz=component(B,2,z)[1];r={'cut':t,'pose':[xy(p),h],'field':ser(B),'active_w':ser(cw),'active_z':ser(cz),'components':sorted(ser(c)for c in comps(B,0)),'fuel':small(B),'births':sorted((xy(q),b)for q,b in born.items())};rows.append(r)
 ref=A['trace'][t];assert(r['field'],r['active_w'],r['active_z'],r['fuel'])==(list(map(tuple,ref['full_black'])),list(map(tuple,ref['active_w'])),list(map(tuple,ref['active_z'])),ref['small_component_fuel'])
 assert born[-2j] is None
 if t==len(word):break
 if word[t]=='R':born[p]=t
 else:born.pop(p)
 p,h,c=step(B,p,h);assert c==word[t]
assert rows[2]['fuel']==1 and rows[-1]['fuel']==3 and max(len(r['active_w'])for r in rows)==8
assert rows[2]['field']==ser({-1-1j,-1,-2j,2+1j})and B=={-2j,0,1-1j,1+1j}and(p,h)==(2+2j,0)
# Check all small graph additions across both fixed sectors and all small thresholds.
cells=[complex(x,y)for x in range(-1,2)for y in range(-1,2)];n=0
for mask in range(512):
 B0={q for i,q in enumerate(cells)if mask>>i&1}
 for q in cells:
  if q in B0:continue
  for k in(0,2):
   for bound in range(1,6):
    delta=small(B0|{q},k,bound)-small(B0,k,bound);assert -2<=delta<=1;n+=1
peak=json.loads((R/'standard_unread_cap_2026-10-23/standard_w_frontier_certificate.json').read_text());masses=[]
for a in peak['phases'][60:65]:
 p=complex(*a['pose'][0]);h=a['pose'][1];C=component({complex(*q)for q in a['black_frontier']},2,wvertex(p,h))[1];masses.append(len(C))
assert masses==[0,39,40,41,42]
files=[D/'ONE_OLD_BRANCH_BREAKS_SMALL_COMPONENT_FUEL.md',D/'check_one_branch_fuel_limit.py',D/'one_branch_fuel_limit_certificate.json',F/'PARAMETER_FREE_SATURATION_AND_FUEL_SCHEMA.md'];hs={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in files};assert hs[str(files[0].relative_to(R))]=='2051b3d245ee161c08c4e407b87f7cdd5cf6b8f88deb851552fc0eefb7998c8d';assert hs[str(files[-1].relative_to(R))]=='19093b03c62b67d24137cc729dd6d5dd489657d9403944a1a2022f947524386e'
out={'status':'PASS finite old-branch scope countercontrol and conditional saturation/leakage schema','source_hashes':hs,'full14_update_control':rows,'small_graph_edge_addition_checks':n,'standard_phase60to64_active_masses':masses,'analytic_review':[
'The complete4-cell initial board physically executesRL+T, births the hook at0, reaches empty T entry, peaks at8 and ends empty. The unread old branch remains the SAME black lifetime throughout; splitting releases it from a3-edge component into a singleton. Complete singleton/dimer count increases1to3. Both paired fixed graphs and every fine cut were independently checked. This only refutes extending the particular cap7 small-component fuel unchanged, not cap8 exit, a different rank, or capture.',
'For anyM>=4, fourR at an empty w root create4distinct new edges. A forced connected old set of exactlyM-4 saturates the component cap and pins its entire field and white boundary. Subsequent finite geometry is exact only until an unexposed R port; a successor can further pin a final RL import by undoing its two toggles. Saturation itself does not imply loss.',
'At empty cuts, assigning finite nonnegative integer weights to COMPLETE passive components gives exact chronological emissions-minus-imports. R can join at most one other complete component; L can detach at most one nonempty far component. Every temporary emission/reimport is counted in both terms, unchanged archives cancel, and no passive merge occurs silently. A finite necessary control graph with universally nonincreasing weights and acyclic zero-cost subgraph excludes infinite paths, but existence of such a graph/weight is a separate hypothesis.',
'Adding one edge changes the number of complete components of sizes1..k by[-2,1], by isolated creation, one-component enlargement/cycle addition, or two-component merger. Summingqadditions gives[-2q,q]. A WHOLE literal-word realizing board equals its minimum board plus the sameqglobally unread edges at both endpoints, so endpoint fuel change differs by at most3q. This is static stability, not descent or a license to regard locally unread-but-later-consumed connectors as globally unread.',
'The signed standard frontier phases60..64 have complete active masses0,39,40,41,42. Thus a genuine already-standard highway itself has a saturated4R gate with38oldedges and no universal depletion. The schema does not prove bounded active mass, a finite global control graph, classification of neutral spatial recurrence, undecidability, or standard capture.'
]}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print('edge additions',n)
