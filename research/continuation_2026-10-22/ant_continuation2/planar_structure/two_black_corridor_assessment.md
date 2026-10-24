# What the unrestricted two-black theorem does and does not give

Status: primary-source assessment, 22 October 2026. The source files have been
read, but the Lean project has not been rebuilt in this workspace. This note
does not claim a new convergence theorem.

## 1. Sources inspected

Repository: <https://github.com/imfinn/langton-two-black>.

- `paper/TWO_BLACK_CELLS_REVISED.md`, revision 5, dated 5 October 2026;
  fetched Git blob `b1b550fbac0a970f343ccc61509168e832bee71d` and saved as
  `source_two_black_revised.md`.
- `lean/TwoBlack/Perp.lean`, blob
  `06a103fc11a5535dde5c0c70e354d4dce63ee78b`, saved as `source_Perp.lean`.
- `lean/TwoBlack/Par.lean`, blob
  `af79be99baf7e385413d97933ebfabbd1aeb231d`, saved as `source_Par.lean`.
- The level-one family table `lean/TwoBlack/Level1Data.lean`, blob
  `2f715b2fd6da5b1643b3442c632011df32845038`, was read through the connector.

The stated theorem is unrestricted in the positions of the at-most-two black
cells and in the initial pose. Its formal conclusion is eventual period-104
position, heading and read-color observations with a diagonal displacement.
Identification of the cyclic turn word with the standard blank highway is an
additional external comparison. The paper reports a native-computation trust
boundary; our inspection is not an independent build of that artifact.

## 2. The reusable mechanism

The basic corridor lemma is much stronger than a one-way flight argument. A
single parameter translates a far part of a board by one highway displacement.
At **every** transit of the separating corridor, including each return
transit, the longer member inserts one period of 104 steps. The proof keeps
two overlapping half-board relations. After an inward transit, the near
half is restored by identity while the far half still has its translated
relation. Keeping both halves is what makes repeated returns legitimate.

The one-corridor successor theorem preserves its own hypotheses, and the
two-corridor theorems transport a second corridor when the first is enlarged.
Perpendicular transport uses the fact that translation along the first drift
does not change the second diagonal coordinate. Parallel transport requires
the second band and its switch windows to lie on one fixed side of the first,
and requires foreign reads to move away from the second band's relevant end.

The Lean family proofs use a chosen parameter order. They first enlarge
parameter 1 while preserving the data for parameter 2, and then apply the
one-parameter family theorem along each resulting row. This is an exact
induction over all separations, rather than extrapolation from a simulation
range.

## 3. Does this automatically compose for arbitrary fixed corridor count?

**No such conclusion follows from the checked two-corridor theorems.** The
mathematical possibility of a larger theorem should be separated from what
the current artifact proves.

At a three-corridor base, suppose the constraints between corridors 1 and 2,
1 and 3, and 2 and 3 all hold. Enlarging corridor 1 transports the individual
corridor hypotheses for 2 and 3. To continue the induction by enlarging 2,
one must also show that the **interaction constraints between 2 and 3**
survive the first enlargement. This is a third-index preservation obligation.
Neither `perp_succ` nor `par_succ` supplies it: their conclusions preserve the
relation between the enlarged first corridor and the transported second one.

Some cases look favorable. A third translation perpendicular to a parallel
pair leaves their common diagonal coordinate unchanged. Fully ordered
parallel bands can also be expected to remain separated as intervening gaps
are widened. But temporal phase assignments, inserted reads, initial board
relations, and the foreign-material hypotheses must all be transported
consistently. I have not proved that the stronger pairwise hypotheses in
paper Section 3 imply all of these third-index obligations, and I have not
found a counterexample to that restricted statement. The justified status
is **unproved extension**, not either automatic composition or disproved
composition.

One can formulate a valid restricted next theorem as follows. For a finite
set of corridor indices, give a base certificate, the initial half-board
relations for each coordinate step, switch ordering maps, and finite
interaction data. Prove that a coordinate step preserves (i) every corridor's
own hypotheses, (ii) every interaction constraint, including those involving
two other indices, and (iii) the prescribed initial relations at the next
parameter values. Then ordinary induction on the sum of coordinate increases
transfers the base highway certificate to the whole parameter orthant. The
certificate time is the base time plus 104 times the total number of inserted
transits. The induction is straightforward **after** the preservation theorem;
the preservation theorem is the substantive missing premise.

## 4. Why even that theorem would not finish a three-cell or finite-seed proof

The existing addition-of-one-cell coverage theorem is for parents with at
most **one** parameter. It transports first reads and splits a single
corridor at a new obstacle. With two or more parameters, the paper explicitly
requires new arguments for positional-image injectivity and for cells whose
first read belongs to more than one corridor span. The present external
checker rejects such overlapping span ownership.

More seriously, Section 11 reports an exploratory three-cell family outside
the present corridor hypotheses: **one parameter lengthens two distinct
parallel tracks**. A transit from one debris site to another uses one track,
whereas a later return from a third site toward the origin uses a parallel
track. The relevant length is shared. This is not simply an extra independent
corridor with another freely variable length. The first normal form can fail
even before a proposed arbitrary-count induction is applicable.

That report is an obstruction to this proof architecture, not a demonstrated
non-highway orbit. The source says tested members form highways and makes no
all-parameter claim for those experiments. The present note has not reproduced
the reported three-cell experiments.

A useful extension must therefore allow a parameter to alter several tracks,
must encode their distinct phases and wakes, and must track interaction
changes as parameters vary. An affine track-length model on a finite graph of
debris sites is one possible language. It still needs a theorem explaining
which parameter regions share the same chronological interaction pattern.

## 5. Exact requirements for an induction over the number of initial cells

A finite-template induction for arbitrary finite seeds would need all of the
following.

1. **Sound transport for the enlarged family language.** Simultaneous changes
   of multiple track lengths must preserve the literal board relation at
   every transit, including returns and intersections with older wakes.
2. **Coverage of every new first read.** Adding an initially black cell at any
   position that the parent trajectory eventually reads must land in some
   represented child family. Images must remain first reads, or duplicate
   images must have a sound coverage rule. All low-parameter slabs and
   interaction-transition regions must be covered.
3. **Closure or a well-founded reduction.** Every child must either have a
   sound highway certificate or reduce to previously proved cases under a
   specified well-founded measure. Repeatedly raising a checker base is not
   a termination proof. Neither is observing highways in many members.
4. **A rule-specific bound on new interaction complexity.** It must be proved
   that the dynamics cannot keep creating longer tracks, new debris states,
   or an unbounded sequence of interaction types while the number of original
   black cells remains fixed. Finite initial support and unboundedness of the
   ant do not supply that conclusion.

The second and fourth requirements are not bookkeeping consequences of the
two-black theorem. In particular, finite initial support bounds the initial
input, while the ant may create unbounded writable support. This is the same
gap that prevents a finite scattering table from automatically becoming a
universal proof.

## 6. A narrower promising use

The theorem supplies exact all-distance one-black scattering channels: 21
ordinary one-transit channels and one exceptional two-transit shuttle among
the 22 blank-highway fresh-cell classes. A hypothetical infinite sequence of
four-black checkpoints has bounded heads, while all four cells escape every
bounded neighborhood (see `mass_four_escape.md`). Each such state therefore
begins with an arbitrarily long blank prefix. Its first distant collision is
one of those 22 channels. This is a genuine finite reduction at the **first**
collision. Later collisions occur in a modified board with old wake and
debris, so further application still requires a coupling or corridor theorem;
one cannot restart the one-black table without proving its hypotheses.

