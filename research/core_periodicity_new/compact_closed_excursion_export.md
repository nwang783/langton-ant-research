# A closed-pose excursion cannot export only a remote compact patch

Status: independently analytically audited on2026-10-22 at21:36 UTC as a corollary of the previously audited integer-clock family. No claim of novelty outside this project.

## Theorem

Consider any feasible finite trajectory interval of length t>0, from a board B to a board C, with IDENTICAL initial and final physical pose(p,h). The backgrounds may be finite or infinite, as justified below. Let A=B symmetric_difference C be its complete odd-read mask, and k=|A|. The mask is nonempty, since an exact finite-state cycle is impossible.

For each diagonal sign define

    w_plus  = max_{q in A}(q_x+q_y)-min_{q in A}(q_x+q_y),
    w_minus = max_{q in A}(q_x-q_y)-min_{q in A}(q_x-q_y).

Then

    t <= k * [3^ceil(min(w_plus,w_minus)/2)-1].                 (1)

In addition, every changed cell q belongs to the physical excursion and therefore

    2 ||q-p||_1 <= t.                                         (2)

In particular, fixing the shape diameter of the COMPLETE XOR mask bounds the excursion duration and the distance of that mask from the port, independently of the initial board mass, all unchanged archival history, and the location where one hoped to place the changed patch.

## Proof

Import the full-state integer clock Theta_c from

    ../sources/kehao95-core/clock_escape/PROOF.md, Section1.

With chi(q)=(-1)^(q_x+q_y), invariant sector sign sigma, f(s)=3^|s|-1, and the stated head correction J, it is

    Theta_c(B,p,h) = -sigma sum_{q in B} chi(q) f(q_x+q_y-c)
                     + J(p_x+p_y-c, epsilon(h)).

Every physical update increases Theta_c by at least1, for EVERY integer c. Since the endpoint poses agree, their head corrections cancel exactly. All unchanged board cells cancel too. Choose c to be an integer nearest the midpoint of the minimum and maximum q_x+q_y over A. Then |q_x+q_y-c|<=ceil(w_plus/2) for all q in A. Consequently

    t <= Theta_c(C,p,h)-Theta_c(B,p,h)
      <= sum_{q in A} f(q_x+q_y-c)
      <= k*[3^ceil(w_plus/2)-1].

Applying the same clock after a quarter-turn rotation gives the identical bound with w_minus. Taking the smaller proves(1). Every q in A is read an odd positive number of times, so it is visited. The path goes from p to q and back to p, requiring at least2||q-p||_1 unit moves. This proves(2).

The argument also handles A empty directly: then the clock difference is zero, contradicting t>0. Thus no separate recurrence theorem is required.

For arbitrary infinite entry backgrounds, copy the entry colors on the finitely many cells visited in this interval into an otherwise white finite board. The entire interval, endpoint poses, and COMPLETE XOR mask are unchanged. Applying the finite-board proof to this copied interval proves the same inequalities. In particular, exact full-state returns are forbidden on arbitrary backgrounds too. This finite-interval transfer does not assert that the same finite copied seed reproduces an infinite trajectory.

## Compact moving-cap obstruction

Suppose a purported fixed-port renewable builder restores its entire old bulk after each excursion, while changing only a finite cap and new debris inside a translate of one fixed bounded set. The cap's internal state may vary or be aperiodic; no finite-state cap assumption is needed. The full XOR mask A of each excursion lies in that translated bounded set. Its k and both diagonal widths are uniformly bounded, so(1)-(2) force every changed cap to stay within a uniform distance of the port.

Therefore such a builder cannot move its active right endpoint indefinitely outward while restoring all bulk exactly. It must instead leave changes whose COMPLETE spatial extent is unbounded, retain changes near the port as well as the remote endpoint, or fail to return to the identical pose.

For a fixed finite cycle of port poses, the same obstruction applies after composing the cycle whenever all changes during that cycle are confined to one uniformly bounded moving neighborhood. A cycle with spatially separated changed patches is NOT covered by that compact-neighborhood hypothesis.

## Infinite-return corollary

If an infinite finite-seed trajectory returns to one fixed physical pose infinitely often, the diameters of the COMPLETE XOR masks between successive such returns cannot be uniformly bounded.

Indeed, bounded mask diameter bounds k by the number of lattice sites in a bounded box, then(1) bounds every return interval's length. Every interval and all its changed cells remain in a uniformly bounded neighborhood of the fixed pose. No other cells are ever read after the first return. This would be an infinite trajectory confined to a finite region, contradicting strict clock growth there.

This does not prove transience. A recurrent counterexample could make increasingly distributed changes during its excursions. Nor does it exclude a builder that changes both a near-port controller and a far cap, even if each patch separately has bounded size: their UNION has unbounded diameter, and its exponential clock capacity can grow.

## Finite-controller pumping corollary

Consider ONE actual uninterrupted infinite physical trajectory and strictly increasing checkpoint times t_n. There are no external resets, teleports, or unrecorded controller updates. Assume:

1. Every checkpoint pose belongs to a fixed finite set P.
2. There is a fixed finite controller cell set C and a fixed finite window W such that the COMPLETE board XOR between checkpoints n and n+1 is contained in

       C union (q_n+W).

3. The window centers q_n belong to Z^2 and have uniformly bounded increments (take the upper bound v to be a nonnegative integer):

       ||q_{n+1}-q_n||_infinity <= v.

Then NO such infinite checkpoint sequence exists. The proof first forces the centers q_n to be uniformly bounded and then obtains an exact full-state recurrence. In particular, these hypotheses cannot describe an indefinitely expanding ONE-ended counterexample with a bounded controller, even if the controller changes state, chooses aperiodic actions, and the moving endpoint deposits permanent debris.

Proof. Put N=|P|*2^|C|. Among any N+1 consecutive checkpoints, two have identical pose and identical board restriction to C. Between those two checkpoints, the controller XOR cancels completely. The remaining XOR lies in the union of at most N windows q_j+W. If W is contained in [-r,r]^2 for a nonnegative integer r, this union is contained in q_n+[-L,L]^2, where L=r+Nv and n is the first checkpoint of the chosen block. Its size is at most K=(2L+1)^2 and both diagonal widths are at most4L. The identical-pose theorem therefore bounds the elapsed physical time by

       T_* = K*(3^(2L)-1),

independent of n and q_n. The complete XOR cannot be empty, because that would be an exact finite-state recurrence. Thus some changed cell is visited, and it is within L of q_n. If R_P=max_{(p,h) in P}||p||_infinity, the round-trip bound gives

       ||q_n||_infinity <= R_P+L+T_*/2.

This holds for every starting block n and uniformly bounds all q_n. Hence all net checkpoint changes lie in one fixed finite set C union union_n(q_n+W). Outside that set, the complete board is frozen at checkpoint times. There are only finitely many checkpoint poses and binary configurations inside the finite set, so two COMPLETE checkpoint states repeat. Strict clock growth forbids that. Thus the assumed infinite checkpoint sequence cannot exist. QED.

The bounded-increment hypothesis matters: without it, the finitely many windows between a repeated controller state could already be arbitrarily far apart. The full-XOR hypothesis also matters: temporary work is unrestricted, but every lasting change outside C must be included in the moving window. A two-growing-end builder changes two widely separated windows and is not excluded. Nor is a general Turing simulation whose physical head does not return to a bounded port set, or whose macro-step leaves spatially distributed writes.


This final strengthening was pointed out by the independent auditor at21:37 UTC. It also gives a computable architecture-dependent bound on the number of checkpoints. For a finite valid sequence with at least N intervals, put Q=ceil(R_P+L+T_*/2). The displayed bound controls q_n whenever N intervals remain after n. The final at most N-1 window centers are therefore bounded by Q_prime=Q+Nv. Thus every checkpoint change lies in a set of size at most |C|+(2(Q_prime+r)+1)^2, and there are at most |P| times2 to that power distinct complete checkpoint states. Sequences with fewer than N intervals have at most N checkpoints. This final-window enlargement was pointed out by the computability analysis. Frozen exterior history need not be bounded or discarded; it is identical at all checkpoints and cancels in every comparison.

The finite-controller theorem also holds on arbitrary infinite backgrounds. Every finite identical-pose interval satisfies the transferred export bound, and an exact complete-state recurrence would contradict the same bound with empty XOR. No globally finite black mass is used in the pumping argument.


## Bounded-write diagonal-corridor corollary

This variant removes the bounded-increment hypothesis and allows arbitrarily many spatially separated write sites, provided their total number of changed cells per checkpoint is bounded and they remain in one FIXED diagonal corridor.

Assume actual uninterrupted checkpoints have poses in a fixed finite P, with a fixed finite controller C. Suppose each checkpoint-to-checkpoint complete XOR outside C contains at most k cells, all lying in a fixed strip

    a <= x+y <= a+w

of integer width w>=0. The rotated x-y version is identical. There is NO assumption on longitudinal distances between changed cells or on their movement between checkpoints. Then an infinite such checkpoint sequence is impossible, on any initial background.

Proof, using the computability analysis's direct clock argument. Choose c to be an integer nearest a+w/2 and fix this SAME clock throughout. Let

    F = 3^ceil(w/2)-1,
    C_* = sum_{q in C} f(q_x+q_y-c),
    H_* = max_{(p,h) in P} J(p_x+p_y-c,epsilon(h))
          - min_{(p,h) in P} J(p_x+p_y-c,epsilon(h)).

For every checkpoint interval, the remote XOR contributes at most kF to the clock difference, controller changes at most C_*, and the endpoint head correction at most H_*. Hence each interval's physical duration is at most

    kF + C_* + H_*.

The same estimate holds for infinite backgrounds by copying the finite visited region. Since all intervals start from the finite pose set P, every later read is confined to a fixed finite neighborhood of P. Only finitely many cells can ever change; exact complete-state recurrence follows, contradicting strict clock growth. QED.

In particular, two or finitely many remote endpoint patches moving arbitrarily far apart along one fixed-width NE/SW or NW/SE corridor do NOT escape the obstruction if their total changed-cell count stays bounded. Axial two-ended builders are not covered, because both diagonal widths grow with their separation. A strip that translates in its normal direction is also outside this fixed-strip theorem.
