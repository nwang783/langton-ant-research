# Exact multiplicity profiles of a lowest axis-four row

23 October 2026, 05:55 UTC. Independently signed elementary all-cap count lemma.

Let a complete white translating front have actual full horizontal drift
(plus or minus 4,0). Choose its lowest active row and the checker sector
so A_i=(2i,0) has vertical departures and B_i=(2i+1,0) horizontal departures,
with i modulo2. Let a_i,b_i be the COMPLETE read counts, allowing zero for
unread classes. All departures from A_i are N; all arrivals at B_i are S.
White alternation therefore fixes the bottom words:

    A_i arrivals W,E,W,E,... ; B_i arrivals S,S,S,S,... .

The exact neighboring horizontal edge counts are

    ceil(a_i/2)=ceil(b_i/2),
    floor(a_i/2)=floor(b_(i-1)/2).                 (1)

These equations do not depend on the sign of the actual drift. They use
no chronological clock or primitive quotient.

Write b_i=2u_i+e_i and a_i=2v_i+f_i, with e_i,f_i in{0,1}. Then

    v_i=u_(i-1),
    u_i-u_(i-1)=f_i-e_i.                         (2)

For two pairs, (2) completely classifies the profiles, up to shifting i
cyclically:

    (a0,b0,a1,b1)=(m,m,m,m), m>=1;
    (a0,b0,a1,b1)=(2u,2u,2u+1,2u+1), u>=0;
    (a0,b0,a1,b1)=(2u+1,2u+2,2u+2,2u+1), u>=0.

Indeed if u0=u1=u, then f_i=e_i and each A_i/B_i pair has length2u or
2u+1. This gives the constant profiles and the second family. If the two
u values differ, (2) forces their difference to be one, the entering bit
pair(f,e)=(1,0), and the leaving pair(0,1), giving the third family.
No other case is possible.

Thus every read count on the lowest row is either m or m+1, and any
nonconstant profile has precisely ONE adjacent high-count pair. If m is
even this high pair starts at an A cell; if m is odd it starts at a B
cell. The exceptional m=0 case consists of exactly two singleton cells
and two empty classes. The all-zero row is excluded by its choice as
active.

This reduces an all-cap axis-four boundary analysis to a common count m
plus one of three exact profile types. It does not bound m, force a fully
singleton boundary, control higher rows, or exclude full axis-four fronts.
Genuine rotations transport the complete statement; reflection is unused.

For general full horizontal drift(plus or minus2K,0), the same formulas
(1),(2) hold with i moduloK. In particular the floor counts u_i form an
integer nearest-neighbor cycle with increments in{-1,0,1}. No stronger
range or chronology statement is asserted here.
