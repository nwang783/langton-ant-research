# A max-turn middle stock hole has at least twelve canonical edges

23 October 2026, 16:59 UTC. Analytic geometric consequence of the repaired
sheets and the pending penultimate orientation lemma. No finite front,
period or polygon scan is used. Pending independent review.

## 1. Exact claim

In a complete WHITE cap-four front, take a contractible canonical sheet
j=M-1 cycle which contains a repaired RIGHT turn around a max C face.
Then its canonical edge length is at least TWELVE.

In particular the higher node of the signed row-5 near return, if it is
contractible, satisfies this bound: at E=S,N,S,S the repaired successor
incoming R2(S) -> outgoing L1(W) is a RIGHT turn around the max H.
The penultimate orientation lemma makes this cycle counterclockwise.

## 2. Length is a multiple of four

Every repaired physical passage turns by a right angle: incoming and
outgoing axes at a fixed cell are perpendicular. Thus a closed canonical
walk has equally many horizontal and vertical edges. Zero displacement
makes each of those numbers even, so its total length is divisible by
four. A canonical sheet uses each physical edge at most once.

A length-four counterclockwise cycle is a square with four LEFT turns,
so it has no RIGHT turn. It remains to exclude length eight, retaining
possible repeated physical vertices after rounding.

## 3. No simple eight-edge straight-free grid polygon exists

If the physical projection has no repeated vertex, it is a simple unit
lattice polygon. Four horizontal and four vertical edges bound its width
and height by two. If either dimension is less than two, its enclosed
unit-cell region has at most two cells and perimeter at most six. In the
2-by-2 box, an eight-edge simple boundary encloses either an L triomino
or the full 2-by-2 square. Both have a boundary segment of length two,
whose intermediate lattice vertex is a STRAIGHT passage. This contradicts
the canonical right-angle pairing at every vertex.

Thus an eight-edge canonical cycle must repeat a physical vertex.

## 4. The only rounded eight-edge exception has no max RIGHT turn

At a repeated vertex, the edge-simple eight-step walk splits into two
positive closed walks, each of length divisible by four. Hence both are
unit four-squares. Their edges cannot overlap, so the two squares meet
diagonally at that vertex. For one counterclockwise rounded cycle, they
are the two diagonal L-face squares, joined by the two RIGHT corner arcs
at their common vertex. The other six turns are LEFT. All its RIGHT
turns occur at that one four-port junction.

At j=M-1, a four-port RIGHT pairing cannot have a max C face there:

- If the C heights were M and M-1, cap four allows only one R. A white
  R or RL inventory cannot make all four physical ports positive: its
  two reads share an input or an output. Four threshold ports are
  therefore impossible.
- If both C heights were M, four active penultimate ports force the
  opposite-L RLRL case, whose repaired penultimate pairing is two LEFT
  turns, not two RIGHT turns.

The only remaining four-port RIGHT junction has both C heights M-1.
Its RIGHT turns are not around a global max face. Therefore this rounded
eight-edge exception cannot be the cycle in Section 1.

Lengths four and eight are excluded, so the next possible length is at
least twelve. No assertion of a realizable twelve-edge white connector
is made.

## 5. Safe counting scope

Several row-5 renewals may use the SAME middle stock-hole node, so the
bound is not twelve reads per renewal. Distinct canonical node-cycles,
however, have disjoint actual edge occurrences. A register of h distinct
contractible middle cycles satisfying this max-RIGHT-turn hypothesis can
safely reserve at least 12h occurrences in the canonical partition. The
max-face top cycles use different sheets and remain disjoint. This does
not create a bound on h or an improved global speed constant by itself.

Sources: chronological_stream_sheet_exchange.md, SHA
fd20e425b8a6bbc3aefd5eca06b4d443c1d2bdfde5f1d2d69c25d5c4d62af484;
penultimate_max_adjacent_contour_orientation.md, SHA
a2170bdce45e58734901f1ebb215f7ac5f7b58ab26deafe2cac8567a3133ec22.
