# Minimal ordered cut transport can carry maximum residual-defect density

23 October 2026. Exact scoped obstruction. The universal finite-seed standard104
conjecture remains open. This note does not construct an infinite finite-seed
ant and does not rule out a mass-sensitive ordering/freshness theorem.

## Result in one paragraph

There is an infinite-support ordinary ant whose live cursor crosses every
axial cut monotonically, whose exact initial alternating row and column sums
are all zero, and whose support change attains every heading-corrected axial
lower bound on every finite interval. Nevertheless every available ten-window
is forbidden and every available eleven-window is a residual UNION6 event.
This is not merely a teleporting-face schedule: every ant update and the
single connected cursor are literal. The missing hypothesis is finite initial
black information. Explicit nested positive binary finite-height seed
completions realize arbitrarily long prefixes of the same history. Therefore
neither charge-minimality, absence of recrossings, their combination, nor an
initial charge vector equal to the blank board can, without a finite-fuel
term, distinguish standard from nonstandard transport.

## 1. Conventions

White reads R, black reads L, the read cell flips, then the ant moves.
Headings N,E,S,W are 0,1,2,3. Begin at (0,0),N, so the sector is sigma=1.
Put

    epsilon(x,y)=-(-1)^(x+y),
    rho(B)(x,y)=epsilon(x,y)*1_B(x,y),
    Delta H(x,y)=H(x,y)-H(x-1,y)-H(x,y-1)+H(x-1,y-1),
    mu(p,h)=p-d_h/2.

The sign convention is that of live_cursor_transport_debt.md. It differs
from the sigma=-1 example in unit_height_bounded_mass_obstruction.md.

## 2. An exact infinite-support live ant

Define

    B_infty={(n+1,n),(n+2,n): n in Z}.

Each individual row and column contains exactly two adjacent black cells.
Consequently all exact alternating row sums S_r and column sums T_c vanish.
These sums are finite on each line, even though total black mass is infinite.
Also

    rho(B_infty)=Delta H_infty,
    H_infty(x,y)=1{x-y<=1}.

Indeed, for k=x-y, Delta H=2f(k)-f(k-1)-f(k+1), which is +1 at k=1,
-1 at k=2, and zero elsewhere. Those signs equal epsilon at the stated
black cells. This is a positive binary height, not a finite-support height.

The literal forward orbit reads

    (RL)^infty,
    p_t=(ceil(t/2),floor(t/2)),
    h_t=N for even t, E for odd t.

Proof: at read 2n, (n,n) is an initially white, previously unread cell;
R moves to (n+1,n). That cell is initially black and previously unread;
L moves to (n+1,n+1),N. This proves the induction for all n>=0.
No site is reread. Head coordinates are nondecreasing. Every horizontal
or vertical line is touched in one contiguous passage and never returned to;
every crossed half-integer axial cut is crossed exactly once.

The exact charge proof uses only a finite change on each individual line,
so all correction-table invariants apply unchanged to this locally finite
infinite board. This extension does not extend any finite-mass theorem.

## 3. The strongest transport-debt inequalities are saturated

At every time

    mu_t=(t/2,(t-1)/2).

For any integers 0<=s<t, precisely the distinct read cells with indices
s,...,t-1 change. Hence

    |B_s symmetric_difference B_t|=t-s
       =2*||mu_t-mu_s||_infinity.                 (1)

This is exact equality, not merely the correct asymptotic rate.
For each individual row and column the heading-corrected discrepancy bound
is also equality:

    |(B_s triangle B_t) intersect row r|
        =delta4(G_r(p_t,h_t)-G_r(p_s,h_s)),
    |(B_s triangle B_t) intersect col c|
        =delta4(F_c(p_t,h_t)-F_c(p_s,h_s)).        (2)

One way to prove (2) is to sum the exact correction lower bounds using the
retained sharp midpoint formula. The row sum and the column sum are both
t-s, including when an endpoint coordinate is equal: then the heading
changes once and its circular distance is one. The actual discrepancies
also sum to t-s. Since every individual inequality is valid and has
nonnegative slack, every slack must be zero.

Thus no excess support above unavoidable ordered transport exists on ANY
subinterval. In particular, summing interval slacks or charging returns
cannot pay for the following defects.

## 4. Residual defects have maximal density

Let F be the 84 cyclic standard104 ten-factors. Direct membership in this
fixed finite set gives

    RLRLRLRLRL not in F,
    LRLRLRLRLR not in F.

Every complete ten-window is therefore bad. Every complete eleven-window
is an adjacent-bad event K, labelled RLRLRLRLRLR or LRLRLRLRLRL. Neither
belongs to the signed six-label union. A length-T prefix consequently has
exactly max(0,T-10) residual events with full eleven-windows in the prefix.
The infinite-support history has residual-event density one.

This disproves the specific implications

- minimum possible distributed transport debt => standard transport;
- no axial recrossings => finitely many residual events;
- these two properties plus exact zero initial line margins => capture,

when finite initial information is omitted. It is not a counterexample to
any of these statements with the ordinary finite-support hypothesis retained.

## 5. Explicit positive finite completions

For every integer K>=0 put

    A=-2K-1, B=2K+1, C=-2K-2,
    H_K(x,y)=1{A<=y<=B and C<=x<=y+1}.

These finite nonnegative binary heights are nested: H_K<=H_(K+1).
Their mixed differences are binary ant boards under rho=epsilon*1_B.
The complete black support is

    {(C,A),(A+2,A),(C,B+1),(B+2,B+1)}
      union {(n+1,n),(n+2,n): A+1<=n<=B}.        (3)

The first and fourth cap cells have rho=+1; the second and third have
rho=-1. The interior diagonal cells have signs +1 and -1 respectively.
All corner sites are distinct, so

    |B_K|=8K+8.

Because H_K is finite, every exact alternating row and column sum of B_K
is zero, not just zero modulo four. Formula (3) also verifies this directly.
The height supports exhaust {x-y<=1}; the boards converge locally to B_infty.

From (0,0),N, B_K executes (RL)^(2K+3), exactly 4K+6 turns. For n=0,...,B,
the required black cell (n+1,n) lies in the diagonal portion of (3). The
last required black cell at n=B+1 is the top-right cap (B+2,B+1). All
required diagonal white cells are absent from (3), and no path site repeats.
This is the full induction, independent of any simulation horizon.

Every subinterval of this guaranteed prefix satisfies (1) and (2), and it
contains max(0,4K-4) residual UNION6 events. Hence arbitrarily long
physically exact FINITE-SEED factors can have maximum defect density,
perfect cut order, and zero transport slack. Any bound on residual count
solely in terms of recrossing count, transport slack, and initial line-charge
vector, independent of initial fuel, is false even for finite seeds.
A bound with a term depending on initial mass or first-L demand survives.
No statement is made about B_K's actual continuation after the guaranteed
prefix, nor about eventual capture of this family.

## 6. A general margin-completion lemma

Let w be any finite physically consistent ant turn word, with visited set V.
Let Q subset V be the sites whose FIRST read in w is L. The necessary seed
bits on V are exactly 1_Q. There is a finite board B* satisfying

    B* intersect V=Q,
    all exact alternating row and column sums of B* are zero,
    |B*|=4|Q|.

Thus w is unchanged, and every initial line charge equals that of the
blank board at the same head pose.

Construction: for each q_i=(x_i,y_i) in Q, choose distinct far-right X_i
and far-above Y_i, outside the visited bounding box, with X_i-x_i and
Y_i-y_i both positive odd. Make the four corners

    (x_i,y_i),(X_i,y_i),(x_i,Y_i),(X_i,Y_i)

black. Choose all X_i distinct and all Y_i distinct. Corner sets are
pairwise disjoint; three added corners per source avoid V. Each pair
in every occupied row and column has opposite parity and cancels exactly.
The union therefore has the required zero margins. It realizes w because
first-read bits agree and repeated reads alternate by physical consistency.

Equivalently rho(B*) is the mixed difference of the sum of rectangle
indicators weighted by epsilon(x_i,y_i). This general completion height is
an integer signed field; nonnegativity is NOT asserted here. The staircase
family in Section 5 separately supplies genuinely nonnegative binary heights.

This lemma is about finite prefixes. It does not preserve an entire infinite
orbit, since that orbit might eventually visit added companion cells.

## 7. What an ordering bridge must still retain

The infinite staircase uses one new initial black cell per L. Its first-L
count is infinite. The finite B_K prefix uses 2K+3 distinct initial black
cells, so its growing defect count is paid by growing initial information.
There is no violation of finite fuel, and the sharp transport debt is not
that fuel count.

For any physically consistent infinite word, a uniform bound m on the total
number of first-read L sites gives a finite realizing seed of size at most m:
make exactly those first-L sites black. Conversely a finite seed of mass m
permits at most m such sites. This is the exact compactness distinction that
the shared zero line-charge vector loses. The unbounded masses 8K+8 prevent
applying bounded-first-L compactness to the finite completions above.

Accordingly a viable residual-defect ordering theorem must retain a bounded
initial-information budget or a non-reuse/ancestry statement that charges
residuals to that budget. Ordering the compulsory axial residues, even with
all interval bounds sharp and no returns, does not itself provide it.
This does not rule out a theorem that combines such ordering with a genuine
finite-fuel or causal-reuse argument, nor does it provide that missing theorem.

## Controls and audit status

check_cut_order_staircase.py independently implements ordinary ant updates,
finite mixed differences, exact margins, both correction tables, and the
fixed standard-factor membership test. The recorded controls pass 24 finite
seeds, 1,248 literal staircase updates, 49,904 sharp per-line endpoint tests,
1,012 residual windows, and 10 arbitrary-prefix margin completions.
Finite controls support the explicit all-parameter inductions; they are not
the proof of any infinite finite-seed claim. Independent review requested.
