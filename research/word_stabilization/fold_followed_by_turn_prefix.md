# A completed C-run immediately after Q or B is an initial-prefix phenomenon

Status: independently replayed finite exact literal certificate.

In every physically feasible word over C,U,V,Q,B:

- QCV can have no prefix, or exactly one preceding macro C,U,V.
- QCCV can have no preceding macro.
- BCV can have no prefix, or exactly one preceding macro C,U.
- BCCV can have no prefix, or exactly one preceding macro C.

In each of the ten feasible cases, the first C phase-1 input is unread in
the entire preceding prefix, as the same literal checker also verifies.
Thus completed C-runs preceded by Q or B satisfy the proposed freshness
statement outright, even when the factor does not begin non-C.

These assertions concern all history BEFORE the displayed factor, not the
continuation after it. In particular, in a factor beginning non-C, the allowed
one-macro prefixes are U,V for QCV, U for BCV, and none for BCCV.

Proof: literal replay verifies each displayed word and its stated one-letter
extensions, excludes every omitted one-letter extension, and excludes all
25 two-letter extensions of QCV, BCV, BCCV. Every longer prefix contains
one of those forbidden two-letter extensions as a suffix. QCCV already has
all five one-letter extensions forbidden.

By the previously audited short-gap grammar, every internal C-run is C or CC
and is followed by V. Therefore, after the first three macro positions, any
completed C-run must be preceded by U or V, never Q or B.

This removes the QCV, QCCV, BCV, BCCV cases from the proposed completed-C
freshness reduction without invoking a local abstraction or a freshness
hypothesis. The UCV, UCCV, VCV, VCCV cases remain unresolved.
