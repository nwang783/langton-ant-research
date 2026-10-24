# A double-C turn forces a longer pure-V return corridor

Status: independently audited analytic proof using the two terminal-C barriers.

In any physically feasible right-infinite five-macro word:

1. An occurrence V^n CC, n>=1, is followed by at least n+1 consecutive V blocks.
2. An occurrence U V^k CC, k>=0, is followed by at least k+2 consecutive V blocks.

The statement concerns infinite continuations. A finite word can stop sooner,
including with a terminal C which cannot be followed by any macro.

## A balanced V corridor has only V as an extendible next macro

At the endpoint of V^r CC V^r, r>=1, the pose is (-1,1,S), normalized at
the first V. The first V reads (-1,-1) exactly once, as L at phase2.
Every later outward read has height>=2. Both middle C blocks have height>=2,
and every returning V read has height>=1. For A in U,Q,B, phase12 reads
(-1,-1) as L, with no earlier read of that cell inside A. Thus

    V^r CC V^r A

is infeasible for A in U,Q,B. The following C is feasible in examples, but
cannot itself be followed by any macro, by the balanced-CC terminal barrier.
Consequently only V can be the next macro in a right-infinite continuation.

After V^n CC, the first returning macro must be V: the exact short-gap
grammar excludes every other extendible choice. After j returning V blocks,
1<=j<=n, the suffix V^j CC V^j has the preceding property. Induction therefore
forces n+1 returning V blocks.

## The extra U rail forces one further V

At the endpoint of U V^k CC V^(k+1), the pose is (-2,2,S). The first U reads
(-1,0) once, as L at phase1. Every outgoing V and middle C reads at height>=3.
Every returning V reads at height>=2. Therefore no intervening block reads
(-1,0). A following A in U,Q,B first reads that cell at its phase13, as L,
giving a consecutive L/L conflict. A following C cannot be extended, by
unbalanced_u_cc_turn_barrier.md. Only V can continue infinitely.

For k>=1 the first part already forces k+1 returning V blocks; for k=0 the
short-gap grammar forces the first V directly. The extra-U argument then
forces one additional V, proving the second statement.

## Scope

This is an unbounded necessary macro-language constraint, not a proof of
completed-C input freshness. In particular U/Q/B moves can occur after the
forced return corridor; the lemma does not control all subsequent turns.
