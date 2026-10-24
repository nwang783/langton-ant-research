# Quadratically many residual windows reuse only linearly many root pairs

23 October 2026. Exact all-parameter colored-genealogy extraction from the
already audited finite inward spiral. This is an obstruction to a specified
initial-root pair budget, not to every possible interaction invariant or to
an O(m^2) universal defect bound.

Inherited geometry and feasible word W_n are those in
../../core_periodicity_new/quadratic_inward_spiral.md. Its first-L seed has
mass 11n+2. Use passive physical token-root labels as in
../../causal_reduction/root_reactivation.md: every initial black cell has
its own coordinate label; R writes receive the active cursor label; an L
consumption supplies the active label for the NEXT read. These labels are
exact genealogy, not independent information bits or counterfactual causes.
Assume n>=4. Capture is inherited only for n>=11.

## 1. A fixed outer row of root identities

For s=1,...,n-1 define the distinct initial-black roots

    r_s=(-2s,2n+1).

All are initial first-L sites on circuit zero's west rail. Circuit k has
j=n-k and physical start time

    t_k=k*(16n+6)-8k*(k-1).

Its west rail starts at offset 4j+1, at position(-k-1,2n-k), heading W.
Number west-rail reads by offsets 0,1,2,... from that start.

For every k>=1, the root-owner sequence from west offset2 onward is

    r_1^4 r_2^4 ... r_(j-1)^4 r_j^3,                  (1)

through and INCLUDING offset4j, the R immediately after the west rail.
The final triple consists of the rail's last L,R and the RLL corner's R.
The two preceding west reads may have another owner and are not used.

### Proof retaining every actual owner

In circuit zero, each west-rail L site is initially black with its own root.
The R at west offset4l+3 (the last R of its lth RLLR) has root r_(l+1).
The next R, at offset4l+4 when present, has the same root: no L intervenes.

For circuit k>=1, the two L sites in its lth west RLLR coincide exactly with
those two R outputs of circuit k-1, by the signed adjacent-circuit overlap.
They therefore BOTH carry root r_(l+1). The first L hands that root to the
second L; the second L hands it to the last R and the following first R and
first L. Thus r_(l+1) owns offsets4l+2,...,4l+5 whenever those reads lie on
the rail. At its final end the RLL corner's first R has the same owner.
Induction on circuits proves (1), including all L reads BEFORE their labels
change. No stale label is carried across an intervening read.

## 2. An explicit triangular set of residual windows

For every pair of integers

    k>=1, l>=0, k+l<=n-3,

select the eleven reads at west offsets 2+4l through12+4l. Since j>=l+3,
the window is present; it may include the corner's initial R but no later
corner letter. Its exact turn word and ALL ELEVEN owners are

    LRRLLRRLLRR,
    r_(l+1)^4 r_(l+2)^4 r_(l+3)^3.                    (2)

Both overlapping ten-factors of this fixed eleven-word are absent from the
84 cyclic standard factors, and its eleven-label is outside UNION6. Every
selected right endpoint is therefore an actual residual event. All selected
endpoints are distinct. Their number is exactly

    N_sel=(n-3)(n-2)/2.                              (3)

The endpoint time and pose are explicitly

    t_k+4j+13+4l,
    (-k-2l-7,2n-k), heading W.

For fixed l, increasing k translates the ENTIRE eleven-read geometric
window by(-1,-1), without changing its turn word, its three initial-root
owners, their within-window order, or their initial relative arrangement.
There are n-l-3 exact repetitions of that same root triple interaction.

## 3. Only 2n-5 distinct co-occurring initial-root pairs

Across every selected window, the unordered pairs that co-occur are exactly

    {r_s,r_(s+1)} for 1<=s<=n-2,
    {r_s,r_(s+2)} for 1<=s<=n-3.

Every listed pair occurs because every consecutive triple
r_s,r_(s+1),r_(s+2), 1<=s<=n-3, occurs at least in circuit k=1. There are
exactly 2n-5 such pairs. If pairs are ordered by their order of occurrence
in the window, the same count holds, with the lower index always first.
The compressed three-root order is always the same increasing-index order.

Consequently ANY assignment that charges each selected event to one of
its co-occurring initial-root pairs has some pair charged at least

    ceil((n-3)(n-2)/(2*(2n-5)))                       (4)

times. This grows without bound. In particular a uniform bounded-use budget
per co-occurring pair, or a requirement of a previously unused such pair or
previously unused within-window ordering at EVERY selected residual event,
is false. The obstruction remains when all eleven owners are retained,
not just the final-read owner used by audit LE.

For example l=0 alone repeats r_1^4 r_2^4 r_3^3 in n-3 circuits. After the
first such event all three of its co-occurring pairs and their order have
already occurred; later repetitions introduce none.

## 4. What remains possible

This does not refute an O(m^2) universal residual bound: the family itself
has mass m=11n+2 and quadratic many events. Nor does it show unbounded events
at one fixed total mass. A finer interaction may retain actual token births,
packet roles, first encounters at a specified spatial separator, complete
simultaneous masks, or cleanup of sibling output identities. None is reduced
here to the coarse initial-label co-occurrence notion.

The theorem also does not prohibit charging an event to an interaction
outside its own eleven-read window, if a separate physical theorem supplies
such a charge. The precise false proposal is a bounded-use charge to one of
the initial-root pairs actually co-occurring in that event's owner window,
with at most a finite root-order refinement of the kind fixed in (2).
An arbitrary generation-sensitive definition could distinguish these repeats
and requires its own resource proof. Independent review requested.
