# A strictly broader capture class from a conditional finite no-reentry cut

24 October 2026. AUTHOR exact full-future certificate; independent audit requested. This is a finite causal PORT CUT, not a connected geometric wall, a component-separation assumption, or a universal record-language cover.

## 1. The condition, with the whole ambient field explicit

The actual head is (0,0), E. The ENTIRE CURRENT half-plane x-y>=0 is WHITE. Let J and W be the fifteen black and four white cells of the signed phase45 outward guard. Let h=(-3,-2), one of its required black cells. Fix these common eighteen bits:

    all fourteen cells of J except h are BLACK;
    all four cells of W are WHITE.

Here

    W={(-3,1),(-3,2),(-2,0),(-1,0)}.

The additional nineteen old-side ports form two finite pockets:

    P_left={(-6,-4),(-6,-3),(-5,-4),(-5,-3),(-5,-2),
            (-4,-3),(-4,-2),(-4,-1),(-4,0)};

    P_upper={(-1,3),(-1,4),(0,3),(0,4),(0,5),
             (1,3),(1,4),(1,5),(2,3),(2,4)}.

Require the CONDITIONAL clause

    h is BLACK, OR every cell of P_left union P_upper is WHITE.

No condition is imposed on any other old-side cell. Every such cell, and every full archive component containing it, is retained.

**Theorem.** Every finite board satisfying these premises is eventually canonical standard104. After time 262 it never again reads the original old half-plane x-y<0. The condition is strictly weaker than the complete original phase45 guard within this ambient class: every original-guard board satisfies it regardless of the nineteen new ports, and the actual fourteen-cell missing-bit board satisfies it while failing the original guard.

Proper rotations and translations give the corresponding other orientations. Reflection or a switch of ant sector is not used.

## 2. BLACK branch: the new ports are genuinely irrelevant

If h is black, the common eighteen bits together with h are exactly the signed original nineteen-bit guard. Its canonical word is valid immediately. The complete infinite old-side read footprint is exactly those nineteen cells, and its LAST old-side read is at time 161. In particular none of the nineteen new ports is ever read in this branch. They may be black, white, connected to a large archive, or arbitrarily placed within that archive without affecting the conclusion.

Thus the new condition has not silently strengthened the original guard with extra whiteness.

## 3. WHITE branch: exact finite exposure and then no re-entry

If h is white, the full old-side exposure of the certified missing-bit continuation consists of exactly

    E = J union W union P_left union P_upper,

with |E|=38. Its initial bits are fourteen black and twenty-four white. All other initial old-side cells are outside the ENTIRE proposed future read set.

The first 262 physical updates are replayed from the complete fourteen-cell seed. Their last old-side read is time 261 at (-2,-1). At cut 262 the actual head is (-1,-1), E and the complete field has 46 black cells. Its next 104-word is a cyclic canonical word with displacement (2,-2). Every read of that first period lies in x-y>=0; each later period advances this projection by four.

An exact all-period ray-parity certificate, with 171 change-point tests, verifies the complete infinite word on this full 46-cell state. Consequently the whole infinite tail stays in the originally pristine half-plane. It never re-enters x-y<0 after the stated exit.

For an arbitrary admitted old archive, first-difference induction is now decisive. Before time 262, every old-side read is in E and has its prescribed bit; every initially fresh-side bit was white and has exactly the reference history of toggles. At and after 262, the reference path never reads an old-side cell at all. The archive cannot cause a late disagreement because it is disjoint from the complete infinite read set, not because it is behind an active component or outside a guessed finite simulation box.

## 4. Why these really are exposed ports

The nineteen first-read times, in temporal order, are

    72,73,169,174,175,176,184,185,186,189,190,191,
    212,225,226,227,235,236,237.

For each port separately, the checker adds one BLACK cell to the fourteen-cell seed at that port. The entire earlier physical history remains unchanged; at its exact listed first read the expected R becomes L. All these added cells lie strictly on the old side, so the current pristine half-plane remains genuinely white.

Therefore simply dropping h from the original guard does NOT force this recovery word. Each additional port condition is necessary for this PARTICULAR white-branch word within the stated ambient class. This is not a necessity statement for eventual capture by some different route: the singly perturbed fields might also capture, and no noncapturing example is asserted.

The two pockets are not claimed to be a complete connected wall. Their role is that every possible first encounter with unspecified old input along these certified branches has been exposed and either prescribed or proved never visited.

## 5. Adversarial controls

The paired-wake control is handled rather than ignored. The correctly filled fifteen-cell guard takes the BLACK branch. Its missing-bit fourteen-cell counterpart takes the WHITE branch, including the four early output lifetimes that later become inputs. The proof waits through all those actual returns and only declares no re-entry at the certified cut 262. It never cashes speculative permanent-wake credit at the earlier common prefix.

Arbitrarily remote old-side black material is permitted outside E. Two explicit complete-board tests add the archive

    {(-1000000,-999999), (999999999,1000000000),
      (-1000000000,5), (-7,0)}

to the two branches. Every added cell remains black and is never read. This is an illustrative regression; the theorem covers arbitrary finite old-side extensions outside the actual branch exposure, not merely these four cells.

The retained tangential interrupter family is different in the exact necessary way. After its two-move RL entry it has a genuine pristine diagonal half-plane, but its candidate tail drifts tangent to that boundary and has infinitely many old-side read sites. Its initially unread cap a_K is first read after 277+104K moves from that entry. Such a tail cannot have a finite old-side no-reentry exposure cut; the signed first-discrepancy construction remains valid. This family also does not satisfy the fourteen mandatory black bits of the present separator. No assumption that pristine freshness alone clears tangential old-side rays is made.

## 6. Genuine record realization and scope

Every board satisfying the displayed common bits can be given an actual two-move pristine-record preparation: replace its black (-1,1) by black (-1,0), start at (-1,1), E, and execute RL. The head's earlier projections are -2 and -1, then the displayed cut has projection 0. The complete field still lies strictly on the old side. This preserves arbitrary other admitted archive cells and does not rely on a fictitious head-position record inside prepared forward input.

The result is a verified broader sufficient capture class. It does not show that every fresh record reaches this class, prove a generic barrier for arbitrary colorings, or resolve global attraction. Its value is a finite, conditional interface that tolerates a real guard defect while retaining and excluding every possible old-input port on the recovery route.

## Artifacts

`check_conditional_port_separator.py` independently constructs both exposure sets, replays the full 262-move recovery and its all-future tail, proves the conditional bit coverage, verifies all nineteen first-discrepancy controls, and preserves the complete huge-archive boards. `CONDITIONAL_PORT_SEPARATOR_CHECKED.json` retains every field, word, parity change and port. The manifest binds the independently signed original guard and missing-bit controls. Independent audit is pending.
