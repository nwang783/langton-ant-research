from pathlib import Path
import json,hashlib
R=Path('/workspace/shared/langton');P=R/'one_foreign_all_ordinary_owners_2026-10-24'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((P/'manifest.json').read_text());assert sha(P/'manifest.json')=='a21324668f65dda82871b5f940592fbffb4821d32381d0d2f68b167a759e152a'
for f,h in m['files'].items():assert sha(P/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
names=['check_ordinary_boundary_beta_independent.json','check_terminal_DCC_ordinary_owner_independent.json','check_leading_C_ordinary_owner_independent.json']
reports={n:json.loads((R/'audits'/n).read_text()) for n in names}
assert all(v['status'].startswith('PASS') for v in reports.values())
# Check the priority partition independently, without the author's branch list.
branches=[]
for first_C in (False,True):
 for terminal_second_C in (False,True):
  lane=366 if terminal_second_C else (594 if first_C else 268)
  branches.append(dict(first_ordinary_C=first_C,actor_real_terminal_DCC_second_C=terminal_second_C,lane=lane))
assert {x['lane']for x in branches}=={268,366,594}
review=[
'Truncate at the chronological global-first contact actor, retaining only real executed RAWs and its actual M11. Every internal M11 is supplied by the next actual RAW, including the D10 spill. No complete next G7 is inferred from the final marker.',
'The signed base-start grammar has maximal C runs of length at most two after V/U, and at most one after D except a real terminal DCC. A D has its genuine preceding RAW, including the first FOREIGN or earlier C, so the incoming-bud DCCC conflict applies. Internal DCC cannot precede any ordinary next RAW. Thus every base-start selected endpoint except the terminal second C is an actual G8 factor.',
'At a real terminal DCC second-C actor, signed366 directly covers outgoing ordinary old owners, including a preceding leading C. This priority prevents any false terminal-DCC parse. Its first C instead gives a genuine DC endpoint.',
'For all remaining leading-C prefixes, signed594 retains the genuine terminal CC possibilities and the first b1-C owner. Any later base follows exactly one leading C and starts D/V. Its actual source-clock translation and beta reserve are already independently signed. Leading C is never silently promoted to a G8 base.',
'All other prefixes start D/V/U and have real G8 endpoints, exactly the scope of signed268. Its universal signed129 first-contact geometry is not merely the U-entry corollary; actual source positions and b1 closures are bound in that report.',
'All three reports retain the same genuine initial U-entry complete-eight factor, its FIRST FOREIGN and global-first-contact stopping premise. Their conclusions exclude only postFOREIGN ordinary outgoing old owners. A FOREIGN terminal vertex is assigned to its actual outgoing b1 ordinary owner, while proper originalFOREIGN and all preFOREIGN owners remain outside.',
'No guard is extended through its contact actor, no old maturation law crosses FOREIGN, and no prepared positive is removed. Original143d universal F-pair claim remains rejected; this composition uses only its separately retained common sublemma through the signed594 proof.'
]
out=dict(status='PASS_SCOPED_DEPENDENCY_COMPOSITION',manifest_sha256=sha(P/'manifest.json'),proof_sha256=sha(P/'owner_join.md'),dependencies=m['dependencies'],independent_lanes={n:sha(R/'audits'/n)for n in names},priority_partition=branches,analytic_review=review,conclusion=m['scope'],nonclaims=['No arbitrary-tail simplicity','No proper originalFOREIGN or preFOREIGN source exclusion','No second FOREIGN or universal attraction','No newly replayed role table; previously independently signed lanes only'])
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n');print(sha(p))
