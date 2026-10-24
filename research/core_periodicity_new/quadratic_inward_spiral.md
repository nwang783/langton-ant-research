# A quadratic-length two-visit inward spiral

Status: independently analytically audited and independently literally replayed on 2026-10-22 at 22:02 UTC. Audit artifacts: ../audits/check_quadratic_spiral_independent.py/json. This is a finite sharpness construction, not an infinite counterexample.

## The family

Set S=RLLR. For an integer n>=1, start at (0,0), heading N, and prescribe

    W_n = product over j=n,n-1,...,1 of
          S^j L S^j RLL S^j L S^j L.

There exists a finite entry seed of exactly

    m_n = 11n+2

black cells realizing this word. Its length and final pose are

    t_n = 8n^2+14n,
    p_final=(-n,n), h_final=N.

No physical cell is read more than twice. The entry seed is the unique minimal seed: make precisely the first-L read sites black, and every other site white. Its final black mass is 7n+2.

Thus the audited universal quadratic bound on two-visit lifetime has the correct exponent. No uniform linear bound in initial black mass is possible.

## Exact geometry of a circuit

Index circuits by k=0,...,n-1 and put j=n-k and T=2n-k. Circuit k starts at (-k,k), heading N. The following table specifies EVERY read site and letter. Integer intervals include both endpoints.

1. North S^j rail:
   - R at x=-k, y in [k,T-1].
   - L at x=1-k, y in [k,T-1].
2. Standalone L at A_k=(-k,T).
3. West S^j rail:
   - R at y=T, x in [-2n+k,-k-1].
   - L at y=T+1, x in [-2n+k,-k-1].
4. The asymmetric RLL corner:
   - R at B_k=(-2n+k-1,T).
   - L at B_k+(0,1).
   - L at B_k+(-1,1).
5. South S^j rail:
   - R at x=-2n+k-2, y in [k+1,T].
   - L at x=-2n+k-3, y in [k+1,T].
6. Standalone L at C_k=(-2n+k-2,k).
7. East S^j rail:
   - R at y=k, x in [-2n+k-1,-k-2].
   - L at y=k-1, x in [-2n+k-1,-k-2].
8. Standalone L at D_k=(-k-1,k).

The final move arrives at (-k-1,k+1), heading N, exactly the next circuit's entry. These formulas follow directly from the four unit read positions of S and its quarter-turn rotations. In particular, every circuit is self-avoiding: the eight sets above are pairwise disjoint.

## Complete chronological overlap proof

Circuit k lies in the rectangle

    [-2n+k-3, 1-k] x [k-1, 2n-k+1].

Every one of its read sites lies within one lattice unit of that rectangle's boundary. Circuit k+2 and every later circuit lie in the rectangle obtained by moving every boundary inward by at least two. Therefore circuits whose indices differ by at least two have DISJOINT complete read sets.

The overlap of circuit k with circuit k+1 consists exactly of:

- The four shorter L-input rails of circuit k+1. Each is the corresponding R-output rail of circuit k with its two endpoint cells removed.
- The first L in the RLL corner of circuit k+1. Its site is (-2n+k,2n-k), which was the leftmost R-output of circuit k's west rail.
- The second L in that corner. Its site is (-2n+k-1,2n-k), which was the R at B_k.

Every overlap is therefore an R read in the earlier circuit followed by an L read in the later circuit. There are no other overlaps, no third reads, and no repeated equal letters at any cell. This proves physical feasibility from the first-L seed, retaining ALL cell history rather than just a rail snapshot.

The number of twice-read cells is

    sum_{j=2}^n [8(j-1)+2] = 4n^2-2n-2.

There are 18n+4 singly-read cells and 4n^2+16n+2 distinct read cells in total.

## Exact initial fuel and final mass

The first circuit has 8n L reads on its four S rails, two L reads at its RLL corner, and three standalone L reads. Hence it needs 8n+5 initial black cells.

For every later circuit, ALL rail L reads and BOTH RLL-corner L reads are supplied by R outputs of the immediately preceding circuit. Its only new first-L sites are A_k, C_k, and D_k. These sites are not read earlier, by the overlap analysis. Thus

    m_n = (8n+5)+3(n-1) = 11n+2.

Every S has net mass change zero. The three standalone Ls contribute -3 and RLL contributes -1, so each circuit loses exactly four black cells. The final mass is consequently m_n-4n=7n+2.

The four S^j blocks and six corner letters give 16j+6 turns in circuit j. Summing proves t_n=8n^2+14n.

## Exact endpoint field for interface reuse

Relative to the final head cell (-n,n), the complete final black field is

    P union union_{j=2}^n A_j,

where

    P = {(1,-1),(1,0),(-1,1),(0,1),(-3,0),(-3,1),
         (-2,-1),(-1,-1),(-2,1)},

    A_j = {(j,-j),(j,j-1),(j-1,j),(-j-2,1-j),
           (-j-2,j),(-j-1,-j),(j-2,-j)}.

All these sets are disjoint. For each nonfinal circuit, the unused R outputs are the two endpoints of the north rail, the right endpoint of the west rail, both endpoints of the south rail, and both endpoints of the east rail. Its west left endpoint and RLL-corner R are used as the next cap's Ls. These seven survivors give A_j. The final circuit leaves all nine of its R reads black, giving P. This establishes the complete field, not merely an interface snapshot.

The output is seven diagonal arms plus a fixed cap, whereas the initial fuel consists of the first outer rail inputs and three inward corner diagonals. No renewable transformation of this output back to the required larger input is claimed.

## Quadratic many adjacent bad-ten events

Let F be the 84 cyclic ten-factors of the pinned canonical standard104 word, and let J(t) indicate that the ten-turn word ending at t is not in F. Define K(t)=J(t-1)J(t), using the true physical history.

All four cyclic ten-factors of S^infinity are outside F. In any S^j block, every eleven-turn factor wholly contained in the block therefore ends at a K event. A block contributes at least max(4j-10,0) such events; these indices are distinct across blocks and their history lies entirely inside the prescribed trajectory. Hence, for n>=2,

    number of K events in W_n >= 4 sum_{j=3}^n (4j-10)
                              = 8(n-2)^2.

For n=1 use the trivial lower bound zero. In particular, along m=11n+2, the total K count is Omega(m^2), even before the first third read.

This does NOT produce unbounded K count at one fixed mass and does not contradict eventual standard104 capture. In fact the unmodified seed is now proved to capture, as recorded below. It is a necessary negative control for any proposed linear-in-mass K rank or linear two-visit lifetime theorem.

## Reproduction

check_quadratic_inward_spiral.py constructs the first-L seed from the literal word, independently replays the physical rule, verifies every predicted read site and adjacent overlap, and binds the four S ten-factors to the canonical W104 hash. The general-n proof is the coordinate argument above; finitely many replays are only error controls.

## Certified-capturing completion

The independently audited four-cell completion port can be placed outside every cell of this protected finite prefix. It adds exactly four disjoint initial black cells and guarantees an eventual standard104 tail without altering W_n. Thus there are CERTIFIED-CAPTURING seeds of mass exactly11n+6 with at least8(n-2)^2 K events. See ../computability/quadratic_capturing_defect_lower_bound.md and ../computability/finite_prefix_density.md. This strengthens the event-count lower bound without claiming any fixed-mass unboundedness.

## Unmodified seed captures: independently audited continuation

The separate exact all-parameter continuation in ../causal_reduction/spiral_endpoint/README.md proves that for every n>=11, the normalized endpoint above follows

    (RL)^n P V^(n-9) C W^n D H^infinity,

where P,V,C,W,D have fixed lengths1540,10,22,10,1549 and H is a cyclic standard104 phase. Here these literal labels belong to that continuation certificate; they are not the earlier seven-word symbolic language. Its full affine-history and infinite-tail audit is in ../audits/check_spiral_affine_continuation_independent.py/json. Consequently the ORIGINAL seed of mass11n+2 captures by time

    8n^2+36n+3021.

No four-cell completion is needed for this family. The proof retains the entire seven-arm field and all subsequent writes. The same original seeds therefore combine an explicit standard tail with at least8(n-2)^2 actual K events. Their coordinates are O(n), so explicit binary-list input length is O(n log n). This improves the generic completed-family constants, not the lower-bound exponent or the distinction from fixed-mass unboundedness.
