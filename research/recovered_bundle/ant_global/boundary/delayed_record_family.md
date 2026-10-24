# A fixed active boundary can hide an arbitrarily long delayed record

21 October 2026. This is an exact computer-assisted obstruction to a proposed
global inference, not a counterexample to Langton-ant highway capture. The
finite certificate proves an entire family indexed by n>=0. It does not infer
the family from a finite sample of n values.

## 1. Statement

Use headings E,S,W,N and the white-right, black-left ant rule. Start at
(0,-7), facing N. For any integer n>=0, make the following five cells black:

    (1,-7), (-1,-6), (-3,-6), (-2,-5),
    q_n=(-18-2n,13+2n).

All other cells are white. Normalize the eventual parallel highway's upper
cap as T: x+y=0, with A,B,C at levels -1,-2,-3.

All members of this family reach the same adaptive record cut at time 83.
At that time:

* the ant is at (0,-4), facing E;
* T and A are entirely white;
* B has exactly one black cell, (1,-3);
* C has exactly one black cell, (1,-4).

The marker q_n is on level -5, strictly below C. The full configurations at
time 83 differ only in that marker's position. In particular their entire
four active rows and their ant poses are identical. Their inherited active
energy is

    Q=4 b_B-b_C=4-1=3.

The first exit above T occurs at exactly time

    970+104n.

The next adaptive record cut is at time 967+104n. On the interval between
the two cuts, the top and A counts are

    M=17+2n,
    N_A=59+7n,
    Delta_A=9+n.

Thus the inherited energy at the next cap is exactly

    Q_next=4M-Delta_A=N_A=59+7n.

Consequently there is no finite upper bound on Q_next that depends only on
the current Q, the full current four-row color configuration, and the ant
pose. Even the number of initially black cells is fixed at five in this
family. The position of the lower marker supplies the missing information.

This does not rule out a global budget that retains the old rows or their
geometry. It does rule out closing the current four-row recurrence by
assuming that those active data determine a bounded next energy.

## 2. What the finite certificate checks

The executable certificate is `certify_delayed_record_family.py`; its retained
output is `delayed_record_family_certificate.json`. It uses exact coordinates,
integer arithmetic, and literal ant updates. There is no optimization solver,
timeout, random choice, or floating-point comparison in the proof.

First omit the marker and use the fixed four-black seed. Directly perform
182 updates. From that state the following 104-letter word repeats forever:

    LRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLR

Its displacement is d=(-2,2), and its heading is restored. Its top level is
zero. The finite prefix before time 182 also stays at or below zero.

The certificate proves the infinite repetition by the translation-orbit
argument in Section 3, rather than by replaying a large number of periods.
There are 312 exact read-color checks: 104 phases at each of the only three
relevant period indices 0,1,2. For every larger index the formula has already
stabilized. Thus the periodic baseline is proved from time 182 onward,
including the first member n=0 of the marker family.

For the baseline, q_0=(-18,13) is first read at time 852. For every n>=0,
q_n=q_0+n d is first read at time 852+104n. This follows by checking the
finite prefix and all translation classes of the 104 periodic phases.

Next add q_0 to the original seed and replay the path from time 852 until
time 970. The path takes 118 updates and reads 61 different cells. All
processed events before time 970 remain at level at most zero; the head
after update 970 is at (-9,10), facing N, at level one. Hence this is the
first cap exit for n=0.

Finally, on each of those 61 cells, the baseline color at time 852+104n,
translated back by n d, is exactly the baseline color at time 852 for every
n>=0. Section 4 gives the finite-threshold formula. Its last threshold is
zero for this footprint, so 61 exact checks prove the claim for all n.
The marker is translated by the same n d. Determinism therefore makes the
whole 118-step perturbed suffix translate exactly, proving the exit time
970+104n for every member of the family.

## 3. Proof that the baseline word repeats forever

Let B_0 be the finite black set at time 182, and let p_i be the position at
phase i of the proposed period, for 0<=i<104. Let c_i be the black/white read
specified by the displayed word. The candidate position at period k and
phase i is p_i+k d.

For two phases i,j, write p_j=p_i+m d when such an integer m exists. The
phase-j visit in an earlier period hits p_i+k d exactly when:

* m>0 and k>=m; or
* m=0 and j<i, within the current period.

No other earlier phase can hit that cell. Therefore the candidate read color
is exactly the initial indicator of p_i+k d in B_0, XOR the number of these
earlier hits modulo two.

For fixed i this formula changes only at finitely many k: the positive m
values from the 104 phase positions, and the indices of the finitely many
initial black cells on the forward ray p_i+k d. The certificate finds that
checking k=0,1,2 reaches or exceeds every last change, including the index
after the last possible initial-black intersection. At all 312 pairs (k,i),
the color equals c_i. Beyond k=2 the formula is constant at every phase.

Induction on actual event time now proves that the candidate trajectory is
the true ant trajectory for all k>=0. Its geometric displacement and heading
were verified by the same 104 literal updates. This proves the baseline
without an infinite simulation assumption.

The first-hit assertion for the marker is checked by the same orbit method.
No pre-period event lies on q_0+n d for any n>=0. Every phase whose orbit
contains q_0 gives a nonnegative period index for that hit. The least time
is 852. Translating the target to q_0+n d increases every such hit time by
104n, and cannot create a pre-period hit.

## 4. Proof that the perturbed suffix translates for all n

Write 852-182=104 k_0+r, with 0<=r<104. Fix any cell v in the 61-cell
perturbed suffix footprint. At baseline time 852+104n the target cell is
v+n d.

For a periodic phase j, write v=p_j+m d when possible. Its visit to that
target is in period m+n. It has occurred before the impact time exactly when

    m+n>=0,
    and either m<k_0, or m=k_0 and j<r.

The second condition is independent of n. The first changes only at the
threshold n=-m. The remaining initial-color term is the indicator that
v+n d belongs to B_0, which also has finitely many possible changes.

The certificate computes every one of these thresholds for all footprint
cells. For this example the last relevant nonnegative threshold is zero.
At n=0 the formula agrees with the directly replayed baseline board at time
852. Thus it agrees for every n>=0. This includes the cell at the first
impact; adding the marker flips that one initial suffix color in every
translated copy.

It follows by induction over the 118 suffix updates that the n-th marked
trajectory follows the n=0 suffix shifted by n d. The path before impact is
the baseline, since the marker has not yet been read. Both prefix and suffix
stay under the cap until their translated final exit, so there is no earlier
exit omitted by the argument.

## 5. The two adaptive cuts and the energy calculation

The baseline's first black top read on the preceding cap x+y=-2 occurs at
time 85. Its previous A event is white, so the prescribed adaptive cut is
85-2=83. Direct replay gives the pose and active rows in Section 1. All
markers are first read much later and are below these four rows, so this
cut and its complete active state are common to all n.

For the marked trajectory, the black T event immediately before its first
exit is at time 969+104n. Its preceding A event is white. The next adaptive
cut is therefore 967+104n and lies on B, at

    (-10-2n,8+2n), facing E.

Direct replay for n=0 gives M=17, Delta_A=9, and N_A=59 between the cuts.
Each extra baseline period before the delayed impact contributes M=2 and
N_A=7; the translated perturbed suffix contributes the same counts for all
n. The initial cut is fixed. Therefore

    M=17+2n, N_A=59+7n, Delta_A=4M-N_A=9+n.

These are genuine consecutive record intervals. The marker has changed a
later return to the old substrate while leaving the initial active cap data
unchanged. This is exactly the information that the four-row ledger alone
cannot bound.

There is a further exact distinction between active energy and nonstandard
motion. The standard cyclic word has 84 different ten-letter factors. Among
all ten-letter windows wholly before the first cap exit, the n=0 trajectory
has exactly 96 windows outside this set. Every larger n inserts whole copies
of the standard period into an already periodic part of the prefix; the two
junction phases stay the same. Consequently this count is exactly 96 for
every n>=0, while Q_next=59+7n is unbounded. In this family the added active
energy records standard motion. This statement makes no claim about windows
after the first exit or about the total number over the infinite future.

## 6. Limit of the result

The family gives arbitrarily long finite delays and arbitrarily large next
active energies. It does not give one seed with an infinite sequence of
such delays. It does not prove that these five-black seeds fail to settle
into highways later. The general highway conjecture remains unresolved by
this result.
