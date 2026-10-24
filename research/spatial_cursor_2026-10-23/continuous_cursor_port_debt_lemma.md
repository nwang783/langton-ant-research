# An exact changed-support decomposition with continuous-cursor port debt

23 October 2026, 17:59 UTC. A proved accounting lemma, not a bound on the debt
and not a global capture theorem. No bounded-discrepancy or finite-memory
assumption is made.

## 1. Statement for an arbitrary actual finite interval

Let an actual Langton-ant interval have duration T, actual endpoint boards
B_s,B_t, complete XOR E, and finite READ set W. An arbitrary common infinite
background is allowed. Partition W into finite regions V_i. Assign one
integer clock center c_i to each region. Use either strict Ke clock:

    z=x+y or z=x-y,
    f(a)=3^|a|-1,
    J_c(p,h)=J(z(p)-c,epsilon_z(h)).

Here J(a,e)=f(a)/2 when e*a>=0, and -3*f(a)/2 otherwise. For x+y,
epsilon_z(N)=epsilon_z(E)=+1 and epsilon_z(S)=epsilon_z(W)=-1;
for x-y, epsilon_z(E)=epsilon_z(S)=+1 and the other two are -1.
Let sigma_z be the corresponding retained clock's sector sign. Define

    F_i(B)=-sigma_z sum_{q in V_i} (-1)^(q_x+q_y) f(z(q)-c_i) 1_B(q),

and the ACTUAL cursor port debt

    P=sum over fine reads r=s,...,t-1 of
        [ J_(c_i)(p_(r+1),h_(r+1))-J_(c_i)(p_r,h_r) ],

where i is the unique region containing the read cell p_r. Then

    T <= sum_i [F_i(B_t)-F_i(B_s)] + P.                   (1)

No equality of endpoint poses is required. Every term is finite. The fields
outside W are kept physically; they cancel and are never assigned divergent
infinite clock sums.

## 2. Proof

For each ACTUAL fine step r, apply the known strict-clock one-step inequality
with center c_i belonging to that step's read region. Only the read cell
changes color, so the full clock's field change is exactly the change of
F_i on this step. Its head change is the displayed J difference. Thus each
fine step contributes at least one. Sum over all actual fine steps.

For a fixed region, F_i changes only on its own selected steps, so its field
changes telescope even if the region is revisited many times. This proves
(1). The head terms do NOT telescope over separated region visits because
the same physical cursor leaves for other regions in between.

Equivalently, group the interval into maximal consecutive temporal streaks
of read cells in a common region. On a streak [a,b), the head contribution is
EXACTLY

    J_(c_i)(p_b,h_b)-J_(c_i)(p_a,h_a).

So P can be recorded by actual entry and exit ports, including heading.
The boundary endpoint (p_b,h_b) need not lie in region V_i. No teleportation,
reset, or independent replacement of that endpoint is permitted.

## 3. Specialization to complete-XOR components plus restored travel

Let C_1,...,C_k be ANY partition of E, in particular its actual even-dual
edge components. Take V_i=C_i and V_0=W\E, the complete restored-read set.
Choose c_i minimizing

    A_z(C_i)=min_c sum_{q in C_i} f(z(q)-c)

for every i>=1; choose ANY c_0 for restored reads. Since V_0 has identical
endpoint colors, F_0(B_t)-F_0(B_s)=0 exactly. Every other field increment
is at most A_z(C_i). Therefore

    T <= sum_(i=1)^k A_z(C_i) + P.                       (2)

This is the honest replacement for the FALSE debt-free component bound.
It retains ALL actual travel via P, including twice-read bridge edges that
disappear from final XOR. P may have either sign; using max(0,P) gives a
weaker nonnegative-debt bound. No upper bound on P is claimed.

The partition is an ex-post analysis of one actual finite interval; it is
not asserted to be a forward-computable state invariant or a well-founded
rank. Making such regions change online needs additional merger/split and
center-change accounting, not free redefinitions.

## 4. Exact tight actual countercontrol

In the ACTUAL blank-ant interval ticks9 through17, word LRRRRLLL and identical
endpoint pose(-1,0,W), use

    Cleft ={(-2,-1),(-2,0)},  center c_left=-2,
    Cright={(0,-1),(0,0)},    center c_right=-1,
    V0={(-1,-1),(-1,0)},      center c_0=-2,

with z=x+y. The two local optimized norms are both2. Their signed field
increments are also2 each; the restored field increment is zero. The eight
successive ACTUAL head increments are

    3, 1, -1, 1, -1, 1, 1, -1,

which sum to P=4. Thus (1) and (2) are TIGHT:

    8 = (2+2+0) + 4.

The four missing units are not an abstract overhead. They are exactly the
continuous-cursor port correction needed when switching between the two net
support components across restored edges. The physical trace, complete board,
dual endpoints and component norm computations are frozen separately in
causal_component_decomposition_countercontrol.md and its literal checker.

## 5. The maximally local center rule puts ALL time into port debt

There is an exact calibration showing why an adaptive center is not free.
Partition W into one-cell regions {q} and choose c_q=z(q). Then f(0)=0,
so EVERY region field term F_q is identically zero, on every board.
On an actual read at q, its entry head has z(p)-c_q=0 and J=0. The next
head has z(p_next)-c_q=+1 or -1. The rotated sign epsilon_z(h_next) is
EXACTLY that signed z displacement, so its product with the new argument is
positive and J=f(1)/2=1. Thus every fine read contributes exactly ONE to P:

    sum_i Delta F_i = 0,       P=T.

The accounting lemma becomes the equality T=T on EVERY actual trajectory,
including an ordinary standard highway and every nonstandard excursion.
This is not a relaxation or constructed endpoint chain. It is a literal
continuous-cursor identity. A local/adaptive-center scheme can make its
field potential vanish only by placing the entire elapsed-time bill in
the port correction. A useful global proof must independently bound or
amortize that correction rather than relabel it as a bounded cap.

## 6. Precise remaining global obligation

The lemma supplies a correct spatial/cursor-sensitive decomposition on ANY
actual finite interval, even without a bounded complete discrepancy. It does
not establish the independent amortized bound needed for global capture.
A useful new theorem would have to pay the accumulated positive port debt
from initial geometry, actual causal creation/retirement, or another finite
resource, while separately handling arbitrarily long zero-defect standard
flights. Merely counting regions, roots, direct producers, or active core
ports does not bound P.

The signed active-star representation ensures the full read-edge graph is
connected. The actual eight-read control shows its net-support components
can nevertheless exchange clock credit through restored travel. This is why
a valid causal ledger needs temporal entry/exit information rather than
only the final graph partition.
