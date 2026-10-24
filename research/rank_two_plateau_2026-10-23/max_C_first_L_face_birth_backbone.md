# Every maximum C plateau carries a first-L face-birth backbone

23 October 2026, 12:55 UTC. New analytic theorem submitted for independent
review. No front exclusion or finite-seed capture conclusion. This is a
closed rank-two chronological coupling on FACES, not an assertion that
the second-R cell graph has no gates.

## Hypotheses and notation

Consider a COMPLETE bi-infinite WHITE translating front of cap four,
with actual full event period P and nonzero full displacement d.
Use signed f(e)=h(C_right)-h(L_left) and H(C)=h(C),H(L)=h(L)+1.
The signed global-maximum theorem gives

    M=max_C h=max_all H,
    h(L)<=M-1 for every L face.

Thus all four directed boundary edges of every max-C face F have positive
flow. For an active directed physical edge e define tau(e) as the actual
time of its FIRST traversal (departure time). Then

    tau(e+d)=tau(e)+P.

No phase is substituted for this physical first-traversal time.

For a maximum C face put

    B(F)=min{tau(e): e is one of F's four boundary edges}.

The minimum is unique: different physical directed edges are traversed
at different actual ant times. B(F+d)=B(F)+P.

## 1. The minimum boundary edge is a first-L entry, followed by second R

Let e be F's unique minimizing edge, departing corner v at time B(F).
Let e_minus be the incoming directed boundary edge of F at v. Since e
is the unique minimum, tau(e_minus)>tau(e). In particular the first
F-output departure happens BEFORE the first F-input arrival at v.

At v the cap-four R-count rule ensures every R selects a maximizing C
face, hence either F or an equal-height C face G across v. The following
local statement is exact:

If F is maximizing locally and both F boundary ports have positive flow,
the first F-output precedes the first F-input if and only if

- v is flat: its R0 chooses the other C face G and its R2 chooses F;
- the incoming heading at L1 equals the R0 heading;
- the first F-output is source L1, and the first F-input is target R2.

Proof: if R0 selects F, it is first at BOTH F ports and its input edge
was traversed one step before its output; impossible here. If R0 selects
G while F remains maximizing, the two R counts must be(1,1), so R2
selects F. L1 shares exactly one F port. If it uses the F input, that
input precedes the first F output R2; if it uses the F output, that
output L1 precedes the first F input R2. No L3 can be first at either
F port, because R2 has already used both. This exhausts the complete
cap-four table and retains source L1 rather than relabeling it R2.

Therefore e's source has the complete prefix

    R0 around G, L1 from G into F, R2 around F,
    incoming headings (h,h,-h), turns R,L,R.

Both F and G have height M. In particular their corner contact is active
and belongs to the same max-C component.

At this selected corner,

    B(F)=T_1(v),
    tau(e_minus)=T_2(v)-1,
    B(G)<=T_0(v)-1.

The last bound uses the G incoming edge's FIRST traversal into R0 at v.
Consecutive local return gaps are positive multiples of four, so

    B(F)-B(G)>=T_1(v)-T_0(v)+1>=5.       (1)

This is stronger than merely an earlier neighboring first R. It ties
the selected maximum-face birth to the actual first L, and the later
second R to the not-yet-used incoming F port.

## 2. A closed face predecessor, not a second-R gate

Define a face predecessor p(F)=G using that unique minimum edge. This
is an outdegree-one map on ALL maximum C faces and is full-drift
equivariant. It never leaves the same corner-connected max component.
There is no initial-head, input-black terminal, or dropped R0 node in
this definition. Crucially, the source L1 at the selected contact is
retained and is exactly the ACTUAL C-face transition G->F.

Every max-C component has finitely many face classes on the full-drift
cylinder. Indeed the signed global maximum M exceeds both exterior
unshifted C constants, so maximum C faces lie within the finite-width
active strip. The quotient map p therefore has a directed cycle in EACH
maximum component.

The cycle edges lie in the natural diagonal C-face contact lattice:
join opposite C-face centers through their common primal corner. This
is an embedded square lattice rotated45degrees. Its distinct edge
interiors do not cross: the other diagonal through any primal corner
joins L faces, not C faces.

The functional cycle has distinct face classes before closure. It cannot
traverse the same contact in opposite directions, since F->G there
requires R0 at that corner around G, while G->F would require the same
R0 around F. Thus a two-edge backtrack is impossible. The resulting
quotient cycle is a simple embedded cylinder circle, including ordinary
multiple-edge or one-edge essential loops in a small full quotient.

Let a lifted p-cycle run from F0 to F0+k*d. Sum the strictly decreasing
B values in (1). It gives kP<0. Embedded simplicity restricts winding
to0,+1,-1; therefore k=-1. Reverse the cycle. Its geometric orientation
is exactly the ACTUAL first-L face transition G->F at each selected
contact, and its full winding is PLUS ONE.

THEOREM: every maximum C plateau of a complete white cap-four front
contains a positive essential cycle of actual FIRST-L transitions, each
at a flat contact where R0 uses the parent max face and R2 uses the child
max face. This is a face-level backbone built from actual rank1 and
rank2 chronology. It does not require a homogeneous R2 cell cycle.

This face cycle is not asserted to be one uninterrupted actual ant
interval. Its diagonal edges are NOT physical directed grid edges and
must not be subtracted as though they were physical integer flow.

## 3. A safe face-cycle length clock

If a p-cycle has ell distinct face classes, reverse orientation and sum
(1) over its ell transitions. Full winding+1 gives

    P>=5*ell.                                         (2)

Every diagonal C-contact edge changes each Cartesian coordinate by1
in absolute value. Therefore ell>=||d||infinity=D and P>=5D. This last
numerical relation is weaker than the existing all-cap P>=8D and is not
advertised as an improved speed bound. The new information is the
L1/R2-labeled essential face structure and the length-sensitive(2).
Its chronological increments can be retained as one whole-cycle bound;
do not add it to overlapping first-read bounds.

## 4. Exact local first-port curl identity

There is a useful equivalent local accounting, before choosing a minimum.
For ANY global-max C face F, let tau_in,tau_out be first times of the
incoming/outgoing F edges at a corner v. If R0 chooses F, then

    tau_out-tau_in=1.

Otherwise v is flat, R0 chooses the other maximum face, and R2 chooses F.
Put q=(T_2(v)-T_1(v))/4>=1. If L1 uses the F output, then

    tau_out-tau_in=1-4q;

if L1 uses the F input, it is 1+4q. Sum around the four boundary corners:
all edge times telescope, so

    sum_negative_corners q - sum_positive_corners q =1.

In particular every maximum C face has at least one negative flat contact.
Choosing its earliest first edge makes one such contact canonical and,
more importantly, furnishes the closed strict birth-time predecessor.
This identity keeps the actual L1/R2 wait; no blind R-to-R port matching
or deletion of equality cases occurs.

## 5. What this does and does not settle

The earlier first-arrival/first-departure cell graphs already required
essential high corridors. The new theorem additionally forces the max-C
FACE-contact graph to carry a coherently oriented first-L switch cycle,
with R0 on one max face and R2 on the other at every selected contact.
It addresses the source-L supplier that broke a second-R-only map.

It still does not rule out such an essential plateau, classify cap-four
fronts, bound repeated gates/nonstandard defects, or establish eventual
periodicity or standard104 capture. A useful next step would compare
this first-L face backbone to the existing opposite first-R physical
backbones while retaining all first/second port ordinals. The face cycle
cannot simply be counted as a third physical flow cycle.

Local rank evidence is in face_birth_local_controls.py/json. The analytic
topology and complete-front scope, not a finite scan, establish the
unbounded claim. Sources inherited unchanged are the signed global-H
maximum and cap-four first-R maximum theorems listed in the main note.
