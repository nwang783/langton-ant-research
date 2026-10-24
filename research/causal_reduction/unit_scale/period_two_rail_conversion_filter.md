# Period-two rail conversion needs an eight-column full drift

23 October 2026, 06:44 UTC. Independently signed analytic consequence of the
signed alternating-row charge. This is a necessary interface filter,
not a front-existence theorem or an exclusion of arbitrary wider-period wakes.

## Exact front contract

Let a full ant state (B,p,h), possibly on an infinite prepared background,
evolve after one finite period to its horizontal translate by d=2m != 0,
with unchanged heading. In each physical row y, suppose the board is eventually
period two in x on BOTH ends. Write the left asymptotic bits as O_0(y),O_1(y)
and the right bits as I_0(y),I_1(y), for even/odd x respectively. The deviation
from these two asymptotic profiles is finite in that row. Only finitely many
rows may be read; spectator rows do not matter. This is an actual full-state
finite-interface traveling front, not an externally reset sweep.

Set a_O(y)=O_0(y)-O_1(y), a_I(y)=I_0(y)-I_1(y). Then

    m [a_O(y)-a_I(y)] = 0 (mod 4)                 (1)

for every row. The sign of m is allowed and does not affect the consequences.

## Proof

Apply the signed alternating-row charge with a(y')=1_(y'=y) to the finite
sequence of actual flips during the period. Its head correction has exactly
the same value after an even horizontal translation and unchanged heading.
Consequently the finite change of sum_x (-1)^x B(x,y) is zero modulo four.
No divergent sum on the infinite prepared board is taken.

For d=2m>0, evaluate that finite difference on a sufficiently large interval
[-2L,2L-1] containing every changed cell. Translation gives

    sum_x (-1)^x [B(x-d,y)-B(x,y)]
      = m [a_O(y)-a_I(y)].

The interior terms cancel; only d left-end cells and d right-end cells remain.
Both endpoints are in their period-two asymptotic regimes. A finite interface
or defect cancels automatically. The same telescoping calculation with reversed
endpoints handles m<0. This proves (1).

## Consequences

A binary period-two row has a in {-1,0,1}. Values +/-1 are the two genuinely
alternating rails; a=0 means a uniform row, either all white or all black.

* If m is odd (d is2 modulo4), a_O=a_I exactly. Every alternating rail and
  its parity phase must be preserved; uniform rows may change black/white.
* If m is2 modulo4 (d is4 modulo8), a_O-a_I must be even. An alternating rail
  may reverse its parity, but alternating versus uniform type is preserved.
* Creating or erasing an alternating row requires m=0 modulo4, hence8 divides
  the full physical displacement d. This condition alone is not sufficient.

Thus enlarging a period/height bound while retaining full drift two cannot
produce the missing alternating-rail converter. The140 retained four-row
full-drift-two front profiles all preserve mixed rows; this is a consequence
of (1), not evidence for a new empirical rule. Folding a larger full drift
into a primitive two-column quotient would discard the relevant cap phase
and is not valid for this filter.

## Constructive relevance and limitations

The signed axial hairpin and A12/B28 operators transfer uniform solid rows
while restoring mixed rails. Composing such operators along a long side does
not move those catalytic rails. Finite corner patches cannot repair a mismatch
on an unbounded portion of a growing side. A proposed expanding finite-width
rectangular frame therefore needs some new bulk mechanism for those rows,
not just four rotated copies of the current transfer. A true full-drift-eight
prepared front is the first eligible horizontal converter; no such converter
has been constructed here.

The theorem assumes period-two asymptotic input/output and an exact translated
full interface. It does not exclude period-four or more complicated profiles,
nonperiodic sweeps, or an autonomous trajectory with no traveling interface.
