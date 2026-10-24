# An exact mass-sensitive residual-defect skeleton budget

23 October 2026. Conditional structural theorem, not a capture proof.
The exact token forest, its finite-root bound, and its explicit comb/dormancy
safeguards are inherited from ../../causal_reduction/forest_theorem.md.
The present budget distinguishes two necessary recycling mechanisms, retains
finite side branches, and exempts harmless infinite standard renewal.
It does not prove that either mechanism stops on arbitrary ant trajectories.

## 1. Residual marks and active initial identities

Fix a finite ant prefix. Mark a cursor node if any physical read in that node
ends a residual UNION6 event: an adjacent pair of bad standard ten-windows
whose full eleven-label is outside the signed six-label set. Use only full
windows inside the prefix, or retain the true inverse history consistently.
A cursor node contains at most five physical reads, hence at most five marks.
Let R be the number of residual EVENTS and M the number of marked NODES.
Then

    M <= R <= 5M.                                      (1)

The full token forest has one virtual root per initial black identity and
one root for the initial cursor node. Keep exactly the roots that have a
marked descendant in this prefix. Let r be their count. It is the number
of distinct ancestral initial-black identities actually involved, plus the
possible initial-cursor component, so r<=|B_0|+1.

Let A be the finite ancestral closure of all marked nodes, including these
roots. Every ancestor is retained, however long a token waited. Give a node
v its number d(v) of children in A. Terminal buds without a known mark below
them are not deleted from the physical forest: they are merely outside this
finite accounting subforest and can enter it later if eventually consumed.

## 2. Two irreversible historical recycling counts

Define

    S = sum over v in A of max(d(v)-1,0),
    I = number of marked v in A with d(v)>=1.           (2)

S counts marked-branch splitting, with multiplicity d-1. An unmarked spine
that repeatedly emits marked finite bushes contributes to S and is NOT
lost. I counts a marked generation that has a later marked descendant.
A single repeatedly marked ancestral chain contributes to I even if it never
splits. Neither count is a count of initial bits or a conserved resource.

Both counts are measurable from the finite past, exact token ownership and
its event labels. As the physical prefix grows, r,S,I are nondecreasing.
A retained child direction never ceases to have a past marked descendant;
a marked internal vertex never ceases to be marked and internal. A dormant
bud that later becomes relevant adds its complete ancestor path at that time.
Thus C=S+I is an irreversible HISTORICAL complexity, not a decreasing rank.

## 3. Exact identity and conditional finiteness theorem

Every leaf of A is marked. Conversely every marked node is either a leaf or
one of the I marked internal vertices. For a finite forest with r components,
the number L of leaves is

    L=r+sum_v max(d(v)-1,0)=r+S.

This follows by summing d(v)-1 over all vertices, or by induction on edges.
Consequently

    M=r+S+I,
    r+S+I <= R <= 5(r+S+I).                            (3)

The empty case has r=S=I=M=R=0. Virtual initial-black roots are unmarked and
have at most one child, so they create no extra branch or mark terms.

In particular, for any finite-seed trajectory and any uniform bound C_* on
S+I over ALL finite prefixes,

    total residual events <= 5(|B_0|+1+C_*),

so the signed UNION6 theorem gives eventual standard104 capture. This is a
sufficient, measurable conditional theorem. The missing universal premise
is bounded S+I, not the already true fact that the number of roots is finite.
Indeed, for a finite-root bounded-degree forest, finitely many residual
marks is EQUIVALENT to bounded S+I. Equation (3) is an exact structural
reduction and must not be sold as progress establishing that bound.

A finite-prefix density consequence is

    R(T)>=delta*T  =>  S(T)+I(T)>=delta*T/5-(|B_0|+1).

Thus positive residual density requires linear accumulation of historical
marked recycling, even if only one ancestral initial identity is involved.
The standard forest can renew forever with no new residual marks, in which
case these counts remain constant. Ordinary branching alone is not charged.

## 4. A second conditional form: chain depth and branch depth

Within each active root component let b_i be the largest number of marked
nodes on one root-to-leaf path in A, and c_i the largest number of vertices
with at least two A-children on such a path. Outdegree is at most four,
including the initial cursor node. A component has at most 4^(c_i) leaves.
Each marked node lies on a root-to-leaf path, so

    R <= 5 sum_i b_i*4^(c_i).                          (4)

Uniform bounds on both depths imply finiteness. Bounds on just one do not:
an arbitrarily long marked unary chain keeps c=0; a comb with unmarked
spine and marked leaves keeps b=1. The latter is why finite bushes cannot
be ignored. Equation (4) is generally much weaker than (3), but its two
hypotheses are sometimes geometrically separable.

Both depths are nondecreasing with the observed prefix. At residual density
delta, the maximum depths b,c satisfy

    b*4^c >= delta*T/[5(|B_0|+1)].

No general spatial theorem bounding S,I,b or c has been proved here.

## 5. Why simple spatial ordering is still insufficient

The companion spiral_monotone_marked_comb.md extracts an ACTUAL finite-ant
component with one initial root, n marked spine nodes, and n-1 marked side
leaves. Its entire causal spine moves by (1,-1) at each step, side edges have
zero displacement, and side depth is one. Nevertheless

    S=I=n-1, M=2n-1, R=4n-2.

Thus monotone causal ancestry, no causal recrossing, and bounded side depth
can coexist with unbounded recycling counts. Other seed roots assist the
full trajectory, and total seed mass grows; there is no fixed-mass
unboundedness claim. The full chronological cursor makes an inward spiral,
so this is NOT a counterexample to a stronger hypothesis bounding the LIVE
cursor's cut crossings.

The existing twenty-cell root-reactivation family separately prevents
replacing S or I by an irreversible ordering of which input root is active:
a root can disappear for an arbitrarily long interval and regain both
infinite standard spines. Lifetime and root dormancy must remain explicit.

## Trust boundary

This is elementary finite-forest accounting applied to an already exact
physical genealogy. It is neither a new global invariant nor a universal
residual-finiteness theorem. The event-filtered subtree is defined using past
marks; it is not an independently predicted finite resource. Its potential
use is to state precisely what a genuinely new ordering or geometric lemma
must bound, without dropping marked bushes or conflating finite roots with
finite descendants. Independent review requested.
