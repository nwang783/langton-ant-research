# Cap-four fronts cannot have full drift (1,1)

23 October 2026. Independently signed analytic proof and complete finite-graph
reconstruction. All widths and periods are covered; this
is not a bounded-width or bounded-period search. Other drift vectors and
higher caps are not classified here.

## Quotient and local states

Choose the checker sector with vertical edges leaving even cells and
horizontal edges leaving odd cells; a translation of the coordinate origin
can always arrange this. On the full-drift (1,1) cylinder take representatives
p_t=(0,t), t in Z. The parity of p_t is t mod2. Every complete white history
is empty, or has turns R,L,R,L truncated at a length from1 through4.
Its incoming headings are chosen independently from E,W at even t, and
N,S at odd t. Thus there are31 states per parity. Directions are N=0,
E=1,S=2,W=3. R adds1 and L subtracts1 modulo4.

Even rows send N to t+1 and S to t-1, both with seam voltage0.
Odd rows send E to t-1 with seam voltage+1 and W to t+1 with seam voltage-1.
Adjacent row count compatibility is therefore exactly:

    even t below odd t+1: out_N(even)=in_N(odd),
                         in_E(even)=out_E(odd);
    odd t below even t+1: out_W(odd)=in_W(even),
                         in_S(odd)=out_S(even).

All but finitely many rows are empty. Pad the lower boundary to begin at
an empty even row and the upper boundary to end at an empty even row.
The total seam voltage is the sum over odd rows of out_E-out_W. An actual
one-period front on its FULL drift cylinder has total voltage1.

## Analytic parity invariant

Starting from the empty lower even row, inductively every even row has
its two R incoming-heading counts equal, and every odd row has its two L
incoming-heading counts equal.

Indeed at an even row

    out_N-in_E = r_W-r_E.

If its R counts are equal, the two compatibility equations force
in_N=out_E in the next odd row, which is exactly l_N=l_S. At that odd row
out_W-in_S=l_N-l_S=0, and the next two compatibility equations force
in_W=out_S at the next even row, which is exactly r_W=r_E.

With cap four, an even row is consequently either empty or has exactly
two R reads, one of each heading. In the latter case all four directed
ports have strictly positive counts. Write a_t=0 or1 according as this
even row is empty or active.

An odd row has l_N=l_S. If both are zero, white alternation makes the
history either empty or a single R. If the odd row is empty, its two even
neighbors are empty. If it is the single R with heading N, the lower even
neighbor is active and the upper one empty. With heading S, the lower
neighbor is empty and the upper one active. Their voltage contributions
are respectively0,+1,-1.

Otherwise l_N=l_S=1, and the history has exactly four reads, with two R
reads. All four ports are positive, so both neighboring even rows are
active. Its voltage is

    out_E-out_W = r_N-r_S,

which is even because r_N+r_S=2. Thus at every odd row between even
neighbors of activity a,b, its voltage is congruent to a+b modulo2.
Summing over the finite strip telescopes to zero because both exterior
activities are zero. Every such static assignment has EVEN total seam
voltage. Voltage1 is impossible, proving the claimed full-drift exclusion.

The same conclusion for rotated unit diagonal drifts follows by applying
a lattice rotation and choosing the checker-origin convention again.
No conclusion for an arbitrary larger diagonal full drift is inferred.

## Exact finite graph control

`check_cap4_unit_diagonal_transfer.py` independently builds all31 histories
per parity and all148 nearest-neighbor edges. The set reachable from either
empty boundary parity has24 parity-labelled states. A parity potential is:

- even empty:0; every reachable active even state:1;
- odd empty and singleton N:0;
- odd singleton S and every reachable quadruple:1.

For every reachable edge u to v, the entering-row voltage is congruent to
potential(v)-potential(u) modulo2. Both empty parities have potential0.
The complete explicit graph, ports, histories, and potential are frozen in
`cap4_unit_diagonal_transfer_certificate.json`. This certificate is finite,
not a truncation in width or voltage magnitude. The independent reconstruction is
`audits/check_cap4_unit_diagonal_independent.py/json`; it verifies the physical
ports, voltages, entire graph, and explicit parity potential.
