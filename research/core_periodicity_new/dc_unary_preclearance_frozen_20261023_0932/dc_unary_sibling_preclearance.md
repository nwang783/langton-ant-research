# Unary-D preclearance: unique order, but no fresh-root inference

23 October 2026 09:32 UTC. Author finite geometry passes; independent review
requested. This is a narrow conditional sibling/actual-cursor lemma, not a
literal control, arbitrary-chain exclusion, or finite-fuel theorem.

Normalize a DC producer to (0,0,N), with outputs A=(2,0), B=(2,3), C=(3,1),
D=(3,2). Suppose A remains the current continuing residual identity, and all
three ORIGINAL spare identities are retired by unary D packets before the next
DC consumes A at (1,0,E). Other support packets may occur, and every replacement
identity is retained. Only the actual retirement packets of B,C,D are required
to be D.

## Complete local alternatives and order

A D retiring a given original spare has input (0,1), so its head is fixed once
its heading is chosen. The physical sector allows exactly these six placements:

- B: (2,2,N), blocked while original D remains in its core;
  or (2,4,S), with no original-sibling blocker.
- C: (2,1,E), blocked while A remains in its core;
  or (4,1,W), requiring originals B and D already retired from white cells.
- D: (3,1,N), blocked while A and C remain in its core;
  or (3,3,S), blocked while B remains in its core.

Therefore the only possible order of ORIGINAL identity retirements while A
survives is

B at (2,4,S), then D at (3,3,S), then C at (4,1,W).

This is complete over all six sector-compatible unary consumers, not one
heuristic choice. A removed original need not stay white: intermediate supports
may install replacements, and the later actual guards must still be satisfied.
The three D replacement outputs are (0,4),(1,3),(4,3), respectively. They miss
all later listed cleanup contexts and the next DC context. Thus original-sibling
and direct-replacement masks do not by themselves force an extra initial root.
No full supported word is asserted feasible by this mask observation.

## Joint actual-head clock surcharge

Let C clock zero be the original DC start, source included/consumer excluded as
in JO. The first D has heading2, hence clock2 modulo4. Its produced input has
age at least3 by JO, so its clock is at least6.

After that D's raw word, the head is (1,3,S). The second D starts (3,3,S).
At fixed heading S, every zero-C packet D,V,U moves with nonpositive x and
nonpositive y. Hence a zero-C intervening word cannot make the required (+2,0)
displacement. Since both D starts have the same heading, their clock gap is a
multiple of four, and it must be at least four. The second D clock is therefore
at least10, not the separately permitted6.

The next heading change S to W requires at least three Cs modulo four. Thus the
third D clock is at least13. The following DC continuation heading E requires
a further two Cs modulo four, so a continuation preceded by all three unary
preclearances has produced age at least15. The individual source-spare ages
6,6,5 cannot simply be combined as a chronological strategy.

These lower bounds do not state that any equality is realizable. Arbitrarily
large zero-C detours can occur once heading-changing packets intervene; no
finite head box, packet-depth cutoff, or increased counted threshold is used.
If the original main A is consumed before all three spares retire, the unique
order and age15 conclusion need not apply. The signed all-N rotating-spine law
remains separate and only requires retirement before the fourth descendant.

Finite source: check_dc_unary_cleanup_order.py and
chronology_dcuv/dc_unary_cleanup_order.json. Dependencies are the signed literal
residual geometry, JO's produced-D age>=3, and the ordered identity/core partition.
