# Exact two-row transfer interface for a six-row right cap

Status: exact interface derivation and finite controls. The new analytic
`six_row_polarity_obstruction.md` proves non-composability by a weaker polarity
condition; independent analytic audit passed. The stronger output invariant below
remains unproved and is not used by that proof.

Use headings N=0,E=1,S=2,W=3. Every input/return pose is (0,0,E).
Initial field within the allowed read strip -1<=y<=4 is:
- row0, x<0: black;
- row-1, x<0: white;
- x>=0: arbitrary finite bit words A_x at y=-1, B_x at y=0;
- all cells y=1,2,3,4: white.
The integer index j=0 is the ROOT COLUMN x=0, not a shifted parity index.
An input word is encoded by sum_x[A_x 2^(2x)+B_x 2^(2x+1)].
Unspecified input bits are zero.

Run the actual ant, rejecting a cap if any read lies outside the strip.
A return to (0,0,E) can start the outgoing W20 arm if and only if the following
complete-future W20 input guard holds:

- row0: black for x<=-2 and x=0; x=-1 irrelevant;
- row1: black only at x=0 among x<=0;
- row2: black only at x=-1 among x<=-1;
- row3: white for x<=-1.

These are exactly all first-read colors for W20^infinity from the origin;
all other cells are outside that infinite arm's read set. In addition, require
row4 white at every x<0: otherwise the next translated incoming S arm would
read a black cell where it prescribes R. These conditions are necessary and
sufficient for the two complete arms near this right cap. Define the output
A'_x = final color(x,3), B'_x = final color(x,4), x>=0.
After the W arm and the next incoming S arm, translated upward4, the next cap
has exactly this output as its input. Older cap debris lies below the strip.
Thus the usable cap defines a partial word map T:(A,B)->(A',B').

A usable return is unique: the exact W guard forces W20^infinity afterward,
which never returns to the origin. A fixed cap requires a fixed point of T;
a q-phase cap cycle requires a q-cycle. This does not yet rule out either.
The two arms are treated as complete half-infinite local histories, as in the
independently audited gluing architecture. Finite wide shuttle realizations
inherit this local interface only once opposite caps are isolated.

## Simple sufficient output condition for failure of the next cap

Let r be the first x>=0 with A'_x=0. If B'_j=0 for every
0<=j<=2 floor(r/2), then the next cap has no usable return:
- r even: outward paired packets are followed by a westward S escape;
- r odd: the first missing lower bit turns downward to y=-2.
This is the same elementary first-gap proof as the lower-strip companion
lemma, because none of the B bits encountered before that decisive event is
black. Input bits farther right are never read.

## Top boundary fact and conjectural strengthening

Because the pose sector is x+y+h=1 mod2, top-row4 reflecting passages are
RR at an odd x then x+1 (00->11), or LL at an odd x then x-1 (11->00).
Starting from white row4, the least black top-row coordinate, once present,
is odd and cannot disappear or move right: a deletion of that least odd bit
would need a black even bit to its left. New creations can only move the
minimum left or leave it unchanged. Consequently a usable cap never creates
a negative top-row bit, and its final least B' site s is odd and >=1.

CONJECTURAL, NOT PROVED: if B' is nonempty, the output has A'_s=0 at its least
black B' site s. This would imply r<=s, hence s>2 floor(r/2), and the simple
first-gap failure condition. If B' is empty the condition is automatic.
It would prove T has no composable pair, and exclude every fixed or mixed-
phase right cap whose reads all stay in this common six-row strip.

## Finite controls, not a theorem

`two_row_transfer.py` simulates the exact interface and tests the complete
W guard. `check_transfer_prefix.py` searches the conjectural implication.
For all 1,048,576 inputs supported in columns0..9:
- 384,511 inputs have a usable return;
- 134 distinct usable return words and 50 distinct output words occur;
- all outputs obey the first-gap failure condition;
- no input exceeds the explicit simulation budget (2,000 steps);
- other inputs leave the strip or satisfy exact S/W20 escape guards.

Some transfers INCREASE the two-row black count, including8->12; this is not
a black-token monotonicity argument. The separate finite language experiment
`learn_two_row_language.py` computes residual outcome signatures but does not
claim the input language is regular or extrapolate finite-state convergence.

The stronger A'_s=0 property was separately checked against all 50 saved
width10 outputs, with no counterexample. It remains unproved.


## Negative controls for proposed simplifications

Top-boundary exclusion alone cannot prove the conjecture. The first-principles
analysis gives an exact two-upper-row port counterexample in
`first_principles_new/upper_port_prefix_counterexample.md`: from all-white
rows3/4, ports2,2,0 with words RR,LRRRRL,RR leave row3 black0..3 and row4
black1,2. Both negative half-rows remain white.

`upper_strip_ports.py` strengthens this negative control. With arbitrary
north injections into row1 at even x, complete excursions confined to rows1..4
can satisfy the ENTIRE upper W guard and still violate the desired prefix.
The seven ports are2,2,2,4,4,2,4, with literal words and exit poses saved in
`upper_strip_ports_lo1.json`. This is a physically consistent port sequence,
not a cap path: the lower connections are not arbitrary in the real problem.
The first three ports can be reached from the cap start with lower connectors
RLLRL, RR, LL, but the third excursion exits(-1,0,S). The actual untouched
negative black half-row then forces the next north entry at x=0, whereas the
port counterexample requests x=4. Thus the genuine lower relay/chronology must
be retained. A proof using only the upper strip, even its final guard, is false.

A bounded search with no witness remains UNKNOWN; the saved upper-strip
records are useful because they are explicit counterexamples, not because
of the explored state counts.
