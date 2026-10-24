# Compactness at fixed initial black count

Date: 21 October 2026. Working theorem and proof. This is not a proof of the
highway conjecture, and no claim of priority is made.

## 1. The compact space, and the correct event topology

Fix the initial ant pose at the origin. Let K_N be the set of all black subsets
of Z^2 with cardinality at most N. Use the product topology on colorings. Then
K_N is compact. It is a closed subset of {0,1}^{Z^2}: a configuration with more
than N black cells has a finite set of N+1 black coordinates, and requiring
those coordinates to remain black gives an open neighborhood disjoint from
K_N. Product compactness therefore applies.

An element S of K_N with exactly N black cells is isolated in K_N. Require all
N sites of S to remain black. The cardinality limit leaves no site for a new
black cell, so this finite-coordinate neighborhood contains only S.

For a fixed finite horizon t, the first t turns depend on only finitely many
initial cells. Hence the number of forward-contained illegal ten-windows
through time t is a continuous integer-valued function C_t on K_N. The total
number C of these windows is sup_t C_t, taking values in N union {infinity}.
It is lower semicontinuous. Specifically, {S:C(S)>=k} is OPEN, since k
witnessing events occur by some finite time. It need not be closed.

Consequently compactness does not convert pointwise finiteness of C to a
uniform bound. A finite-valued lower semicontinuous function on a compact
space can be unbounded. A concrete example on K_1 is f({(n,0)})=n for n>=1,
and f=0 at every other point. Each listed singleton is isolated in K_1, so
{f>a} is open; the singletons converge to the empty field, where f=0.
This example is a topological counterexample, not an ant trajectory.

The exact missing compactness premise is local boundedness. For fixed N,
the following are equivalent:

1. C is bounded on all of K_N.
2. Every S in K_N has a finite-coordinate neighborhood on which C is bounded.

The reverse implication follows by a finite subcover and the maximum of its
finitely many bounds. The forward implication is immediate.

## 2. Singular limits of unbounded event counts

Assume a sequence S_j in K_N has C(S_j) tending to infinity, but C is finite
at each S_j. Take a convergent subsequence, with limit S. Its limit has
cardinality k<N: an N-cell limit would be isolated and the sequence would
eventually be constant. Since S is finite, after deleting finitely many terms
we may write

    S_j = S union D_j,
    |D_j| <= N-k,
    D_j intersection S = empty,

where D_j leaves every fixed finite set. There are no persistent deleted
cells: convergence requires all sites of the finite set S eventually to be
present, and all other sites that remain in a fixed finite box eventually to
be absent.

Now add the hypothesis that the orbit from S eventually has the standard
P104 path and turn trace. This hypothesis is independent of the preceding
topological facts. Let tau_j be the first time its ant reads D_j. For all
large j this time is finite. Otherwise the complete trajectory from S_j
would agree with the one from S for all future time, and C(S_j)=C(S), contrary
to the unbounded counts. We may restrict to those large j.

First-difference induction gives equality of both trajectories through the
state just before update tau_j. The two fields then differ exactly on D_j.
Every site of D_j is still unread at this time. Moreover tau_j tends to
infinity: any finite trace reads only finitely many sites and D_j leaves
every fixed finite set. Thus tau_j eventually lies on S's standard tail.

Only finitely many highway phases exist, so pass to a subsequence having
one fixed phase i. Write

    tau_j = T+i+k_j P,   P=104,   k_j -> infinity,
    p(tau_j) = p_T+p_i+k_j d,

with fixed nonzero drift d and fixed incoming heading h_i.

## 3. Exact first-divergence field at infinity

Translate each state at tau_j so its head is at the origin. Do not reverse
time or change its incoming heading. The unperturbed complete fields
converge locally to a precisely defined field H_i. It is the field obtained
from the backward-infinite standard trace ending at phase i, with virgin
white cells off that past trace.

For standard relative positions p_0,...,p_(P-1), its full past read set is

    U_i^- = {p_a-p_i+l*d : 0<=a<P, l in Z, a+l*P<i}.

The black indicator H_i(q) is the parity of the number of pairs (a,l) in
this display whose position equals q. This is a finite count for each q:
for each of the P phases, nonzero d allows at most one l.

To prove convergence, fix q. The initial finite field at time T, when
translated by -p(tau_j), eventually misses q. Each relevant past phase
occurrence has a fixed relative epoch l. For all sufficiently large k_j,
that occurrence is included in the actual finite history if and only if
a+l*P<i. There are finitely many such occurrences, so the color at q
eventually equals H_i(q). The same argument gives local convergence of
the historical read sets to U_i^-.

The translated D_j have at most N-k sites. A further compact subsequence
converges to a finite set D. The origin belongs to each translated D_j,
so 0 belongs to D. Most importantly,

    D intersection U_i^- = empty.

Indeed, a fixed q in U_i^- occurs in the actual unperturbed past for all
large j. If q were also in the limiting D, the corresponding added initial
black site would have been read before tau_j, contrary to the definition
of the first divergence.

Thus the limiting perturbed field and pose are exactly

    (H_i union D, origin, h_i),
    0 in D,  |D|<=N-k,  D intersection U_i^-=empty.

The union is disjoint since every black site of H_i belongs to U_i^-.
These are virgin black additions, not arbitrary flips of an old highway.
The limiting background has an infinite wake behind the ant. It is not a
finite-support state, so an induction theorem restricted to fewer initial
black cells cannot be applied to it.

Because 0 is not in U_i^-, phase i is a first physical visit in the
infinite standard trace. In particular its unperturbed turn is R and the
perturbed turn is L. The retained standard word has 22 such phases, one
per visited drift class. The companion script reconstructs them exactly.

## 4. Sector restriction

With headings N,E,S,W=0,1,2,3, the arrival sector is

    sigma = (-1)^(h-x-y).

Each update preserves sigma. Adding or removing black sites at fixed pose
also preserves it. The recentered perturbed and unperturbed fields have
identical pose and therefore identical sector. Fixing phase also fixes the
sector after translation. No limit operation changes this fact.

A time reversal that changes the heading by an odd number of quarter-turns
has the opposite sector. A reversed ant that consumes a backward-infinite
highway forever therefore cannot be substituted into this first-divergence
limit without also proving a mechanism that changes the allowed sector.

## 5. What has not followed

The counts after tau_j remain unbounded, since the counts before tau_j
are bounded by the total count of the captured orbit from S. But finite
speed only transfers each FIXED finite time interval to the limit. It
does not imply that the limit field H_i union D has infinitely many J10
events. Events can move to later and later times, including a new encounter
with a marker that disappears in the centered limit.

Thus a proof would need a uniform, full-history scattering bound for these
matched-sector virgin-marker inputs, plus a way to account for the remote
markers and all previously written trails after scattering. Pointwise
recovery of each limiting infinite-wake state is not by itself that uniform
statement. The compactness argument identifies a necessary boundary class;
it does not prove global attraction or a fixed-cardinality event budget.

## 6. Source boundary

The compactness and first-difference arguments above are elementary and
written here in full. The supplied prior work already used first-difference
coupling and finite-support compactness for bounded populations. The J10
definition and its equivalence to standard capture come from Hao Ke's
factor-language work; the topological result only needs that J10 is a
finite-window event. No unverified attraction theorem is needed to prove
Sections 1-4, conditional on the explicitly assumed captured limit S.
