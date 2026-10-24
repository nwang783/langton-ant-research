# Phase-forced quarter-turn/through return: an untouched guard obstruction

23 October2026,10:44UTC. Author exact finite-word/phase calculation, submitted
for independent review. This is a CONDITIONAL interface obstruction. It does
not assert that the missing return route exists, nor exclude additional repair
work that visits the stated witness.

## Frozen interfaces and complete fields

C is the independently signed43871-letter NW-to-NE word in
`opposite_wake_quarter_turn_word.json`. The complete parametric input, entry,
and output boards are in `opposite_wake_quarter_turn_certificate.json`.
Its old NE profile has canonical origin0; incoming NW phase is a=(3,0),
collision starts(23,-20,N), and its output NE canonical origin is b=(91,-63).

T is the27928-letter NW-through-NE word in
`opposite_wake_through_phase21_word.json`. Its separate complete prepared-input
certificate is AUTHOR-ONLY, not a dependency of the conditional obstruction
below. Relative to its old NE origin0, its incoming phase is(2,1), its start
is(22,-19,N), and its output canonical origin is b_T=(-18,29,N). Its complete
read list and XOR1578 are frozen. `certify_opposite_wake_through_phase21.py`
checks the candidate independently of any composition; no transfer of that
input contract to C's actual output is assumed here.

## Why the second phase is forced in the clean four-link bookkeeping

Use the profile phase quotient

    Lambda = Z(2,2)+Z(-2,2).

A class is determined by x mod2 and(x+y)mod4. Let J be clockwise90-degree
rotation, and put a_j=J^j a, b_j=J^j b. A right-turn C encounter with old
profile origin P_j requires incoming origin P_j+a_j modulo Lambda and emits
origin P_j+b_j. If four old profiles are phase-compatible for a closed cycle
of these encounters, their successive differences satisfy

    P_(j+1)-P_j = b_j-a_(j+1) modulo Lambda.

This is an explicit compatibility hypothesis, not inferred just from seeing
four turns. After the first profile has been replaced by the newly written
profile P_0+b, a returned incoming phase P_0+a meets it in class

    a-b=(-88,63) = (2,1) modulo Lambda,

not the(3,0) class required by C. Thus drift and quarter-rotation matching alone
cannot directly repeat this turning rule on its own new rail.

## The proposed T bridge and its precise local failure

Normalize P_0=0 and the returning incoming NW canonical line to x+y=3.
The new NE profile b may be represented with origin

    O_T=b-7(2,2)=(77,-77).

The phase-consistent T would start at(99,-96,N), end at(59,-48,N), and then
sixteen canonical H periods would reach(27,-16,N). This last pose is exactly
C's original start translated by(4,4). Thus the tempting local proposal is
T, H^16, then C translated by(4,4), following some unprovided return route.

It FAILS without additional work on the old strip. Specifically q=(5,4) is
white on the original mature NE profile. The first C reads it eleven times,
with alternating history RLRLRLRLRLR, and leaves it black. The translated C
first reads q at its zero-based update888 and requires R, hence white.
There are307 first-read mismatches on the old strip in the full comparison;
one untouched witness is enough.

The relevant normal is z=x-y. The old complete black strip is -7<=z<=3 and
q has z=1. All the following bounds are exact literal geometry, independent
of whether the proposed composition is ant-legal:

- Every outgoing H read after the first C has147<=z<=157, for arbitrarily many
  periods, since the NE drift preserves z.
- Every T read translated by O_T has101<=z<=213. This is a finite-word bound,
  not a claim about an unlimited subsequent NW tail.
- The sixteen H periods from T's endpoint to the proposed next C have z>=37.
  More generally all canonical NW periods strictly before that next C cut
  have this lower bound, from the one-period minimum and the+4 backward drift.

Therefore these pieces cannot change q. If all other return-route work also
avoids q (in particular if it avoids the old strip), the next shifted C has
this forced first-read conflict. Allowing a return route that repairs q, a
different phase word, a different translation, or another affected input
profile is OUTSIDE this narrow statement.

For an explicit complete-board formulation, let B_C be the signed complete
C-output relation. Apart from the unprovided return route, the proposed board
before the second C is exactly

    B_C XOR (O_T+X_T) XOR X_(H^16 from(59,-48,N)).

The frozen word files supply both finite XORs. The omitted route is not
silently assigned zero XOR: the theorem requires its XOR at q to be zero.
No claimed infinite run is assembled from these formal updates.

`check_quarter_turn_two_phase_guard.py/json` reconstructs the quotient,
translations, all normal bounds and the first-white witness directly. The
T all-parameter legality certificate is separate and remains pending audit.
