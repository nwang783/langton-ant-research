from pathlib import Path
from collections import defaultdict
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'MIDDLE_SHORT_FOUR_BOUNDARY_TYPES.md':'020d0dbcb303130c57bb8c8aefe7df9ed8dce1728785d610e2bd24307759a2ed','certify_middle_short_four_boundary_types.py':'c080e3fbf569f0675522d6047db7eef15f3841adc6b1d6e10a3f63c6b3eb93c7','middle_short_four_boundary_types_certificate.json':'2336b5687658316a4e92883d05b225ffff7041739f6201b2f03441941be8870a'}
for f,h in files.items():assert sha(D/f)==h
J=json.loads((D/'middle_short_four_boundary_types_certificate.json').read_text());old=json.loads((D/'lifetime_boundary_graph_certificate.json').read_text())['middle_short28_boundary_pairing_types']['all28_types']
for f,h in J['dependencies'].items():assert sha(D/f)==h
H={int(k):v for k,v in J['complete_lower_histories'].items()};assert H==dict(enumerate(['S','W','S','EEWE','SSNS','EEWE','NNNSS','EEEWW']))
forced=[]
for x,y in [(0,1),(6,7)]:
 src=[i for i,c in enumerate(H[x])if (('NESW'.index(c)+(1 if i%2==0 else -1))%4)==3];dst=[i for i,c in enumerate(H[y])if c=='W'];assert len(src)==len(dst)and(src[-1],dst[-1])==(len(H[x])-1,len(H[y])-1)and src[-1]%2==dst[-1]%2==0
 assert y==x+1;forced.append((src,dst))
for (src,dst),z in zip(forced,J['actual_forced_horizontal_output_components']):assert z['complete_source_port_ranks']==src and z['complete_target_port_ranks']==dst and z['physical_voltage']==0
# Rebuild all complete noncrossing matchings, not author matching generator.
def perfect(v):
 if not v:return [()]
 a=v[0];return [((a,b),)+m for k,b in enumerate(v[1:],1)for m in perfect(v[1:k]+v[k+1:])]
def nc(m):return all(not(a<c<b<d or c<a<d<b)for i,(a,b)in enumerate(m)for c,d in m[i+1:])
hs=[m for m in perfect(tuple(range(8)))if nc(m)];vs=[((0,3),(2,6))+m for m in perfect((1,4,5,7))if nc(m)];assert len(hs)==14 and len(vs)==2
kept=[(h,v)for h,v in product(hs,vs)if(0,1)in h and(3,4)in h];assert len(kept)==4
coef=[(0,0,0),(0,0,1),(0,0,2),(0,0,6),(0,0,7),(0,6,1),(6,0,2),(6,0,4)]
expected=set()
for h,v in kept:expected.add(tuple(sorted([('H',a,b,(0,0,0))for a,b in h]+[('V',a,b,tuple((y-x)//3 for x,y in zip(coef[a],coef[b])))for a,b in v])))
actual=set();cycletypes=[]
for r in J['four_necessary_open_types']:
 es=[(e['axis'],*e['ends'],tuple(e['voltage_coefficients_a_c_constant']))for e in r['edges']];actual.add(tuple(sorted(es)));adj=defaultdict(list)
 for axis,a,b,v in es:adj[a].append((b,v,axis));adj[b].append((a,tuple(-x for x in v),axis))
 seen=set();polys=[]
 for c in r['unoriented_cycles_with_one_declared_orientation']:
  ns=c['vertices'];assert not seen.intersection(ns);seen.update(ns);vv=[0,0,0]
  for a,b in zip(ns,ns[1:]+ns[:1]):
   opts=[v for z,v,ax in adj[a]if z==b];assert len(opts)==1;vv=[x+y for x,y in zip(vv,opts[0])]
  assert vv==c['winding_coefficients_a_c_constant'];polys.append(vv)
 assert seen==set(range(8));essential=[v for v in polys if any(v)];assert len(essential)==1
 v=essential[0];assert v in([0,-2,1],[-4,2,-1],[4,-2,1]);cycletypes.append(polys)
assert actual==expected
ids=lambda r:(r['horizontal_choice'],r['vertical_choice'])
keepids=set(map(ids,J['four_necessary_open_types']));dropids=set(map(ids,J['all24_excluded_types']));assert not keepids&dropids and keepids|dropids==set(map(ids,old))and len(dropids)==24
for r in old:
 missing=[p for p in [(0,1),(3,4)]if not any(e['axis']=='H'and tuple(e['ends'])==p for e in r['edges'])];assert bool(missing)==(ids(r)in dropids)
out=dict(status='PASS four necessary boundary types only; all remain open',script=sha(S),files=files,forced_ports=forced,original_types=28,rejected=24,remaining=4,cycles=cycletypes,analytic_review=['The two moves connect actual LAST-R endpoints. Each endpoint has no outgoing lifetime, and the actual horizontal unit move has no intervening vertex. Hence these are complete horizontal boundary components, not merely subpaths or geometric adjacency. Full port ordinal matching gives6 rank4 to7 rank4, not an arbitrary W match.','Full representatives(-T,0) give horizontal voltage0 and vertical voltage(Tj-Ti)/3. Full odd order stays strict at a=c. Complete noncrossing row and column fibre covers are rebuilt without assuming combined projected planarity.','Every surviving graph has one nonzero-voltage component and optionally one zero-voltage component. Absolute windings are2c-1 or4a-2c+1; c>=3,a>=c give minimum5. This is an exact prospective obligation, not a realization, unit-winding impossibility or exclusion of any remaining branch.'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
