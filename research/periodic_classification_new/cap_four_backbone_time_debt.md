# First-read backbone time debt in a white cap-four front

23 October 2026, 09:50 UTC. Analytic candidate; independent review pending.
Depends on the separately reviewed cap_four_first_read_stream_backbone.md.
No multiplicity, drift-radius or local-word inventory is searched.

Take its maximal-C actual-edge backbone in winding+1 orientation, with
vertices v_i, length ell and first-read times T_i in its physical lift.
After ell edges, v_ell=v_0+d and T_ell=T_0+P. Let j_i be the complete read
rank at v_i which IMMEDIATELY precedes the first read at v_(i+1).

Successive physical visits to one cell are separated by at least four
steps. Consequently

    T_(i+1)>=T_i+4*j_i+1.

A right backbone corner may use j_i=0. At a LEFT corner, its outgoing edge
is not the first R departure, so j_i>=1. The simple essential circle has
equally many R and L corners. Summing gives the candidate stronger bound

    P>=3*ell>=6D.                                      (1)

This does not say the backbone is one uninterrupted ant interval; the
waiting time is precisely what j_i records.

## An additional four units per left-turn run

Every difference T_(i+1)-T_i is1 modulo4, because it consists of one step
following an actual number of complete physical returns at v_i. Write

    T_(i+1)-T_i=1+4*q_i,       q_i>=j_i.

Thus q_i>=1 at every L corner, and q_i>=0 at an R corner. Suppose an L
corner v is preceded ALONG THE BACKBONE by an R corner u, and q_v=1.
Then j_v=1 and the selected L at v occurs exactly four steps after v's
first R. The selected L exits along the backbone's left-turning edge,
so its incoming heading is the SAME as v's first incoming heading. Among
the complete four-step first-return words this forces RRRR, not RLLL.

The last intermediate read of that RRRR unit loop is at u, the physical
predecessor of v's first read. Between that previous u read and this later
u read there is no other u read, and the later one is R. Therefore the
previous u read was L. That previous read is exactly the selected rank
j_u before the first read at v, so j_u>=1, whence q_u>=1.

For each start of an L run, either q_v>=2 (one extra beyond its mandatory
one) or its preceding R vertex has q_u>=1 (one extra beyond its mandatory
zero). These payments are disjoint across L runs: starts are distinct L
vertices and predecessors are distinct R vertices. If s is the number of
L runs and m=ell/2 the number of L corners, then

    sum q_i>=m+s,       P>=3*ell+4s.                   (2)

An essential simple unit-edge circle cannot have four consecutive R turns
or four consecutive L turns: four such unit edges return to the same
physical vertex and close a contractible face. Hence R runs have length
at most three. There are s R runs as well, so s>=ceil(m/3)=ceil(ell/6).
Since ell>=2D, (2) yields

    P>=6D+4*ceil(D/3).                                (3)

This already has the compulsory residue P=2D modulo4. It is a necessary
relation for WHITE cap FOUR only. It does not extend the first-R maximum
rule to cap five, prove a general cap-four exclusion, or settle capture.
The weaker independently reviewed4D+2 multiplicity bound is retained in
its frozen source; this note requires a separate chronology signoff.
