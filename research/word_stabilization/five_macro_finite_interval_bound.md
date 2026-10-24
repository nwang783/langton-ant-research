# Quantitative bound for finite five-macro factors

Let a physically feasible finite word start and end in a non-C macro and
satisfy the audited internal C-gap grammar. Every C-run then has length1 or2
and is followed by V, so the completed-C packet theorem applies. Let m be
the black-cell count at this factor's entry and r its number of C-runs.

There is no such nonempty factor for m<6. Otherwise

    r <= m-6.

Indeed every first-C input is a distinct entry-black cell. They are disjoint
from the first non-C macro's first-L inputs, since those inputs have already
been read before any of the marked C inputs. Every non-C macro needs at
least6 first-L cells (V realizes the minimum).

Split the word into r+1 nonempty C-free segments separated by the C-runs.
Write M_j for the black count entering segment j, with M_0=m. Its exact fuel
cost is c_j=5u_j+2v_j+15q_j+18b_j, and c_j<=M_j-4. Its mass gain is
4u_j+4v_j+6q_j+6b_j<=2c_j. A C-run adds at most6 black cells. Therefore

    M_(j+1) <= 3M_j-2,
    M_j <= (m-1)3^j+1.

The C-free segment takes at most9c_j ant steps, because its block lengths
28,18,64,74 are bounded by9 times5,2,15,18 respectively. The C-runs take at
most30r steps. Thus the whole factor has at most

    (9/2)(m-1)(3^(r+1)-1) + 3r - 27

ant steps, and at most

    floor(((m-1)(3^(r+1)-1) + 2r - 6)/4)

macros. Substitution of r<=m-6 gives explicit bounds depending only on m:

    steps <= (9/2)(m-1)(3^(m-5)-1) + 3m - 45,
    macros <= floor(((m-1)(3^(m-5)-1) + 2m - 18)/4).

These are deliberately loose but exact bounds, not simulation fits.

For an arbitrary finite feasible five-macro word, remove its initial C-run
(at most4 macros, adding at most12 black cells) and its final C-run (at most3
macros after a non-C). Apply the bound to the remaining non-C-ended core,
using its actual entry mass, or conservatively m+12. Add at most105 ant steps
for the removed C macros. A word containing only C has length at most4.
The bounds also apply when additional read constraints come from actual H
ports, because those constraints only shrink the feasible language.

This is NOT a bound on arbitrary ant trajectories, total forbidden-ten
windows, or the length of an interval that may traverse the standard W104
component. Such an interval can contain long ordinary highway motion.
