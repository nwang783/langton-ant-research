"""Signed-premise assembly and exact arithmetic; no search or lower-parent shortcut."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;W=R.parent
DEPS={
 'causal_cycle_renewal_20261023_1841/manifest.json':'27db0bc457534074587a988c16bbf57c994464656df7c9aa06427ab23203d7d4',
 'U_renewal_exact_clock_frozen_20261023_1902/manifest.json':'91f5cb870b1dacd19c793820cef537c1410bca05c8b71294d80a2ccc823b7fd6',
 'genealogy_role_speed_frozen_20261023_0840/manifest.json':None,
 'chronology_dcuv/literal_residual_geometry.json':None,
 'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv':None,
}
for f,sha in list(DEPS.items()):
 got=hashlib.sha256((W/f).read_bytes()).hexdigest()
 assert sha is None or sha==got
 DEPS[f]=got
G=json.loads((W/'chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
root=json.loads((W/'genealogy_role_speed_frozen_20261023_0840/optimal_speed_root_potential.json').read_text())
assert root['K']==13
assert all((0,3)in map(tuple,G[a]['inputs'])for a in(7,8,9))
# The U parent of the signed role graph is upper d. It is deliberately NOT
# reused as a certificate for a lower-east ancestry edge.
source=(W/'genealogy_role_speed_frozen_20261023_0840/genealogy_role_two_thirds_speed.md').read_text()
assert 'floor((2*j+13)/3)'in source

# Exact equivalence of the claimed finite-chain inequality. This is an
# integer identity for arbitrary M,j; finite controls merely check coding.
checks=0;examples=[]
for M in range(101):
 for j in range(1,3*M+25):
  lhs=3*j<=M+(8*j+5)//3
  rhs=j<=3*M+5
  assert lhs==rhs;checks+=1
 if M in(0,1,2,3,10,100):
  examples.append(dict(max_entry_root_rightward_coordinate=M,maximum_renewals=0 if M<3 else 3*M+5,maximum_U_events=1 if M<3 else 3*M+6))

# Optional typed renewal restrictions, all at the exact full-source C gap4.
IDS=(0,1,4,5,6,7,8,9);mp={a:i for i,a in enumerate(IDS)}
COUNT={tuple(map(int,l.split()[:8]))for l in(W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()}
types=[];allowed=set()
for a in(7,8,9):
 for b in(7,8,9):
  queries=[(mp[a],mp[b],3,-1,0,*o,4)for o in((2,0),(2,1))]
  excluded=[q in COUNT for q in queries]
  assert excluded[0]==excluded[1]
  row=dict(source_packet=a,source_name=G[a]['name'],breaker_packet=b,breaker_name=G[b]['name'],count4_queries=queries,count4_excluded=excluded)
  types.append(row)
  if not any(excluded):allowed.add((a,b))
assert allowed=={(7,7),(7,8),(8,7),(9,7)}
assert all(b!=9 for a,b in allowed)

out=dict(status='AUTHOR_ANALYTIC_SIGNED_PREMISE_ASSEMBLY_PENDING_INDEPENDENT_REVIEW',scope='A single directed U-cycle inheritance chain inside an actual complete recurrent-eight suffix, reset at that chain head. Spatially sensitive finite length only; not a bound on chain births or total U.',normalization='First chain U has head(0,0,N), C clock0; all entry residual identities are separate roots. M=max root x>=0.',theorem='The j-th chain U has pose(3j,-j,N), C clock4j. Its upper d identity at(3j,3-j) is already current at clock4j-4. The global signed root-box theorem implies j<=3M+5 for j>=1. If M<3, no renewal exists; otherwise at most3M+5 renewals and3M+6 U events.',integer_equivalence='3j <= M+floor((8j+5)/3) iff j<=3M+5',arithmetic_controls=checks,examples=examples,typed_renewal_rows=types,unexcluded_typed_edges=sorted(allowed),corollaries=['No individual cycle inheritance chain can be infinite on a finite entry board.','Infinitely many U events would require infinitely many separate finite chains.','The terminal cycle of each such finite chain is permanent for the remaining complete-eight history; infinitely many U therefore require infinitely many distinct permanent unit cycles.'],not_claimed=['No uniform mass-only chain-length bound.','No upper bound on separate chain births.','No historical-component merger theorem or global U/confinement/capture theorem.','No selected-role inequality is asserted for a lower-east input ancestry edge.'],dependencies=DEPS)
(R/'chain_root_budget.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],arithmetic_controls=checks,typed_edges=sorted(allowed),bound='j<=3M+5'),indent=2))
