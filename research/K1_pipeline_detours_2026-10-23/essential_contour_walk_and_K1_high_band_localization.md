# Essential contours form an exact level walk; K1 maxima stay in ceiling bands

24 October 2026, 01:48 UTC. Complete WHITE cap-four translating front,
actual full P,d. Positive required odd output is retained. Pending
independent review. Dependencies: simultaneous scalar terrain3c25695f,
unconditional clockwise C-face classification2c2d0905, contact barriers
ad564468 and locally maximal WHITE plateau theorem ab9fad0a.

## 1. Ordered essential circles and the annulus separation lemma

All essential canonical circles across ALL sheets are simultaneously
disjoint by the scalar terrain theorem. There are finitely many in the
full cylinder, at least one, and they have a global transverse order
from the LEFT exterior to the RIGHT exterior. Write their sheet labels
j_1,...,j_n and oriented full-drift windings w_i in {+1,-1}.

The scalar level at label j is ell_j=j-1/2. At a positive circle higher
F is on its global RIGHT; at a negative circle higher F is on global
LEFT. Between two consecutive essential circles there is an annulus
with NO essential canonical circle of any sheet in its interior.

Use this elementary separation fact: if, on collars of the two annulus
boundaries, F-ell has opposite signs for a half-integer ell, then the
level F=ell contains an essential circle inside that annulus. A finite
union of contractible level circles cannot separate its two ends. This
also applies when one boundary itself has value ell, by using the open
collar on the indicated side, not the boundary value.

## 2. Exact adjacent-label rules

The absence of an intermediate essential circle forces

    w_i,w_(i+1)       j_(i+1)-j_i
        +,+                 +1
        -,-                 -1
        +,-                  0
        -,+                  0.

For example, in the +,+ case the left inner collar is above ell_(j_i),
and the right inner collar below ell_(j_(i+1)). If j_(i+1)<=j_i, the
right boundary's own half-level separates these collars, forcing another
essential circle. If j_(i+1)>=j_i+2, a strict intermediate half-level
does the same. Thus the difference is exactly1. The other same-sign
case is its reversal. For opposite signs the two inner collars are
both above, or both below, their respective levels; unequal labels
force a separating additional circle at the higher or lower boundary's
own half-level. Hence those labels agree.

The constant exterior values give exact end rules. At the first circle,

    w_1=+1 => j_1=c_left+1;
    w_1=-1 => j_1=c_left.

At the last,

    w_n=+1 => j_n=c_right;
    w_n=-1 => j_n=c_right+1.

Otherwise a half-level between the exterior constant and its boundary
collar, possibly that boundary's own level, would force an earlier or
later essential circle.

Consequently there is an EXACT nearest-neighbor integer walk

    u_0=c_left,   u_i=u_(i-1)+w_i,   u_n=c_right,
    j_i=max(u_(i-1),u_i).

The intermediate annular band after circle i has integer base u_i;
the two outer regions have bases c_left and c_right. This is not a
hypothesis that the actual cursor follows a contour or monotone spatial
path. It is a theorem about the ordered scalar level circles.

## 3. Contractible graph components cannot jump essential barriers

At every exchange the two shared-port tracks have adjacent labels.
The short open dual-edge connector has values strictly between their
half-integer levels and therefore crosses NO canonical contour. A
contractible circle lies wholly in one complementary band of the full
essential family. Thus every connected component of the repaired graph
after deleting its essential nodes stays in one such spatial band.
It can attach only to that band's one or two essential boundary nodes,
not jump over a third essential circle. A direct essential exchange
likewise joins consecutive essential circles. Graph connectedness
requires communication across every intervening band, but does not
say that this communication is a literal chronological factor.

This is an exact localization of the remaining face-patch/odd-defect
assembly. It does not assume those graph components are trees.

## 4. The C height in a base-a band is at most a+1

At the half-level a+1/2, every boundary collar of a base-a band is on
the LOW side. Indeed its boundary labels are a or a+1 by section2;
a label-a boundary is lower than this level, and a label-(a+1) boundary
has the base-a band on its low side. In an outer region its constant
exterior is a, also below this level.

A high component F>a+1/2 inside the band therefore has its boundary
inside the band. It cannot be essential, since no additional essential
circle is allowed there. Its outer boundary is a clockwise canonical
circle at sheet a+1, hence a unit C-face loop enclosing only a C face
of height a+1. It cannot contain any C face of height>=a+2. Therefore

    every C face in a base-a band has h(C)<=a+1.           (1)

Odd-root low depressions may still be arbitrarily deep; no dual bound
is inferred in the positive-output case.

## 5. Every up/down peak is at or above c_right

Suppose consecutive essential signs are +,-. Their common label is j,
and the intermediate band has base a=j and is on the HIGH side of both
circles. An essential circle has zero total turning over a period, so
has a LEFT corner. At such a corner a C sector on its RIGHT has height
at least j+1 by the signed turn inequality. That sector lies inside
the high band. Equation(1) makes its height exactly j+1.

The C superlevel >=j+1 cannot cross either sheet-j boundary by the
contact barrier. A connected height-(j+1) maximum plateau inside the
band is therefore locally maximal in the whole plane, not just after
cutting the band. It is finite in the full quotient. Its incident
corners are all initially WHITE, so the signed plateau theorem gives

    j+1>c_right, equivalently j>=c_right.                (2)

This restriction is all-output. No condition on reverse first colors
is being silently imported for valleys.

## 6. K1 has only ceiling peaks

For K1, M=c_right+1. The sheet M is entirely elementary top C-face
loops, and there are no higher active sheets. Hence every essential
label satisfies j_i<=M-1=c_right. The integer walk stays at or below
c_right. Equation(2) then says that EVERY local up/down peak of that
walk is exactly the ceiling c_right.

Writing U=+1 and D=-1, its sign word consequently has the form

    D^a U^(a+1) (D^b1 U^b1) ... (D^br U^br),

where a>=0 and every b_k>=1. This is a contour grammar, NOT a turn-word
grammar for the actual ant. It allows arbitrarily deep valleys and
arbitrarily many ceiling returns.

By equation(1), a global maximum C face at M can occur only in a band
whose base is c_right. These are exactly the high +,- ceiling bands
and the final RIGHT outer region. All other bands have C height<=M-1.
At the boundaries of each ceiling band, the C>=M contact barrier
confines an entire maximum C component there. Therefore its canonical
max-face parent edges, branches and source suppliers C=M cannot jump
to a DIFFERENT essential band. Cross-Gamma transfer within the SAME
ceiling band or maximum component remains open and must be retained.

## 7. Scope

The level walk and high-band localization are exact structural necessary
conditions, not an attained complete-front construction. They do not
bound the number of bands or face-patch exchanges, forbid positive odd
defects, make a spatial decrease a chronology contradiction, or supply
an initial-fuel upper bound. The actual single-cursor exchange order
within each band remains the main unresolved assembly obligation.
