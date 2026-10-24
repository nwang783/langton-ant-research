# Exact symbolic interfaces of maximal flow-two/three first-departure segments

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d. b(v) is the neighbor after v's FIRST R, not a last-arrival map.
The physical multiplicity f is the TOTAL use of the edge, not its first
selected occurrence or a unit threshold sheet. Pending independent review.

This classifies the complete local alphabet, endpoints, strand transport
and first-return obligations of a WHOLE arbitrary-length constant-flow
segment. It does not prove that every b-cycle is single-used or that an
unclosed local mode has a complete front exterior.

## 1. Constant selected C height, but not constant physical multiplicity

The signed cap-four first-R maximum rule makes m(b(v))>=m(v). On a
b-cycle the selected clockwise C height is therefore constant c. At
RIGHT geometric corners the incoming b heading is the first-R heading;
at LEFT corners it is opposite. A LEFT corner consequently has BOTH
C sectors at c and opposite R0/R2 headings.

Normalize a RIGHT corner to incoming E/outgoing S and a LEFT corner to
incoming E/outgoing N. The six LEFT profiles have equal incoming/outgoing
physical multiplicities:

    WWE, WWEW:1; WEE, WEEW, WWEE:2; WEEE:3.

At RIGHT corners multiplicity may change; the full fifteen-row control
is first_R_departure_cycle_local_multiplicities.py/json. This alone
already prevents inferring one-use from first-port ownership.

## 2. Arbitrary maximal flow-two segment: complete internal alphabet

Internal vertices preserving flow TWO have exactly these modes. Lists
in/out name actual chronological ranks on the two cycle ports.

    RIGHT EEWW: in(0,1), out(0,3), exterior in(2,3), out(1,2).
    RIGHT EWWE: in(0,3), out(0,1), exterior in(1,2), out(2,3).

    LEFT WEE:   in(1,2), out(0,1), exterior in(0), out(2).
    LEFT WEEW:  in(1,2), out(0,1), exterior in(0,3), out(2,3).
    LEFT WWEE:  in(2,3), out(0,3), exterior in(0,1), out(1,2).

Exterior ports are both physically LEFT at RIGHT corners and RIGHT at
LEFT corners. Every same-rank incoming/outgoing pair is the ACTUAL read;
join outgoing cycle ordinal j to next incoming cycle ordinal j. This
fully specifies the strand network for any geometric corner word,
including all L1/L3 sources. No exterior strand is closed by assumption.

The segment starts and ends at RIGHT changes. In the same normalization,
all possible changes INTO flow2 are

    EW or EWW:1->2; EEE:3->2; EEEE:4->2,

and all changes OUT of flow2 are

    EE or EEW:2->1; EWE:2->3; EWEW:2->4.

Modes may vary along the segment. Odd three-read LEFT WEE and same-R
three-read endpoints are retained, not replaced by a four-read corridor.

## 3. Arbitrary maximal flow-three segment is exactly a G3 subpath

Internal constant-flow THREE modes are

    RIGHT EEEW: in(0,1,2), out(0,2,3);
    RIGHT EWEE: in(0,2,3), out(0,1,2);
    LEFT WEEE:  in(1,2,3), out(0,1,3).

Their single exterior in/out ports are respectively LEFT,LEFT,RIGHT.
The exact internal same-rank connections, not a guessed three-strand
cursor path, are retained. All internal vertices are G3(c) vertices:
LEFT is always negative incoming R2->outL1; RIGHT may be positive or
negative. Thus the segment is a directed G3(c) path with fixed C and
low L=c-3 components.

Its complete endpoint changes are

    START EWE:   2->3, an actual odd same-R G3 source;
    START EWWW:  1->3, G3 enters from an exterior LEFT port;
    END EEE:     3->2, an actual odd same-R G3 sink;
    END EEWE:    3->1, G3 leaves through an exterior LEFT port.

The two rerouting endpoints remain internal G3 vertices, not odd roots.
No endpoint can be dropped just because b chooses its first outgoing
copy. Consequently on a b-cycle with NO one-use edge, every nonclosed
flow3 segment is the ENTIRE source-sink G3 path, with two distinct same-R
odd endpoints. It cannot hide an exterior G3 continuation in an internal
one-use port. Distinct such segments are distinct full-quotient paths;
this is the existing paired-output stock, not a new additive charge.

## 4. Exact all-length clocks for a flow3 segment

Let a segment run from its RIGHT start s to RIGHT end t through m
physical edges. Put a(v)=T1(v)-T0(v), Delta(v)=T2(v)-T1(v). For internal
LEFT corners the first cycle arrival is L1; RIGHT corners receive R0.
Thus the first-R spine gives exactly

    T0(t)-T0(s)=m-sum_(internal LEFT v) a(v).

Middle G3 ordinal2 begins at source/entry L1 and ends at target/exit L1
in ALL four endpoint types. Let epsilon=+1/-1 according as the repaired
middle corner is incoming L1->outR2 or incoming R2->outL1. Then

    T1(t)-T1(s)=m+sum_internal epsilon(v)*Delta(v),

hence

    sum_internal epsilon*Delta
      =a(t)-a(s)-sum_(internal LEFT v)a(v).

These are physical-time identities and retain arbitrary return spans
and full translation voltages. They are not strict monotonicity or
permission to sum overlapping waits as fuel/time budgets. Following
G3 ordinal2 is a repaired path, not an actual uninterrupted ant factor.

## 5. Flow-four blocks between segments retain two persistent strands

A four-use b edge can only be

    RIGHT source EWEW:2->4,
    next RIGHT target SSSS:4->2

in the physical quarter-rotated frame. Source/target first R0 and R2
match exactly across the edge; the incoming/outgoing flow2 strands
persist as R0 and R2. The two additional actual side channels are
source.L1->target.L1 and source.L3->target.L3. They must not be erased
as though unused. Algebraically this is a matched exchange pair, but
there is no physical ant splice.

LEFT corners have flow at most3. Essential simplicity forbids three
successive equal turns, so every flow4 block has a preceding and
following LEFT turn. It is an isolated 2->4->2 atomic block, not an
arbitrarily long flow4 segment.

## 6. Closed flow3-only case inside a local C maximum is impossible

If every edge of a b-cycle has multiplicity at least3, all multiplicities
are exactly3: LEFT corners cannot exceed3, and the RIGHT inventory
permits only3->3 when both sides are>=3. It is therefore a G3 circle
with all LEFT corners negative and winding-1.

If its C component is locally maximal, an LRL triple cannot occur.
In NE coordinates its two LEFT profiles are WEEE, while the middle
RIGHT is either NNNS or NSNN. The same exact single-port calculation
as a31d409e puts the fourth cell's W output before its S input, forcing
NNNS and an adjacent C height c+2. That contradicts local maximality.
With no LRL, essential simplicity and zero signed turning force RRLL.
But signed0cdec955 makes every RRLL G3 strip winding+1, contradiction.

Hence every b-cycle inside a locally maximal C component, in particular
a global M component, has an edge of multiplicity1 OR2. This is NOT a
proof of a one-use edge, let alone of all edges being one-use.

## 7. Physical first-return obligations and current whole-mode controls

For any finite segment word, expose every exterior port occurrence
with its physical source/target coordinate and ordinal. Follow the
actual same-rank read and internal ordinal joins until the next exterior
port or segment end. A resulting chain of n steps has exact clock
increment n. If it returns to the SAME external physical cell and has
no intermediate visit there, its endpoints must be consecutive reads
of that cell, not merely compatible rank-time inequalities. Unknown
exterior ports, including zero-use constraints, remain open elsewhere.
This is the essential additional whole-segment obligation.

Signed90b57415 is a concrete forbidden flow2 word: five consecutive
staircase corners Bprev WWEE,A NSSN,B WWEE,Anext NSSN,Bnext WWEE force
outer SSNN cells and an impossible eight-step return second-N->first-E.
No period cutoff is used. Other internal profile sequences remain open.

The companion flow3_source_sink_segment_open_mode.py/json provides a
DIFFERENT exact globally unclosed flow3 mode: source EWE, negative LEFT
NSSS, sink EEE. Its required side helper is NSS or NSSS. It forces source
T1-T0>=12 and an adjacent lower L height c-4 or c-5. An explicit13-event
partial clock network with helper NSS keeps ALL named histories WHITE,
maximum multiplicity4 and all incoming/outgoing exterior ports open.
It is not a board factor, shared global field, closed b-cycle or complete
WHITE front. It shows why a single short-age completion failure cannot
be promoted to a universal segment obstruction.

The general one-use question remains open after these reductions.
The current alternatives are flat flow2 profile changes, same-R odd
source/sink stock paths, exterior rerouting at one-use endpoints, and
isolated four-use matched blocks, with their full first-return obligations
rather than a hypothetical one-use boundary imposed as a premise.
