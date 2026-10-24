# C-free spatial separation and exact finite fuel

Status: independently audited by a separate literal-word/complex-coordinate
checker. The stronger certificate uses no prior marked-site freshness theorem.

## Theorem

Let W be a physically feasible nonempty word over U,V,Q,B. Every non-seam
first-L input of every macro is unread in the portion of W before that macro.
There are5 such inputs for U,2 for V,15 for Q, and18 for B. If W C is feasible,
the additional C's phase1 input(-1,0), in its entry frame, is also unread earlier
in W. All freshness is relative to the factor's entry cut, not earlier history.

The exact number of black cells required on the initially read footprint is

    4 + 5u + 2v + 15q + 18b.

Consequently every finite-support entry board realizing W has at least this
many black cells. For W C, the exact required number is one larger. Debris
outside the read footprint can of course add arbitrarily many black cells.

## Finite spatial-pair lemma

Normalize an earlier macro A to position(0,0), heading N. Record a later macro
B by its type, relative position(x,y), and relative heading h. Here A is one
of U,V,Q,B; B may also be a terminal C. Every macro strictly between them is
C-free. Hence h is N or S and x+y is divisible by4.

Consider all1010 types whose two literal read footprints overlap. A saved
family S of952 types is forbidden in every such feasible factor. The
certificate gives one of the following local reasons for each type.

1. Equal-read separation. There is a common physical cell at which the last
   read in A equals the first read in B. Enumerate EVERY possible intermediate
   macro whose footprint can read that cell, using all four types, both
   headings, and every literal read offset. Each such possible reader forms
   an S-type with A or with B.
2. Neighbor descent. Enumerate EVERY possible immediate successor X of A and
   immediate predecessor Y of B, retaining all locally feasible A X and Y B
   pairs. For every choice, at least one of(A,Y),(X,B),(X,Y) has a type in S.

All physically feasible gap1 and gap2 cases were excluded from S by complete
literal-word checks. These use arbitrary entry colors through the exact
consecutive-read alternation criterion, not a particular finite seed.

## All-length proof

If a forbidden S-pair occurs, select an occurrence of minimum positive macro
index gap. Gaps1 and2 are ruled out by the base checks. For an equal-read
certificate, every intervening macro reading the named cell would give a
strictly smaller forbidden pair, so there is no intervening read. The equal
last/first letters then violate the flip rule. For a neighbor certificate,
the actual successor and predecessor are distinct because the gap is at
least3. One of their three indicated pairs is forbidden and has strictly
smaller gap, again a contradiction. Cyclic dependencies inside S are harmless:
the descending quantity is an actual positive integer gap, not certificate
construction order. A terminal C remains terminal in every subpair using it.

## Freshness query and fuel

For each first-L site of a proposed later macro, enumerate all normalized
poses at which an earlier C-free footprint could read it. The certificate
excludes every such pose for all40 non-seam inputs, and all56 poses for the
terminal C input. Thus these sites are globally new within the factor and
pairwise distinct across its macros.

The four common seam first-L inputs are

    (0,0),(-1,-1),(0,-1),(1,0).

For every macro after the first, all four were read by the immediately
preceding macro. This is checked directly from the four endpoint footprints.
The first macro's seam inputs are new by definition. Every other first-L
input is one of the40 proved fresh sites. Exact consecutive-read feasibility
then gives the stated minimal black count. A following C adds just its one
proved fresh input; its other first-L inputs are the same four seam sites.

## Artifacts and independent validation

- spatial_pair_kernel_no_marks.py and spatial_pair_kernel_no_marks.json:
  discovery and the stable952-type certificate, comprising700 neighbor
  certificates and252 equal-read certificates.
- cfree_spatial_kernel_fresh_sites.json: the exact queried first-L sets.
- verify_cfree_spatial_fuel.py: seam and complete first-L accounting checks.
- ../audits/check_spatial_pair_no_marks_independent.py and
  ../audits/spatial_pair_no_marks_independent.json: independent replay rebuilt
  from literal words with complex coordinates, using none of the discovery
  rotation, trace, or feasibility helpers. It checks5855 neighbor options
  and14440 potential intermediate-reader options.

This theorem does NOT give freshness across a C block, exclude every
five-macro finite-support tail, or prove the global highway conjecture.
