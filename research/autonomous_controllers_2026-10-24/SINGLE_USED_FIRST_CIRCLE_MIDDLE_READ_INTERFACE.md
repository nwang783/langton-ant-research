# Single-used first circles expose an actual middle-read obligation

24 October 2026. Author proof, submitted for independent review. This is a
conditional all-cap structural reduction of the acyclic-E remainder, not
an exclusion of growth eight or a classification of controllers.

## 1. Exact boundary lemma

Assume a COMPLETE WHITE translating front, with the actual full drift d,
period P, complete alternating histories, one actual event orbit, and all
used support retained. Let F be its first-R-departure graph. Suppose a
quotient F circle C has every cycle edge used exactly once in the full
physical history. The invariant incoming/outgoing axes forbid a hidden
reverse traversal of any of these edges.

The signed first-departure theorem makes C a simple essential circle of
winding -1. At a vertex, let A be its first incoming heading. Because its
first outgoing port is used only once, its entire heading history is

    A, A, -A, A, -A, A, ... .

This is the source-port formula from the signed single-use lemma; no
visit-count cap is assumed. Its cycle incoming port is also used once.

- At a geometric R corner, that incoming heading is A. The source formula
  uses A again at rank1 if any further read exists. Hence the cell is a
  singleton.
- At a geometric L corner, that incoming heading is -A. The formula first
  uses -A at rank2 and uses it again at rank4. Hence the complete history
  is exactly A,A,-A or A,A,-A,A, with respectively three or four reads.

Every off-circle used port at an L corner lies to the RIGHT of C, with
multiplicity two or three. A singleton has no off-circle used ports.
The connected full used support and cylinder separation therefore put
ALL other read support to the right. In particular there is at most one
such single-used F circle. This does not assert that one exists.

At an incoming edge whose target is a triple, the arrival is its LAST
read, so this is an E edge. At a target quadruple, the arrival is its
MIDDLE R at rank2, followed later at that same physical cell by L3.
Thus a single-used F circle is an E circle exactly when it has no
quadruples. The independently signed acyclicity theorem for g=8 forces
at least one quadruple on such a circle, if it exists.

This is an actual missed terminal event, not an assignment of its resource
to the first-R edge. The R2-to-L3 lifetime and all other reverse BLACK
output roots remain present.

## 2. The four-edge, one-quadruple case

Specialize only now to full d=(2,-2), sector sigma=+1 and a four-edge
single-used F circle. Up to a genuine physical translation and rotation,
its lower two rows are

    t=-1: T0=(0,-1), T1=(1,-2), both heading W;
    t= 0: B0=(0,0), SSNS; B1=(1,-1), SSN.

There is exactly one quadruple in this case. The two-quadruple case is
separate and remains open; a general acyclic front need not have this
circle at all. With t=x+y the complete remaining read support has t>=1.

The three E edges form the directed path B0 -> T1 -> B1 -> T0, with
physical drift lifts retained. The next first edge T0 -> B0 lands on
B0.R2, NOT B0.L3. In particular it does not close E.

Let A0=(0,1), A1=(1,0). Exact ordinal matching gives:

    A0: two incoming E reads and three outgoing S reads;
    A1: three incoming E reads and two outgoing S reads.

At either A cell, its FIRST S departure executes an uninterrupted physical
four-step return through B.firstR, T.singletonR, and the neighboring
B.R2, ending at its SECOND E arrival. No intermediate read hits that A
cell. If s0 is the rank of its first S departure and e1 the rank of its
second E arrival, therefore

    e1 = s0 + 1, with actual clock gap exactly 4.

B0.R2 need not be terminal for this argument, which is the point of the
acyclic extension.

## 3. Exhaustive complete histories at the immediately adjacent row

For a C cell with I incoming E and J outgoing S reads, write n for its
complete history length and a for the number of R reads arriving E.
Alternating WHITE turns give

    floor(n/2) + 2a = I+J.

Thus n<=2(I+J)+1 is DERIVED, not an imposed cap. Combining this count,
I fixed E occurrences, and e1=s0+1 gives exactly

    A0: EEWWWW, WEWWEW, EEWWWWW, WEWWEWW;
    A1: EEE, EEWEWW, EEWWWE, WEWWEE,
        EEWEWWW, EEWWWEW, WEWWEEW.

All 28 pairs satisfy the lower patch's open matching and rank conditions.
No statement that all 28 physically complete is made. Some are already
six- or seven-read histories, outside the earlier cap-four framework.

## 4. An exact standard-positive branch, and the remaining g=8 choices

The genuine standard104 front contains this precise one-quadruple circle
and adjacent pair

    A0=EEWWWW, A1=EEE.

The checker reconstructs ALL 22 stable histories directly from the literal
standard word, with full d=(2,-2), including all classes outside the named
patch. This control has g=12, not eight; the proof does not substitute a
cropped standard patch for a complete g=8 field.

For this adjacent pair the next Q row has counts

    Q0: incoming N=3, outgoing W=0;
    Q1: incoming N=1, outgoing W=4.

The lower patch forces the second W departure of Q1 to its first N arrival
by an uninterrupted eight-step physical return, so these two ranks are
consecutive. Full WHITE alternation and the counts give exactly

    Q0 = NSNSNS or NSNSN;
    Q1 = SSSNSS or SSSNS.

All four are open local interfaces. For a hypothetical FULL g=8 extension,
the signed x/y residues modulo2 give, in bin order (00,01,10,11),

    v00-v01 = v11-v10 = v00-v10 = v11-v01 = 2 (mod 4),
    v00+v01+v10+v11 = 8.

The lower patch already has (0,1,2,1). Thus:

- Both Q histories even: possible full inventories (0,2,2,4) or (1,3,3,1).
- Q0 even, Q1 odd: only (0,2,2,4).
- Q0 odd, Q1 even: only (1,3,3,1).
- Both odd: IMPOSSIBLE at g=8, since no full inventory dominates (1,1,2,2).

The remaining three branches retain every higher port and an unbounded
higher region. They are not translators or realizations. This one exact
parity rejection is not a general g=8 exclusion. A discovery extension
of those branches leaves further open interfaces; it is not being
promoted to a classification or an exhaustive certificate here.

## Dependencies and controls

- EXTREMAL_SINGLE_USE_EDGE_LEMMA.md, SHA5648cb49; independent report9b0906ab.
- G8_CYCLIC_E_EXCLUSION.md8981c7ff WITH mandatory read-footprint addendum
  b24cf42a; independent report e1d595f2.
- ../periodic_classification_new/white_first_departure_counterflow.md.
- Signed residue source ../sources/kehao95-core/wake_synthesis/proof/
  periodic-growth-closure.md, with its retained attribution.
- check_single_used_first_circle.py and matching JSON reconstruct the
  row lists, every full standard history, and the four parity inventories.
  They import the frozen ordinal graph engine
  enumerate_g8_cycle_two_outer_rows.py (SHA c23d88a3).

No historical width-ten exhaustion, arbitrary visit cap, opaque solver,
infinite prepared input, or cap-four terrain claim is a premise.
