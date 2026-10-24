# Small pure position inflations without heading preservation

Status: independently audited, 22 October 2026, 20:48 UTC. The short trees
were independently regenerated without cutoffs, and every oriented inventory
and owner set was independently reconstructed. This is a broader class than
the earlier pure position-and-heading inflation family.

## Statement

For a finite-black-seed square ant, there is no integer k with 2<=k<=5 and
complex expanding scale a, |a|>1, such that

    p(kn)=a p(n) for every n>=0,

where p(0)=0. There is **no assumption** that h(kn)=h(n), and no finite-state,
substitution, or regularity assumption on the choice of local refinements.
Since p(1) is a unit Gaussian integer, a is automatically Gaussian.

## Complete geometric reduction

Every k-block starts at a p(n), ends at a p(n+1), and may have either allowed
fine heading phase. Enumerate all internally feasible k-letter words and their
oriented displacements. The coarse next letter is already present in the fine
prefix; select any image matching the required displacement, without constraining
its final heading. Consecutive equal reads of a fine cell are the only chronology
pruning rule. Root images must begin with the selected coarse root letter.

search_position_only_inflations.py implements this finite-prefix tree. Its
EXHAUSTED results are complete, while its NODE_CAP and DEPTH_CAP labels are only
UNKNOWN outcomes. It obtains:

* k2: a=1+-i both exhaust, 11 nodes and maximum5 macros each.
* k3: only a=2+-i survive the prefix test; use fuel below.
* k4: a=+-2i exhaust in11 nodes and maximum4 macros; a=2 exhausts
  in5 nodes and maximum1 macro. The remaining a=2+-2i use fuel.
* k5: a=-1+-2i exhaust in16,391 nodes and maximum27 macros;
  a=1+-2i exhaust in5,391 nodes and maximum26 macros. The remaining
  a=3+-2i and a=3 use fuel.

These are all possible expanding scales from internally feasible root images.
Long capped branches are genuinely feasible prefixes, generally self-avoiding
and requiring thousands of distinct initial black cells. They are not finite-seed
countermodels or evidence that one exists.

## Correct normalization of heading phases

Start in pose-sector x+y+h=0 mod2. At the coarse read n, let its incoming heading
be H. Translate that coarse cell to zero and rotate H to north. Translate the
fine coordinates by a p(n) and apply the same rotation. A possible earlier
coarse owner has center q and normalized heading Hc, so

    q_x+q_y = Hc mod2.

A fine boundary heading Hf obeys

    Hf = (k mod2) Hc + theta mod2,

where theta=0 for odd k, and theta=H mod2 for even k. The scale parity
Re(a)+Im(a)=k mod2 follows from the first k-block's displacement.
Thus odd k needs one normalized inventory; even k needs both theta=0 and1.
The script position_only_ownership.py includes both permitted values of Hf,
all four Hc, both coarse turn letters, and every matching local word.
It does not silently restore the discarded heading-equality hypothesis.

## Exact owner calculation and fuel

For a target first-L offset z, another oriented image at coarse center q can
possibly read it only if

    z = a q + o,

where o is one of that image's physical offsets and the above parity constraints
hold. Exact Gaussian division lists all such q. The calculation deliberately
keeps every geometrically possible owner, whether a global history can actually
realize it or not.

For every target coarse-R image in each surviving scale and phase inventory,
there is a locally first-L cell z whose possible owners all have q_y>=0.
The full owner sets are saved in position_only_ownership_2_5.json. Except for
some k5,a=3 images, these witnesses are actually private to q=0.

Now take a strict outward coordinate record of the actual coarse path, beyond
the initial pose. Its incoming heading points outward. After the normalization,
every earlier coarse center has q_y<0. The protected first-L fine cell is therefore
unread by every earlier macro, and is unread earlier within its own macro by
construction. It consumes a distinct initial black cell.

Among strict records, coarse first-L records themselves consume distinct initial
black cells, and every coarse first-R record consumes an initial black cell by
the fine witness above. A seed of mass m has at most m of each type, hence at
most2m strict coordinate-record increments. The full trajectory is bounded,
contradicting the previously audited finite-domain exclusion.

The argument is valid occurrence by occurrence. No heading phase is assumed
periodic, computable, or selected by a finite controller.

## Independent verification

The no-cutoff tree replay is audits/check_position_only_small_trees_independent.py
and its JSON report. It matches all nine EXHAUSTED trees exactly. The independent
phase-aware geometry replay is computability/check_position_only_owners_independent.py
and its JSON report:160 oriented inventory records and20 target images, all
owner sets and private/forward flags matched. Both reviewers checked that the
normalization does not restore the omitted heading-equality hypothesis.
