# Exceptional-renewal input placement separates the three supplied transports

23 October2026. Author theorem, frozen for independent audit. This is a
conditional finite-WORD organization result, not a classification of arbitrary
ants, arbitrary nonstandard words, or all possible translating mechanisms.
Every board in the statements is its COMPLETE actual finite black field.
No infinite prepared background, bounded-width assumption, cropped archive,
periodic full board, mass descent, or original-root upper budget is used.

## 1. Exact statements

Use the signed paired-cursor convention. A genuine **w erasure** is an actual
L whose deleted edge is a nonbridge in the FULL current w black graph.
It is therefore an exceptional renewal in the signed global cubic theorem.
An **entry-black lifetime** means a black cell present at the beginning of
the stated word interval, with no toggle between entry and its consuming L.
This refers to its CURRENT lifetime, not its original seed cell or original
black root. Earlier R writes are included as entry black when appropriate.

Let H be the retained104-word, phase pose(0,0),W, drift(-2,-2). Let W1564 and
W4352 be exactly the retained words with the hashes and phase poses below.
For every integer N>=1 and EVERY actual complete finite-board realization
of the corresponding literal N-word interval:

1. **Standard self-feeding.** After the first104 updates of H^N, EVERY L
   consumes a black lifetime born by an R within the preceding116 updates.
   In particular, every subsequent exceptional renewal is self-fed on this
   bounded time scale. At most13 entry-black lifetimes are consumed anywhere
   in the whole H^N interval, all within its first period. Extra unread
   initial black archives remain present; none is silently removed.
2. **1564 exceptional placement.** During W1564^N, at least40N DISTINCT
   entry-black lifetimes are consumed at genuine w-nonbridge L updates.
   There are40 certified such updates in EVERY one of the N word copies.
3. **4352 exceptional placement.** During W4352^N, at least102N+19 DISTINCT
   entry-black lifetimes are consumed at genuine w-nonbridge L updates.
   The constant includes the explicit finite start/end eligibility fringes.

The word1564 has730 L slots per period, and4352 has2084. Hence at least4/73
of ALL exceptional updates in a1564^N interval consume entry-black lifetimes;
for4352 the analogous lower fraction is51/1042. These fractions follow from
the crude upper bound exceptional-count<=L-count and are not claimed optimal.
They do NOT assert every exceptional update is input-fed.

This is not the earlier total first-L fuel count197N+1 or406N+57. It locates
an indispensable positive portion of that input at the actual cycle-erasing
archive renewals themselves, with explicit geometric cycles. StandardH,
in contrast, becomes uniformly lifetime-local after its first period.

## 2. Keep the complete normalized field, not just a profile

For any finite literal turn word A, its physical pose trace is determined
from its initial pose, independently of the board. Let READ(A) be its complete
finite read set, and let I(A) contain exactly the cells whose FIRST read
requires L. In any actual realization, the initial color on READ(A) is forced:
black exactly on I(A), white on the other first-read cells.

Thus the COMPLETE entry board has the exact disjoint form

    B_entry = I(A) union F,       F disjoint READ(A).

At every actual cut t,

    B_t = (I(A) XOR OddReads_before_t) union F.          (1)

The entire finite F is retained UNCHANGED with its actual coordinates. This
is an identity for a supplied actual word, not a boundary summary or a
claim that arbitrary words are realizable. It permits arbitrary nonperiodic
remote caps, arbitrarily long rail extensions, and old unread components.

Consequently any black CYCLE certified using only the forced left term of(1)
is also present in the full graph with F. Extra black edges cannot destroy
the nonbridge status of an edge on that cycle. This one-sided topological
monotonicity is the reason the following placement claims survive complete
archives, unlike a claim that a deleted edge is a bridge. We infer neither
bridge status nor full exceptional-word recurrence after discarding F.

## 3. Finite affine read certificates imply every N

Write P for the word length, d for its heading-restoring physical drift,
and p_i for its physical cell at slot i,0<=i<P, at the stated phase pose.
Then copy j reads p_i+j*d at time jP+i. For one template cell q, its FULL
list of possible occurrences relative to copy k consists exactly of triples

    (alpha,i,c_i) with p_i+alpha*d=q,
    relative time tau=alpha*P+i.                       (2)

The list is finite and reconstructed by exact integer coordinate equality,
not by a temporal cutoff. In copy k this occurrence is present precisely
when0<=k+alpha<N. No other read can occur at q+k*d.

At a selected deletion slot s, a template edge is certified black in one of
two ways:

* Its LAST full-list occurrence before s is an R. If that particular read
  is eligible, there is no intervening read at all, so the current lifetime
  was born by that R and is still black at s.
* There is NO full-list occurrence before s and the FIRST full-list occurrence
  is an L. If that particular future read is eligible, the cell must already
  be black at interval entry and has not yet been toggled at s.

For first-copy-only templates, first discard alpha<0, since those copy reads
are outside the interval. The same argument then applies at k0. Removing
further ineligible future reads cannot invalidate an eligible first read;
removing earlier reads cannot invalidate an eligible last-before read.

For each selected cycle, let alpha_min/max be the smallest/largest offsets
among its chosen black-edge witness reads. Its copies are certified whenever

    k>=l=max(0,-alpha_min),
    k<=N-1-r with r=max(0,alpha_max).                  (3)

At the target edge itself, the first full-list occurrence is exactly its
selected L at relative time s. Thus the target is an entry-black lifetime,
not merely a black cell that may have been recreated during the interval.
For start-only templates use the first copy-restricted list instead.

The file forced_input_cycle_templates.json gives every cell of each cycle,
every edge's complete occurrence list, chosen witness, copy eligibility and
target read. check_forced_input_cycles.py reconstructs all these lists from
ONE word copy, verifies every equality independently of the builder, and
checks that each listed black edge set is a connected degree-two simple
cycle in the actual w lattice. Cycles need not be disjoint; their target
lifetimes ARE distinct. The explicit coordinate disjointness checks below
prevent charging one input lifetime twice.

## 4. The exact cycle inventory and counting

The1564 word has SHA256
96e6e1dd2935e1e7afeb9dc14759320bb2b82bd2855b1596f9b1a591d1ff2122,
phase pose(-6,-6),N, drift(14,14). Its40 cycle templates all have(l,r)=(0,0).
They therefore contribute40N targets. Their cycle lengths are

    length4:24; length6:8; length8:6; length10:1; length12:1.

The4352 word has SHA256
ab99d9772e331733e765e37c6c7350929cc652431631de27320c0205c88ff30b,
phase pose(-2,3),W, drift(26,26). Its102 core templates have

    (l,r)=(0,0):96;
    (0,1):1;
    (1,0):5.

They contribute96N+6(N-1) for every N>=1. There are21 additional first-copy
input targets, distinct from core target slots. Four of the five left-fringe
core targets have alternate first-copy cycles and are restored by four
explicit start-only overrides. All25 start templates use witness reads
within copy0. Hence the complete lower count is

    96N+6(N-1)+21+4 = 102N+19.                         (4)

Every core target belongs to a different spatial drift orbit. A startup
target either lies in a different orbit, or at an index strictly below that
core template's first eligible copy. This is checked by solving exact
q_start-q_core=alpha*d. Startup targets are themselves distinct. Therefore
all counts in(4) refer to distinct physical cells and distinct entry-black
lifetimes, not multiple charges to one old edge.

Altogether there are167 explicit cycle witnesses with992 edge occurrences.
These finite geometric facts and exact eligibility inequalities prove the
all-N LOWER bounds. The finite examples N1,2,3,5 attain the displayed lower
counts on their minimal input boards, but equality for all N is NOT inferred
or needed. Arbitrary extra full-board archives may create still more erasures.

## 5. Why the standard renewals are uniformly self-fed

For H, reconstruct the same occurrence lists(2) for every one of its46 L
slots. In ALL cases the last preceding occurrence is an R with copy offset
alpha in{-1,0}, with no intervening occurrence, and the elapsed physical time
is at most116. These46 exact matching records are retained in
standard_self_fed_lifetime_certificate.json and reconstructed by the checker.

Thus at every L in any copy k>=1, the matching R belongs to the actual finite
interval: k+alpha>=0. It creates exactly the black lifetime then deleted by
that L. Every L, not just the cycle-erasing subset, is covered. This statement
uses no assumption about the topology of the unread full archive F.

In the first period only13 first-read cells require initial black, verified
by the literal104-update read history. Later L slots all have the stated prior
R witness, so no further entry-black lifetime can be consumed. Hence the
whole H^N interval consumes at most13 such lifetimes, all in its first copy.
The full word retains its emitted wake and every unread black component.

The age bound concerns black lifetimes, not mere physical cell revisits,
not a root's original birth time, and not distance to a current frontier.
It is also a conditional consequence of actually executing H^N; the theorem
does not assume that arbitrary finite ants execute H or classify self-fed
words as uniquely standard.

## 6. Literal finite original-seed controls and an unbounded-age obstruction

The placement theorem applies directly to the retained all-N184-cell1564
producer. Its immutable affine source is
../causal_reduction/unit_scale/prepared1564_uniform_support_manifest.json,
SHA25690fcf1a66046418c38d07f7e935ea80cf873751aefae69a4b07af89ba3bd8399.
The independently signed source-endpoint and backward certificates already
show this SAME family is bi-standard; no new reachability premise is added.
For every N it executes the prescribed wave N times with NO post-start edits.

Among the40 certified entry-black target lifetimes in each of the last five
copies there are200 distinct lifetimes. At most184 lifetimes can descend
unchanged from the original initial black cells without an intervening R.
Thus for N>=5, at least one of these200 exceptional targets was actually
R-born during the earlier preparation, before wave entry. Its consuming w
erasure occurs no earlier than1564(N-5) updates after wave entry. Its actual
R-to-L lifetime age is therefore at least1564(N-5)+1.

Consequently there is NO finite upper bound depending only on original mass
for the lifetime age consumed by exceptional updates, EVEN for R-born tokens
and EVEN within these already bi-standard original184-cell orbits. This is
an actual finite-seed family countercontrol, not a cycle of abstract profiles.
Different N give different finite seeds; no one seed with infinitely many
nonstandard renewals or unbounded-age exceptions is claimed.

The author also executes the entire finite preparation on its whole board
before measuring three wave periods, retaining all old writes and remote
seed cells. The observed N3 controls are:

*1564: original mass184, preparation163819 updates, wave-entry mass19121;
 old-input genuine w erasures77,78,78 versus total input L198,197,197.
*4352: original mass394, preparation245802 updates, wave-entry mass28354;
 old-input genuine w erasures141,112,112 versus total input L463,406,406.
*StandardH from its13-cell seed: old-input L13 in the first period, zero
 thereafter; all later L lifetimes have age<=116.

The larger counts in prepared fields are compatible with the universal
lower certificates: unread rails and cap debris can supply additional cycles.
All extra full-board data is retained in these literal controls. These finite
numbers are controls only, not the source of the all-N quantifier.

## 7. Exact gain, and the remaining organization gap

The result is a robust causal discriminator for the THREE SUPPLIED WORDS:
standard renewals become bounded-age self-fed, while both named nonstandard
words force recurring cycle erasures of black lifetimes already present
before the entire word interval. It does not merely count total input fuel,
and its cycle witnesses survive arbitrary unread archive modifications.

It does not show that every nonstandard word is input-fed, that every
self-fed word is standard104, that all finite ants eventually have bounded
renewal age, or that arbitrary endcap scattering cannot prepare more fuel
and launch another word. The fixed184-cell family specifically forbids a
uniform original-mass age budget as a shortcut. Universal finite-seed capture
remains open; a genuine organization proof must handle new self-fed words
or arbitrarily renewed preparations, not just exhaust these two supplied
wave input stocks.
