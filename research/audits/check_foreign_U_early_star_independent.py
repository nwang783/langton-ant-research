from pathlib import Path
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';old=R/'audits/check_foreign_U_tag_interfaces_independent.py';ns={'__file__':str(old)};exec(old.read_text().split('results={}')[0],ns);G,K,L,at,oldcenter,W,walk,xy=(ns[k]for k in('G','K','L','at','oldcenter','W','walk','xy'));data=json.loads((D/'foreign_U_early_star_exclusion.json').read_text());gates=set()
for a in'FQB':
 g=G[a]
 for tag,slot,h in product(L,g['I'],range(4)):
  p=tag-at(slot,0,h)
  if(int(p.real+p.imag)+h)%2 or L&{at(q,p,h)for q in K|g['white']}or oldcenter(p,h):continue
  gates.add((a,int(p.real),int(p.imag),h))
assert len(gates)==69
zero={g for g in gates if g[3]==0};one={g for g in gates if g[3]==3};assert len(zero)==len(one)==18
zpass={g for g in zero if g[1]>=0 and g[2]-4>=g[1]};opass={g for g in one if g[2]>=5 and g[1]<=(0 if g[2]==5 else 1)}
assert zpass=={('B',2,6,0)};assert opass=={(a,1,6,3)for a in'FQB'};assert all(g[2]<=6 for g in one)
# Exact surviving equations: zero case d+v=2,d+3v+4u=2 =>v=u=0,d2.
assert[(d,v,u)for d,v,u in product(range(3),repeat=3)if d+v==2 and d+3*v+4*u==2]==[(2,0,0)]
# One case positive y budget is one; g affects only x and is forced zero
# by the maximal x=1 case. No unbounded variable is silently capped.
assert[(d,e,f)for d,e,f in product(range(2),repeat=3)if d+e+f==1 and d-e-3*f>=1]==[(1,0,0)]
for ref in data['forced_word_conflicts']:
 w=''.join(W[a]for a in ref['recipe']);stop=ref['actual_prefix_length'];p,h,odd,req,reads=walk(w[:stop]);seed={q for q,b in req.items()if b};assert sorted(map(xy,seed))==ref['actual_consistent_prefix_seed'];assert w[stop]=='L';assert not(req[p]^(p in odd));assert {q for q in seed^odd if q in L}==L
 cf=ref['immutable_conflict'];assert xy(p)==cf['cell'];assert reads[p]==[(cf['previous_reads'][0][0],'L')];assert stop in(69,91)
manifest=D/'foreign_U_early_star_exclusion_manifest.json';assert hashlib.sha256(manifest.read_bytes()).hexdigest()=='84e4dbff1daef858ba3931b93c27eea4a1fce68cf754d021b6a76b78822819b6'
out={'status':'PASS no first-foreign original U-star effect at source-entry C ages0 or1','manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest(),'note_sha256':hashlib.sha256((D/'foreign_U_early_star_exclusion.md').read_bytes()).hexdigest(),'full_gate_count':69,'zero_heading_gates':18,'one_heading_gates':18,'forced_words':['UDDB','UDCF','UDCQ','UDCB'],'analytic':'The exact nonnegative head equations reduce all N gates to d2 and all W gates to sole d1 before C, with all post-C counts zero. In the y6 equation v/u vanish and d+e+f=1; x1 forces d1 and g0, so unbounded W-U motion cannot escape the uniqueness proof. Four literal prefixes force R instead of proposed L while all original star tags remain black.','scope':'Minimum age only for first foreign RAW star retirement or actual marker-only exit-core absorption. No exclusion of a star-missing foreign, age>=2, or postforeign permanence.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
