# All-scale recovery for sixteen black cells at four square corners

Date: 21 October 2026

Status: a parametric, computer-assisted exclusion for the specific family
below. Every finite leaf has an exact all-future tail certificate. The
unbounded parameter is covered by a written translation and guard argument.
This is not a proof of the general highway conjecture or a priority claim.

## 1 Statement

Let a belong to {0,1}, let u belong to {-29,-27,-25,-23,-21,-19,-17}, and let
n be any positive integer. Put

    B(a,u,n)={(a+2*s*n+i, a-u+2*t*n+j):
               s,t in {-1,+1}, i,j in {0,1}}.

Start the ordinary white-right, black-left ant at (0,0), facing north. The
input has exactly 16 black cells. They form four disjoint 2-by-2 blocks at
the corners of an axis-aligned square. Each block has favorable checkerboard
parity: its lower-left cell has sign -1, while the ant's invariant sigma is +1.

For n>=1, the two possible x-coordinate intervals are
{a-2n,a-2n+1} and {a+2n,a+2n+1}. Their closest coordinates differ by
4n-1>=3. The same argument applies to the y intervals. The four blocks
are therefore pairwise disjoint, so the input has 4*4=16 cells even at n=1.
The lower-left checkerboard sign is (-1)^(2a-u+2n(s+t))=-1 because u is odd.

**Theorem.** Every input B(a,u,n) has an eventual standard period-104 future.
For n>=34, a standard tail is certified by time

    104*n+35904.

For 1<=n<34, every case has a standard tail certified by time 102660. Thus
max(102660,104*n+35904) is a uniform all-parameter upper bound. The bound is
not asserted to be the first highway time.

This family comes from the sparse endpoint candidates that pass the four
directional clock tests. These actual physical seeds do not renew feedback.
The conclusion uses dynamics; the endpoint tests alone cannot establish it.

## 2 Exact reference and finite impact classes

Use the complete blank-orbit state at time 9977:

    p=(-15,10), h=W, |B|=715.

Its standard word W has length 104 and drift d=(-2,-2). The checker simulates
the entire blank prefix and verifies the infinite standard tail from the full
715-cell state using the supplied-word parity certificate. The future read
band is -28<=x-y<=-18.

A favorable 2-by-2 block can meet this band only if its lower-left normal
coordinate u is one of the seven odd integers in the theorem. Translation
by the full drift (-2,-2) leaves two longitudinal phase classes, represented
by a=0,1. These give the 14 impact cases. This does not claim that arbitrary
arrangements of four blocks reduce to the displayed square family.

For n>=34 all four input blocks miss the finite blank prefix. Their x
coordinates alone are outside the prefix's exact x range [-19,29]. The northwest and
southeast blocks also miss the entire forward standard band, since their
normal coordinates are u-4n and u+4n. The northeast block lies beyond the
largest x coordinate of the future southwest ray. Consequently the first
changed read is in the southwest block.

For each phase q_i of W and each cell b of the unshifted southwest block,
solve b-q_i=j*d in integers. The actual block is shifted by n*d, so the
read time after 9977 is 104*(n+j)+i. The finite minimum gives

    hit(a,u,n)=104*n+c(a,u).

All relevant epochs are nonnegative for n>=34. The checker records every
candidate ray and checks the minimum exactly. The first-read pose, after
translation by (2n,2n), is independent of n.

## 3 Why one finite recovery covers every larger scale

Recenter the complete first-hit state by (2n,2n), so that the southwest
block is always at lower-left corner (a,a-u). Let S_n be the black field
in this frame for the single-block input.

The input block has not yet been read. The preceding physical path is the
certified blank prefix followed by the specified number of standard periods
and one fixed phase prefix. Increasing n by one adds one full standard
period before the hit and then recenters by -d=(2,2).

Let C be the net flip set of that standard period in the common first-hit
frame, excluding the untouched block. For the corresponding blank fields A_n,

    A_(n+1)=translate_(2,2)(A_n symmetric_difference C).

It follows algebraically that, with

    E_n=S_(n+1) symmetric_difference S_n,

one has

    E_(n+1)=translate_(2,2)(E_n).                         (1)

The fixed block cancels in the symmetric difference. This is an identity
of finite XOR fields, not an inference from samples at two parameter values.

The checker computes S_34 and S_35 exactly. In all 14 impact cases, E_34 has
796 cells and its minimum x+y coordinate is 115. Equation (1) therefore
places every further change E_n in x+y>=115+4(n-34).

From S_34, execute the case's finite recovery word and certify its infinite
standard tail. Let H be the largest x+y coordinate of all recovery reads
and one full tail period. Every certified outgoing drift is southwest,
northwest or southeast, so its x+y increment is nonpositive. Thus its
ENTIRE future lies in

    Omega={q:q_x+q_y<=H}.

The largest H among all cases is 111. Therefore E_n is disjoint from Omega
for every n>=34. All complete first-hit states S_n agree on Omega.

The three other square-corner blocks, in the same recentered frame, have
minimum x+y at least 4n+2a-u. At n=34 this is at least 153, and it increases
with n. They also miss Omega.

First-difference coupling now proves the entire future: the full 16-cell
physical input, at its first hit, agrees on Omega with the single-block
reference S_34. The reference never leaves Omega. Hence the actual ant
executes the same finite recovery and standard infinite tail. All remote
black cells remain in the complete field; none is deleted for the proof.

## 4 Exact recovery data

Here c is the constant in the first-hit offset 104n+c after update 9977.
R is the number of updates from the first hit to the certified tail.
H is the guard from Section 3. All times use states before updates.

| a | u | c | R | H | Outgoing drift |
|---|---|---|---|---|---|
| 0 | -29 | -1011 | 624 | 34 | (-2,-2) |
| 0 | -27 | -1012 | 18580 | 111 | (2,-2) |
| 0 | -25 | -983 | 16188 | 101 | (-2,2) |
| 0 | -23 | -984 | 7160 | 51 | (-2,-2) |
| 0 | -21 | -881 | 26808 | 105 | (2,-2) |
| 0 | -19 | -864 | 1707 | 37 | (-2,-2) |
| 0 | -17 | -761 | 12791 | 87 | (-2,2) |
| 1 | -29 | -1025 | 3499 | 49 | (-2,-2) |
| 1 | -27 | -1026 | 511 | 37 | (-2,-2) |
| 1 | -25 | -1002 | 2324 | 44 | (-2,-2) |
| 1 | -23 | -994 | 952 | 44 | (2,-2) |
| 1 | -21 | -978 | 1205 | 41 | (2,-2) |
| 1 | -19 | -875 | 7117 | 64 | (-2,2) |
| 1 | -17 | -743 | 10730 | 57 | (-2,-2) |

The certified absolute tail time is 104n+9977+c+R. Its largest constant
is 35904. None of these single-block impact classes reverses northeast
along the incoming wake. This conclusion holds for the guarded clean
incoming standard field used here, not for arbitrary old fields.

## 5 The finite parameter range

There are exactly 14*33=462 inputs with 1<=n<34. The checker starts every
one from its entire 16-cell input, at (0,0),N. It retains all black cells
during every literal step. For each input it obtains an exact infinite
period-104 certificate. There are no timeouts or unresolved cases.

The finite leaves use 8,033,591 literal updates in total. The largest
certified time is 102660, for (a,u,n)=(0,-21,16). Its certified outgoing
drift is (2,2). Thus small scales can have behavior different from the
large-scale scattering table; they were checked separately.

Each record saves the exact 16-cell seed, complete-field hash, certified
time, head pose, cyclic word phase, and all-future certificate count. The
full field can be reconstructed by the recorded literal replay.

## 6 Why a finite tail certificate proves all future periods

For a prescribed periodic word with phase positions q_i and nonzero drift d,
the cell read at phase i, epoch k is q_i+k*d. Its pre-read color is the XOR
of its membership in the complete initial black field and the parity of
all previous phase writes at the same cell.

An initial black cell can meet a phase ray at one integer epoch. A previous
phase contribution becomes present at one integer overlap threshold. The
color is therefore constant between a finite set of breakpoints. Checking
epoch zero, all thresholds, every initial hit, and the next epoch after
each hit checks every k>=0. Induction on the prescribed reads proves the
entire infinite tail. Mere observation of repeated periods is not used as
the mathematical stopping condition.

The implementation is in ../ant_exact.py, supplied by the parent research
process. It implements the standard finite-support periodic-word criterion.

## 7 Files and reproduction

Run, in this order:

    python3 single_blocks.py
    python3 certify_corner_blocks.py
    python3 check_small_corner_blocks.py
    python3 audit_corner_blocks.py

The first command records the discovery controls at n=64 and n=96. The
second command reruns the exact reference at n=34 and n=35, checks every
finite ray condition and every guard inequality, and certifies all 14 tails.
The third command covers all remaining finite parameter values.
The fourth command independently audits the 14 large-scale leaves with a
complex-coordinate step implementation and a different infinite-tail checker.
It starts with each entire 16-cell input at n=34, checks the exact first hit,
finite recovery guard, and complete-field infinite tail, and independently
recomputes both source fields whose difference is E_34. It also certifies
the complete blank reference and checks the affine prefix/ray exclusions.

This audit passes all 14 cases. The full 16-cell replays use 286,239 updates
and 3,871 tail epoch checks; the blank reference uses 274 tail epoch checks.
The smallest source-difference guard margin is 4, and the smallest margin
between a protected future and the other corner blocks is 52. These are
strict positive margins at n=34 and increase for larger n. The range
n<34 is handled by the separate 462 finite certificates, so no threshold
interpolation is used.

Data files:

- single_blocks_results.json
- corner_blocks_guard_certificate.json
- small_corner_blocks_results.json
- corner_blocks_independent_audit.json

The JSON guard certificate includes all 796 source-change coordinates per
case. Its minimum-sum bound, the affine translation identity (1), and the
read-set guard supply the unbounded-parameter coverage.

## 8 Scope

This rules out one explicit all-scale 16-cell candidate family. It also
provides a complete favorable 2-by-2 block scattering table in a sufficiently
long clean standard channel. It does not prove that several such scattering
events can never create a renewable circuit. Arbitrary block placement and
interactions with an old wake require further arguments.
