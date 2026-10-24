# Ordinary retained cores on the northwest fresh frontier

## Statement and dependencies

Let W be the fixed104-letter standard word in `ant_exact.py`, and let p_r
be its phase-r read position when started at(0,0),S. Put

    q_n=(-33-2n,-14-2n),
    b_r=(-15,29)-p_r,
    s_{r,m}=b_r+m(-2,2).

There are22 fresh first-contact phases

    13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89.

For every ordinary phase r other than72, every n>=200, and every m>=100,
the complete two-black initial state {q_n,s_{r,m}}, at head(0,0),N, has a
standard tail with the exact phase, pose, time and archive bounds in
`ordinary_interfaces.json`. There is no relation required between n and m.
The input retains the complete q_n history: no old cell is discarded.

This new interface theorem uses two separately audited dependencies:

1. The complete one-bit q_n parent, including its entire northwest tail,
   from the exceptional rectangle certificate. At time208n+70738 it is at
   (-15,29),N, phase0. Its stationary discrepancy H1 from the clean
   thirteen-cell NW core satisfies -82<=u<=58 and z<=39, where
   u=x-y and z=x+y.
2. The reconstructed739-case canonical one-toggle certificate, with exact
   all-age old-wake exclusion. Its threshold case for each ordinary fresh
   phase is literally replayed here; the complete field hash, standard
   infinite tail and all-old-age guard are rechecked.

The new checker is `certify_ordinary_interfaces.py`. It also reconstructs
all22 first-contact classes and the one-period exact deposition identity.
The coupling and its sparse-recurrence corollary have passed independent
review and fresh snapshot replay. This is not a theorem about every possible retained one-black core.

## Exact archive coupling

At the stated q-parent phase0 checkpoint the complete field is

    clean NW core XOR H1.

Both the clean core and the complete q-parent have the same standard
infinite future. Thus H1 misses that entire incoming trace. Its support
bounds follow from the complete prefix and the placed clean core. In
particular the extra fixed core s_{r,m}, with u<-82, is not read anywhere
in that finite prefix.

The source construction C_j has j complete older deposit copies. Following
m NW periods and r phase updates therefore gives exactly the rotated and
translated C_m at the impact, still XOR the unchanged H1. The added core
is fresh white in this unperturbed field; flipping it gives the source
one-toggle input at phase r. Its first read occurs at

    208n+104m+70738+r.

For the source threshold N_r, the entire post-impact recovery and infinite
tail are checked. Every extra older deposit copy for ages m>N_r is unread
by that same future, by the exact all-age guard. Thus the threshold word
and pose trace apply at every m>=100 after translation by m(-2,2).

For each of the21ordinary phases, the checker obtains an all-future bound

    u(read)<=-4m+A_r < -82  for m>=100.

The final strict inequality is checked separately for every phase. It
proves that the complete recovery and outgoing tail miss H1 as well.
First-difference coupling now proves the claimed two-bit trajectory. This
is why the argument can use existing canonical certificates despite the
noncanonical q-parent archive.

## Canonical outgoing archive, including all old deposits

Let D be the twelve-cell source deposit, BASE=(-15,29), and let F(q)=BASE-q.
After rotating the source threshold case into the NW frame and shifting by
m(-2,2), its final complete field and its outgoing clean core are finite
explicit sets. Their XOR is the local part of the new archive.

The extra older deposits are exactly

    E_m = union_{k=0,...,m-N_r-1} (F(D)+k(-2,2)).

This identity follows by writing k=m-j for source deposit ages
j=N_r+1,...,m. The checker bounds this entire range algebraically, not by
sampling m. Every point of E_m has fixed z; its u minimum is

    -4m + min u(F(D)) + 4(N_r+1).

The complete outgoing archive is supported in the union of H1, these
extra deposits, the transformed threshold final field, and its clean
outgoing core. Taking their union is conservative even when XOR cancels
points. This gives the recorded upper-z bound independent of n,m and the
lower-u bound of the form -4m+L_r. The archive is stationary thereafter,
because both the actual and clean fields execute the same tail forever.

The complete finite prefix has u bounded on both sides for every fixed m,
and an upper-z bound independent of n,m. The checker separately records
the normal coordinate constant on each outgoing ray. These are precisely
the bounds needed to compare with cells escaping along the allowed remote
incidence shapes; no unverified shape of the scar is assumed.

## Twelve retained-core rays excluded by the global mass-five geometry

Fix m>=100 and one of the following phases:

    15,28,32,38,45,46,47,55,57,60,61,71.

The core is unread by the blank parent: u(s)<-34, below its complete
all-future u bound. At a hypothetical recurrent mass-five subsequence
retaining only this core, the first remote hit must therefore be q_n,
with n tending to infinity, by the previously audited first-collider
lemma. Its incoming exceptional branch reaches the two-bit parent above.
The core is encountered before any escaping northwest cell.

The12 phases split as follows.

### Southwest output: r=15,45,46,47,57

The entire two-bit future has bounded u for fixed m and bounded-above z.
In both four-edge shapes all remaining remote cells have |u| tending to
infinity. In the four-cycle a and c have divergent negative and positive
u, while d has z tending to positive infinity. Hence no remaining cell is
read and the standard future is permanent.

### Northwest output with incompatible exceptional column: r=28,60,61

The complete finite prefix has bounded u, and the NW tail has bounded z
and decreasing u. Only a can interrupt it. The outgoing exceptional
phase72 ray has even x, whereas a shares q_n's odd x-coordinate. Thus an
a-hit is ordinary. Its favorable ordinary future satisfies
u(read)<=u(a)+58. This is below the fixed-m archive lower bound and below
d by the divergent gap x(d)-x(a). It also misses c. In the four-edge
orientation with bounded y(a), a's z tends to minus infinity and it
misses the tail outright. The other orientation has the same ordinary-hit
exclusion. Capture is therefore permanent in all allowed shapes.

### Northeast output with incompatible exceptional corner: r=32,38,55,71

The complete finite prefix and NE tail have bounded u for fixed m, so a
and c are absent. The outgoing exceptional phase72 ray has coordinate
parity(odd,even), whereas the remote opposite corner d must have
parity(even,odd). Thus any d-hit is ordinary. Its entire future satisfies
z(read)>=z(d)-58, above the fixed archive bound and above a,c by the two
diverging side lengths. Both four-edge shapes miss the NE tail entirely.
Again capture is permanent.

The ordinary half-plane lemma applies here because the invariant
checkerboard/heading sector and the remote alternating endpoint signs
force the same favorable ten frontier channels as in the global argument.
The incompatible phase72 is the only exceptional one; the other nine
have the audited58-unit bounds. The exact check is
`certify_corner_sectors.py`: rephase every outgoing tail to W0; the
invariant (x+y+h) modulo2 equals0. A NW W0 head has even checkerboard
color and a has parity(odd,odd); a NE W0 head has odd checkerboard color
and d has parity(even,odd). Hence either collision has an even fresh
phase. The even fresh phases are exactly14,28,32,38,46,56,60,62,70,72.
The checker repeats this calculation in all21 actual output frames.

This independently audited argument excludes the twelve rays just listed
for m>=100. The remaining cases are now completed as follows.

## Complete first-frontier classification

All22 asymptotic fresh classes of this specified q-parent NW frontier
are now independently audited, for each fixed m>=100:

- The twelve ordinary-interface cases proved above.
- Phase72, by the separate fixed_core_rectangle proofs, in fact for m>=0.
- Phases13,14,27,89, by LOCALIZED_SCARS.md: the complete local correction
  rejoins the original rail and stays unread through the old parent chain.
- Phases70,75, by displaced_nw/PROOF.md: exact bivariate exceptional-a
  continuations capture southwest with uniform complete-future bounds.
- Phases29,56,62, by opposite_ne/PROOF.md: one-depth exact opposite-corner
  certificates plus untouched-old-deposit and H1 separation lemmas prove
  uniform three-geometric-parameter capture. No three-parameter arithmetic
  engine is required because the age and remote-origin parameters factor
  out of the source interaction.

The bases b_r represent exactly every (z,x modulo2) class with7<=z<=17.
Their minimum u is-54. Consequently every lattice site with

    7<=x+y<=17 and x-y<=-454

lies on one of these excluded rays with m>=100. This is a whole-band
consequence, not merely a count of phase labels. The coverage is recorded
in frontier_lattice_coverage.json.

This completes the chosen first-frontier problem, not the highway
conjecture or all retained-core cases. PRISTINE_BANDS.md maps the next
far-NW target bands encountered later in the old exceptional chain;
that geometric reduction is a separate review item.
