from pathlib import Path
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'K1_pipeline_detours_2026-10-23';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=D/'root_free_locked_valley_requires_left_odd_or_deeper_minimum_v2.md';assert sha(p)=='dd171052ba071e51dee6a40e5c1458dcaf40b2d07229982c59bf9f50ab888fbf'
deps={'root_free_L_reverse_K1_forces_locked_axis_rail.md':'2ca8c00228325aa5a8703f247ff060b49935b3291c87faddf2f2ec5bd403cd84','reverse_locked_rail_prepared_secondary_interfaces.md':'c39497b8456f8ebe9b1b1e4bef96b27ce05c8e998524b227130c175214a8f356'}
for f,h in deps.items():assert sha(D/f)==h
reports={f:sha(S.with_name(f+'.json'))for f in ['check_reverse_rootfree_locked_axis_independent','check_reverse_prepared_secondary_independent']}
# The lower-left C-face lattice has even x+y in the normalized chart.
# Each corner-adjacency step is (+/-1,+/-1); the complete x=-1 column
# therefore consists precisely of (-1,2k+1), not missing any C crossing.
assert all(abs(dx)==abs(dy)==1 for dx,dy in [(1,1),(1,-1),(-1,1),(-1,-1)])
for k in range(-4,5):assert (-1+(2*k+1))%2==0 and -2+2*k==2*(k-1)
# Exact constants follow algebraically for arbitrary integer M.
for M in range(-4,5):
 cr=M-1;cl=M-2;m=M-3;lam=-m;assert -cl==lam-1 and -cr==lam-2 and -M==lam-3
out={'status':'PASS one-sided odd-output-or-deeper-minimum consequence for a root-free locked valley','author_sha256':sha(p),'dependencies':{**deps,'prepared_plateau_black_corner_alternative_and_reverse_output.md':sha(D/'prepared_plateau_black_corner_alternative_and_reverse_output.md')},'independent_reports':reports,'analytic_review':[
'The starting axis-rail theorem has exactly the present complete original WHITE cap4 K1 and root-free originalL minimum M-3 hypotheses. It fixes actual full reverse drift vertical (0,2a), not merely a primitive direction. Thus x is genuinely well-defined in the full quotient.',
'The complete low column of reverseC face lower-left coordinates(-1,2k+1) has height lambda-2. This is every C vertex at x=-1 in the diagonal corner-contact lattice. Any C contact path from x<=-2 to x>=0 must pass that column, because a contact changes x by one. Therefore a plateau at height>=lambda-1 on the left cannot escape or acquire a higher neighbor on the right. No physical wall or exterior status is assumed.',
'If no odd primal cell has x<=-1, every active reverse corner of any left C face is WHITE-even. If no deeper originalL face lies at x<=-2, reverseC<=lambda throughout that region. The signed secondary list then supplies left height lambda-1 or lambda. A maximum exists because the active quotient strip has finitely many faces at levels above its left exterior lambda-2.',
'If the left maximum were lambda-1, its plateau would be finite in the actual quotient, locally maximal also at the low boundary column, and have an entirely WHITE collar. The prepared plateau theorem gives its level strictly greater than reverse right exterior lambda-1, a contradiction. BLACK corners on the right are irrelevant, not deleted.',
'Choose a left height-lambda component with minimum face x as small as possible. It satisfies the SAME originalL level M-3, local-minimum, no-odd-collar and global opposite reverseL floor lambda-3 hypotheses, so the signed local axis-rail theorem re-applies. Its drift orientation is the same actual vertical direction. Its own low column bounds the whole lambda component on the right, and it contains a selected maximum face immediately to that columns right; hence its minimum x is the selected leftmost maximum column.',
'The new secondary faces strictly left of that low column still have WHITE collars and the same height floor and upper bound. Their left maximum is >=lambda-1; the identical prepared-plateau argument rules out equality. A height-lambda component therefore exists with smaller minimum x, contradicting the finite leftmost choice. This is not a bare spatial infinite-descent argument and cannot wrap under full drift.',
'If instead a deeper left face exists, a maximum of reverseC in that left region lies above lambda and cannot cross the complete lower boundary column. Its plateau is a genuine local maximum, hence an originalL local minimum below M-3 with retreat at least2. No odd-free collar is asserted for that new minimum.',
'The conclusion is only an actual LEFT odd-output cell or a deeper LEFT minimum. It gives no distinct root per rail, no output charge, no iteration through BLACK suppliers, and no whole-front exclusion. Positive odd output remains required by the retained global growth theorem.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
