# Real clocks are exact in the finite cylinder model

23 October 2026. Independently analytically signed. This is an exact
reformulation, not a new classification or an UNSAT certificate.

Fix a finite set of full-drift cell classes and a finite discrete set of
complete white histories at each class. Directed-edge counts match, and
the kth traversal of each directed edge is matched to the kth arrival.
This defines a permutation of N active events with integer edge seam
voltages k. Require P=N>0. For each successor arc u to v impose

    t(v) + k P = t(u) + 1.

Also impose every strict chronological inequality between consecutive
visits of a cell. The t variables may be REAL rather than integer.

Indeed, summing the equations around a permutation cycle of length L
and total voltage K yields L=KP. Thus K is a positive integer. Summing
all cycle lengths gives P=N=P times the sum of their positive integer
voltages. Consequently there is exactly one cycle, and its voltage is1.
Fix one active clock to0. Along the unique cycle, each next clock differs
by 1-kP, an integer. Every active clock is therefore integral automatically.
The converse is immediate: an integer-clock solution is a real solution.
Inactive clock placeholders need not be integral and are ignored.

Discrete state and count choices MUST be preserved. Pure linear real
arithmetic is possible by representing each state variable as a real
variable constrained to an explicit finite disjunction s=0 or ... or s=q-1.
All multiplicities and counts are then integer-valued functions of these
finite choices, and P is their integer-valued sum even if declared Real.
Merely replacing integer state bounds 0<=s<q by real bounds would be an
invalid relaxation and is not done.

`probe_cylinder_real_clocks.py` supplies two implementation experiments:
variant0 changes only clocks and port clocks to Real, retaining integer
states, counts, and P; variant1 uses pure linear real arithmetic and adds
an explicit finite-disjunction constraint on every state. The derivation
above is signed. These new formula transformations and solver outputs
still need independent implementation review before promotion.
