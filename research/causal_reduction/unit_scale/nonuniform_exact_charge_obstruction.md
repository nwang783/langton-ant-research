# Fixed exact-charge physical-state controllers cannot grow legally

23 October 2026, 05:14 UTC. Independently signed analytic extension at 05:17 UTC.
Its common-Gaussian-unit two-turn corollary is independently signed too.

## 1. Statement and genuine root phase

For each of the eight physical incoming-heading/turn states s, choose a finite
nonempty turn image with exactly the same unit displacement, incoming heading,
final heading, and signed turn charge as s. Image lengths may be arbitrary
and unequal; identity images are allowed. The same fixed eight-state controller
is used at every depth.

No growing rooted power-limit of this controller can be a Langton-ant path,
even on an arbitrary initial coloring.

First pass to the power defining the actual rooted fixed point, if needed.
All four local preservation properties survive composition. We do not assume
that an intermediate root phase is legal. In the actual fixed presentation,
a growing root eventually reaches a nonidentity image. By the independently
signed local structure in `checker_axis_transport_structure.md`, every
internally legal nonidentity image contains ALL eight physical states, and
its parent state occurs at least twice. Hence all eight states occur in the
actual path, all their refined images are actual legal factors, and every
nonidentity image satisfies this structure.

The assertion is only about eight UNDECORATED physical states, exact local
charge preservation, and spatial matrix I. It does not silently cover hidden
context states, arbitrary phase schedules, or arbitrary nonconserving images.

## 2. Active matrix and identity absorbers

Let T be the nonempty set of active states, whose images are nonidentity.
The other states are identity absorbers. With active states first, the exact
weighted incidence matrix has block form

    M(X,Y) = [[B(X,Y), C(X,Y)], [0, I]].

Every entry of B is a nonzero Laurent polynomial with nonnegative integer
coefficients, because every active image contains every physical state.
Moreover every diagonal entry B_ss contains at least two monomial occurrences.
Thus B is strictly positive at every positive character. Its Perron eigenvalue
lambda(X,Y) is positive, simple and real-analytic on the whole positive
quadrant, and lambda(1,1)>1.

Unlike the uniform closed-SCC proof, we do NOT assert lambda>1 everywhere.
Only a nonempty open clock domain with lambda>1 is required.

## 3. Such a clock domain always exists

Choose any active state s. If every self-occurrence in its image has spatial
offset zero, then B_ss>=2 at every positive character.
Otherwise select one nonzero self-offset q=(q_x,q_y). Choose a real vector
z=(z_x,z_y) with both coordinates nonzero and z dot q>0. For

    X=exp(t z_x), Y=exp(t z_y), t tending to +infinity,

that monomial tends to infinity, so B_ss>1 and lambda>=B_ss>1 for large t.
Rotate the positive clock by one of the four physical quarter turns so that
both transformed characters X',Y' exceed one. Both tend to infinity, hence
its strict positivity condition

    1-2/(X'+1)-2/(Y'+1)>0

holds for all sufficiently large t. Strict inequalities persist on a nonempty
open neighborhood U of one such character. Thus on U the rotated literal
clock increment g is strictly positive in every physical state and lambda>1.

A quarter rotation changes the checker-axis sign vector d by a global sign
and permutes the spatial variables. Either sign still has coefficients in
{-1,0,1} on every legal block. The finite-valued rational-series denominator
argument therefore applies unchanged to this chosen orientation.

## 4. Absorbers cannot cancel the active Perron pole

Use the rotated clock head vector H and checker vector d, and put g=H-d>0
on U. Exact unit-pose preservation still gives

    (M^r g)_s = H_s-(M^r d)_s.

For the identity states, the resolvent is g_I/(1-t). The active part is exactly

    [(I-tM)^(-1)g]_T
      = (I-tB)^(-1) [g_T + t C g_I/(1-t)].

At t_0=1/lambda in (0,1), the bracketed vector is strictly positive. The
Perron residue in every active coordinate is therefore nonzero and positive.
The head boundary H_s/(1-t) is analytic there. Consequently the signed checker
occupation series of every active state has a genuine pole at t_0.

All refined blocks are actual legal factors. Their integer occupation
coefficients are in{-1,0,1}, and their offsets are O(r). The signed rational
semilinearity theorem supplies a fixed denominator

    P_s(t;X,Y)=product_j (1-t^(a_j) X^(b_j) Y^(c_j)), a_j>0.

Hence P_s(1/lambda(X,Y);X,Y)=0 on U. This expression is real-analytic on the
connected positive quadrant, so it also vanishes at(1,1). But
lambda(1,1)>1 and P_s(t;1,1) has no zero in(0,1), a contradiction.

## Consequence and limit

This replaces the earlier finite-length fixed-controller exclusions by
an all-length, unequal-length theorem for exact-charge eight-state unit
controllers. The explicit legal21/29 transports remain valid local controls;
what fails is using any fixed collection of such transports recursively to
produce a growing ant word.

The proof relies on the local all-eight-states and repeated-parent incidence
lemma. These fail for arbitrary decorated states, and are not assumed there.
Changing the controller at each level destroys the single rational transfer
used here. No arbitrary-directive or general finite-support conclusion follows.

## Common-Gaussian-unit two-turn corollary

The independently signed `nonuniform_charge_reduction.md` proves exact image
charges +1 and -1 for every growing rooted power-limit of a fixed two-turn
morphism whose images preserve the coarse final heading and share one
Gaussian-unit spatial multiplier a. Image lengths need not agree. That proof
already handles reducible images and genuine first-letter cycles, on arbitrary
initial colorings.

Take a substitution power divisible by both the root-cycle length and the
order of a. Its spatial multiplier is I; its images preserve unit poses and
exact charges. Lift its two turn images to the eight physical incoming-heading
states by rotation. This is precisely a fixed controller covered above.
Therefore NO growing rooted limit in that entire heading-preserving,
common-Gaussian-unit two-turn class is ant-realizable, on any coloring.

This corollary retains all its common-unit and heading hypotheses. It says
nothing about changing controllers, additional context labels, or unequal
spatial multipliers for the two images.
