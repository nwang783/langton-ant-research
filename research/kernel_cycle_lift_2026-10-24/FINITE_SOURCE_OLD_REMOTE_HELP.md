# A finite-source bound for completed bounded-active feedback

24 October 2026. This is an existence theorem, not a quantitative route
conjecture. It uses the independently checked fixed-parameter erasure lemma
in Sections2/3 of `PRODUCTIVE_RETURN_REMOTE_HELP_TEST_v2.md`, with the
qualification preserved in Version3: the ORIGINAL supplied bound M remains
the parameter after deletion. It neither uses nor proves RH16/4.

## 1. Exact setup and statement

Use a complete finite black board B_t and the ordinary deterministic ant.
C_t is its COMPLETE active w component at fine cut t. A black lifetime is
one uninterrupted black interval at a fixed physical cell; a later rebirth
at that cell is a different lifetime.

At update d-1 a bridge L leaves a surviving marked black lifetime e in a
dormant complete w component at cut d. Its next physical read is its actual
consuming L at update c, where c>=d. Between d and c it may undergo
arbitrarily many unproductive activations and departures. Suppose M>=1 is
an integer upper bound on |C_t| at EVERY fine cut d-1<=t<=c. It need not be
the actual maximum. Put p=p_d and Q_M=[-4M,4M]^2 intersect Z^2.

The old cohort consists of the lifetimes already black at cut d. An OLD
REMOTE CONSUMPTION means an actual L at some update j in [d,c], at a cell
outside p+Q_M, consuming that cell's lifetime already present at cut d.
Later R births outside the box are not old-cohort resources.

**Theorem.** There is a finite integer F(M), depending only on M, such that
every episode above with NO old remote consumption satisfies c-d<=F(M).
Consequently, if c-d>F(M), at least one old remote lifetime is actually
consumed during [d,c]. No computable cutoff, explicit estimate, capture,
or eventual-periodicity conclusion is asserted.

The lag c-d counts updates before the marked read. The interval including
the consuming update has c-d+1 updates, hence at most F(M)+1 in the no-help
case. In particular every head excursion before that read is at most F(M)
in infinity distance from p, by unit-speed motion.

## 2. A finite deterministic ensemble defining F

For fixed M let S_M contain ALL triples (B,h,x), with B a subset of Q_M,
h one of the four headings, and x an element of B. The initial head is 0.
These are full physical states, not abstract active shapes, summaries,
archived-module types, or variable environments. They retain every initial
black cell in the fixed box. No outside black cells are supplied later.
All subsequently written cells, however far away, evolve normally.

Writing N=(8M+1)^2, the exact cardinality is 4N*2^(N-1), hence finite.
For s=(B,h,x), let tau(s) be the least t>=0 at which the physical head
reads x, or infinity if it never does. Because x starts BLACK and has not
previously been read, a finite first read is its L consumption. Define

    F(M) = max( {0} union { tau(s) : s in S_M and tau(s)<infinity } ).

This maximum is finite. We do not need to identify the successful states,
decide which marks are never reached, or decide any eventual behavior.
One could restrict to states satisfying cap M until their finite first
read, but the larger ensemble above is simpler and already sufficient.
Including all four headings avoids any rotation-normalization assumption.
Translation of a physical state and its mark preserves tau; the coupled
w convention is translated with the actual pose, not held to an unrelated
fixed checkerboard label.

## 3. Why every no-help episode has exactly one such first-read time

The signed active metric and fixed-parameter localization lemma give:

* At cut d the marked component and its cell x lie within M+1<=2M of p.
* At every cut through c, the ENTIRE complete component containing the
  still-black marked lifetime lies in p+Q_M. While active this follows
  from head-to-mark and edge-to-head bounds; while dormant its complete
  component is frozen until an R import. Later departures preserve the
  same induction. No bound on the opposite z component is assumed.

At cut d delete ONCE the old black cells outside p+Q_M. Each deleted cell
is unread during [d,c]: its first later read, if any, would be an old L,
contrary to the no-help hypothesis. The first-difference argument therefore
preserves the entire physical read trace, head, headings and both cursor
positions through the marked read at c. The new board at each cut is the
old board minus precisely these never-read old cells.

The new black graphs are subgraphs, so their active w cap cannot increase.
Unmarked temporary active components may shrink or change cycle labels;
we do NOT infer graph equality from unchanged physical execution. For the
marked component, localization proves that no removed edge belongs to it
at ANY cut. It stays connected and complete, and deletion cannot attach
new edges. Thus its complete field and its active/dormant itinerary are
exactly preserved, including the final productive import and consumption.

Translate p to 0 and keep the heading h_d. The resulting complete board
B is a subset of Q_M and x-p is one of its black cells. It defines one
state s in S_M. The actual marked lifetime remains black until update c;
there is no earlier read of that coordinate. Exact trace coupling hence
gives tau(s)=c-d, not merely an upper bound on some later visit. Historical
birth time, whether the mark originally came from a seed or an R, and all
earlier unproductive reattachments are irrelevant to this deterministic
first-read identity. The definition of F proves the theorem.

## 4. Parameter and effectiveness scope

Deleting old exterior may lower the reduced orbit's actual active maximum
from M to M'. This causes NO problem: its board remains in the ORIGINAL
Q_M and the theorem always uses the ORIGINAL certified M. We make no claim
that the reduced board lies in Q_(M') or preserves a predicate recomputed
at M'. This is not the withdrawn exhaustive reduction for RH16/4.

Finite cardinality proves existence of F(M), but does not by itself provide
an algorithm that knows when every future successful first read has been
seen. In particular no finite search deadline or decision procedure is
claimed. Nor do we claim that F is uncomputable: that would require a
separate proof. The word 'non-effective' describes the present argument,
not a proved impossibility of effective bounds.

The conclusion charges an actual old lifetime, not unread topological
support, and allows all legal new-field regeneration. It bounds departure-
to-first-consumption lag in the NO-old-remote-help case, not total birth age
or arbitrary dormant waiting without eventual consumption. The existence
bound supplies no control on how often fresh helper modules can be made.

## 5. Exact dependencies

* `active_w_archive_itinerary_2026-10-23/ACTIVE_EPISODES.md`, SHA256
  ad3cb9f07e078bcbaaa02622004f56254b211de2ed238fa2bd031e7d5e3d5721.
* `PRODUCTIVE_RETURN_REMOTE_HELP_TEST_v2.md`, SHA256
  b64ec3398bcdfe34ea458d6df099653817b453ce4367fb22d6159fcc74683f9b,
  ONLY Sections2/3, under the original-parameter qualification.
* `PRODUCTIVE_RETURN_REMOTE_HELP_TEST_v3.md`, SHA256
  d186f40a3f4b1d15a41b58cdcf2e4a30bcfc6c5ee55584770762331f98a936a4,
  preserving that qualification and withdrawing the actual-maximum shortcut.
* Independent erasure report `audits/check_marked_component_old_cohort_erasure_independent.json`,
  SHA256 dd96119ec0f88e45d9a3cb43c66e6c167dba5794b62a07da8af7cd6d5379c1c4.

No new simulation or broad seed scan is a dependency of this finite-set
argument. Its proof obligation is the exact compact first-read coupling,
not any experimental estimate for F(M).
