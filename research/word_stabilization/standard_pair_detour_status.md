# Standard motion can reconnect after one adjacent bad pair

This is a negative control for a possible overstrong extension, not a new
counterexample to the highway conjecture.

The exact finite enumeration fixes150 initial standard104 turns, then exactly
two bad ten-windows at ending indices150 and151, then149 good-window updates.
Among117 feasible301-turn survivors,13 have final histories that can reach
the standard104 cycle through the legal150-word graph. All13 bridges are
literally physically feasible, and all13 can be completed by finitely many
unread initial black cells to exact infinite standard tails. The completion
uses the previously independently checked infinite periodic-word verifier,
not a long finite simulation.

Every example begins in canonical standard phase8, leaves at phase54 by L
instead of the standard R, and has entry mass between30 and44. The13 controls
include24-turn inserted-run patterns. Their certified full finite seeds,
finite words, tail periods and final poses are stored in
standard_pair_detour_certificates.json; certify_standard_pair_detours.py
replays their finite words and invokes the exact infinite-tail test.

The finite enumeration is deliberately scoped: it fixes a150-turn standard
prefix immediately before the pair. There are two outgoing ten-legal edges
from the standard149-history cycle, so this does NOT classify every possible
standard-to-standard excursion with an arbitrary legal prelude. Nor are the
13 controls asserted to classify arbitrary-length post-pair legal bridges.
The observed24-turn pattern has not yet received an all-parameter proof.

Thus an isolated adjacent pair CAN reconnect standard motion, even with no
later bad windows. A larger defect-language proof must account for these
finite-fuel scattering events rather than forbid them outright.
