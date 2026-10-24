# Exact prepared secondary suppliers of the reverse locked rail

24 October 2026, 02:38 UTC. Complete original WHITE cap-four front;
reverse corners on a root-free Q plateau are WHITE-even, but BLACK-odd
suppliers off Q remain allowed. Conditional on the locked main rail;
the axis-rail derivation is separately pending as2ca8c002. No global
reverse-WHITE or zero-output hypothesis is made here. Pending review.

Normalize reverse plateau height lambda=0, low row b=-2, and genuine
reverse L lower bound -3. Use the exact locked rail coordinates:

    Z_k=(0,2k)=WWWE, Y_k=(0,2k+1)=NNNS,
    A_k=(1,2k)=NNSN, B_k=(1,2k+1)=EEWE.

The secondary cells are O_k=(-1,2k+1) and E_k=(-1,2k). Their common other
C face H_k has height eta. Main port matching fixes O_k's ONE W input
at S_k=T1(Y_k)+1, and E_k's ONE E output at F_k=T3(Z_k)-1. The actual
K1 order retains

    S_k<F_k<S_(k+1).

All N departures from O_k enter E_(k+1); all S departures enter E_k.
Other external suppliers remain unspecified, not free or deleted.

## 1. All six O and six E histories

A complete original WHITE history reverses to WHITE RL/RLRL or BLACK
L/LRL. These are the ONLY initial-color/length alternatives. Reconstruct
the local faces with C_NE(O)=b, C_SE(E)=b and every L>=-3. Then exactly:

    eta     O_k headings, first color     E_k headings, first color
     -2       W, BLACK                     S, BLACK
     -1       EW, WHITE                    SS, WHITE
     -1       WEE or EEW, BLACK            NSS or SSN, BLACK
      0       EEEW or EWEE, WHITE           SSSN or SNSS, WHITE.

Rows at the same eta can mix across O/E subject to exact ordinal ports.
No eta below -2 or above0 is possible. Thus unraised secondary supply
at eta=-2 necessarily uses two BLACK singleton L reads. A WHITE active
supplier requires a raised secondary C height. BLACK three-read supply
at eta=-1 is retained, not silently identified with a WHITE RLR cell.

The complete same-eta S-port match plus strict S_k<F_k leaves ELEVEN
necessary O/E pairs. They still must match their N ports across k and
all deeper external ports; none is declared an attained global rail.

## 2. An unraised pair is one exact four-L fuel return

If eta=-2, its two singleton reads are forced consecutive:

    Y_k.L1 -> O_k.singleton-L -> E_k.singleton-L
            -> Z_k.L3 -> Y_k.R2.

These are actual physical port occurrences, every arrow one time unit.
The reverse factor is LLLLR, and T2(Y_k)-T1(Y_k)=4. Original forward
time gives

    Y_k.L1 -> Z_k.R0 -> E_k.singleton-R
            -> O_k.singleton-R -> Y_k.R2,

with word LRRRR. The two odd outputs are genuine original TOP singleton
R classes, with both original L heights M-1. The old main L3 stock is
retained. This is a conditional literal factor, not proof that all its
outside histories can be completed indefinitely.

This interface explains exactly why the original all-WHITE secondary
obstruction cannot be imported into the prepared reverse setting.
BLACK singleton fuel really can meet those immediate ports.

## 3. BLACK three-read suppliers are shallow top outputs too

At eta=-1 the allowed BLACK LRL histories have opposite endpoint L
headings and one middle R. Both reverse L sectors are -3. On reversing
to the original front, they are opposite-R three-read output classes
incident to C=M, with original L heights M-1 and M-2. They are SHALLOW
outputs, not roots of the original L minimum M-3.

At eta=0 both secondary cells are WHITE four-read and H_k is another
reverse height-lambda face to the LEFT of the complete low row. It is
not automatically in Q, nor locally maximal or root-free: its farther
corners can meet odd defects or a higher reverse C plateau (a deeper
original L minimum). Same-height or deeper transfer must remain open.

## 4. One exact full-quotient count, without an added payment

In a full vertical rail quotient, let B1 count eta=-2 pairs and B3 count
BLACK three-read O cells. Each such O has one N output; eta=0 O cells
also have one, while all other O cells have none. Likewise BLACK3 E and
eta=0 E have one N input. Since the latter eta=0 counts agree by pairs,
complete O_k->E_(k+1) N-port matching gives

    number of BLACK3 O = number of BLACK3 E.

Hence the distinct secondary odd-output classes number

    2(B1+B3),

all shallow TOP types. O/E cannot fold into one class because their
checker parities differ and full drift preserves parity. This register
may overlap other shallow-output reservations and is NOT added to them.
It does not charge an initial seed, one resource per stage renewal, or
an arbitrary deeper supplier path.

## 5. Certificate and unresolved assembly

`reverse_locked_rail_secondary_prepared_ports.py/json` enumerates the
allowed initial-color/length histories, reconstructs both incident C
and L heights, matches every same-pair S occurrence and same-cell gap,
and retains strict S<F. It finds six profiles on each side and eleven
local pairs. Full N matching, deeper connectors and actual finite or
infinite realization remain separate obligations. No period, width,
drift or radius search is performed.
