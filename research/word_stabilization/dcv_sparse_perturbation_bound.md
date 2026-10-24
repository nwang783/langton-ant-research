# Sparse arbitrary perturbations of the DCV language

Status: independently SIGNED by analytic/arithmetic review, 2026-10-23 03:13 UTC, audit HZ. This is a robust duration bound, not a proof that the global K defect set is finite.

Let a finite actual ant turn factor, beginning with m black cells, be parsed as DCV macro blocks separated by arbitrary nonempty fine-turn strings. Let s be the total fine length of those exceptional strings. The exceptional strings need not belong to any fixed macro alphabet and may decrease black mass. Empty DCV blocks may be omitted, so there are at most s+1 DCV blocks and at most s internal bridges.

Define

G=193(s+1)+s=193+194s,
B=57+38(m+G)+3G+60s,
R=ceil(2B/5)+G+1,
t=floor(((2R+1)^2+G)/3).

Claim: the entire factor has duration at most

G+20R(t+s+1)+18t.

Consequently it has duration at most200(3383+16m+3400s)^3. This statement applies to every chosen parsing of an arbitrary actual ant factor. It does not assert that a useful parsing with small s always exists.

## Proof

Apply the signed arbitrary-DCV trimming lemma to every DCV block. Total discarded fine duration, including the arbitrary exceptions, is at mostG. If nothing is retained, the duration bound is immediate.

Otherwise anchor at the first retained recurrent-five factor. Entry mass m0 is at most m+G. Exactly as in the signed seven-word bridge-reset proof, all inactive initial identities lie in that entry board; at most m0 of them can activate at cost76. At each of at most s internal bridges of length g, reset surviving active black residual cells, including unread old core black cells outside the new core, to baseline60. The bridge costs at most6g+120 per rotated max potential, independently of its particular turn string or mass change. Cells entering the new core are charged only through the core term. No DCV198 transfer is used across a bridge.

The same four strips give the statedB at every retained part, and addingG+1 to the inverted strip radius covers every discarded read and endpoint. Hence all changed cells lie inside a square of at most(2R+1)^2 cells, independently of the initial seed diameter.

Let n be the number of C or V macros in the retained factors. Their total black-mass increment is at least3n, while discarded fine steps can decrease mass by at mostG. The total net mass increment is at most(2R+1)^2. Therefore3n<= (2R+1)^2+G and n<=t.

The retained factors together contain at most n+s+1 maximal D runs. Each run has at most2R D macros because its endpoints lie in the square and D advances by a fixed rotated(1,1). Each retained non-D macro has length at most18. Adding the discarded length proves the first bound.

For the optional simplified constant, R<=3383+16m+3400s, G<=R and s<=R. Since R>=1,

t <= (4R^2+5R+1)/3 <= (10/3)R^2.

Thus G+20R(t+s+1)+18t <= (200/3)R^3+80R^2+21R <200R^3. This proves the stated conservative cubic expression.

For a fixed finite starting mass m, every parsing of lengthT therefore has

s >= ((T/200)^(1/3)-3383-16m)/3400.

The lower bound is vacuous when its right side is negative. It measures fine-step distance from concatenated DCV blocks, not the previously defined global adjacent-bad-window count K; no equivalence between those two counts is assumed here.

Independent signoff: audit HZ and the signed bridge-reset literal constants. The distinct parsing scope and absence of a global-K equivalence are part of the signoff.
