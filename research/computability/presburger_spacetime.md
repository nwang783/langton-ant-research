# Exact periodicity equals Presburger-definable space-time

22 October 2026. Status: analytic metatheorem, independently audited. This concerns a single complete finite initial ant state, and does not establish that all such states become periodic.

## Theorem

For a finite-support initial state X, the following are equivalent:

1. Its turn stream is eventually periodic (with any period, not necessarily standard104).
2. Its entire forward space-time history has Presburger-definable head and color relations:
   P(t,x,y,h) iff the head has pose (x,y,h) at time t;
   C(t,x,y) iff cell (x,y) is black at time t.

Moreover, a supplied pair of Presburger formulas can be checked effectively and exactly as a certificate for the entire forward orbit of X. Given an exact periodic-tail certificate, formulas can be effectively constructed.

Presburger arithmetic here is the first-order theory of integers with addition, order and constants, not multiplication of variables. Multiplication by a fixed integer is allowed.

## Forward construction

Suppose a periodic suffix starts at T and has a heading-restoring period p with nonzero displacement d. Such a period can be chosen whenever the ant turn stream is eventually periodic: a nonrestoring net rotation would bound the repeated geometric path, and zero displacement would also bound it, contradicting finite-domain escape.

Let q_j,h_j be the head pose immediately before phase j of that period, for 0<=j<p. Let B_T be the complete finite black set at T.

For t>=T the head formula is the finite disjunction, over j,

   exists k>=0: t=T+pk+j and (x,y)=q_j+kd and h=h_j.

For each phase j define the Presburger relation

   E_j(t,x,y) iff exists k>=0:
        (x,y)=q_j+kd and T+pk+j<t.

Since d is nonzero, any fixed cell occurs at most once in each phase ray. Therefore its bit at time t is exactly

   C(t,x,y) = 1_{B_T}(x,y) XOR E_0(t,x,y) XOR ... XOR E_{p-1}(t,x,y).

This is a finite Boolean formula in Presburger relations. The strict inequality correctly counts writes completed before state time t. A finite disjunction supplies the complete explicit states at times 0,...,T-1. This constructs the whole space-time, including persistent old debris and the infinite wake; no translating equality of whole boards is assumed.

## Reverse implication

If P is Presburger-definable, then each unary time set

   D_h={t>=0: exists x,y P(t,x,y,h)}

is Presburger-definable. A unary Presburger set is ultimately periodic. Taking a common period and threshold for the four D_h shows that the heading sequence is eventually periodic. The turn at t is determined by the pair of headings at t and t+1, so the turn stream is eventually periodic as well. The color formula is not needed for this direction.

The arithmetic fact used here follows from the classical characterization of Presburger sets as semilinear sets. Primary reference: Ginsburg and Spanier, *Semigroups, Presburger formulas, and languages* (1966), https://www.csa.iisc.ac.in/~deepakd/atc-common/ginsburg-spanier-PJM-1966.pdf . In one dimension a finitely generated additive monoid is eventually periodic in its gcd class, and finite unions preserve ultimate periodicity.

## Exact verification of a proposed formula certificate

Given formulas P and C and finite X, form Presburger sentences asserting:

1. At every integer t>=0, P specifies exactly one pose with h in {0,1,2,3}.
2. At time zero P and C agree with X, with C false at every cell not in the finite input black set.
3. For all t>=0 and all cells q, C(t+1,q) equals C(t,q) XOR the assertion that q is the current head position.
4. For the unique current pose, C at that cell determines the right/left turn and the unit move, and P at t+1 specifies exactly that resulting pose.

All four are first-order Presburger sentences after substitution of P,C. Decide them using Presburger decidability. If they hold, ordinary induction on t and determinism show that they describe the actual orbit exactly. No additional finiteness-of-each-time-field axiom is required: finite initial support and one flip per step already imply it by induction.

Conversely the constructed formulas above pass these conditions. Enumerating formulas and running this verifier is thus another semidecision procedure for eventual periodicity, equivalent in scope to enumerating word-tail certificates. It is not a recognizer for genuine nonperiodicity.

## Consequences and limits

- On every certified eventually periodic input, arbitrary first-order questions in addition/order over the head/color space-time are decidable by substitution and Presburger arithmetic. This includes fixed-cell visitation, finite local patterns, and recurrence expressed with first-order quantifiers over times and coordinates.
- If the universal standard104 conjecture is true, there is a total effective algorithm that converts every finite seed to its complete Presburger space-time description: simulate until an exact standard-tail certificate is found, then apply the construction.
- A genuine nonperiodic counterexample cannot have a finite Presburger description of its time-indexed head history. A spatial drawing, an unbounded loop schema with nonlinear time indexing, or a more expressive induction certificate is not excluded.
- A semilinear set of cells visited at some time is not the same as a semilinear time-indexed head graph. The former alone does not imply periodicity.
- These statements do not make every conceivable question about an ant input decidable. The query language must itself be specified; the claim here is precisely first-order Presburger queries over the certified space-time relations.
