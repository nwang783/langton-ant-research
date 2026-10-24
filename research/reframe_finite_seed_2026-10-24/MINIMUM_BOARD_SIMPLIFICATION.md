# Mandatory scope clarification: minimum-board replay precedes CNF

24 October 2026. Author proof and controls pending independent audit. This
clarifies SYMBOLIC_CAPPED_WORD_GUARD.md without invalidating its equivalence.
Minimum-board reasoning and finite-board reversal are retained facts, not
claimed discoveries. The CNF is NOT necessary for bare word existence.

## Exact minimum-board principle

Fix a literal finite word and its head path. At each visited cell, its initial
color is forced by the first read: initially black for a first L, white for a
first R. Repeated reads must alternate colors; any inconsistency excludes the
word. Let B_min contain exactly the first-read-L cells.

Every realizing initial board is B_min union X, where X consists of cells NEVER
read by this entire word. Such extras remain unchanged. At every cut the actual
black field is exactly B_min,t union X, on the same head path. Consequently its
complete black w component contains the minimum-board component. Additional
unread cells cannot repair an upper-cap violation or make a nonempty required
seam empty.

Thus literal B_min replay decides existence of the word with any prescribed
UPPER active-component caps and EMPTY seams: if minimum replay passes, it is
itself a finite witness; if it fails, every realizing board fails.

## First-return interior nonemptiness does not create an exception

For this ant's actual transition algebra, the active w root is empty exactly
when the next four turns are RRRR. Four R turns keep w fixed and read each of
its four incident cells once, so all four were initially white; conversely
four incident white cells force those turns.

Suppose the minimum board has an interior empty cut in a word whose final
minimum-board root is empty. That final empty cut must be reached by an L,
because any R leaves its newly inserted edge active. If fewer than four turns
remain after the interior empty cut, they would all be R, contradicting the
final L. Otherwise the next four prescribed turns are RRRR, forcing that same
interior root to be empty on EVERY board spelling the word. Hence unread
extras cannot repair first-return interior nonemptiness either.

Therefore minimum-board replay is necessary and sufficient for bare capped
FIRST-return existence as well. No SAT solver, bounded-neighborhood expansion
or enumeration of component profiles is required for this existential question.

## What remains useful in the symbolic guard

The depth-M reachability lemma and shared-cell CNF remain exact alternate
encodings. Their potential use is in ADDITIONAL observations not monotone under
unread black extras: prescribed imported modules, complete component shapes,
resource changes, or universally quantified fuel inequalities. A minimum board
can fail a required lower component-size or resource condition that a larger
board satisfies. For example, on the one-turn word R the blank minimum has
active mass1, while adding the unread cell(-1,1) gives active mass2 without
changing that turn. Such extra observations need their own exact constraints.

The CNF paper must therefore be read with this clarification. Its construction
is not promoted as a necessary/new solution to bare word existence. All23
surviving cap-seven words are already witnessed by their minimum finite boards;
the separate packed CNF models verify the alternate encoding, not a harder
new satisfiability discovery. Their mutual composition is a different question.

## Controls

minimum_board_word_checker.py checks350 read-consistent words of length at most8
against2,800 explicit unread-background supersets, comparing actual complete
components and first-return existence at caps4 and7. It also reconstructs all23
cap-seven minimum-board first-return witnesses. These tests accompany the
proof; they are not a replacement for its monotonicity and four-R arguments.
