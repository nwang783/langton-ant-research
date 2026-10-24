# Old consumed memory must arrive through a recent productive R import

24 October 2026. A short conditional placement corollary of the independently
signed active-episode clock. This is not a new bounded-age-to-periodicity
theorem, and no sustained active-component bound is inferred from finite input.

## 1. Actual event and exact last-active-episode identity

Retain the COMPLETE black board at every physical cut, with active w component
C_t. Suppose |C_t|<=M for every t>=T, where M>=1. As in ACTIVE_EPISODES.md put

    H=Q(2M+1),       Q(n)=4 n^2 2^(n^2).

The signed metric/escape lemma bounds every continuous active episode by H
integer cuts, including the intermediate cuts of R-only resets.

Fix an eventually consumed lifetime x born at an R update b>=T and next read
at L update d. If it is active at every cut b+1,...,d, its age d-b is at most H.
Otherwise let r be the update immediately before its LAST active episode.
The exact signed gate theorem says that r is a genuine nonempty R import of
the COMPLETE dormant component containing x. Its last active episode is
EXACTLY the cuts

    r+1,...,d,         number of cuts = d-r <= H.

In particular x is actually consumed before its next archival departure, not
merely imported temporarily and left dormant again. Call an import productive
for a particular lifetime when this actual consumption-before-next-dormancy
property holds. A productive import may still contain other lifetimes never
consumed in that active episode. Do not charge the whole component as causal
consumed input.

Writing its birth-to-import age as r-b gives the exact identity

    d-b = (r-b)+(d-r),       d-r<=H.                     (1)

Therefore any consumed lifetime of age L>H has a last productive import with
birth-to-import age at least L-H, followed by consumption within H updates.
The imported complete component has at most M-1 edges, by the importing R's
extra edge. It is literally frozen during the immediately preceding dormant
episode. That LAST dormant episode need not itself be the long excursion
guaranteed in BOUNDED_ACTIVE_FROZEN_EXCURSIONS_v2.md; do not merge these claims.

## 2. A scope-specific organization criterion

If there is a uniform A such that every late R-born lifetime consumed after
having been dormant has birth-to-LAST-productive-import age <=A, then (1)
gives every such consumed age <=A+H. Lifetimes never dormant have age <=H.
After removing the finitely many lifetimes already present at T, the RETAINED
bounded-consumed-age theorem in
`../sources/kehao95-core/memory_feedback/proof/stale-memory.md` gives eventual
nonzero translating periodicity, not necessarily104.

This condition does NOT require that every imported edge be young. It concerns
only actual R-born lifetimes consumed before that lifetime's next archival
departure.
Unconsumed old cycle support and unproductive temporary imports are not
charged. It is a placement of the old stale-memory obstruction in the actual
white-read whole-component import chronology, not an independent attraction
argument or a finite state summary.

## 3. Necessary old causal imports on a bounded-active nontranslating orbit

Suppose instead that the trajectory is not eventually translating while the
same sustained cap M holds. For every age threshold A, finite spatial set K
and tail time T'>=T, the RETAINED remote-stale-feedback.md Section7/Theorem6
provides infinitely many distinct unbounded cells x outside K with R births
b>T' and consumption age greater than A+H. Apply (1) to EACH lifetime. Its
last productive R import has birth-to-import age >A, brings in a complete
frozen component of at most M-1 edges, and is followed within H updates by
the ACTUAL consumption of that old R-born lifetime.

Thus the required migrating memory cannot consist only of unread topology or
of old components that are endlessly touched and discarded without using
their old contents. Arbitrarily old causal input must repeatedly enter an
active component and be consumed in one uniformly bounded active episode.
The importing update is spatially near x: its post-R active component contains
x and the same stationary w cursor, so the metric proof gives head distance
at most M at that importing pre-update cut as well.

The migrating-cell and arbitrary-age quantifiers are inherited from the cited
remote theorem. The new corollary only gives the exact last-import location
and bounded final active delay under the sustained active cap. Neither this
cap nor a bound A has been established on arbitrary finite-seed trajectories.

## 4. Actual controls and remaining gap

The signed twenty-cell family has one sustained all-component cap independent
of its spacing parameter, yet an R60 token with unbounded birth-to-consumption
age across the family. Hence these scopes are not empty. Named n20,40,80
complete-board controls in twenty_cell_active_cap_probe.json show the final
active episode of that token has exactly10 cuts, starting at e-9; its last
import is at e-10. Those offsets are named controls ONLY, not an all-parameter
claim in this note. Every member of the all-parameter family still captures.

On an actual standard104 tail the separately signed W_FRONTIER.md proves all
complete active-w lifetimes are eventually young (age<=240), hence productive
imports are young too. This is conditional standard organization, not evidence
that all arbitrary trajectories acquire it.

A global attraction proof with bounded active components would therefore need
to constrain indefinitely renewed OLD productive imports, while permitting
young self-fed imports and keeping all complete dormant archives. No such
constraint or eternal finite-seed counterexample is claimed here.
