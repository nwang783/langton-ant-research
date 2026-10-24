# An optimal finite zero-margin staircase prefix

23 October 2026. Companion refinement of cut_order_minimal_transport_obstruction.md.
No eventual-tail or infinite finite-seed claim is made.

For every even integer N>=4 there is a finite seed of black mass exactly 2N,
with ALL exact alternating row and column sums zero, which from (0,0),N
executes (RL)^N. Its seed is the binary mixed difference of a nonnegative
binary finite height. The mass 2N is optimal among zero-row-margin seeds
realizing this exact prefix.

Use the same sigma=1 conventions, epsilon=-(-1)^(x+y), and Delta as in the
companion note. Put

    H^(N)(x,y)=1{0<=y<=N-2 and 1<=x<=y+1}.

Direct mixed differentiation gives the complete black support

    B^(N)={(n+1,n): 0<=n<=N-1}
          union {(n+2,n): 0<=n<=N-2}
          union {(1,N-1)}.                         (1)

Every listed point is distinct. The first diagonal has rho=+1. The second
has rho=-1, as does (1,N-1) because N is even. There are N+(N-1)+1=2N black
cells. This proves binary validity and rho(B)=Delta H. Finiteness of H implies
all exact alternating row and column margins vanish. Directly, each row has
two black cells of opposite x parity; every occupied column has two black
cells of opposite y parity. In the final row the pair is (1,N-1),(N,N-1),
whose x parities differ because N is even.

All (n,n), 0<=n<N, are initially white. The only potential cap collision
would be (1,N-1)=(n,n), which would require N=2; that is why N>=4 is imposed.
All (n+1,n), 0<=n<N, are black. These 2N read cells are distinct, so induction
proves the exact (RL)^N prefix. As in the companion note, every sharp axial
and midpoint bound is saturated on every subinterval, and every complete
eleven-window is a residual UNION6 event. There are max(0,2N-10) such events.

For optimality, in any seed realizing (RL)^N, each (n+1,n) is a distinct
first-read black cell. If the exact alternating sum in row n is zero, this
row must contain at least one further black cell, since a single black cell
has signed weight +1 or -1, not zero. The N distinct rows therefore contain
at least 2N initial black cells. Construction (1) attains this lower bound.
This optimality is for the exact prefix and zero row margins, not for general
residual events or for all N. Neither an odd-N optimum nor actual eventual
capture of this family is asserted.

The finite heights H^(N) are nested over even N but their limit is only a
one-sided wedge. A cap escapes to infinity in column 1, so the limit does
NOT preserve every initial zero column sum. Use the symmetric family in the
companion note when a locally finite infinite limit with all zero line sums
is required. This distinction avoids an illegitimate interchange of a
local limit and an infinite line sum.
