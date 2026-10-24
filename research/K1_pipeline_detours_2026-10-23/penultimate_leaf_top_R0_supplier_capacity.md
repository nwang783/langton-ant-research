# Distinct penultimate stock-hole leaves need distinct top R0 suppliers

23 October 2026, 17:15 UTC. Exact source-occurrence capacity, pending
independent review. This counts physical full-period classes, NOT original
seed roots, max components, or renewal sites.

## 1. Restricted family and notation

Use a complete WHITE cap-four front. Let gamma_1,...,gamma_h be DISTINCT
contractible graph-leaf cycles of the repaired sheet j=M-1, each with
its unique repaired root corner a RIGHT turn around a global max C face.
Write ell_i for their lengths and L=sum ell_i. The signed orientation
and length results give ell_i>=12.

The exact leaf-return inventory of max_turn_leaf_stock_balance.md gives

    r_i=(ell_i-6)/2 fresh R0 reads;
    p_i=(ell_i+4)/2 final old L reads,

where final L retains both one-R RL.L1 and RLRL.L3. Its initial L1 and
terminal R2 cancel in color. The root is a height-two defect: its L1
output is M-1, R2 output M-2, and R0 is on top sheet M.

All leaf edge sets, and their terminal R2 occurrences, are pairwise
disjoint as proved in that note. Full-drift translates of a physical
root or stock are retained; counting is by actual occurrence class.

## 2. Every final-L stock at M-1 has a top-sheet first R0

At a one-R RL cell, the final L1 is one level below its R0. Therefore a
final L1 at M-1 has earlier R0 at M.

At a four-read cell, write lambda for the locally higher C height. The
signed L3 label law gives its level at most lambda-1, with equality only
for a flat pair and opposite L1/L3 headings. Since the global C maximum is M, an
L3 at M-1 must be exactly that flat case, and its R0 is again at M.

Each final L belongs to a different physical cell class: a complete
cell history has only one FINAL L read, and the leaf sets contain
distinct such occurrences. Consequently the p_total=(L+4h)/2 old stocks
have p_total DISTINCT earlier TOP R0 occurrence sources. This is actual
source chronology, not an inference from the canonical hole signature.

In addition, the h distinct leaf roots have h distinct R0 occurrences
on top sheet M. None can coincide with one of those stock sources:
a root's two-R height-two history either ends at R2 (no final L), or
has final L3 at level M-2 or M-3, never at M-1. The initial two-R root
L1 is not a final stock read.
This remains true for every drift translate of the root class.

Therefore, writing N_top_R0 for the number of actual top-sheet R0
occurrences,

    N_top_R0 >= p_total+h = (L+6h)/2.             (1)

No two source classes have been declared to descend from distinct
original black roots. They may share arbitrary earlier ancestry.

## 3. Every maximum face reserves one non-R0 top occurrence

Let F_max be the number of global-max C face classes. The canonical top
sheet has exactly 4F_max edge occurrences, partitioned into its four-edge
max-face cycles. The signed positive-port first-L birth theorem gives
each maximum face its canonical birth departure L1, with output ordinal
one and label M. Different max-face classes have different birth edge
occurrences, because one directed edge has only one right C face.

Thus there are at least F_max non-R0 TOP occurrences, and

    N_top_R0<=3F_max.

Combining with (1) gives the exact source capacity

    6F_max >= L+6h,
    F_max >= ceil((L+6h)/6) >= 3h.                (2)

This is a FACE-class count, not a new maximum COMPONENT or a finite
supply theorem. A large component may contain many such faces.

## 4. A disjoint full-period register

The following actual edge-occurrence families are pairwise disjoint:

- all top cycles, 4F_max occurrences on sheet M;
- the h contractible leaf cycles, L occurrences on sheet M-1;
- their h terminal R2 occurrences, all on sheet M-2.

The terminal-sheet assertion uses the max-RIGHT root hypothesis; it
must not be assumed for arbitrary contractible leaves. Hence

    P >= 4F_max+L+h
      >= L+h+4 ceil((L+6h)/6)
      >= 25h.                                    (3)

In the target K=1 scope, c_right=M-1. That carrying sheet has an essential
canonical cycle of length at least 2D, D=||d||infinity. It is disjoint
from the contractible M-1 leaves and from the TOP and M-2 families above.
Thus, specifically for K=1,

    P >= 4F_max+L+h+2D >= 25h+2D.                 (4)

Without K=1 the carrying sheet may be M-2 and overlap terminal R2s, so
this extra +2D is NOT asserted by the same register.

## 5. What remains uncontrolled

The stronger source count does not bound the number of renewals: many
renewal sites may share one NONLEAF stock-hole cycle, or use essential
middle cycles or the other signed topology alternatives. Nor does (2)
charge faces to original finite-seed roots. Top R0 sources can be
replenished by ordinary white exploration and can share old ancestry.

The prepared star's singleton-black-L fuel has no earlier R0 source and
therefore correctly falls outside Section 2. Its old-white four-L leaves
have canonical root LEFT, not the max-RIGHT hypothesis. The controls
are not contradicted. Do not add (3)/(4) to overlapping corridor bounds;
only the explicit disjoint register above is claimed.

Sources: signed chronological sheet labels and birth theorem; signed
penultimate orientation and >=12 length; max_turn_leaf_stock_balance.md,
SHA 5e1794e79ae8bf226af2c4ff6e693ffc233128f2bb4e8132cf9cc82e90aaad2b.
