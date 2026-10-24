# Complete-state reachability modulo rigid motion

Research date: 22 October 2026. Status: analytic corollary of two previously established dependencies; finite implementation controls pass. The midpoint-to-finite-target reduction was independently reviewed by the audit analysis. No novelty or global highway claim is made.

## 1. Model and dependencies

A complete finite state is X=(B,p,h), with h=N,E,S,W numbered 0,1,2,3. Let F be the literal white-right/black-left, flip-then-move update, d_h the corresponding unit vector, and m(X)=p-d_h/2. Let tau_z denote translation by z and R_r a clockwise quarter-turn through r steps, rotating both the field and heading.

The two imported results are:

1. For any two actual states X_s,X_t of one orbit,

   |B_s symmetric_difference B_t| >= 2 ||m(X_t)-m(X_s)||_infinity.

   Source: continuation_2026-10-22/ant_continuation2/chronology/axial_separator_proof.md, Section 4. This is an all-time endpoint theorem, not a bound on the maximum mass between the endpoints.

2. There is a computable integer clock Theta on complete finite states with Theta(FX)>=Theta(X)+1. Therefore specified complete-state forward reachability and signed two-sided orbit equivalence are decidable.

   Source: sources/kehao95-core/clock_escape/PROOF.md, Sections 1 and 4; the detailed manuscript proves the computable orbit section as well.

## 2. Finite-target theorem

Given complete finite X=(B,p,h) and Y=(C,q,g), it is decidable whether

   F^t X = tau_z R_r Y

for some t>=0, z in Z^2 and r in {0,1,2,3}. It is also decidable with t in Z.

Proof. Fix r and replace Y by R_r Y. Put M=|B|+|C|. Every possible equality satisfies

   2 ||q+z-d_g/2-(p-d_h/2)||_infinity <= M.

For coordinate j, write a_j=2(q_j-p_j)-(d_g)_j+(d_h)_j. Then

   -M <= 2 z_j+a_j <= M.

Thus z_j lies in an explicitly computable interval of length M, containing at most M+1 integers. There are at most (M+1)^2 shifts for a rotation, and at most 4(M+1)^2 fully specified targets overall. Test each using the exact complete-state clock algorithm. All tests terminate; forward tests restrict the returned signed offset to t>=0. QED.

The target's given coordinates can be enormous, and the resulting clock simulation bound can be enormous. This is a decidability theorem, not a practical or polynomial-time bound. A supplied finite family of target templates is handled by a finite union.

## 3. Consequences and strict scope

A halting reduction cannot use a finite effectively supplied list of FULLY SPECIFIED finite accepting states, even if each accepting state may appear at an arbitrary translation or quarter-turn rotation. Such a target language has the decision procedure above. The number or size of templates may depend computably on the machine input.

This does not exclude local accepting patterns, arbitrary accepting memory contents, an unbounded family of garbage fields, or a terminal condition specified by an unbounded numerical parameter. It does not decide standard-highway capture, because a highway state includes arbitrary complete old debris and its terminal predicate is not a finite union of complete rigid templates.

The equivalence relation 'same complete orbit up to time shift, translation and quarter-turn rotation' is decidable. We use this precise equivalence, not mere turn-stream equality, below.

## 4. No exact finite-support rigid cycles

There is no t>0 and rigid motion tau_z R_r with F^t X=tau_z R_r X for a finite state X.

If r=0, determinism and translation covariance give F^(nt)X=tau_(nz)X for every n. The midpoint inequality then gives 2n||z||_infinity<=2|B|, hence z=0. Exact recurrence contradicts the strictly increasing clock.

If r is nonzero, take k in {2,4} with R_r^k=identity. The sum z+R_r z+...+R_r^(k-1)z vanishes for a nontrivial planar quarter-turn rotation. Iterating the hypothesized equality gives F^(kt)X=X, again contradicting the clock.

This is compatible with a standard highway: the turn/pose trace translates, but the complete black field grows a wake and is not a finite translating template.

## 5. Finite controls

check_rigid_reachability.py is a separately written literal implementation. It checks the inverse and exact clock gain on 7,200 updates, the allowed-shift inequality on 7,200 actual endpoint examples, signed exact-state offsets on 2,160 examples, and five rigid-offset examples. Its saved output is rigid_reachability_controls.json. Those controls catch implementation/convention errors; they do not replace the analytic all-time argument.
