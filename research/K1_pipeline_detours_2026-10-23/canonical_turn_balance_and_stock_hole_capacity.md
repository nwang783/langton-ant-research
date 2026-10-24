# Canonical turn balance gives a safe capacity for distinct stock holes

23 October 2026, 17:10 UTC. Exact global cycle register, pending independent
review. It does not charge a hole per renewal or identify fresh roots.

## 1. Full-period identity

Use a complete WHITE cap-four front and its signed repaired sheet cycles.
Let C_plus count all contractible CLOCKWISE canonical cycles, and C_minus
all contractible COUNTERCLOCKWISE canonical cycles, across every sheet.
Then

    R-L = 4(C_plus-C_minus).                       (1)

The L1/R2 occurrence repair preserves the aggregate physical turn
inventory at each cell. Its two visits share one incoming or outgoing
physical port; swapping their occurrence association keeps the same two
physical R/L corner turns, one of each. R0, optional L3, and one-R cells
are unchanged. Thus actual total R-L equals the canonical total signed
quarter turns.

Each rounded canonical circle is embedded. A contractible clockwise
circle has turn +4, and a counterclockwise one -4. An essential embedded
circle in the flat drift cylinder has turn zero: the annulus between it
and a distant parallel straight circle has zero Euler characteristic
and zero interior curvature. Summing gives (1), including cycles whose
physical projections touch a vertex in two disjoint rounded corners.

A complete WHITE cell history contributes one to R-L if its length is
odd, and zero if even. Hence

    number of odd complete cell classes = 4(C_plus-C_minus)>=0,
    C_plus>=C_minus.                              (2)

The canonical orientation count is not the graph cycle excess and is
not the number of original black roots.

## 2. A distinct stock-hole count, not a renewal count

Let H be the number of DISTINCT contractible penultimate-sheet cycles
with at least one repaired RIGHT turn around a global max C face. The
signed orientation and length lemmas make them counterclockwise cycles
of length at least twelve. They need NOT be graph leaves.

Therefore C_minus>=H, and (2) gives C_plus>=H. Distinct canonical node
cycles partition actual edge occurrences. We may reserve:

- at least 12H occurrences in those H stock-hole cycles;
- at least 4H occurrences in H distinct clockwise cycles;
- at least 2D occurrences in one essential canonical cycle, where
  D=||d||infinity.

The first two families are disjoint by orientation, and the essential
cycle is disjoint from both. An essential cycle exists because total
sheet homology is one. Its horizontal and vertical edge totals are
equal, and winding is +/-1, giving its length at least 2D. Consequently

    P >= 16H+2D.                                 (3)

This is a genuine nonleaf-capable capacity statement per DISTINCT
canonical hole. It does not say that many renewal sites force many holes:
they may share the same node, graph cycle or old-stock archive.

## 3. Retaining the already known top-face register

If F_max is the number of global-max C face classes, there are exactly
F_max top-sheet clockwise four-edge cycles. Thus

    C_plus>=max(F_max,H).

The same disjoint canonical partition gives the slightly fuller register

    P >= 12H + 4 max(F_max,H) + 2D.                (4)

Do not replace max(F_max,H) by F_max+H: the existing top cycles may be
exactly the clockwise compensation for these counterclockwise holes.
Do not add (3)/(4) to overlapping first-read or side-current bounds without
a separate joint register. They may safely be combined with another
whole-period lower bound by taking the maximum.

## 4. Exact controls and open issue

The prepared W20 star has 2a clockwise top squares, 2a counterclockwise
lower squares, and one essential middle cycle. It gives R-L=0 in (1),
but has explicit black singleton-L inputs and is not a WHITE front.
Its old-white and black-fuel lower leaves still have identical simple
graph signatures. Neither(1) nor(3) identifies their causal supply.

The signed row-5 return may choose an essential middle node instead of
a contractible hole, and multiple renewals can choose one shared hole.
Thus no all-case K>=2 theorem, permanent fuel bound or finite-seed capture
follows. The separate -5 bracket identity applies only to the stricter
contractible graph-LEAF subcase and is not summed into (3) here.

Sources retained unchanged: signed chronological sheet repair
fd20e425b8a6bbc3aefd5eca06b4d443c1d2bdfde5f1d2d69c25d5c4d62af484;
penultimate orientation a2170bdce45e58734901f1ebb215f7ac5f7b58ab26deafe2cac8567a3133ec22;
stock-hole length 1527bbd19fa04c9ad92a8a2c97f8e5926b8537ac2e51c40b0a0a1c57dbf0c43f.
