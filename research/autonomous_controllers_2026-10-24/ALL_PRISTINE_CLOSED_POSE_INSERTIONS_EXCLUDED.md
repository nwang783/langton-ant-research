# No single pristine closed-pose insertion decorates the standard highway

24 October 2026. Author exact classification of one surgical construction family;
independent audit pending. No general controller or attraction theorem is claimed.

## The unbounded construction class being tested

Call a finite actual ant factor PRISTINE when the first read of EVERY physical
cell within that factor is WHITE. Unread BLACK cells outside its footprint may
exist and are not erased. A pristine same-pose excursion is nonempty and ends
at its initial POSITION AND HEADING. Its final root color may be either color.

Consider one standard104 turn period, and insert any such excursion once, at
any of its104 cuts. The intended alternative controller would repeat the enlarged
word forever. This is a genuine positive-output construction attempt: pristine
closed-pose excursions can emit BLACK cells while restoring the head pose.
They are not whole-state-neutral loops and not zero-output fronts.

**Claim.** Every word in this entire construction class has a complete
full-drift read class with consecutive identical turns. Consequently none can
repeat on ANY initial board, finite or infinite. In particular none gives a
nonstandard finite-seed regenerative controller.

The excursion need not be restricted in advance by length, width, number of
visits or output size. The proof derives the finite list from the already
certifiable blank orbit, not from a search cutoff. Prepared-input excursions,
heading-changing excursions, multiple inserted excursions, and changes to the
retained standard letters are outside the claim.

## 1. Pristine factors are actual blank prefixes

Translate and properly rotate the initial head pose to (0,0),N. Every first read
is WHITE by hypothesis; every later read is determined by the previous flips at
that same physical cell. Step-by-step induction therefore identifies the entire
factor with a prefix of the actual blank-board orbit. Arbitrary unread BLACK
fields elsewhere have no effect on this conclusion.

This equivalence does not say that a generic prepared connector is pristine,
or that a factor starting at a WHITE root has all other inputs WHITE.

## 2. Exact all-future exhaustion of blank same-pose returns

Literal blank replay reaches the complete715-cell BLACK field at time9977,
head(-15,10),W. Its next104 turns are exactly the retained standard word. The
retained exact periodic-tail checker verifies the WHOLE future from that full
state, with drift(-2,-2), using finite threshold tests for every phase and every
initial BLACK cell. It does not infer infinite repetition from observed repeats.

For every one of the104 absolute read positions q_i of that tail, the equation

    q_i + k*(-2,-2) = (0,0)

has no integer solution k>=0. Hence the blank ant never revisits the origin at
or after time9977, regardless of heading. Complete literal replay before that
certified tail therefore gives every positive return to the initial head pose:

    4,16,52,184,276,384,436,472,660,6168,6764,
    8048,8052,8056,8068.

All fifteen full words and full emitted BLACK fields are retained. Nine return
the root WHITE, at52,184,384,472,660,6168,8048,8056,8068. The other six return it
BLACK. Both types are included; requiring root-color restoration would omit
possible suppliers before a later standard L.

Thus there are exactly fifteen pristine same-pose words, not merely fifteen
found below a chosen duration cap. Their proper rotations have the same turn
words and cover all inserted headings.

## 3. Exact enlarged-period rejection

Let S be the retained standard word, U one of the fifteen words, and 0<=i<104.
The candidate is

    S[:i] + U + S[i:].

Since U restores its whole head pose, the enlarged period has the same full
drift as S. In the checker's N-normalized representation this is(-2,2). Its
length is104+|U|, not104, and that full length is used in chronology.

For every candidate the checker reconstructs ALL read positions, groups them
modulo the FULL drift d, writes q_t=r+k_t*d, and sorts each complete physical
history by t-P*k_t. The certificate supplies one complete class with a pair
of consecutive R/R or L/L reads for EACH of the15*104=1560 candidates.

Every read flips its cell, so consecutive identical turns at that same physical
cell are impossible for either starting color. All unread fields and possible
initial BLACK support are irrelevant to this contradiction rather than being
silently discarded. The failures are not just BLACK-first fuel requirements.
Cyclically recutting or properly rotating a candidate changes no physical
alternation condition, so it cannot evade the cover.

## Dependencies and exact files

Blank-tail algorithm:
../computability/periodic_tail_checker.py
SHA256 72f6736c6eb3f97b826b6c18a70ff93bbdda97619fa772a811854dcf85015804
../computability/check_rigid_reachability.py
SHA256 07af03b92d33d1508f5e28be11237f7a795464dec7c9d420cd00c65ce1147e5c
The certificate retains the exact standard.json hash, complete blank tail-entry
field, all104 no-return ray checks, every pristine output and every rejection.

certify_all_pristine_pose_insertions.py
SHA256 f981a923c6377a0d701e4c657236784d4cbecda634dd3684a62a7fe7be4a0642
all_pristine_pose_insertions_certificate.json
SHA256 bcce5fddcb550669c2af06d58cbb8054cbd49c6d83ced98b41ce4b3aa00e8260

This is a single-insertion theorem only. It does not make arbitrary output
components independent, prohibit prepared returns, or settle periodic uniqueness.
