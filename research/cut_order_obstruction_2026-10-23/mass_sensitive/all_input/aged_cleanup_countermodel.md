# Eight finite roots can fund compulsory sibling cleanup in an aged resource DAG

23 October 2026. Explicit countermodel to an all-input RESOURCE relaxation.
It is not an ant, not a literal packet-mask model and not a proof that any
physical cleanup ordering is feasible.

## Exact included premises

Use eight root families r=0,...,7, processed round-robin by an abstract C clock.
Initially family r has one main identity at (0,10r). At clock k, set r=k mod8.
If k>=8, first perform a V-type helper with two inputs and six outputs and
a D-type helper with one input and one output, clearing the previous three
spares of this family. Then perform a DC-type main reproduction with one
input and four outputs. V,D preserve the abstract C clock; DC increments it
by one. These names specify INPUT/OUTPUT COUNTS only, not literal masks.

For family generation n, put x=4n, y=10r. The main identity at (x,y) is replaced
by

    next main (x+4,y),
    spare a=(x,y+1), b=(x+1,y+1), c=(x+2,y+1).

Eight C units later, immediately before this family's next main reproduction,
V retires a,b and produces six immutable buds

    (x,y),(x+1,y),(x+2,y),(x+3,y),(x,y+2),(x+1,y+2).

Then D retires c and produces the immutable bud(x+2,y+2). All three ORIGINAL
spare identities are therefore retired and their cells left white before
the next main reproduction. No original spare is silently recolored or
relabelled. Every output is a fresh identity; buds are never consumed.

## Binary cells, ages and all-input parentage

Different generation blocks have disjoint x ranges[x,x+3]; different families
have disjoint y bands[y,y+2]. Main anchors are on block boundaries and never
coincide with a surviving bud. Every output cell avoids the surviving board
at installation, and every required input is present. Thus all current
identities occupy distinct ordinary lattice cells, with finite support at
each finite clock. The initial roots lie in one fixed segment of length70.

Every produced main or spare is consumed at C age EXACTLY8. Every parent-to-
output displacement, for EVERY input parent of a multi-input helper, has
L-infinity norm at most4. Thus plain all-input coordinate speed is at most1/2,
with a separate initial edge of length at most4. Assign birth heading
h(k)=-k modulo4. Then every produced-parent age obeys the heading congruence;
V,D preserve heading and DC changes it by-1. This is only the marginal
heading label, not an actual moving head or full role potential.

At cumulative C count K, each family has advanced at most ceil(K/8) main
steps. Every current cell is within K/2+4 of its own root, hence within

    floor((2K+13)/3)

since K/2+4 <=(2K+13)/3. Initial roots have displacement zero. The signed
numerical LB root-box ceiling is therefore satisfied. No claim about exact
literal output coordinates or all272 role inequalities follows.

## Exact mass and topology

After K main reproductions, the number of completed V helpers and D helpers
is H=max(K-8,0). Each DC gains three identities, each V gains four, and D
gains zero. Therefore

    r(K)=8+3K+4H.

This is exactly the recurrent-eight mass formula with k=K,v=H,u=0. There are
no cross-family dependencies or mergers. Every identity's FULL initial root
set remains the singleton{r}, including every V output, because both helper
inputs descend from the same root.

Build the full incidence DAG from the companion note. It is directed-acyclic
by construction. Its component count is always8. Every V consumes siblings
already connected through their common DC producer, and creates one genuine
undirected reconvergence cycle. Thus

    beta(K)=H=max(K-8,0).

All compulsory cleanup is funded internally from produced side identities;
no additional initial root, root pair or strict growth of ancestor root sets
is required. The undirected rank grows without any directed causal cycle.
This does NOT challenge the conditional bounded-beta theorem: beta here is
unbounded, and the model is not an actual chronological packet word.

## Omitted literal requirements

The model does not satisfy or claim the exact DC,V,D relative input/output
masks, one transported five-cell core, full RAW+marker white guards, the full
role-potential graph, or spatial endpoint continuity of a single head. Those
are precisely where a physical obstruction must enter. Assigning packet
counts, ages, current binary cells and full causal parents is not enough to
supply those omitted requirements.

This is an exact all-time relaxation limitation, not an infinite finite-seed
ant counterexample or a proof that a V helper can occupy the needed literal
pose. Independent review requested.
