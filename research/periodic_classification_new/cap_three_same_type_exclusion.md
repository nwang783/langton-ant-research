# Same-type triples cannot occur in a complete white cap-three front

22 October 2026. Independent analytic review accepted and bound the saved four-case argument
below. This is an
all-period local theorem, not a bounded-search result.

## Setting and statement

Consider a nonzero translating Langton-ant word whose stable histories at
every full-drift class alternate R,L,R,... from white and have length at
most three. Lift its periodic path to all integer times. Every physical
cell has a finite complete history and every event has an actual predecessor.
There is no initial-head exception in this two-sided front.

**Theorem. Every triple cell has opposite first and third incoming headings.**
Thus the same-type AAA and ABA classes do not occur. The proof uses the
established triple-edge pairing, but does not use a bound on the period,
a primitive drift substitution, or a topological disk assumption.

## A paired normalization

Suppose a same-type pair exists. Rotate and translate it so its shared
triple edge goes east from u=(0,0) to v=(1,0). The ordered incoming headings
are

    u: N,S,N  (ABA),       v: E,E,E  (AAA).

The three consecutive passages through the pair are RR, LL, RR. Put
p=(0,-1) and q=(1,-1). The edge p->u is used exactly twice, on the first
and third R reads of u. The edge v->q is used exactly twice, on the first
and third R reads of v. The relevant first passage is therefore

    p --X--> u --R--> v --R--> q --Y--> ...

where X and Y are the turns at p and q.

If X=R, this is p's globally first read: p->u has another later traversal,
so this R cannot be its third read. If X=L, it is p's middle read and the
later p->u traversal is p's third R; the heading pattern at p is AAB.
Likewise Y=R is q's first read, while Y=L is q's middle read and q has
heading type ABB. These assertions hold also when p or q is a double
cell or another same-type cell in the R cases.

## Four exhaustive cases

**X=R, Y=R.** All four displayed reads at p,u,v,q are first reads.
The R at p exits north, so its incoming heading is west. Its immediately
preceding cell is q. This requires an earlier q read before the displayed
first q read, a contradiction.

**X=L, Y=R.** The R at q has incoming heading south and exits west back to p.
Since p just read L, its immediate reread is R and exits north back to u.
This is the second traversal of p->u, hence should deliver u's third R.
But between the displayed first R at u and this reentry only v,q,p were
read, leaving no middle L read at u. Contradiction.

**X=R, Y=L.** The first R at p again requires a preceding read at q exiting
west. Since the displayed q read is its middle L, that earlier q read is
its first R. A right turn exiting west has incoming heading south, so
that earlier q read was preceded by a read at v. This precedes the
displayed first R at v, a contradiction.

**X=L, Y=L.** On the third passage through the pair, the consecutive reads
are p's third R, u's third R, v's third R, q's third R. The last of these
exits west to p, forcing a fourth read there. Contradiction.

All four cases fail, proving the theorem.

## Scope of finite-trace variants

The same proof applies to a complete initially white local configuration
in a finite trace when every predecessor invoked above exists, and the
forced continuation in the last case is part of the trace. It must not
be applied blindly at the initial head or at the terminal boundary. The
saved finite control `double_cycle_initial_head_exception.json` contains
a same-type doubled square through the initial head, so this caveat is
real. The theorem above concerns a complete translating white-input front
and has neither boundary exception.
