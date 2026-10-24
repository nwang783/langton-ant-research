# Earlier TOP R0 suppliers bound distinct penultimate stock holes, including nonleaves

23 October 2026, 17:19 UTC. New actual-source occurrence register, pending
independent review. No graph-leaf, original-root or permanent-fuel
assumption is made.

## 1. Local supplier rules with exact multiplicities

Use a complete WHITE cap-four front and its signed repaired sheets.
Let lambda be the locally higher C height at a visited cell. The
canonical top sheet at that cell, j=lambda, turns only RIGHT. This is
immediate from all one-R, flat two-R and height-two local inventories.
The first R0 also chooses a locally higher C face and has label lambda.

Therefore a canonical LEFT turn at penultimate level j=M-1 is possible
only when lambda>=M, hence lambda=M. Its cell has an actual earlier
TOP R0 occurrence at label M. One physical cell contributes at most TWO
canonical LEFT corners on that sheet, since the sheet has at most two
incoming/outgoing ports. Thus each such earlier R0 supplies at most two
penultimate LEFT corners, even if they belong to different node-cycles.
The required predecessor is a real first R0, not a static face count.

A canonical RIGHT turn at j=M-1 whose right C is a global max M has a
DIFFERENT local type. The C-height difference must be TWO:

- difference one has only one R, on sheet M, and a possible L on M-1;
- flat M/M contacts have their R turns at M, and only L turns on M-1;
- the height-two case has its second canonical R on M-1.

Consequently each max-RIGHT corner has its own earlier TOP R0 and NO
LEFT corner at M-1 anywhere in that cell. Different such corners belong
to different physical cell classes, because there is only one canonical
M-1 R passage there. These TOP R0 suppliers are disjoint from all the
suppliers of the preceding LEFT-corner inventory.

The facts above are exact consequences of the complete 30-row signed
local sheet table, including RL final L1, RLR roots with no L3, and all
four-read equality cases.

## 2. An arbitrary family of distinct contractible holes

Let H be the number of DISTINCT contractible penultimate cycles having
at least one max-RIGHT corner. They need NOT be leaves. The signed
orientation and length results make each counterclockwise with length
ell_i>=12. Put

    L=sum ell_i,
    T=total max-RIGHT corners on these cycles, so T>=H.

A counterclockwise cycle of length ell_i has (ell_i+4)/2 LEFT corners.
Thus the entire family has

    N_LEFT=L/2+2H.

At most two of these corners share one earlier TOP R0 supplier. The
T max-RIGHT suppliers are distinct from these and from each other.
Therefore

    N_top_R0 >= N_LEFT/2+T = L/4+H+T.              (1)

Every ell_i is divisible by four, so no fractional rounding is hidden.
This is a bounded-multiplicity actual source map, not a declaration
that the sources have disjoint original-seed ancestry.

## 3. Reserve the top birth L1s rather than counting them as R0s

Let F_max count global-max C face classes. The signed top-sheet repair
has 4F_max edge occurrences. The positive-port first-L birth theorem
gives each max face a distinct TOP L1 birth edge occurrence. These
cannot be counted as R0 sources. Hence

    N_top_R0<=3F_max.

Together with (1),

    3F_max >= L/4+H+T,
    F_max >= ceil((L/4+H+T)/3) >= ceil(5H/3).      (2)

The last inequality uses L>=12H and T>=H. Face classes, not separate
max components or original fuel roots, are being counted.

## 4. Disjoint capacity, with the K=1 essential sheet retained

Top cycles at M and the H contractible penultimate cycles are disjoint
actual edge-occurrence families. Thus all complete-white cap-four
fronts satisfy

    P >= L+4F_max
      >= L+4 ceil((L/4+H+T)/3).                   (3)

For K=1, c_right=M-1. This carrying sheet has at least one essential
canonical cycle, disjoint from the contractible holes and from TOP.
It has length at least 2D, D=||d||infinity. Therefore

    P >= L+4 ceil((L/4+H+T)/3)+2D
      >= 12H+4 ceil(5H/3)+2D
      >= (56/3)H+2D.                             (4)

This is one explicit disjoint register. Do not add it to overlapping
A/B, side-current or earlier whole-period bounds. The previous
clockwise-compensation register may be combined by max, not by summing.

## 5. How it meets, and does not solve, the renewal problem

The signed row-5 supplier can put its higher node in one of these
contractible holes. Several renewals may occupy different max-RIGHT
corners of the SAME hole. Their corners appear in T, not automatically
as distinct H. A renewal-to-corner injection must be specified before
using a renewal count in (1); none is assumed here.

Equality L3 sources and one-R final-L1 stocks remain valid. The new
bound uses their real earlier TOP R0, and explicitly allows two LEFT
corners to share that source. It therefore does not pretend that every
old-stock contact is a height rise or a fresh source.

Essential higher nodes, graph handles and lower essential-pair
alternatives remain. Original finite-seed black mass is not bounded by
F_max, and TOP R0 supply can grow with ordinary white exploration.
Thus no finite-fuel, K>=2 or eventual-capture conclusion follows.

Sources retained unchanged: signed cap-four local R maximum and stream
sheet repair fd20e425b8a6bbc3aefd5eca06b4d443c1d2bdfde5f1d2d69c25d5c4d62af484;
positive-port first-L max-face birth c91710090256c728ae9876e7188a39fff3617fcb151a9fd3fc595c5bdbb7f6a5;
penultimate orientation a2170bdce45e58734901f1ebb215f7ac5f7b58ab26deafe2cac8567a3133ec22;
stock-hole length 1527bbd19fa04c9ad92a8a2c97f8e5926b8537ac2e51c40b0a0a1c57dbf0c43f.
