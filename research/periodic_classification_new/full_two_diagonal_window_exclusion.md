# Cap-four exclusion for full drift (2,2), with no width bound

23 October 2026. Independently signed analytic and finite-certificate result.
No complete white-input translating front of full drift (2,2), or an
orientation-preserving quarter rotation of that vector, can have every
physical cell visited at most four times. Neither the event period nor the
support width is bounded. This does not exclude cap five, larger diagonal
full drifts, or arbitrary cap-four fronts.

## Physical representatives and local states

For full drift d=(n,n), let row t contain the n representatives
p(t,i)=(i,i+t), 0<=i<n. Here n=2. Choose the checker sector in which even
rows have vertical outgoing edges, and odd rows have horizontal outgoing
edges. The other checker sector is an integer translation of this one.
Each cell history is an incoming-heading list of length zero through four,
with its turns alternating R,L,R,L, beginning R. There are31 possible
histories per cell and parity, hence 2*31^2=1,922 unpruned parity-labelled
row states.

A vertical edge keeps column i and changes t by +1 for N or -1 for S;
its seam voltage is zero. An east edge from an odd row changes t by -1,
changes column to i+1 modulo n, and has seam voltage floor((i+1)/n).
A west edge changes t by +1, changes column to i-1 modulo n, and has
seam voltage floor((i-1)/n). These are literal physical edge displacements,
not a primitive-diagonal identification. Match each directed edge's kth
exit to its kth arrival. Count-compatible adjacent rows have8,320
transitions before the optional balance reduction.

Summing the port equations across a row gives the same empty-exterior
balance induction as in the unit-diagonal argument: on every even row
the total numbers of R arrivals from E and W agree, and on every odd row
the total numbers of L arrivals from N and S agree. This leaves259 even
and225 odd row states, with3,304 transitions. The independent checker
starts without this reduction, so the theorem does not depend on trusting
its implementation.

## Three-row necessary chronology tests

Apply exactly the signed internal-path and sealed-cycle rules in
`unit_diagonal_window_exclusion.md`. An internal simple successor segment
of length L<P and seam voltage w has representative clock difference
L-wP. Earlier-to-later local event indices therefore forbid w>=1;
later-to-earlier indices forbid w<=0. A sealed internal successor cycle
must be the entire global event cycle. A cycle containing every active
window event is explicitly treated as a possible whole-front exception
when its voltage is one and all local orders are correct; it is not
silently rejected. No such exception occurs in this certificate.

A transfer node records the parity and exact states of the last two rows,
and cumulative seam voltage modulo two. Starting with two empty rows,
append every compatible next row, reject just the preceding sound
three-row obstructions, and shift one row. This is a finite graph
construction, not a bounded-width orbit search.

## Complete certificate and conclusion

The complete reachable lifted graph has1,275 nodes and4,944 accepted
edges. Both possible all-empty boundary parities occur only with cumulative
voltage parity zero. There are738 nodes that can return to an empty state,
including736 active nodes: nonempty returns are NOT excluded. The exact
invariant is instead that every empty-to-empty path has even total voltage.

Any finite-width full-drift front pads with two empty rows on both sides,
so its row sequence would give a path in this complete graph. The total
voltage of its one full event cycle is one, contradicting even voltage.
This proves the stated all-width, all-period exclusion.

Producer: `probe_diagonal_n_window.py`.
Summary: `diagonal_n2_cap4_window3.json`.
Complete certificate: `diagonal_n2_cap4_window3.certificate.json`.
Certificate SHA256:
`c68dcc6fc7331c543fa153e03227503c8bbc6b8db0f36bca338ca9edf4942bcb`.

Independent reconstruction starts from all1,922 row states and8,320
physical transitions, derives representative edges, seam voltages,
rank-matched successors and clocks separately, and recovers the same
complete reachable graph. Its files are
`../audits/check_diagonal_full_drift_window_independent.py` and
`../audits/diagonal_n2_cap4_window3_independent.json`; signed ledger HM.
