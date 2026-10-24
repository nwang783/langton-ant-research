# A one-sided positive-moment fuel obstruction

2026-10-23 02:23 UTC. Analytic extension, submitted for independent audit.
This note is separate from the frozen Fourier bridge so its proof and
implementation can be reviewed independently.

For any actual ant prefix on a finite initial seed B, its signed occupation
polynomial F satisfies coefficientwise F=1_(B_after)-1_B. Consequently for
EVERY positive real x,y,

    F(x,y) >= -sum_(b in B) x^(b_x) y^(b_y).                (1)

The right side is a fixed finite constant. This does not require charge
preservation. Thus a sequence of proposed prefixes for which F_r(x,y) is
unbounded below at one fixed positive character cannot have finite support.
No claim is made for infinite initial black backgrounds.

For the unit-scale heading-preserving refinement model of bridge.md, the
same eight-state periodic Laurent transfer evaluates at rational x,y>0 to
rational matrices. It gives exact scalar linear recurrences, even for unequal
image lengths. Unlike the unit-torus test, positive moments need not be
bounded above. Positive divergence alone is not an obstruction.

positive_moments.py implements one sufficient, terminating certificate.
For each rotation phase and even/odd grouped-level subsequence it computes
and verifies the exact minimal scalar recurrence. It requires all irreducible
factors to be linear over the rationals or cyclotomic. If there is a unique
positive rational root R>1 of largest modulus, with multiplicity m, write
its generating function as N(z)/D(z) and

    H(z)=D(z)/(1-Rz)^m,
    C=N(1/R)/(H(1/R)*(m-1)!).

Then the sequence is C R^n n^(m-1)+o(R^n n^(m-1)). Minimality makes C nonzero.
C<0 certifies negative divergence, contradicting(1). Factors not satisfying
the stated root condition yield NO CERTIFICATE, not a boundedness verdict.
A positive dominant coefficient also gives no finite-support exclusion.
The even/odd subsequences can expose an alternating negative mode; they do
not license forgetting which refinement phases are actual prefixes.

The method deliberately does not claim to decide general positivity or
boundedness below for arbitrary linear recurrences.

A useful strict separation from the Fourier test is the formal polynomial
sequence F_r=2-X^r. It has charge1, uniformly bounded Laurent L1 norm and
bounded evaluations at every unit-torus character. But F_r(2,1)=2-2^r is
unbounded below, because its negative particle moves through infinitely
many initially black sites. It cannot be an actual finite-seed occupation
sequence. This is an algebraic control, NOT a geometric ant model.

Conversely F_r=X^r and F_r=X^r+X^(-r)-1 pass these necessary algebraic tests;
that is not a realizability claim. The second displays exactly the two-sided
positive transport with fixed negative support that these tests leave open.

On the24 already excluded k9 geometric controls, eight small positive
characters yield10 certificates in positive_controls.records.json. This is
an implementation control, not another newly closed construction family.
The Fourier test already rejects all24. Direct transfer checks and synthetic
negative/positive leading-coefficient controls are in
check_positive_moments.py/json.
