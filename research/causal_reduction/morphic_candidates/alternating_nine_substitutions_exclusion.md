# Two alternating scale-three substitutions: exact finite exclusion

Status: source computation complete; independent replay requested. This is a
bounded-family theorem, not an exclusion of arbitrary multiscale controllers.

## Class and statement

Let phi and eta be substitutions on the two letters R,L. Each image has length
nine. Starting with incoming heading N, each R image has endpoint (3,0),
heading E, and each L image has endpoint (-3,0), heading W. No assumption is
made that eta's images or its intermediate infinite curve are ant-legal.

There is no standard-ant turn word on ANY initial coloring that is a
prolongable fixed point of the composite substitution phi o eta. Both possible
root letters are included. Consequently this class supplies no finite-seed
aperiodic counterexample.

This is genuinely broader than requiring a turn word to refine itself at
scale nine: the composite has length 81 and spatial scale nine. An intermediate
coarse curve can fail the ant's alternation rule. It is also outside the earlier
single-substitution enumeration through length 17.

## Reduction and exact certificate

Enumerating all 512 nine-letter words gives 24 geometric images for each of R
and L. Every such image contains both letters. Thus every composite fixed
point uses both outer images. If either outer image repeats a read at a cell
with the same turn, that occurrence itself is impossible on any coloring.
Requiring internal alternating reads leaves exactly nine outer images for each
letter. No such filter is applied to inner images.

There are therefore 81 outer substitutions and 576 inner substitutions, or
46,656 ordered phase pairs. Retain each root z for which (phi o eta)(z) begins
with z. This produces 49,248 rooted cases. For each case, expand the root to
6,561 letters, the square of the composite length. Replay the path and record
its first occurrence of two consecutive visits to one cell with identical
turns. Initial colors are unrestricted; such a conflict is an exact obstruction
on every initial coloring.

Every case has a conflict, and the latest is at zero-based time 201. Therefore
only the first 202 reads are actually needed, although the common generated
prefix is longer. The JSON preserves every root, phase index, conflict cell,
previous visit time, conflicting visit time and turn. No timeout, search cap,
solver, heuristic rejection, or UNKNOWN status occurs in this result.

The complete record digest is
4a3a57b3e23f0d0ca57e84fbfc55626855490099c41d261669ffa460b4067f15.

Source and certificate:

- probe_alternating_nine_substitutions.py
- probe_alternating_nine_substitutions.json

## Scope boundaries

This does not exclude three or more alternating phases, substitutions on a
larger control alphabet, different geometric scales, occurrence-dependent
images, orientation-reflecting refinement, or arbitrary finite seeds. Roots
that are not prolongable for this composite do not define a fixed point of
this composite; squaring a first-letter two-cycle would be a different,
four-phase class and is not silently included.
