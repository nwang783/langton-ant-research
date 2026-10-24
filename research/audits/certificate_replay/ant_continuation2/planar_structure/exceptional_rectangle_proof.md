# An exact all-parameter theorem for the forced exceptional rectangle

Date: 22 October 2026.

Status: computer-assisted theorem with an exact integer/rational verifier.
The full field, including all old marks, is retained. The verifier covers
every integer parameter in the stated range and every future highway period.
It is ordinary Python, not a Lean formalization. The parent reduction from
hypothetical four-black recurrence is recorded separately in the chronology
notes; this note states and proves the explicit family theorem and its
one- and two-cell prefix interfaces.

## 1. Statement

Use north = positive y, with headings N,E,S,W. White turns right, black
turns left; the cell is then flipped and the ant moves one unit. For an
integer n>=200, put

    q_n=(-33-2n,-14-2n),
    a_n=(-33-2n, 41+2n),
    c_n=(  8+2n,-14-2n),
    d_n=(  8+2n, 41+2n).

**Theorem.** Start at (0,0),N with exactly these four black cells. At time

    T(n)=728n+200304

the ant is at (-2n-58,2n+98),N, and from then on its read word is a fixed
cyclic phase of the standard 104-letter highway word. Each complete period
advances the head by (-2,2) and preserves the heading. The initial cell d_n
is never read, either before or after T(n).

The first reads of the other three initially black cells are exactly

| Initial cell | First-read time |
| --- | ---: |
| q_n | 104n+10881 |
| a_n | 312n+71330 |
| c_n | 520n+144036 |

The same eventual tail therefore holds if d_n is omitted from the initial
seed. The theorem supplies a sufficient certified tail-entry time; it makes
no earliest-entry claim.

## 2. Two useful prefix theorems

Let u=x-y and z=x+y.

**One-bit prefix.** With only q_n initially black, at time
`T1(n)=208n+70733` the ant is at the fixed pose (-15,26),E. It follows the
standard word from phase 99 forever, with drift (-2,2). Every read before
T1 satisfies

    -82 <= u <= 58,   z <= 39.

The complete black field at T1 has `-82<=u<=58`. In particular the generated
archive fits in a fixed diagonal strip even though its length grows with n.
The phase-72 fresh-cell ray of this NW tail is

    (-23,31)+k*(-2,2),  k>=0,

whose z-coordinate is 8.

**Two-bit prefix.** With exactly q_n,a_n initially black, at time
`T2(n)=416n+146040` the ant is at the fixed pose (40,-50),S. It follows the
standard word from phase 100 forever, with drift (2,-2). Every read before
T2 satisfies

    u <= 98,   z <= 71.

The complete black field at T2 satisfies u<=98. Its phase-72 fresh-cell ray is

    (48,-54)+k*(2,-2),  k>=0,

whose z-coordinate is -6.

These are all-parameter statements, not conclusions from sampled depths.
The verifier obtains them as prefixes of the same four-cell calculation,
proves that the other initial cells have not been read, removes those
unchanged input bits, and then verifies the entire future periodic word
against the remaining full affine field.

The chronology analysis independently checked the phase-correct canonical
fields. After five more one-bit updates there is a literal phase-0 13-cell
core at (-15,29),N; its XOR residual is in `-82<=u<=58`. After four more
two-bit updates there is a phase-0 13-cell core at (40,-52),S; its XOR residual
has u<=97. No assumption that the core is a subset of the full field is
needed: the comparison uses symmetric difference.

## 3. The finite witness word

Write W for the standard 104-letter word starting at phase 0, and W_r for its
cyclic phase r. The candidate trace is a concatenation of fixed finite words
and variable numbers of copies of W_r. The fixed words are stored literally
in `exceptional_rectangle_template.json`.

| Stage | Type | Length or period count | Phase for period stages |
| --- | --- | ---: | ---: |
| 0 | fixed word | 9977 updates | — |
| 1 | highway periods | n+8 | 0 |
| 2 | fixed word | 51118 updates | — |
| 3 | highway periods | n+7 | 0 |
| 4 | fixed word | 8078 updates | — |
| 5 | highway periods | n+5 | 99 |
| 6 | fixed word | 51123 updates | — |
| 7 | highway periods | n+7 | 0 |
| 8 | fixed word | 22936 updates | — |
| 9 | highway periods | n-20 | 100 |
| 10 | fixed word | 51122 updates | — |
| 11 | highway periods | 2n+15 | 0 |
| 12 | fixed word | 2310 updates | — |
| 13 | highway periods | 13 | 100 |

The finite word generator compares literal runs at n=200 and n=201 only to
produce this candidate. Agreement at two depths is **not** the proof. The
subsequent verifier accepts the candidate only after checking all prescribed
colors symbolically for every n>=200. It explicitly asserts that every
period-stage word has length 104 and is a cyclic rotation of W.

The template's SHA-256 is

    16246ec40cbdd4ad94c35698992582b27a942dc7d539683f1b3684892cd5687d

## 4. Exact affine representation of the complete field

An affine scalar is an integer pair `(a,b)` denoting an+b. An affine point
is a pair of affine scalars. At every macro boundary the complete field is
represented as the XOR of:

- finitely many affine points;
- finitely many finite diagonal rays
  `{base(n)+k*d : 0<=k<N(n)}`, where d has coordinates +/-2 and N is affine.

This representation starts from all four initial bits. Each verified finite
word adds its odd-read cells, and each verified repeated period adds one
finite ray for each odd-read cell of the period. There is no removal of the
blank transient, no deletion of old tracks, and no replacement of a remote
region by a white background.

For a fixed finite word, repeated visits to a cell determine the required
color at the beginning of that word. The checker verifies internal
consistency and then checks each required color against the entire affine
field. It verifies every possible isolated coincidence of affine points and
every point/ray incidence for all integers n>=200.

For a period repeated N(n) times, a required local cell is read on a ray
`q(n)+k*d`. Its intersection with a previous field ray is empty, a singleton
epoch, or an interval of epochs with affine endpoints. Earlier copies of
the current period contribute a half-interval beginning at a positive
integer offset. All these contributions are clipped to `0<=k<N(n)`.

An interval [a(n),b(n)] has parity boundaries at a(n) and b(n)+1. XORing all
interval boundaries, including the interval on which the required initial
color is black, must give the empty set. This exact identity proves the
required color at every epoch k simultaneously. All order comparisons and
integrality conditions are checked uniformly for n>=200. A comparison that
would change above the cutoff, or would need an unhandled residue class,
causes rejection rather than being evaluated at a representative depth.

The algebra is the same previously documented affine-field method used in
`../../ant_continuation/wake_clock/certify_four_scatterer_prefix.py`, with a
new witness word, initial seed, prefix interfaces and infinite-tail test.
The present result is not inferred from that earlier 16-cell example.

## 5. Why the final tail is proved for infinitely many periods

The final test is not a finite stability test. Starting from the entire
symbolic field at T(n), the verifier checks the periodic read constraints for
every epoch k>=0. Initial point and finite-ray terms contribute finite epoch
intervals. Net writes of earlier tail periods contribute half-lines. A black
requirement contributes the half-line [0,infinity).

Finite intervals contribute two parity boundaries; half-lines contribute
one. The checker proves that the XOR of all boundaries is empty for each
distinct required cell of the period. Thus every future read has its
prescribed color, for all k>=0 and all n>=200. The same infinite test is
performed independently at the one-bit and two-bit prefix interfaces after
removing the proved-unread extra input bits.

The final tail uses phase 100 of W, contains 44 distinct required cells and
36 odd-read cells, has displacement (-2,2), and preserves heading N. The
verifier also proves that d_n belongs to no finite read point, no finite read
ray, and no future read ray of this tail. This establishes the never-read
claim against the complete infinite future.

## 6. Verification output and reproduction

The completed exact run checked:

- 21,030 distinct finite-word initial-color requirements;
- 424 periodic read constraints, including the two parent tails and final
  infinite tail;
- 22,010 affine inequality/range guards;
- exact first-input-contact times and the never-read fourth corner.

`exceptional_rectangle_affine_certificate.json` records the successful
result, all stage poses and times, bounds and contact times.
`exceptional_affine_fields.json.gz` contains complete symbolic field
snapshots at the one-bit prefix, two-bit prefix and final tail boundary.
These snapshots support independent literal evaluation at selected depths;
the symbolic checker, rather than those selected evaluations, supplies the
all-parameter proof.

From the workspace root, run

    python ant_continuation2/planar_structure/extract_exceptional_template.py
    python ant_continuation2/planar_structure/certify_exceptional_rectangle.py

The second command takes about 80 seconds on the present workspace. It uses
the previously saved exact engine and `ant_exact.py`; the research bundle
must retain those dependencies. Independent canonical-core and all-future
XOR audits are recorded in
`../chronology/audit_exceptional_stage_cores.py` and
`../chronology/exceptional_stage_core_audit.json`.

## 7. Scope

The theorem proves a specified infinite family of three- and four-black
starts. Its relevance to arbitrary finite input comes from a separate
reduction: a hypothetical infinite sequence of four-black checkpoints has
bounded heads, escaping cells and diverging clocks, which can force three
successive exceptional collision channels and then this rectangle. Every
ordinary-channel exclusion must retain the entire old archive. The strip
and half-plane interfaces above are provided exactly for those exclusions.

Neither the rectangle theorem alone nor a conclusion that mass four occurs
only finitely often would settle the full finite-seed highway conjecture.

