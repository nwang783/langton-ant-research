# Parallel selected-input transport forces inherited transverse width

23 October2026,20:12 UTC. Author causal production proof for review. This is an
explicit width-to-length bound for finite aperiodic epoch transport, not a
periodic-profile assumption or a global descending potential.

## 1. Odd output supply is the relevant parallel resource

Use the signed distinguished inputs D/DC(0,1), V/VC(1,2), and
VCC/U/UC/UCC(0,3). Their local coordinate sum is always odd:1 or3.

If source and consumer full-entry headings are parallel or antiparallel,
sector conservation makes their head coordinate sums have the same parity.
For a source output o to be consumed in a distinguished consumer slot i,

    p_source+rot_source(o)=p_consumer+rot_consumer(i).

Taking coordinate sums modulo2 therefore forces o_x+o_y to be ODD. This is
independent of longitudinal length, normal profile, or chronological distance.

The exact fresh residual output counts at odd local coordinate sum are

    D:0, DC:2,
    V:3, VC:5, VCC:6,
    U:5, UC:7, UCC:8.

Thus a long D-only source rail creates NO selected-input supply for any later
parallel/antiparallel epoch, even though it creates many physical black cells.
D outputs can still participate through perpendicular transfers or unselected
input roles; neither possibility is silently excluded.

## 2. Supply capacity of one completed source epoch

Let a be one full-entry C clock, hence one fixed-heading epoch. Let v_a and
u_a count its V-family and U-family bases. All packets other than its final
C-bearing packet are plain zero-C D/V/U. There is at most one C-bearing packet
at this clock, with one or two C tails. The full-clock/source labels are not
reset at an internal atomic installation.

Summing the literal odd output counts yields

    total odd births =3v_a+5u_a+kappa_a,

where kappa_a is0,2,or3 according as the epoch has no terminal C packet, one
C tail, or two. In particular total odd births<=3v_a+5u_a+3. Every produced
identity is consumed at most once, so this is an honest upper bound on the
number of later distinguished input uses that this cohort can supply in any
parallel consumer epoch. Already consumed IDs or incompatible lateral geometry
can only reduce usable supply.

The signed permanent U left-star theorem gives a stronger causal count: two
odd outputs from EVERY U base, at(0,1) and(1,0), can never be consumed later in
this factor. Omitting them gives usable odd births at most

    3v_a+3u_a+kappa_a <=3(v_a+u_a)+3.                     (1)

The coarser transverse-width bound below remains valid even without this
permanent-star refinement.

## 3. The capacity is paid by an actual transverse base sweep

Normalize the epoch's heading toN and set t=x-y. Before its terminal C tails,
all base steps have the exact head/center increments

    D:(1,1), V:(1,3), U:(0,4).

They change t by0,-2,-4, respectively. Hence, from the epoch's first full entry
to the atomic cut at the END of its final base and BEFORE any C tails, the
actual monotone normal drop is exactly

    W_a=2v_a+4u_a,       w_a=W_a/2=v_a+2u_a.              (2)

This is physical source-path geometry, not a component diameter or a ghost
ancestry connection. The terminal base is included; its later C tails are not.
The intervening zero-C packets preserve the common heading.

Since3v_a+5u_a<=3(v_a+2u_a), the supply bound becomes

    usable distinguished-input supply <=3w_a+3.         (3)

With permanent U stars one can instead use3(v_a+u_a)+3 from(1).

## 4. Explicit post-entry width-to-length inequality

Take a consumer epoch j after the untouched-entry INPUT horizon20R+211, with
N_j packet starts. Remove at most4851 packets having any perpendicular-source
produced input, by the signed transverse exception theorem. Every remaining
packet's distinguished input is supplied by a parallel/antiparallel source
epoch of even age2,4,...,294. There are at most147 source cohorts.

For each such source clock a apply(3), retaining actual ordered identities.
Distinct consumer packets cannot spend one source identity twice. Therefore

    N_j <=4851+sum_a(3w_a+3)
        <=5292+3*sum_a w_a.                              (4)

Using permanent U stars gives the sharper directional base-count form

    N_j <=5292+3*sum_a(v_a+u_a).                         (4a)

The sums cover at most147 recent even-age source clocks. With entry funding
still present add at most r0 to these bounds; expiration removes that term,
not the source intervals or widths.

In particular, if each relevant source epoch's ACTUAL base sweep lies in a
normal strip of width W (the strip anchors may differ), then w_a<=floor(W/2)
and

    N_j <=5292+441*floor(W/2).                            (5)

This is an explicit finite aperiodic corridor width-to-length bound. It uses
no translation period, normal density, infinite prepared field, or complete
periodic bulk-interface contract.

Conversely any unbounded sequence of post-entry epoch lengths forces an
unbounded recent parallel source transverse sweep: some source has

    w_a >= max(0,ceil((N_j-5292)/441)).

Using(4a), at least one source epoch also has an unbounded number of V/U bases,
not just an arbitrarily long D chain. No independent U-birth count is asserted.

## 5. What is and is not proved

The331-layer online frontier remains finite but growing. Equations(4)-(5)
identify an explicit way that growth must be financed: young parallel epochs
must provide growing transverse source sweeps or V/U production. A corridor
with uniformly bounded recent source widths cannot hide unbounded longitudinal
D runs after entry roots cease to fund inputs.

This does NOT bound those widths uniformly on an arbitrary actual history,
make their sum decrease, construct a complete corridor transducer across
changing widths, or establish periodicity/stabilization. One growing epoch
may inherit supply from earlier growing epochs; that renewal is the remaining
transport problem. Existing periodic-profile clocks are not imported.

The signed all-N young rail UCC,V^N,VCC,V^(N-1) remains entry-funded: its return
V distinguished input(1,2) is an untouched entry root. It therefore does not
contradict(4). Its outbound V train has growing normal sweep anyway; it is not
a bounded-width D-supply construction.

## Dependencies and exact controls

- Signed294 input lifetime and zero-C epoch fuel.
- Signed33-per-perpendicular-epoch /4851 exception theorem.
- Literal retained masks and base increments.
- Signed U left-star permanence ONLY for optional sharper(1)/(4a).

parallel_epoch_width_controls.json records every literal odd slot/count and
its permanent-star subtraction, the exact base normal increments, and the
integer capacity inequalities. The main width bound(4) does not need a new
search or the optional permanence premise.
