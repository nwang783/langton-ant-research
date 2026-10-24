# Modulo four is sharp for the unit-winding signed-turn cocycle ansatz

24 October 2026. Analytic author result for independent review. This is a limit
of a specified proof method, not an impossibility theorem for other invariants.

## Precise ansatz

Let w(T) and psi(T,incoming heading) take values in Z/mZ, on every allowed
incoming-axis state for T=3y-x. Suppose the same identity holds for EVERY right
and left move from every such state:

psi(after)-psi(before) = w(T)*sigma - delta_y,

where sigma is +1 for R and -1 for L. No period in T is required. Thus a
heading-restoring path of displacement(3,1) has zero endpoint potential change
and gives sum w(T)*sigma=1.

Then m must divide4. In particular, simply increasing the positional period or
using modulus8 cannot strengthen the unit-winding congruence within this ansatz.
The previously supplied explicit modulus4 potential shows the bound is attained.

## Local proof

At an even-T vertex, denote its N and S incoming potentials by A and B, and
its E and W successor-state potentials by E and W. Horizontal moves have no
vertical displacement. The four allowed transitions give

E-A=w, W-A=-w, W-B=w, E-B=-w.

The first and fourth equations imply B-A=2w; the second and third imply
B-A=-2w. Hence4w=0 at every even-T vertex.

At an odd-T vertex, write A,B for incoming E,W and N,S for the two vertical
successors. The equations are

S-A=w+1, N-A=-w-1, N-B=w-1, S-B=-w+1.

They again give B-A=2w and B-A=-2w, hence4w=0 at every odd-T vertex.

Finally the literal turn word RLRRLL starts incoming N, restores N and moves
by(3,1). Its normal coordinate returns exactly to its starting value. Summing
the cocycle gives1 as a signed sum of weights w, each annihilated by4.
Therefore4=0 in Z/mZ, or m divides4.

## Scope

The argument uses a universal move identity, not board legality, first colors,
visit caps or trajectory periodicity. The six-step path can be geometrically
used even without assuming a finite-seed infinite controller.

It also works for position-dependent weights and potentials periodic under
full displacement(3,1), by comparing the same four successor states at each
physical vertex and then following that displacement path. It does NOT cover
potentials depending on chronology, local visit rank, the evolving board,
nonlinear products, or extra terms retaining actual multiplicities. It does
not preclude stronger mod-eight chronological identities such as the retained
all-multiplicity residue theorem.

For nonprimitive full drifts the winding coefficient may not be a unit; this
note makes no analogous modulus bound there. Its purpose is to avoid an
unproductive higher-modulus search in this exact linear signed-turn family.
