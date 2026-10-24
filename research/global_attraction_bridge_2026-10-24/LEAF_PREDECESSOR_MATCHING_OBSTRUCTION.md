# An injective first predecessor step does not supply a leaf-resource injection

24 October 2026. Exact chronological sublemma and literal countercontrols; independent audit pending.

## 1. The valid first-step map

Take an actual interval[s,t] whose endpoint has not been read within that interval. Its interval-read last-exit tree has that fresh endpoint as root. For a read vertex v, let ell(v) be its last read. If ell(v)>s, let u be the actual cell read at ell(v)-1. Define f(v)=u when ell(u)>ell(v), and leave f undefined otherwise.

This partially defined map is injective. The directed edge u->v cannot be u's selected last-exit edge, because u is read again later than v. The sector gives u exactly two outgoing physical neighbors, one already occupied by its last-exit-tree edge. There is only one remaining neighbor v. Thus two distinct vertices cannot map to the same u.

Every tree leaf lies in this domain except possibly the initial-cut vertex if its last read is exactly s. For a leaf, its last incoming edge is not a selected tree edge, so its predecessor must have a later departure.

The fresh endpoint hypothesis matters. For an arbitrary old endpoint, its earlier exit edge is deleted; it is an exceptional predecessor with no selected outgoing edge and may supply two leaves. No exception is omitted in the stated lemma.

Repeated f steps strictly increase last-read times, so they terminate. This does NOT show that they terminate at an old-cut input or a last-R output. Also, although the f graph consists of disjoint chains, one chain can contain more than one tree leaf. Terminal assignment is therefore not automatically an injection from leaves.

## 2. What an unpaid leaf would need

Let C be the set of BLACK-at-s cells actually read during the interval, and O its last-R output vertices. A vertex outside C union O starts WHITE, ends WHITE, and has first turn R and last turn L. The proposed resource route was to continue an unmarked leaf along f until it met C or O.

The following actual controls show that this continuation can stop at an unmarked NONLEAF. This invalidates the proposed direct-chain proof, not every possible injection or the conjectural numerical bound leaf(T)<=|C|+|O|+1.

## 3. Literal empty-seed obstruction

Use the already signed complete empty-seed interval[5710,6042]. In its interval-read last-exit tree, v=(0,8) is a leaf. Its reads are

    R5812, L5844, R5880, L5884.

The predecessor of its last read is u=(-1,8), read R at5883. That vertex is read later, at5919, so f(v)=u. Both v and u are WHITE at the two interval endpoints; neither is an input in C nor an output in O.

The reads at u are R5811,L5879,R5883,L5919. Its final incoming predecessor is(-1,7) at5918, which is that predecessor's LAST departure. Hence f(u) is undefined: the chain has stopped at an unmarked indegree1 vertex. All fields and all exterior reads are the retained actual empty-seed history, not a supplied port model.

## 4. A genuine completed pristine-drought obstruction

In the signed MT100 pristine drought[40071,109168], the leaf v=(432,449) has reads R40189,L40197. Its last predecessor u=(432,450), read at40196, is revisited at40212. Again f(v)=u, and both vertices are WHITE at both endpoints. At u, the last incoming predecessor is(431,450), last read40211, so the chain stops at unmarked indegree1 u.

A second exact chain in the SAME completed drought is

    (213,234), last57427 -> (213,233), last71738
                           -> (214,233), last71753.

The first TWO vertices are unmarked tree leaves. The terminal vertex is an unmarked indegree2 vertex with its last incoming edge in the tree. Thus there are both uncharged terminal vertices and multiple leaves on a single predecessor chain.

The checker reconstructs the full interval tree and all last-arrival times. It finds783 unmarked leaves in this MT interval;275 starting leaves have forward chains ending at unmarked vertices. The number275 counts starting leaves, NOT distinct terminal vertices, disjoint cohorts, or independent resource debts.

## 5. Scope

The valid injection is a precise local chronological fact. The countercontrols identify the exact failure of its proposed continuation: reaching a normal WHITE-to-WHITE nonleaf, potentially after traversing several unmarked leaves. A stronger argument would have to account for those terminal branches and their other subtrees without reusing the same inputs or outputs.

No universal leaf bound, amortized renewal law, or global attraction conclusion is obtained. The gross inequality leaf(T)<=|C|+|O|+1 remains OPEN and unused. The complete whole-history tree and the interval-reset tree are distinct objects; this note explicitly uses the latter only for the proposed fixed-cohort leaf charge.
