# C-free joint freshness and finite-fuel theorem

Status: independently analytically audited and reproduced by a separate
current-color transfer implementation rebuilt from literal macro words.
All 29 final closures pass, with state counts matching target by target.
See `../audits/check_cfree_kernel_independent.py` and
`../audits/cfree_kernel_independent.json`.

## Theorem and consequence

For every physically feasible finite word over U,V,Q,B, the following
marked first-L inputs are unread earlier within the word (all coordinates
are in the marked macro's north-facing entry frame):

U: (-1,0), (-1,2), (-1,1), (0,3).
V: (1,2).
Q: (-1,0), (-2,2), (-3,2), (-3,3), (-5,2), (-5,1), (-4,0),
   (-3,-1), (-2,-1), (-4,-1), (-4,-3).
B: (-1,0), (-2,2), (-3,2), (-3,3), (-5,2), (-5,1), (-4,0),
   (-3,-1), (-2,-1), (-4,-1), (-2,-3), (-2,-2), (-3,-4).

There are 4,1,11,13 sites respectively, 29 in total.

Consequently, if a nonempty such word with u,v,q,b macro counts is realized
from a complete finite board with m black cells, then

    4 + 4u + v + 11q + 13b <= m.

In particular its number of macros is at most m-4, and no finite-support
trajectory can have an infinite C-free tail over these four macros.

The four extra cells are the first macro's seam first-L inputs
{(0,0),(-1,-1),(0,-1),(1,0)}. They are distinct from the first macro's marked
set. No later marked cell can equal them, by freshness. Every marked cell
and these four initial seam cells must already be black at interval entry.
No claim is made about pre-interval history or a word containing C.

## Simultaneous least-counterexample argument

Fix exactly the same 29-site family S throughout this argument. Suppose a
feasible word has a reused S-input, and select its first macro with any
such reuse. Choose one reused input q in that macro. Its first read there
is L, so its last earlier read must be R. Trim the word to the start of
the macro containing that last R. All intervening macros avoid q.

Every macro strictly before the target macro has all its S-inputs globally
unread at its entry. This follows from the choice of the first offending
macro, not from an inductive assumption about only one target type.

Normalize the target macro's entry heading to N and position to (0,0).
Every C-free macro preserves heading or reverses it, so all headings are
N/S. Every literal endpoint displacement has coordinate sum divisible by
4, also after a half-turn. Hence every macro entry satisfies x+y=0 mod4.

For each of the 29 target types, the finite checker overapproximates every
such last-R-to-target suffix. It records the last read letter and whether
each cell has been read in the 5x5 patch around q. Unknown cells are not
assigned an initial color. Any read of a known cell must alternate with
its stored last letter; its letter then becomes the stored last letter.

All macro poses that can read the patch are enumerated exactly by inverse
read occurrence equations, restricted to N/S and x+y=0 mod4. Every other
pose is represented by OUT. OUT preserves patch information and may reenter
at any sensitive pose having an outside predecessor under some macro.
This deliberately allows arbitrary outside excursions and is conservative.

Initialization includes every sensitive source macro whose last read of q
is R. Its post-macro patch read letters are fixed only on cells it reads;
all others remain unknown. The source macro is not constrained by the
freshness hypothesis, a safe enlargement.

For an intermediate macro, reject if it reads q. Also reject if any of
its S-inputs was already read in the retained patch before the macro. This
is necessary for its true globally fresh S-inputs. Inputs outside the patch
are ignored, another safe enlargement. The goal macro bypasses ALL these
freshness guards; only its literal patch read alternation is tested.

Every exact first-counterexample suffix therefore gives a path in the
corresponding finite graph. The complete finite closures exclude every
one of the 29 target types. This contradicts the chosen first offending
macro and proves all 29 freshness statements simultaneously.

## Discovery versus final proof

The discovery started from all 40 non-seam first-L sites. Unproved targets
were deleted, including targets with abstract witnesses or capped searches.
This deletion is only a method for finding S; it is not a proof step.

Only the final stable round matters: the guards use the same 29 sites that
are all conclusively excluded. No final check hit its state cap.
Final closures have 476,218 states for odd coordinate sum and 131,896 for
sum0 mod4. No surviving site has sum2 mod4.

After translating q to the origin, the q-free intermediate closure depends
only on q's residue class modulo4, while the particular macro/site is a
final goal query. Thus shared residue-class closures can replace 29
redundant runs without changing the mathematical certificate.

Artifacts:
- cfree_first_reuse_patch.py: exact finite-patch overapproximation.
- cfree_kernel_current_marks.json: the final 29-site family.
- cfree_kernel_rounds.json: complete final target outcomes and discovery.
- cfree_inductive_kernel.py and .log: reproducible discovery routine.

Do not confuse the earlier 122,258-state V-tip check under a larger assumed
family with the final stable certificate. The latter is the one required
by the simultaneous least-counterexample proof.
