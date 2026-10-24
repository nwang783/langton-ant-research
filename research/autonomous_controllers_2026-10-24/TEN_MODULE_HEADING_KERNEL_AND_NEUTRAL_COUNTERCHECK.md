# Exact heading-count kernel and five failed neutral completions

24 October 2026. Author analytic lemma and all-parameter physical certificate;
independent audit pending. No general four-heading exclusion is asserted.

## 1. A reusable fixed-router reduction

Let M=RRRRLLLLRL. Consider any FIXED finite template of router words with a
fixed finite number of inserted runs M^n_i. Each n_i is an arbitrary nonnegative
integer. M restores its incoming heading and has even length, so all run headings,
run checker parities, router headings and router checker parities are fixed by
the template, independently of the exponents. Normalize the initial heading to
N and the initial read position to (0,0).

Let N,E,S,W be the TOTAL numbers of M copies used at the respective actual
incoming headings. Let (X0,Y0), q0 and g0 be the full drift, odd-checker signed
charge and total signed charge of the concatenated routers with all M runs
empty. Assume those routers restore heading; otherwise the whole template
cannot be a heading-restored translating period.

The contributions of one M to (X,Y,q), where q is odd-checker R-minus-L, are

    N: ( 1, 1,-1),       E: ( 1,-1, 1),
    S: (-1,-1,-1),       W: (-1, 1, 1).

The checker signs are not optional decorations: the actual invariant sector
forces vertical arrivals at even relative checker parity and horizontal arrivals
at odd relative checker parity. Directly, M has charges(1,-1) from an even start.

Therefore every member, legal or not, satisfies

    X-X0 = N+E-S-W,
    Y-Y0 = N-E-S+W,
    q-q0 = -N+E-S+W,
    g = g0.

The kernel of this linear map is EXACTLY span(1,1,1,1): the first two zero
equations give N=S and E=W, and the third then gives N=E. In particular its
nonnegative kernel consists of simultaneous equal additions to all four heading
totals. It is not a finite-state or chronology theorem.

For a complete WHITE front the retained signed-residue theorem gives
|X|,|Y|<=g0/2, while exact complete-history balances give 0<=q<=g0. If g0<=0
there is no such front. For positive fixed g0 there are only finitely many
possible integer triples(X,Y,q). For each triple all four heading totals are
fixed UP TO their common additive parameter. If at least one heading has no
run in the template, its total is exactly zero and fixes that common parameter.
Thus only finitely many nonnegative run vectors can be complete WHITE, with
bounds derived from the template. This is what made e3812742 finite.

If all four headings occur, the common parameter is genuinely invisible to
these three balances. A finite exponent bound cannot be inferred from them.
No claim is made that every algebraic common-mode increase is a physical word.

## 2. A specific neutral extension of prepared80

Use the exact routers A,B,C,D of e3812742. In the supplied prepared80, C begins
with incoming S. Its cuts with incoming E are precisely k=3,5,7,9,13, counting
characters from zero. For such k and any integer n>=1 form

    W_k(n) = M^(n+2) A M^(n+1) B M^(n+1)
             C[:k] M^n C[k:] M D.

The inserted run is E-headed. Relative to the prepared80 base, this adds n
modules in EACH of headings N,W,S,E. Hence every W_k(n) has

    P=80+40n,      full drift(4,4),      growth12,

and the SAME two checker charges as prepared80. The simple count constraints
cannot reject these words by making n large. The n=0 word is the literal
prepared80 wave, regardless of k.

**Physical obstruction.** For every one of these five cuts and every n>=1,
W_k(n) is not even a finite factor on an arbitrary initial BLACK field. The
following are consecutive reads of the SAME physical cell, with the same turn:

    k=3, all n>=1:
      cell(-n,n+2), R at30n+52 and30n+56.
    k=5, all n>=1:
      cell(1,1), L at26 and40n+58.
    k=7, all n>=1:
      cell(3,1), R at22 and40n+66.
    k=9, n=1:
      cell(1,1), L at26 and90.
    k=9, all n>=2:
      cell(2,0), R at12 and40n+52.
    k=13, n=1:
      cell(1,1), L at26 and90.
    k=13, all n>=2:
      cell(3-n,n), R at30n+61 and30n+65.

Consecutive here means consecutive reads OF THAT PHYSICAL CELL, not consecutive
updates. Every read flips the cell, so either equal-turn pair is impossible,
independently of the cell's first color and all unread background bits.

## 3. Complete affine-history certificate

The certificate lists all event templates, not just the two selected endpoints.
Within a variable M run each phase has

    position = p0(n) + j*v,
    time = t0(n) + 10j + phase,
    0<=j<count(n),

where p0,t0,count are explicit integer affine functions of n. Every router
phase is explicitly retained with j=0. Matching a queried physical cell q(n)
requires two linear coordinate equations. One coordinate solves j as an affine
integer function of n; the other either agrees identically, singles out one
integer n, or has no solution. The exact j bounds give integer intervals of n.
Thus the algorithm enumerates EVERY read at the queried physical cell for every
n, without a geometric search radius or multiplicity bound.

Splitting only at those interval endpoints and exact clock-order crossings
gives nine complete-history pieces. Some listed witnesses have additional reads
before or after them, all retained. For example, at k=13,n=2 the queried cell
has an earlier L25, but its two later R121,R125 are still consecutive; n>=3
has no such earlier read. The complete table signs those distinctions rather
than assuming the witness cell was fresh.

This excludes these five neutral extension families only. Other E-heading
insertions, other router choices, reallocations of neutral counts, or reordered
runs remain open. It does not prove WHITE unit winding, prohibit all null modes,
or supply an autonomous controller.

certify_prepared80_neutral_four_heading_obstruction.py
SHA256 cb7b05d9f2ce36d89a8f32585897b439f7e798adf85973e7ccdb5359e2b5d823
prepared80_neutral_four_heading_obstruction_certificate.json
SHA256 9f427efe09e882dbbf0de8166f69081975ff531e2e549585e0cf155ff46263f6
