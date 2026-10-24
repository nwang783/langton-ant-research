# Paired-arm endpoint resets: exact local model, not an autonomous construction

Status: analytic reduction and literal discovery implementation, 22 October 2026.
The earlier swept-front certificate and modular column filter were independently
audited; the particular reset implementation below has not yet been independently
audited. No renewable endpoint cycle or finite-seed counterexample is known.

Use N,E,S,W = 0,1,2,3, with north increasing y. Let

    S = RLLR,
    W = LLRLRRRRLRRRRLLLLRLL,
    rev(w) = complement(reverse(w)).

S from an E pose drifts (2,0). W from an E pose drifts (-2,0).
The reverse words are cyclic phases of the same literals: rev(S) is shift2
of S, and rev(W) is shift6 of W. This observation alone supplies no cap.

## 1. The two ideal resets

For n>=10, consider either finite paired history:

* From (0,0,E), W^n goes to (-2n,0,E). An EXTERNAL, OMITTED
  turnaround changes the pose to (-2n,0,W). Then rev(W)^(n-3)
  goes to (-6,0,W).
* From (0,0,W), rev(S)^n goes to (-2n,0,W). An EXTERNAL, OMITTED
  turnaround changes the pose to (-2n,0,E). Then S^(n-3)
  goes to (-6,0,E).

No assertion is made that changing this heading is itself an ant operation.
A future complete construction must replace it with a legal finite left cap
and retain all its colors, phases, and interactions. Here only the RIGHT end
of these histories is used as a local comparison.

Each word has bounded horizontal footprint. Consequently every history at
x>=-12 is independent of n once n>=10. Away from both ends, the histories
are also independent of horizontal parity and are exactly:

    W pair: row0 LR; row1 RLRLRLRL; row2 RLRLRLRL; row3 RL.
    S pair: row0 LR; row-1 RL.

Thus the middle bulk restores its initial colors, requiring only a solid
black row0 and white other touched rows. This is an all-n calculation: a
middle site's contributing copies are obtained by solving x=p_i-2k for
its finitely many literal phase positions p_i; there is no extrapolation
from a long simulation. The leftmost O(1) fringe is deliberately excluded.
The right fringe has the following full guards, on the whole ideal left
half-arm, and finite XOR updates.

W guard:
- row0: x<=-2 and x=0 black; x=-1 is unread.
- row1: x<=0, with only x=0 black.
- row2: x<=-1, with only x=-1 black.
- row3: x<=-1 all white.

W flip set:
(-6,0),(-6,2),(-5,1),(-5,3),(-4,0),(-4,3),(-3,0),(-3,3),
(-2,0),(-2,3),(-1,2),(-1,3),(0,0),(0,1).

S guard: row0 x<=0 black; row-1 x<=0 white.
S flip set: every (x,y) with -6<=x<=0 and y in {-1,0}.

Each reset therefore flips fourteen cells, preserves total black mass on its
guard, moves x by -6 and reverses heading. The code keeps guard coordinates
x>=-12 explicitly and checks the uniform far-left part separately.

## 2. The current exact ideal endpoint dynamics

Take black half-rows y=0,U, x<0, with even U>=4, and a finite XOR defect field.
Start at (0,0,E). Perform ordinary ant steps except that, whenever the full
translated guard of one of the preceding resets holds at y=0 or U, replace
the outgoing/incoming pair by its finite reset map. The base-row intersection
check forbids a reset from crossing the other black half-row.

This is a precisely defined HYBRID SYSTEM on an infinite rail background,
not the original autonomous ant on a finite seed. A positive translation cycle
of its complete field and pose would certify a renewable right endpoint.
It would still need finite-arm gluing and legal left-end/port construction.

The complete-state cycle key is obtained by changing the half-row cutoff
from x=0 to the current head x, then translating every finite defect by -x.
No remote debris is discarded. Hence equality of keys really means equality
of the whole infinite field up to horizontal translation. It is not merely
a repeated local pose or bounded-window pattern.

## 3. A modular necessary condition on any endpoint cycle

In this sector, every reset at a base row has even x. Apply the exact
alternating-row charges modulo4. Ordinary ant steps conserve them. A W reset
at height Y has charge anomaly

    -e_Y + 2e_(Y+1) + 2e_(Y+2) - e_(Y+3)  (mod4),

whereas an S reset has anomaly e_(Y-1)+e_Y. These follow directly from the
fourteen guarded flips and the heading correction. They describe the omitted
far-left contribution, not a failure of conservation for actual ant words.

Any complete relative cycle has even horizontal drift, by the pose sector.
Such a translation changes none of these row charges: an even-length segment
of a solid half-row has alternating sum zero, and finite defects retain their
signs. Thus the sum of all reset anomalies in the cycle is zero.

At row-1 this forces the number of lower S resets to be0 mod4. Row0 then
forces lower W resets to be0 mod4. Row U-1 forces upper S resets to be0 mod4
(the possible U=4 overlap with lower W is already zero), and row U forces
upper W resets to be0 mod4. Therefore EACH of the four reset types occurs a
multiple of four times in any relative cycle, of any drift.

This is only a pruning condition. It does not exclude a four-phase or longer
endpoint cycle and does not construct the missing left interface.

## 4. Discovery controls and known limitations

`arm_reset_interfaces.py` records literal paired histories for several return
phase offsets. `reset_endpoint_probe.py` implements the exact ideal maps above.
`search_reset_caps.py` sampled 2000 finite charge-compatible initial defects,
using only adjacent equal-color pair flips. Every run reached a declared
spatial/step/defect bound, so all outcomes are UNKNOWN. No complete relative
cycle was seen. The best bounded sample made24 resets; a larger follow-up
window made29 before leaving that window. Its reset positions drifted mainly
left, consuming pre-existing rail rather than demonstrating rightward growth.

The initially pure U=4,6,8,10 rail controls likewise do not give a cycle.
A normalization-variable shadowing bug in the earliest probe was corrected;
U=6 and the sampled-seed controls were rerun with the corrected key. No
positive claim relies on the earlier U=4,8,10 key statistics.

The global finite-seed conjecture remains open. Failure of these bounded
samples is not an exclusion of other endpoint fields, more rail profiles,
other cap architectures, or autonomous nonstandard behavior.
