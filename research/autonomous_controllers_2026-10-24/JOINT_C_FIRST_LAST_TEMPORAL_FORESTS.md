# Joint first/last C forests: exact temporal layers and a literal obstruction

24 October 2026. Author proof and complete literal controls; independent audit
pending. This gives a sound joint graph and rejects a natural false cycle
shortcut. It does not force a canonical module or classify controllers.

## 1. Two clocks are necessary

Use the signed all-cap active-C scaffold1ae8a8e5/audit317e4dce. For every active
physical C face v, write A(v) and B(v) for its first and last active read times.
Under the FULL supplied period P and drift d,

    A(v+d)=A(v)+P,  B(v+d)=B(v)+P,  S(v)=B(v)-A(v)>=0.

The same face generally has two different event clocks. A first-parent edge
and a last-successor edge cannot be concatenated chronologically merely because
their projections meet at v. Such a concatenation must pay the exact A/B
switch, with the correct physical translate.

## 2. Exact directed two-layer graph

There are nodes A_v and B_v for each full-drift face class. Every edge has a
full integer voltage nu and gap g, with

    T(target)+nu P-T(source)=g.

The edge represents the actual contiguous time interval between those two
specified occurrences in an existing complete trajectory. Its interior is not
assumed to be a new independent channel or module.

- FIRST: reverse a selected parent arrow. If the first-entry data gives
  child v -> parent u with voltage eta and positive clock gap g, use
  A_u -> A_v with voltage -eta and the same g. WHITE edges retain the actual
  selected R0 owner, its first L and their full period offsets. BLACK-first
  entries remain explicitly marked prepared roots, not deleted.

- LAST: use the selected last-exit arrow B_u -> B_v, with its actual voltage
  and positive gap. If the selected physical cell ends R, keep its actual
  final R and opposite-heading relation to that last L.

- SPAN: A_v -> B_v, voltage0 and gap S(v).

- LITERAL HANDOFF: if a particular last L of u is immediately followed by the
  FIRST active read of v, use B_u -> A_v with that physical step's voltage
  and gap1. No such edge is inferred from adjacency or basin connectivity.

- CANONICAL FORWARD CARRY: put

      k(v)=ceil(S(v)/P),
      B_v -> A_v with voltage k(v) and gap k(v)P-S(v).

  This target is the FIRST read of the DIFFERENT physical face v+k(v)d,
  unless k=0. It is not a return to the retired face v or a free time switch.
  If S=0, A_v and B_v are the very same event and may be identified. If S>0,
  S cannot be a multiple of P: a fixed event phase has only one occurrence at
  a fixed physical C face under nonzero d. Thus the carry gap is then positive.

All these edges are exact in an actual controller; carrying forward may pass
through arbitrary other faces and many reads. No bound on S/P has been
proved here. Powers of a period split classes and change the numerical carry,
so carries are not treated as representation-invariant input costs.

## 3. Sound necessary cycle condition

Along any directed closed walk of the TWO-LAYER graph, telescope its clocks:

    w P = sum g,

where w is its FULL voltage. Once zero-span event identifications are
contracted, every nonempty directed cycle has at least one positive gap, so
w>=1. Equivalently, a proposed exact interface with a positive-gap closed walk
of voltage<=0 cannot be completed to an actual front. This is a checkable
clock-cycle obstruction, not an opaque solver status.

Conversely, satisfying these necessary clock conditions is not a physical
completion certificate. The explicit first/last arcs can share events when
viewed in different graph walks, and graph-node simplicity is not spatial
embedding. A closed walk of voltage w follows w actual periods, not necessarily
one. One must not import the embedded C-first-cycle unit-winding theorem to
this two-layer graph.

For example standard104 has S((0,-3))=254 and k=3. Its simple two-node graph
cycle A_(0,-3) -> B_(0,-3) -> A_(0,-3) has gaps254 and58, and winding3.
It is an actual312-update continuation of the known WHITE controller. This
is not a lifetime-boundary circuit and does not contradict any WHITE S1 target.

## 4. Exact debt identity for a collapsed mixed walk

Suppose one only projects FIRST and LAST edges onto face vertices and takes
a closed mixed walk. Let w be its voltage, and retain the positive edge gaps.
At each face where the incoming/outgoing edge types switch, the exact identity
is

    wP = sum(edge gaps)
         + sum(S at FIRST->LAST switches)
         - sum(S at LAST->FIRST switches).

Repeated occurrences are counted separately with their correct full lifts.
Thus a nonpositive winding of this projected walk is NOT a contradiction:
it can be paid by a LAST->FIRST switch backward through a face's history.
Replacing each such switch by the canonical forward carry instead produces
an actual two-layer closed walk with the added voltage and its positive gap.
One must retain the spans or independently prove bounds on them; neither a
spatial common path nor an uncharged one-period reset is enough.

## 5. Literal WHITE standard countercontrol

In standard104 with full d=(-2,2), choose

    u=(0,-7): A=-346, B=-219, S=127,
    v=(1,-8): A=-341, B=-324, S=17.

The FIRST edge u->v has voltage0 and gap5. The LAST edge v->u has voltage-1
and gap1. Their collapsed mixed loop therefore has winding-1 despite both
positive gaps. The exact accounting is

    -104 = 5+1+17-127.

The LAST->FIRST switch at u is the missing backward-time operation. Its
canonical physical carry is2, not1. Restoring it yields the actual contiguous
arcs

    A(u) -346 -> A(v) -341       : 5 updates,
    A(v) -341 -> B(v) -324       :17 updates,
    B(v) -324 -> B(u-d) -323     : 1 update,
    B(u-d) -323 -> A(u+d) -242   :81 updates.

The repaired voltage is1 and the duration is104. This is a literal standard
period, not a contradiction, an artificial reconnection, or an assumed path.

A fresh empty-board replay realizes this exact partition, up to a checked
proper rotation/translation, at absolute blank time10359. The five complete
fields at cuts0,5,22,23,104 contain761,764,765,764,773 BLACK cells. Every unread
archive bit is retained. The exact all-future checker certifies the complete
finite field at the starting cut, not just its104-step repeat.

## 6. Prepared10 and prepared80 pass the same honest graph

Prepared10 has a collapsed zero-voltage two-edge loop with edge gaps5/1 and
switch spans11/17:

    0 = 5+1+11-17.

The carry at the ending face is2. Its repaired actual arcs have lengths
5,11,1,3 and cover TWO full10-step periods, with voltage2. The complete finite
three-cell paid seed and every intermediate field are replayed. Infinite
repetition still needs the retained infinite input ray.

Prepared80 has the same collapsed gap/span pattern, but period80 and carry1.
Its actual repaired arcs have lengths5,11,1,63 and cover one80-step period.
The four-cell paid seed ends with16 BLACK cells, and all fields are retained.
Its two genuine input classes and both infinite input rays remain explicit.

The base graph counts are: standard10 faces, maximum span254/carry3, one
literal last-to-first handoff; prepared10 two faces, maximum span17/carry2,
no literal handoff; prepared80 fourteen faces, maximum span65/carry1, two
literal handoffs and one zero-span face. The checker also rebuilds sixty
rotation/power/phase representations, without replacing the full drift by a
primitive vector. These counts are controls, not a classification argument.

## 7. What the joint approach still needs

The joint forests give genuine chronological cycles only after all temporal
switches are represented. A new impossibility theorem needs actual bounds or
additional rank/port obligations on those switches; their spatial projection
alone is insufficient even on the standard WHITE positive control. A proof
that a canonical module occurs would also need the full intervening literal
word/field obligations, not merely the endpoint clocks and voltage.

No visit/width/period cap, finite span bound, input exclusion, WHITE lifetime
unit-winding claim, new controller, or universal entry theorem follows.

## Frozen artifacts

certify_joint_C_temporal_forests.py
joint_C_temporal_forests_certificate.json

The certificate includes every graph edge, actual selected R/L ownership,
three full finite-field replays, all positive-control arcs and dependency hashes.
