# Positive-output assembly: exceptional holes and two-level face patches

24 October 2026, 01:34 UTC. Complete WHITE cap-four translating front,
actual full P,d. Positive odd output is retained, including the already
known Nodd>=2||d||_infinity. No global zero-output hypothesis. Pending
independent review, including the simultaneous terrain interface3c25695f.

Use the all-output clockwise classification2c2d0905, the contact barriers
ad564468, and the exact scalar interpolation3c25695f. A TOP C-face node
means a clockwise four-edge node on sheet j=h(C). A BOTTOM L-face node
means a counterclockwise four-edge node on sheet j=h(L)+1. The word
BOTTOM matters: a four-edge L loop at a higher sheet is NOT declared
free or bottom merely from its geometric length.

THEOREM, pending review:

A. At any FIXED sheet j, the bounded disks of all counterclockwise
   contractible canonical nodes are pairwise disjoint, including all
   physical full-drift translates. They do not nest.

B. Let h_j count its distinct counterclockwise nodes that are NOT bottom
   L-face nodes. Then h_j<=Nodd. For j=M-1 the sharper typed capacity is

       h_(M-1)<=Nodd-Ntop+J,

   where J counts G3(M) source-sink path components. This extends the
   signed max-RIGHT stock-hole capacity to every exceptional penultimate
   contractible node, including raised four-edge L loops.

C. In the repaired graph, top C-face nodes are always the UPPER endpoint
   of every incident exchange; bottom L-face nodes are always the LOWER
   endpoint. Consequently every connected component induced only by
   these two elementary node types is confined to one adjacent pair of
   sheets: top C nodes at k, bottom L nodes at k-1.

Together with the pending essential sign rule3c25695f, this reduces
assembly to essential sign-preserving direct exchanges, two-level face
patches, and required positive-output exceptional nodes. It does not
exclude an assembled front or certify a necessary graph as realizable.

## 1. A clockwise unit loop encloses no other same-sheet contour

The signed all-output theorem makes every clockwise contractible node
on sheet j a C-face loop around height j. In the scalar triangulation,
its central C-face vertex has F=j>j-1/2. The four primal corner values
are below j-1/2, because each of its arcs is RIGHT; each adjacent L-face
value is also below the level, by active port support. Its disk is the
one high component in the star of that C-face vertex, with NO other
triangulation vertex inside. Therefore its entire open disk has
F>j-1/2 and contains no other sheet-j contour. This is stronger than a
choice of rounded sketch and follows from the single scalar field.

## 2. Counterclockwise same-sheet disks cannot nest

Suppose a counterclockwise circle gamma_in lay inside the bounded disk
of a counterclockwise gamma_out at the SAME sheet j. Both contours have
higher F on RIGHT. The outer side collar of gamma_in has F>j-1/2; the
inner side collar of gamma_out has F<j-1/2.

The high component containing the first collar is therefore physically
bounded inside gamma_out. Its outer boundary is a clockwise sheet-j
contour enclosing gamma_in. Section1 makes that contour a unit C loop
whose disk has no other same-level contour. This is a contradiction.
Hence the counterclockwise disks do not nest. Disjoint simple planar
contours can only have disjoint or nested disks, so the disks are
pairwise disjoint. The same argument applies to all physical translates
and handles short quotients without any primitive-drift replacement.

## 3. Every non-bottom counterclockwise disk needs an odd defect

Let gamma be a counterclockwise contractible sheet-j node.

If it contains a singleton-R corner, that actual singleton class is an
odd defect on its boundary. It belongs to only one canonical node.

Otherwise, if gamma has a RIGHT corner, it is non-singleton. The signed
turn-level inequality2c2d0905 puts an L sector<=j-2 on its LEFT, inside
the bounded disk. If gamma has no RIGHT corner, it has exactly four LEFT
corners and bounds an L face at some height m<j. Unless it is bottom,
m<=j-2, again giving such a low interior L face.

The L barrier confines the sublevel<=j-2 to this disk. Choose an actual
minimum plateau Q inside, as in signed e2161703. It is a locally minimal
finite physical L component. The signed reverse prepared-plateau theorem
ab9fad0a forces an odd-output incident corner, since its alternative is
an essential reverse curve, impossible inside a bounded physical disk.
No condition m>=c_left is imposed or needed.

Thus every exceptional node is paid either by a singleton-R on its own
boundary or by an odd root at an interior low minimum.

Different disks cannot reuse an odd physical cell. A low root touching
two disks would have either the same L face in both or two incident L
faces<=j-2 in different disks; the former contradicts disjointness and
the latter contradicts the L contact barrier. A boundary singleton-R
has both L heights j-1 and cannot also be a low root for another disk at
this sheet. Two boundary uses cannot share its sole occurrence. This
also prevents mixed payment reuse. Translating a proposed quotient
alias translates the disk, so physical nonoverlap proves injection in
the actual full quotient. Therefore h_j<=Nodd.

## 4. Typed penultimate improvement

At j=M-1, a singleton-R boundary payment has higher C height j=M-1 and
is NOT a top output. A top odd interior root at height<=M-3 can only be
a same-R three-read endpoint at L level M-3. Its G3(M) pairing remains
on the SAME minimum plateau. A complete path component therefore pays
at most one disjoint disk. Non-top root classes pay at most one each,
so h_(M-1)<=Nodd-Ntop+J. Bottom L-face loops are not in this count.
No extra output is added to earlier overlapping reservations.

## 5. Exact elementary-node sheet directions

All exchange levels at a two-R corner are a_v+1 (RIGHT) and a_v (LEFT).
A top C-face node contains only RIGHT arcs and its enclosed C height is
its sheet. Thus it can only be the UPPER endpoint. In a same-R profile
the upper RIGHT arc encloses C height a_v+2, not its own sheet a_v+1,
so that arc cannot lie on a top C-face loop; the flat case is consistent.
The lower endpoint is LEFT and cannot lie on a clockwise C loop.

A bottom L-face node contains only LEFT arcs. Thus it can only be the
LOWER endpoint. Its enclosed L height is a_v-1 at level a_v whenever
such a bottom loop occurs; a different low L height would instead be
a raised, exceptional L loop. The upper endpoint is RIGHT and cannot
lie on a counterclockwise L loop.

Hence a top C node at k can meet elementary bottom L nodes only at k-1,
and each of those bottom L nodes meets elementary top C nodes only at k.
Any connected elementary-only patch stays in those same two sheets.
This does NOT make the patch a tree, forbid parallel graph edges, bound
its size, or allow removal as a literal pose-preserving ant splice.

## 6. Exact remaining mechanism

Direct essential-to-essential exchanges preserve winding sign under
the simultaneous terrain interface. Opposite signs may still be linked
through elementary face patches or exceptional odd-root nodes. Required
positive odd defects can recur in the full quotient and can support
several DIFFERENT sheets, so the fixed-sheet bound must not be summed
over all j without a new injection. No original-fuel implication,
whole-front exclusion or actual complete positive construction follows.
