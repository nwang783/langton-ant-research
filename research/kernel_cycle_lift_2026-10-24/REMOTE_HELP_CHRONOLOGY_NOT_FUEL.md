# Remote-helper ancestry: exact chronology, not a termination rank

24 October 2026. Companion to `FINITE_SOURCE_OLD_REMOTE_HELP.md` SHA256
a858ddf0a392e5242dbee99e5882db3a0e7a1ea6f65095faf85807953c19711b.
The finite-source theorem is an existence bound only. This note specifies
the actual dependency relation it supplies and its remaining limitation.

## 1. A helper is dormant earlier and consumed earlier

Keep a completed marked episode (e,d,c) as in that theorem, under supplied
fine-cut cap M. Suppose c-d>F(M). Choose any old remote consumption provided
by the theorem: a lifetime f, already black at cut d, is consumed by L at
update j in [d,c], at a cell y outside p_d+[-4M,4M]^2.

The following facts hold on the actual COMPLETE field:

1. f is dormant at cuts d-1 and d. An active edge at cut d is within M of
   p_d. At cut d-1 it is within M of p_(d-1), and the two heads differ by
   one move, so it is within M+1<=2M of p_d. The remote cell y is outside
   even the4M box. Thus f cannot be in either active component.
2. Its consuming update satisfies d<=j<c STRICTLY. The marked cell x is
   within M+1 of p_d, whereas y is remote; the unique read at update c is
   x, so j cannot equal c. No lifetime is consumed twice.
3. If f has previously been active, let s be its LAST active-to-dormant
   transition cut not later than d. This exists and satisfies s<d, because
   f was already dormant at d-1. Such a transition is an actual bridge-L
   departure leaving the surviving f on the departed side. Then (f,s,j)
   is itself a legitimate completed marked episode, allowing arbitrary
   later unproductive reattachments and departures.
4. Otherwise f is an initially black, initially dormant lifetime which
   has remained dormant from the trajectory's initial cut through d.
   This is an INITIAL ROOT; no artificial earlier departure is assigned.
   In particular an R-born helper cannot be such a root: its birth R
   inserted it into the then-active w component.

There is no requirement that the helper's final departure before j be
earlier than d. The chosen s is the last departure AT OR BEFORE d, which
is what makes s<d valid despite later unproductive reattachments.

## 2. Precisely what is well-founded

An ancestry arrow (e,d,c)->(f,s,j) therefore strictly decreases BOTH integer
departure cuts and integer consuming-update indices: s<d and j<c.
Initial dormant helpers are terminal roots. Since trajectory time starts
at0, no infinite backward ancestry chain is possible. One can choose the
first remote old consumption to make the helper selection deterministic,
but no such choice is needed for the strict inequalities.

The ordering concerns absolute times, not physical distance, birth age,
the duration j-s, the last dormant run, component mass, component type,
or the amount of fresh output. None of those is proved to decrease.
The old helper can be consumed very early in a long marked excursion;
its own departure and reimport can be close together. Hence a long parent
episode supplies no lower bound on its helper's own wait or age.

The cap M is only known on [d-1,c]. If s<d-1, applying the finite-source
theorem recursively to (f,s,j) requires a separate cap bound on [s-1,j].
A sustained tail cap supplies this only when s-1 is in that tail. Earlier
lifetimes/episodes must instead be treated as a finite prefix boundary.
Even with sustained cap, a helper episode shorter than its own F(M)
need not have a helper at all.

## 3. Why this does not prove finite fuel or attraction

Well-founded backward causal dependency is consistent with an infinite
forward execution. Fresh short-lived helper modules can be created and
consumed indefinitely, and each new long episode may depend on one of
those earlier, short episodes. The finite-source theorem does not prohibit
such replenishment or charge its creation against any decreasing resource.

Furthermore a single helper consumption can witness many overlapping
marked episodes. The relation is not an injection from long feedback to
distinct fuel events. An individual helper has only finitely many such
parents in a fixed finite history, but no uniform bound on that number is
provided by this argument. No bounded branching or mass-only fuel budget
is inferred.

Thus the rigorous output is a chronological dependency DAG (with possible
sharing), not a globally decreasing potential. A useful next invariant
would have to restrict spatially usable replenishment or quantitatively
charge whole archive configurations across regeneration. The present
theorem alone supplies neither such a charge nor eventual translation,
standard104 classification, or universal finite-seed capture.
