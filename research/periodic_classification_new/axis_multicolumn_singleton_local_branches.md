# Exact local branches above a uniform singleton axis boundary

23 October 2026, 05:42 UTC. Independently signed all-cap necessary condition
(analytic review completed 05:47 UTC). This note does NOT assert that the lowest row
of a general axis-four front must be singleton.

Let the actual full drift be d=(-2K,0), K>=2. Suppose every cell of the
lowest active row has exactly one complete read. Choose representatives
A_i=(2i,0), B_i=(2i+1,0), C_i=(2i,1), D_i=(2i+1,1), i modulo K.
A_i and D_i have vertical departures. All bottom reads are white R.
The unique lower path associated with each D_i is

    D_i(q_i) --S--> B_i(0) --W--> A_i(0) --N--> C_i(p_i).

Here p_i is C_i's sole incoming-N rank and q_i is D_i's sole outgoing-S
rank. Consequently c_i(p_i)=d_i(q_i)+3. Every other C_i arrival is S;
every other D_i departure is N. Local ranks are zero-based.

The precise necessary alternatives in EACH column are

    q_i odd:  p_i=q_i;
    q_i even: p_i=q_i+2.

No cap is imposed on any history length or on upper rows. In particular,
asserting that all the marks must be odd would be unjustified.

## Proof of the two alternatives

On both C_i and D_i the E-port bit is "marked XOR odd rank". Its count
before rank r is floor(r/2), plus +1 if the unique earlier mark is even,
or -1 if it is odd. The entire E-edge multiset stays within the same i:
E from C_i goes to D_i with zero seam. These occurrences match by ordinal.
Every two distinct visits to the same physical cell are at least four
steps apart: the walk alternates horizontal and vertical axes, so a
positive return has length divisible by four.

If q_i is even, its E source is C_i(k). This source followed by S,W,N
first-returns physically to C_i in four steps, hence p_i=k+1. The source
is before the unique mark and is therefore an unmarked odd E rank.
Matching E ordinals gives (k-1)/2=q_i/2, hence p_i=q_i+2 is even.

If q_i is odd and p_i were even, the lower S,W,N path followed by the
E departure from C_i(p_i) first-returns to D_i. Its endpoint must be
rank q_i+1, which is even and arrives E. It would turn R to S, producing
a second downward mark. Thus q_i and p_i are both odd.

Suppose these odd marks satisfy p_i<q_i. Then E ordinal matching sends
C_i(p_i+2) to D_i(p_i). But the source occurs after C_i(p_i), which is
three steps after D_i(q_i), while the target occurs before D_i(q_i).
This contradicts the edge clock d_target=c_source+1.

Suppose instead p_i>q_i. E ordinal matching sends C_i(q_i) to D_i(q_i+2).
Because q_i<p_i at the same C_i cell,

    c_i(q_i) <= c_i(p_i)-4 = d_i(q_i)-1.

The E clock would give d_i(q_i+2)<=d_i(q_i), a contradiction. Therefore
p_i=q_i. All invoked E ranks exist: equality of full E counts gives equal
floors of the two column history lengths in these equal-parity branches.

The four-step paths are proper. At least one event occurs in each of the
4K named classes, so P>=4K>=8. Their literal compass traces have no earlier
physical return, so the consecutive-rank rule applies.

## The downward mark cannot be constant around the entire boundary

Assume q_i=h for every i. The alternatives above also fix every p_i.

If h is odd, all p_i=h. The marked W departure at C_i(h) matches the
marked W arrival at D_(i-1)(h), since their W ordinals are both (h+1)/2.
Together with the K lower paths, these form a closed successor cycle of
length 4K and voltage one around the full-drift cylinder. A complete front
has only one successor cycle, so P would equal 4K. But the bottom already
has 2K events and each upper cell has at least h+1>=2 events, giving
P>=6K. Contradiction.

If h is even, p_i=h+2. The E source of D_i(h) is C_i(h+1), so
c_i(h+1)=d_i(h)-1 and c_i(h)<=d_i(h)-5. The W departure at C_i(h) has
ordinal h/2; on D_(i-1), whose unique removed W port is h, its target is
rank h+2. Let s_i=1 for i=0 and 0 otherwise, the negative-drift W seam.
Then

    d_(i-1)(h+2)=c_i(h)+1-s_i*P <= d_i(h)-4-s_i*P.

In particular d_(i-1)(h)<d_i(h)-4-s_i*P. Summing over i contradicts
0<-4K-P. Thus the q_i cannot all be equal, even when the upper complete
history lengths differ. This is local boundary symmetry breaking, not a
universal reduction to a smaller supplied full drift.

## Scope

For K=2 this says that, CONDITIONAL on a fully singleton lowest row, the
two downward marks are distinct, and each column has exactly the branch
above. It does not classify non-singleton lowest rows, bound either mark,
bound higher histories, or exclude full drift (-4,0). Genuine rotations
may transport the whole statement; reflection is not used.
