# A spatial archive-or-older-input condition for fresh helper interleavings

24 October 2026. This applies the RETAINED axial transport charge to current
complete archive components. It is not a new conservation law, not a stack
rule, and not an impossibility theorem for long-range fresh interleavings.
The new application is a linewise older-input/fresh-archive alternative.

## 1. Setup and the geometric alternative

Use one complete finite-board trajectory. A helper f is R-born at physical
cell y at update b. In the intended application it is dormant at departure
cut d of another marked episode, and later consumed at j<c, with its own
earlier departure s<d. For the inequality itself we only need b<d and
p_b=y. Suppose EVERY full active w component at cuts b,...,d has at most
M edges, M>=2. This is an ADDITIONAL earlier cap premise, not supplied by
the parent episode's cap on [d-1,c] alone.

Choose a coordinate axis i on which L=|p_d[i]-y[i]| is maximal. Let J be
the L-1 strict separating integer coordinate lines; if L<=1 it is empty.
The older cohort consists of the actual black LIFETIMES present at cut b,
before the helper's R birth. For each line r in J define:

* K_r: the number of distinct older-cohort lifetimes on that line ACTUALLY
  consumed during updates [b,d). A later rebirth does not refund K_r.
* F_r: the number of cells on that line BLACK at cut d whose CURRENT
  lifetime was R-born at some update in [b,d).

Then the exact linewise condition is

    K_r + F_r >= 2                 for EVERY r in J.               (1)

Thus crossing each separating line without retiring any older lifetime
requires at least TWO current fresh black lifetimes on that line. They
must still be physically present at checkpoint d, not merely have been
written and erased sometime in the past. This is the precise conditional
older-connector-or-persistent-output condition; it does not assume a
frozen Jordan fence, an infinite exterior path, or a simple cursor chord.

Put K=sum(K_r) and let N_new(d) count the COMPLETE dormant w components
at cut d containing at least one of those current fresh lifetimes (or,
more generously, any current lifetime born in [b,d)). Then

    fresh black mass on J >= 2(L-1)-K,
    N_new(d) >= ceil( (2(L-1)-K-M)_+ / (M-1) ).                   (2)

In particular, bounded older-input retirement K and fixed active cap M
force linearly many DISTINCT current dormant components as L grows.
They cannot be replaced by an unchanged type-count assertion: their fresh
lifetimes must occupy the actual separating lines.

## 2. Proof with identities and complete fields retained

Let B_b and B_d be the full black fields at the two cuts. The retained
axial invariant says that on each strict separating line the alternating
signed difference between B_d and B_b is2 modulo4. Consequently that
line contains at least two cells of B_d symmetric_difference B_b. This
is the strict-line part of `global_capture_bridge_2026-10-23/
live_cursor_transport_debt.md`, applied with comparison board B_b and
zero height modification; the line charge itself is inherited.

A cell of B_b\B_d has consumed its original cut-b black lifetime, hence
contributes to K_r. A cell of B_d\B_b has a current lifetime actually born
after cut b, hence contributes to F_r. These two sets partition the bit
discrepancy. Therefore K_r+F_r>=2. A cut-b black cell which was consumed
and reborn before d contributes to BOTH actual resource categories but
not to the discrepancy; this only strengthens (1). Summing (1) proves
the first inequality in (2), with distinct coordinate lines counted once.

At most M current fresh cells can be active at d. Consider ANY dormant
complete component at d containing a still-black lifetime born after b.
That lifetime was active immediately after its R birth. Take its LAST
active-to-dormant transition before d. It is an actual bridge-L departure:
the pre-L full active component has at most M edges, one edge is deleted,
and the departed complete component has at most M-1 edges. That component
then stays EXACTLY frozen until d; otherwise there would be a later active
cut. No passive/passive merger can occur without an active R import.
Hence EVERY such dormant full component has at most M-1 edges, even if it
also contains older lifetimes or cycles. Dividing the fresh dormant mass
lower bound by M-1 proves the second inequality.

No arbitrary initial archive is discarded. Older components may be huge,
but importing one into a fresh component under this cap would itself be
charged by the complete active bound. Both checkerboard graphs and the
continuous head remain the actual physical ones.

## 3. Legal regeneration and the exact limitation

Equation(1) is valid even when old cells are deleted, rewritten, imported,
split, merged, and later released. Old-cohort retirement is counted once
per actual lifetime, while F_r uses the CURRENT birth label. An unread
initial exterior component contributes nothing for free to the difference:
its bits cancel unless it is actually retired or becomes part of a fresh
component, in which case the cap argument still applies.

This is nonetheless a CHECKPOINT ledger, not a global decreasing resource.
Fresh archives may later be consumed or legally regenerated; the same
distributed output can support several overlapping episodes. Standard104
itself emits linearly many fresh dormant trees during transport. The
inequality does not prove those trees cannot later be recycled through a
different route, and does not charge one unique older input per parent.

Thus long-range interleavings with no substantial older-input use would
need a growing spatial stock of actual fresh archives. Ruling out their
usable recycling remains the attraction gap. Neither a bounded active
component nor the chronological order s<d<=j<c alone closes it.

## 4. Two exact named controls, with different scopes

`check_interleaving_spatial_archive_ledger.py` keeps all black fields and
current birth labels and checks every separating line and full component.
It does not perform a seed, pose, word, ratio, or cap scan.

1. Start the ordinary blank ant at(0,0),N. The helper at(1,0), born R1,
   is released at cut17 and consumed L53. The parent at(0,1), born R7,
   is released at cut18 and consumed L59. Thus17<18<53<59 is an actual
   COMPLETED fresh interleaving, extending the retained42-step non-LIFO
   reactivation witness to actual consumption identities. The only older-
   than-helper lifetime (R0) was already consumed at4, so no such older
   connector is consumed DURING cuts17 through59. This is SHORT-range:
   distance2, cap10 on [1,18], not a long-range countercontrol.

2. In the signed20-cell n400 orbit, take the actually returning R60
   lifetime at(0,2), and checkpoint d=20627, the first remote port entry.
   The exact interval cap on [60,d] is42, displacement L=399. There are
   398 separating columns and11 older cut60-cohort retirements on them.
   The checkpoint has2396 current fresh black cells and199 complete
   dormant components containing fresh cells. Formula(2) requires at
   least19 and is genuinely positive. Every old remote port remains on
   the board. Its known later target consumption is248084. This checkpoint
   is NOT asserted to be the departure of a second completed parent
   episode: it tests the spatial lemma on an actual returning lifetime,
   not arbitrarily many fresh interleavings or free turnaround regeneration.

## 5. Dependencies and no new global claim

The line charge is the retained axial invariant, as applied in
`global_capture_bridge_2026-10-23/live_cursor_transport_debt.md` Sections1--3.
The complete-component freezing/metric rules are independently checked in
`active_w_archive_itinerary_2026-10-23/ACTIVE_EPISODES.md`. The blank archive
regression is retained in `global_renewal_archive_2026-10-23/
serial_bridge_release_and_archive_splice_v2.md` Section7. The20-cell orbit
and its all-parameter eventual capture are retained in the signed scalable
feedback circuit and sustained-cap package. Their source proofs are not
replaced by this one named n400 replay.

No persistent-loop surgery, generic LIFO ordering, mass descent, finite
summary, arbitrary preparation deletion, or universal capture is inferred.
