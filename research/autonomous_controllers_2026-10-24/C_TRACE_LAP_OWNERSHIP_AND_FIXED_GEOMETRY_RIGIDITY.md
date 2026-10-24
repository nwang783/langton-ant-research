# Literal C-trace ownership: an all-length fixed-geometry reduction

24 October 2026. Author proof and exact certificates; independent audit pending.
This is a classification of FIVE specified spatial C traces, not arbitrary
controllers, not first/last-union connectivity, and not a global entry theorem.

## 1. Spatial trace, not a prescribed temporal period

Use the signed active-C definition: R stays on the same C face; L crosses to
the diagonally adjacent C face. Fix a bi-infinite sequence of these L crossings,
including its physical embedding and one incoming head pose, with

    C[i+N] = C[i] + d,   d != 0.

N counts C transitions, NOT ant updates. At each occurrence of each C visit,
allow a separately chosen number of intervening R reads. In particular, do
NOT identify the choices in different spatial periods. A possible realization
can have a longer temporal period or have no temporal period at all.

The five fixed geometries below are extracted from the exact supplied standard
104, prepared10, prepared80, prepared1564 and prepared4352 words. Their complete
unread fields are not discarded or replaced by their read footprints.

## 2. The only freedom is a local four-R lap

Immediately after an L crossing the cursor is fixed by that crossing. Given
the next specified C edge, there is a unique minimal number k in {0,1,2,3} of
R steps before crossing it. Four R steps return to the same head pose.
Five consecutive R steps are impossible: the fifth would read the first
cell again, which the first R made BLACK and no intervening read changed.

The k=3 case is also impossible in any actual trajectory. It would cross
straight back over the preceding L edge, still WHITE: the three intervening
R reads are at the other three corners. Adding four more R steps is already
impossible. Thus an actual C trace is nonbacktracking.

For k=1 or 2 there is no alternative. For k=0 the only possibilities are
L and RRRRL. Introduce a binary variable X_i(n) for this lap at spatial visit
i+nN. All four R reads of a chosen lap must be legal; the next section imposes
that condition exactly rather than treating a lap as a freely insertable loop.
No imposed visit, width, time or period cap appears here.

## 3. Full physical chronology without a temporal period

For a representative cell q, a candidate read at physical q+k*d in C block i
occurs at the representative q in block i-k*N. Its lap variable is X_i(-k).
For q+ell*d the variable is X_i(ell-k). These INTEGER offsets are retained.

Order candidate reads by (i-k*N, slot). Put the mandatory L at slot4, forced
R reads at their earlier slots, and the four optional lap R reads at slots0..3.
This order is independent of which laps are present: all C blocks occur in
strict chronological sequence and a lap only adds reads within its own block.
It is therefore valid even with nonperiodic lap choices. It does not use
(i-k*P) with a falsely fixed ant period.

The maximal candidate read set is finite modulo the FULL supplied drift d.
Different corners can lie in the same drift class, and the same phase variable
can occur more than once in a constraint with DIFFERENT offsets. Such copies
are distinct Boolean variables, not a repeated scalar or a primitive-drift
identification.

## 4. Exact ownership constraints

At each physical cell, call the always-present reads mandatory. All other
candidate reads are optional R reads, belonging to lap variables. Thus between
two consecutive mandatory reads there are only optional R candidates.

- Mandatory R then R is impossible: no optional R can supply the missing L.
- Mandatory R then L, or L then R, requires ZERO selected optional R reads.
- Mandatory L then L requires EXACTLY ONE selected optional R read. This is
  its actual preceding R owner, not a net color or an assumed supply.
- Before a first mandatory R there must be ZERO selected optional reads.
- Before a first mandatory L, complete WHITE requires EXACTLY ONE optional R;
  allowing a genuine initially BLACK input instead gives AT MOST ONE.
- After a last mandatory R there must be ZERO optional R reads.
- After a last mandatory L there may be AT MOST ONE optional R, its possible
  permanent output.
- If the class has no mandatory read, it may contain AT MOST ONE optional R.

These constraints are necessary AND sufficient for color compatibility of the
entire specified trace. They enforce literal alternation and the first color
at every physical cell. The geometry already supplies every head pose, turn,
step and C crossing. Hence satisfying all the constraints constructs the
actual trajectory on the board determined by its first colors. This is not a
claim that the required prepared board has finite support.

In a periodic assignment, the retained exact stable-class checker independently
checks the reconstructed word, with full drift and complete class histories.
No output classes or possible never-read optional classes are assumed fixed.

## 5. Transparent forcing, retaining independent copies

Each raw constraint is a finite sum of Boolean occurrences, equal to zero or
one, or at most one. The certificate uses only two elementary rules:

1. If the already known terms reach the permitted total, every other term is0.
2. If an equality can reach its total only by making every remaining term1,
   those terms are1. Since the total is at most1, a nonempty such inference
   uses exactly one remaining occurrence.

An empty required-one constraint or an exceeded/insufficient total contradicts
compatibility. No SAT/UNSAT result or opaque exhaustion is used.

A phase is marked uniformly forced only because the corresponding constraint
holds at EVERY spatial translate. Each copy X_i(n) remains distinct. The rules
then force the whole phase orbit, by translating the same physical inference.
They never infer X_i(n)=X_i(n+1) merely from notation. In particular, duplicated
phase names in a constraint are counted as separate occurrences, with their
full offsets, until their values have already been uniformly forced.

The checker additionally records finite-boundary thresholds. If raw constraints
hold for anchors ell>=B and X_j(n) is known for n>=B+r_j, a constraint using
X_j(ell+s) is ready by ell>=B+max(0,r_j-s). A newly forced occurrence X_i(ell+t)
therefore has threshold B+max(0,r_j-s)+t. Each proof contains finitely many such
steps. This establishes eventual forcing without identifying early copies.

## 6. Why a finite entry field suffices for eventual forcing

Now assume only a forward infinite actual tail with this C trace, starting on
an arbitrary FINITE whole BLACK field. Every physical cell has finitely many
candidate reads, since d!=0 and there are finitely many templates per C period.
For sufficiently large ell, all candidate reads of q+ell*d occur after entry,
and q+ell*d is outside the finite entry BLACK field. Its first actual read is
therefore WHITE. This holds simultaneously for the finitely many candidate
classes after increasing one threshold B.

Consequently all WHITE raw constraints hold eventually, with no restriction
on the initial lap pattern and with EVERY unread entry bit retained. The finite
forcing proof applies with the thresholds from Section5. This is not a claim
that BLACK first reads in a general finite factor are impossible, nor that a
fixed cropped stock is monotone. It is the exact spatial finiteness of this
specified forward trace and the complete entry field.

## 7. Concrete fixed-geometry conclusions

For standard104's spatial C trace there are46 C transitions,32 lap phases and
86 local ownership constraints. The uniform proof forces all32 phases; the
resulting ten four-R laps reproduce standard104 exactly. Thus:

    Every infinite actual finite-field tail with this precise spatial C trace
    is eventually the standard104 word, even if its lap choices were not
    assumed periodic.

In a one-spatial-period representation the kinematic family has2^32 choices
and derived ant lengths64 through192. These numbers describe the family; the
all-length proof above does NOT cap a tail's temporal period at192.

For the other supplied geometries the WHITE constraints contradict:

    prepared10:    5 C transitions,    4 lap phases,   11 constraints;
    prepared80:   34 C transitions,   25 lap phases,   78 constraints;
    prepared1564:730 C transitions,  480 lap phases, 1745 constraints;
    prepared4352:2084 C transitions,1361 lap phases, 4332 constraints.

The exact short forcing certificates are stored, with each physical cell,
source occurrence and voltage. Therefore none of these FOUR exact C traces
can persist forever from a finite entry field, even with nonperiodic lap choices.
Their known prepared trajectories remain legitimate: they satisfy the prepared
constraints and keep their explicit infinite inputs. This is more than rejecting
the one supplied turn word, but says nothing about changed C routes or connectors.

## 8. Relation to the joint first/last forest question

The frozen disconnected abstract C ladder also fails this encoding. It contains
mandatory R/R pairs at a single physical cell with no mandatory L between.
No choice or nonperiodic sequence of four-R laps can repair such a pair. The
certificate retains the full physical offsets rather than a projected crossing.

This explains a concrete ownership defect missed by the two forests. It does
not prove that every disconnected forest union has such a defect. Their general
connectivity and the WHITE lifetime unit-winding target remain OPEN.

## 9. Controls and frozen artifacts

certify_C_trace_lap_ownership.py
C_trace_lap_ownership_certificate.json

The checker reconstructs every candidate read and constraint for all five
geometries, checks their actual supplied lap assignments against complete stable
histories, and repeats100 rotation/phase/full-period-power controls. It freshly
replays the complete P/Q bulk normal forms with their finite XOR caps, including
all unread passive strands. It also independently rebuilds the complete finite
blank field at10392 and checks the standard phase103 future by the retained
exact all-future checker. Prepared10/80 full-field certificates remain bound
by their exact dependency hashes. No infinite input is silently removed.
