# Bounded active components reduce nontranslation to long frozen-archive excursions

24 October 2026. Version2, preserving the first frozen draft unchanged.
Separate continuation of the signed active-episode theorem.
This removes its unnecessary bound on the NUMBER of dormant episodes. It is
a conditional theorem and an exact characterization of a remaining gap, not
a proof of universal attraction or a classification of translating words.

## 1. Scope and retained ingredients

Use COMPLETE actual finite black fields and every physical pre-update cut.
The fixed w graph and active component C_t have exactly the definitions in
`ACTIVE_EPISODES.md` (signed ad3cb9f0). A lifetime at physical cell x is born
by an R at update b and consumed by its next read, an L at update d. Its
integer cuts b+1,...,d number exactly d-b. It is active when its edge belongs
to C_t and dormant otherwise. Both its first and last cuts are active.

Two retained ingredients are used, not claimed anew:

* If x belongs to C_t and |C_t|<=M, then ||p_t-x||_infinity<=M, including
  every intermediate R-only cut. This is the signed exact metric lemma.
* Put Q(n)=4 n^2 2^(n^2). An actual finite-support ant cannot have Q(n)+1
  consecutive cuts with its head in a FIXED n by n cell square. Before exit,
  exterior cells are unchanged; repetition among the Q(n) interior complete
  states would give a bounded periodic orbit, excluded by the retained
  classical escape theorem. This is the same clock as ACTIVE_EPISODES.md.

The final finite-memory implication is the RETAINED theorem in
`../sources/kehao95-core/memory_feedback/proof/stale-memory.md`, Sections1--4:
eventually bounded ages of all actually consumed lifetimes imply eventual
nonzero translating periodicity of the actual trace. It does not assert104.
Its retained remote strengthening, `../sources/kehao95-core/memory_feedback/
proof/remote-stale-feedback.md`, Section7/Theorem6, supplies infinitely many
late-born consumed lifetimes of any prescribed age at distinct unbounded
cells on every non-eventually-translating orbit. That migrating-cell result
is also attributed, not newly proved here.

## 2. The number of reattachments is unnecessary

**Theorem 1.** Suppose integers T>=0, M>=1 and A>=0 satisfy:

1. |C_t|<=M at EVERY fine cut t>=T.
2. Every completed dormant episode of every eventually consumed R-born
   lifetime born at b>=T has at most A integer cuts.

Then each such lifetime has age at most

    D=Q(2(M+A)+1),

and the trajectory is eventually a nonzero translating periodic trace.
No bound on the number of dormant episodes is needed.

**Proof.** Fix such a consumed lifetime x, born b and consumed d. At every
active cut its head is within infinity-distance M of the FIXED cell x.
Let u,...,v be any dormant episode within its life. It is completed because
the life begins and ends active; in particular cut u-1 is active. Its length
a=v-u+1 is at most A. At any t in this episode, unit physical head motion
gives ||p_t-p_(u-1)||_infinity<=t-u+1<=a<=A. Thus every dormant head position
is within distance M+A of x too. The entire life, however many reattachments
it contains, lies inside the ONE fixed (2(M+A)+1)-cell square centered at x.
There are d-b such cuts, so the escape clock gives d-b<=D.

There are only finitely many black lifetimes already present at cut T. Each
can be consumed once; after their last future consumption, all L updates
consume one of the bounded-age R-born lifetimes just considered. Apply the
retained bounded-consumed-lifetime theorem. Permanently unread old cells
remain on the full board and are not counted as consumed lifetimes. QED.

The bound is intentionally crude. The point is the logical removal of the
episode-count hypothesis, not a better numerical escape deadline. The older
signed M,A,J criterion remains valid, but is strictly unnecessary here.

## 3. Dormant components are literally frozen complete modules

**Lemma 2.** During one continuous dormant episode u,...,v of a surviving
lifetime x, its COMPLETE w component D is exactly unchanged at every cut
u,...,v. Its reactivation at update v is an R joining an outside active
cursor to D. If the sustained active bound M holds, then |D|<=M-1.

**Proof.** At L the read edge is incident to the active w cursor, so it lies
in the active component and cannot delete an edge of D. A new R edge is also
incident to that cursor. If its other endpoint meets D, the entire D becomes
active at the next cut, ending the dormant episode; otherwise it does not
change D or attach any new edge to it. This proves literal invariance, not
merely retention of one marker or of an abstract graph type. The exact gate
lemma in ACTIVE_EPISODES.md proves the final reactivation is R. The import
retains all |D| edges and adds at least the importing edge, so its following
active mass is at least |D|+1 and |D|<=M-1. QED.

In particular, under sustained active cap M, an inactive component of at
least M edges can never be imported in that tail. It stays forever frozen
and dynamically untouched. This does not permit arbitrary deletion of other
small archives: those are precisely the modules that may later be imported.

## 4. Exact necessary mechanism if bounded active mass does not attract

**Theorem 3.** Assume |C_t|<=M for every t>=T0, but the actual trajectory is
NOT eventually a translating periodic trace. Then for every T>=T0 and every
integer R>=M and every finite set K of cells, there are infinitely many
eventually consumed R-born lifetimes x, at DISTINCT unbounded cells outside K
and born b>=T, each having a completed dormant episode u,...,v such that:

* The head at some cut of that episode has ||p_t-x||_infinity>R.
* Its COMPLETE archive D is fixed for the entire episode, with |D|<=M-1.
* The archive is later R-imported and x is actually consumed at its next L.
* The dormant-episode length a=v-u+1 satisfies a+1>2(R-M).

Consequently late-born, ACTUALLY CONSUMED lifetimes must have arbitrarily
long SINGLE completed dormant intervals and arbitrarily distant excursions
away from a MIGRATING population of bounded-size frozen complete archives.
A fixed finite collection of old memory locations cannot supply this
necessary mechanism. Many individually bounded
reattachments do not suffice to evade Theorem1.

**Proof.** Apply the retained remote-stale-feedback theorem, Section7/
Theorem6, with age threshold Q(2R+1), finite exclusion set K and time T. It
supplies infinitely many R-born consumed lifetimes at distinct unbounded
cells outside K, born after T, each with age greater than Q(2R+1). Fix any
one of these lifetimes. Its head
cannot stay in x+[-R,R]^2 for its entire life. At any outside cut, the metric
lemma and R>=M rule out activity. Thus the outside cut belongs to a completed
dormant episode. Lemma2 gives its frozen complete archive and size bound.
The adjacent active cuts u-1 and v+1 are each within M of x. Reaching distance
greater than R and returning therefore takes more than 2(R-M) unit physical
moves; there are exactly a+1 moves between those two active cuts. QED.

This is a necessary mechanism, NOT an impossibility proof. The separately
certified20-cell family in TWENTY_CELL_SUSTAINED_CAP.md realizes arbitrarily
long completed waits in a fixed15-edge archive across different finite
seeds, while all complete w components have one uniform cap. Every seed in
that family still captures. It blocks a uniform mass-only waiting bound,
not an orbit-dependent eventual bound and not the proposed implication
"bounded active components alone => eventual translating periodicity."

## 5. The precise environmental state still missing

The active embedded component plus pose determines the next color and every
L transition exactly: the read port is incident to w; L crosses it and the
arrival-side component after deletion is the new active component. For R,
the pose determines the absent edge to insert, but the active component alone
does NOT specify the complete component at its OTHER endpoint. An isolated
endpoint, a small dormant archive, and a return to an old active vertex are
different exact cases. The first two are distinguished only by the ambient
full board; an R joining a dormant component imports ALL of it.

Under cap M there are finitely many possible shapes for each importable
component up to translation, and each is frozen while dormant. However the
number, positions, orientations and actual boundary ports of those complete
modules are not bounded by that assertion. Previously emitted modules remain
in this environment and may later be encountered. This is an exact passive-
module environment, not a finite closed dynamical state or a new local
validator. Theorem3 identifies what any counterexample to attraction with
bounded active components would have to do in this environment: repeatedly
make arbitrarily distant, eventually returning excursions to bounded frozen
modules holding late-born lifetimes that it then consumes, at distinct
unbounded spatial locations. This is not a proof of a universal compiler
obstruction; it excludes only a fixed finite-location memory substitute for
the necessary migrating mechanism.

The signed serial-chain/archive-splice laws and ordinary archive-growth law
constrain such imports within ordinary epochs, but do not yet prohibit this
unbounded inter-renewal organization. No finite-seed trajectory executing it
forever, and no theorem ruling it out, is claimed here.
