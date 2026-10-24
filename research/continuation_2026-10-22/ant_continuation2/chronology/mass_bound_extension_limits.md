# What the mass-five theorem leaves for a general mass bound

The theorem in **eventual_mass_five.md** excludes recurrent mass four. Its
scattering argument has a specific starting advantage: after fixing the
checkpoint pose, all four current black cells escape every bounded set. The
complete forward input therefore approaches the blank input locally.

There is a general version of this observation, but it does not provide an
induction from one eventual mass bound to the next.

## A local-limit lemma

Suppose a finite-seed trajectory has infinitely many checkpoints with mass
at most K. The axial separator bound permits an infinite fixed-pose
subsequence. Normalize that pose to `(0,0),N`. The four critical clocks tend
to positive infinity along this subsequence.

The two z-clocks have positive field terms precisely at the `chi=-1` cells.
Their divergence forces one such cell to have z arbitrarily large positive
and another to have z arbitrarily large negative. The two u-clocks similarly
force two distinct `chi=+1` cells with u tending to opposite infinities.
For every fixed finite box, at least four distinct black cells are therefore
outside it at every sufficiently late checkpoint.

By a diagonal subsequence on finite lattice boxes, the checkpoint fields
converge locally to one fixed field C: on each fixed finite set, their bits
are eventually exactly those of C. The mass bound makes C finite. The four
escaping cells prove

    |C| <= K-4.

For each fixed finite time interval, the checkpoint trajectory then agrees
with the trajectory started from C at `(0,0),N`, for all sufficiently late
checkpoints. Indeed, that input trajectory reads only finitely many cells
in the fixed interval; local equality on those cells gives exact coupling.

This is an analytic consequence of the clock and endpoint theorems, with no
simulation premise.

## Why the blank baseline stops at K=4

For K=4, the lemma forces C to be empty. This is exactly the blank-prefix
reduction used in the mass-five proof.

For K=5, C may have one black cell. This is compatible with all current
endpoint tests. For example, take the four rectangle corners

    {-2n,2n+1} x {-2n+1,2n+2}

and add the fixed cell `(0,0)`, keeping the head `(0,0),N`. The four corner
fields have diverging positive critical clocks and zero signed charges on
each occupied remote row and column, as verified analytically in
**low_mass_recurrence.md**. The fixed extra cell changes each clock by a
constant and only changes the fixed central row/column residues. Thus these
five-cell endpoint states still satisfy all those necessary conditions.
They have local limit `{(0,0)}` and start with a left turn. They are not
claimed to occur as successive states on an actual orbit.

Known one-black capture gives a standard baseline for each such fixed C.
That does not automatically give the next scattering reduction. A distant
exceptional hit may return to the complete debris of that one-black parent;
the two fixed parent templates used in the mass-five proof cover the blank
parent and its particular exceptional descendants. They do not cover
arbitrary one-black historical residue or every placement of the remaining
four cells. These would be concrete new certificate and coverage obligations.

At K=6 the local core can have two cells, so the external two-black theorem
could similarly provide a baseline if its required results are imported and
verified. The same interaction and coverage obligations remain. From K=7
onward even the local core can be a three-black input, whose general capture
is not established by the present work. More generally, a core of K-4 cells
may itself be any unclassified finite input.

An eventual mass lower bound does not classify those parent trajectories.
It only says that they eventually acquire more black cells. Consequently a
mass-bound induction cannot be substituted for a highway-capture induction.
Even a proof of `M_t -> infinity` would still need a further argument to
force the standard turn word. No such general interaction closure or
eventual-language theorem is supplied by the mass-five result.
