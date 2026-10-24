# The one-sided initially-white first-departure forest has at most m+1 roots

23 October 2026, 11:22 UTC. Stronger nonperiodic analytic candidate.
The independently signed nested-cycle statement is a weaker consequence.
No eventual-periodicity, finite visit cap or finite-width assumption.

Consider an ordinary infinite ONE-SIDED Langton trajectory from head o at
time0 on an arbitrary initial board. For every visited INITIALLY-WHITE
cell v let T(v) be its first read time, I(v) its first read heading, and
b(v) the target of that first R departure. Include visited initially-black
cells as TERMINALS with no outgoing b edge. At o the first heading is the
given initial heading, NOT a fictitious predecessor arrival.

THEOREM CANDIDATE:
1. Every b-path reaches an initially-black terminal or one exceptional
   unit-clockwise cycle through o.
2. That cycle exists exactly when the actual first four turns are RRRR;
   its four vertices are precisely the initial unit face at times0,1,2,3.
3. Hence with m initially black cells, the complete graph has at most
   m+1 weak components, each a terminal-rooted tree or the exceptional
   cycle with trees feeding it. Infinite incoming trees are permitted.

This is a global finite-seed causal-forest theorem, NOT a bounded bad-step,
branch-count, record, period or capture theorem. The same root can support
unbounded or infinite branches.

## A. Exact first-time inequalities along white b edges

On a white b-path, consider a target white vertex v entered from u.
Its outgoing edge b(v) is R(I(v)). If the geometric path turns RIGHT at v,
its incoming heading equals I(v). For v!=o, the first R at u is the first
use of u->v, and v's FIRST incoming edge is that same physical edge, so

    T(v)=T(u)+1.

For v=o the initial incoming-edge exception is retained; only
T(v)<=T(u)+1 is asserted. Their time difference is still1 modulo4.
If the path turns LEFT at v, its incoming heading is -I(v), so this is a
later read of v, at least four steps after its first read:

    T(v)<=T(u)-3.

Both conclusions hold at arbitrary visit multiplicity and through any
initially-black interior geometry. These first-time statements are only
used while both source and target are initially white.

## B. No infinite simple b-ray

Four consecutive RIGHT corners of a unit checker path close a unit face,
so a simple b-ray has at most three consecutive RIGHT corners. Partition
its target-corner sequence into blocks R^r L with0<=r<=3, with a possibly
unfinished first/last R run. Across every complete block, the first-time
increment is at most r-3<=0. At every prefix it is at most+3. Therefore

    0<=T(v_i)<=T(v_0)+3

throughout the hypothetical infinite simple white b-ray. Distinct
physical cells have DISTINCT integer first-read times. The ray would
contain at most T(v_0)+4 distinct white vertices, a contradiction. This
argument is for a ray, not a separate no-four-R assertion about a truncated
finite path just before an exceptional unit-cycle closure. Every b-orbit must therefore
reach a black terminal or repeat a white cell, forming a finite cycle.

## C. The only finite cycle is the initial unit face

A simple finite checker cycle has length ell divisible by four. At each
RIGHT corner use T(v)-T(u)=1-4q_v with q_v=0 except possibly at o, where
q_v>=0. At each LEFT corner q_v>=1. Summing gives

    ell=4Q,       Q>=m_L.

Counterclockwise turning m_L=m_R+4 is impossible. For clockwise turning,
m_L=(ell-4)/2, so ell>=4m_L gives ell<=8. Thus ell is4 or8.

A simple checker eight-cycle cannot exist. It would have six R and two L
corners. A run of four R would already close a proper unit face, violating
simplicity. Its two R runs must therefore both have length3, and its cyclic
turn word is(RRRL)^2. Starting with incoming N, its successive positions are

 (1,0),(1,-1),(0,-1),(0,-2),(-1,-2),(-1,-1),(0,-1),(0,0).

The third and seventh positions coincide. Rotation/cyclic shift do not
remove this repetition. Hence ell=4 and every corner is RIGHT.
If o were not on the cycle, every first-time increment would be+1,
impossible around a closed cycle. So o is a vertex. Starting there at
T(o)=0, the three other increments are exact+1; these are the actual first
three successor reads and their first R departures. The first four turns
are RRRR. Conversely those literal four initially-white R reads give this
unit b-cycle. There is at most one because a functional graph has disjoint
cycles and only one can contain o.

## D. Component count, and the precise remaining gap

Every forward orbit has just been shown to reach a terminal or that one
cycle. Adjacent vertices in the underlying undirected b graph have the
same eventual root, so each weak component has exactly one such root.
There are at most m initially-black terminals, plus at most one unit cycle.
This proves the m+1 component bound.

It does NOT bound the number of vertices in one component, its number of
branching vertices, its number of infinite ends, or the ant's later reads.
In particular the two negative first-departure cycles of a standard104
FULL-DRIFT quotient may lift to two infinite incoming branches of the SAME
one-sided root component. There is no contradiction and no capture proof.
