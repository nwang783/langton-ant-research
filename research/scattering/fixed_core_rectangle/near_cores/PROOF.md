# Near members of the retained phase-72 core ray

## Exact nine-parent result

Use the same coordinates as the surrounding fixed-core certificate:

    q_n = (-33-2n,-14-2n), s_m = (-23-2m,31+2m).

For each m in {0,2,3,4,5,7,8,9,10}, the complete two-cell initial field
{q_n,s_m}, with head (0,0),N, has a permanent standard northeast highway,
for every integer n>=200. This is a finite list of nine all-parameter
statements, not a sampled assertion in n. `certify_parents.py` starts with
both cells, checks every read of the supplied affine word, and checks every
read of its infinite tail against the complete accumulated field. Its
underlying one-parameter engine was separately audited for the earlier
rectangle theorem. The new proof instances await independent audit.

`certify_ne_interfaces.py` binds each proof to its word template and builds
a canonical clean highway state at the same phase and pose. The actual
field is that canonical state XOR a stationary finite archive H. For each
fixed m in the list, the complete finite prefix has bounded u=x-y on both
sides and an upper bound on z=x+y independent of n. The entire NE tail has
bounded u. The archive has z upper bounds as follows:

    m:       0   2   3   4   5   7   8   9  10
    max z:  47  53  53  49  53  51  71  71  71

All nine outgoing exceptional phase-72 rays have x odd and y even.
Their exact bases, finite-prefix bounds, and tail u ranges are recorded in
`ne_interfaces.json`.

## Conditional recurrent-mass-five implication

Combine these exact interfaces with the already derived mass-five remote
incidence classification and ordinary-impact half-plane lemma. This is an
analytic corollary, not a claim about arbitrary five-cell initial fields.

Suppose a recurrent mass-five subsequence retains s_m, with one of the nine
listed m, as its unique fixed local cell. The blank parent never reads s_m,
and the first remote hit is q_n with n tending to infinity. The fixed core
is read before any escaping northwest candidate. In either allowed
four-edge remote strand, every remaining remote cell eventually has
unbounded u of one sign, so it is absent from the finite two-bit prefix and
NE tail. That parent therefore captures permanently.

For a remote four-cycle, the other cross corners a=(l,t), c=(r,b) have
u(a) tending to minus infinity and u(c) tending to plus infinity. They too
are never read by this two-bit parent. Only d=(r,t) could meet its NE tail.
The remote row/column sign constraints force q=(odd,even) and
 d=(even,odd). Thus d cannot lie on any of the nine exceptional phase-72
rays. If d is read, it is an ordinary impact. The ordinary outgoing future
is confined to z>=z(d)-58. This eventually misses H, the fixed core, a and
c, since z(d)-z(a)=r-l and z(d)-z(c)=t-b both tend to infinity. The standard
ordinary capture is permanent, again a contradiction.

Consequently the nine retained-core points are excluded once these new
proof instances and the analytic coupling are independently audited.
This does not exclude arbitrary cores in the fixed-width diagonal cross.

## Remaining near-core branches

Literal two-sample discovery, not yet a theorem: m=1 yields a NW tail whose
exceptional phase-72 ray is parity compatible with remote a. It forces
 a=(-33-2n,2n-21). The three-cell parent then appears to emit SE, with a
possible next c=(2n-100,-14-2n).

For m=6 the two-cell parent emits SE, with possible exceptional
 c=(2n+12,-14-2n). Its three-cell parent appears to emit NW, with possible
next a=(-33-2n,2n+93). Exact proof and complete-cycle continuation are in
progress. These are precisely the two non-NE low-core types among
m=0,...,10; no conclusion about them is inferred from these discoveries.

## Exact completion of m=1 and m=6

The discovery statements above have now been replaced by exact proofs.
`certify_parents.py`, `certify_branches.py`, and
`certify_branch_interfaces.py` verify these four interfaces for all n>=200:

- m=1, two bits: NW tail z in [-55,-45]; finite prefix u in [-82,66]
  and z<=47; stationary archive u>=-82 and z<=47.
  The only exceptional cell sharing the q column is
  a=(-33-2n,2n-21).
- m=1, three bits q,s,a: SE tail z in [-123,-113]; finite prefix u<=94
  and z<=47; archive u<=94 and z<=47.
  The only exceptional cell sharing the q row is
  c=(2n-100,-14-2n).
- m=6, two bits: SE tail z in [-11,-1]; finite prefix u in [-112,90]
  and z<=51; archive u<=90 and z<=51.
  The only exceptional cell sharing the q row is
  c=(2n+12,-14-2n).
- m=6, three bits q,s,c: NW tail z in [59,69]; finite prefix u>=-112
  and z<=73; archive u>=-112 and z<=73.
  The only exceptional cell sharing the q column is
  a=(-33-2n,2n+93).

The archive bounds include the exact canonical clean core at the outgoing
phase. They therefore apply to the stationary XOR discrepancy, not just the
finite field at the instant of capture.

`certify_cycles.py` includes all five initial cells and the entire written
history. It proves these completed cycle families:

- m=1, with the forced a and c above and d=(2n-100,2n-21): permanent SE
  capture at 624n+219856, pose (38,-46),N, standard phase42.
- m=6, with the forced a and c above and d=(2n+12,2n+93): permanent NE
  capture at 624n+230464, pose (70,18),S, standard phase99.

In both families d is never read, including during the infinite tail.
These are fresh all-parameter instances; independent audit is pending.

### How the interfaces close the remote incidence alternatives

For m=1, the two-bit NW parent can meet only a: c is beyond its upper-u
bound and d beyond its upper-z bound. In the first four-edge orientation,
a has bounded y and hence z(a) tends to minus infinity, so it also misses
the NW tail and capture is permanent. In the transposed orientation, a
may be read. An ordinary a-impact is confined to u<=u(a)+58 and misses the
archive and all other cells: the gap from d is x(d)-x(a), which tends to
positive infinity. Hence a must be the exceptional cell above. The
three-bit SE parent then misses c and d: c has bounded x, so its z tends
to minus infinity, whereas d has z tending to plus infinity. Its finite
prefix excludes them by the upper-u and upper-z bounds respectively.

In a four-cycle, the same ordinary-a argument forces that a. The
three-bit parent excludes d by z and can meet only c. An ordinary c-impact
is confined to u>=u(c)-58, above the archive and above d by the divergent
gap y(d)-y(c). The exceptional case forces c, and therefore also d. The
complete-cycle certificate above then gives permanent capture.

For m=6, interchange the order of a and c. In the transposed four-edge
orientation c has bounded x and its z tends to minus infinity; all other
cells are excluded by the two-bit parent's finite u bounds or outgoing SE
strip. In the first orientation, c may be read. An ordinary c-impact
escapes in its upper-u half-plane, including past d by the divergent gap
y(d)-y(c). The exceptional case forces c. The three-bit NW parent then
misses a and d: a has bounded y and z tending to minus infinity, d has z
tending to plus infinity; the finite prefix excludes a by its lower-u
bound and d by its upper-z bound.

In a four-cycle, exceptional c is forced. The three-bit parent excludes d
and can meet only a. An ordinary a-impact escapes below the archive in u,
and below d by the gap x(d)-x(a). The exceptional case forces a and d,
so the full m=6 cycle certificate applies.

Thus, subject to independent audit and the stated global incidence
lemmas, m=1 and m=6 are excluded as retained mass-five local cores too.
