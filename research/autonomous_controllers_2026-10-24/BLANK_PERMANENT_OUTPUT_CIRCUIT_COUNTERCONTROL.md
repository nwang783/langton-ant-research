# A permanent output-only circuit born from the blank board

24 October 2026. Author exact countercontrol; independent audit pending.
This is a finite transient followed by the standard highway, not an alternative
translating controller or a counterexample to WHITE unit essential winding.

## What survives without any BLACK inputs

Start the literal standard ant at(0,0), incoming N, with the entire board WHITE.
After read7688, at cut7689, its finite lifetime boundary graph contains a CLOSED
component with66 event vertices and66 edges. It has exactly six output roots:

    R7338 at(-1,13),   R7537 at(-1,12),   R7543 at(-2,13),
    R7549 at(-3,12),   R7686 at(-3,11),   R7687 at(-2,11).

Every one of these BLACK lifetimes is permanent. The component never rejoins
the head path. There were no initial BLACK roots anywhere, and every finite
BLACK lifetime in this circuit has its actual earlier R owner.

This falsifies two local proof shortcuts:

- No-input physical chronology does NOT force every permanent output edge to
  remain on the start-to-head boundary component.
- A graph made of permanent R-born BLACK w edges need NOT be a forest.

The full periodic WHITE target is stronger: the example is contractible and
transient. It does not realize winding3 or5 in a repeated WHITE front, does not
alter the standard tail, and does not exclude or realize any middle-short type.

## Exact finite graph, with all owners retained

For a finite trace through cutT, alpha pairs each R birth r with its actual next
L consumption l<T. Add its beta conjugate(r+1,l+1), without a period seam. At
every still-BLACK output root r, add the actual step(r,r+1). Because the initial
board is empty, there are no input roots. Vertices0 andT have degree1, all others
degree2: there is one start-to-head path and possibly closed circuits.

The selected component is the one containing event1695. It has30 alpha edges,
30 beta edges and6 output-step edges. Those60 finite-lifetime copies belong to
55 actual owned lifetimes: five have both copies in this circuit, fifty have
only one here. Their other copies have NOT been deleted or declared irrelevant.
The complete finite graph is built from the actual blank trace before selecting
this component. The same66-event component and all its edges occur both at
cut7689 and at the later standard capture cut9977.

The certificate retains every selected event, every actual R/L owner pair, and
every complete physical history at the six permanent output cells. It does not
replace a last R with a conveniently selected earlier birth or assume the cells
were read only once.

## Complete all-future permanence, not a long simulation

The deterministic blank trace at cut9977 has715 BLACK cells, head(-15,10),
incoming W. The full field is retained. The supplied standard104 word is
certified from that exact state using the retained finite-threshold infinite
periodic-word checker. The result is no mismatch at ANY future time, not merely
many observed repeats.

The one-period read footprint has x coordinates from-19 through-14 and full
drift(-2,-2). Hence every future read has x<=-14, while the six marked cells have
x>=-3. They are never read after capture. Direct literal replay confirms no read
of a marked cell between its listed final R and cut9977. This proves permanence
for all future time.

## Physical w cycle versus lifetime circuit

The six marked BLACK cells, viewed as w edges in the fixed C checker graph,
form a simple six-edge cycle with six distinct vertices. This is a SUBGRAPH,
not an isolated six-edge component.

At cut9977 their COMPLETE containing physical w component has501 BLACK edges,
446 vertices and cycle rank56. All501 edges and every vertex are retained in the
certificate. Exact full-drift ray tests show that the standard future reads none
of these501 cells, so that whole archive component is permanently frozen.
Thus the small six-root lifetime circuit must not be identified with its much
larger physical w component. Nothing is cropped to make the countercontrol work.

## Consequence for the live winding problem

A finite-prefix argument for WHITE S1 cannot simply say that, with no inputs,
closed output circuits never detach or that permanently emitted w graphs are
forests. Both operations actually happen from the blank board. A successful
periodic argument must use translation/homology or another genuinely global
condition in addition to the no-input lifetime ownership.

certify_blank_permanent_boundary_cycle.py
SHA256 3369386d32c17638d670931dbc202aef1d8b0fda32da67edcb000f80bf62d1fe
blank_permanent_boundary_cycle_certificate.json
SHA256 3bb74c05013b775e10feab181e779c241e49647d336120fcae49b1caac63c7f4

The certificate binds exact hashes of the retained tail checker and its State
implementation. Independent review is separate from this author's verification.
