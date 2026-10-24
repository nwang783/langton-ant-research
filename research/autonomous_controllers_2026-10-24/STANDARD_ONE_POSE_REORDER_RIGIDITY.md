# Standard104 is rigid under one-pose excursion reordering

24 October 2026. Exact finite-family author theorem, pending independent audit.
This is a bounded, structurally explained causal surgery result, not unrestricted
periodic classification or eventual-standardness of arbitrary finite seeds.

## The surgery family

Let W be the exact retained standard104 turn word. For EACH cyclic phase i,
start the word W_i at position(0,0) with headingN and trace its104 physical reads.
Record EVERY return to that same physical position AND heading within those104
reads, including the initial cut0. If the cuts are

    0=t0<t1<...<tk<104,

write A_j=W_i[t_j:t_(j+1)] and T=W_i[t_k:104]. Each A_j returns to exactly the
same pose. Replace the word A_0...A_(k-1)T by

    A_pi(0)...A_pi(k-1)T

for ANY permutation pi of these k complete excursions. All remaining reads are
unchanged. The empty or singleton excursion cases are included as controls.

This includes changing any subset of these slots while fixing the others, and
all physical root locations/cyclic period seams through the104 starting cuts.
It permits ONE chosen physical pose per surgery. It does not permit coupled
surgeries at multiple different poses, changed excursions, missing/new reads,
or longer windows spanning several full periods.

Because every excursion begins and ends at the same pose, its entire physical
read path is unchanged by moving it to another slot. Hence the FULL multiset
of (physical read cell, incoming heading, outgoing heading, turn) is identical
to W_i. Full drift, restored heading, length104, signed growth12 and all output
class counts are therefore unchanged. Only causal event order changes. This
is precisely a possible Euler-excursion rearrangement of the same spatial
controller, not a seed simulation or an arbitrary random word mutation.

## Complete result

There are47 starting cuts with no return excursion,31 with one,18 with two,
seven with three, and one with four. Thus the exact number of permutation
parameters is

    47*0!+31*1!+18*2!+7*3!+1*4! =180.

All180 resulting words are distinct. Exactly104 are cyclic phases of W; each
has the expected complete WHITE stable chronology. Every one of the OTHER76
has two consecutive equal turns in a complete physical drift-orbit history.
Consequently NONE of these76 can repeat forever on ANY static initial board,
even one with infinitely many prepared black cells. This is stronger than a
first-BLACK fuel rejection within this precise family.

The longest available excursion is92 updates, derived from W itself. This is
not a fresh arbitrary length escalation. Retained earlier studies permitted
short pose-return insertions at every standard phase, seven-site original-loop
replacement, and backbone mutations. This present claim is ONLY the explicitly
reconstructed one-pose reordering family; no claim is made that all its cases
were absent from every earlier larger test, or that it resolves those broader
families.

## Exact certificate and completeness argument

For every candidate word, trace q_j at phase j and its nonzero full drift d.
Choose one representative r for each class modulo Z*d and write q_j=r+k_j*d.
Complete visits to any far physical representative occur in increasing order
of the exact integer key j-104*k_j. Every physical ant toggles a cell at each
read, so consecutive turns in that complete list MUST alternate regardless
of the initial color. Each rejected candidate stores its actual class, the
adjacent conflicting phase/copy records, and the equal requested turn.

check_standard_pose_excursion_surgery.py independently checks each excursion's
literal pose, exhausts permutations (no solver or timeout), verifies the entire
spatial event inventory before classification, then builds all complete lists.
standard_pose_excursion_surgery.json retains every starting cut, the exact
return lengths, every permutation, every full candidate word, all76 explicit
contradictions, and the104 standard controls. Thus the finite enumeration
coverage and each rejection are separately auditable integer calculations.

The exact stable-list criterion is retained prior machinery, not a new checker
or a new general periodicity theorem. No finite-repeat heuristic is used.

## What this does and does not identify

This shows that these spatially conservative excursion swaps do not preserve
the standard controller's causal color obligations: the first/last inventory
and positive output alone leave room for abstract reordering, but every actual
nontrivial one-pose reordering in the stated family breaks a read alternation.
It does not show that simultaneous changes at different poses cannot compensate
those conflicts. It also does not classify another spatial event inventory,
other periods/drifts, inserted feeder paths, or nonperiodic finite-seed orbits.
