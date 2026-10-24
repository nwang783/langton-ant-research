# All-cap active-C first-entry and last-exit ownership

24 October 2026. Author proof and exact controls; independent audit pending.
This is a necessary physical causal scaffold, not a controller classification,
a WHITE unit-winding proof, or a new multiplicity bound.

## Setting and precise objects

Let an actual stable translating R/L word have period P, restored heading and
supplied full nonzero drift d. Use every physical read in its two-sided repeated
history. Each physical cell has its complete finite alternating history. Its
first read may be BLACK in the prepared controls; a complete WHITE front has
no such BLACK-first classes. No input, output, internal lifetime, or unread
background field is removed or changed here.

The active C face is the square immediately to the right of the incoming ant
edge. If its read cell is (x,y), its lower-left coordinate is respectively
(x,y-1), (x-1,y-1), (x-1,y), (x,y) for incoming N,E,S,W. An R keeps this face;
an L moves to the other C face diagonally opposite across that read cell.
All active C faces have one checker parity. Their physical adjacency graph is
a rotated square lattice. This is NOT the physical BLACK w-component and is
NOT the compressed H/V lifetime-boundary graph.

Every physical C face has finitely many visits, because d is nonzero. Write
A(v) and B(v) for its first and last active cut times. Include every active cut,
not just L events or first/last reads. A(v+d)=A(v)+P and similarly for B.
There are finitely many C-face classes modulo the FULL d.

## First-entry ownership

The step just before A(v) must be L, from a C face u to v. Select the physical
edge v -> u, directed backward along that step. This L is the FIRST L of its
physical read cell: any earlier L there would already have activated both u
and v. Thus exactly one of the following holds:

1. WHITE-first cell: the selected read is L1, owned by its actual R0, and R0
   has the SAME incoming heading as L1. Indeed the two possible arrival
   headings at a cell differ by180 degrees. If the headings differed, R0
   would already have been based at v, contradicting its first activation.
   Therefore R0 took place at u, strictly before L1.
2. BLACK-first cell: the selected read is its initial L0. It has no preceding
   R owner in that physical history. These edges must remain marked inputs.

In case1 the actual source age a=L1-R0 is a positive multiple of4, at least4.
The canonical parent-clock gap is

    A(v)-A(u) = 1 + a + [R0-A(u)] >= 5,

where the physical occurrences of u and v on this selected edge are used.
In case2 the same gap is at least1. These are exact ownership identities,
not an assumption that every BLACK input is a discovery step. Inputs may
instead enter a C face that has already been active.

## Last-exit ownership

At B(u) the update must be L; otherwise R would keep u active at the next cut.
Select the physical edge u -> v traversed by this L. It is the LAST L of its
physical read cell, since any later L there would reactivate u.

If the complete read history ends L, there is no following read. If it ends R,
that R is immediately next in the cell's read order, is the permanent output,
and its incoming heading is OPPOSITE that last L. A same-heading R would
reactivate u after B(u). Thus the last R is based at v and

    B(v)-B(u) >= R_last-L_last >= 4.

For an edge whose cell ends L, B(v)-B(u)>=1. Initial BLACK-first histories are
allowed in both conclusions. The final R remains a distinct output root even
when its class also has an initial BLACK input.

## Embedded full-winding cycles

Each C-face class has exactly one first-entry parent and exactly one last-exit
target. Each selected physical read-edge orbit is used at most once in either
graph, since a cell has just one first L and one last L. The two graphs are
therefore embedded functional graphs on the actual C lattice modulo full d.
A functional cycle is simple as an embedded curve on this cylinder; parallel
edges and one-edge loops in the quotient are retained, not discarded.

For a first-entry arrow v -> u+nu*d, define its positive clock gap
A(v)-A(u)-nu*P. Summing around a cycle gives -P sum(nu)>0. A zero-winding cycle
is impossible. A simple essential cylinder curve has primitive winding, so
EVERY first-entry cycle has full winding exactly -1 and the gaps sum to P.
The last-exit graph similarly uses gap B(v)+nu*P-B(u)>0, so EVERY cycle has
full winding exactly +1 and its gaps sum to P.

Deleting ONLY the marked BLACK-first entry edges leaves a WHITE-parent
functional forest with some rooted components and some intact -1 cycles.
For a complete WHITE front, no edge is deleted: at least one actual embedded
essential cycle of same-heading R0/L1 ownership is forced. This does NOT say
that its read cells are single-used or have any visit cap. A WHITE-parent
cycle of length ell satisfies the derived clock bound P>=5ell. A last-exit
cycle with ell edges, o of whose cells end R, satisfies P>=ell+3o. These are
bookkeeping consequences, not the point of the reduction or a classification.

## Exact supplied controls and counterchecks

The certificate reconstructs ALL read histories and ALL active-C histories,
all arrows, physical read owners, seam voltages, clock gaps and cycles for:

- standard104:10 C classes, I0/O12, two first-entry cycles, both WHITE-owned,
  and two last-exit cycles. One first-entry cycle uses histories NNS and NNSN;
  the other uses NNSNSSN and NNSNNSSN. High multiplicities are real, not ignored.
- prepared1564:292 C classes, I197/O301,168 BLACK first-entry edges; one full
  first-entry cycle but no cycle after deleting those input edges; one last
  cycle. Its29 other input classes enter already visited C faces.
- prepared4352:592 C classes, I406/O590,319 BLACK first-entry edges; one full
  first-entry cycle but no WHITE-parent cycle; one last cycle. Its87 other
  inputs likewise do not enter new C faces.
- prepared10 RRRRLLLLRL:two C classes, I1/O1, NO BLACK first-entry edges; one
  WHITE-parent -1 cycle and one last-exit +1 cycle. Its genuine BLACK input L5
  enters an already visited face. Thus a fully WHITE-owned discovery scaffold
  does NOT establish the no-input premise or bound lifetime boundary winding:
  this actual prepared word has lifetime boundary S=3.
- prepared80:14 C classes, I2/O14,one BLACK first-entry edge,one full first
  cycle but no WHITE-parent cycle,one last cycle. The other BLACK input is
  again not a discovery entry. Its S=3 and full fields remain as signed before.

These are the supplied stable words with their already signed full field
interpretations, not newly claimed WHITE realizations. The script checks105
rotation/full-period-power/phase controls. Powers multiply face/input/output
and discovery-root counts, but the numbers of essential cycles remain fixed;
all retain full winding ±1. No equality of first-cycle and last-cycle counts
for arbitrary actual words is asserted merely from these examples.

## Exact remaining obligation

The first/last C graphs are spatially embedded, unlike the combined projected
H/V lifetime-boundary graph. Their relation to its multiple-time ownership is
still unproved. Neither one discovery cycle, absence of discovery input roots,
small ages, output forests, nor head-connectedness can replace no-input
ownership. Standard has two discovery cycles; prepared10 hides its input from
the discovery roots; the separately signed blank transient permanently
freezes an output-only contractible lifetime circuit and cyclic w support.
No WHITE S1 result, four-type exclusion, new translating controller, or global
finite-seed attraction follows from this scaffold alone.

## Artifacts

certify_active_C_entry_exit_forests.py reconstructs the graphs from the words.
active_C_entry_exit_forests_certificate.json stores all complete histories and
arrows, the five base controls and105 representation checks. Dependency hashes
are embedded in the certificate. All earlier signed artifacts are preserved.
