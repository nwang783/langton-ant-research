# The separate C-face L-transition flow

23 October 2026, 13:00 UTC. Analytic extension to the independently approved
max_C_first_L_face_birth_backbone.md. This flow is NOT the physical-cell
flow used by the A/B/C rank-two subtraction theorem. Independent review
requested before use.

For each actual directed ant edge e, record the center z(e) of its
clockwise C face on the right. At a primal R read, the incoming and
outgoing edges have the SAME C face. At an L read they have the two
opposite C faces incident to that cell. Thus z follows a walk on the
natural diagonal C-face graph, with a pause for each R and exactly one
diagonal step for each L. Each diagonal step changes each Cartesian
coordinate by one in absolute value.

Over one actual full event period the C-face walk displaces by the SAME
d. The resulting nonnegative integer L-transition flow on the full-drift
C-face cylinder is balanced and has homology+1. Its total edge mass is
L_total, the total number of L reads in the actual period. The flow may
have both orientations on the same undirected diagonal; no fixed checker
orientation is asserted for this new graph.

Every selected first-L face-birth backbone transition G->F is an actual
L1 occurrence of this flow. Distinct functional face-birth cycles have
disjoint face nodes, so they select distinct L1 transition occurrences.
For any c selected such cycles, of total length N, subtract those
occurrences from this SEPARATE transition flow. The residual is balanced,
nonnegative and has homology1-c, hence displacement(1-c)d. Each remaining
diagonal step contributes at most one to any Cartesian displacement, so

    L_total >= N + ||d||infinity * abs(1-c).

This does not assert the same subtraction from the physical-cell flow.
It does not authorize adding the bound to overlapping A/B/C budgets.

There is also an exact maximum-face count. Let n be the total number of
GLOBAL-max C face classes, and let delta be the number of primal classes
where both R reads use the same global-max C face (a max height-two
boundary defect). All four corners of each max face are active. At each
corner its R count is one, except for precisely these delta repeated-R
corners, where it is two. Since every R belongs to exactly one C face,

    R_max = 4n+delta,
    R_total >= 4n+delta.

The canonical birth of EACH max face is one L1 occurrence with that face
as its outgoing C face. One L1 cannot birth two faces, so L_total>=n.
Together,

    P=R_total+L_total >= 5n+delta.

The signed global-H defect theorem gives delta>=1, but this is a plateau
area/read-budget relation, not a new universal speed constant or an
exclusion. Combining only the two independent L_total necessities is safe:

    P >= 4n+delta + max(n, N+D*abs(1-c)).

These claims keep the true global counts and actual full drift. They do
not count nested chronological waits as separate paid work, bound the
number of gates, or prove standard104 capture.
