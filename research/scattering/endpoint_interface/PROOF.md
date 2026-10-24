# One old endpoint, four clean incoming tracks

Status: exact checker passed, independent review pending. This is a guarded
local scattering theorem, not a finite-state reduction of all Langton-ant
trajectories.

## A reusable finite interface

Let H={x-y<=0}. Let K be the explicit387-point set saved as
reduced_common_cap in common_cap_certificate.json. For a pose p,h and canonical
word phase j, C(p,h,j) means the mature canonical NW highway configuration at
that pose, restricted to H. It is a finite set: the active core plus the finite
portion of its southeast trailing deposits still in H. The canonical construction
is implemented exactly by canonical_clip; it uses the standard13-cell core,
12-cell per-period deposit, cyclic104-word, and a180-degree rotation.

For each of the following four inputs, K and C are disjoint. Start with black
set K union C(p,h,j) in H, and ANY black configuration outside H:

* Input28: p=(9,55), h=N, phase102. After642 steps: (-32,72),N,phase100.
* Input38: p=(1,41), h=N, phase0. After926 steps: the same output.
* Input60: p=(6,67), h=E, phase99. After11133 steps: the same output.
* Input75: p=(9,54), h=E, phase99. After523 steps: the same output.

In every case the output is a permanent standard NW highway. Every read of
the finite recovery and the infinite tail stays in H. The respective maximum
read u values are-46,-40,-8,-45. Consequently the rule is insensitive to all
outside-H changes, not merely to a bounded set or a finite sampled distance.
The input seed sizes within H are552,528,601,553.

The arbitrary external configuration may be finite, as required for the
original problem, or even infinite without affecting this local theorem.
Translations and rotations give the corresponding transported guarded rules.

## Why this is the actual old endpoint

Normalize the old a-corner by subtracting A_n=(-2n,2n). For every m>=100 and
n-m>=100, exact restriction of the complete old q+a+c history to H is one
constant2458-point field K_full. No history is discarded before restriction:
every finite point and every finite deposition ray is retained in the affine
field. A point is dropped only after proving u>0 uniformly. A ray is either
uniformly outside H or its exact intersection with H is reduced to a constant
interval in a (z,x modulo2) class. There is no z cutoff. An injected point at
(10^60,10^60+1), still inside H, is correctly retained.

At the final endpoint checkpoint of the four third-band full-history families,
the complete field restricted to H equals exactly K_full XOR C(p,h,j).
All retained-core and unrelated remote histories are on the positive-u side.
The new highway's deposited segment supplies precisely its canonical incoming
state inside H. The four prescribed recoveries and final tails are then checked
against these finite fields by literal read/color replay and exact infinite
ray-intersection certification.

K is K_full intersected with the union of the complete read sets of all four
certified executions. Deleting the other2071 old black points therefore changes
none of the four trajectories. The checker also freshly replays all four
reduced kernels, rather than relying solely on that deletion argument. This
is a minimum deletion-only common subset preserving all four specified words;
it is not a claim of the smallest cap that could realize the same outputs via
different transients.

## The full interface is not renewed

At the output, factor out the outgoing canonical configuration C_out within H.
The residual finite fields have774,636,1228,774 black points, respectively,
rather than387. Their XOR differences from K have589,585,1295,589 points.
The checker saves each exact update, not merely its cardinality. The residual
is disjoint from the entire certified outgoing read set, so capture follows.
Every tail also rejects a newly inserted marker10^60 periods ahead.

Thus the endpoint's four inputs have a common output front but do NOT restore
the same complete residual cap, even up to translation, under this explicit
canonical-front factorization. The earlier provenance example is consistent:
its first triggering bit is restored to black, while many other bits change.
This does not rule out renewal after quotienting by rigorously irrelevant
memory, or renewal in a different interface encoding. It certainly does not
prove that all future possible arrivals would ignore the residue.

## What a compositional graph would still need

A finite macro word w has a read set R(w) and an odd-write set D(w). Starting
from a certified field F, any additional XOR field E disjoint from R(w)
leaves that word unchanged, and the final field is F XOR E XOR D(w).
For an infinite translating tail, replace R(w) by its whole infinite read set.
This is the exact environment-independence lemma used here.

To compose rules into a sound finite interaction graph, one must therefore:

1. Specify the complete interface field, pose and incoming phase for every node.
2. Carry every side-effect field into the next node, or prove it misses that
   next node's whole certified read set. A scar irrelevant to the last output
   is not automatically irrelevant to a later return from another direction.
3. Prove coverage of every reachable interaction, including old endpoints and
   nonstandard or preinstalled rails, rather than only pristine local models.
4. Supply a well-founded rank for every noncapturing transition, or separately
   exclude all recurrent/renewable circuits in the closed interaction system.

The four rules establish a real common local interface and exact update laws.
They do not establish closure, a decreasing resource, or absence of renewed
circuits. In particular, counting consumed old triggering black bits cannot
serve as that missing rank.

## Reproduction

Run certify_common_cap.py. Its affine history dependency is
return_nw_frontier/full_field.py and its four completed templates/certificates.
The generic four finite-kernel capture rules are separately replayed literally
inside the checker. All input/output data, residual updates, provenance hashes,
and negative controls are saved in common_cap_certificate.json.
