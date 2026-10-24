# Seven-word marker return bridge and a finite D-return obstruction

Status: author literal reconstruction complete; independent audit requested.
Scope: the seven supplied raw words D, C, V, U, F, Q, B and actual ordinary Langton dynamics on a complete finite black board. No identification of a finite physical control with an original 150-history quotient class is asserted.

## 1. The actual shared section

The frozen 214-class, 993-edge quotient supplies D10, C15, V18, U28, F56, Q64 and B74. Every actual word boundary has the common 11-turn marker M = LLLLRLRRRRL. For D, its raw ten turns do not themselves contain the complete marker: the first L of its successor completes M, and the next L completes its 12-turn start marker. Every supplied successor begins LL. For the other six words, their raw prefix already contains M.

Literal first-read reconstruction of M gives exactly the five forced black cells
K = {(-1,-1), (-1,0), (0,-1), (0,0), (1,0)}.
For each of the seven words W, the physically supplied turn stream W M has M occurrences exactly at offsets 0 and |W|. Its raw endpoint board contains the translated and rotated K required at the next boundary. Thus the common core is a checked property of the actual marker, not a shared-core convention imported from another parser.

The normalized raw endpoints and total black-mass gains are:
D: (1,1,N), 0;
C: (0,1,W), +3;
V: (1,3,N), +4;
U: (0,4,N), +4;
F: (-4,-2,S), +2;
Q: (-4,-4,S), +6;
B: (-3,-5,S), +6.

In particular F, Q and B are indivisible first returns to this marker section. None has an internal M reset. They rotate the heading by two quarters without any literal C word. A return abstraction that retains the eight-language literal-C heading clock is therefore not justified.

## 2. What signed no-D fuel does give between D returns

Use the independently signed no-D theorem on C,V,U,F,Q,B. In an actual continuing seven-word trajectory, let consecutive D entries have total finite entry mass m. The first D has zero mass gain. The intervening no-D word X has at most four leading C words. Remove them; their total cost is at most 60 raw turns and their mass gain at most 12. Any nonempty remainder starts with a non-C word and has its actual right marker supplied by the following D and its successor context. The signed marked-fuel theorem therefore gives

raw duration from the first D entry to the next D entry <= 33m + 334,
next D-entry mass <= 8m + 68.

If X is empty or consists only of the at most four C words, the same conservative bounds hold directly. These are local finite-return bounds, not a decreasing return potential. They also imply that an infinite finite-support seven-word trajectory, if one exists, must meet D infinitely often. The freshness certificate is reset relative to each no-D factor and cannot be summed across D returns without a new argument.

Marker ownership matters: the no-D target context includes M, while each earlier source/reader owns only its raw word. The D following X supplies the first ten turns of that M, not an extra no-D packet or an extra disjoint resource.

## 3. One explicit physical obstruction to naive monotonicity

The attached checker derives a 23-black-cell finite seed, with all unspecified cells white, and replays D V F D followed by the actual M marker under the ordinary rule. At the raw word cuts:

D at turn 0: head (0,0,N), mass 23;
V at turn 10: head (1,1,N), mass 23;
F at turn 28: head (2,4,N), mass 27;
D at turn 84: head (-2,2,S), mass 29.

The D-to-next-D return D V F therefore has 84 raw turns, displacement (-2,2), a heading flip, zero literal C words, and mass gain 6. The final D ends at turn 94 with mass 29; the appended actual M is also physically replayed, for 105 checked turns in total. The M occurrences are exactly 0, 10, 28, 84 and 94. At every raw cut, the actual active five-cell core is black and all supplied 12-turn start markers and 11-turn end markers match the replay.

Separately, the frozen 214-class quotient has 77 paths labelled D V F D; one is class path 8,75,163,2,3. This is only graph-label compatibility. It does not certify that the 23-cell seed realizes this particular history-class path, nor that the short path extends indefinitely in the original component.

Consequently neither decreasing D-entry black mass nor a literal-C-only return-heading clock can justify the desired seven-word extension. This finite control does NOT refute seven-word termination, a richer complete-resource return potential, or the independently signed retained-eight theorem. It is a precise obstruction to those two shortcuts.

## 4. Reproduction and limitations

Run check_marker_and_D_return.py. It inspects exactly the seven supplied words and the single explicitly prescribed D V F D control, with its right marker. It does not enumerate actual prefixes or claim new long-path caps. The JSON records the full finite seed and end board, all cut poses/masses/cores, literal residuals, exact marker occurrences, quotient path count and dependency hashes.

The remaining seven-word problem is a genuinely global return-budget problem: the return section is valid, but the complete finite board, marker context and ancestry/resource history must be carried across returns. Neither previously proved sublanguage finiteness nor finite local return bounds alone pay for arbitrarily many returns.
