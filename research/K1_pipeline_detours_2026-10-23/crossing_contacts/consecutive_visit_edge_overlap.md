# A literal all-cap contact obligation

## Result and scope

At a fixed square-grid Langton-ant cell, any two consecutive visits share
at least one undirected incident edge. Consequently a prescribed pair of
opposite-heading R turns, which would use all four incident edges, cannot
be two consecutive visits. It requires at least one intervening L visit
at the same cell. That L visit reuses one incoming and one outgoing port
of the proposed R pair.

This is a local chronology statement for arbitrary initial colors and
arbitrary visit counts. It is not a global no-crossing theorem, a bound
on the number of compatible crossings, or a paid resource. A repeated
edge may be perfectly legal and may later be used again.

## Proof with the physical-heading convention

Let h_t in Z/4 be the incoming movement heading at the cell read at time
 t. Use N=0, E=1, S=2, W=3, with an R adding 1 and an L subtracting 1.
Every step changes the heading parity and the vertex checkerboard parity.
Therefore h_t - x_t - y_t modulo 2 is constant. All incoming headings at
one fixed vertex have the same axis: two such headings are equal or
opposite. Outgoing headings have the perpendicular axis.

At each read the cell color is toggled. Thus consecutive visits to that
cell have opposite turns, independent of all intervening motion. Write
those turns as epsilon and -epsilon, where epsilon is +1 or -1.

If their incoming headings are equal, they reuse the incoming edge.
If the incoming headings differ by 2, their outgoing headings are
h + epsilon and h + 2 - epsilon. These are equal modulo 4, so they
reuse the outgoing edge. These are the only two possibilities.

For two proposed R reads with incoming headings h and h+2, their input
ports are distinct and their output ports are distinct. Hence they use
all four incident edges. They cannot be consecutive reads, since colors
would then demand R,L. Between any two actual R reads at that cell
there is an odd positive number of visits, starting and ending in L.
Each intervening L connects one of the proposed input ports to one of
its proposed output ports. In the minimal R,L,R history, this L is the
explicit cross-pair bridge: L(h) exits h-1, the second R's output, while
L(h+2) exits h+1, the first R's output.

## The existing prepared-1564 itinerary certificate

The frozen input certificate is
causal_reduction/unit_scale/prepared1564_connected_itinerary.json.
Its first case has n=100 and T=(200,400,600). The first contradictory
prescribed read is at cell (383,380), absolute time 205680, stage
B_incoming offset 20752, incoming W, proposed R. Its preceding read at
that cell is absolute time 94896, stage router1 offset 1034, incoming E,
R. The accompanying checker updates last[p] after every compatible read;
therefore these are consecutive visits, not merely two selected reads.

The earlier actual R(E) exits S and leaves that cell black. The next
actual read must consequently be L(W), also exiting S. The proposed
second R(W) would exit N instead. Thus the first mismatch has the exact
local merge form, with one shared outgoing S edge. Replacing that R by
L determines only this one next step, not the later global lane.

The second certificate case analogously contains consecutive prescribed
R(N), R(S) at (766,806), times 157767 and 266931. The actual second L(S)
exits E, the same edge as the earlier R(N).

No itinerary was replayed for this note. The existing JSON and the
checker's last[p] update rule supply the certificate. No cap-four,
white-front, stream-height, primitive-period or disjoint-support
assumption was imported.
