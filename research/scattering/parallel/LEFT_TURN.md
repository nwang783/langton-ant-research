# A finite-support left-turn obstruction to clockwise scattering monotonicity

22 October 2026. This proves one specified pristine parallel interaction and its
finite-support transfer. The larger `discovery.json` table is exploratory only;
its cutoffs and sampled offsets are not a classification theorem.

## Exact result

Let C, W, d=(-2,-2), and H be the canonical 13-cell standard seed,104-letter
word, drift, and mature incoming-past field from `../transverse/PROOF.md`.
For W's read positions p_i, write H = XOR over i and j<0 of {p_i+j*d}.
Let R(x,y)=(y,-x) and v=(-40,-34). The infinite reference field is

    H XOR (v + R^2 H), with ant at0 heading west.

This is an opposed pair of canonical mature half-wakes, not two bilateral
settled lines. Both writer poses have the same invariant sector because the
relative heading is180degrees and v has even checkerboard parity.

The ant first deviates from W at update1,797. After5,201 recovery updates,
at time6,998, it is at(-19,-41), heading west, on an exact standard104tail
with drift(2,-2). Incoming drift was(-2,-2): this is a counterclockwise90degree
turn. Therefore the absence of counterclockwise turns in the clean transverse
crossing table does not extend even to pristine opposed half-wake ends.

## Complete finite inputs, not an infinite-fuel example

Define the finite M-period write packet

    H_M = XOR over0<=i<104 and -M<=j<0 of {p_i+j*d}.

For every integer k>=0 and M>=11, the completely finite seed

    B(k,M) = C union (k*d + v + R^2 H_M)

produces W^k followed by the reference trajectory, and then its standard
SE104tail. The two input parts are disjoint. Its capture time is104k+6,998
and capture pose is(-19,-41)+k*d, heading west. With M=11, this is exactly
165 black cells for every k. There is no changing external environment.

There is also an irregular complete135-cell finite kernel that produces the
reference trajectory exactly, obtained by retaining only initially black
cells that its entire infinite read future needs. The kernel is explicitly
listed in `left_turn_certificate.json`.

## Verification and reusable guard

Run `python certify_left_turn.py`. The checker:

1. Replays the entire reference word, checking every background read against
   the literal208-ray XOR definition independently of the optimized index.
2. Verifies every infinite tail read by exact line/ray interval parity.
3. Extracts all initial black cells needed by that complete infinite read
   future. Every intersection interval is bounded; the finite kernel then
   passes a second, finite-set simulator and the older exact tail oracle.
4. Checks the missing incoming-cap discrepancy against all finite reads and
   every infinite phase ray, using the exact per-class half-ray union for all
   k>=0 from the transverse finite-transfer lemma.
5. Checks every raw old-profile ray separately. No future read uses an old
   write epoch beyond10, so every M>=11 preserves every old-profile read.
6. Checks coordinate-sum disjointness uniformly, exact first-contact time shift,
   and replays the complete165-cell endpoint seed independently.

These are all-parameter future-read guards. The inference does not rely on
having simulated many large gaps or rail lengths. The current source and
result have been sent for independent scoped audit; they are not a proof of
arbitrary finite-seed capture, stability of disturbed parallel wakes, or any
complete collision graph.
