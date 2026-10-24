# All-age minimum-clock cohorts in the strict U1 premise

23 October 2026 11:18 UTC. Independently signed LN phase-parametric theorem,
11:20 UTC. This is one fixed finite birth-chronology construction for arbitrary
input ages, not an age-by-age kernel escalation or a bounded ant-path search.

Normalize a U consumer to(0,0,N), global phase1, with input labels
a=(-1,1),q=(-1,2),b=(-1,4),c=(0,2),d=(0,3). Suppose q is produced with
C age k>0 and EVERY other input has age>=k (entry infinity is permitted).
Thus q belongs to the youngest C-clock group S, which may contain tied births.
No claim is made here when another input is strictly younger than q.

Proposition. In the strict U1 unfunded-record premise, ALL identities in S
share one actual source packet. There are only the sixteen necessary source
templates listed below, depending on k modulo4. None is asserted attainable.

## Finite necessary construction for an unbounded age parameter

Every identity in S is born at C clock Cconsumer-k, with source heading
h=k modulo4. The complementary inputs have larger ages and are already
current before all these births. Actual input birth packets, in chronological
order, form a finite subsequence. Between two such packets every retained
packet has zero C, hence is D/V/U at the fixed heading h. Each producer except
the last must itself have zero C. The last may contain C, included in k.

Rotate any displacement from one producer exit to the next source head back
by -h to (dx,dy). Exact endpoint compatibility is

 dx=d+v, dy=d+3v+4u,  d,v,u nonnegative integers.

Equivalently dx,dy>=0 and some integer 0<=v<=dx has dy-dx-2v a nonnegative
multiple of4. This retains arbitrary intervening zero-C lengths exactly at
the endpoint level, while forgetting their guards and input supply. Such
forgetting only enlarges the candidate histories.

For each h, enumerate every sector-compatible retained producer placement
having at least one output in the five fixed input cells. There are
97,103,111,103 placements for h=0,1,2,3. A birth source must avoid the complete
contexts of all older/current FINAL input identities. It may produce any
nonempty subset of the not-yet-born final inputs contained in its outputs.
Other outputs are not assumed to persist. This allows temporary identities at
later-final cells to be retired and replaced; no identity is silently reused.

The finite state is (current final-input subset, last source placement,
number of relevant source packets). Every edge adds at least one of just
five final identities. Thus at most five relevant source packets is a
mathematical consequence, not a search-depth cap. Sixteen older subsets are
possible because q is new. The checker exhausts ALL reachable states and
records ALL transitions, with no early stopping at a completion.

Before the strict-record intersection, the four finite graphs have
(states,arcs,completed states)=(301,389,20),(257,289,8),(251,270,3),(240,238,9).
The heading-zero graph genuinely permits two-source completions in this
necessary relaxation; they must not be dropped just because the other
headings have only one-source completions.

## The FULL strict-record filter

Use H=y-x, A=(0,22,20,10) and existing created-peak table T. A source at(p,h)
is permitted only if BOTH

 2H(p)+A[(h+1) mod4] <30,  2H(p)+T[source,(h+1) mod4] <30.

The first is its ENTRY CORE value. It must not be omitted when the created
peak is lower than the entry core. The checker independently recomputes A
and every T from the retained literal geometry and potential weights, then
compares them with the existing U1 metadata. Every relevant birth source is
strictly before the U consumer, so both strict inequalities are necessary.
Record restrictions on unobserved intermediate zero-C packets are forgotten,
again conservatively enlarging the graph.

The filtered finite graphs have respectively
(20,4,4),(100,84,3),(251,270,3),(237,235,6) states/arcs/completed states.
Every one of their sixteen completions uses ONE producer, proving the first
assertion. In each following case S is exactly the displayed set and every
other input is STRICTLY older than k (or entry-old):

- k=0 mod4: S={a,q}. Source VC/VCC at(-4,-2,N), or UC/UCC at(-3,-3,N).
- k=1 mod4: S={a,q,c}. Source V/VC/VCC at(-1,2,E).
- k=2 mod4: S={q,c,d}. Source U/UC/UCC at(1,3,S).
- k=3 mod4: either S={a,q,c,d}, source U/UC at(0,1,W),
  or S={a,q}, source V/VC/U/UC at(-1,0,W).

These are four+three+three+six templates. Small k can have additional signed
counted-age exclusions; the table is a necessary superset uniformly for all
k in its residue class. It does not invent exact-k kernel clauses from the
overflow class and does not assert that every template is realized.

## Direct consequences and relation to earlier partial filters

For q age4, LN plus KV already proves q is tied with a and all upper inputs
are older. The full strict U1 filter therefore leaves FOUR of the earlier
eight necessary source templates: the heading-zero line above. The prior
six-template statement explicitly used only CREATED peaks. DC(-4,0,N) and
UC(-3,1,N) additionally have forbidden ENTRY core value30.

For q age5 and a>=5, KV makes q a youngest input, so the heading-one line
applies: a=q=c=5, b,d>5, one V-family source. The prior unrestricted eight
cohorts remain valid. Their four-input U-family sources(-1,4,E) enter at core
value30, and their distant pair sources enter at38, although their created
peaks alone were lower. This is why full strict-record filtering removes
them. No previously signed partial created-peak calculation is reversed.

The theorem constrains simultaneous origin and older-support obligations in
the open U1 premise. It does not close U1: another input may be younger than
q, and even the sixteen surviving templates have a genuine funding-score gap
to target30. No score30 debt is propagated backwards here. No finite U, C,
incidence-cycle-rank or initial-root budget, or global capture, is inferred.
