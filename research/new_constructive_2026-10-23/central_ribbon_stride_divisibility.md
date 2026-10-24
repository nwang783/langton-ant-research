# A color-period quotient forces78-divisible stride on any central output consumer

23 October2026. Author general lemma, exact finite graph certificate and one
application; independent review requested. No word-length/visit/width cap,
turn-word enumeration, cap search, or simulation horizon is used.

## Application: precise all-word statement

Take the COMPLETE3300-class mature actual15324 output, period(78,78), including
both untouched exterior helper bands, and add ANY finite XOR cap. Suppose an
actual ant has an eventual periodic turn word with full displacement(s,s),
s a nonzero integer. Assume its repeating read support contains at least one
cell in the fixed central ribbon

    8 <= t=x-y <=24.

Then78 DIVIDES s. The period length, repeated visits, head phase, translation,
finite transient, and finite cap are unrestricted. This is a necessary
condition, not existence at stride78 or a classification of those consumers.
A finite consumer episode or a nonperiodic future is not excluded.

This applies to an exact prepared periodic source profile, not to arbitrary
finite boards or arbitrary archives. It does not assert that the infinite
profile is a finite-seed orbit. For a long finite slab, a growing distributed
repair may alter the interface; no unqualified finite-slab theorem is asserted.

## 1. General color-period compatibility lemma

Let a source board have colors S(t,x mod N), with finite normal black support,
plus a finite cap. Suppose a prescribed actual tail repeats a finite word
with heading restored and nonzero full displacement(s,s). Set g=gcd(|s|,N).

For EVERY physical read orbit of the repeating word, all sufficiently far
forward copies have the same required first-read letter. Indeed the finite
set of within-period slot offsets has a fixed earliest chronological slot
on that physical orbit once the initial fringe has passed. Earlier repeats
supply the same alternating read history at every subsequent copy. Therefore
its initial source color must be constant along q+Z(s,s) beyond a finite
fringe. A finite cap can affect only finitely many such points.

The residues x+ks mod N run through exactly the residue class x mod g.
Periodicity of S therefore implies the necessary condition:

    for every read class(t,a mod g),
    S(t,a), S(t,a+g), ... are ALL the same bit.            (1)

The bit may be white OR black. No white-input/front assumption is made.
Classify as ALLOWED exactly the classes satisfying(1); classes with both
colors are forbidden to every such infinite repeating word.

## 2. A finite quotient detects necessary longitudinal winding

Quotient physical cells by(g,g). Write each as

    q=(a+kg, a+kg-t), 0<=a<g.

A vertex is(t,a), and an edge is any one of the four lattice moves between
allowed vertices. Label the edge by its change in k:

- E:(t,a)->(t+1,a+1 modg), weight1 if a=g−1, else0;
- W:(t,a)->(t−1,a−1 modg), weight−1 if a=0, else0;
- N:(t,a)->(t−1,a), weight0;
- S:(t,a)->(t+1,a), weight0.

One actual repeat projects to a CLOSED walk in this quotient, with total
edge weight s/g, which is NONZERO. All of its read vertices lie in the same
connected allowed component. Hence that component must contain a cycle of
nonzero longitudinal winding.

A component has NO such cycle precisely when integer potentials v satisfy
weight(u->w)=v(w)−v(u) on EVERY edge. In that case all closed walks telescope
to zero, regardless of their length or repeated vertices. This necessary
condition even ignores the ant's forced quarter-turns and alternating flips,
so its exclusions cannot depend on a guessed local visit cap.

## 3. Exact source reconstruction and graph certificate

The attached checker reconstructs the COMPLETE source directly. Lift all964
period26 black classes of prepared15324_return_normal_form.json to period78,
then XOR the odd read mask of the literal15324 word at(13,7,N). The result
has3300 black classes. None of the936 helper classes is omitted. Its normal
black support lies in[-64,92].

For each proper divisor g=1,2,3,6,13,26,39 of78, construct ALL allowed vertices
in -66<=t<=94. The two white collar levels on each side lie beyond every
source black. At every component meeting central ribbon[8,24], the checker
finds an integer edge potential and verifies it on EVERY directed lattice
edge. Every such component is strictly inside the truncation: none meets
-66 or94. Thus it is a complete CLOSED component of the INFINITE quotient,
not an artifact of trimming an exterior escape path. An actual path from it
to outside would require an allowed edge leaving its listed component, which
the complete adjacency check rules out.

The numbers of allowed central vertices/components are:

    g1:0/0; g2:0/0; g3:0/0; g6:1/1;
    g13:10/10; g26:110/64; g39:329/37.

For every listed component, all closed walks have zero winding by its exact
potential. For g1/2/3 there is not even an allowed central cell. Consequently
no repeating consumer meeting the central ribbon can have proper g. Necessarily
g=78, equivalently78|s. This proves the application.

As a nonvacuous positive relaxation control, g=78 permits every physical
class. Its graph is connected and has nonzero-winding cycles, including all
central vertices. This is NOT an ant construction: the graph deliberately
forgets turn and color-history chronology after first-color compatibility.
The two-row white exterior also carries an explicit unit-winding staircase,
checking the quotient/edge-weight convention independently of the output.

## 4. Constructive consequence and limitations

A new eraser cannot merely be another short-stride prepared rewriter such as
the known108-word drift2 operator: regardless of its local cap, any infinite
periodic drift2 readout of this source must avoid the central ribbon. More
generally the same holds at EVERY stride not divisible by78, even for an
unknown word, huge period or unbounded cell multiplicity. A consumer may
still run outside the ribbon or touch its ends in only a finite transient.

The earlier supplied-word matrices answered questions about three chosen
words. This is instead a color-period/topological obstruction covering ALL
parallel repeating words with incompatible stride, without asserting they
are standard or that they have any specified input mask. It therefore gives
a genuinely new necessary scale for full-core replenishment synthesis.

The remaining viable targets include a new78-multiple-stride consumer, a
nonperiodic old-rail eraser, changing field profiles between phases, or a
widening two-end topology. None is supplied by this theorem. Universal
finite-seed capture remains open.

Files central_ribbon_stride_divisibility.py/json contain the source
reconstruction, every mixed-color witness, all finite central-component
vertex potentials, and nonvacuous g78/exterior controls. The proof does not
use old supplied-word mismatch witnesses or extend a search horizon.
