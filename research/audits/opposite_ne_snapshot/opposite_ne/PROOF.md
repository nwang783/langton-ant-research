# The three northeast-output retained-core channels

Status: exact source-depth certificates and all-age coupling completed;
independent review pending. No three-parameter arithmetic engine is used.

## Uniform finite-seed statement

Normalize the initial pose to(0,0),N, and write q_n=(-33-2n,-14-2n).
For phases r=29,56,62, respectively, define

    b_r=(-16,33),(-21,33),(-22,32),
    e_r=(2,57),(4,59),(2,45),
    s=b_r+m(-2,2),  d=e_r+m(-2,2)+k(2,2).

For every n>=200,m>=100,k>=200, the complete three-black input {q_n,s,d}
reaches a permanent standard southwest tail. Certified checkpoints are

    time208n+104m+104k+C_r,
    position(-2m+2k-44, 2m+2k+Y_r),

where, in phase order29,56,62,

    C_r=134992,129896,129688;
    Y_r=78,76,62;
    headings=S,S,N;
    canonical W phases=103,59,91.

No claim of earliest capture is made. If additionally n>=m+100, one may
add the two other rectangle corners

    a=(q_n.x,d.y), c=(d.x,q_n.y)

without changing a single read: both are never visited. Thus this is
also a uniform three-geometric-parameter five-black-cell theorem.
Its proof factors into a one-depth exact certificate and two half-plane
couplings, rather than inferring an infinite family from samples.

## Exact source-frame certificate

Use the audited canonical source with P containing13 black cells,
standard drift e=(2,-2), and12-cell deposit D. Its aged phase0 field is

    C_m=P union union_{j=1,...,m}(D-j e).

Let p_r be the phase-r read position of W from(0,0),S. Put BASE=(-15,29).
The source opposite cell is

    v_{r,k}=BASE-e_r-k(2,2).

For each r, certify_source.py starts with exactly

    C_100 union {p_r,v_{r,k}}, at head(0,0),S,

and checks the complete field for every k>=200. The canonical source
and the two toggles are not approximate local substitutes for this field.
The checker proves p_r is initially white, and the opposite cell lies
strictly below the source field and p_r in y.

The templates were discovered separately and carry no proof authority.
The exact checker verifies every finite color read, every read of its
k-dependent periodic corridor, and every read of the final infinite NE
source tail. It computes the following COMPLETE all-future source-u
bounds, where u=x-y:

    r29: -68<=u<=86;
    r56: -52<=u<=86;
    r62: -64<=u<=74.

For all periodic pieces, u is constant along the drift. Every affine
u expression has zero parameter coefficient, so these are uniform in k.
The final source tail has drift(2,2), hence also constant u. The checker
requires all periodic words to be canonical104-letter phases, and binds
the displayed output phase, time, position and u bounds explicitly.

The source capture times are104k+64254,104k+59158,104k+58950. Its final
positions are(29-2k,-49-2k),(29-2k,-47-2k),(29-2k,-33-2k), and headings
N,N,S. These values give the actual checkpoints after the rotation below.

The first opposite hit is bound to the already audited ordinary parent:
its time is that parent's source recovery time, plus the phase advance
to72, plus104k. This explicitly establishes that v_{r,k} is the proposed
exceptional opposite-corner branch, not an arbitrary sampled target.

## Every older source age is inert

All extra deposit cells for ages m>100 lie in

    union_{j=101,...,m}(D-j e).

Every such cell satisfies

    u <= max u(D)-4*101 = -395.

This is strictly below all three exact source read ranges. The difference
between the aged source fields is therefore never read. First-difference
coupling proves the exact same source word, pose and permanent tail for
EVERY m>=100, with no relation between m and k. No old field is discarded.

The checker also verifies the standard one-period deposition identity,
disjointness of distinct D translates, and disjointness of P from all
older deposits. These bind the all-age interpretation of C_m to the
actual repeated clean-period evolution.

## Coupling to the complete q_n history

The audited q_n parent is at BASE,N, W phase0, at time208n+70738. Its
complete field differs from the clean NW core by a stationary archive H1
with -82<=u<=58. After m NW periods, the complete canonical part is the
image of C_m under

    G_m(p)=BASE-p+m(-2,2).

The two new inputs map exactly: G_m(p_r)=s and G_m(v_{r,k})=d.
Neither is read earlier by the q-parent's finite prefix, because its
u lower bound is-82. The incoming NW leg misses d by its bounded z,
whereas z(d)=sum(e_r)+4k is already far larger at k=200. The first read
of s is the prescribed fresh phase r at epoch m.

Under G_m, source u maps to actual u=-44-4m-u_source. Thus every read
from the source checkpoint onward lies in

    r29: -4m-130 <= u <= -4m+24;
    r56: -4m-130 <= u <= -4m+8;
    r62: -4m-118 <= u <= -4m+20.

For m>=100 all upper bounds are strictly below-82. The entire perturbed
future therefore misses the unchanged H1, so it is valid on the actual
complete q_n field. Combining the source time with208n+104m+70738 gives
the stated three-cell capture formulas. This is the step that removes n
from the new exact computation, without erasing its history.

## The other two corners stay unread

For n>=m+100 and k>=200,

    u(a)=-2n-2m-2k-33-e_r.y,
    u(c)= 2n-2m+2k+14+e_r.x.

The checker verifies that u(a) is below the complete source-mapped read
range and below the incoming NW leg's lower bound. It is also below-82,
so a misses the earlier q-prefix. Similarly u(c)>58, above the whole
q-prefix and the entire later perturbed future. Both corners are therefore
unread at ALL times, including the infinite tail. Adding them leaves the
three-cell trace unchanged. This proves the full five-cell statement.

## Exclusion of the three retained-core rays

Fix m>=100 and one of the three core phases. At a hypothetical recurrent
mass-five subsequence retaining that core, the audited incidence lemmas
and blank-inertness force the first remote collider q_n, with n tending
to infinity. The complete ordinary two-bit parent after meeting s has a
NE tail and bounded u for fixed m.

Both four-edge strand shapes have all remaining cells escaping in u, so
they miss this parent entirely. In a four-cycle, a and c have u tending
to negative and positive infinity, respectively; only d can interrupt.
If d never does, the parent already captures.

An ordinary d-hit has complete future z>=z(d)-58, by the independently
audited favorable-sector guard. This misses the stationary ordinary-parent
archive, whose z upper bound is fixed, and misses a,c by the two diverging
axial gaps. Hence the only noncapturing possibility is exceptional phase72,
so d=e_r+m(-2,2)+k(2,2). The condition z(d) tending to infinity forces
k tending to infinity. Eventually k>=200 and n>=m+100, exactly the uniform
five-cell domain above. Its permanent SW capture is the contradiction.

This excludes the three whole retained-core rays for fixed m>=100,
conditional only on the previously audited global/ordinary lemmas and
the pending audit of this new source certificate and coupling. Combined
with the other nineteen classes, it completes all22 asymptotic fresh
classes of THIS incoming northwest frontier. It does not classify
arbitrary one-black parents, all retained-core locations in D82, or
arbitrary finite seeds.
