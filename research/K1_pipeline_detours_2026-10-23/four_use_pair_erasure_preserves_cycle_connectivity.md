# Deleting every four-use exchange pair leaves the canonical graph connected

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d. Positive output is retained. No K1, plateau, root-free or global
zero-output premise. Pending independent review.

Let sigma be the actual one-P-cycle on outgoing edge-occurrence classes;
sigma0 the signed full L1/R2 repair; G its connected canonical-node graph.
Let F4 count physical edge classes of full flow FOUR. Each has the exact
source/target profiles from signed160ea8de, and contributes TWO distinct
parallel graph exchanges. Distinct physical four-use edges have disjoint
source/target cell classes.

THEOREM: remove BOTH exchange edges at EVERY physical four-use pair.
The resulting graph G_minus is STILL CONNECTED. Consequently

    beta(G)-2F4 >=0 and is EVEN,
    beta(G)>=2F4.

The former beta>=F4 remains true but is weaker. More importantly, the
parallel four-use pairs cannot be the only connection across any cut
of the canonical graph. A deep essential ladder supported by such a
pair needs an additional route using other exchanges; the pair alone
cannot close the one actual event orbit.

This is connectivity of a repaired occurrence graph, NOT permission to
erase physical ant reads, change the board, splice poses, or construct
a new legal ant trajectory.

## 1. Exact successor conjugacy at one physical four-use edge

Normalize source v's complete headings to EWEW, target w's to SSSS,
with every v departure along e to w. Actual chronological ordinal
matching gives T_r(w)=T_r(v)+1 for all four ranks. Write a,b for the
outgoing occurrence classes at v.L1,v.R2. Their actual successors are
c=sigma(a), d=sigma(b), the outgoing classes at w.L1,w.R2.

The source repair transposes a,b; the target repair transposes c,d.
Thus, with s=(a b), t=(c d),

    t=sigma s sigma^(-1),
    st sigma=s sigma s.

The last expression is a CONJUGATE of sigma, so repairing BOTH cells
preserves its single-cycle structure. This uses exact actual successors,
not merely equal physical support or the fact the graph edges are
parallel. The two L suppliers at ranks1 and3 are still actual reads.

All four classes are distinct. Source/target cells have different
saturation types and opposite checker parity, while full drift preserves
parity. Each cell's L1/R2 classes differ: otherwise their physical return
span would be a nonzero multiple of P with zero displacement, impossible
for d!=0. No primitive period or short-quotient assumption is hidden.

## 2. All pairs can be repaired simultaneously

A four-read WHITE cell cannot have both a four-use incoming and a
four-use outgoing port. Different physical four-use edges therefore
have disjoint cell classes, hence disjoint source/target transposition
supports. Let S be the product of ALL source transpositions and T the
product of ALL target transpositions. Then

    T=sigma S sigma^(-1),   S^2=1,
    sigma_F4=ST sigma=S sigma S.

Here ST is EXACTLY the product of repairs at all four-use source and
target cells. Thus sigma_F4 is one P-cycle, even when the source/target
pairs interleave arbitrarily in actual time. No nested-interval or
nonoverlap-of-time-spans hypothesis is made.

## 3. Recover the graph after deleting those exchanges

Let U be the product of all OTHER two-R cell transpositions. All local
repair transpositions are disjoint, so

    sigma0=U sigma_F4.

The nodes of G_minus remain the cycles of sigma0; its edges are exactly
the transpositions in U. A union of graph components is invariant under
sigma0 and every U transposition, hence under sigma_F4. Since sigma_F4
is one P-cycle, no proper nonempty node union is possible. G_minus is
connected. Applying the same permutation-sign argument as fd20e425 to
U and sigma_F4 proves its cycle excess is even. Its edge count is
|E(G)|-2F4, with the SAME nodes, so beta(G_minus)=beta(G)-2F4>=0.

## 4. Independent clock interpretation of the same obstruction

At v and w the actual Delta=T2-T1 is EQUAL. The two graph exchanges
connect the same upper/lower nodes with OPPOSITE clock signs: at v,
outL1 is upper and outR2 lower; at w their roles reverse. Across ANY
node-union cut their equal weighted clock transfers cancel exactly.

If G_minus had a proper component A, no other exchange would cross it.
Summing the signed canonical clock identity would then give

    P*sum_(gamma in A) winding(gamma)=sum_(gamma in A) length(gamma).

The right side lies strictly between0 and P because the canonical nodes
partition the P occurrence classes. The left side is an integer multiple
of P. Contradiction. This also retains physical return spans larger
than P; it never replaces Delta by a residue modulo P.

This is an alternate proof of the same connectivity theorem, not an
extra additive period or fuel payment.

## 5. Essential-band consequence and exact limitations

Use simultaneous scalar geometry3c25695f and ordered bands fd44da68.
Deleting four-use pairs leaves a route between every consecutive pair
of essential nodes. Thus the direct root-free deep ladder ef3f393d
cannot be assembled solely by its matched parallel pairs: some other
exchange path across that spatial band is compulsory. It may use
ordinary essential contacts, elementary C/L face patches or odd-root
exceptional nodes. Those alternatives are not excluded here.

For the old distinct max-RIGHT contractible family h, the signed
h<=J+F4 gives the dependent stronger h<=J+beta/2. It is a distinct-node
capacity, NOT a new per-renewal count, and it must not be added to the
already stronger odd-root capacity without disjointness.

The conjugated permutation is not an actual ant trace; no controller
or WHITE-front positive is built by this manipulation. There is still
no beta upper bound, original-fuel bound or global cap-four exclusion.
The proof is genuinely cap4: an edge used four times in a higher-cap
front does NOT ensure these exact L1/R2 source/target successor pairs.

The companion control verifies one exact16-event permutation with two
interleaved pair supports. It is a sanity check of the algebra only;
no finite physical or translating ant realization is asserted. The
all-size proof is sections1-3.
