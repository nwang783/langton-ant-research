# Fuel requirements of a reachable recursive block constrain its wrapper

2026-10-23 06:03 UTC. Elementary analytic bridge, submitted for review.
This applies to actual finite-support rooted refinements, not merely local
legality on independently chosen backgrounds.

## General bound

Let a fixed nonerasing typed substitution have a growing rooted fixed word
that is an actual ant path from initial black mass M. Let s be any reachable
state, and choose one occurrence of it in a finite root power, with preceding
typed word w. Denote by E_r(w) the signed R-minus-L charge of phi^r(w), and by
m_r(s) the minimum number of initial black cells needed for the finite word
phi^r(s) to be internally ant-legal.

Then, at every refinement depth r,

    m_r(s) <= M+E_r(w).                                    (1)

Indeed, phi^r(w) phi^r(s) is an actual prefix segment inside the corresponding
larger root power. The ant has exactly M+E_r(w) black cells immediately before
the chosen block. Its entry board realizes that block, so contains at least
its minimum required first-L fuel. This uses one fixed canonical occurrence,
not an earliest occurrence or an independently reset board.

In particular, if every local image preserves its parent's signed charge,
then E_r(w)=E_0(w) is constant. Every reachable recursively refined block
must have uniformly bounded required initial fuel, with a bound depending on
M and this finite preceding word.

More generally a known lower bound m_r(s)>=f(r) forces
E_r(w)>=f(r)-M. Bounded checkpoint mass or bounded root charge alone should NOT
be substituted for this precise canonical-prefix condition without proof.

## Consequence for the certified decorated hairpin

The all-r positive transport with

    U=LRLLLLRRRRLRRL,   s=R,   V=RLRRLL

has phi^r(s)=U^r R V^r and exact minimum entry fuel6r. Therefore any finite-seed
stationary rooted wrapper containing this recursive state needs, for EACH
fixed representative occurrence with preceding word w,

    E_r(w) >= 6r-M.

It cannot appear as a reachable recursive state of an exact-charge-preserving
finite-seed controller, even if arbitrary extra context labels, rotations,
multiple drifting cycles, or complicated root words are added. The local
hairpin itself preserves net charge+1; its growing rail requirement cannot be
met by merely adding other charge-preserving components.

This does not exclude a wrapper whose earlier refined blocks genuinely create
the required growing mass, or a nonstationary setup. Such a proposal must also
satisfy all complete input/output tile and chronological constraints. No such
wrapper or growing finite-seed model is supplied here.
