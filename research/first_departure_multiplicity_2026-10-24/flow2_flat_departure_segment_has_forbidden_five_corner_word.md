# A whole flat flow-two departure segment has a forbidden five-corner word

24 October 2026. Complete WHITE cap-four translating-front histories,
actual physical cells and full chronology. No period, drift, support,
global maximum, minimum or one-use premise is imposed. Pending review.
This is a symbolic segment obstruction, NOT a classification of all
multiply-used first-R departure cycles.

Let b(v) be the target after v's first R. Normalize a staircase portion
of a b-path to A_k=(k,k), B_k=(k+1,k), with physical edges
A_k->B_k->A_(k+1). Consider the COMPLETE history word

    B_(k-1): WWEE;
    A_k:     NSSN;
    B_k:     WWEE;
    A_(k+1): NSSN;
    B_(k+1): WWEE.

Every b-edge in this word has physical flow TWO, not merely one selected
occurrence. All headings are complete incoming histories and all first
R departures follow the displayed path. No arbitrary period bound is
being searched.

THEOREM: these five consecutive corner profiles cannot occur if the
outside cells also obey WHITE cap-four histories. The word forces two
outer cells SSNN and then an all-cap ordinal-return collision. Other
flat states, odd three-read LEFT corners, turn changes, flow changes and
other exterior configurations remain live.

## 1. Both outer D cells are forced to SSNN

Put D_j=(j+1,j-1) for j=k,k+1. It receives exactly two S arrivals from
B_j and supplies exactly two W departures into B_(j-1). Exhaust complete
WHITE1..4 histories on incoming N/S. The only possibilities are

    NNSS, NSSN, SNNS, SSNN.

Its FIRST W departure follows this actual return chain:

    D_j.W(first) -> B_(j-1).R0 -> A_j.R0 -> B_j.R2
        -> D_j.S(second).

This is FOUR physical steps and has no intermediate visit to D_j. All
ordinals are forced by the complete named histories. In the four candidate
D histories, the source/target ranks are respectively

    NNSS: 1 -> 3; NSSN: 2 -> 2;
    SNNS: 0 -> 3; SSNN: 0 -> 1.

Same-cell consecutive reads are at least four steps apart. Only SSNN
can satisfy this exact return; its first W departure is R0 and its second
S arrival L1. Thus BOTH D_k and D_(k+1) are SSNN. No guessed old input,
future read or optional rank is dropped.

## 2. The next exterior cell has an impossible return at every multiplicity

Let E=(k+2,k-1). It has exactly TWO E arrivals from D_k and exactly TWO
N departures into D_(k+1). Its other ports and total number of reads
are not assumed. The SECOND N departure now has the exact chain

    E.N(second)
      -> D_(k+1).L3
      -> B_k.L1
      -> D_k.R0
      -> B_(k-1).R0
      -> A_k.R0
      -> B_k.R2
      -> D_k.L1
      -> E.E(first).

There are EIGHT physical steps. No intermediate cell is E. This is not
a rank-clock relaxation: the physical successor at every named read
is retained, including both visits to B_k and D_k. The first E arrival
is therefore the VERY NEXT read at E after its second N departure.

That is impossible at ANY multiplicity. Before its first E arrival,
there has been no incoming E read. A departure N is either R(W) or L(E),
so the second N departure must be R(W). The next read is L, and its
incoming heading is E; it therefore departs N. This would be a THIRD N
departure, contrary to the known total two. No WHITE assumption at E
itself is needed for this final alternation argument.

Thus any completion of the five-corner word must violate cap four at
an earlier forced D cell (or change a named complete history/port), not
merely insert missing middle reads at E. No completed board or global
counterexample is constructed.

## 3. Exact symbolic-segment scope

A maximal constant-flow-two staircase segment using the A=NSSN,
B=WWEE modes cannot contain this five-corner subword. It must end, change
its geometric turns, change one of its profile modes, or meet a cell
whose global multiplicity exceeds four before such a repetition occurs.
This is independent of the total segment length or actual full quotient.

The proof does not assert that every flow-two segment uses these modes,
that all multiply-used b edges are impossible, or that one-use follows
from first-ordinal ownership. All exterior incoming AND outgoing ports
of the finite named patch are explicit in the companion JSON. They are
left open except for the three literal return chains above.

check_flow2_staircase_flat_segment_obstruction.py/json reconstructs every
named rank, checks the D candidate histories and replays the exact
physical return paths. It performs no front, period, width, drift,
seed or global multiplicity search.
