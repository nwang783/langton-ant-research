# A uniform fresh-band obstruction for real-scalar position inflation

22 October 2026. Status: Sections1--9 independently passed audit through
22:00 UTC, including separate no-import finite inventory replays.
The causal-reduction analysis independently derived the same odd-scale
low-retreat inequality. This is a restricted self-similarity theorem, not
the highway conjecture and not a finite-controller assumption.

## 1. The all-parameter theorem

Let an actual finite-support Langton-ant path, normalized by p(0)=0, satisfy

    p(kn)=a p(n) for every n>=0,

where k>1 and a>1 are integers. No equality of headings at n and kn is
assumed. Then necessarily

    k >= 3a-2.

The statement permits arbitrary history-dependent choices of all fine
macros. In particular it is not limited to substitutions or automatic paths.

## 2. Axis counts, including even scales

Write epsilon=a mod 2. Checkerboard parity gives k congruent to a modulo 2.
The invariant p_x+p_y+h modulo 2, with headings N,E,S,W numbered 0,1,2,3,
implies that for odd a the fine heading at kn has the same axis as the
coarse heading at n. A north coarse STEP has horizontal incoming coarse heading. Consequently
a fine macro for that north step starts with a vertical move. Zero horizontal displacement forces its
(k-1)/2 horizontal moves to be even. Thus k=4 ell+1 when a is odd.

For even a, k is even and each macro makes k/2 moves on each axis.
A north macro has zero horizontal displacement, forcing k/2 even.
Thus k=4 ell when a is even. Combining both cases,

    k=4 ell+epsilon.

A north-displacement macro has exactly

    s=ell+(epsilon-a)/2

south moves. This must be a nonnegative integer. Its maximum relative
height, at any read or endpoint, is at most a+s. An east- or west-displacement
macro has ell north moves; a south-displacement macro has s north moves.
Since s<=ell, every macro whose coarse step is not north has maximum
relative read height at most ell. These bounds allow every compatible
fine heading and do not impose heading restoration.

## 3. A pristine band before a coarse record

The finite-support ant cannot stay in a finite region. Rotate an unbounded
coordinate direction to north; positive real scaling commutes with this
quarter rotation. Let t=t(Y) be the first coarse time reaching a sufficiently
high positive row Y. At time t the incoming heading is north, the cell has
never been read, and the read is R. The predecessor macro goes from height
a(Y-1) to aY.

For every earlier macro n<t-1, one of the following holds:

- its coarse center has height Y-1 and its coarse step is not north, so
  all its fine reads have height at most aY-a+ell;
- its coarse center has height at most Y-2, so all its fine reads have
  height at most a(Y-2)+(a+s)<=aY-a+ell.

Choose Y so large that aY-a+ell+1 also exceeds every initial black height.
Immediately before the predecessor macro, all rows

    y >= aY-a+ell+1

are therefore entirely pristine white.

## 4. Each intermediate fresh row spends a south move

The elementary fresh-row fact is independent of any inflation: on its first
ever entry into a completely unread, initially white horizontal row from
below, the ant arrives facing north. It reads R, moves east in that row,
reads a second fresh R, and then moves south. Before it can reach the next
higher row it has therefore spent a south move.

If b=a-ell-1 is positive, the predecessor macro must first reach each of
the b pristine intermediate rows

    aY-a+ell+1, ..., aY-1

before it ends at aY. Each forces a distinct south move inside this same
macro. Hence b<=s. If b<=0 the inequality b<=s holds automatically because
s>=0. In either case

    a-ell-1 <= ell+(epsilon-a)/2,
    3a <= 4ell+epsilon+2 = k+2.

This proves the theorem. No shifted infinite-path inflation identity is
used; the only scaling identity is the original one at aligned times.

## 5. Scope and useful families

For odd a, write k=2a-1+4r. Here r=s is precisely the number of south moves
available in a north macro. The theorem becomes a<=4r+1, or equivalently
excludes every a>=4r+3. This is the independent odd-scale formulation.

For k=2a+3, all even a are excluded by checkerboard parity, and all odd
a>=7 are excluded by this theorem. The remaining a=3 case is separately
excluded by the audited position-only scale-nine record certificate.
The a=5,k=13 boundary case needs more than this first inequality, and is
closed analytically in Section7 below;
the discovery inventory in probe_record_bands.json reports no compatible
pristine predecessor/record pair with white first reads on y>=-1, but that
extra finite computation is not a dependency of the all-parameter theorem.

The inequality does not exclude critical-area scales k=a^2 for large a,
non-real Gaussian scales, or arbitrary non-self-similar trajectories.

## 6. Stronger bounce accounting (independently audited)

Consider the interval from first arrival at a pristine white row j, facing
north, until the first arrival at row j+1. If this interval contains exactly
one south move, its word is forced to be

    F=RRRRLR,

with displacement (-1,1) and final heading north. To see this, put its first
cell at q. The first RR reaches q+(1,-1), facing south. An L there would move
east; avoiding another south move would next require L, reaching the still
fresh cell q+(2,0). Its next RR forces a second south move. Therefore the
third turn is R. The fourth must also be R to avoid an immediate second
south move. This returns to q, which is black, forcing L; the fresh cell
q+(-1,0) then forces R and the first arrival at row j+1.

This interval rereads its entry predecessor q+(0,-1) with R. That cell was
read immediately before q, so that preceding read must have been L. But F
ends by reading the NEXT entry predecessor with R. Consequently two
consecutive pristine-row crossings cannot both contain exactly one south
move.

For b positive consecutive intermediate fresh rows, the predecessor macro
therefore needs at least

    b+floor(b/2)

south moves. In the notation of Sections2--4 this strengthens the necessary
condition to

    s >= max(0,b)+floor(max(0,b)/2),
    b=a-ell-1, s=ell+(epsilon-a)/2.

In particular it excludes all equality cases k=3a-2 with b>=2. This statement
again concerns arbitrary history-dependent macro choices.

## 7. The one-retreat boundary (independently reviewed, both endpoint phases)

If s=1 and b>=1, Section4 forces b=1. The predecessor's first arrival at
its final row completes F. It can then stop or take exactly one extra
horizontal R before its aligned endpoint: any further move is vertical,
and with its sole south move already spent, it could not end at this same
height. For odd a in the ORIGINAL unshifted positive-scalar setting, endpoint
heading-axis parity forbids the extra horizontal move. For even a both
suffixes F and F R must be handled. In the broader affine setting of
Section8, odd k=3 mod4 also permits the F R branch; both branches below
are retained there.

First suppose the suffix is F. Normalize its endpoint to (0,0,N). Its reads are

    (1,-1):R, (2,-1):R, (2,-2):R,
    (1,-2):R, (1,-1):L, (0,-1):R.

Row0 and everything above it remain pristine. The next macro corresponds
to the coarse R at its first north record, so its displacement is a east.
It starts north and has exactly s=1 west moves by the same axis count.
However its first four turns are forced R,R,R,L, reading

    (0,0), (1,0), (1,-1), (0,-1),

and ending at (0,-2), facing south. One west move has already occurred.
If its next turn is R, a second west move occurs immediately. If its next
turn is L, the next cells (1,-2) and (1,-1) are both black from the displayed
histories, forcing L,L and again a second west move. All these moves occur
within seven steps, hence within the macro in the cases under discussion.
Contradiction.

For the other suffix F R, normalize the aligned endpoint to (0,0,E). F ended
at (-1,0,N), leaving (0,-1) white and (-1,-1),(0,-2) black; the extra R read
(-1,0). The following east macro is forced R,R,L at (0,0),(0,-1),(-1,-1),
ending at (-1,-2), facing south, with one west move spent. Its next R spends
a second west immediately; its next L forces L,L at (0,-2),(0,-1), again
spending a second west. This contradiction occurs within six moves.
Even k gives equal axis counts regardless of entry heading, so the one-west
budget applies to this E-entry branch as well.

This excludes s=1,b>=1, in particular (k,a)=(13,5) and (16,6), without any
finite search. Combined with the independently replayed (9,3) exclusion and
Section5, it excludes the ENTIRE family k=2a+3, a>1: even a violate parity,
odd a>=7 violate k>=3a-2, a=5 is this boundary argument, and a=3 is the
scale-nine record theorem. The causal analysis and auditor independently
checked both local branches. The even F R possibility was supplied during
audit and is essential; the original N-ending-only argument was incomplete
for even a. No discovery enumeration is needed for this family claim.

## 8. Eventual affine and quarter-rotated inflation (independently audited)

The same local argument extends to an identity holding only eventually,

    p(kn+c)=A rho p(n)+d for every n>=n0,

where A>1 and k>1 are integers, c is any integer, d is a lattice vector,
and rho is any orientation-preserving quarter rotation. There is no heading
premise. Require kn+c>=0 on the asserted domain, increasing n0 if necessary.

Here the odd case may have either residue modulo4. Define

    epsilon=0 if k is even,
    epsilon=1 if k=1 mod4,
    epsilon=-1 if k=3 mod4,
    ell=(k-epsilon)/4.

Local displacement parity forces k congruent to A modulo2. If k is even,
zero displacement on the perpendicular axis forces k divisible by4. For
odd k, the perpendicular move count is even and the parallel count is odd,
so they are respectively 2ell and 2ell+epsilon. This allows the fine entry
axis to differ from the rotated coarse entry axis in the epsilon=-1 case;
discarding that phase would be an unjustified heading restriction.

For a macro whose displacement is A north in the rotated fine frame,

    s=ell+(epsilon-A)/2

is its south budget. All macros not directed north have top at most ell,
and every macro has top at most A+s, exactly as before.

Choose a coarse unbounded record direction u. In the fine frame use
direction rho u. If the coarse record height is Y, its corresponding
endpoint height is AY+beta, where beta is the projection of d onto rho u.
Before the predecessor macro, all earlier aligned macros lie below
AY+beta-A+ell+1. The finite fine prefix before kn0+c also lies below this
threshold when Y is chosen sufficiently large. Choose Y still larger so
the threshold exceeds every initial black height in that fine direction.
Thus the identical pristine-band argument applies, with beta merely
translating every displayed row.

Consequently this eventual affine class still requires

    k>=3A-2,
    s>=max(0,A-ell-1)+floor(max(0,A-ell-1)/2),

and s=1 with A-ell-1>=1 is impossible by the two endpoint branches in
Section7. Those branches already cover both vertical and horizontal fine
endpoint phases. In the epsilon=-1 case the following east macro likewise
has 2ell+epsilon horizontal moves, hence the same west budget s.

This extension uses only ONE sufficiently remote coarse record and its
next macro. It does not shift the infinite recurrence or require that the
fine record be exactly aligned beyond what the one-retreat local argument
itself establishes. The separate scale-nine affine record/refinement
extension is independently audited in
`../causal_reduction/morphic_candidates/eventual_affine_k9_exclusion.md`.
Together with Section9, this excludes the entire k=2A+3 family in the
eventual affine, quarter-rotated scope: even A violate parity, A>=5
violates k>=3A, and A=3 is precisely that audited ninefold base case.

## 9. Closing the remaining cone-equality cases (independently audited)

In the eventual affine scope of Section8, the weak boundary k=3A-2 can in
fact be excluded entirely. Since k and A have the same parity, this gives
the necessary condition

    k>=3A.

Apart from a tiny ownership inventory, this is a consequence of the
existing analytic inequalities. If k=3A-2 satisfies the required parity
and axis counts, direct substitution gives s=b. For b>=2 this contradicts
Section6; for b=1 it contradicts Section7. The only b=0 cases with A>1 are
(k,A)=(4,2) and (7,3). Values A divisible by4 would give even k=2 mod4 and
are already geometrically impossible.

The remaining finite inventories are independently regenerated in
check_affine_small_owners_independent.py/json, with no source imports:

- (k,A)=(7,3), fine-entry axis opposite the coarse-entry axis: 96 oriented
  macro records, 12 north-facing coarse-R targets; every target has a
  first-L cell all of whose possible coarse owners have relative y>=0.
- (k,A)=(4,2), all fine entries vertical in the normalized fine frame:
  32 oriented records, 4 north-facing coarse-R targets, with the same
  forward-ownership property.

For clarity, an owner of a target cell z is a coarse pose (q,h) such that
some permitted macro at that pose reads z, i.e. z=Aq+v for one of its read
offsets v. All four headings and both coarse turns are included. The exact
coarse sector restriction after normalizing the record pose to (0,0,N) is
q_x+q_y+h=0 mod2. The scripts enumerate every internally alternating word
of length k, all compatible fine headings, and every such integer owner.

At a sufficiently high strict coarse north record, no earlier coarse
macro center has relative y>=0. Hence a forward-owned first-L cell has no
earlier aligned fine read. Its absolute fine height tends to infinity with
the coarse record, so it also avoids the finite exceptional fine prefix and
all initial black cells. Its first L is impossible. Spatial affine offsets
cancel in the owner equation, and quarter rotations are removed separately
from the coarse and fine frames. This is the usual record-ownership fuel
argument, not a claim that a shifted whole trajectory preserves inflation.

For k=7, the odd phase epsilon=-1 forces the opposite-axis inventory, so
the argument applies directly. For k=4, the fine headings at aligned times
4n+c all have one fixed physical axis. We must choose an unbounded coarse
record direction mapped by rho to that axis to use the stated inventory.
Such a direction exists because BOTH physical coordinates are unbounded
in absolute value for any eventual affine expanding path of this kind.

To prove that last fact, suppose one coordinate were bounded. For rho=+/-I,
iteration of n->kn+c makes that coordinate obey an expanding scalar affine
recurrence, forcing it to equal the affine fixed point for every sufficiently
large n. A Langton path cannot have one coordinate constant on a tail,
because its move axes alternate. For rho=+/-i, the recurrence transfers
boundedness of one coordinate to the other. Iterating the expanding vector
affine map then forces the entire path eventually constant, also impossible.
Thus the required coarse coordinate has a positive or negative unbounded
direction, which can be rotated to north while rotating its fine image
direction to north as well. The fine-entry axis is then vertical, as needed.

The small checker signs off the finite inventories. The auditor also
independently regenerated every owner set with integer-vector geometry in
../audits/check_affine_cone_boundary_independent.py/json and accepted the
affine owner argument and both-coordinates-unbounded lemma. This
strengthening is not a highway theorem.

Further independently audited strengthening,23:26 UTC: `pristine_climb_cost.md` defines a total elementary-computable superadditive minimum c(H), with c1=1,c2=3,c3=7. Replace the earlier H+floor(H/2) fresh-row budget by c(H)>=7floor(H/3)+[0,1,3][H mod3]. The earlier inequalities remain valid, but are no longer the strongest recorded cone.
