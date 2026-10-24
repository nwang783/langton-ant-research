# Fresh-record constraints for rectangular rather than scalar inflation

2026-10-23 00:17 UTC; signed extension added 00:25 UTC. Status: Sections1–4
independently reviewed by the audit analysis.
This keeps the two different coordinate multipliers separate. In particular,
the old scalar (k,a)=(13,5) exclusion MUST NOT be imported for diag(3,5).

## 1. Pure positive diagonal inflation

Suppose an actual finite-support ant satisfies

    p(kn)=diag(a,b) p(n) for all n>=0,

where a,b>1 are integers. There is no finite-controller or image-word assumption.
Pure matrix parity forces either a,b odd and k=4ell+1, or a,b even and k=4ell.
Write epsilon=1 or0 respectively. For z equal to either a or b put

    s_z=ell+(epsilon-z)/2,
    h_z=max(0,z-ell-1).

Then each of the following is necessary:

    s_a>=c(h_a),                 s_b>=c(h_b),                 (1)

where c is the audited pristine-climb cost. In particular we may use

    C(h)=7 floor(h/3)+(0,1,3)[h mod3] <= c(h).

The two coordinate directions are both unbounded in absolute value: some
position has each coordinate nonzero (unit moves alternate axes), and pure
positive diagonal inflation scales that coordinate indefinitely. Rotate the
chosen sign of either unbounded axis to north. The other multiplier remains
different but does not enter the following height calculation.

A north-displacement macro of height z has s_z south moves and maximum height
at most z+s_z. A macro whose coarse step is not north has height at most ell
above its center: horizontal macros have ell north moves, and a south macro
has only s_z<=ell north moves. Before the predecessor of a high coarse north
record Y, the rows at or above zY-z+ell+1 are therefore pristine white, exactly
as in the audited scalar fresh-band argument. The predecessor has to climb
h_z pristine rows before its endpoint. This costs at least c(h_z) south moves,
proving (1). The horizontal endpoint displacement has played no role.

## 2. Correct anisotropic one-retreat coupling

If s_b=1 and h_b>=1, the pristine argument forces h_b=1 and the predecessor
ends with the known one-south crossing F=RRRRLR, or the allowed even-phase F R.
The exact next-macro local history forces at least TWO backward horizontal
moves within the next seven reads. Its horizontal displacement is a, not b.
Thus the correct necessary consequence is

    s_b=1 and h_b>=1 implies s_a>=2,
    s_a=1 and h_a>=1 implies s_b>=2.                         (2)

The proof is precisely the two already-audited local F/F R histories in
`fresh_band_inflation_obstruction.md`, Section7; only their final budget changes.
The cases in question have macro length at least13, so all forced reads lie
inside that next macro.

For diag(3,5), k=13, one has ell=3, (s_a,s_b)=(2,1), and (h_a,h_b)=(0,1).
It passes (1) and (2). The old scalar k13,a5 model instead had (s_a,s_b)=(1,1),
which failed. This is a real surviving rectangular possibility, not a found ant.

## 3. Conditional finite list when the smaller multiplier is three

Suppose also that an independent argument gives k<=ab. For example the separate
independently signed half-turn-symmetric area/excess obstruction supplies
this necessary condition for its stated substitution/directive class.
The ACTUAL same-path identity from Section1 remains essential here. An arbitrary
directive limit need not satisfy it, and a general first-letter two-cycle gives
only the squared-parameter identity unless an additional symmetry is proved.
No directive/root-cycle-wide four-case list is inferred merely from an area bound.

Let a=3 and let b>=3 be odd. Combining k<=3b, k=1 mod4, and (1) leaves ONLY

    (a,b,k)=(3,3,9), (3,5,13), (3,7,21), (3,11,33).         (3)

Coordinate swaps give the same list. This reduction is conditional on k<=ab;
it is not asserted for arbitrary positive diagonal inflation.

Proof. For fixed b, s_b increases and h_b decreases with k, so it suffices first
to check the largest allowed k<=3b. If b=4j+1, that maximum is3b-2 and
(s_b,h_b)=(j,j). Since C(j)>j for j>=2, only b=5 survives with b>=3 in this
residue, giving k13. If b=4j+3, the maximum is3b and (s_b,h_b)=(j+1,j).
For j>=3, C(j)>j+1, so only b=3,7,11 survive. Substituting the immediately
smaller k values, in steps of four, eliminates all but k9,21,33 respectively.
The a=3 coordinate bound and coupling (2) hold at every displayed surviving
triple; they do not eliminate those triples.

The (3,3,9) pure scalar case is already independently excluded by the prior
fresh-record/refinement theorem, without any substitution assumption. The other
three triples are genuine remaining targets of this combined restriction, not
claims that legal images or finite seeds exist.

## 4. Half-turn first-letter two-cycles are covered

Suppose a single direction substitution phi is half-turn symmetric, has common
positive diagonal displacement A, and its first-letter map takes d to -d.
Let P_d be its phi-squared prolongable infinite word rooted at d. Half-turn
symmetry and uniqueness of this limit give

    P_(-d)=-P_d,             phi(P_d)=P_(-d).

Consequently the actual path has p(kn)=-A p(n). Although this is NOT the
positive same-path identity of Section1, exactly the same fresh bounds hold.
Use the coarse finite-support ant p and the fine finite-support ant -p. The
latter is just the 180-degree rotation of the former, and

    (-p)(kn)=A p(n).

Thus its macro endpoints, its pristine-band history bound and its turn-preserving
local coupling are precisely those used in Sections1–2. The sign changes neither
the compass parity condition nor either backward-move budget. The same
conditional four-triple list follows when k<=ab.

Combining this with the independently signed area/excess theorem yields the
four-triple restriction for BOTH fixed and antipodal two-cycle roots of a single
half-turn-symmetric direction substitution with smaller multiplier three.
This extension does not apply to arbitrary directive schedules or to independent
opposite-direction image cycles. Those require separate hypotheses.

Independent analytic review: audit analysis message at 2026-10-23 00:25 UTC.
