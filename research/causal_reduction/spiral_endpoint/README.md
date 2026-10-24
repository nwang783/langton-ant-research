# Exact continuation of the quadratic inward spiral

Status: independently audited computer-assisted all-parameter theorem,22 October2026. This is a family that DOES capture, not a proof
of the general conjecture and not an autonomous renewable circuit.

Start at the normalized final pose(0,0,N) and final black profile from
core_periodicity_new/quadratic_inward_spiral.md. For every n>=11, the exact infinite turn word is

    (RL)^n P V^(n-9) C W^n D H^infinity,

with literal words saved in family_words.json. Their lengths are

    P1540, V10, C22, W10, D1549, H104.

V=LLRLRRRRLL drifts(-1,-1), and W=RLLLLRLRRR drifts(-1,+1).
P starts at(n,n,N) and ends at(n-8,n-6,N). The first long sweep ends at
(1,3,N); C connects to(-2,2,S). The second sweep ends at(-n-2,n+2,S),
and D reaches(-n-13,n+6,W). H is a cyclic phase of the standard104 word
with drift(-2,-2). Thus standard capture occurs no later than22n+3021
updates after the inward spiral, or8n^2+36n+3021 updates from its original
11n+2-cell seed. This time is a guaranteed phase boundary, not asserted to
be the earliest capture time.

The first(RL)^n transfer is elementary from the seven-arm profile: each(j,j)
is white and each(j+1,j) is black for0<=j<n. It moves the outer NE arm onto
the main diagonal. The two later ten-step runs consume old diagonal arms;
they do not reconstruct the initial square perimeter.

## Exact finite reduction, including the infinite tail

The checker does NOT infer an all-n result from a long simulation. It constructs
an explicit incidence arrangement proving a finite set of representatives
covers every possible cell-history pattern.

Each initial-cell family and each read-phase family has the form

    cell(n,j)=a*n+b+v*j, 0<=j<c*n+d,

with an infinite upper bound for H. Constant families use v=0 and one event.
Every nonzero v in this certificate has nonzero x coordinate of magnitude1
or2. The block and phase indices specify chronological order. There are only
finitely many families; the source lists are generated from the literal words
and the exact seven-arm initial profile.

For a target event(n,j), membership in any earlier nonconstant source family
is determined by solving its x coordinate for its source index i. The resulting
conditions are:

- a congruence modulo abs(v_x), at most2 here;
- one linear equality for the y coordinate;
- linear inequalities0<=i<count(n);
- within the same repeated block, i<j or i=j with earlier phase.

A constant source gives two linear equalities. Thus the entire read color is
a Boolean function of signs/zeros of finitely many integer forms A*n+B*j+C
and residue classes of n,j modulo M=2. The checker collects a conservative
superset of these atoms, including all domain boundaries and both possible
same-block phase orders. Deduplicating identical geometric families is safe
for this arrangement computation: actual colors are still checked by the full
literal replay, not by a deduplicated parity sum.

For B!=0, an atom's zero set is a rational boundary j=alpha*n+beta. For B=0,
its sign is fixed beyond its last n root. The checker finds N such that for
n>=N every pair of nonparallel boundaries has a fixed order and is separated
by more than2M. Parallel boundaries maintain their exact spacing. Choose a
period P such that P*alpha is an integer multiple of M for every slope and
P is a multiple of M. For n in one residue class modulo P:

- every cluster of parallel boundaries translates by a multiple of M;
- all equality/boundary residue patterns remain the same;
- every gap between distinct-slope clusters contains every j residue modulo M,
  because its width exceeds2M;
- hence the complete atomic truth patterns, including event-domain membership,
  are exactly those already present at the representative n in[N,N+P-1].

For each fixed representative n, checking through j greater than every boundary
plus2M covers the unbounded final region and all its residues. This validates
ALL future H periods, not just a sampled standard-looking segment. Earlier
finite blocks are replayed completely. Values11<=n<N are checked individually
with the same exact infinite-j reduction.

The current exact inventory is743 target geometries,759 source geometries,
212 atoms,153 boundaries,6 slopes, stable threshold N=46 and period P=4.
Literal replay for11<=n<=49 therefore covers all n>=11 and all future times.
The certificate records the word hash, horizons and exact read counts.

## Files and scope

- family_words.json: the complete literal turn-word definition.
- certify_affine_family.py: exact arrangement construction and finite replays.
- affine_family_certificate.json: final counts and word hash.
- probe_continuation.py and extract_family.py: discovery controls only.

The original inward-spiral proof supplies its finite seed and endpoint profile.
This continuation certificate neither proves all finite seeds capture nor
excludes other endpoint architectures. Its reusable contribution is a small,
solver-free exact verifier for this one-parameter affine event family.

## Independent verification

The auditor independently rebuilt every block pose and every seed/read family,
regenerated all212 atoms and153 boundaries, reproduced N46/modulus2/period4,
and replayed all395,343 representative reads including the unbounded-tail region.
Files audits/check_spiral_affine_continuation_independent.py/json. The SHA256 of
the literal family_words.json file is
139251fe8a802a019e474fd4c8bbf1b8dd93bfd9023536e1ec09cb90d2942926.
The source certificate separately records a canonicalized-JSON word hash.
