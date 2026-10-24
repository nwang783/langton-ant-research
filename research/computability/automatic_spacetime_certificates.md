# A stronger exact certificate language: automatic space-time

22 October 2026. Status: general analytic certificate framework, independently audited for standard numerical encodings; the complex-base implementation extension is stated separately below. No nonperiodic ant certificate has been found. This is a distinct, potentially useful synthesis target, not a universality claim.

## Why move beyond Presburger descriptions?

presburger_spacetime.md proves that a finite ant trajectory has Presburger-definable time-indexed space-time exactly when its turn stream is eventually periodic. Thus searching only for such descriptions cannot certify a genuinely aperiodic counterexample.

Synchronous finite automata over integer digits describe a strictly broader class of relations, while retaining effective closure under first-order definitions. For example, powers of a fixed base are automatic but not Presburger-definable. That example concerns the expressiveness of the language, not an ant trajectory.

Fix a base and a standard automatic presentation of the integers with addition and order. Supply finite automata for the four head relations P_h(t,x,y) and the color relation C(t,x,y). All use that same numerical encoding. Restrict the evolution times to t>=0.

## Exact certificate verification

Use exactly the initial-state, unique-head, bit-flip and turn/move sentences from presburger_spacetime.md. They are first-order sentences in the structure consisting of integer addition/order together with the supplied automatic P_h and C. Boolean operations and projection of synchronous automata effectively decide all these sentences.

If validation succeeds, determinism and induction prove that these automata describe the actual complete orbit from the supplied finite initial black set. There is no assumed bound on time, support, period, width or retreat.

Then define the left-turn predicate by

   L(t) iff exists x,y: C(t,x,y) and OR_h P_h(t,x,y).

For a fixed cyclic standard word w of length104, define its phase predicate A_w(r) as the disjunction of those residue classes modulo104 where the word has L. Eventual standard capture is the first-order sentence

   exists T>=0: forall t>=T, L(t) iff A_w(t-T).

Allow the finitely many phases if a chosen word convention requires them. Heading rotations do not change the relative L/R word. Decide this sentence, or its negation, using the automatic presentation. Consequently a validated automatic model together with a negative answer is a finite, exactly checkable certificate of a finite-seed counterexample.

General eventual periodicity is likewise first-order:

   exists T>=0 exists p>=1: forall t>=T, L(t) iff L(t+p).

Therefore the same framework separates alternative periodic highways from genuine aperiodicity.

## Computability consequence

The set Auto of finite seeds whose complete history has some automatic presentation in the chosen effective class is c.e.: enumerate the finite automata and run the validator. Every eventually periodic seed belongs to Auto by the Presburger construction.

Membership in standard capture is decidable on the promise Auto: wait for a validated presentation, then decide the capture sentence. If every finite seed belonged to Auto, capture would therefore be decidable on all finite seeds. This is conditional, not a proved automaticity theorem.

Thus any proof that standard capture is undecidable would force histories outside this automatic-certificate class, not merely histories outside the ultimately periodic class. Conversely, finding one validated automatic NONcapture model would already refute the universal highway conjecture without any halting reduction.

The existence of automatic predicates is not itself evidence that the ant admits any such aperiodic trajectory. A model must pass the full all-time local-rule and finite-initial-data validation.

## Precise implementation obligations

- Do not use arbitrary custom numerations unless their integer addition/order automata and equality conventions are provided effectively.
- The automata must represent complete numerical relations, including padding/canonical-encoding conventions; projected variables may need longer digit strings than free variables.
- Validate uniqueness/existence of the head at every time, not just the updates at recognized head points.
- Validate global initial whiteness outside the finite seed, not only a finite tested rectangle.
- Decide the negated capture sentence exactly, rather than relying on long nonperiodic samples.

These are ordinary automatic-structure constructions. A primary reference for their effective first-order closure is Khoussainov and Minnes, *Three Lectures on Automatic Structures*, Theorem7 (2008), https://arxiv.org/abs/0809.3430 . Its finite-automaton Boolean/projection proof supplies the algorithmic foundation; the ant application above is the deduction made here.

## Stronger inverse theorem: pose automata alone suffice

This extension has independent analytic audit approval. Suppose a supplied automatic relation specifies a unique pose at every time. All of the following conditions are first-order and hence decidable:

1. Consecutive poses are linked by exactly one quarter-turn and the corresponding unit move.
2. At any two consecutive visits to the same cell, the prescribed relative turns are opposite. Consecutive means that no intermediate time visits that cell.
3. The set B_min of cells whose first visit prescribes L is finite.

These are necessary and sufficient for that entire pose path to be the trajectory of some finite initial black set. Necessity follows from the local flip rule. For sufficiency take B_min as the black set and every other cell white; induction through each cell's visit order gives its prescribed read bit and hence the prescribed complete path. Unvisited black cells would be optional and irrelevant. Thus B_min is the unique minimal seed.

For ordinary coordinate encodings, finiteness is the FO assertion that B_min is contained in some bounded square. Once it holds, search for such a square using the decision procedure, then enumerate its finitely many cells. The minimal seed is effectively recoverable, not just existentially asserted.

The color history can be recovered by FO definitions without a counting extension: before any read of q, retain its initial B_min bit; otherwise its bit is black exactly when its most recent read before t prescribed R. Most-recent-read is itself FO. This construction is sound after the alternating-visit condition has passed.

The research implementation automatic_relations.py provides base-two Boolean operations, quantification, arithmetic atoms and the first-visit/consecutive-visit tests for nonnegative coordinate variables. Existential projection explicitly allows hidden witnesses with longer encodings than the free variables. Controls cover36,864 arithmetic point comparisons, a value1024 (eleven-bit) hidden witness, an infinite RL staircase that passes alternation but fails finite-first-L, and an R-only geometric square that fails alternation. It is not a formally verified library and does not yet implement the complete proposed-path search.

## Representation extension for genuinely self-similar geometry

The inverse theorem needs an effective automatic presentation of time order and the physical grid; it does not intrinsically require ordinary binary x,y coordinates. One may use binary time and encode a cell z=x+iy as a Gaussian integer in complex base beta=-1+i with digits0,1. Every cell has a unique finite digit string up to zero padding, and each unit-neighbor relation is recognized by a finite carry automaton.

Here is the direct carry argument. For the relation w=z+delta, start with carry -delta. On the next least-significant digits a of z and b of w, replace the carry by (carry+b-a)/beta, rejecting a non-Gaussian quotient. Accept at the end precisely for zero carry. Carries stay bounded because their magnitude is at most (previous magnitude+1)/sqrt(2), and unit delta has magnitude1. Thus only finitely many carry states occur. This checks actual grid adjacency, not adjacency in the numeral's lexicographic order.

The canonical representation is a standard number-system result. A primary modern source is *Automata and Arithmetics in Canonical Number Systems* (2025), https://www.mdpi.com/1999-4893/18/3/122 . The unit-carry proof above is the special construction needed here. A self-contained existence check is also short: choose digit a=(x+y) mod2 and divide z-a by beta; the magnitude strictly decreases outside radius sqrt(2)+1, and the finite remaining Gaussian points can be checked to reach zero. Uniqueness follows successively modulo beta.

For this grid encoding, test finiteness of B_min after intersecting its regular numeral language with canonical representations (no most-significant zero except the zero convention). Regular-language finiteness is decidable. It must not be confused with finiteness of the zero-padded language, which is infinite even for a singleton cell.

This extension does not make an arbitrary k-regular integrated position sequence automatic. A candidate still needs an actual synchronous pose-graph automaton in the chosen numerical presentations.

A simple folding negative control: let the outgoing direction at step n be i^popcount(n xor(n>>1)), with an eastward first move and initial heading N. The resulting ordinary dragon walk prescribes R at the same cell(-2,1) at consecutive visits7 and11. Thus this specific path violates condition2 on every initial coloring; it is not a finite-seed candidate.

## Important scale distinction: a negative-only mixed-base class

The binary-time / beta=-1+i grid representation above is NOT the same class as ordinary binary-time/binary-coordinate automatic histories. In particular it does not contain standard highways. This distinction has independent analytic audit approval.

Suppose an N-state synchronous automaton represents a total single-valued position function in this mixed encoding. Its canonical output has length at most the canonical binary input length plus N (up to a fixed encoding convention). Otherwise, in the portion after the time input has become all zero, an automaton state repeats before the last nonzero cell digit. Pump that loop. The time value is unchanged, but the last nonzero output digit moves to a later position, producing a different canonical Gaussian integer. This contradicts single-valuedness.

A cell with l beta digits has norm at most (sqrt(2)^l-1)/(sqrt(2)-1). Thus every such position function satisfies |p(t)|=O(sqrt(t+1)). Every ultimately periodic finite-seed ant turn stream instead has a nonzero linear drift; a zero-drift or heading-nonrestoring periodic turn stream would have bounded path, which is impossible for the classical ant. Consequently ANY finite-seed ant successfully realized in this mixed-scale automatic class would be genuinely aperiodic and would refute the universal standard-highway conjecture. No such realization is known.

This makes the mixed-scale class a useful negative-only synthesis target. The earlier assertion that every periodic ant belongs to Auto refers to the ordinary common-base coordinate presentation, or to an effective union of presentations containing it, not this mixed-scale subclass.

Implementation note: the current bounded() method orders a cell's canonical digit CODE as an ordinary natural number, not its physical x or y coordinate. Because canonical codes biject grid cells, bounded code is equivalent to finitely many cells, so this is a valid finiteness test. A direct finite-language test is an equivalent alternative. No geometric inequality is inferred from CODE order.
