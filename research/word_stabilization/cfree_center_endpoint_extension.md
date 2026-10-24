# The terminal C-free boundary center is new as well

Status: analytic strengthening of the independently audited C-free start-center
theorem, suggested and independently checked by the audit analysis.

For every feasible finite C-free word over U,V,Q,B, ALL its macro boundary
centers, including the final endpoint, are pairwise distinct. Define the
center by K(p,h)=2p+rot((-1,1),h) as before.

Only the final boundary requires proof. Suppose it repeats the center of an
earlier macro A, normalized to start at(0,0,N). A single macro has nonzero
center displacement, so at least two macros remain from A to the endpoint.
Let P be the last macro. Its marked terminal-star input is always

    final_pose_position + rot((0,-1), final_heading).

This identity holds for all four macro types, and that input is one of the
already proved29 globally fresh sites. Since P is strictly after A, it cannot
be a site read by A.

If the final pose has heading N, equal centers require position(0,0), making
P's marked input(0,-1). Every A reads this cell, a contradiction.

Otherwise the final pose is(-1,1,S), and P's marked input is(-1,2). Each of
U,Q,B reads this cell, so A must be V. The two-macro case is kinematically
impossible, using the four V+macro displacements in the start-center proof.

There are therefore at least three macros from A to the endpoint. Let E be
the successor of A, at(1,3,N), strictly before P. Every E reads(0,3),(1,4).
The same predecessor table as in the start-center proof forces P=V: P=U/B
would mark(0,3), and P=Q would mark(1,4). Its entry is then(0,4,S).
The starts of E and P have equal centers. They are distinct macro starts,
contradicting the already proved start-center theorem.

This extension still applies only to C-free factors. It does not assert
that a C-containing path has distinct boundary centers.
