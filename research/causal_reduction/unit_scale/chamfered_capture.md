# Exact actual capture after the chamfered-frame near-renewal

23 October 2026, 07:25 UTC. Independently signed exact certificate (audit KN).
This is one explicit two-parameter finite seed family, not a global result.

For every integer r>=10,k>=10, start from the exact minimum input I_(r,k)
in `chamfered_frame_nearrenewal.md`, with head(0,0,E). The first
16r+8k+4 turns execute the proved self-avoiding outward frame, leaving exactly
O_(r,k) and the same head pose. The ACTUAL continuation is

    P V^(r-1) C H^infinity,

where |P|=50, |V|=20, |C|=257, |H|=104. Every literal word is frozen in
`chamfered_capture_certificate.json`; specifically

    V = LRLLLLRLRRRRLRRRRLLL.

The104 tail starts after20r+287 continuation turns, hence at total time
36r+8k+291 from the original seed. Its pose is(2r+1,4,N), and H has displacement
(-2,2) and restores N. These are sufficient phase boundaries, not claimed
minimal capture times or minimal parameter thresholds.

## Exact unbounded check

`certify_chamfered_capture.py` compiles431 affine read families for the two
fixed segments, one repeated20-arm and every future104-period slot. Each
family has a Presburger domain(r,k,x,y) with r,k>=10 and a unique chronological
time at each cell. The repeated-arm and infinite-tail drifts are nonzero,
so one family never reads the same cell twice for fixed parameters.

For each family, intersect its cell domain with the COMPLETE O_(r,k) black
relation from `chamfered_frames_certificate.json`. XOR the domains of ALL
prior same-cell reads from every other family, using strict exact affine
time comparisons. The resulting current-color relation agrees with the
prescribed R/L turn everywhere. All185,330 ordered distinct-family pairs
are checked, with923 nonempty earlier-read relations and no bad read set.
No compatibility pruning is used. Infinite tail repetitions are quantified,
not replaced by a long finite simulation. The two-parameter seed relation
is essential: distant untouched frame cells are retained, not discarded.

The continuation candidate was discovered from finite samples; discovery
alone proves nothing. Exact chronology from the specified initial field and
determinism establish the all-parameter/all-future statement. Any resource
exception is an error, not an empty relation or a proof.

The checker source, candidate-selection input and full seed relation are
bound by `chamfered_capture_hashes.txt`. The certificate records exact words,
pose coefficients and libisl version. Other finite perturbations, small
parameter regions, changed corners, or a different two-phase frame operator
remain outside this result.

## Independent review

The independent checker rebuilt the complete initial output from literal side
words and checked all185,761 ordered family pairs, INCLUDING self, using explicit
repeat indices rather than the author inverse-time formula. All923 nonempty prior
relations agree and every bad domain is empty. The tail is exactly the retained
standard104 word. This signs the stated all-r,k>=10 theorem without changing its
threshold or scope.
