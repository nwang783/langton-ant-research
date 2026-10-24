# The four-corner endpoint model cannot regenerate

## Exact scoped result

For n>=0 let

    B_n={(-n,-n),(-n,n+1),(n+1,-n),(n+1,n+1)}.

Start classical Langton's ant at the origin, heading east, with precisely
B_n black and all other cells white. Then:

1. For every n>=1, the black-cell count is greater than four at every
   positive time.
2. For n=0, the only positive times with black-cell count at most four are
   updates 1,2,3,4, with masses 3,2,3,4 respectively. None has the original
   ant pose.
3. Consequently, for no n,m>=0 and positive time does this trajectory reach
   the state with black board B_m and ant pose (origin,E).
4. Every member of this family reaches a standard period-104 highway.

This is an all-size, computer-assisted family result. It is not a statement
about arbitrary four-black-cell initial patterns or arbitrary low-mass
returns. It does not prove pointwise divergence of mass in the general
finite-support problem.

The main simplification is first-contact geometry, not a simulation cutoff.
All parameters n>=21 have four cells that are never read. Only the finite
parameters 0,...,20 require individual continuation certificates.

## 1. First-difference coupling

If an added black set is never read by a reference trajectory, the modified
trajectory is identical to the reference trajectory forever. If a first
difference existed, it would occur at a first read of an added cell; before
then, the two boards agree at every processed cell and make identical moves.

We use the blank reference trajectory from the origin facing east. An exact
finite-ray certificate proves its standard tail beginning at update 10,088.
At that time its pose is (6,18,E), its black count is 728, and its drift is

    d=(-2,2).

For the next 104 processed positions R, the exact coordinate ranges are

    18 <= x+y <= 28,
    -19 <= x-y <= -9.

Every future read is in R+k*d for some k>=0. Translation by d leaves x+y
unchanged and decreases x-y by four. Therefore every future read satisfies

    x+y in [18,28],  x-y<=-9.

## 2. Every corner misses the entire future tail

The two same-sign corners of B_n lie on x=y:

    (-n,-n), (n+1,n+1).

They have x-y=0 and thus miss every future read ray of the blank tail.

The other two corners lie on x+y=1:

    (-n,n+1), (n+1,-n).

They also miss every future read ray, whose sums lie between 18 and 28.

These statements apply to every n>=0. They are inequalities on complete
infinite rays, with no distance cutoff or assumption about how long the
trajectory has already looked periodic.

## 3. The entire finite-prefix contact inventory

For a processed cell (x,y), membership in some B_n is determined explicitly:

- if x=y<=0, then n=-x;
- if x=y>=1, then n=x-1;
- if x+y=1 and x<=0, then n=-x;
- if x+y=1 and y<=0, then n=-y.

These four cases are exactly the four corner definitions. Scanning the
10,088-cell blank prefix gives precisely the touched parameters

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20.

There is no touched parameter above 20, and parameter 17 is not touched.
Combined with Section 2, all four cells of B_n are unread forever when
n>=21, and also when n=17. First-difference coupling proves that each such
trajectory is exactly the blank trajectory with four permanent unread
black cells added.

The blank trajectory has positive mass at every positive time: direct
replay gives a minimum of one before update 10,088. Its next-period mass
minimum is 726, and each subsequent period adds twelve. Thus every member
with unread corners has mass strictly greater than four at every positive
time.

## 4. Complete finite-case coverage

The remaining parameters are contained in 0,...,20. Each was run from the
complete four-cell board, and an exact infinite-tail certificate was checked.
No cells or scars were discarded. All 21 certificates completed:

| n | Certified tail starts by update | Tail's first-period minimum mass |
|---:|---:|---:|
| 0 | 11,960 | 859 |
| 1 | 9,152 | 665 |
| 2 | 728 | 105 |
| 3 | 6,032 | 542 |
| 4 | 1,456 | 201 |
| 5 | 1,872 | 216 |
| 6 | 1,768 | 208 |
| 7 | 14,976 | 914 |
| 8 | 13,104 | 834 |
| 9 | 3,952 | 378 |
| 10 | 2,288 | 248 |
| 11 | 2,392 | 271 |
| 12 | 12,272 | 844 |
| 13 | 17,472 | 995 |
| 14 | 11,752 | 726 |
| 15 | 14,768 | 983 |
| 16 | 10,296 | 753 |
| 17 | 10,296 | 754 |
| 18 | 10,296 | 765 |
| 19 | 10,296 | 754 |
| 20 | 10,296 | 753 |

The table gives sufficient certificate times, not earliest entrance times.
Parameter 17 is included redundantly as a check on the first-contact result.

For n>=1, the complete prefix before each certificate contains no positive
time of mass at most four. Each certified word has net mass gain twelve.
Therefore the period-k mass minimum is the displayed minimum plus 12k;
the infinite suffix also has no such time.

For n=0, the complete prefix has only four low-mass states:

| Update | Mass | Ant pose |
|---:|---:|---|
| 1 | 3 | (0,1,N) |
| 2 | 2 | (-1,1,W) |
| 3 | 3 | (-1,2,N) |
| 4 | 4 | (0,2,E) |

These first four updates can also be read directly from the initial square:
the first two processed cells are black and the next two are white, giving
turns L,L,R,R. None returns the ant to (0,0,E). Every later state has mass
greater than four. This proves the stated exclusion for every n,m.

## 5. What makes the infinite certificates exact

At a candidate tail start, let B be the complete finite black set. Simulate
one standard period with read list R to obtain B1, the same heading, and
diagonal displacement d. Form the finite discrepancy

    D=B1 XOR (B+d).

The checker verifies that D avoids R+k*d for every k>=1, by exact integer
translation classes and longitudinal thresholds. After j periods the board
has the form

    (B+j*d) XOR XOR_{i=0}^{j-1}(D+i*d).

The discrepancy terms avoid all reads in period j. Induction therefore
proves the repeated word for every later period. Since that word has twelve
more right turns than left turns, each period raises the total black count
by twelve, regardless of the retained old field.

This check uses no optimization solver and no floating-point arithmetic.
The implementation is the shared exact ray checker already used for the
scattering checks in this branch. It is not proof-assistant verification or
an external human audit.

## 6. Interpretation of the endpoint model

The states B_n remain a valid example of endpoint data passing the signed
row/column conditions and the all-center clock inequalities in
`../constructive_alternatives/signed_cut_and_explicit_mass_bound.md`.
The clock-compatible putative transitions are not physical trajectories.

Here the missing chronology has a direct geometric explanation: for all
sufficiently large n, the ant never reaches any of the proposed four stored
bits. It cannot erase them and recreate the next larger square. The few
parameters where it does read a corner are all certified to escape into a
standard wake with mass above four.

This obstruction is specific to the locations and pose of this endpoint
family. A different placement that intersects the moving read strip does
not satisfy the same unread-cell argument. No conclusion about every
possible finite controller follows from this family exclusion.

## Working records

- `certify_corner_family.py`: complete blank guard and finite-case checker.
- `corner_family_certificate.json`: full structured certificate summary.
- `corner_family_certificate.jsonl`: progress record for all completed cases.
- `first_marker_scattering.py`: the shared integer finite-ray verifier.

Run from the workspace root:

    python3 ant_rethink/defect_dynamics/certify_corner_family.py

No Z3 dependency is needed. Any failed certificate or unfinished finite case
raises an error rather than being treated as an exclusion. No novelty or
priority claim is made; the target family arose as an arithmetic endpoint
model in this session, and first-difference coupling is a standard argument.
