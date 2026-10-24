# Moving endpoints with permanently recycled bulk: a finite certificate target

Status: independent analytic audit passed22 October2026. No moving-endpoint candidate
or finite-seed counterexample is known. This is a verification architecture,
not a convergence theorem. The audit covers the explicit finite-arm gluing hypotheses, not any candidate.

## Why ordinary translating-front chronology is not the right model

In an expanding out-and-back rail builder, an old bulk cell is read on every
later lap. It has infinitely many reads even though the right endpoint moves
east. Thus the usual finite list of reads per translation class is not itself
an adequate certificate. The complete history is instead a finite transient
followed by a periodic read string.

Fix a positive horizontal endpoint drift D=(d,0). A packet contains finitely
many fixed finite cap words and finitely many horizontal half-arms. Each arm
is a heading-returning finite word with nonzero horizontal drift, repeated
away from its endpoint toward x=-infinity. Its within-packet chronological
order is toward the endpoint for an incoming arm and away for an outgoing
arm. Cap words and arm endpoints must be geometrically joined. Between two
successive arms at the remote left boundary, a separate controller is to be
provided; no teleporting autonomous ant is claimed.

Translate the entire packet by nD on lap n. Every packet's read set is bounded
on the right and lies in a fixed finite set of rows. For each representative
p=(r,y),0<=r<d, let H_n(p) be the finite ordered string of turns read at
p-nD in the untranslated packet. Within each arm, the integer period index
orders its reads; packet stage orders different arms/caps. Literal phase
positions determine H_n without assuming any colors.

Then:

* H_n is empty for all sufficiently negative n, because the packet is bounded
  on its right.
* For all sufficiently positive n, finite caps are absent and H_n is periodic
  in n. A valid period divides the least common multiple of
  |a|/gcd(|a|,d), over all horizontal arm drifts(a,0).
* Both thresholds and a valid eventual period are computable from the finite
  footprints and cap extrema. Only finitely many rows and representatives
  need be checked.

Consequently, the concatenated complete read history

    ... H_-1(p) H_0(p) H_1(p) ...

starts R and alternates if and only if an explicitly finite transient check
and one eventual-cycle check pass. If the eventual cycle is nonempty, its
concatenated turn string must alternate cyclically, hence have even length.
An empty eventual cycle simply leaves a finite history to check.

This criterion is exact for the ideal right-end history: a white cell can
follow the prescribed turns exactly when its first turn is R and successive
turns alternate. Different representatives encode every physical cell, and
translation merely shifts the lap index of its history.

## Conditional finite-arm gluing

A real builder truncates every half-arm at a fixed left boundary and supplies
finite left-end connector words or controlled boundary resets. Assume:

1. The geometric finite arm lengths and the finite connectors join correctly
   for every n>=0, all cells are visited finitely many times in each lap, and
   each lap has finitely many steps.
2. Outside fixed left and moving-right neighborhoods, the finite arms have
   exactly the automatic periodic bulk histories used above.
3. The complete fixed-left history is alternating, including cyclic joins,
   and its overlap with the bulk has the same phase colors.
4. The complete moving-right histories pass the first-R/transient/periodic
   test above. The two exceptional neighborhoods are initially disjoint.

Then a finite initial field realizes every lap. To see this, every cell ahead
of the initial endpoint has no negative-lap read, so its valid complete
history begins white. Only the finitely many cells in the initial finite
body and left fringe can have a missing negative-lap prefix. Seed each of
those cells with the bit required by its first actual read. Alternation then
proves the entire prescribed history by induction on actual read events.
The left and right conditions agree in their common automatic bulk, so there
is no conflicting initial assignment.

This is a conditional construction theorem. No connector or cap pair has yet
passed these conditions. For an autonomous counterexample, controlled resets
must additionally be removed, for example by the independently audited
half-turn-copy port-gluing theorem of the computability analysis.

## An immediate invariant filter

For any completed right-half-plane excursion from(0,r,E) to(-1,s,W), every
physical column's alternating black sum is conserved modulo4:

    C_x(B) = sum_y (-1)^y 1_B(x,y) mod4.

This strengthens mere black-count parity. Rotate the known row-charge formula
by90 degrees. For arbitrary a(x), choose A(x+1)-A(x)=a(x). The entry pose
correction is2A(0), while the exit correction is
2A(-1)+2a(-1)=2A(0), independently of r,s. The black-board sum is therefore
unchanged modulo4 for every a; choose a supported on one column.

Thus every settled new column and every complete moving-cap column beyond
the initial support must have alternating charge0 modulo4. A single solid
rail cannot grow with only a bounded translated cap and no compensating wake.
Two rails on rows of the same parity also fail. Two rails on opposite row
parities pass this necessary test, as do four same-parity deposits. Passing
it is far from sufficient for geometric realizability.

## Concrete bulk modes and remaining obligations

Let S=RLLR and W=LLRLRRRRLRRRRLLLLRLL. An east S sweep moves a solid row up1;
a west W sweep moves a solid row up3. Their reverse-complements are cyclic
shifts2 and6 of the same words, respectively. Rotated sweeps can therefore
restore the bulk in a second mode. To preserve the original pose sector,
reverse interfaces require an odd horizontal phase offset. Unlike a sparse
odd/even input rail, a solid rail has no bulk-color obstruction to that offset.

A possible target alternates an up4 and a down4 sweep and emits a compensating
opposite-parity rail as the right endpoint advances. The complete left fringe,
right cap, odd phase offset and all subsequent rereads remain to be supplied.
No such target is being treated as feasible merely because its bulk profiles
match or its modular charges vanish.
