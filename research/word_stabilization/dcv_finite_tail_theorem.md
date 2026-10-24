# Finite-support exclusion of the D/C/V language

Status: independently signed on 2026-10-23 at01:28 UTC. This is a restricted-language theorem, not the universal finite-seed highway conjecture.

## Statement and convention

A turn L is a left turn on a black square and R a right turn on a white square; every read flips the color. Starting pose and heading may be arbitrary. Define the literal words

- D = LLLLRLRRRR, length10;
- C = LLLLRLRRRRLRRRR, length15;
- V = LLLLRLRRRRLRRLRRRR, length18.

There is no Langton-ant trajectory beginning with finitely many black squares whose turn sequence has an infinite tail in {D,C,V}^omega. Equivalently, no infinite concatenation of these exact macros is physically realizable on a finite-support initial board. This does not say that every finite-seed ant eventually enters this language.

## Packet and residual representation

The common actual marker is M11=LLLLRLRRRRL. Every C or V begins with it. A D followed by the first L of its successor also supplies it. The literal short grammar bounds pure C runs. Form maximal packets D C^k or V C^k. DCC cannot have a following packet and DCCC cannot have a preceding packet; after finite boundary exceptions, only D, DC, V, VC, VCC recur. Each owns its RAW word and has the actual M11 following it.

At each marked cut the black board is the disjoint union of a rotated/translated core

K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}

and finitely many residual black cells. The exact ledger lists the residual inputs consumed by each packet and its residual outputs. All other residual cells persist unchanged. A produced residual token receives a producer-packet/output-slot identity until consumed. A token present at the initial cut receives an initial identity. If a produced token later supplies a residual input, every strict intermediate complete RAW+M11 context avoids its cell. This full-context protection, including marker-only reads, was independently reconstructed from the literal ledger.

Exact packet endpoints, input/output sets and guards are in `dcv_residual_core_resources.json`. The independently reconstructed boundary and protection proof is `../audits/check_dcv_tail_boundary_ledger_independent.json`.

## The finite protected-transfer theorem

Normalize a protected producer/consumer pair by placing the source packet at(0,0,N). A tuple(A,B,x,y,h,qx,qy) specifies its packet types, target pose and distinguished source output/target input q. The original ordinary and protected relations are independently signed. A102-row companion family was then proved by simultaneous least-gap induction.

The larger family `dcv_producer_closed_family.tsv`, SHA256 c4585979213b8f6bdec63aee6daec119ab16226bce6a9d5401a3ae5968d994e4, contains198 such impossible protected tuples. Its96 new obligations are proved simultaneously, not assumed individually. Choose a hypothetical counterexample of least temporal packet gap across the entire family. Each finite model retains exact colors on a selected patch and exact near-patch poses, while permitting arbitrary conservative OUT excursions. Watched cells retain the latest genuine residual producer, with conservative retirement on every complete-context touch. Identical rejection signatures may be quotiented. Unproved family clauses reject only strictly smaller temporal subpairs; every outer-origin label is exempt at the outer target. Thus the least-gap physical history maps into its finite overapproximation without being improperly deleted.

For every one of the96 obligations, a supplied inductive invariant contains the complete initial color cube, is closed under every guarded color/label/OUT transition, and avoids the target. The independent auditor reconstructed all geometry, frame normalization, producer identities, quotient classes and transition partitions from literal reads, then verified every invariant with a separately implemented reset-BDD checker. All96 use exactly the same final198-row family and the already signed102 relation. Therefore the hypothetical least-gap occurrence is impossible and the198 clauses follow together. The audit checks32,447,374 represented invariant states and73,682 inclusions; these counts are diagnostics, not substitutes for invariant closure.

The manifest `dcv_producer_closed_family_manifest.json` binds every model and invariant. Its historical provisional status is superseded by `dcv_producer_closed_family_signoff.md` and `../audits/closed_producer_family_independent.json`.

## Four bounded directional potentials

Let R_h be clockwise quarter rotation, kappa=(-1,1), and L(x,y)=x+3y. At a marked head pose(p,h), assign the core value

L(2p+R_h kappa)+c_h.

Each produced residual token q has value2L(q)+w_(packet,slot,producer heading). Each initial residual token has value2L(q)+I, where I=60 dominates every input lower-bound weight u. The exact integer weights are frozen in `dcv_free_direction_family102.json`.

For every recurrent packet and every global heading, the new core value and each output value are at most the maximum of the old core value and the consumed input lower-bound values. These are148 exact integer inequalities. Unchanged residual tokens retain their values. Every actual transfer satisfies u<=w: independent enumeration leaves exactly25 potentially violating protected tuples, and all25 belong to the now signed198 family. Consequently the maximum over the core and residual-token values cannot increase.

Apply the same construction to L(R_r z), r=0,1,2,3, with heading-indexed offsets and weights shifted by r. The two independent forms are x+3y and-3x+y, with determinant10; opposite rotations bound both signs. Initial support is finite and the stored weights lie in a finite set, so all marked head positions and all residual black cells lie in a fixed finite box. Literal packet lengths bound every intermediate read as well.

The independent arithmetic and enumeration audit is `../audits/check_directional25_potential_independent.json`; the precise25 tuples are `dcv_directional25_targets.tsv`. This tilted potential differs from the older69-obligation potential. Old case7 remains unproved but satisfies the new weight requirement and is unnecessary here.

## Contradiction

At macro boundaries, D changes total black mass by0, C by3 and V by4. A fixed finite box can support only finitely many C and V macros. The remaining eventual pure-D tail has fixed heading and nonzero displacement, a quarter-rotation of(1,1) per D, contradicting confinement. This proves the stated theorem.

The argument permits finite token recycling, including the literal DCVCCVV control. It does not claim that every V uses fresh initial fuel. Stronger explicit duration bounds are recorded separately so their analytic review status is not confused with this signed theorem.
