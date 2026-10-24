# The retained RR maximum-stock gate must immediately enter strict STRAIGHT

23 October 2026, 20:14 UTC. Version 2, exact continuation of the retained RR stock
inventory, submitted for independent review. No global constant-state,
leftmostness, fuel payment or original-root assumption is needed.

Use precisely K1_locked_RIGHT_to_max_branched_RIGHT_stock_gate.md,
SHA b9f4b64f05d7680c431086a6d0deb3cbfea3c149681c4db127f0b05d694965b0.
Thus a locked RIGHT F=(0,0) is followed by a max-branched RIGHT G=(1,1),
with selected contacts A=(1,0),B=(1,1),C=(2,1), and complete histories

    B=EEWE, C=SSNS, n=(1,2):NNSN, p=(2,2):EWWW,
    both branches J=(0,2), I=(2,2) at M,
    m=(0,2):WWW or WWWE.

The next curve face H has lower-left (2,0), reached through C. All
coordinates and histories are physical lifts, not phase representatives.

## 1. H cannot turn RIGHT

The next RIGHT direction after F,G would return to the physical maximum
face P=(1,-1) preceding F. Explicitly the four directions are NW,NE,SE,SW
along P->F->G->H->P. This closes a contractible four-edge contact-lattice
square, impossible for the embedded essential Gamma. This is the usual
three-consecutive-RIGHT geometric obstruction, including small quotients.

## 2. H cannot turn LEFT

If H were LEFT, its exit would be D=(3,1) with prefix EEW and LEFT L3,
that is D=EEWE: the one-edge LEFT arc preserves C's LEFT-L3 bit1.
The face after H is K=(3,1). It has only three possible types.

- LEFT is forbidden by the signed all-K no-LL theorem.
- RIGHT would make H,K a LEFT/RIGHT pair with input bit1. The signed
  complete LR theorem requires its lower q helper to have NNNS after
  undoing the quarter rotation, hence EEEW in this pose. That q helper
  is EXACTLY p=(2,2), whose complete history is EWWW. Contradiction.
- STRAIGHT would have first unused LEFT C neighbor I=(2,2), which is
  maximum. A straight equal-M branch requires input LEFT-L3 bit0, while
  D has bit1. Contradiction.

The three face types are exhaustive for a simple embedded curve without
backtrack. Therefore H cannot be LEFT.

Only STRAIGHT remains. Its input C has LEFT L3, so its unused LEFT C
neighbor must be strict. We have proved the exact local word extension

    locked RIGHT -> max-branched RIGHT -> STRICT STRAIGHT.

The following selected output may have bit0 or1; neither is silently
assumed. No global constant-one hypothesis was used.

## 3. An older upper max supplier is forced at this strict gate

Retain C's prefix SSNS and normalize the strict STRAIGHT H=(2,0).
Its near helper v=(3,1) is EEE or EEEW according to its output bit.
The incident other C J'=(3,1) has height M-2. Its unique N output is L1,
supplied by C.R2, so time of that N departure is T2(C)+1.

Put a=(3,2). The NW C face at a is I=(2,2)=M and SE is J'=M-2.
Both its R reads therefore arrive S and choose I. Its W outputs supply
p's THREE W inputs. Its N input edge is supplied by v's ONE N departure.
The complete histories retain BOTH early and late N-entry alternatives:

    a=SNS, SNSS or SSSN.

The late-L3 SSSN alternative is essential and was omitted from the
unreviewed v1 supplier list; no v1 deadline is imported. Exact matching
ALWAYS gives T0(a)=T1(C)-2. The remaining clocks have two different modes:

- For SNS or SNSS, the N input is a.L1, so
  T1(a)=T2(C)+2, T2(p)=T2(C)+3 and T3(C)>=T2(C)+8.
- For SSSN, the N input is a.L3, so
  T3(a)=T2(C)+2 and T3(C)=T2(C)+4.
  It gives the actual consecutive four-L route
  v.L1 -> a.L3 -> p.L3 -> C.L3 -> v.R2.

In both modes a.R0(S)'s W output feeds p.L1(W), whose S output feeds
C.L1(S), proving the common T0(a) clock. The late mode is old-L3 stock,
not an input black terminal or a violation of cap four. It prevents any
unconditional claim T3(C)>=T2(C)+8 in this configuration.

Both BOTTOM corners of I cannot be its canonical birth: p.R0 chooses
G and p.L1(W) uses I's INPUT before its R2 output, while a.R0 already
chooses I. Hence I's parent is one of its two TOP diagonal max neighbors

    parent(I)=(1,3) or (3,3),
    B(I)<=T0(a)-1=B(H)-3,
    B(parent(I))<=B(H)-8.

Both upper suppliers and their optional L3 remain. This is one actual
earlier max birth obligation, not a recursively identical branch pattern,
new component, original-root payment or a general K1 exclusion.

The conclusion preserves the RR four-L old-stock connector. It says that
its legal next geometry is strict STRAIGHT and requires the stated real
older upper supplier, not that the connector is realizable as a full
white front or that its stock is permanent fuel.

Dependencies: signed all-K noLL, signed complete LEFT/RIGHT input1
inventory in K1_LRLR_forces_locked_row4_and_straight.md (SHA4f9db2ac...),
signed strict-straight port table and max-face first-L birth theorem.

A saved complete closure control locked_RR_to_straight_ports.py/json
matches all RR stock ports plus C->v->a->p->C, permits all three a
histories and all output-contact L3 sides, and retains18 necessary rows.
They are not literal exterior traces or complete front realizations.
