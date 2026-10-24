# Cursor counterflow is stream-height excess; the K=1 pipeline is rigid

23 October 2026, 13:18 UTC. Clarification and conditional consequence of
the independently signed face_birth_curve_cursor_counterflow.md. The
stream identification has been analytically reconstructed by the auditor;
the complete frozen note is submitted for final review. No global K=1
assertion, detour exclusion or front exclusion is made.

## 1. Exact stream identification, with oriented sign fixed

Use the positively oriented first-L face-birth curve Gamma and its LEFT
and RIGHT sides, with actual full drift d. Write c_left,c_right for the
original exterior stream constants on these two sides. Retain the signed
convention f=h(C_right)-h(L_left). Since the full physical current has
positive homology1 in the d direction,

    c_right-c_left=1.

This explicitly fixes the sign; c_right is not an unlabeled c_plus.
The curve intersects only global-max C faces and selected primal vertices.
Thus any original face whose interior Gamma cuts has original height M.
Define a new face stream

    h_R=h-M on RIGHT faces,
    h_R=0 on LEFT faces,
    h_R=0 on the C faces cut by Gamma.

The definitions agree at a cut C face because h=M there. Every physical
edge's interior lies strictly on one side. On RIGHT edges the differences
of h_R equal those of original h; on LEFT edges they vanish. Thus h_R
is exactly the stream of the physical RIGHT current proved in the cursor
note, not a flow assigned to diagonal face-switch edges.

Its exterior left/right constants are0 and c_right-M. The same oriented
stream-jump convention therefore gives its homology

    c_right-M=-K,
    K=M-c_right.

The LEFT current has stream h-h_R, exterior constants c_left,M, and
homology M-c_left=K+1. This agrees with the independent excursion endpoint
calculation. The positive integer K measures the global stream-ridge
excess on the right, not a newly invented defect charge.

## 2. If K=1, each right excursion retreats exactly one contact

Use the signed endpoint map E(i) for the RIGHT excursion from R0(v_i)
to R2(v_(E(i))). The cursor theorem gives E(i)<i and

    sum_(i=0)^(ell-1) (i-E(i))=ell*K.

When K=1, every positive integer i-E(i) must be exactly1. Hence

    E(i)=i-1 for EVERY lifted contact i.

This is not an assumed noncrossing matching or a primitive-winding
shortcut. It follows from the exact integral sum and the individual
strict backward order.

## 3. The temporally next R0 and left excursion are forced too

Let H(i) index the temporally next selected R0 after R0(v_i), and let
G(j) index the end R0 of the LEFT excursion starting at R2(v_j).
Chronological crossing alternation gives H=G composed with E. The cursor
theorem gives G(j)>j. In the K=1 case,

    H(i)=G(i-1)>i-1.

H(i)=i is impossible: a fixed physical contact has only one R0 read.
Therefore H(i)>=i+1. The temporally next-R0 permutation traverses all ell
distinct R0 phases in one full period P and then reaches the translate
by+d. Its total lifted contact-index advance over those ell steps is
ell. Consequently all ell increments H(i)-i, each at least1, equal1:

    H(i)=i+1,   G(j)=j+2.

Thus RIGHT excursions retreat one contact, LEFT excursions advance two.

The selected R0/L1/R2 events have the rigid chronological restriction

    ... R0_i, R2_(i-1), L1_i, R0_(i+1), R2_i, L1_(i+1), ...

with arbitrary additional visits elsewhere and optional L3 visits still
retained. L1_i lies on the LEFT and between its own R0_i and R2_i. The
only LEFT interval in that span is from R2_(i-1) to R0_(i+1), forcing the
displayed placement. This does not turn any of these actual excursions
into a straight geometric path or remove its possible detours.

## 4. A concrete analytic subcase, not closure

Index the max faces along Gamma so contact v_i switches first L from
parent F_i to child F_(i+1). Then RIGHT excursion

    R0(v_i) -> R2(v_(i-1))

starts and ends at the TWO selected contacts of the SAME max face F_i.
The intervening LEFT excursion runs from R2(v_(i-1)) through the actual
L1(v_i) switch F_i->F_(i+1), then ends at R0(v_(i+1)). This is a canonical
one-face backward/two-contact forward pipeline architecture.

Classifying or excluding its allowed literal detours would be a concrete
next first-principles task. The result does not prove every cap-four
front has K=1, does not classify K>=2, and does not bound old-wake or
optional-L3 revisits. No prepared-profile solver or bounded period/drift
search was run for this architecture.
