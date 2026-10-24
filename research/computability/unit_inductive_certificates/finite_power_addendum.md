# Extension to any eventually periodic sequence of integer matrix powers

2026-10-23 03:16 UTC. Analytic addendum independently signed as audit II.
The unit-scale proof in bridge.md remains frozen. No accepted model is known.

## 1. Geometric hypothesis

Replace the Gaussian unit by an integer matrix A. Supply integers mu>=0 and
q>=1 with the exactly checked identity

    A^(mu+q)=A^mu.

Then A^(j+q)=A^j for every j>=mu, so the whole sequence of powers is finite.
This includes nonorthogonal finite-order matrices, for example
A=[[1,2],[0,-1]], q=2, mu=0, and possibly singular eventually periodic matrices.
There is no need to classify all such matrices or decide this property from
an unrestricted input: mu,q are supplied and the identity is a finite check.

The typed images retain their parent's incoming and final outgoing headings,
and their net displacement is A*d_s. Endpoint and internal read-position
scaling under refinement is therefore exactly A^r. No angle preservation or
invertibility of A is used in the block-composition proof.

## 2. Exact weighted automaton for decreasing exponents

For mu=0 use the cyclic phase graph from bridge.md, replacing a^l by A^l.
A length-r walk starts at phase r-1 modulo q. Its weights are precisely those
of the decreasing exponent sequence A^(r-1),...,A^0.

For mu>0 and r>mu, use a cyclic high part with phases c in{0,...,q-1}, whose
weight matrix is A^(mu+c). For every substitution occurrence, a high edge
from c goes to c-1 modulo q; at c=0 there is also an exit edge to the low
phase mu-1. The starting high phase is (r-1-mu) modulo q.
The low phases mu-1,...,0 are a forced finite chain, with weight matrices
A^(mu-1),...,A^0. A low-zero edge enters a terminal state. Every edge also
updates the physical letter state to the selected child letter, and has
weight equal to its phase matrix times that occurrence's proper prefix
position. Terminal states have no outgoing edges.

Accept ONLY walks of exactly r edges ending at a terminal state. Every such
walk has exactly mu low edges. Hence its high part has r-mu edges. Its start
phase and the requirement to exit from high phase zero force precisely the
correct decreasing matrix sequence, regardless of how often the cyclic high
part is traversed. Conversely every depth-r read choice gives such a walk.
For 1<=r<=mu use the corresponding finite low chain starting at r-1;
for r=0 the read set is {origin}.

The Euler edge-count formula now fixes the allowed terminal endpoint rather
than disjoining unrestricted endpoints. It is otherwise unchanged. Start
phase congruences, finitely many small-r cases, and endpoint restrictions are
Presburger. Thus the exact relation R_s(r,x,y) remains effectively Presburger.

## 3. Induction, finite seed, and aperiodicity

Every shift A^r*p_j has only finitely many values and is eventually periodic
in r. Consequently all I/O frame-agreement and XOR endpoint checks from
bridge.md remain Presburger. The same accumulated black/white demand test
extracts one genuine finite initial seed.

A growing accepted root has infinitely many refining checkpoints but only
finitely many endpoint poses, since the powers of A have finite range and
headings are preserved. The same finite-domain-escape argument therefore
excludes every eventually periodic movement tail.

This is a sufficient supplied-template validator for a broader geometric
class, not a counterexample and not a general finite-seed decision procedure.
The implementation controls accompanying this addendum concern the exact
read-set graph, not an end-to-end Presburger solver or a successful template.
