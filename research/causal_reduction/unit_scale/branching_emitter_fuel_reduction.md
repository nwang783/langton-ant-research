# A single branching emitter cannot fund charge-preserving growing shuttles

23 October 2026, 15:00 UTC. Author analytic lemma, independent review requested. The conclusion is a finite-initial-support obstruction, unlike several neighboring arbitrary-board local exclusions.

## Exact model

Use a finite nonerasing typed substitution with exact spatial scale I: every label has a fixed finite physical base word, and its image has the same displacement and incoming/final headings as that base word. Let e_s be the base turn charge, number of R minus number of L. A distinguished root a is prolongable, so its iterates are nested genuine prefixes and grow without bound.

Assume:

1. No nonroot image contains a.
2. Every nonroot image preserves its own base charge e_s exactly. This permits arbitrary finite hidden states, image lengths and geometry in that nonroot subsystem.
3. The root image contains m>=2 occurrences of a. Write c for the sum of the base charges of all its nonroot letters, counting multiplicity.

Then legality of all root prefixes, even on an arbitrary infinite background, forces the root image to preserve charge too:

    m e_a + c = e_a.

In particular the whole presentation is charge preserving. If a reachable nonroot state s has minimum required initial black mass tending to infinity along its refined blocks, there is NO finite seed realizing the root path.

## Polynomial footprint eliminates the scalar exponential

Exact unit geometry and finitely many finite images give a constant C such that every depth-r read lies within distance C(r+1) of the root start. Indeed the location of a leaf is the sum of at most r fixed image-prefix displacement vectors and one base-word offset. This remains true for unequal image lengths, branching and macro bases. There are therefore O((r+1)^2) possible read cells.

On any legal finite read word, consecutive turns at each cell alternate. Its local signed turn excess is thus at most1 in magnitude. Consequently the total turn charge E_r of phi^r(a) satisfies

    |E_r| = O((r+1)^2).

All nonroot refined words have their original charges by induction, and cannot introduce a. Hence

    E_(r+1) = m E_r + c,
    E_0 = e_a,
    E_r = m^r (e_a + c/(m-1)) - c/(m-1).

Since m>=2, the polynomial bound forces the exponential coefficient to vanish. Thus c=(1-m)e_a and E_r=e_a for every r. No assumption about finite initial mass was used in this step, only actual read legality.

## Canonical entry fuel stays bounded

Choose one occurrence of the reachable state s in a fixed root power, with finite preceding typed word w. At the corresponding occurrence in deeper root prefixes, the preceding word is phi^r(w). Every label now preserves charge, including a, so its charge is the fixed number sum_(t in w)e_t, independent of r.

If the initial board has M black cells, the actual total black mass on entry to phi^r(s) is exactly M+charge(w). This is a uniform finite bound. But any entry board realizing that block must contain at least its minimum first-L count. If that minimum is unbounded, a contradiction follows.

This is the canonical-block fuel inequality with the missing root charge hypothesis now FORCED by scalar branching. It does not identify original black cells with later fuel or ignore colors outside the block.

## Application to the supplied axial primitive

Every decorated identity/17-read axial primitive state in axial_primitive_hierarchy_collapse.md preserves charge exactly: R images have charge1 and L images charge-1. Each unbounded chain surviving its local certificates is a supplied axial hairpin, possibly with a fixed outer prefix/suffix and a depth offset. A direct hairpin requires AT LEAST4r+2 initial black cells for r>=1: this is exact for R, while a reflected/complemented L hairpin requires6r+2. A fixed prefix of length L can change at most L cells, so surrounding it by fixed work still requires at least4r+2-L initial black cells.

Therefore no single branching root with m>=2 can fund any reachable unbounded component from that primitive on a finite seed, even though its multiple root occurrences can move component centers. The m=1 fixed-emitter case is instead excluded by the separate signed remote-column potential; the scalar recurrence here would permit linear root charge and is not applied to it.

This does not exclude several interacting charge-varying root types, nonroot images that emit the root, non-unit spatial refinement, arbitrary directives, or a different shuttle with bounded entry fuel. It does not by itself exclude a model in which every nonroot block stabilizes; such a model has no growing shuttle to which this fuel conclusion applies.
