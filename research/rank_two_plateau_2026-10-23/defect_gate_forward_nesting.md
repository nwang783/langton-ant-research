# Three-fold output law and adjacent defect-gate nesting

23 October 2026, 12:47 UTC. Analytic addendum to
second_R_gate_or_corridor.md. Independent review requested. This adds a
specific forward/second-wave coupling, not a global resource budget.
All statements concern complete WHITE histories of cap four. They hold
for actual physical cells and hence for full-drift quotients without
folding the drift. No front search or prepared-profile solver is used.

## 1. The defect type with an opposite first L

Call a two-R same-face cell an E defect if its first three incoming
headings are (h,-h,h), with turns R,L,R. Its R0,L1,R2 departures ALL use
one output port g=R(h). Let w be that physical output neighbor. The first
three uses of this port, in that order, are exactly source ranks0,1,2.
If L3 also uses this port, the flow is four; otherwise it is three.

The target w has at least THREE arrivals with incoming heading g.
Because its complete history has at most four reads, its possibilities
are exactly the following six lists (a bar means the opposite heading):

- g,g,g; g,g,g,g; g,g,g,bar(g): S / locked defect,
- g,bar(g),g,g: another E defect,
- bar(g),g,g,g or g,g,bar(g),g: flat two-R contact.

Every source R2 departure therefore reaches either target R2 or target
L3, never R0/L1. In the locked case it reaches R2. In the E or flat
case it reaches L3. Source L3, if it is the fourth same-port departure,
forces the all-g locked target case.

If source v's two R turns use a maximal C face F, w is incident to F.
In a flat target, its two C faces have equal height, so the other face
is maximal too. Thus the flat alternatives are genuine transitions
inside the SAME corner-connected max-C plateau, not lost suppliers.

## 2. The E-to-E alternative is a strictly nested synchronized gate

Write T_i(v) for the actual complete read times, i=0,1,2. If w is E,
its three g arrivals occur at its ranks0,2,3. Exact chronological port
matching therefore gives

    T_0(w)=T_0(v)+1,
    T_2(w)=T_1(v)+1,
    T_3(w)=T_2(v)+1.

Its R2 is supplied by v's L1 and paired with v's R0: it is exactly the
same-face gate classified in the main note. Put

    B(v)=T_2(v)-T_0(v),   A(v)=T_1(v)-T_0(v).

Then

    B(w)=A(v) <= B(v)-4.

This is strict actual chronology, not a comparison of quotient phases.
It proves that E-to-E propagation cannot close any quotient cycle with
translation-invariant B values. More concretely, both E turns use F,
so an uninterrupted E chain follows the clockwise four corners of that
same physical unit face; four E corners cannot close consistently.
The latter impossibility is already implied by the older first-R
contractible-cycle theorem, but the synchronized span decrease is an
additional rank-two time correlation.

The sharp same-face gate bound from the main note gives B(w)>=16.
Consequently ANY E-to-E adjacency forces

    A(v)>=16,   B(v)>=20.

For a chain v0,...,vr of E vertices with r>=1 such adjacencies, induction
on the exact identity gives

    B(v0)>=16+4r.

Thus three consecutive E corners force the first one's R0-to-R2 span
at least24. This uses the same nested span repeatedly in an exact
inequality; it does NOT add the nested spans as independent payments.
At most three E corners can be consecutive around the same face, since
all four would close the prohibited E-to-E loop.

## 3. What the other alternatives mean

- Locked target: source R2 directly supplies target R2, so the second-R
  predecessor retains rank2 with zero paired-source wait on this edge.
  A locked defect has input ordinal3 at its R2 and cannot be an R0 gate.
- Either flat target: source R2 supplies target L3. Its preceding R2 is
  strictly earlier than that L3 by a physical return gap. One flat case
  has target R2 supplied by source L1, hence an explicit flat R0 gate;
  the other receives its R2 on the OTHER incoming port. The latter R2
  supplier is not identified or deleted by this law.

In the same-face incoming gate, the earlier source R0->target R0 event
is simultaneously a first-arrival edge at the target and a first-
departure edge at the source. It is a genuine shared edge of the TWO
full functional graphs, although the signed positive/negative BACKBONE
cycles cannot share it. At least one graph therefore treats it as a
noncycle attachment. This does not bound the number of attachments.

The law identifies exactly where the rank-two wave passes to a flat
plateau contact, is retained at a locked defect, or coalesces through a
strictly nested first-R gate. None of the alternatives has been globally
excluded. No finite-fuel or nonstandard-only defect budget follows.
