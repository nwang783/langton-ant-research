# Exact chronology for a moving recursive hairpin

2026-10-23 05:52 UTC. Executed exact certificate independently audited at05:58 UTC.
`hairpin_presburger.py` hash:
eae46d759b779bc5231e9895dbde53871c257416a56ab491701c751f0f42a22a.

## Scope and contract

Supply R/L words U,V, one parent turn c and its incoming heading h. Require
U to return its heading to h, V to return the post-c heading to itself, and
net(U)=q=-net(V) with q nonzero. The finite word at depth r>=0 is U^r c V^r.
No image-length or recursion-depth cutoff is used. The solver decides its
internal ant legality at ALL r and computes exact first-read black requirements.

Internal legality means that the turns at successive reads of each individual
cell alternate. It allows a different entry board at each r. A positive result
is NOT a single finite board realizing all r, a growing prolongable root, or
an infinite ant counterexample. The final-black formula is an actual board
transition only on legal instances, starting from the minimal first-read board.

The system libisl performs exact integer relation operations. Resource failures
raise errors and are never interpreted as empty bad-depth sets. An initial
general time-relation implementation hit its operation cap; it was replaced by
the finite spatial-coset decomposition below, not accepted as a negative result.

## Finite spatial-coset proof

Put a=|U|, b=|V|. The reads in each slot of U, the single c, and each slot of V
form families at positions l*q+p. After choosing one representative p0 for each
coset modulo Z*q, write p=p0+k*q and use z=l+k as the common cell coordinate.
Because q is nonzero, a fixed (r,z) has at most ONE read from each slot family.

The exact family domains and times are:

- U slot j: 0<=z-k<r; time a*z+j-a*k.
- central c: z=r+k; time a*r.
- V slot j: 1<=z-k<=r; time (a+b)*r-b*z+1+j+b*k.

All formulas are affine in r,z. Two same-turn families form a bad consecutive
read exactly where both are present, the first time is smaller, and every
other family is absent or not strictly between their times. The implementation
subtracts the finite union of those intermediate-family domains and existentially
projects z. The resulting Presburger set is exactly ALL bad r.

A first-read family has no earlier present family in its coset. Its L domains
map to the exact minimal initial black set. Analogously, the last-read R domains
give the final black set on legal words. The union of all domains gives read
support. Distinct cosets cannot interact, and the finite list exhausts all reads.

## Executed results on the existing21/29 primitives

The input inventory is precisely the constructor's nine eligible nonzero-offset
same-physical-parent decorations from three previously retained legal words.
No longer-word search or new palette was run.

Eight cases have bad-depth set exactly {r:r>=2}. The remaining R21/read14 case is
internally legal for EVERY nonnegative r:

    U = LRLLLLRRRRLRRL,
    c = R, incoming N,
    V = RLRRLL,
    q = (-1,3).

The exact verifier also checks all-r set equality with the constructor's tiles:

    I={(-2,0),(-2,1),(-1,1),(-1,2),(0,0),(0,2)},
    O={(-2,1),(-2,2),(-1,0),(0,3),(1,1),(1,2)}.

The input is union_(0<=i<r)(I+i*q); the output is
union_(0<=i<r)(O+i*q) together with {r*q}. The read-support tile J is saved
explicitly in the JSON and likewise verified symbolically with the far cap.
The twelve J points have distinct values of3x+y from-6 through5.

Consequently the initial/final masses are6r and6r+1, the complete XOR has
10r+1 cells, the read support has12r+1 cells, and the duration is20r+1. These
counts also follow from the constructor's independent direct history table in
`causal_reduction/unit_scale/decorated_oblique_hairpin.md`.

All225 literal depth controls r0..24 for the nine families match both the
bad-depth decision and COMPLETE first-read black sets. Those finite controls
supplement the exact all-r relation operations; they are not the certificate.

## What this positive control establishes

A nonzero-offset decorated recursive state is not an empty formal escape:
there is an actual all-length legal outbound/return family on linearly prepared
boards. The required fuel grows as6r, and the recursive label is interior rather
than prolongable. A self-supplying finite-support construction still needs a
separate mechanism to prepare or transform those boards and maintain one actual
root trajectory. No such mechanism is provided here.
