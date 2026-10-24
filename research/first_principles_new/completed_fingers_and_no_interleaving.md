# Completed fingers, projected no-interleaving, and square-to-coset inclusion

Status: independently reviewed proof,22 October2026. The auditor checked the analytic grammar, footprint bounds, finite incidence tables, unfinished-call argument, rebasing, and noncircular first-violation coupling. Snapshot/replay: `../audits/module_inclusion_snapshot/` and `../audits/module_inclusion_replay.log`. It uses the independently reviewed autonomous face-module theorem, not any presumed square-to-coset inclusion. Square-language inclusion also appears as an existing claim in Gajardo2003 Theorem3; this is an independent reconstruction and repair of the route, not a claim of priority or a proof of highway attraction.

## 1. Exact return-word grammar

Write b for the opposite of a. A completed module call uses only completed G calls of its children. If the parent return is G, it skips child1, and either skips child2 or calls it once. Its word therefore is

    G_a = a^4  or  a^2 G_b a^2.

If the parent return is B, it calls child1 once, and either skips child2 or calls it once:

    B_a = a G_b a^3  or  a G_b a G'_b a^2.

The primes denote possibly different finite G calls. These are exact consequences of the return table in `face_module_return_lemma.md`, not extra hypotheses. Every completed module word reduces to the identity in G=C4*C4.

## 2. The G ladders and B fingers

Use square coordinates with the module root w=(0,0), incoming heading north, sign R, and predecessor p=(0,-1). The two parent interior cells are x=(1,0),y=(1,-1).

A G call of recursive depth n has word G_R(0)=R^4 and G_a(n+1)=a^2 G_b(n) a^2. Its read set is exactly

    {(i,j): 0<=i<=n+1, j in {-1,0}}.

The four endpoint-column cells are read once; each cell of an interior column is read twice with opposite symbols. Its total square-lamp toggle is therefore exactly the four corners of this unit-height rectangle. In particular, the initial and final-column coordinates are not a finite-depth approximation.

Induction proves that equal projected cells anywhere in one G call are equal cosets. The inner G_b ladder is translated one column east. The two newly added cells lie in column0. The only overlaps with the two initial/suffix root-face steps are the inner module's root and predecessor, which are precisely the same cosets by the module alias lemma.

A B_R call has a G_L ladder rooted at x with heading east. This is a northward vertical ladder in columns0,1, starting at row0. It may also have a G_L ladder rooted at y with heading south. This is an eastward horizontal ladder in rows-1,0, starting at column1. The two ladders intersect only at x, and the two copies of x are the first child's root and the second child's predecessor, hence the same coset. Their overlaps with the parent face are likewise exactly the named root/predecessor boundary cosets.

Consequently each completed G/B module call is injective from its visited cosets to physical square cells: two reads in that call at the same square cell belong to the same coset. In particular every physical hit of either boundary point is at its actual boundary coset.

For finite-interface purposes, all complete R calls are contained in the fixed unbounded set

    Q_R = {x>=0, y in {-1,0}} union {x in {0,1}, y>=0}.

The analogous set Q_L is reflection across x=0. Rotate and translate these sets with the incoming pose. These are bounds for COMPLETED calls only; unfinished calls can wander elsewhere.

## 3. A finite interface for a tracked old coset

Start at an equal-colored incoming edge and use the trapped module realization. Let w=(0,0),p=(0,-1) be the two root boundary cells. We prove the following for a tracked coset A equal to w,p,R,or R^2; the L,L^2 cases are reflections:

    If a physical read at the projection of A is followed by a later read of coset A, then that physical read also belongs to A.

It is enough to inspect a finite explicit interface, but every abstract call must be treated as potentially infinite rather than truncated.

### 3a. Root or predecessor

Keep the two root faces explicit. Their four opposite-sign child modules are abstract. Their entry cells are the four distinct root-face interior cells, not w or p. By the prefix alias/separation lemma, their interiors contain neither tracked coset; only the first child of either root face has w as predecessor. No child has p as predecessor.

The rotated Q sets show the same statement for PHYSICAL hits during complete calls: the first child of either face can hit w only at its actual predecessor coset, while the other two children miss w, and all four miss p. All explicit root-face reads have their stated cosets.

### 3b. R-face interior x=(1,0) or y=(1,-1)

Keep the R root face and its two L children explicit. Treat the opposite root L module and the four R grandchildren as abstract calls. The four grandchildren have the following root poses:

    (1,1), north;   (0,1), west;   (2,-1), east;   (2,0), north.

The Q_R footprints, respectively, intersect {x,y} as follows:

    {x}, empty, {y}, empty.

The first intersection is precisely the first grandchild's predecessor; the third is precisely the third grandchild's predecessor. The Q_L footprint of the opposite root module misses x,y entirely. The explicit cells are w,p,x,y,(1,1),(0,1),(2,-1),(2,0); these physical points are distinct except for the already identified boundary aliases.

### 3c. Why unfinished calls cannot conceal a counterexample

In both interfaces every abstract entry cell is different from the tracked coset A. Its abstract interior also excludes A by the algebraic separation lemma. Hence, if a physical hit under consideration occurs inside an abstract call and a later read of A exists, that call must eventually return. The only qualification is when the later A read is its last boundary: the trapping theorem then forces completion on the very next step. Either way the hit belongs to a COMPLETED call, so its Q bound and boundary-coset identification apply.

Thus the abstract calls cannot contribute a physical hit at A's projection in a different coset before a later A read. The explicit interface cannot do so either. This proves the tracked-coset statement without imposing any bound on call duration or depth.

## 4. Global autonomous no-A-B-A

Take any purported visits at times s<u<t to the same physical point, with the coset at s,t equal to A and that at u different from A. Time-shift to s and left-rebase the group and physical pose. The autonomous lamp dynamics remains the same model.

Let a be the first turn. The first different turn occurs at index j in {1,2,3,4}; four equal turns return to a flipped starting lamp. Before that index the square path is one simple unit-face arc, so there is no other-lift physical return to its initial point. At index j, the previous lamp was just flipped to b=opposite(a), and the current lamp is b. Rebase at this equal-colored edge.

The old target A is now a^{-j}H. For j=1,2,3,4, respectively, this is the special predecessor, a^2, a, or the root. All are covered by Section3 (with reflection if a=L). Any later physical hit of its point followed by a read of A must therefore itself be A. This contradicts the alleged middle visit u.

Hence, for EVERY autonomous coset-ant orbit with arbitrary initial lamps, visits to one fixed coset form a contiguous block in the visit chronology of its projected square cell. This is stronger than ordinary per-coset alternation.

## 5. Square-to-coset legality by first violation

Lift the prefix of any square-ant turn stream by reduction in G, and assign each coset its actual first-read color. Suppose there were a first A-B-A interleaving in a projected physical-cell chronology. Before its final A read, all coset blocks are contiguous in their physical chronology. The turns at every coset therefore alternate, so the entire prefix preceding that read is a legal autonomous coset-ant prefix with the assigned lamps.

Extend these assigned lamps arbitrarily to all other cosets. Its autonomous orbit has exactly the same prefix and reaches that same final coset A, regardless of the symbol that will now be read. It therefore already exhibits the forbidden A-B-A pattern, contradicting Section4.

There is no first interleaving. Every square-ant turn stream is consequently legal for an autonomous coset ant with the first-read assignment. The independently audited bounds of five visits per group state and six per coset, and unique limiting reduced boundary ray, then transfer to every square-ant trace.

This is NOT standard highway attraction. The assigned coset coloring can have infinite black support even for a blank square seed. The exact standard104 obstruction in `standard_lift_infinite_seed_obstruction.md` still applies, and periodic selection plus side-excursion stabilization remain unproved.

## Independent finite incidence certificate

`../audits/check_module_projection_neighborhood_global.py` independently checks a unified neighborhood consisting of both root faces and their four child faces. Its eight abstract grandchildren cover all cases above simultaneously. It verifies16 explicit-face representatives, all eight exact unbounded-Q intersections, and all eight first-letter/rebase cases. The saved JSON is `../audits/check_module_projection_neighborhood_global.json`.

Only the footprint bound and correctness of predecessor hits are necessary for the interval proof. The stronger full completed-packet projection injectivity in Section2 is an additional consequence, not an assumption needed for the bridge.
