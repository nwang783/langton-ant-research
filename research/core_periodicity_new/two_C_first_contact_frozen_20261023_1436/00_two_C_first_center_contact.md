# A first center self-contact cannot have a two-C entry gap

23 October 2026, 14:36 UTC. This is a literal core-to-residual age obstruction,
not just a geometric inventory. Independent reconstruction is requested. It
uses ordinary signed JO ages, not a higher counted threshold or path search.

## Statement and canonical contact conventions

Inside an actual complete recurrent-eight factor, split into its actual atomic
marked cuts. The first repeated point of the corrected center path cannot
have atomic ENTRY C-clock gap two between its outgoing earlier atom and
incoming later atom. This includes endpoint and nontransverse contacts.

Use the signed 1412 convention: at the earlier repeated parameter choose its
outgoing chord a, and at the later parameter choose its incoming chord b.
If s and t are their respective segment parameters, then 0 <= s < 1 and
0 < t <= 1. A contact that occurs at a later chord's start is represented
using the preceding incoming chord instead. No arbitrary endpoint choices
are substituted for those canonical choices.

The signed angle refinement says that at gap two, alpha(a) > alpha(b).
The later heading is S relative to earlier N. The only atom-type pairs are
D or C followed by V or U, and V followed by U. Their chords are not parallel,
so there is no missing collinear-overlap family at this gap.

## Complete exact geometric reduction

The contact equation places the later integer head in a parallelogram with
the four exact corners obtained by allowing s and t to be zero or one.
The checker derives its integer bounding box from these corners. There is
no guessed spatial radius or path-length bound.

After sector and canonical-parameter checks, exactly eight geometric cases
remain. In every one, s = 0: the return touches the earlier atomic center.
For earlier D or C there are three later poses:

- V at (0, 2, S), reaching the old center at the end of its V chord.
- U at (-1, 1, S), touching it halfway along the U chord.
- U at (-1, 3, S), reaching it at the end of the U chord.

For earlier V, only the latter two U poses remain. These are eight cases
because the first three each occur for D and C.

## The actual input cannot be an old entry identity

At an atomic marked cut, every cell of its five-cell core is excluded from
the ordered current residual identities. An entry residual label cannot
remain secretly attached to a core cell and later reappear as an initial-age
exemption. Becoming residual again requires a genuine output installation.

In each geometry choose the following true input of the later packet:

- For V(0, 2, S), selected input (1, 2) is the old core cell (-1, 0).
- For U(-1, 1, S), upper input (0, 2) is the old core cell (-1, -1).
- For U(-1, 3, S), upper input (-1, 4) is the old core cell (0, -1).

All three old cells are in the earlier atom's actual entry core. The required
produced input minima exceed two: selected V needs at least three, and the
chosen U upper slots need at least four already under ordinary JO. Attached
VCC or U-family tails do not weaken those minima.

There is one essential internal-cut check. A core cell at the earlier atomic
cut might conceivably become an output of the SAME full producer later in
its remaining C tail, whose full birth clock is earlier than the atomic cut.
The checker explicitly reconstructs all 15 actual atom/full-source roles
and verifies that the chosen old core cell is NOT in that full producer's
complete output mask. It cannot be supplied through that loophole.

Thus the identity consumed at the chosen later input must be born in a full
packet strictly after the earlier atom's containing full packet has exited.
That producer's entry C clock is at least the earlier atomic clock. At the
target, only two C increments have elapsed, so its produced age is at most
two, in fact at most two minus the remaining source C tails. This contradicts
the selected input's signed minimum. The same argument covers all 99 actual
source-role and target-tail combinations.

This is an ordered-identity statement, not an assertion about when a black
cell is physically read. A core cell may remain physically black while its
residual status changes, but that does not preserve a retired entry identity.

## Consequences and limits

Combined with the signed first-contact horizon, every first center contact
has entry gap at least three and at most six. A proper transverse first
crossing already has only gaps three or five from the separate static
crossing catalogue. The new result addresses the previously missing
two-C vertex-touch cases; it does not settle gap-four or gap-six degenerate
contacts, or the remaining gap-five D-first transverse branch.

No full-pose return, local fuel, V1, U1 or global capture closure follows.
There is no factor-first exception here because the chosen cell lies in an
actual core and the initial residual exemption has been explicitly removed.

Working checker: check_two_C_first_center_contact.py.
Finite table: chronology_dcuv/two_C_first_center_contact.json.

Dependencies are the signed atomic-cut geometry, first-contact angle theorem,
ordinary JO age rules and ordered residual/core separation. No KV overflow
clauses are needed for this result.
