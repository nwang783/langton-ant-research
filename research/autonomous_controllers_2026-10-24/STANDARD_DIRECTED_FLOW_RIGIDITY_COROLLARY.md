# Directed-flow formulation of the signed fixed-inventory theorem

24 October2026. Elementary corollary of the independently signed
STANDARD_FIXED_INVENTORY_RIGIDITY.md SHAbef4d9c4 (audit29920102).
This changes the description of the exact hypothesis, not the search family.

Let a COMPLETE WHITE translating ant front have full drift d=(-2,2). Suppose
its entire directed physical edge-flow count, modulo Z*d, is EXACTLY that of
the retained standard104 trace normalized to headingN. In particular edges
outside that supplied finite quotient support have count zero; the condition
is not agreement only on a cropped strip. Then the front is standard104 up
to temporal phase. Properly rotating/translating the entire flow inventory
preserves this conclusion. There is no assumption that arbitrary controllers
have this flow inventory.

Proof that the directed-flow hypothesis suffices. At any visited cell, let a,b
be its incoming counts on the two opposite headings + and-. Label the outgoing
+ heading to be R applied to incoming+. Let c be its outgoing+ count. Its total
read count is n=a+b, and complete WHITE alternation fixes r=ceil(n/2) R turns.
Write X,Y,Z,T for the numbers of events(incoming+,R),(incoming+,L),
(incoming-,R),(incoming-,L), respectively. The flow and WHITE equations are

    X+Y=a,   Z+T=b,   X+Z=r,   X+T=c.

They have the UNIQUE solution

    X=(c-b+r)/2,   Y=a-X,   Z=r-X,   T=b-r+X.

Thus the directed edge flow fixes every per-cell turn/heading event count;
there is no hidden free matching count. The actual standard flow makes these
integers nonnegative. Summing its incoming counts gives exactly104 reads, so
its full event period is104. The signed fixed-inventory theorem now applies
to ALL possible ordered local histories with these counts and returns the
standard ordered histories and single successor orbit.

Do not replace directed edge counts by undirected support, total visits per
cell, final output colors, or first/last graphs. Those weaker data need not
fix a,b,c and do not meet this corollary's hypothesis. No new bound on width,
period, multiplicity, other inventories, or arbitrary finite-seed dynamics
is inferred.
