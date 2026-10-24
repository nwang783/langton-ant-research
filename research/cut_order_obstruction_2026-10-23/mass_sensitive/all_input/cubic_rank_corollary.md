# Historical reconvergence rank gives a direct cubic physical bound

23 October 2026. Conditional theorem, combining the exact all-input incidence
identity with the independently signed HS epoch-reset theorem. No rank budget
is proved here. This sharpens, rather than invalidates, the weaker iterated
bound in `reconvergence_budget.md`.

Consider a physically feasible, context-complete factor of the eight recurrent
packets D, DC, V, VC, VCC, U, UC, UCC, starting with complete black mass m and
r0=m-5 residual identities. Retain the entire historical incidence graph,
including every input, every fresh output, and every retired identity. Let
beta be its undirected cycle rank and c its component count. The graph is
initialized with ALL r0 residual roots, including unread isolated debris.

A nonempty factor has r0>=1 and c>=1. The exact identity is

    beta=v+4u-r0+c.

Consequently, if beta<=B at the factor's endpoint, then

    u<=U_B:=floor((B+m-6)/4).                         (1)

Historical beta is nondecreasing, so an endpoint bound also bounds every
prefix. B is assumed to be a nonnegative integer. Empty factors, including
r0=0, have duration zero and are handled separately.

## Direct cubic duration and confinement

The signed theorem `../../../word_stabilization/dcuv_epoch_reset_bound.md`
(HS, independent controls `../../../audits/check_dcuv_epoch_reset_independent`)
states, for an ACTUAL chronological factor with u U-family packets,

    b=57+38(m-5)+60u,
    R=ceil(2b/5), t=floor((2R+1)^2/3),
    duration <= F(m,u):=20R(t+1)+28t.                (2)

Every visited or newly produced cell lies in the radius-R square about the
entry head. Remote initial debris can remain outside the square, untouched.
The right sides are nondecreasing in u. Therefore define b_B,R_B,t_B by (2)
with u=U_B. Every nonempty factor with historical rank at most B has

    duration <=20 R_B (t_B+1)+28 t_B,
    every visited/newly produced cell within radius R_B.       (3)

This is O((m+B)^3), independently of initial seed diameter. For a slightly
looser radius requiring no floor in (1),

    b_B<=53m+15B-223,
    R_B<=ceil((106m+30B-446)/5).

This is a genuine sufficient condition for finiteness in the recurrent-eight
language. It is not a proof that physical beta is bounded. It repackages the
signed U-count theorem through an all-input historical resource.

For fixed entry mass m, every infinite physical recurrent-eight tail would
therefore require unbounded beta. More quantitatively, (3) forces historical
beta(T)=Omega(T^(1/3)) as fine duration T tends to infinity. No contradiction
follows from this necessary growth rate. The relevant hidden resource is
historical RECONVERGENCE, not directed causal cycles or the number of roots.

## An exact sibling-join lower bound

At a target packet, suppose its a current input identities lie in g historical
components. Adding the packet and its outputs gives

    delta beta=a-g.

If k>=2 inputs are still-current outputs of ONE earlier packet, those k
identities already lie in one component, because their producer and its edges
remain in history. Thus g<=a-k+1 and

    delta beta>=k-1.                                (4)

More generally partition the target inputs by actual historical component;
delta beta is the sum over nonempty input classes of (class size minus one).
For several disjoint sibling groups the sum of their k_i-1 is a lower bound,
whether or not their groups have already joined elsewhere. These are
simultaneous target-input statements. A sibling retired earlier by unary D
need not create any rank, and cannot be counted again merely because its
cell or a replacement identity later reappears.

The finite DC spare-only template layer exhibits this exact dichotomy: a
unary D helper on one original spare has delta beta=0, while a V helper on
two still-current source spares has delta beta=1. Template compatibility
alone does not supply a jointly executed history. The symbolic investigation
has separately found an actual DC,VCC,V,V factor whose last V rejoins two
first-DC siblings from a singleton-root component; its frozen proof and direct
literal audit are separate dependencies. Such an event imports no new root
into that component. No new-root-per-cycle charge may be assumed.

## Remaining bridge

Finite initial roots pay only r0-1 cross-component merger units. They do NOT
pay reconvergences inside already joined ancestry. To finish a fixed-mass
physical argument using (3), one must prove an independently bounded rank
budget using literal chronology, geometry or an irreversible interaction
resource. Directed acyclicity, stabilized ancestor-root sets, planarity of a
resource DAG and compulsory spare retirement alone do not supply that budget.
The explicit aged resource countermodel keeps those latter marginal features
(except no planar claim is needed) while beta grows forever. It omits literal
packet masks, the transported core, full white context and endpoint continuity.

This theorem has no claim outside the context-complete recurrent-eight
language and no universal finite-seed capture conclusion. Independent review
requested.
