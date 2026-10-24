# Controlled half-strip growth and exact autonomization

22 October 2026. Status: fixed-port gluing, periodic-port gluing, and the exact odd-port-period classification passed independent analytic audit. These are conditional reductions. No infinite safe builder has been constructed.

## 1. Model and the distinction between control and autonomy

The right domain is x>=0. Its field is initially a finite set C of black cells in that domain. A controlled excursion begins at (0,r),E, reads and updates only right-domain cells, and ends immediately upon the first left exit, at (-1,s),W. The exit cell is NOT yet read. An external reset can choose the next entry row; the reset is not itself a legal ant move and must not be silently treated as an autonomous device.

A safe half-strip excursion additionally stays within a fixed finite interval of rows. For a fixed pose sector, the audited driven-block binary rank makes every finite-width graph of complete safe left-to-left excursions acyclic. A bounded static controller region therefore cannot itself supply infinitely many such excursions. Another growing region, or a different exact physical interface, is needed.

The following gluing constructions supply that second region by a half-turn copy when the ports match. They require no extra static endcap.

## 2. Fixed-port half-turn gluing

Suppose there is a sequence of finite fields C_0,C_1,... in the right domain such that, for fixed rows r,s, the actual ant from (C_j,(0,r),E) has a finite first-left-exit excursion ending at (C_(j+1),(-1,s),W), for EVERY j>=0. Each excursion reads only x>=0. No assumption that the fields repeat or have bounded size is made.

Define the half-turn

    T(x,y)=(-1-x,r+s-y),

with heading rotated by180 degrees. It maps the right domain to the disjoint left domain x<=-1, maps the entry pose to the exit pose, and maps the exit pose back to the entry pose. A half-turn preserves the R-white/L-black dynamics; it is not a reflection and requires no color complement.

Start the autonomous ant at (0,r),E with the finite black set

    C_0 union T(C_0).

Inductively, at the start of paired round j the right field is C_j and the left field is T(C_j). The right excursion updates only the right field, producing C_(j+1), and reaches the exact entry pose of the rotated left excursion. That left excursion updates only the left field to T(C_(j+1)) and returns to (0,r),E. This proves the induction for every j.

The autonomous trajectory visits the SAME cut pose infinitely often. Any genuine eventually periodic ant tail has nonzero translation drift, so it cannot revisit a bounded set infinitely often. The constructed finite-seed orbit would therefore be genuinely nonperiodic, not merely a nonstandard periodic highway. If the right excursions have a fixed row bound, the combined trajectory is also confined to the union of that strip and its half-turn image, a fixed horizontal strip.

The invariant pose sector causes no hidden mismatch: an actual right excursion already forces r+s odd, and then this half-turn preserves the sector of its input/output poses.

A useful unconditional negative consequence is that such a fixed-port infinite builder C_0=empty cannot exist at ANY height. Its glued seed would be the empty board, whose exact standard104 tail is independently certified. This does not exclude eventual fixed-port behavior after a finite warm-up: the resulting nonempty C_0 would instead provide a legitimate counterexample seed if the infinite builder were proved. In fact the pristine case has a direct two-excursion obstruction, needing no asymptotic theorem: from (0,r),E the first excursion is RR, exits at row r-1, and leaves blacks (0,r),(0,r-1). After resetting to the same entry, the second excursion is LRRRRL and exits at row r+1. If a fixed-height constraint cuts off either trace earlier, safety already fails. Thus the two exit rows cannot agree.

## 3. Periodic ports and a phase-offset copy

More generally let the right process have k-periodic entry rows r_j and exit rows s_j, with finite fields C_j. An excursion maps (C_j,(0,r_j),E) to (C_(j+1),(-1,s_j),W). Let delta>=0 be a fixed phase offset, and use

    T(x,y)=(-1-x,S-y).

Initialize the autonomous right field with C_0 and left field with T(C_delta). The paired-round induction works exactly when, for every j modulo k,

    s_j = S-r_(j+delta),
    r_(j+1) = S-s_(j+delta).

After j paired rounds the fields are C_j and T(C_(j+delta)), with the head at the right phase-j entry. Thus this also constructs a genuinely nonperiodic finite-seed orbit, since the finite set of right entry poses is visited infinitely often.

A convenient sufficient condition is:

    k is odd,
    2delta = 1 modulo k,
    s_j = S-r_(j+delta) for every j.

The second port equation then follows by applying the first at j+delta. These sufficient congruences are not necessary if the port words have a smaller actual period. Finite warm-up and eventual port periodicity can be absorbed by choosing a later C_0. The field C_delta is finite because it is reached after only finitely many finite excursions.

### 3.1. Exact odd-period restriction for a single shifted copy

The phase equations also give a necessary condition. Eliminating s yields

    r_(j+1)=r_(j+2delta).

If the entry sequence is periodic with minimal period d, then d divides 2delta-1, hence d is odd. The first equation makes the exit sequence have the same minimal period d. Consequently the minimal period of the PAIR of port sequences is odd, and, modulo d, delta=(d+1)/2. Conversely, those conditions and s_j=S-r_(j+delta) suffice. This completely classifies periodic port words for this single-half-turn, constant-phase-offset gluing.

In particular, a genuine two-row alternating entry word cannot self-glue this way, regardless of the exit rows. A two-mode internal process with one fixed entry row can self-glue only if its exit row is also fixed. This is not a no-builder result and does not exclude gluing two genuinely different complementary builders.

Even without assuming periodic ports in advance, the same equations force an eventual odd period: for delta>=1, r_(j+2delta-1)=r_j for all j>=1, with at most the initial entry exceptional. For delta=0 the entry and exit ports are constant. Thus this particular self-gluing always gives infinitely many returns to a finite set of poses.

## 4. What all-width reachability does and does not imply

For fixed height and sector, consider the finitely branching tree of safe controlled MICROSTEP histories, allowing a finite choice of entry row at each left-boundary reset. A finite right boundary can be checked by complete finite-state closure. Reachability of arbitrarily large widths is equivalent to this tree having arbitrarily long histories, and hence to an infinite safe history by finite branching. The driven-block rank and finite-domain escape ensure that any such infinite history penetrates unboundedly far to the right: it cannot remain in a fixed finite block.

This compactness conclusion does NOT guarantee a finite-state, periodic, or even computable controller. That failure is a general logical limitation, not a demonstrated pathology of this ant. For example, a computable binary tree can require its e-th path bit to differ from program e's output on e whenever that computation halts with a bit. A finite string of length n is admitted when it obeys all such requirements discovered within n steps. The tree is computable, prefix closed, and has nodes of every length, but no infinite computable path.

Thus an exact regenerative builder is substantially stronger than observing safe reachability at every tested width. An autonomously realizable builder is stronger again, unless the port gluing equations above already apply.

## 5. Exact certificate target

A tractable candidate is a family consisting of a fixed left cap, n copies of a rail word, and a fixed moving front cap. Supply a counted excursion word taking C_n to C_(n+1), along with an eventual periodic port sequence. In event coordinates (n, segment, within-segment index), affine positions and lexicographic chronology are Presburger or automatic even when physical time is quadratic in n.

The ordered-event inverse framework validates the entire controlled history by requiring correct interior unit moves, opposite consecutive reads at each interior cell, and first-read bits equal to the supplied initial field. For a pristine right domain, every first interior read must be R. Boundary resets are explicit controller transitions, not ant updates. If those exact tests pass and the port equations match, Sections2 or3 turn the certificate into a finite autonomous counterexample. No such certificate currently exists.

## 6. Column-charge obstruction to a growing single rail

Status: direct application of the established row/column parity invariant, independently audited in this controller setting.

For each physical column x define

    Q_x = (# black cells in column x mod2)
          XOR 1[the ant is vertical and is currently in column x].

Every ordinary ant step preserves Q_x for every x. If the incoming heading is vertical, the flip and removal of the vertical-head indicator cancel in the read column. If it is horizontal, the flip and addition of that indicator cancel there. No other column changes its charge.

Both boundary poses of a complete right excursion are horizontal. Therefore the parity of the black population of EACH right-domain column is unchanged by the excursion. The external reset also has horizontal heading on both ends and does not change the field, so it preserves these column parities. This conclusion does not require fixed entry/exit rows or a row-height bound.

Consequently, from any finite initial field C_0, every column beyond its support has EVEN black occupancy at every completed-excursion checkpoint. A regenerative family with a longer and longer SINGLE solid black rail, bounded fixed/moving endcaps, and no other persistent column content is impossible: eventually some new far column lies in the rail bulk and has one black cell, contradicting its conserved even parity.

More generally, every column of a purely periodic growing bulk word must have even black weight, unless an additional wake or second rail supplies its odd-parity compensation. A bounded moving cap cannot compensate for infinitely many settled bulk columns. This is not an exclusion of rail builders with debris; it is an exact design requirement for their full fields.


### 6.1. Stronger alternating column charge modulo4

Status: independently derived here from the existing modular row-charge invariant; the displayed potential passed independent analytic review.

For every physical column j, write C_j=sum_y (-1)^y b(j,y). A complete right-half-plane excursion preserves C_j modulo4, not merely its parity. This holds independently of the chosen entry/exit rows, and therefore also across arbitrary externally selected horizontal resets.

Here is a direct verification. Fix the invariant pose sector sigma=(x+y+h) mod2, headings N,E,S,W=0,1,2,3, and let c=(-1)^(sigma+j). Define the head potential

    f_j(x,h)=c[-2*1[x>j]+(h-1)*1[x=j]] modulo4.

For a turn epsilon=+1 on white or -1 on black, the column charge change is

    Delta C_j=1[x=j] c (-1)^h epsilon.

Checking the eight heading/turn cases, including the resulting horizontal move, gives Delta f_j=-Delta C_j modulo4. Thus C_j+f_j is invariant. At a right entry(0,r,E) and first left exit(-1,s,W), f_j=0 for every j>=0. Hence C_j is unchanged. Although sigma depends on the entry row, these two zero boundary potentials do not, so changing the externally chosen row does not spoil the conclusion.

All newly built far columns must therefore have alternating black charge0 modulo4 at completed-excursion checkpoints. Two compensating solid rails need opposite row parities; two rails on the same parity still fail despite even occupancy. Four same-parity rails pass this necessary charge test. Additional wake can compensate, but it must be included in the full field certificate.

## Three-phase two-column growth: a stronger signed-row filter

22 October2026. Independently cross-checked with the causal analysis using its
signed-row invariant; no builder is constructed.

For entry rows r=(0,2,4), choose half-turn offset delta=2 and constant S=5.
The gluing equations force exit rows s=(1,5,3). Over those three complete
right-half-plane excursions, the row-wise alternating black charge

    C_y = sum_x (-1)^x * black(x,y)

changes modulo4 by

    Delta_y=2(#{j:r_j>y}-#{j:s_j>y})
            +#{j:r_j=y}-#{j:s_j=y}.

This is -1 on EVERY row0..5, and zero on every other row. It follows directly
from the pose-corrected invariant: at entry(0,r,E) the correction is
2A(r)+a(r), and at exit(-1,s,W) it is2A(s)+a(s), for arbitrary row weight a.

Suppose a putative same-phase renewal restores its finite left fringe,
translates an identical right cap by TWO columns, and inserts two bulk
columns supported on rows0..5. Translation by2 preserves the cap's signed
row charges, so the new bulk alone must supply the displayed increment.
Parity already says the two column masks are complements P and1-P. At
columns L,L+1 their contribution is(-1)^L(2P_y-1). To equal-1 modulo4 for
every row, P_y must be the SAME bit for every y:

    every even new column is empty;
    every odd new column is black on all six rows.

Thus arbitrary balanced complementary masks are not candidates for this
precise two-column renewal. The individual column alternating vertical
charges vanish for the full six-cell column, so the stronger necessary
condition is consistent. Fixed caps of total height<=9 remain independently
excluded by the pristine-barrier theorem; a taller moving cap is not excluded
by this calculation. No finite or infinite regenerative circuit is supplied.
