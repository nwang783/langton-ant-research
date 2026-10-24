# Simple center paths impose a finite C lifetime on produced residual inputs

23 October 2026 17:17 UTC. This is a geometric turning consequence, not a
larger counted-age enumeration, a component budget, or a capture theorem.
The topological argument has passed analytic review; the frozen literal role
maximum and source-clock conversion are submitted for independent replay.

## Nearby-return turning bound

Let P be a finite injective corrected-center atomic subarc in the actual
D/V/U/C splitting of a complete recurrent-eight factor. Its endpoints A and
B are atomic cuts. Let n be the number of C atoms between these cuts, and put

    dx = |B_x-A_x|, dy = |B_y-A_y|,
    N = (dx+11)(dy+11).

The center coordinates are half-integers, so dx and dy are integers. Then

    n <= 8N+11.

If the two cuts coincide, injectivity makes them the same path parameter and
n=0. The nontrivial proof below assumes distinct endpoint centers. No bound
on the length, diameter or number of zero-C atoms of P is assumed.

Choose a point W generically inside the rectangle spanned by A and B,
expanded by one in each coordinate. The two straight segments B--W--A form
a simple closing bridge. Since P is finite, W can avoid the finitely many
lines or segments causing collinearity, tangency, passage through an old
vertex, coincidence with P, or an opposite endpoint corner. Thus the closed
polygon has only finitely many ordinary transverse crossings between the
bridge and interiors of P's atoms, away from its intentional A/B closure.

Every atomic chord has coordinate span at most four: the corrected steps
are D/C=(1,1), V=(1,3), U=(0,4), up to rotation. Therefore an atom meeting
the bridge has its entry center inside the A/B rectangle expanded by five.
That rectangle contains exactly N half-integer lattice sites. Injectivity
makes all atomic entry centers distinct. Each straight atomic chord meets
each of the two generic bridge segments at most once. Hence the number k
of transverse crossings is at most 2N.

For completeness, the elementary turning-index bound for this closed curve
is |I| <= k+1. At a transverse crossing, split the oriented curve into its
two closed subcurves. Their newly introduced principal corner angles cancel,
so their signed turn sums add to the original sum. Repeating on self-crossings
leaves at most k+1 simple Jordan polygons, each of turning index +1 or -1.
Intersections between distinct resulting polygons do not affect this sum.
This proves the bound without assuming the original closed curve simple.

Let a_first and a_last be the first and last atoms of P, and let e_last be
one if its last atom is C and zero otherwise. The independently signed
atomic tangent lift gives the EXACT open turn sum

    T_open = pi*(n-e_last)/2 + alpha(a_first)-alpha(a_last),

where alpha(D)=alpha(C)=pi/4, alpha(V)=atan(1/3), alpha(U)=0. All principal
turns use this same lift, with no hidden whole-turn adjustment. The two
endpoint corners and the corner at W contribute at most 3*pi in absolute
value. Consequently

    pi*n/2 <= |T_open| + 3*pi/4
              <= 2*pi*|I| + 15*pi/4
              <= 2*pi*(k+1) + 15*pi/4.

Thus n <= 4k+11.5. Since n is integral, n <= 4k+11 <= 8N+11.
Retaining e_last is essential when the target cut immediately follows C.

## Literal producer-to-consumer specialization

Suppose a current residual identity was freshly installed by a full packet
inside this simple factor, and is later consumed by another full packet.
Normalize its producer entry head and heading to (0,0,N). If o is its output
slot, i the consumer input slot, and h the relative consumer heading, then

    consumer head p = o - rotation_h(i),
    A = (-1/2,-1/2),
    B = p + rotation_h(-1/2,-1/2).

These are the PRODUCER ENTRY and CONSUMER ENTRY atomic cuts. The ordered
source-included/consumer-excluded C age is exactly their clock difference n.
For a source with one or two C tails, do not replace the full source birth
clock by the output's later atomic installation clock: the entire source
prefix is included in this subarc, exactly as required by the age convention.

The literal retained geometry has 68 output slots and 23 input slots. Across
four relative headings there are 6,256 alignments. Conserved boundary sector
removes half. The complete 3,128 remaining role alignments satisfy

    (|B_x-A_x|+11)(|B_y-A_y|+11) <= 289.

A maximizing literal example is source UCC output (-2,6), target U input
(-1,4), relative heading E, consumer head (-6,5). Here B-A=(-6,6), so the
rectangle count is 17*17=289. This is a conservative static role maximum,
not an asserted feasible transfer or an attaining age example. No HB or
counted-age clause is needed to reduce the bound.

Therefore EVERY produced residual input whose source and consumer lie in a
simple corrected-center factor has source-included C age at most

    8*289+11 = 2323.

In particular this applies to all produced inputs of a complete factor which
begins U, UC or UCC, by the independently signed U-entry simplicity theorem.
It includes internal atomic cuts in the geometric proof but compares actual
FULL-packet entry clocks in the residual-age corollary.

## Irreversible old archives, within the stated factor only

If a produced identity is still current more than 2,323 C increments after
its full source-entry clock, no later complete packet in the same simple
factor can consume it. Any hypothetical later consumer would violate the
bound above. By the ordered complete-context ledger, such an unconsumed
identity also remains outside every later packet's complete context. It is
therefore a permanent residual archive cell throughout that factor.

This does not apply to untouched entry identities, to sources before the
chosen factor boundary, or to arbitrary later ant history outside the
retained language. It does not bound the total number of permanent archive
cells, their component mergers, U count, raw duration, or C count. Infinite
spiral-like growth is not excluded by this lifetime statement alone.
