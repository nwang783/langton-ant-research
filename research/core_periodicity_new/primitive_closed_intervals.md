# Primitive closed physical-pose intervals

Status: the lemma below was independently reviewed by the proof auditor on 2026-10-22 at 19:14 UTC. It is an exact chronological observation, not a proof of core periodicity.

## Lemma

Consider a feasible finite ant interval with physical poses P_0,...,P_T, where a pose is the cell and incoming heading. Suppose P_T=P_0 and P_0,...,P_{T-1} are pairwise distinct. Then its T read cells are pairwise distinct. Consequently its physical edges form a simple rectilinear lattice polygon, every vertex is a quarter-turn, its raw signed turn sum is +4 or -4, and its odd-visit mask is precisely the set of polygon vertices.

Proof. In a fixed parity sector, each cell permits only two incoming headings, which are opposite. If a read cell occurs twice before T, its incoming headings must be opposite, since equal headings would repeat a proper-prefix pose. There cannot be a third occurrence. Feasibility makes the two turns opposite. Writing the earlier incoming heading as h and turn as a in {+1,-1}, the later outgoing heading is h+2-a, equal modulo 4 to the earlier outgoing heading h+a. Thus the two visits have identical successor poses. If both successors are proper-prefix states, this violates distinctness. If the later successor is P_T=P_0, the earlier successor is also P_0 but has positive index less than T, again a violation. Hence all read cells are distinct. Unit grid edges cannot cross except at lattice vertices, so the resulting polygon is simple; the remaining conclusions follow from its turning number and one visit per vertex.

The smallest clockwise example is RRRR. A non-unit example is (RRL)^4. It reads 12 distinct vertices, has eight R turns and four L turns, and returns to the starting pose. Its four L vertices are exactly the minimal entry black set.

## Essential limitation

This is a statement about a literal feasible interval. Deleting one such loop from a longer turn word generally destroys read alternation at its vertices. Therefore it does not justify iterating chronological loop erasure while retaining feasibility, charging every resulting loop to a fresh initial seed cell, or replacing the whole history by a disjoint family of simple polygons. The causal information lost by that erasure is exactly the unresolved obstacle.

## Quotient and curvature bookkeeping

The physical-pose action of G=C4*C4 has the additional relation (R L^{-1})^2=1: R L^{-1} reverses the heading at the same physical cell. With S=L^{-1}, the quotient is the square Euclidean triangle presentation R^4=S^4=(RS)^2=1. This algebraic observation does not itself retain the chronological order of visits to a puncture/cell.

For alternating syllables a_i^{e_i}, let f=sum sign(a_i)(e_i-2). Then f=c-2 sum sign(a_i), |f-c|<=2, f(g^{-1})=-f(g), and its multiplication defect is at most 2. Inverse syllables cancel in pairs; after those cancellations, at most one non-inverse equal-generator merge remains, whose defect is +2 or -2. In particular f((R L^3)^2)=-4. These formulas were independently checked, but no finite-seed bound on f follows from them alone.
