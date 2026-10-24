# A finite record-language certificate against arbitrary-choice inflation

22 October2026. Status: general abstraction independently passed analytic review (21:25 UTC).
Its concrete k=9,a=3 instance has a complete independent replay in
check_position_k9_record_independent.py/json and the causal analysis's
position_only_k9_record_exclusion.md. No controller assumption is made.

## 1. Target class and finite local obligations

Suppose a finite-seed ant path, with p(0)=0, obeys

    p(kn)=a p(n)  for all n>=0,

where k>1 and a>1 are integers. We impose no relation between the headings
at n and kn. A geometric macro record consists of a coarse incoming heading,
a coarse turn, a fine incoming heading, and a length-k word whose displacement
is a times the corresponding coarse unit step. Keep every internally feasible
record; ignoring initial colors is a sound overapproximation.

The following THREE finite checks suffice to exclude the whole class.

(A) Relative to the macro's starting center, every read height is at most
2a-1. If its coarse step is not north, every read height is at most a-1.

(B) Enumerate all pairs of macros: the first goes from(0,-a) to(0,0), and
the next from(0,0) to(a,0), with their fine headings connected. Impose read
alternation in the pair and white FIRST reads throughout y>=0. Every retained
pair must have ALL first-macro reads below y=0 and second-macro entry heading
north. Let Aset be its finite set of possible second-macro words.

(C) Form a directed graph on Aset. Put an edge U→V whenever there is an
internally alternating k²-letter fine word refining the coarse k-letter word
U, both starting north, whose first fine macro is V. Every fine boundary
heading other than the first is unrestricted. Require exact positions
p_fine(kj)=a p_coarse(j),0<=j<=k, and allow arbitrary initial colors.
The resulting finite graph must be acyclic.

All obligations are decidable by finite literal enumeration, with SAT or
other search machinery merely accelerating a finite problem. An empty Aset
already certifies exclusion. A nonempty cyclic graph proves nothing positive.

## 2. Proof from arbitrarily high fresh records

A finite-seed ant is unbounded. After a quarter rotation, choose arbitrarily
high north-coordinate records Y above the initial black support and origin.
Let t(Y) be the first time row Y is reached. Its incoming heading is north
and its read is R.

For any earlier coarse macro n<t(Y)-1, either its center has height<=Y-2,
when(A) bounds all fine reads by a(Y-2)+(2a-1)<aY, or its center is at Y-1
and its step is not north, when the bound is a(Y-1)+(a-1)<aY. Therefore the
fine upper half-plane y>=aY is pristine before the predecessor macro.

The predecessor/record pair falls under(B), after translation. Consequently

    t(aY)=k t(Y),
    heading at k t(Y) is north,
    W[k t(Y):k t(Y)+k] belongs to Aset.

Repeat at Y,aY,a²Y,... . With t_r=k^r t(Y), all words

    U_r=W[t_r:t_r+k], r>=1,

belong to Aset. The original global identity gives the FINITE relation

    p(k t_r+kj)-p(k t_r)=a*(p(t_r+j)-p(t_r)),0<=j<=k.

Thus the actual k²-letter block at t_(r+1) gives an edge U_r→U_(r+1).
This produces an infinite path in the finite acyclic graph from(C), a
contradiction.

One must not assert that the entire time-shifted trajectory obeys the original
inflation equation. Only the displayed two-level finite-block relation is
needed and is valid.

## 3. The checked scale-nine instance

For k=9,a=3, independent checks give:

- 262 internally feasible nine-letter words;
- 240 oriented geometric macro records;
- maximum read heights4 overall and2 for non-north coarse steps;
- exactly6 pristine predecessor/record pairs;
- Aset={RRLRRRRLR};
- no edge from that sole word to itself: complete refinement BFS has635
  nodes and8,877 literal conflicts, with no seventh macro extendible.

Hence the theorem excludes arbitrary history-dependent position-only
scale-nine inflation, not merely finite-symbol substitutions or controllers.

## 4. Possible extensions, not established here

The same scheme can retain more finite record context when the next record
is reached slightly before an aligned macro boundary. That requires proving
an exact offset-state transition, not pretending records align automatically.

For non-real Gaussian scales, fresh records rotate between supporting
directions. A finite direction-cycle/heading-state version is plausible for
rational-angle rotations; diagonal supporting lines may have two possible
incoming record headings. None of those extra cases is claimed by this note.

This certificate checks a self-similarity architecture. It does not bound
the number of scales in a general ant trajectory and does not establish
standard-highway capture.
