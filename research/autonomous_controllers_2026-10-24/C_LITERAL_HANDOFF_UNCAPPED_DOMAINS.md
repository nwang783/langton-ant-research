# Exact uncapped domain of a literal first/last C handoff

24 October 2026. Author corollary and complete controls; independent audit
pending. This refines the correctly layered joint graph9a1c3716, not its
collapsed spatial projection. Existence of such a handoff is NOT proved.

Suppose the actual last active read of physical C face u is an L at a cell p,
and the next update is the FIRST active read of C face v. This is a literal
one-step chronological handoff, B(u)+1=A(v), with the appropriate full-drift
translate included when using representatives.

## Complete cell histories, with no visit cap

The signed first-entry theorem makes this selected L the first L of p. If p
is WHITE-first, its preceding R0 has the SAME incoming heading h. If it is
BLACK-first, this L is rank0 and the actual input remains explicit.

After this L, any read of p from heading h would activate the retired face u,
which is impossible. A later read from heading -h is at v, but if that read
were L, its next update would activate u again, also impossible. Thus there
can only be one later opposite-heading R, and no further read. The complete
possibilities are exactly

    WHITE:  h,h with turns RL; or h,h,-h with turns RLR.
    BLACK:  h with turn L; or h,-h with turns LR.

The final R, when present, is a genuine permanent output of the WHOLE history,
not merely an output of a cropped factor. A BLACK LR case retains BOTH the
initial input and the later output as distinct lifetime roots. These four
modes derive a local read bound at the handoff cell; no bound is imported at
its neighboring C faces or elsewhere in the controller.

## Exact identities and conditional span bounds

Let S(u)=B(u)-A(u), S(v)=B(v)-A(v). The FIRST edge from u to v and LAST edge
from u to v both exist at this same physical L. Their exact gaps are

    g_FIRST=S(u)+1,       g_LAST=S(v)+1.

If this edge belongs to a first-entry cycle, its gap is at most that cycle's
full-period sum P, so S(u)<P. If it belongs to a last-exit cycle, analogously
S(v)<P. In particular a shared-cycle handoff bounds both endpoint spans.
The claims apply to the supplied FULL period, including powers, and retain
all edge voltages. They do not establish that any handoff lies on a cycle.

## Positive controls and retained alternatives

Standard104 has one literal handoff per primitive period, at L26. It belongs
to a WHITE first-entry cycle and a last-exit cycle. Its complete cell history
is R14,L26,R30, with incoming N,N,S. Its source/target face spans are13/101,
and the corresponding first/last gaps are14/102. These are actual complete
histories inside the known finite-seed standard future.

Prepared10 has no literal handoff. Prepared80 has two: WHITE RLR at L51 and
WHITE RL at L75. Neither is on a WHITE first-entry cycle. Its two infinite
input rays remain necessary. Thus the local RLR mode alone is not a WHITE
controller certificate, and the RL option must not be silently removed.

Supplied1564 and4352 have100/90 literal handoffs with all four modes retained.
For example1564's WHITE RL handoff at phase2 lies on BOTH full first/last
cycles, but that full first-entry cycle contains prepared BLACK roots. It is
not a counterexample to any theorem requiring a complete WHITE cycle; equally,
cycle intersection alone cannot discard the even RL mode.

The checker rebuilds every complete handoff history in all five controls and
forty-eight rotation/power controls for standard,10 and80. No cap on the
surrounding histories, period or read footprint is assumed. No finite local
alphabet for the intervening excursions or source fields is inferred.

## Remaining target

A proof that a suitable shared-cycle WHITE RLR handoff MUST occur would be a
new global statement. It is not supplied by these local domains, the temporal
forests, or a spatial path between their components. Even that statement alone
would not force the standard12/4 return ages or the104-word module.

Artifacts: certify_C_literal_handoff_domains.py and
C_literal_handoff_domains_certificate.json. Exact dependencies are embedded.
