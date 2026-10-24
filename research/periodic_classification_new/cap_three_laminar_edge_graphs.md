# Simultaneous odd-edge and doubled-edge geometry under cap three

22 October 2026. Sections 1–4 independently analytically reviewed.
No general cap-three nonexistence theorem is claimed.

## 1. The two graphs

For a white-input translating front with at most three reads per physical
cell, let f_e be the number of traversals of a directed physical edge in
its full-drift quotient. All traversals of a given edge have the same
direction. Write

    f_e = h_e + 2 d_e,     h_e,d_e in {0,1}.

Let H be the graph of h_e=1 and D the graph of d_e=1. The already reviewed
odd-edge theorem says H has degree two at every read class and no other
vertices. Its components are embedded circles on the drift cylinder.

D has degree zero at a singleton, degree one at a double cell, and degree
two at a triple cell. At each triple cell one D edge enters and one leaves;
thus its components are directed paths and directed circles. A D path
starts at an RL cell whose two incoming headings are opposite, and ends
at an RL cell whose incoming headings agree. Equivalently it goes from
a sink of H's edge directions to a source of H's edge directions.

At an opposite-type triple (AAB or ABB), D makes a left turn. At a same-type
triple (AAA or ABA), D makes a right turn. Same-type vertices are paired
through a triple-used edge, with source ABA and target AAA, so their D
right turns occur in consecutive RR pairs.

## 2. A noncrossing simultaneous embedding

The apparent overlap of H and D can be resolved by small local isotopies.
At an opposite-type triple, H and D use complementary adjacent pairs of
ports, both directed left corners; these pairs can be joined disjointly
inside a small vertex disk.

For a same-type pair, normalize its triple edge to point east, u to v.
D enters u from the south, uses u-v, and leaves v to the south. H enters
u from the north, uses u-v, and leaves v to the north. Put the H lane just
north of the shared edge and the D lane just south. The two vertex-disk
connections then do not cross. Distinct same-type pairs are vertex-disjoint,
so all these resolutions can be made simultaneously.

At a double cell, H is straight and D ends there from one perpendicular
side. These endpoint incidences are retained. At a singleton only H is
present. Consequently H and D have a simultaneous embedding in the cylinder
with disjoint interiors, meeting only at endpoints of D paths on straight
H vertices. Every D circle is disjoint from H after resolution and hence
lies in one complementary region of H.

This is not a forest assertion. The previously saved exact cap-three
prefix has an all-white D square, and is consistent with this theorem.

## 3. Circles containing no same-type vertices

A D circle with no same-type vertices has left turns at every vertex.
It is therefore a counterclockwise unit square, not an essential circle
of the drift cylinder. Among its four triple vertices, exactly two are
AAB and two are ABB, and the two AAB vertices are consecutive around D.

Here is an exact chronology proof of the last sentence. Lift the square
to the plane. For its edges e_i in directed cyclic order let a_i<b_i be
the first and second traversal times, and put l_i=b_i-a_i. Repeated traversal
of one directed square-lattice edge is separated by at least four steps,
so l_i>=4. The middle L at the vertex between e_i and e_(i+1) gives

    AAB: a_(i+1)=b_i+1,
    ABB: b_(i+1)=a_i+1.

The center-time difference is therefore

    c_(i+1)-c_i = 1 + epsilon_i (l_i+l_(i+1))/2,

where epsilon is +1 for AAB and -1 for ABB. Sum around the four-cycle.
Zero AAB gives 0=4-sum l_i, impossible; four gives 0=4+sum l_i,
also impossible. With one AAB, the right side is 4 minus the lengths of
the two edges not incident to that vertex, and is negative. With three
AAB it is 4 plus the lengths of the two edges not incident to the ABB,
and is positive. With two alternating AAB the length terms cancel,
leaving 0=4. Thus exactly two adjacent AAB and two adjacent ABB are forced.
Their total contribution to the chronological Whitney sum is zero.

The chronology argument also works in a finite feasible cap-three trace
provided all four cycle cells have their complete initially white RLR
histories and the displayed two edge traversals are the corresponding
ones in those histories. Initial whiteness and a visually present square
alone are not substituted for those complete-history premises. This
scoped extension does not require a periodic trace. It does not exclude D circles containing same-type vertices.

## 4. Circle separation theorem

Independently analytically reviewed. This section concerns a complete
translating front, not an arbitrary truncated trace.

**Theorem. Every D circle is a counterclockwise all-opposite unit square.
All same-type vertices lie on D paths. In particular n2>=2.**

### Exact route labels

Label the first and third traversals of each triple-used edge D, and its
middle traversal H. On a double-used edge both traversals have label D;
on a single-used edge its traversal has label H. These are route labels,
not an assertion that a physical shared edge has a unique side.

At an opposite triple, the first and third R passages switch between H
and D, while the middle L passage stays on D. Both H ports lie to the
RIGHT of directed D. Hence all three local passages belong to the union
of D and its right side, with no passage into the left side.

At a same-type pair, normalize D to enter from the south, traverse the
shared edge east, and leave to the south. H enters from the north and
leaves north, so lies to the LEFT of D. Across the WHOLE pair the three
passages are RR, LL, RR. Their route types are D-to-D, H-to-H, D-to-D.
None switches between sides. Considering only one endpoint of the shared
edge would obscure this separation.

### Successor-invariant side partition

Let gamma be a D circle in the simultaneous embedding. A simple circle
separates the cylinder into two components, whether it bounds a disk
or is essential. Use its direction to call the components left and right.
Partition the actual event phases as follows:

- The right-side set contains all events strictly in the right component,
  all D passages on gamma, and therefore all three events at each opposite
  vertex of gamma.
- The left-side set contains all events strictly in the left component
  and the middle H passages at same-type pairs on gamma.

The local route table above shows that neither set sends a successor
event into the other. Other lattice edges cannot cross gamma except through
the listed port configurations; the exact H/D labels handle the shared
triple edges. These sets exhaust all event phases.

The right-side set is nonempty, since gamma has D traversals. If gamma
had a same-type pair, the left-side set would also be nonempty. But event
successor in a full period is the single cyclic permutation
0 -> 1 -> ... -> P-1 -> 0. It has no nonempty proper invariant subset.
This contradiction excludes every same-type vertex on gamma.

Thus gamma has only left turns, and Section3 shows that it is a
counterclockwise unit square with consecutive AAB,AAB,ABB,ABB. In particular
there are no essential D circles. This essential-circle exclusion is
NOT a claim that its physical lift closes: it uses separation of the
cylinder and cyclicity of the full event permutation, not a bounded-face
or zero-voltage time argument.

For comparison, in the contractible case one can also lift to a disk.
A clockwise gamma would trap its nonempty D routes in a bounded region;
a counterclockwise gamma with a same-type pair would trap that pair's
middle H route. A nonempty finite set of physical read times cannot be
closed under successor. The cylinder argument above is stronger and
keeps the essential case distinct from this bounded-disk argument.

### At least one D path

If n2=0, D has no degree-one vertices, so every D component is one of the
unit squares just classified. Every opposite triple lies on exactly one
such square. Each square contributes A-B=0 by Section3; the same-type
count is zero. Hence the complete chronological Whitney sum is zero,
contradicting g/4>0 for a finite-seed translating front. Therefore n2>0;
the independently proved evenness of n2 strengthens this to n2>=2.
