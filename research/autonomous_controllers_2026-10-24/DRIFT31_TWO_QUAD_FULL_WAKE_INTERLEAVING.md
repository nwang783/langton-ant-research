# Exact full-wake interleaving in the live two-quadruple F-circle branch

24 October 2026. Author symbolic all-parameter calculation, submitted for
independent review. This is a necessary parameter restriction, NOT a complete
front exclusion or realization. It concerns the single-used FIRST-R circle
with TWO quadruple breaks at full drift(3,1), not an already excluded E circle.

## The live full-inventory family

The circle-shape cover102da4e3 gives the complete T=0..5 histories
S,W,S,EEWE,SSNS,EEW in its two-quadruple case. The separate middle-read
cover92380db9 forces T6=NNN and T7=EEEW. At g8, their odd classes are exactly
T={0,1,2,5,6}. The full single-used-circle support is to its RIGHT, so every
other read class is at T>=6; the named complete histories at6 and7 are retained.

In x-fibres modulo3, the signed remaining odd demands have minimum absolute
sizes1,2,0 at residues2,1,0 after subtracting those five named odd classes.
There are exactly THREE odd classes still available, so each demand is tight:

- One negative-checker class at T=6a+1, where a>=2 because T7 is complete/even.
- Two equal-checker classes at T=6b+s and6c+s, where s=2 or5 and1<=b<c.

Thus every front in this live branch has candidate FULL odd inventory

    O_T={0,1,2,5,6,6a+1,6b+s,6c+s},
    a>=2, 1<=b<c, s in{2,5}.                             (1)

Physical representatives are(-T,0), and the actual FULL drift is(3,1).
The set(1) is the entire eight-class inventory, not a partial emitted subset,
a proposed initial BLACK seed, or a second physical wake manufactured by
subtracting the circle. The middle-read cover's independent status is a
separate premise for the application. The family calculation below is valid
for the explicit sets(1) whether or not any ant realizes them.

## Exact period-free character

Use the retained general non-axis quadratic wake obstruction in
`../sources/kehao95-core/wake_synthesis/verification/general_wake_parity/PROOF.md`.
It requires winding Omega=1 and quadratic port sign q=1+3=0 modulo2.
Its signed-residue, geometric port, and author attribution are retained.

For(1), canonical coordinates are

    r0: y=0,2;
    r2: y=1,2a+1;
    r1: y=1,2,2b+delta,2c+delta,

where delta=1 for s2 and delta=2 for s5. The signed x-fibre sums are
(2,+/-2,-2), and the sole y-fibre sum is+/-2. All are2 modulo4. The canonical
y sum is odd, so Omega=1 for EVERY parameter choice. These are direct identities,
not sample-screen results.

The exact quadratic sign is

    q=0  if b<a<=c;
    q=1  if a<=b or a>c.                                 (2)

Therefore any complete front in this branch must have the negative-checker
class6a+1 strictly between the two same-checker classes6b+s and6c+s in normal
order. This is only a NECESSARY interleaving. There is no proved chronological
ordering incompatible with it, so the branch remains open.

## A finite symbolic certificate, independent of gap size

There are three endpoint-order regions. Each is parametrized by unrestricted
u,v,w>=0 integers, with no omitted boundary equality:

    a<=b:      a=u+2, b=u+v+2, c=u+v+w+3;
    b<a<=c:    b=u+1, a=u+v+2, c=u+v+w+2;
    a>c:       b=u+1, c=u+v+2, a=u+v+w+3.

The full odd-edge graph consists of horizontal intervals pairing consecutive
sorted T values, and vertical intervals pairing consecutive canonical y values
within each x fibre. Direct symbolic application of these geometric endpoint
formulas produces arithmetic edge runs. EVERY run here has step2; its length
and source/target endpoints are integer affine forms in u,v,w. Zero-length
runs are explicitly allowed as empty, not discarded by a numerical cutoff.
All run lengths are nonnegative affine forms on the stated region.

For two runs A,B the source/target port-order inversion thresholds differ by
at most a fixed unit-edge constant. For each eligible integer difference z,
the number of pairs with source_y(A)-source_y(B)=z is exactly the number of
points in the overlap of two step-two intervals. After parity matching it is

    max(0, (min(end_A,end_B+z)-max(start_A,start_B+z))/2+1).

The numerator is even. Thus every pair-inversion term is an exact piecewise
AFFINE function, with no expansion proportional to the unbounded gaps.
Summing these terms and adding the positive-edge count plus odd C-vertex count
is precisely the retained definition of q. The C count is always odd.

Every affine min/max choice is certified by a componentwise nonnegative or
nonpositive difference on its nonnegative-integer parameter domain. Where a
boundary value needs separation, the certificate splits one variable into its
current minimum value versus at least the next integer. These two children
cover the whole domain exactly. The six sign/order cases close in TEN total
tree nodes and EIGHT leaves. At every leaf the final affine parity coefficients
of all free variables are even, and the constant is exactly the value in(2).
All comparisons, branch domains, runs and final affine expressions are stored.
No solver UNSAT claim, fitted polynomial, interpolation, or bounded parameter
sample is a premise. Literal compressed-screen comparisons, including enormous
gaps, are retained only as controls.

## Passing inventories are not controllers

For example a2,b1,c2,s2 gives the complete candidate odd set
{0,1,2,5,6,8,13,14}. The retained screen returns NOT_EXCLUDED: its signed
residues, winding and quadratic character all pass. This does not mean it
extends the complete read histories or yields a finite-seed controller.
Indeed a separate later top-boundary check may still exclude a passing
inventory; the present calculation never promotes screen sufficiency.
A less tightly packed passing example is a2,b1,c3,s2, giving
{0,1,2,5,6,8,13,20}; no complete chronology is supplied for it either.

The exact calculation is in `certify_drift31_two_quad_wake_interleaving.py` and
`drift31_two_quad_wake_interleaving_certificate.json`. Direct theorem, source,
code and certificate hashes are bound in `DRIFT31_WAKE_INTERLEAVING_SHA256SUMS`.
No publication, external priority claim, all-front g>=12 conclusion, or
finite-seed attraction claim is made.
