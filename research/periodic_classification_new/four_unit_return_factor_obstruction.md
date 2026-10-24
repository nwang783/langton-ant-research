# Four consecutive unit-face returns are impossible on any ant board

23 October 2026, 08:41 UTC. Complete local certificate, audit pending.
This is a finite word-FACTOR theorem on arbitrary input, not a finite
period search or a claim that three such returns are impossible.

No ordinary Langton trajectory can first be at one physical cell, return
to it after four steps, then again after four, then again after four, and
then again after four. Thus four successive four-step physical returns to
the SAME cell are forbidden, on every finite or infinite input board.
Three such returns ARE possible on prepared boards.

A four-step physical return follows one unit-face boundary. Its three
noncentral turns all have a common orientation q in{R,L}. The turn at the
common cell alternates from one loop to the next. After fixing its initial
incoming heading by a genuine rotation, four loops have exactly
2*2^4=32 possible literal turn words: two initial central turns, four
loop orientations. This enumeration is complete, not a word-length cutoff.

For each case, certify_four_unit_returns.py reconstructs all sixteen actual
read positions and headings and exhibits two CONSECUTIVE reads of one
physical cell requiring the same turn. A cell flips at each read, so those
two turns must instead be opposite. Every case therefore fails on EVERY
possible initial coloring. frozen four_unit_returns.certificate.json lists
all32 literal contradictions, not a solver UNSAT result.

The same enumeration for three loops has four consistent prepared words
and supplies their exact finite minimum black inputs. For instance
RRRRLLLLRLLL is consistent. This guards against the tempting but false
stronger assertion excluding three loops.

## Stronger coupled visit/drift period bound

Let an actual translating ant trajectory have full drift d, D=||d||infinity
>=3, periodP, and complete multiplicity n>=5 at one full-drift class. The
already reviewed quotient packing bound gives P>=4(n-1)+2D. Equality would
force exactly one nonzero-winding class gap, of displacement d and length
2D, and all other n-1 gaps to be four-step zero-displacement returns.
Indeed D>2 makes any additional nonzero-winding gap strictly costly, and
any longer zero gap is also strictly costly.

Those n-1>=4 zero gaps are consecutive around the class cycle after
removing its sole winding gap. They are four or more consecutive unit
returns to one PHYSICAL cell, which the factor theorem forbids. Thus
packing equality is impossible. Both P and4(n-1)+2D have the same residue
modulo4 (heading/axis parity), so the strengthened necessary bound is

    P >= 4n+2D.                                  (1)

This is an all-cap lower bound, not an all-cap front exclusion. From signed
KR, fullaxis4 requires n>=6, hence P>=32. KS full(5,±1) requires n>=5,
henceP>=30. KW full(4,4), and the signed full(4,±2) cases, require P>=28.
The D3 cap4-excluded odd-odd cases requireP>=26. The D2 diagonal-two
case is deliberately excluded from this strengthening; its reviewedP>=28
bound remains valid from the basic packing lemma.
