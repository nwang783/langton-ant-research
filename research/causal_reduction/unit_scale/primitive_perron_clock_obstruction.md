# Positive clocks forbid irreducible unit-scale refinement

23 October 2026, 05:04 UTC. Independently signed analytic proof at 05:11 UTC.
The noncancellation argument is explicit below. No global ant theorem follows.

## 1. A precise typed statement

Let S be a finite typed alphabet. Each state s specifies an incoming heading
h_s and turn c_s in{+1,-1}, hence one unit displacement v_s and final heading
h'_s. Let phi be nonerasing; its image of s is a physical quarter-turn word
with total displacement v_s, initial heading h_s and final heading h'_s.
Thus positions refine with spatial matrix I and every iterated image is
geometrically well-defined. Decorated states are allowed.

Let M(1,1) be the row-incidence matrix. Assume it is irreducible and its
Perron eigenvalue exceeds one. Then the iterated images phi^r(s) cannot all
be internally ant-legal, even on arbitrary initial colorings. In particular
no growing rooted limit of such an irreducible presentation is an ant path.

A uniform length K>1 version follows WITHOUT global irreducibility: restrict
to a reachable terminal strongly connected component. It is closed, all row
sums are K, and its refined images are factors of the proposed actual path.

The proof uses the independently signed finite-valued rational-series theorem
in `computability/finite_power_exact_validator/bounded_particle_structure.md`
and its cited Bell--Chen/Cobham--Semenov ingredient. It does not assume bounded
black mass or bounded occupation support size.

## 2. Weighted incidence and finite-valued checker occupation

For positive characters X,Y write w(q)=X^(q_x)Y^(q_y). Define the Laurent
matrix

    M_s,t(X,Y)=sum_{children j of image s of type t} w(p_sj),

where p_sj is the read offset of child j. Since the spatial scale is I,
M(X,Y)^r counts the weighted states in phi^r(s).

Set a(h)=+1 for vertical headings and -1 for horizontal headings, and

    d_s=a(h_s)c_s,       C_s(r;X,Y)=(M(X,Y)^r d)_s.

At a fixed read offset q in phi^r(s), every incoming heading has axis sign
 a(h_s)(-1)^(q_x+q_y). Therefore its coefficient in C_s(r) is that fixed sign
times the signed R-minus-L read count. If the word is internally ant-legal,
this coefficient lies in{-1,0,1}.

All offsets in a depth-r image have norm O(r), being sums of r members of one
finite offset set. After shifting each spatial coordinate by Cr, the joint
series sum_r t^r C_s(r;X,Y) is rational with polynomial denominator of constant
term1: use det(I-t X^C Y^C M(X,Y)). Its integer coefficients take only the
three values above. The signed semilinearity theorem therefore applies.

A disjoint simple-linear-set representation of the nonzero coefficient sets
gives a rational expression whose denominator is a finite product

    P_s(t;X,Y)=product_j (1-t^(a_j) X^(b_j) Y^(c_j)),       (1)

where a_j are POSITIVE integers and b_j,c_j are integers. A nonzero period
with zero time coordinate would give an infinite spatial fiber, impossible;
zero periods can be discarded. Undoing the Cr shift only changes b_j,c_j.
There may be polynomial numerators and repeated factors. No uniform fiber
cardinality bound is required. In particular

    P_s(t;1,1) has no positive zero strictly between0 and1. (2)

## 3. The exact positive clock functional

Choose X>1,Y>1 in the open domain

    kappa=1-2/(X+1)-2/(Y+1)>0.

Use the signed clock from wake_synthesis/PROOF.md Section9, with

    gamma_N=2/(Y+1),       gamma_E=2/(X+1),
    gamma_S=-2Y/(Y+1),     gamma_W=-2X/(X+1).

For one coarse state define

    H_s=gamma_(h'_s) w(v_s)-gamma_(h_s),
    g_s=H_s-d_s.

The literal eight-case clock identity says g_s=kappa in six physical states,
and g_s=kappa+4 in S/black and W/white. Hence g is STRICTLY positive on this
whole open domain. This assertion is independent of a seed or legality.

Telescoping the head correction over the geometric word phi^r(s) gives the
EXACT identity

    (M(X,Y)^r g)_s = H_s-C_s(r;X,Y).                       (3)

The left side is a positive weighted sum of every literal read increment.
The boundary term H_s is independent of r because the complete initial/final
poses and displacement are the coarse ones. Thus

    [(I-tM)^(-1)g]_s = H_s/(1-t)-sum_r t^r C_s(r).         (4)

This is the point at which signed Perron cancellation is excluded; positivity
of raw incidence alone would not justify it.

## 4. The Perron pole cannot disappear

The zero/nonzero pattern of M(X,Y) is fixed and irreducible for every positive
X,Y, so its Perron eigenvalue lambda(X,Y) is simple, positive and real-analytic
on the connected positive quadrant.

Every image's first child lies at offset0. Its first-child map has a directed
cycle, whose selected weighted edges all have weight1. The full irreducible
matrix dominates this cycle matrix and is not equal to it (its Perron value
at(1,1) exceeds one). Strict Perron monotonicity therefore gives

    lambda(X,Y)>1 for ALL positive X,Y.                   (5)

Let r,l be positive right/left Perron vectors. On the clock domain, g>0, so
[(I-tM)^(-1)g]_s has a genuine simple pole at t=1/lambda, with nonzero
coefficient r_s(l^T g)/(l^T r). The boundary H_s/(1-t) is analytic there by(5).
Equation(4) proves that the signed checker-occupation series has that same
nonzero pole. Thus its semilinear denominator must satisfy

    P_s(1/lambda(X,Y);X,Y)=0                               (6)

throughout the nonempty open clock domain.

The left side of(6) is real-analytic on the connected positive quadrant.
It therefore vanishes identically. Evaluating at X=Y=1 contradicts(2), since
lambda(1,1)>1. This proves the typed theorem.

## 5. Reachable terminal components in the uniform case

For a uniform substitution of length K>1, choose any terminal SCC reachable
from the root. It is closed under all child edges, and its incidence matrix
has row sums K, hence irreducible Perron K. All its states occur in some root
power, so all their further refined images are actual factors whenever the
rooted presentation is legal. The restricted images retain unit geometry and
poses. The preceding argument applies on this component.

For a genuine root cycle, first replace the presentation by the power defining
the actual rooted fixed point. Spatial I and uniformity persist; choose a
terminal SCC of that power. Intermediate phase words are not assumed legal.

## 6. A harmless periodic-boundary extension

The proof is unchanged if the incoming/final heading pair of phi^r(s) varies
eventually periodically with r, while its net displacement remains v_s and
the typed words and weighted matrix iteration remain exact. In that case the
boundary term H_s(r) has a rational depth series with poles only at roots of
unity. It is still analytic at t=1/lambda<1, so (4)--(6) remain valid with that
boundary series in place of H_s/(1-t). Checker-occupation coefficients remain
bounded: at each fixed r the initial axis sign is fixed and the same per-cell
alternation argument applies.

This extension requires an ACTUAL finite boundary-phase description, not an
assumption that arbitrary heading mismatches can be ignored. The adjacent-pair
application in the companion note supplies one explicitly.

## Limits

General reducible NONUNIFORM systems are not excluded by this argument: they
may have only singleton identity terminal components, with branching in a
nonclosed upstream component. No claim is made that a globally fastest mode
has the same component at every positive character. Arbitrary changing phase
schedules need not have rational occupation arrays and are also outside scope.
