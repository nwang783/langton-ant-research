# A literal prepared twenty-read control for the bent K=1 gate architecture

23 October 2026, 15:20 UTC. Exact algebraically prescribed control, not a
period search and NOT a white-input front. Independent replay requested
independently of the wave audit.

## Literal word, full displacement and complete quotient histories

Start at physical(1,0), incoming N, and execute

    W20=LRRRRLLLLRLLLLRLRRRR.

The actual endpoint is(1,2), incoming N, so full P=20,d=(0,2). For full
copies1,2,3 the retained data are P=20a,d=(0,2a), not a silently reduced
primitive quotient. Exact repeated physical read colors alternate.

For the one-copy quotient, with y reduced mod2, the complete histories are

| cell | incoming headings in rank order | turns | input |
| ---- | ------------------------------- | ----- | ----- |
| (0,0) Z | W,W,W,E | RLRL | white |
| (0,1) Y | N,N,N,S | RLRL | white |
| (1,0) A | N,N,S,N | RLRL | white |
| (1,1) B | E,E,W,E | RLRL | white |
| (-1,0) | S | L | BLACK fuel |
| (-1,1) | W | L | BLACK fuel |
| (2,0) | E | R | white |
| (2,1) | S | R | white |

Thus the FOUR main cells have the complete WHITE cap-four histories of
an alternating RIGHT/LEFT first-L curve with locked gates. The two
missing black suppliers are explicit LEFT single-L rails; the two RIGHT
single-R cells are black outputs. These fuel reads are not pretended to
have hidden R predecessors.

The exact physical stream, normalized with RIGHT/east exterior0, has
c_left=-1,c_right=0,max_C=1. Hence the prepared control has excess K=1.
The max C faces form the alternating-bend rail (0,even) and(1,odd),
with immediate LEFT other-C height -1. This stream is reconstructed from
literal edge counts; no white-input global-max theorem is imported.

## The old-stock cleanup is physically connected

The main interval beginning at A's L1 has actual events

    A.L1,Z.R0,Y.R0,B.R0,A.R2,Z.L1,
    Y_prev.L3,B_prev.L3,A.L3,Z.R2,Y.L1,
    fuel_odd.L,fuel_even.L,Z.L3,Y.R2,B.L1,
    A_next.R0,right_even.R0,right_odd.R0,B.R2.

The next event is A_next.L1. In particular Z.L1 and the next three
L3 reads are a literal LLLL cleanup square. This control connects their
rank histories, not merely independently completable helper words.
A second four-L loop consumes the two explicit prepared fuel cells.
Neither cleanup is a proof of permanent fuel loss for a general front.

## Exact finite fuel controls and stopping defect

For any integer n>=1, use black seed

    {(1,0),(0,-1),(1,-1)} union {(-1,y):0<=y<2n},

all other cells white. The three first cells are finite head helpers;
the other2n are the named fuel rail. Starting at(1,0),N, the ant executes
W20^n exactly and reaches(1,2n),N. Its exact black output is

    {(1,2n),(0,2n-1),(1,2n-1)} union {(2,y):1<=y<=2n}.

Thus2n+3 black cells remain: the head helper pattern is translated and
the consumed LEFT rail has transferred to the RIGHT rail. Direct replay
checks n=1,2,3,10,100, up to2000 reads. On attempting the next stage the
first failure is offset11 at(-1,2n+1): expected prepared L but actual R.

The executable bent_pipeline_W20_controls.py/json records all complete
profiles, physical streams, exact finite seeds and failures. This is a
valid positive local/finite control, not a sustainable white front,
nonstandard finite-seed highway, external RIGHT-to-LEFT interface, or
proof that K=1 is globally realizable. A global exclusion must address
these named black suppliers rather than rejecting the connected old-L3
cleanup mechanism itself.
