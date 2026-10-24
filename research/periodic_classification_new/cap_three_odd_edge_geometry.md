# Cap-three odd-edge geometry and an all-drift growth congruence

22 October 2026, 22:22 UTC. Independently analytically reviewed on 22 October 2026.
The result is a necessary classification of local geometry and multiplicity,
not an exclusion of every cap-three front.

## Setting and odd-edge graph

Let a finite-seed translating periodic front have full displacement
 d=(a,b) != (0,0), restore its heading, and have at most three reads in each
full-displacement class. Its stable class histories are R, RL, or RLR.
Let n1,n2,n3 be their counts and g=n1+n3 the growth per period.

On the lattice cylinder Z^2/Zd, retain an undirected edge precisely when
its traversal multiplicity is odd. Keep parallel edge identities when
quotienting. Call the resulting finite graph H. All traversals of a physical
edge have one direction, by the checkerboard heading-axis invariant.
Use these actual directions when referring to an incoming/outgoing port.

### Local table

Write J for a clockwise quarter turn, and normalize a class's first
incoming heading to A. Odd incoming/outgoing headings are:

    history   incoming-heading list   odd incoming   odd outgoing
    R         A                       A              JA
    RL        A,A                     none           JA,-JA
    RL        A,-A                    A,-A           none
    RLR       A,A,A                   A              -JA
    RLR       A,-A,A                  -A             JA
    RLR       A,A,-A                  -A             JA
    RLR       A,-A,-A                 A              -JA

The table follows by counting the incoming and outgoing ports modulo two.
It proves:

1. Every read class has degree exactly two in H. There are no hidden read
   classes whose every incident edge has even multiplicity.
2. An R class is a right-turn corner of H.
3. An RL class is a straight vertex, with its two odd edges both incoming
   or both outgoing.
4. An RLR class is a left-turn corner of H.

Thus H is a finite disjoint union of cycles, including possible length-two
cycles formed by parallel quotient edges. Its geometric corners are exactly
the odd-multiplicity wake classes.

## 1. All-drift congruence

Heading reset gives an even period and a+b even. The square-lattice checker
color therefore descends to the full-drift quotient. H is bipartite, so each
of its cycle components has an even number of vertices. Consequently its
total vertex count V=n1+n2+n3 is even. Since g is a multiple of four, n2=V-g
is even.

The independently reviewed chronological Whitney identity says

    g/4 = K.

An R or RL class contributes zero to K; an RLR class contributes +1 or -1.
Therefore K = n3 modulo two. On the other hand,

    P = n1+2n2+3n3 = g+2(n2+n3),
    P/2 = n3 (mod 2),

using 4|g and 2|n2. There are exactly P/2 horizontal and P/2 vertical
moves, so a=b=P/2 modulo two. We conclude

    g/4 = a = b (mod 2),
    equivalently g = 4a = 4b (mod 8).                    (1)

For example, no cap-three finite-seed periodic front can have even-even
drift and growth congruent to four modulo eight. In particular growth12
with drift(2,2), drift(2,-2), or any even-even drift is excluded under cap
three. No restriction on the period, width, or supplied wake is assumed.
The statement does not exclude all cap-three fronts: growth8 with even-even
drift and growth12 with odd-odd drift survive this congruence alone.

## 2. A supplied non-axis wake fixes every multiplicity and the exact period

Assume additionally a*b != 0 and prescribe the finite odd wake O. The
existing odd-edge reconstruction theorem gives H directly from O: on each
horizontal and each vertical quotient line, pair successive O vertices by
finite intervals. This reconstruction is unique because the quotient lines
are infinite paths, not cycles.

The cap-three theorem above then gives an exact necessary geometric test:

- The reconstructed graph must have degree two at every one of its vertices.
  Any degree-four crossing excludes cap three at every period.
- Every vertex of the reconstructed graph is read; no additional read class
  outside it is possible under cap three.
- Choose the checker/heading-axis convention. Direct horizontal edges from
  horizontal-outgoing vertices and vertical edges from vertical-outgoing
  vertices. A directed right corner has multiplicity1, a straight source or
  sink multiplicity2, and a directed left corner multiplicity3.

Hence all multiplicities, and the exact period

    P = N_right + 2 N_straight + 3 N_left,

are determined by the supplied wake and the checker convention. If the
convention is not prescribed, there are only its two possibilities; reversing
it exchanges the right and left corner roles. This is stronger than merely
having an upper period bound for that fixed wake, but it is still not a
realizability theorem. Chronological edge-rank matching and the one-tour
condition can fail after this geometric test passes.

The non-axis hypothesis in this section is essential for wake-only edge
reconstruction. The all-drift congruence (1), using the actual odd-edge graph,
remains valid for axis drift.

## Scope and provenance

The odd-edge reconstruction used in Section2 is an existing result, not new:
`../sources/kehao95-core/wake_synthesis/verification/general_wake_parity/PROOF.md`,
Section2. The new cap-three observations are the exhaustive degree-two local
table, the forced multiplicities/exact period, and the congruence obtained
by combining that topology with the integer chronological Whitney identity.
No global cap-three exclusion, period classification, or priority claim is
asserted.
