# The charged third-pass architecture exits through an exact 11-cell boundary trap

24 October 2026. AUTHOR all-future continuation and universal boundary criterion; independent review requested. The four preceding three-pass constructions have independent PASS report `../audits/check_three_positive_passes_independent.json` (069b66ba). This addendum does not yet carry that PASS.

## 1. A fixed spatial capture criterion, not a finite-repeat detector

Start the ant at (0,0), SOUTH. Let

    I={(-9,0),(-8,-1),(-7,-2),(-6,-2),(-5,-1),(-4,-2),
       (-4,-1),(-3,-2),(-3,0),(-2,1),(-1,1)}.

The literal fixed word C in `TERMINAL_TRAP_CERTIFICATE.json` has length278. On EXACTLY this eleven-black seed it is legal, ends at (−9,−5),S, and is followed forever by the retained canonical104 word H, with drift (2,−2). The 104-letter literal H is included in the certificate, so no guessed phase is used. All eleven initial cells are consumed during C. No priority or minimal-seed assertion is made.

Let G be the set of read positions of C and ONE subsequent copy of H whose y coordinate is at least−4. It has exactly63 cells. Its full list, eleven required black cells I, and52 required white cells G\I are recorded in `TERMINAL_TRAP_CHECKED.json`.

**Boundary-trap theorem.** The same C H^infinity executes from ANY initial black board B satisfying

    B is contained in {y>=−4},       B intersect G = I,

with head (0,0),S. B need not have bounded mass, bounded component sizes or bounded support in the half-plane. Proper rotations/translations of the entire statement are permitted. This is a sufficient capture condition, not a claim that arbitrary finite seeds reach it.

**Proof.** The exact source replay and periodic ray/parity test establish the proposed future on I. Every C read outside G has y<−4 by definition. The first H footprint lies at x∈[−9,−1], y∈[−9,−4]; its y>=−4 part is already in G. Every H copy with epoch k>=1 has y<=−6 because the drift is (2,−2). Therefore EVERY future read outside G lies in the required initially white half-plane. The initial fields I and B agree on the ENTIRE future read set. Ordinary first-difference induction then keeps all later flips, turns and poses identical forever. No old component is erased in this argument: the rest of B is literally never read. QED.

The infinite periodic test is exact, not “several matching periods.” For phase i and epoch k, the read cell is q_i+k d. Earlier same-cell visits are the finite phase-pair translation thresholds, while the initial board contributes only at its exact nonnegative ray intersections. Between successive thresholds the required parity is constant. The checker tests every threshold and the final constant interval for all104 phases.

## 2. All FOUR complete third-pass endpoints satisfy this criterion

For q=3,5,7,9 normalize the actual third endpoint to (0,0),S by translation and, for q=5,9, a half-turn. On EACH complete board:

- every black cell has normalized y>=−4;
- its exact63-cell guard is I;
- the same fixed278-turn C executes, then the exact H tail continues forever.

The resulting certified standard-tail times FROM THE ORIGINAL enlarged seeds are respectively1357,2599,4321,6523. These are sufficient canonical tail-start times, not asserted minimal. Their actual tail poses are:

- q3: (−29,−32),S, drift(2,−2);
- q5: (54,33),N, drift(−2,2);
- q7: (−53,−56),S, drift(2,−2);
- q9: (78,57),N, drift(−2,2).

The source replay first found the identical486-turn continuation after observing two extra canonical periods; the proof removes those208 redundant steps and verifies the278-turn entry directly. No claim is based on those observed repeats.

## 3. Exact failure to regenerate, over the WHOLE actual future

At each third endpoint the ONLY currently black cells that are ever read again are the transformed eleven cells I. The other339,713,1231,1893 black cells, respectively, remain on the complete board and are never read again. This is an all-future read-set exclusion, not a component cutoff.

In particular ALL101,231,409,635 third-pass R lifetimes remain black and are NEVER consumed in the future. None of that newly written gain-bearing output is recycled into a fourth ordinary pass. The q−1 missing direct next stitches are not merely currently white: their cells are outside G in the permitted upper half-plane, are NEVER read, and therefore remain white forever. No guide or stitch repair occurs later on these exact unmodified boards.

Of the five retained second-R boundary lifetimes, exactly TWO lie in I and are consumed by C. The other THREE remain unread forever. The complete lists are recorded. The three surviving old added-cycle lifetimes all lie in I; they too are consumed during C, rather than being quietly ignored or mistaken for a rebuilt return guide.

This identifies a genuine spatial termination mechanism for the charged architecture: after its third pass, the continuing head sees a fixed exterior boundary patch and then enters a virgin half-plane. The large distributed positive output behind it is inaccessible along its actual future, despite being fully retained.

## 4. Scope of the all-parameter question

The boundary-trap theorem itself is unbounded and analytic. The claim that the supplied odd-q construction REACHES that boundary has been proved only for the FOUR literal seeds so far. The original two-pass author's all-q statement was itself not yet a signed premise, and the new guide generator uses a repeated local smoothing operation; neither may be silently generalized from the displayed formulas.

The existing Presburger read-set machinery is relevant, but its published fixed-number-of-affine-arms interface does not directly certify this family: q controls an unbounded number of spiral runs, and absolute stage times are quadratic in q. A concrete route around the clock issue is to express each ordinary pass as injective, disjoint old-L and new-R read masks; whole-stage XOR then replaces absolute within-stage clock formulas. The remaining necessary implementation is a finite symbolic corner/straight-role decomposition of BOTH guide smoothing operations and the actual second/third output rods, with all-q separation and endpoint guards. No such all-q computation has been executed or reported PASS here.

Thus the current conclusion is exact: these four charged THREE-pass designs all capture; an arbitrary archive satisfying the stated63-cell/pristine-half-plane boundary also captures; global finite-seed attraction and an all-odd-q construction/capture theorem remain open.
