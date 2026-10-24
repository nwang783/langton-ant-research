# Exact S/T first-port and last-port normal forms with an inherited R-born hook

24 October 2026. Symbolic arbitrary-exterior interface for the binary cap7
tail, not merely the23 minimum seeds. The full interior resource ledger is
a separate dependency owned by the kernel analysis. This note pins its input
and last-import boundary without assuming a particular exterior or periodicity.

Use S=RRRRLRLRL and T=RRRRLLLLRLRL. Both start and end at COMPLETE empty
active w components in the tail under consideration, with every fine-cut
active mass<=7. All actual old components and both cursors are retained.

## 1. Any RL exit leaves the same genuinely R-born hook

Normalize the actual postcut head/heading to(0,0),N. If its last two turns
were RL, the R read was at

    a=(-1,-1),

and the following L was at(0,-1). Therefore a is BLACK and its current
lifetime was born by that actual preceding R. There was no intervening read
of a. The current empty root is r=(1,-1) in doubled w coordinates, sector1.
The edge a touches its FOURTH star neighbor, not its first. This statement
does not depend on what word preceded the RL or on any inverse convention.

## 2. The next S or T pins ALL old imports at the first four R updates

At the new empty cut, four R edges are forced. They cost4 edges, so cap7
allows at most THREE old edges in the complete old components they touch.
The inherited hook a is one such old edge.

If the next actual word is S, its first-read L cells are(-1,1),(-2,2).
They are already black at entry and form a straight two-edge component in
the forced old subgraph, touching the FIRST star tip. Together with a the
forced old union has mass3. Thus every complete old component imported
during the four R updates is pinned EXACTLY:

    singleton {a};
    straight dimer {(-1,1),(-2,2)}.

Any extra edge at either component, any connection between them, or any
other component at another star tip would add an old edge and violate7.
The first edge's old far component is the dimer; the hook is a separate
fourth-port component. A type-only count cannot interchange those roles.

If the next actual word is T, its first-read L cells are(-1,0),a,(2,1).
The forced old union again has mass3 and pins the complete components:

    corner dimer {a,c}, where c=(-1,0);
    singleton {e}, where e=(2,1).

The corner joins the FIRST and FOURTH star tips; e touches the SECOND tip.
Again arbitrary extra black fields cannot enlarge or merge those components
or enter through another tip: the old-edge budget is already saturated.
These are actual COMPLETE components, not minimum-field sketches. This
argument is the signed general import-budget equality applied to an occupied
FIRST tip, rather than incorrectly treating it as the nonfirst-tip trap.

## 3. Successor choice determines the complete last-tooth component

Both S and T end RL, so their fresh last R cell becomes a in the successor's
normalized chart. If the successor is S, Section2 forces its COMPLETE
component to be the singleton{a}. If the successor is T, that component must
be EXACTLY {a,c}. No larger archive or hidden attached field is permitted.

This determines the last R import of the preceding block, not only its output
mask. Undo just the two SPECIFIED toggles to see the full geometry. At the
postcut r=(1,-1) is isolated. The last L cell l=(0,-1) is white and has
endpoints r and v=(-1,-3). The last R cell a is black, with endpoints v and
u=(-3,-1). The connector c has endpoints u and(-1,1).

* If the complete a-component is{a}, adding back l and removing a leaves
  precisely the old l edge active at v and an isolated u. Hence the last R
  imported NOTHING.
* If that component is{a,c}, adding l and removing a leaves precisely the
  old l edge active at v and the separate COMPLETE singleton{c} at u. Hence
  the last R imported EXACTLY that old singleton c.

Every external component remains disjoint because the postcut r is isolated
and the a-component was specified complete. This is a local two-toggle
component calculation, not an assumption of generic reversible routing or
a graph-role swap. The pre-last-R active component is pinned to the single
old last-L edge in both cases.

Thus, in the current block's entry chart, last-R imports are:

    successor S: empty, for either current S or T;
    current S, successor T: singleton{(-3,1)};
    current T, successor T: singleton{(1,2)}.

The latter connector cells are not read ANYWHERE in the current S or T.
Their old lifetimes were already black at that block's entry; no mid-run
preparation is supplied. They may of course have been R-born in earlier
actual history, so this is not an original-seed fuel claim.

## 4. Two older non-tail inputs per actual junction

The next S requires its two straight-dimer cells; the next T requires c and
e in addition to the incoming R-born hook. In the PRECEDING block's chart
these non-tail input cells are respectively:

    S then S: {(-4,1),(-5,0)};
    S then T: {(-3,1),(-4,4)};
    T then S: {(1,3),(0,4)};
    T then T: {(1,2),(4,3)}.

None is read by that preceding block. Since each is required black before
its first L in the successor, each current lifetime already existed before
the preceding block began. The successor ACTUALLY consumes both: S at
local6/8, T at local5/11. The inherited hook is separate and R-born during
the preceding block. These are precise older-input placement statements,
not a bound on how many such lifetimes previous blocks can regenerate.

## 5. Finite one-block fixtures and scope

The checker realizes four fixtures without any intervention. Start from
the corresponding required entry field in Section2; for successor T add the
specified last connector. To give the hook a literal finite R-born history,
move the start back to a,N, remove a from the initial field and add(0,-1).
The two actual updates RL then reach the desired empty entry with a born
at update0. Continue the one current block S or T.

The fully pre-funded initial masses are3,4,3,4 for SS,ST,TS,TT. All complete
active fine cuts remain<=7. The hook is genuinely R-born, last imports and
complete tail components match Section3, and both graph sectors/cursors are
recorded. These fixtures execute RL plus ONE current block; their successor
label specifies the necessary final tail type, not an uncharged claim that
the entire successor executes without its other input cells.

Artifacts are `check_st_last_port_normal_form.py` and
`st_last_port_normal_form_certificate.json`. Universal statements are proved
by three-edge saturation and complete two-toggle geometry, not inferred from
the four finite fixtures. Full interior pinning and the resulting global
component-count ledger remain separately auditable dependencies; no cap7
exit or universal attraction is claimed by this interface lemma alone.
