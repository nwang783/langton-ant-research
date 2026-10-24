# Positive-flat three-read output cannot fund a half-turn rail defect

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d. No K1 or zero-output hypothesis for the rail itself. H counts the
same exact initial half-turn sources as63ee2ab8, including their terminal
NE child and stable opposite leaf; arbitrary relaxed RIGHT rows are not
counted. Define Npos to be the number of physical full-drift THREE-read
classes with opposite R headings and L1=R2, not R0. These are positive
flat RLR classes. Then

    H <= 6 (Nodd-Npos)+|U|
      <= 7 (Nodd-Npos)-n_Sanc.

Here U is the exact residual negative set from f02b2276. The optional
singleton ancestor family n_Sanc can be set to zero. This strengthens
the signed H<=11Nodd-n_Sanc by actual local defect types, not just a
smaller geometric constant. It is OUTPUT capacity only.

## 1. Classify the actual parent and child squares, keeping odd cases

Normalize a carried half-turn source D_n=(0,0), with NW w=(0,1)=SSNS,
SW h=(0,0)=WWEW, the terminal/degree-one right-child k/j histories, the
stable opposite leaf, and the upper-left strict C face at height b=M-2.
All these are the exact carried interface of45753ce6.

First complete the ACTUAL parent U_n=(-1,1), retaining its SE w=SSNS
and NE opposite C height b. All110 canonical profiles/four rotations
give exactly FIVE upper profiles, written SW z, NW y, NE v, SE w:

    z     y     v     w
    EEW   NNSS  EWE   SSNS
    EEWE  NNN   EWE   SSNS
    EEWE  NNNS  EEEW  SSNS
    EEWE  NNNS  EWEE  SSNS
    W     SSNS  EEEW  SSNS.

Every profile with ANY odd cell has a NON-positive-flat odd witness at
one of z=(-1,1), y=(-1,2), v=(0,2). These witnesses are negative-flat
EEW, same-R NNN/EWE, or singleton W. If there is any odd cell, stop
and select such a witness. If all are even, retain the signed exact
+12 ordinal cycle using the carried k=EEWE/j=NNNS histories; this
excludes v=EWEE and leaves the full clean upper profile.

Next complete the ACTUAL lower child R_n=(-1,-1), whose canonical entry
is NE h=WWEW. Its NW a=(-1,0) receives exactly one S input from clean
z=EEWE; its SE l=(0,-1) emits exactly one E output into the stable
opposite-leaf corner. The complete canonical inventory gives NINE
profiles. Every one with an odd corner has a non-positive-flat odd
witness at l=(0,-1) or SW s=(-1,-1): l=SSS or s=WWW/WEW.
The possibly positive-flat a=SNN never occurs alone; its row also has
l=SSS. Thus we may stop at one of the stated NON-positive witnesses.

If all four lower corners are even, the same physical canonical-cycle
exclusions as45753ce6 eliminate a=NNSN. The remaining R_n is the stable
terminal flag-one leaf. Stop if R_n belongs to U. Otherwise its exact
inverse-I association activates an ACTUAL positive D4 at D_(n+1),
forcing its remaining source corners to be four-read and propagating
the full next interface.

There are no hidden extra odd tests in that activation: membership
outside U means R_n=I of an actual D4 by definition, not merely a
potential row. The inverse physical source is unique. Hence all failed
steps can be covered by the stated non-positive odd witnesses or U.
At every continued step the whole exact clean interface is retained.

## 2. Six eligible stopping sources per available odd class

The witness offsets are only

    S={(-1,1),(-1,2),(0,2),(0,-1),(-1,-1)}.

Four rotations about the source face center produce TWELVE distinct
offsets, six per checker parity. Actual full drift preserves parity.
Thus a fixed non-positive odd class can witness at most six distinct
first-stopping source classes in the full quotient.

The signed rail periodicity and nonmerge arguments63ee2ab8 apply
unchanged: a never-stopping exact interface contradicts full-drift
history equivariance, and two distinct initial sources cannot share a
carried or stopping D because terminal NSSS would equal degree-one
SSNS. A U stop still injects into its residual leaf, by that leaf's
unique actual parent. Consequently

    H <=6(Nodd-Npos)+|U|.

This is not a claim that each source needs six outputs or that the
stopping cells inject. The bounded degree is six and has already
accounted for all orientations and quotient aliases.

## 3. Positive-flat output is also absent from the U payment

The signed identity and output partition give

    |U|=N_O+D_C+D_H+D_S.

Its reserved outputs are negative-flat three-read canonical entries
(O and C), same-R three-read strict helpers (H), and singleton R cells
(S). These physical classes are disjoint as proved in bf0785e8.
The optional singleton n_Sanc family is disjoint from them as well.
NONE is a positive-flat three-read class: the canonical entries have
L1=R0, helpers have equal R headings, and singletons have one read.
Therefore all Npos classes are additionally disjoint from this entire
reserved union, and

    |U|+Npos+n_Sanc <= Nodd.

Substitution proves the second displayed rail bound. No new original-
fuel injection is inferred from this output partition.

## 4. Coupling to the signed early positive-flat output family

Under K1 let n3 count all surviving early source classes, S or R
ancestors, with the lower interface x=EWW,r=WEEW,e=SNN. The signed
first-leaf role injection ef9fc2e0/d8ba383a reserves TWO distinct
positive-flat three-read classes x,e per such source. Thus Npos>=2n3,
and the same bound gives

    H <=7Nodd-14n3-n_Sanc.

This subtraction is justified by TYPE disjointness, not by adding an
early output lower bound to an overlapping half-turn resource budget.
H still requires the exact initial half-turn interface; no global K1
or finite-seed exclusion follows.

Control `half_turn_rail_nonpositive_odd_defect_cover.py/json` reconstructs
the five upper and nine lower canonical profiles, verifies each odd
profile has the retained non-positive witness, and checks the twelve
rotated offsets/six parity split. It performs no front, period, drift,
radius or multiplicity scan. The only transported chronology used is
the already signed exact rail cycle/exclusion and inverse-I activation.
